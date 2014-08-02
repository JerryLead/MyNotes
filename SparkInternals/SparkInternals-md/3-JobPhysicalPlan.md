# Job 物理执行图

在第一章里我们初步介绍了 job 的 DAG 物理执行图，里面包含 stages 和 tasks。这一章主要解决的问题是：

给定 job 的逻辑执行图，如何生成物理执行图（也就是 stages 和 tasks）？

## 一个复杂 job 的逻辑执行图

![ComplexJob](figures/ComplexJob.pdf)

代码贴在本章最后。给定这样一个复杂数据依赖图，如何合理划分 stages，并确定 task 的类型和个数？

一个直观想法是前后关联的 RDD 组成一个 stage，每个箭头是一个 task。对于 2 个 RDD 聚合成一个 RDD 的情况，这三个 RDD 组成一个 stage。这样虽然可以解决问题，但显然效率不高。除了效率问题，这个想法还有一个更严重的问题：**大量中间数据需要存储**。对于 task 来说，其执行结果要么要存到磁盘，要么存到内存，或者两者皆有。如果每个箭头都是 task 的话，每个 RDD 里面的数据都需要存起来，占用空间可想而知。

仔细观察一下逻辑执行图会发现：在每个 RDD 中，每个 partition 是独立的，也就是说一个 RDD 内部的每个 partition 的数据依赖不会相互干扰。因此，一个大胆的想法是将整个流程图看成一个 stage，为 finalRDD 中的每个 partition 分配一个 task。图示如下：

![ComplexTask](figures/ComplexTask.pdf)

粗箭头组合成第一个 task，计算结束后将 CoGroupedRDD 中已经计算得到的第二个和第三个 partition 存起来。之后第二个 task（细实线）只需计算两步，第三个 task（细虚线）也只需要计算两步，最后得到结果。

这个想法由两个不靠谱的地方：
- 第一个 task 太大，碰到 ShuffleDependency 后，不得不计算 shuffle 之前 RDD 的所有 partition，而且都在这一个 task 里面计算。
- 需要设计精妙的算法来判断哪个 RDD 中的哪些 partition 需要 cache。而且 cache 会占用存储空间。

虽然这是个不靠谱的想法，但有一个可取之处：**pipeline 思想**。**数据用的时候再算，而且数据是流到要计算的位置的**。比如在第一个 task 中，从  FlatMappedValuesRDD 中的 partition 向前推，只计算要用的 RDD 及 partition。在第二个 task 中，从 CoGroupedRDD 到 FlatMappedValuesRDD 计算过程中，不需要存储 MappedValuesRDD 中 partition 的全部计算结果。更进一步，从下图的 record 粒度来讲，第一个 pattern 中先算 g(f(record1))，然后中间结果都可以丢掉，然后算 g(f(record2))，丢掉中间结果，最后算 g(f(record3))。对于第二个 pattern 中的 g，record1 进入 g 后，理论上可以丢掉（除非被手动 cache）。其他 pattern 同理。

![Dependency](figures/pipeline.pdf)

回到 stage 和 task 的划分问题，上面不靠谱想法的主要问题是碰到 ShuffleDependency 后无法进行 pipeline。那么只要在 ShuffleDependency 处断开，就只剩 NarrowDependency，而 NarrowDependency 可以进行 pipeline。划分图如下：

![ComplextStage](figures/ComplexJobStage.pdf)

所以划分算法就是：从后往前推，遇到 ShuffleDependency 就断开，遇到 NarrowDependency 就加入该 stage。每个 stage 里面 task 的数目由该 stage 最后一个 RDD 中的 partition 个数决定。

粗箭头表示 task。因为是从后往前推算，因此最后一个 stage 的 id 是 0，stage 1 和 stage 2 都是 stage 0 的 parent。如果 stage 最后要产生 result，那么该 stage 里面的 task 都是 ResultTask，否则是 ShuffleMapTask。之所以称为 ShuffleMapTask 是因为其计算结果需要 shuffle 到下一个 stage，本质上相当于 MapReduce 中的 mapper。ResultTask 相当于 MapReduce 中的 reducer（如果需要从 parent stage 那里 shuffle 数据），也相当于普通 mapper（如果该 stage 没有 parent stage）。

还有一个问题：算法中提到 NarrowDependency chain 可以 pipeline，可是这里的 ComplexJob 只展示了 OneToOneDependency 和 RangeDependency 的 pipeline，普通 NarrowDependency 如何 pipeline？

回想上一章里面 cartesian(otherRDD) 里面复杂的 NarrowDependency，图示如下：

![cartesian](figures/cartesian.pdf)

经过算法划分后结果如下：

![cartesian](figures/cartesianPipeline.pdf)

图中粗箭头展示了其中一个 ResultTask。由于该 stage 的 task 直接输出 result，所有 task 都是 ResultTask。这个图也说明不管是 1:1 还是 N:1 的 NarrowDependency，只要是 NarrowDependency chain，就可以进行 pipeline，生成的 task 个数该 stage 最后一个 RDD 的 partition 个数相同。

## 物理图的执行
生成了 stage 和 task 以后，下一个问题就是 task 如何执行来生成最后的 result？

回到 ComplexJob 的物理执行图，如果按照 MapReduce 的逻辑，从前到后执行，map() 产生中间数据 map outpus，然后经过 partition 后放到本地磁盘。再经过 shuffle-sort-aggregate 后生成 reduce inputs，最后 reduce() 执行得到 result。执行流程如下：

![MapReduce](figures/MapReduce.pdf)

整个执行流程没有问题，但不能直接套用在 Spark 的物理执行图上，因为 MapReduce 的流程图简单、固定，而且没有 pipeline。

回想 pipeline 的思想是**数据用的时候再算，而且数据是流到要计算的位置的**。Result 产生的地方的就是要计算的位置，要确定 “需要计算的数据”，我们可以从后往前推，需要哪个 partition 就计算哪个 partition，如果 partition 里面没有数据，就继续向前推，形成 computing chain。这样推的结果就是：需要首先计算出每个 stage 最左边的 RDD 中的某些 partition。

对于没有 parent stage 的 stage，该 stage 最左边的 RDD 是可以立即计算的，而且每计算出一个 record 后便可以流入 f 或 g（见前面图中的 patterns）。如果 f 中的 record 关系是 1:1 的，那么 f(record1) 计算结果可以立即顺着 computing chain 的反方向流入 g 中。如果 f 的 record 关系是 N:1，record1 进入 f() 后也可以被回收。总结一下，computing chain 从后到前建立，而实际计算出的数据从前到后流动，而且计算出的第一个 record 流动到不能再流动后，再计算下一个 record。这样，虽然是要计算 partition 中的 records，但并不是要所有 records 计算得到后再向后流动。

对于有 parent stage 的 stage，只要所有 parent stages 中最后的 RDD 中数据已经计算好，经过 shuffle 后，问题就又回到了计算 “没有 parent stage 的 stage”。

> 代码实现：每个 RDD 包含的 getDependency() 负责确立 RDD 的数据依赖，compute() 方法负责接收 parent RDD 或者 data block 流入的 records，进行计算，然后输出 records。经常可以在 RDD 中看到这样的代码`firstParent[T].iterator(split, context).map(f)`。firstParent 表示该 RDD 依赖的第一个 parent RDD，iterator() 表示 parentRDD 中的 records 是一个一个流入该 RDD 的，map(f) 表示每流入一个 recod 就对其进行 f(record) 操作，输出 record。为了统一接口，这段代码仍然返回一个 iterator，来迭代 map(f) 输出的 records。

## 生成 job
前面介绍了逻辑和物理执行图的生成原理，怎么触发执行图的生成？已经介绍了 task，那么 job 是什么？

下表列出了可以触发生成执行图生成典型 [action()](http://spark.apache.org/docs/latest/programming-guide.html#actions)，其中第二列是 processPartition，定义如何计算 partition 中的 records，得到 result。第三列是 resultHandler，定义如何计算从各个 partition 收集来的 result，得到最终结果。


| Action | finalRDD(records) => result | compute(results) |
|:---------| :-------|:-------|
| reduce(func) | (record1, record2) => result, (result, record i) => result | (result1, result 2) => result, (result, result i) => result
| collect() |Array[records] => result | Array[result] |
| count() | count(records) => result | sum(result) |
| foreach(f) | f(records) => result | Array[result] |
| take(n) | record (i<=n) => result | Array{result] |
| first() | record 1 => result | Array{result] |
| takeSample() | selected records => result | Array{result] |
| takeOrdered(n, [ordering]) | TopN(records) => result | TopN(results) |
| saveAsHadoopFile(path) | records => write(records) | null |
| countByKey() | (K, V) => Map(K, count(K)) | (Map, Map) => Map(K, count(K)) | 

用户的 driver 程序中一旦出现 action()，就会生成一个 job，比如 foreach() 会调用`sc.runJob(this, (iter: Iterator[T]) => iter.foreach(f))`，向 DAGScheduler 提交 job。如果 driver 程序后面还有 action()，那么其他 action() 也会生成 job 提交。所以，driver 有多少个 action()，就会生成多少个 job。这就是 Spark 称 driver 程序为 application（包含多个 job）而不是 job 的原因。

每一个 job 包含 n 个 stage，最后一个 stage 产生 result。比如，第一章的 GroupByTest 例子中存在两个 job，一共产生了两组 result。在提交 job 过程中，DAGScheduler 会首先划分 stage，然后先提交**无 parent stage 的 stage**，并在提交过程中确定该 stage 的 task 个数及类型，并提交具体的 task。无 parent stage 的 stage 提交完后，依赖该 stage 的 stage 才提交。


DAGScheduler 负责提交 job，将 

	eventProcessActor ! JobSubmitted(jobId, rdd, func2, partitions.toArray, allowLocal, callSite, waiter, properties)
 eventProcessActor 是 DAGScheduler new 出来的 DAGSchedulerEventProcessActor。实际上当 DAGScheduler 收到 job 后，仍然是调用其 
 
	dagScheduler.handleJobSubmitted(jobId, rdd, func, partitions, allowLocal, callSite, listener, properties)

来执行。
