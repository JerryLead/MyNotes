# Task生成

## Job
![deploy](../svgFigures/deploy.pdf)

从部署图中可以看到
- 整个集群分为 Master 节点和 Worker 节点，相当于 Hadoop 的 Master 和 Slave 节点。
- Master 节点上常驻 Master 守护进程，负责管理全部的 Worker 节点。
- Worker 节点上常驻 Worker 守护进程，与 Master 节点通信。
- Driver 官方解释是 “The process running the main() function of the application and creating the SparkContext”。其实就是用户自己写的 Spark 程序，比如 WordCount.scala。如果 Driver program 在 Master 上运行，比如在 Master 上运行
```
	./bin/run-example SparkPi 10
```
那么 SparkPi 就是 Master 上的 Driver。如果是 YARN 集群，那么 Dirver 可能被调度到 Worker 节点上运行（比如上图中的 Worker Node 2）。
		
- 每个 Worker 上存在一个或者多个 ExecutorBackend 进程。每个进程包含一个 Exectuor 对象，该对象持有一个线程池，每个线程可以执行一个 task。
- 在 Standalone 版本中，ExecutorBackend 被实例化成 CoarseGrainedExecutorBackend 进程。在我的集群中每个 Worker 只运行一个 CoarseGrainedExecutorBackend，没有发现如何配置多个 CoarseGrainedExecutorBackend 进程。
- Worker 通过持有 ExecutorRunner 对象来控制 CoarseGrainedExecutorBackend 的启停。

之后会写一章专门介绍如何配置各个角色的 CPU、内存限制等。了解了部署图之后，我们先探究 job 如何运行。

## Job 例子
假设我们在 Master 节点运行 Spark 自带的 examples 包中的 GroupByTest，命令是
```
	
```
具体代码如下

```scala
package org.apache.spark.examples

import java.util.Random

import org.apache.spark.{SparkConf, SparkContext}
import org.apache.spark.SparkContext._

/**
  * Usage: GroupByTest [numMappers] [numKVPairs] [KeySize] [numReducers]
  */
object GroupByTest {
  def main(args: Array[String]) {
    val sparkConf = new SparkConf().setAppName("GroupBy Test")
    var numMappers = if (args.length > 0) args(0).toInt else 2
    var numKVPairs = if (args.length > 1) args(1).toInt else 1000
    var valSize = if (args.length > 2) args(2).toInt else 1000
    var numReducers = if (args.length > 3) args(3).toInt else numMappers

    val sc = new SparkContext(sparkConf)

    val pairs1 = sc.parallelize(0 until numMappers, numMappers).flatMap { p =>
      val ranGen = new Random
      var arr1 = new Array[(Int, Array[Byte])](numKVPairs)
      for (i <- 0 until numKVPairs) {
        val byteArr = new Array[Byte](valSize)
        ranGen.nextBytes(byteArr)
        arr1(i) = (ranGen.nextInt(Int.MaxValue), byteArr)
      }
      arr1
    }.cache
    // Enforce that everything has been calculated and in cache
    pairs1.count

    println(pairs1.groupByKey(numReducers).count)

    sc.stop()
  }
}

```
分析一下job 的执行逻辑：

1. 初始化 SparkConf()
2. 初始化 numMappers 等参数
3. 初始化 SparkContext。这一步很重要，是要确立 driver 的地位，里面包含创建执行环境初始化 `SparkEnv.create()` 等。
4. 每个 mapper 创建一个 Array[(Int, Array[Byte])]，length 为 numKVPairs。每一个 Array[Byte] 的 length 为 valSize，Int 为随机生成的整数。arr1 的总大小为 `numKVPairs * (4 + valSize)`，所以 paris1 的总大小为 `numMappers * Size(arr1)`。
5. 每个 mapper 将产生的 arr1 数组 cache 到内存。
6. 然后执行一个 action 操作（count），来统计所有 mapper 中 arr1 的元素个数，执行结果是 `numMappers * numKVPairs`。这一步主要是为了将每个 mapper 产生的 arr1 cache 到内存。
7. 在已经被 cache 的 paris1 上执行 groupByKey 操作，groupByKey 产生的 reducer 个数为 numReducers。理论上，如果 hash(Key) 比较平均的话，每个 reducer 收到的 <Int, Array[Byte]> record 个数为 `numMappers * numKVPairs / numReducer`，大小为 `numMappers * numKVPairs * (4 + valSize) / numReducer`。
8. reducer 将收到的 <Int, Array[Byte]> records 中拥有相同 Int 的 records 聚在一起，得到 <Int, ArrayBuffer[Array[Byte], Array[Byte], ..., Array[Byte]]>。
9. 最后 count 将所有 reducer 中 <Int, ArrayBuffer[]> 的 record 个数进行加和，最后结果就是不同的 Int 总个数。

## Job 分解执行
根据上面的分析可知
- 用户程序 main() 初始化 SparkContex 以后成为 driver。
- parallelize() 产生最初的 RDD
- 在 RDD 上的 transformation 操作（如这里的 flatMap）在各个 worker 上执行
- Count 执行时，每个 partition 上的 count 执行结果被发送到 driver，然后在 driver 端进行最后的加和。
- groupByKey 引入了 reducer，groupByKey 操作在 reducer 上执行
- 最后的 count 与上一个 count 的执行方式类似。

## 研究路线
已经知道 job 的执行过程，我们想进一步探究这些执行细节，接下来主要探究下列问题：

1. 如何生成 task
2. task 是什么，分配到哪里，执行了什么操作
3. task 怎么处理中间数据，shuffle 过程是什么样的
4. driver 和 task 执行是怎么协作，分配计算逻辑，收集计算结果的
5. cache 是怎么做的

