# Spark Internals

Based on Spark-1.0  

## Authors
Version 0.1 - Lijie Xu - 2014年7月10日 


## Introduction
本文主要讨论 Apache Spark 的设计与实现，重点关注其内部架构，附带讨论与 Hadoop MapReduce 设计与实现的区别。请不要将此文档称之为“源码分析”，因为该文档不仅仅解读实现代码，还会讨论设计思想、性能、可靠性方面的问题。

本文档并不是面向 Spark 的普通用户，而是面向渴望对 Spark 内部设计与实现机制深入了解的 Geeks。

因为 Spark 社区很活跃，更新速度很快，本文档也会尽量保持同步，目前文档版本为 v0.1。

该文档目前由 [@JerryLead](http://weibo.com/jerrylead) 撰写，由于实验条件、经验、技术水平等限制，当前只讨论 standalone 版本中的核心功能，而不是全部功能。

## Contents
本文档首先讨论 job 如何执行，然后讨论与 job 执行相关的一些数据存储、通信、调度等内容。具体内容如下：

1. 基本架构
2. Job 与 task 的执行
3. 数据存储
4. Job 与 task 调度
5. 性能分析
6. 可靠性分析

## Worker
Worker持有的数据结构

```scala
val executors = new HashMap[String, ExecutorRunner]
val finishedExecutors = new HashMap[String, ExecutorRunner]
val drivers = new HashMap[String, DriverRunner]
val finishedDrivers = new HashMap[String, DriverRunner]
```

{ {{ val executors = new HashMap[String, ExecutorRunner] }} }
Worker中的一些metrics

```scala
cores: Int  // 启动worker的时候需要指定core的个数
memory: Int // 启动worker的时候需要执行memory的大小（MB）

var coresUsed = 0
var memoryUsed = 0
def coresFree: Int = cores - coresUsed
def memoryFree: Int = memory - memoryUsed
```
Worker的属性


Worker启动时要做的工作

- 建立工作目录，也就是 $SPARK_HOME/work/
- 向所有Master注册自己，告诉他们自己启动了

Worker与Master之间的Heartbeat只是workerId
`Worker` 收到LaunchExecutor的指令后，会
case LaunchExecutor(masterUrl, appId, execId, appDesc, cores\_, memory_) =>

![](figures/shuffle-write-graph.svg)


CoarseGrainedExecutorBackend (Actor)
在 standalone 模式下，CoarseGrainedExecutorBackend 作为默认的 ExecutorBackend启动，负责启动和管理 Executor。它的主要功能是：
接收 task、然后启动和管理 Executor。Executor 负责执行具体的 task
	与 driver 通信

CoarseGrainedExecutorBackend 由 ExecutorRunner 对象启动（使用 ProcessBuilder 直接调用其 main 函数），因此 CoarseGrainedExecutorBackend 以进程的方式存在，与 worker 进程并存于 slave 机器上。

与 Driver 通信：
向 driver 注册自己。在启动时，根据 driver 的 URL 查询到 driver actor 位置，然后向 driver 注册自己。注册信息包含 executorId, hostPort 和 cores。
定时向 driver 汇报 task 的执行状态。通过driver ! statusUpdate(taskId, taskState)
接收来自 driver 的注册成功或失败的反馈信息。成功是 RegisteredExecutor，失败是 RegisterExecutorFailed。如果收到注册成功信息，那么就 new 出来一个 Executor 对象 executor，用于执行具体的 task。
接收来自 driver 的 task 执行命令，LaunchTask(data)，data 存放 task 的序列化信息，如 taskId，taskFiles， taskJars， taskBytes（里面是什么）？。
另外，还接收 KillTask， StopExecutor 等指令。

执行具体的 task：
接收到 LaunchTask 命令后，交给 executor 执行具体的 task。

Executor：管理并执行具体的Task
Executor 开辟了一个线程池（newCachedThreadPool） 来执行具体的 task，一个 Executor 管理多个 task，并且为每个 task 分配一个线程执行。
LaunchTask => 将 task 包装成 TaskRunner 对象，然后放入线程池 threadPool中（线程池大小？）。
Executor 还负责监控、维护、管理每个 task ，比如 runningTasks 维护所有正在执行的 task，killTask 方法可以结束执行的 task。

TaskRunner 对象是 Runnable 的，主要的执行逻辑如下：
做一系列的初始化。设置环境变量，初始化 Context，打印”Running task ID“，向 ExecutorBackend 报告自己的状态已经是 RUNNING，初始化 task 开始时间，GC 时间等，清空 Accumulator 等。
得到可以执行的 task。将 task 反序列化出来，更新 task 依赖的 files 和 jars，生成 具体要执行的 attemptedTask。
执行 task。记录 task 开始时间，调用 task 的run()，记录 task 的结束时间。
将执行结果 result 的 valueBytes 进行序列化，并记录序列化的耗时。其中，ShuffleMapTask 的 result 是 MapStatus （主要记录该 task 输出的每个 partition 大小），ResultTask 的 result 是 func() 的真正的执行结果。
记录 task 的 metrics。包括反序列化 task 的耗时，task 运行时间，JVM GC 时间以及 result 的序列化时间。这些 metrics 都会在 Web UI 中展示。
Result 包装。将 task 的执行结果 result 中的 valuesBytes，accumulators 和 metrics 包装成 directResult: DirectTaskResult，并序列化，打印 log（"Serialized size of result for " + taskId + " is " + serializedDirectResult.limit）。
向 driver 发送 result。如果 result 大小超过了 message 大小（默认10 MB），那么将序列化后的 result 存放在 blockManger 中，以 MEMORY_AND_DIRK_SER 存储，并打印 log（"Storing result for " + taskId + " in local BlockManager”），将 blockId 送回到 driver。反之，直接将序列化的 result 通过 statusUpdate 送回到 driver。
清理。shuffleMemoryMap 存放了<threadId, 用于 shuffle 的 memory 大小?线程？>。将 task 对应的 threadId 清理掉，清理 runningTasks 中的自己。
Akka 有默认的 message 大小限制（spark.akka.frameSize，默认是10 MB），task 本身（经过序列化后）或者 task result 默认通过 message 在 driver 和 executor 之间传递。如果 task 的 result 超过这个大小限制，那么 executor 使用 block manager 将 result 送回到 driver。
Executor 里面会 initialize SparkEnv，里面会启动：
httpFileServer: HttpFileServer
mapOutputTracker: MapOutputTrackerMasterActor (or ref)
shuffleFetcher: BlockStoreShuffleFetcher
broadcastManager: BroadcastManager
blockManager: BlockManagerMasterActor (or ref)
blockManger.master: BlockManagerMaster
metricsSystem: MetricsSystem
Task：具体的数据处理任务
Executor 管理并运行多个 task。Task 里面包含具体的数据处理逻辑。Spark 里面有且仅有两种 task：ShuffleMapTask 和 ResultTask。Spark job 包含多个 stage，每个 stage 对应一组 task（每个 task 处理一个partition） 。最后产生结果的 stage 会被转换成 ResultTask，前面的 stage 被转换成 ShuffleMapTask。ResultTask 还负责将最后的 result 送回到 driver，ShuffleMapTask 还要将执行结果进行划分成多个 bucket。
Task 具体包含 task 依赖的 files，jars 的名字和位置，以及 stageId 和 partitionId。

ReduceTask 的输入：
stageId: Int => 对应哪个 stage
rdd: RDD[T] => 在哪个 RDD 上进行计算
func: (TaskContext, Iterator[T]) => U，要执行的函数，Iterator 意味着是 streaming 形式的。
partitionId: Int => 在 RDD 上的哪个 partition 上执行。
locs: Seq[TaskLocation] => task 到哪里运行，loc 是 host 或者 <host, executorID>。前者只指定了哪台机器，后者还指定了哪台机器上的哪个 executor。
outputId: Int => ？

ReduceTask 的处理逻辑：

处理数据

如果 task 有 Callbacks 方法，那么处理完数据后调用。该方法可以通过 TaskContext.addOnCompleteCallback 方法进行注册。比如，HadoopRDD 注册了一个 callback 方法来关闭 input stream。
返回 func 的计算结果 result。

序列化 ReduceTask 包含的信息：

stageId, rdd, fuc, partitionId, outputId, epoch, split

ShuffleMapTask 的名字是 (stageId, partitionId)

ShuffleMapTask 的输入：
stageId: Int => 对应哪个 stage
rdd: RDD[T] => 对应该 stage 中最后的 RDD
dep: ShuffleDependency => 记录 shuffle stage 的依赖关系
partitionId: Int => 在 RDD 上的哪个 partition 上执行。
locs: Seq[TaskLocation] => task 到哪里运行，loc 是 host 或者 <host, executorID>。前者只指定了哪台机器，后者还指定了哪台机器上的哪个 executor，方便 locality-aware 调度。

ShuffleMapTask 的处理逻辑：

处理数据

这里的 shuffle 类型是 ShuffleWriterGroup，一个 ShuffleMapTask 包含一个 ShuffleWriterGroup，一个 writer 对应一个 reducer。


ShuffleBlockManger:
shuffleFile 可以看做是 3 元组 <shuffleId, bucketId, fileId>。每个 shuffle stage 拥有唯一的 shuffleId，bucketId 对应 reduce id。fileId 对应具体的一组 file（file 个数与 reducer 个数一样），每个 task 持有一个 fileId，当 task 完成时，将 fileId 放回留给下一个 task 使用。
每个 bucket 在内存中有 spark.shuffle.file.buffer.kb 大小的 buffer，默认是 100KB。如果开启了 spark.shuffle.consolidateFiles，那么多个 bucket 共用一个 shuffleFile。默认是不开启 coslidateFiles 的，所以每个 bucket 会有一个 shuffleFile。
每一个 writer 的类型是 BlockObjectWriter，
ConsolidateFiles = true
这次的 Bucket 代表内存 buffer，默认大小为 100 KB，通过 spark.shuffle.file.buffer.kb 来配置。每一个 ShuffleBlock 被包装成 FileSegment。
记录 offset 的数据结构:
mapIdToIndex: HashMap<Int, Int>，假设 ShuffleMapTask-0，ShuffleMapTask-1 依次在 core 0 上执行，ShuffleMapTask-3，ShuffleMapTask-2 依次在 core 1 上执行。由于调度算法、时延等问题，task执行顺序与其 id 关系不大。reducer 的个数假设为 3，产生的 shuffle files 如上图。那么 mapIdIndex 内容如下，其中 index 严格递增。
假设每个 ShuffleMapTask 输出的 FileSegment (shuffleBlock) 的 bytes 如下：（上面的 shuffleFile 和下面的 shuffleFile 分属于不同的 ShuffleFileGroup。

因为每个 reducer 对应一个 shuffleFile 那么 blockOffsetsByReducer 中的内容就是

对于某一个 ShuffleFileGroup 来说，给定 mapId 和 reduceId，可以先通过 mapIdToIndex 获得对应的 index；通过 reducerId 获得该 shuffleFileGroup 中的 offsets 数组，然后通过 offsets[index] 获得具体的 offset，然后后面的 offsets[index + 1] - offsets[index] 就是该 FileSegment 的 bytes。
ConsolidateFiles = false

将 ShuffleBlock 和 ShuffleblockFile 统称为 FileSegment。
假设可以同时运行的 task 个数为 N(core)
可以看到当 ConsolidateFiles = true 时：
产生的 ShuffleFile 的总个数为 N(core) * N(reducer)
可以同时存在于内存的 buffer 的总个数为 N(core) * N(reducer)

可以看到当 ConsolidateFiles = false 时：
产生的 ShuffleFile（这里是 blockFile）的总个数为 N(ShuffleMapTask) * N(reducer)
可以同时存在于内存的 buffer 的总个数仍为 N(core) * N(reducer)，不同的是，这里的 buffer 没有重用，前面的 ShuffleMapTask 执行完后，buffer 被释放。

当某个 ShuffleMapTask 执行结束后会返回一个 result: MapStatus，这个 MapStatus 包含两部分：blockManagerId 和 compressedSizes 数组。数组中每个元素是该 ShuffleMapTask 输出的 FileSegment（也就是 ShuffleBlock/ShuffleBlockFile） 的大小。值得注意的是，每个 worker 节点都有自己的 BlockManager，在该 worker 节点上运行的 task 都可以获得该 BlockManager 的 Id，而该 BlockManager 持有这些 task 的 output 记录，比如 ShuffleFile 个数、位置、offsets 等。

ShuffleBlockManager 中的 def forMapTask(mapId: Int) 中的 mapId 有一定的误导性，实际上不是 shuffleMapTask 的 taskId，而是要处理的 partition 的 partitionId。TaskId 实际上是 stageId + partitionId。

BlockStoreShuffleFetcher：reducer 去读取 ShuffleMapTask 的结果
在 ShuffledRDD 的 compute() 中调用 fetch() 去获得要处理的数据，fetch() 相当于 MapReduce 中 reducer 的 shuffle 阶段。这里的 split.index 相当于 reduceId，因为每个 task 处理一个 partition (split)，ShuffledRDD 自身的 partition 个数在 ShuffleMapTask 运行时已经确定了（也就是 reduce 的个数）。


由于 compute() 在 task 中运行，因此这里的 SparkEnv 是 executor 的 SparkEnv。那么得到的 shuffleFetcher 是 BlockStoreShuffleFetcher。要获得所有 ShuffleMapTask outputs 中属于该 reducer 的数据（FileSegment），首先要知道 FileSegment 的 location（在那台 worker 上，也就是 BlockManagerId）和大小。
如何获取 reducer 所需的 FileSegment 信息呢？答案是到 driver 中的 MapOutputTrackerMaster 那里去取，因为当 ShuffleMapTask 完成时会将其  MapStatus（所在的 location 和 输出的每个 FileSegment 大小）发送到 driver。driver 将这些 MapStatus 信息存放到 MapOutputTrackerMaster 里面（通过 DAGScheduler）。取的过程如下：
经过这个 RPC 过程，BlockStoreShuffleFetcher 可以得到属于给定 (shuffleId, reduceId) 的 Array[FileSegment信息] （也就是Array[(BlockManagerId, Long)]）。如果用 ShuffleMapTask 中的图示来表示的话，Reducer 1 里面运行 ShuffleRDD.compute()，通过 fetch() 中的getServerStatuses(shuffleId, reduceId) 可以得到 两个 ShuffleBlockFile 1 和两个 ShuffleBlockFile 1’ 的位置和大小。但此时还不知道每个 FileSegment（也就是 ShuffleBlockFile）是来自哪个 ShuffleMapTask。
如何知道每个 FileSegment 的来源（也就是对应的 ShuffleMapTask 的 mapId）？
其实 Array[FileSegment信息] 的 index 就是该 FileSegment 的 mapId。因为 driver 的MapOutputTrackerMaster 在存储每个 ShuffleMapTask 的 MapStatus 的时候，会将该 MapStatus 放到 ShuffleMapTask mapId 对应的数组位置，如果简单化里面的一些数据结构。
mapStatuses: HashMap<shuffleId, Array[MapStatus]>
shuffleId 代表一个 stage，mapStatuses 存放这个 stage 里面所有的 ShuffleMapTask 的 output 信息。Array 的 index 代表 ShuffleMapTask 的 mapId（也就是该 task 处理的 partitionId）。也就是说 mapStatutes 保存了所有 ShuffleMapTask 的输出信息。
BlockStoreShuffleFetcher 从 mapStatues 获取了某个 stage（给定 shuffleId）里所有 ShuffleMapTask 的输出信息，再从这些信息中抽取出每个 ShuffleMapTask 输出的属于某个 reducer（给定 reduceId）的输出信息 Array[(blockManagerId, Long)]。
从网络流量来说，每次 executor 请求 mapStatuses 信息时，driver 会将该 stage 里所有的 ShuffleMapTask 的 output 信息送到 executor 中的 MapOutputTrackerWorker ，MapOutputTrackerWorker 会 cache 这些信息到 HashMap。这样下次其他 reducer 要请求 MapStatus 的时候，直接从本地读取，不需要 RPC 了。
得到 stage 里所有 ShuffleMapTask 的 Array[(blockManagerId, Long)] 后，对 blockManagerId 做 aggregation，并将 index 转换成 mapId，最后得到

这里的 BlockId 就是 mapId，代表这个 FileSegment (blockFile) 来自哪个 ShuffleMapTask（处理的 partitionId）。

要写的东西
BlockStoreShuffleFetcher => BlockFetcherIterator.initialize() => next() => aggregate [( BlockManagerId, Seq[(BlockId, Long)] )] => 切割 FetchRequest => sendRequest(limited by maxBytesInFlight) => receive(BlockMessage)
data skew 的问题，超越 maxBytesInFlight。sender 仍然要 buffer 数据，receiver 也要 buffer 数据。
NettyBlockFetcherIterator 也要看。
blockMessage.getData 要占内存，dataDeserialized 在反序列化的时候也要占内存。

BlockManager架构