# Shuflfe 过程

上一章里讨论了 job 的物理执行图，也讨论了流入 RDD 中的 records 是怎么被 compute() 后流到后续 RDD 的，同时也分析了 task 是怎么产生 result，以及 result 怎么被收集后计算出最终结果的。然而，我们还没有讨论数据怎么通过 ShuffleDependency 流向下一个 stage 的。

## 对比 Hadoop MapReduce 和 Spark 的 Shuflfe 过程
如果熟悉 Hadoop MapReduce 中的 shuffle 过程，可能会按照 MapReduce 的思路去想象 Spark 的 shuffle 过程。

从 high-level 的角度来看，两者并没有大的差别。都是将 mapper（Spark 里是 ShuffleMapTask）的输出进行 partition，不同的 partition 送到不同的  reducer（Spark 里 reducer 可能是下一个 stage 里的 ShuffleMapTask，也可能是 ResultTask）。Reducer 以内存作缓冲区，边 shuffle 边 aggregate 数据，等到数据 aggregate 好以后进行 reduce() （Spark 里可能是后续的一系列操作）。

从 low-level  的角度来看，两者差别也不小。Hadoop MapReduce 是 sort-based，进入 combine() 和 reduce() 的 records 必须先 sort。这样的好处在于 combine/reduce() 可以处理大规模的数据，因为其输入数据可以通过**外排**得到（mapper 对每段数据做排序，reducer 的 shuffle 对排好序的每段数据作归并）。目前的 Spark 是 hash-based，使用 HashMap 来对 shuffle 来的数据进行 aggregate，mapper 和 reducer 都不会对数据进行提前排序。如果用户需要经过排序的数据，那么需要自己调用类似 SortByKey() 的操作。

从实现角度来看，两者也有不少差别。Hadoop MapReduce 将处理流程划分出明显的几个阶段：map(), spill, merge, shuffle, sort, reduce() 等。每个阶段各司其职，可以按照过程式的编程思想来逐一实现每个阶段的功能。在 Spark 中，没有这样功能明确的阶段，只有不同的 stage，及每个 stage 里面是什么类型的 task。

如果我们将 map 端划分数据，持久化数据的过程称为 shuffle write，而将 reducer 读入数据，aggregate 数据的过称为 shuffle read。那么，在 Spark 中，问题就变为怎么在 job 的逻辑或者物理执行图中加入 shuffle write 和 shuffle read 的处理逻辑？以及两个处理逻辑应该怎么高效实现？

## Shufle write

由于不要求数据有序，shuffle write 的任务很简单：将数据 partition 好，并持久化。之所以要持久化，一方面是较少内存存储空间压力，另一方面也是为了 fault-tolerant。

任务很简单，那么实现也很简单：将 shuffle write 的处理逻辑加入到 ShuffleMapStage 的最后，该 stage 最后一个 RDD 每输出一个 record 就将其 partition 后持久化。图示如下：

![shuffle-write-no-consolidation](figures/shuffle-write-no-consolidation.pdf)

上图假设有 4 个 ShuffleMapTask 要在一个 worker node 上运行，CPU core 数为 2，可以同时运行两个 task。每个 task 的执行结果（该 stage 的 finalRDD 中某个 partition 包含的 records）被逐一写到本地磁盘上。每个 task 包含 N 个缓冲区，N = reducer 个数（也就是下一个 stage 中 task 的个数），缓冲区被称为 bucket，其大小为`spark.shuffle.file.buffer.kb` ，默认是 100KB。

所以 ShuffleMapTask 的执行过程很简单，先 pipeline 计算得到 finalRDD 中对应 partition 的 records。每得到一个 record 就将其送到对应的 bucket 里，具体是哪个 bucket 由 partitioner.partition(record.getKey())) 决定。每个 bucket 里面的数据会不断被写到本地磁盘上，形成一个 ShuffleBlockFile，或者简称 FileSegment。之后的 reducer 会去 fetch 属于自己的 FileSegment，进入 shuffle read 阶段。

这样的实现很简单，但有几个问题：

1. 产生的 FileSegment 过多。每个 ShuffleMapTask 产生 R（reducer 个数）个 FileSegment，M 个 ShuffleMapTask 就会产生 M * R 个文件。一般 Spark job 的 M 和 R 都很大，因此磁盘上会存在大量的数据文件。
2. 缓冲区占用内存空间大。每个  ShuffleMapTask 需要开 R 个 bucket，M 个 ShuffleMapTask 就会产生 M * R 个 bucket。虽然一个 ShuffleMapTask 结束后，对应的缓冲区可以被回收，但一个 worker node 上同时存在的 bucket 个数可以达到 cores * R 个（一般 worker 同时可以运行 cores 个 ShuffleMapTask），占用的内存空间也就达到了`cores * R * 100KB`。对于 8 核 1000 个 reducer 来说，占用内存就是 800MB。

目前来看，第二个问题还没有好的方法解决，因为写磁盘终究是要开缓冲区的，缓冲区太小会影响 IO 速度。但第一个问题有一些方法去解决，下面介绍没有被默认开启的 FileConsolidation 方法。先上图：

![shuffle-write-consolidation](figures/shuffle-write-consolidation.pdf)

可以明显看出，在一个 core 上连续执行的 ShuffleMapTask 可以共用一个输出文件 ShuffleFile。先执行完的 ShuffleMapTask 形成 ShuffleBlock i，后执行的 ShuffleMapTask 可以将输出数据直接追加到 ShuffleBlock i 后面，形成 ShuffleBlock i'，每个 ShuffleBlock 被称为 FileSegment。下一个 stage 的 reducer 只需要 fetch 整个 ShuffleFile 就行了。这样，每个 worker 持有的文件数降为 cores * R。FileConsolidation 功能可以通过`spark.shuffle.consolidateFiles=true`来开启。

## Shufle read
先看一张存在 ShuffleDependency 的物理执行图，来自 reduceByKey：

![reduceByKey](figures/reduceByKeyStage.pdf)

很自然地，要计算 ShuffleRDD 中的数据，必须先把 MapPartitionsRDD 中的数据 fetch 过来。那么问题就来了：

- 在什么时候 fetch，一个 ShuffleMapTask 执行完还是全部 ShuffleMapTask 执行完？
- 边 fetch 边处理还是一次性 fetch 完再处理？
- fetch 来的数据存放到哪里？
- 怎么获得要 fetch 的数据的存放位置？

 
解决问题：
- 当 parent stage 的所有 ShuffleMapTasks 结束后再 fetch。理论上一个 ShuffleMapTask 结束后就可以 fetch，但是为了迎合 stage 的概念（即一个 stage 如果其 parent stages 没有执行完，自己是不能被提交执行的），还是选择全部 ShuffleMapTask 执行完再 shuffle。
- 边 fetch 边处理。本质上，MapReduce shuffle 阶段就是边 fetch 边使用 combine() 进行处理，只是 combine() 处理的是部分数据。MapReduce 为了让进入 reduce() 的 records 有序，必须等到全部数据都 shuffle-sort 后再开始 reduce()。因为 Spark 不要求 shuffle 后的数据全局有序，因此没有必要全部数据 shuffle 完成后再处理。那么如何实现边 shuffle 边处理，而且流入的 records 是无序的？答案是使用 HashMap。每 shuffle 得到一个 \<Key, Value\> record，直接将其放进 HashMap 里面。如果该 HashMap 已经存在相应的 Key，那么直接进行 `func(hashMap.get(Key), Value)`。这个 func 功能上相当于 reduce()，但实际处理数据的方式与 MapReduce reduce() 有差别，差别相当于下面两段程序的差别。

	```java
	// MapReduce
	reduce(K key, Iterable<V> values) { 
		result = process(key, values)
		return result		}

	// Spark
	reduce(K key, Iterable<V> values) {
		result = null 
		for (V value : values) 
			result  = func(result, value)
		return result	}
	```
MapReduce 可以在 process 函数里面可以定义任何数据结构，也可以将所有的 values 都 cache 后再进行处理，非常灵活。而 Spark 中的 func 的输入参数是固定的，一个是上一个 record 的处理结果，一个是当前读入的 record，他们经过 func 处理后的结果被下一个 record 处理时用。因此一些算法比如求平均数，在 process 里面很好实现，直接`sum(values)/values.length`，而在 Spark 中 func 可以实现`sum(values)`，但不没法去`/values.length`。
- 

 
 
