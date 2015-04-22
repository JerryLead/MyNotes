## Issues that contain "Out of Memory" or "OOM" or "OutOfMemory" in Spark user mailing list

1. [Re: Out of memory on large RDDs](http://apache-spark-user-list.1001560.n3.nabble.com/Re-Out-of-memory-on-large-RDDs-tp2533.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code: Yes

2. [Running out of memory Naive Bayes](http://apache-spark-user-list.1001560.n3.nabble.com/Running-out-of-memory-Naive-Bayes-tp4866.html)

	Root cause: Too many features stored in the driver  
	Pattern: Unknown  
	Reproducible: No  

	Even the features are sparse, the conditional probabilities are stored 
in a dense matrix. With 200 labels and 2 million features, you need to 
store at least 4e8 doubles on the driver node. With multiple 
partitions, you may need more memory on the driver. Could you try 
reducing the number of partitions and giving driver more ram and see 
whether it can help

3. [Kafka streaming out of memory](http://apache-spark-user-list.1001560.n3.nabble.com/Kafka-streaming-out-of-memory-tp2639.html)
	
	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	
4. [Serializer or Out-of-Memory issues?](http://apache-spark-user-list.1001560.n3.nabble.com/Serializer-or-Out-of-Memory-issues-tp8533.html)
	
	Occuring phase: reduceByKey()  
	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  

5. [OUT OF MEMORY ERROR: HEAP SPACE](http://apache-spark-user-list.1001560.n3.nabble.com/OUT-OF-MEMORY-ERROR-HEAP-SPACE-tp8698.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : Yes
	
6. [Out of Memory - Spark Job server](http://apache-spark-user-list.1001560.n3.nabble.com/Out-of-Memory-Spark-Job-server-tp12852.html)


	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
7. [Driver fail with out of memory exception](http://apache-spark-user-list.1001560.n3.nabble.com/Driver-fail-with-out-of-memory-exception-tp14188.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
8. [Running out of memory on livejournal](http://apache-spark-user-list.1001560.n3.nabble.com/Running-out-of-memory-on-livejournal-tp18890.html)

	Occuring phase: GropuLoader + graph.pageRank()
	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : Yes
	
9. [MLlib Logistic Regression run out of memory](http://apache-spark-user-list.1001560.n3.nabble.com/MLlib-Logistic-Regression-run-out-of-memory-tp22210.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
10. [Executor out of memory and gets killed](http://apache-spark-user-list.1001560.n3.nabble.com/Executor-out-of-memory-and-gets-killed-tp22419.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
11. [out of memory errors -- per core memory limits?](http://apache-spark-user-list.1001560.n3.nabble.com/out-of-memory-errors-per-core-memory-limits-tp12565.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

12. [help me: Out of memory when spark streaming](http://apache-spark-user-list.1001560.n3.nabble.com/help-me-Out-of-memory-when-spark-streaming-tp5854.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
13. [Out of memory exception in MLlib's naive baye's classification training](http://apache-spark-user-list.1001560.n3.nabble.com/Out-of-memory-exception-in-MLlib-s-naive-baye-s-classification-training-tp14809.html)

	Occuring phase: combineByKey() or collect()
	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
14. [Meaning of persistence levels -- setting persistence causing out of memory errors with pyspark](http://apache-spark-user-list.1001560.n3.nabble.com/Meaning-of-persistence-levels-setting-persistence-causing-out-of-memory-errors-with-pyspark-tp17412.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
15. [Spark SQL 1.1.0 - large insert into parquet runs out of memory](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-SQL-1-1-0-large-insert-into-parquet-runs-out-of-memory-tp14924.html)


	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
16. [Common crawl parsing has high fan out and runs out of memory](http://apache-spark-user-list.1001560.n3.nabble.com/Common-crawl-parsing-has-high-fan-out-and-runs-out-of-memory-tp21708.html) (*)


	Root cause: ArrayList in Java flatMap()  
	Pattern: Large accumulated results  
	Reproducible: Yes (large flatMap())  
	Source code : No
	
	The code works, but it requires almost 12G of memory per ParseWarc.call, because even though I know how to read one record a time from the gzip, and I can output one record a time, the flatMap api requires that the whole Iterable is created in memory before being returned. 
	
17. [Long running time for GraphX pagerank in dataset com-Friendster](http://apache-spark-user-list.1001560.n3.nabble.com/Long-running-time-for-GraphX-pagerank-in-dataset-com-Friendster-tp4511.html)


	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
18. [distinct on huge dataset](http://apache-spark-user-list.1001560.n3.nabble.com/distinct-on-huge-dataset-tp3025.html)


	Root cause: Distinct() on large dataset  
	Pattern: Improper data partition   
	Reproducible: Yes
	
19. [Lost executors](http://apache-spark-user-list.1001560.n3.nabble.com/Lost-executors-tp11722.html)


	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
20. [Any issues with repartition?](http://apache-spark-user-list.1001560.n3.nabble.com/Any-issues-with-repartition-tp13462.html)


	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
21. [Partitioning - optimization or requirement?](http://apache-spark-user-list.1001560.n3.nabble.com/Partitioning-optimization-or-requirement-tp3359.html)

	Root cause: Hotspot key (doing unbalanced joins (ie. cardinality of some joined elements much larger than others)  
	Pattern: Hotspot key
	Reproducible: No  
	Source code : No
	
22. [tiers of caching](http://apache-spark-user-list.1001560.n3.nabble.com/tiers-of-caching-tp8927.html)

	Root cause: (graphx liberally cache RDDs for efficiency, which makes sense. however it can also leave a long trail of unused yet cached RDDs, that might push other RDDs out of memory.)    
	Pattern: Too many rdds cached in memory  
	Reproducible: No   
	Source code : No
	
23. [Buffering for Socket streams](http://apache-spark-user-list.1001560.n3.nabble.com/Buffering-for-Socket-streams-tp22164.html)

	Root cause: (writing large files to HDFS via Socket streamer)  
	Pattern: Unknown
	Reproducible: No  
	Source code : No
	
24. [configuration needed to run twitter(25GB) dataset](http://apache-spark-user-list.1001560.n3.nabble.com/configuration-needed-to-run-twitter-25GB-dataset-tp11044.html)
	
	Occuring phase: GraphX iteration large graph.  
	Root cause: Unknown  
	Pattern: Unknown
	Reproducible: No  
	Source code : No
	
25. [how to debug ExecutorLostFailure](http://apache-spark-user-list.1001560.n3.nabble.com/how-to-debug-ExecutorLostFailure-tp15646.html)

	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
29. [OutOfMemory of spark streaming on standalone in 5 minutes, but run normal on local mode](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-of-spark-streaming-on-standalone-in-5-minutes-but-run-normal-on-local-mode-tp21352.html)

	Root cause: Input data => socketTextStream => store data onto HDFS  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
30. [Spark streaming](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-streaming-tp22255.html)

	Root cause: Unknown
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

31. [How to join two PairRDD together?](http://apache-spark-user-list.1001560.n3.nabble.com/How-to-join-two-PairRDD-together-tp12729.html)

	Symptom: adding the same key to every element, and joining  
	Root cause: Unknown
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

35. [[SQL] Set Parquet block size?](http://apache-spark-user-list.1001560.n3.nabble.com/SQL-Set-Parquet-block-size-tp16039.html)

	Symptom: Out of Memory issues when writing parquet files. The rdd we are saving to parquet have a fairly high number of columns (in the thousands, around 3k for the moment).   
	Root cause: Unknown
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
37. [trouble with broadcast variables on pyspark](http://apache-spark-user-list.1001560.n3.nabble.com/trouble-with-broadcast-variables-on-pyspark-tp1301.html)

	Symptom: A ~1GB array seems to be blowing up beyond the size of the driver machine's memory when it's pickled. I've tried to get around this by broadcasting smaller chunks of it one at a time.   
	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

44. [spark streaming rate limiting from kafka](http://apache-spark-user-list.1001560.n3.nabble.com/spark-streaming-rate-limiting-from-kafka-tp8590.html)

	Symptom: accumulate a lot on kafka topic-partitions.   
	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
45. [RDD join: composite keys](http://apache-spark-user-list.1001560.n3.nabble.com/RDD-join-composite-keys-tp8696.html)

	Symptom: accumulate a lot on kafka topic-partitions.   
	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
46. [AppMaster OOME on YARN](http://apache-spark-user-list.1001560.n3.nabble.com/AppMaster-OOME-on-YARN-tp12612.html)
	
	Symptom: groupBy() .mapValues().fold()   
	Root cause: Unknown  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	

48. [Yarn Driver OOME (Java heap space) when executors request map output locations](http://apache-spark-user-list.1001560.n3.nabble.com/Yarn-Driver-OOME-Java-heap-space-when-executors-request-map-output-locations-tp13827.html)
	
	Symptom: the driver appears to be making 500 (5gb of data) copies of this data to send out and running out of memory.  
	Root cause: Dirver generates large dataset  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
49. [MLLib ALS question](http://apache-spark-user-list.1001560.n3.nabble.com/MLLib-ALS-question-tp15420.html) (Further study)

	Symptom: The current ALS 
implementation constructs all subproblems in memory. With rank=10, 
that means (6.5M + 2.5M) * 10^2 / 2 * 8 bytes = 3.5GB. The ratings 
need 2GB, not counting the overhead.   ALS still needs to load and deserialize the in/out blocks (one by one) 
from disk and then construct least squares subproblems. All happen in 
RAM. The final model is also stored in memory.  
	Root cause: Large data loaded into memory, intermediate computing results. 
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
50. [Accumulator question](http://apache-spark-user-list.1001560.n3.nabble.com/Accumulator-question-tp15715.html) (Further study)

	Symptom: we're gathering data from repeated queries using some relatively sizable accumulators; at the moment, we're creating one per query, and running out of memory after far too few queries.
	Root cause: Large accumulated results in Accumulators.  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
51. [Lag function equivalent in an RDD](http://apache-spark-user-list.1001560.n3.nabble.com/Lag-function-equivalent-in-an-RDD-tp16448.html)

	Symptom: I have tried reduceByKey and then splitting the List of position in 
tuples.   
	Root cause: Hotspot key, one vehicle has a huge amount of data that could fail. 
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

53. [JVM Memory Woes](http://apache-spark-user-list.1001560.n3.nabble.com/JVM-Memory-Woes-tp19496.html)
	
	Symptom: It is a filter job that creates the error above, not the reduceByKey.  	Root cause: probably reduceByKey(), although authors claim the causes exist in filter()  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No


56. [Memory allocation in the driver](http://apache-spark-user-list.1001560.n3.nabble.com/Memory-allocation-in-the-driver-tp8406.html)

	
	Symptom: call to "b.first" will cause the spark driver to allocate a VERY large piece of memory. The first item of the first partition is very small (less than 200 bytes). However, the size of the entire first partition was about 380 MB.  
	Root cause: large data collected() by driver, although each partition is small.
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
57. [GC issues](http://apache-spark-user-list.1001560.n3.nabble.com/GC-issues-tp1422.html)
	
	Symptom: OOM  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	

59. [Spark limitations question](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-limitations-question-tp3296.html) (Further study)

	Symptom:  join Base to Skewed, works well on all but one of the nodes on the cluster 
	Pattern: Skewed data  
	Reproducible: No  
	Source code : No

60. [Kyro serialization slow and runs OOM](http://apache-spark-user-list.1001560.n3.nabble.com/Kyro-serialization-slow-and-runs-OOM-tp1073.html)

	
	Symptom: I load my dataset, transform it with some one to one transformations, and try to cache the eventual RDD - it runs really slow and then runs out of memory.   
	Pattern: Large data cached  
	Reproducible: No  
	Source code : No

65. [Pyspark Memory Woes](http://apache-spark-user-list.1001560.n3.nabble.com/Pyspark-Memory-Woes-tp2538.html)

	Symptom: Discussion    
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
66. [Doubts regarding Shark](http://apache-spark-user-list.1001560.n3.nabble.com/Doubts-regarding-Shark-tp5756.html)

	Symptom: Discussion    
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
67. [advice on maintaining a production spark cluster?](http://apache-spark-user-list.1001560.n3.nabble.com/advice-on-maintaining-a-production-spark-cluster-tp5848.html)

	Symptom: Running out of memory on the driver side (esp. with large broadcast variables)   
	Pattern: Driver is going to broadcast large dataset  
	Reproducible: No  
	Source code : No

69. [pyspark join crash](http://apache-spark-user-list.1001560.n3.nabble.com/pyspark-join-crash-tp6938.html)

	I think the problem is that once unpacked in Python, the objects take considerably more space, as they are stored as Python objects in a Python dictionary. Take a look at python/pyspark/join.py and combineByKey in python/pyspark/rdd.py. We should probably try to store these in serialized form.
	
72. ["Spilling in-memory..." messages in log even with MEMORY_ONLY](http://apache-spark-user-list.1001560.n3.nabble.com/Spilling-in-memory-messages-in-log-even-with-MEMORY-ONLY-tp10723.html)

	These messages are actually not about spilling the RDD, they're about spilling intermediate state in a reduceByKey, groupBy or other operation whose state doesn't fit in memory. We have to do that in these cases to avoid going out of memory. You can minimize spilling by having more reduce tasks though, which will mean less data per task. 
	
73. [Understanding RDD.GroupBy OutOfMemory Exceptions](http://apache-spark-user-list.1001560.n3.nabble.com/Understanding-RDD-GroupBy-OutOfMemory-Exceptions-tp11427.html) (Further study, groupByKey())
	
	Symptom: OOM in groupByKey() but no error in reduceByKey()
	Pattern:  large input record, 
	Reproducible: No  
	Source code : No
	
	The groupBy operator in Spark is not an aggregation operator (e.g. in SQL where you do select sum(salary) group by age...) - there are separate more efficient operators for aggregations. Currently groupBy requires that all of the values for one key can fit in memory. In your case, it's possible you have a single key with a very large number of values, given that your count seems to be failing on a single task.

75. [Question regarding spark data partition and coalesce. Need info on my use case.](http://apache-spark-user-list.1001560.n3.nabble.com/Question-regarding-spark-data-partition-and-coalesce-Need-info-on-my-use-case-tp12214.html)

		
	Symptom: Without using coalesce() or repartition() on the input data spark executes really slow and fails with out of memory exception.  
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
76. [pyspark/yarn and inconsistent number of executors](http://apache-spark-user-list.1001560.n3.nabble.com/pyspark-yarn-and-inconsistent-number-of-executors-tp12406.html)

	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
77. [Bulk-load to HBase](http://apache-spark-user-list.1001560.n3.nabble.com/Bulk-load-to-HBase-tp14667.html) (Further study)

	Symptom: OOM on mapPartitionsWithIndex() for splitKeys, I have to merge the byte[]s that have the same key. 
	Pattern:  Large accumulated results
	Reproducible: No  
	Source code : No
	
	
	The problem is that you will first collect and allocate many small byte[] in memory, and then merge them. If the total size of the byte[]s is very large, you run out of memory, 

78. [Setup an huge Unserializable Object in a mapper](http://apache-spark-user-list.1001560.n3.nabble.com/Setup-an-huge-Unserializable-Object-in-a-mapper-tp14817.html) (Further study)
			
	Symptom: getTree function in each iterator of map()  
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
79. [driver memory management](http://apache-spark-user-list.1001560.n3.nabble.com/driver-memory-management-tp15305.html)

	Symptom: driver OOM  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
81. [something about rdd.collect](http://apache-spark-user-list.1001560.n3.nabble.com/something-about-rdd-collect-tp16451.html)

	Symptom: driver OOM  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
83. [MLLib /ALS : java.lang.OutOfMemoryError: Java heap space](http://apache-spark-user-list.1001560.n3.nabble.com/MLLib-ALS-java-lang-OutOfMemoryError-Java-heap-space-tp20584.html)
	
	Symptom: shuffle buffer + storage buffer > limit 
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No

89. [Spark Processing Large Data Stuck](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-Processing-Large-Data-Stuck-tp8075.html)
		
	Symptom: Java.deserialization.buffer + ExeternalAppendOnlyMap  
	Pattern:  Large buffer
	Reproducible: No  
	Source code : No

	
90. [memory leak query](http://apache-spark-user-list.1001560.n3.nabble.com/memory-leak-query-tp8961.html)
			
	Symptom: Loop of rdd.count()  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No


96. [OOM with groupBy + saveAsTextFile](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-with-groupBy-saveAsTextFile-tp17891.html) (Further study)
			
	Symptom: GroupBy + saveAsTextFile, The value after groupBy() is too large  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No

	
97. [trouble with "join" on large RDDs](http://apache-spark-user-list.1001560.n3.nabble.com/trouble-with-join-on-large-RDDs-tp3864.html)

	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
98. [What should happen if we try to cache more data than the cluster can hold in memory?](http://apache-spark-user-list.1001560.n3.nabble.com/What-should-happen-if-we-try-to-cache-more-data-than-the-cluster-can-hold-in-memory-tp11175.html)
	
	Symptom: Individual partitions were too big to fit in memory.  
	Pattern:  Improper data partition
	Reproducible: No  
	Source code : No

99. [Spark app throwing java.lang.OutOfMemoryError: GC overhead limit exceeded](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-app-throwing-java-lang-OutOfMemoryError-GC-overhead-limit-exceeded-tp11350.html)

	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
101. [java.lang.OutOfMemoryError: Requested array size exceeds VM limit](http://apache-spark-user-list.1001560.n3.nabble.com/java-lang-OutOfMemoryError-Requested-array-size-exceeds-VM-limit-tp12993.html)

	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
102. [processing large number of files](http://apache-spark-user-list.1001560.n3.nabble.com/processing-large-number-of-files-tp15429.html)
	
	Symptom: large array/model in the driver 
	Pattern:  Large data generated in the driver
	Reproducible: No  
	Source code : No
	
103. [RowMatrix PCA out of heap space error](http://apache-spark-user-list.1001560.n3.nabble.com/RowMatrix-PCA-out-of-heap-space-error-tp16305.html)

	
	Pattern:  Large matrix in the driver 
	Reproducible: No  
	Source code : No
	
105. [Problems with broadcast large datastructure](http://apache-spark-user-list.1001560.n3.nabble.com/Problems-with-broadcast-large-datastructure-tp331.html)

	Symptom: Broadcast large data
	Pattern:  Large data cached in memory
	Reproducible: No  
	Source code : No
	
106. [OOM - Help Optimizing Local Job](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-Help-Optimizing-Local-Job-tp643.html) (Further study)
	
	Symptom: combineValuesByKey()
	Pattern:  Large data cached in memory
	Reproducible: No  
	Source code : No
	
107. [Spark streaming questions](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-streaming-questions-tp1494.html) (Further study)

	Symptom: DStream.persist() constantly  
	Pattern:  Large data cached in memory
	Reproducible: No  
	Source code : No
	
108. [shuffle memory requirements](http://apache-spark-user-list.1001560.n3.nabble.com/shuffle-memory-requirements-tp4048.html)

	Symptom: partitionBy()
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	

111. [OutofMemoryError when generating output](http://apache-spark-user-list.1001560.n3.nabble.com/OutofMemoryError-when-generating-output-tp12847.html)

	Symptom: distinct().countByKey()  
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	

113. [Getting java.lang.OutOfMemoryError when calling mkString on a parition](http://apache-spark-user-list.1001560.n3.nabble.com/Getting-java-lang-OutOfMemoryError-when-calling-mkString-on-a-parition-tp19527.html) (Further study)
		
	Symptom: constant ++ sampleItem, partitionedHeader(header, index) ++ rows
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
114. [newbie : java.lang.OutOfMemoryError: Java heap space](http://apache-spark-user-list.1001560.n3.nabble.com/newbie-java-lang-OutOfMemoryError-Java-heap-space-tp365.html)

	Symptom: the driver program is dying trying to serialize and broadcast large data
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
117. [extremely slow k-means version](http://apache-spark-user-list.1001560.n3.nabble.com/extremely-slow-k-means-version-tp4489.html)

	Symptom: groupByKey()
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
118. [Join : Giving incorrect result](http://apache-spark-user-list.1001560.n3.nabble.com/Join-Giving-incorrect-result-tp6910.html) (Further study, inconsistent results)
	
	Symptom: join() + AppendOnlyMap
	Pattern:  Unknown
	Reproducible: No  
	Source code : No


128. [Help alleviating OOM errors](http://apache-spark-user-list.1001560.n3.nabble.com/Help-alleviating-OOM-errors-tp8534.html)'

	Symptom: (1) partition is too large => unroll the entire partition, (2) application is super memory-intensive (e.g., creates large data structures)  
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
129. [[Streaming]Executor OOM](http://apache-spark-user-list.1001560.n3.nabble.com/Streaming-Executor-OOM-tp12383.html)

	Symptom: Unknown  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
130. [serialization changes -- OOM](http://apache-spark-user-list.1001560.n3.nabble.com/serialization-changes-OOM-tp13843.html) (Further study)

	Symptom: 620MB serialization uses more than 10GB memory
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
131. [OOM for HiveFromSpark example](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-for-HiveFromSpark-example-tp21129.html)

	Symptom: Unknown  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
132. [Driver OOM while using reduceByKey](http://apache-spark-user-list.1001560.n3.nabble.com/Driver-OOM-while-using-reduceByKey-tp6513.html) (Further study)

	Symptom: Too large MapStatus in the driver  
	Pattern:  That hash map is just a list of where each task ran, it’s not the actual data. How many map and reduce tasks do you have? Maybe you need to give the driver a bit more memory, or use fewer tasks (e.g. do reduceByKey(_ + _, 100) to use only 100 tasks).  
	Reproducible: No  
	Source code : No
	
133. [OOM writing out sorted RDD](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-writing-out-sorted-RDD-tp11828.html)

	Symptom: groupByKey() + sortByKey() 
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
134. [spark master OOME from maxMbInFlight buffers](http://apache-spark-user-list.1001560.n3.nabble.com/spark-master-OOME-from-maxMbInFlight-buffers-tp1441.html)

	Symptom: 70 byte[]s, owned by various Akka threads, all 48mb 
each (3.3gb total)  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
135. [GroupByKey results in OOM - Any other alternative](http://apache-spark-user-list.1001560.n3.nabble.com/GroupByKey-results-in-OOM-Any-other-alternative-tp7625.html)

	Symptom: groupByKey().map( x => (x_1, x._2.distinct)) ...map(x => (x_1, x._2.distinct.count))  
	Pattern:  Hotspot key  
	Reproducible: No  
	Source code : No
	
136. [Spark on Mesos cause mesos-master OOM](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-on-Mesos-cause-mesos-master-OOM-tp12631.html)

	Symptom: large TaskStatus    
	Pattern:  dirver
	Reproducible: No  
	Source code : No
	
137. [Beginner Question on driver memory issue (OOM).](http://apache-spark-user-list.1001560.n3.nabble.com/Beginner-Question-on-driver-memory-issue-OOM-tp21676.html)

	Symptom: Broadcast large table + select + rows.collect()    
	Pattern:  dirver
	Reproducible: No  
	Source code : No
	
138. [Spark-Shell: OOM: GC overhead limit exceeded](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-Shell-OOM-GC-overhead-limit-exceeded-tp15890.html)

	Symptom: Hive query: select + groupBy  
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
139. [OOM Java heap space error on saveAsTextFile](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-Java-heap-space-error-on-saveAsTextFile-tp12604.html)

	Symptom: Unknwon 
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
140. [pyspark sc.parallelize running OOM with smallish data](http://apache-spark-user-list.1001560.n3.nabble.com/pyspark-sc-parallelize-running-OOM-with-smallish-data-tp9452.html)

	Symptom: Unknwon 
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
141. [[PySpark] large # of partitions causes OOM](http://apache-spark-user-list.1001560.n3.nabble.com/PySpark-large-of-partitions-causes-OOM-tp13155.html)

	Symptom: repartition().keyBy(len(x)).reduceByKey() 
	Pattern:  Unknown
	Reproducible: No  
	Source code : No
	
142. [OOM - Requested array size exceeds VM limit](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-Requested-array-size-exceeds-VM-limit-tp17996.html)

	Symptom: local run 
	Pattern:  Individual record (key, value or key and value is relatively small, but number of records in the collection is large.)
	Reproducible: No  
	Source code : No
	
143. [OOM when calling cache on RDD with big data](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-when-calling-cache-on-RDD-with-big-data-tp1894.html)

	Symptom: RDD cache + serialization 
	Pattern:  Large cached RDD (has large individual record)
	Reproducible: No  
	Source code : No
	
144. [Running Wordcount on large file stucks and throws OOM exception](http://apache-spark-user-list.1001560.n3.nabble.com/Running-Wordcount-on-large-file-stucks-and-throws-OOM-exception-tp12747.html)

	Symptom: WordCount,  reduceByKey().saveAsTextFile()
	Pattern:  driver memory is not large enough to hold the whole result set of saveAsTextFile In-Memory  
	Reproducible: No  
	Source code : No
	
146. [What the initial steps to understand root of this OOM exception](http://apache-spark-user-list.1001560.n3.nabble.com/What-the-initial-steps-to-understand-root-of-this-OOM-exception-tp16296.html)

	Symptom: Unknown  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
147. [Command exited with code 137](http://apache-spark-user-list.1001560.n3.nabble.com/Command-exited-with-code-137-tp7557.html)

	Symptom: Unknown  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
148. [Bug in DISK related Storage level?](http://apache-spark-user-list.1001560.n3.nabble.com/Bug-in-DISK-related-Storage-level-tp17954.html)

	Symptom: OOM when DISK_ONLY or MEMORY_AND_DISK_SER storage level, MEMORY_ONLY_SER not OOM  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
149. [how to set spark.executor.memory and heap size](http://apache-spark-user-list.1001560.n3.nabble.com/how-to-set-spark-executor-memory-and-heap-size-tp4719.html)
	
	Symptom: readCompressedStringArray  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	

150. [OutOfMemory in "cogroup"](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-in-cogroup-tp17349.html) (Further study)

	Symptom: join() => coGroup()
	Pattern:  Unbalanced partition => inaccurate size estimator (spill is inaccurate) => OOM AND Spilling data to disk helps nothing because cogroup() needs to read all values for a key into memory.
	Reproducible: No  
	Source code : No
	
151. [how spark dstream handles congestion?](http://apache-spark-user-list.1001560.n3.nabble.com/how-spark-dstream-handles-congestion-tp3540.html)

	Symptom: Unknown  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
152. [Setting only master heap](http://apache-spark-user-list.1001560.n3.nabble.com/Setting-only-master-heap-tp17047.html)

	Symptom: Unknown  
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
153. [How to correctly extimate the number of partition of a graph in GraphX](http://apache-spark-user-list.1001560.n3.nabble.com/How-to-correctly-extimate-the-number-of-partition-of-a-graph-in-GraphX-tp17903.html)

	Symptom: Large graph used in GraphX   
	Pattern:  Unknown  
	Reproducible: No  
	Source code : No
	
154. [[0.9.0] MEMORY_AND_DISK_SER not falling back to disk](http://apache-spark-user-list.1001560.n3.nabble.com/0-9-0-MEMORY-AND-DISK-SER-not-falling-back-to-disk-tp1278.html)

	Symptom: I dropped down to 0.5 but still OOM'd, so sent it all the way to 0.1 and didn't get an OOM  
	Pattern:  Large data buffered in memory    
	Reproducible: No  
	Source code : No

156. [Is there a way to limit the sql query result size?](http://apache-spark-user-list.1001560.n3.nabble.com/Is-there-a-way-to-limit-the-sql-query-result-size-tp18316.html)

	Symptom: Query causes driver OOM  
	Pattern:  Unknown   
	Reproducible: No  
	Source code : No
	

159. [GroupBy Key and then sort values with the group](http://apache-spark-user-list.1001560.n3.nabble.com/GroupBy-Key-and-then-sort-values-with-the-group-tp14455.html)

	Symptom: I have a lot of data for a group & I cannot materialize the iterable into a List or Seq in memory    
	Pattern:  Unknown   
	Reproducible: No  
	Source code : No
	Solution: repartitionAndSortWithinPartitions()

161. [How to compute RDD[(String, Set[String])] that include large Set](http://apache-spark-user-list.1001560.n3.nabble.com/How-to-compute-RDD-String-Set-String-that-include-large-Set-tp21248.html)

	Symptom: distinct.count()    
	Pattern:  Unknown   
	Reproducible: No  
	Source code : No
	
162. [spark streaming and the spark shell](http://apache-spark-user-list.1001560.n3.nabble.com/spark-streaming-and-the-spark-shell-tp3347.html)

	Symptom: Unknown     
	Pattern:  Unknown   
	Reproducible: No  
	Source code : No
	
163. [Does foreach operation increase rdd lineage?](http://apache-spark-user-list.1001560.n3.nabble.com/Does-foreach-operation-increase-rdd-lineage-tp879.html)

	Symptom: foreach is an action, it will collect all data from workers to driver. You will get OOM complained by JVM  
	Pattern: Driver collect()   
	Reproducible: No  
	Source code : No
	
164. [Problem when sorting big file](http://apache-spark-user-list.1001560.n3.nabble.com/Problem-when-sorting-big-file-tp5893.html)

	Symptom: sortByKey()  
	Pattern: hotspot key
	Reproducible: No  
	Source code : No
	
166. [About optimize ALS parameters](http://apache-spark-user-list.1001560.n3.nabble.com/About-optimize-ALS-parameters-tp12824.html)

	Symptom: ALS on large dataset    
	Pattern: hotspot key
	Reproducible: No  
	Source code : No
	
167. [[Streaming] Cannot get executors to stay alive](http://apache-spark-user-list.1001560.n3.nabble.com/Streaming-Cannot-get-executors-to-stay-alive-tp12940.html)

	Symptom: ALS on large dataset    
	Pattern: hotspot key
	Reproducible: No  
	Source code : No
	
168. [KafkaInputDStream mapping of partitions to tasks](http://apache-spark-user-list.1001560.n3.nabble.com/KafkaInputDStream-mapping-of-partitions-to-tasks-tp3360.html)

	Symptom: Unknown
	Pattern: hotspot key
	Reproducible: No  
	Source code : No
	
169. [Memory footprint of Calliope: Spark -> Cassandra writes](http://apache-spark-user-list.1001560.n3.nabble.com/Memory-footprint-of-Calliope-Spark-Cassandra-writes-tp7674.html) (Further study)

	Symptom: Each record generates an Array[]  
	Pattern: Large accumulated results  
	Reproducible: No  
	Source code : No

172. [Stream RDD to local disk](http://apache-spark-user-list.1001560.n3.nabble.com/Stream-RDD-to-local-disk-tp1045.html)

	Symptom: collect() in driver 
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
174. [Questions about productionizing spark](http://apache-spark-user-list.1001560.n3.nabble.com/Questions-about-productionizing-spark-tp4825.html) (Further study)

	Symptom: join() OOM 
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	Solution: co-partition
	
175. [ExternalAppendOnlyMap: Spilling in-memory map](http://apache-spark-user-list.1001560.n3.nabble.com/ExternalAppendOnlyMap-Spilling-in-memory-map-tp6186.html)

	The ExternalAppendOnlyMap is used when a shuffle is causing too much data to be held in memory.  Rather than OOM'ing, Spark writes the data out to disk in a sorted order and reads it back from disk later on when it's needed.  

178. [Only master is really busy at KMeans training](http://apache-spark-user-list.1001560.n3.nabble.com/Only-master-is-really-busy-at-KMeans-training-tp12411.html)
	
	Symptom: vectors.repartition(100) => too large partitions   
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

179. [JVM heap and native allocation questions](http://apache-spark-user-list.1001560.n3.nabble.com/JVM-heap-and-native-allocation-questions-tp12453.html)

	Symptom: native JNI   
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

181. [How to run kmeans after pca?](http://apache-spark-user-list.1001560.n3.nabble.com/How-to-run-kmeans-after-pca-tp14473.html)
   
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
182. [Spark Bug? job fails to run when given options on spark-submit (but starts and fails without)](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-Bug-job-fails-to-run-when-given-options-on-spark-submit-but-starts-and-fails-without-tp16618.html)

	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
	
185. [Not getting it](http://apache-spark-user-list.1001560.n3.nabble.com/Not-getting-it-tp3316.html)

	Symposium: join() => OOM
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
187. [something about memory usage](http://apache-spark-user-list.1001560.n3.nabble.com/something-about-memory-usage-tp5107.html)

	Symposium: Multiple tasks memory usage > limit  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
188. [news20-binary classification with LogisticRegressionWithSGD](http://apache-spark-user-list.1001560.n3.nabble.com/news20-binary-classification-with-LogisticRegressionWithSGD-tp7725.html)

	Symposium: Broadcast large data, task serialization. TreeAggregation  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
189. [Use Spark streaming to process events in a stream and maintain aggregate statisitics on it](http://apache-spark-user-list.1001560.n3.nabble.com/Use-Spark-streaming-to-process-events-in-a-stream-and-maintain-aggregate-statisitics-on-it-tp12184.html)

	Symposium: Maintain some aggregate statistics on the stream  
	Pattern: Unknown  
	Reproducible: No  
	Source code : Yes
	

191. [closure serialization behavior driving me crazy](http://apache-spark-user-list.1001560.n3.nabble.com/closure-serialization-behavior-driving-me-crazy-tp18468.html)

	Symposium: Large array generated  
	Pattern: Large intermedoate results  
	Reproducible: No  
	Source code : Yes
	

192. [RDD Blocks skewing to just few executors](http://apache-spark-user-list.1001560.n3.nabble.com/RDD-Blocks-skewing-to-just-few-executors-tp19112.html)

	Symposium: These become a hotspot and eventually I start seeing OOM errors    
	Pattern: Unbalanced partitions   
	Reproducible: No  
	Source code : Yes
	

194. [com.google.protobuf out of memory](http://apache-spark-user-list.1001560.n3.nabble.com/com-google-protobuf-out-of-memory-tp6357.html)

	persist(storage.StorageLevel.MEMORY_AND_DISK) instead of .cache()

195. [Spark Memory Bounds](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-Memory-Bounds-tp6456.html)

	Dicussion of the memory usage of Spark.
	
	
196. [Using Spark on Data size larger than Memory size](http://apache-spark-user-list.1001560.n3.nabble.com/Using-Spark-on-Data-size-larger-than-Memory-size-tp6589.html)
	
	Symposium:  I'm using mapPartitions() but as you say, it requires that every partition fit in memory      
	Pattern: Large partition  
	Reproducible: No  
	Source code : Yes
	
	
197. [RDD with a Map](http://apache-spark-user-list.1001560.n3.nabble.com/RDD-with-a-Map-tp6849.html)

	Symposium: groupByKey(Map())
	Pattern: Hotspot key
	Reproducible: No  
	Source code : Yes
	
198. [spark.default.parallelism bug?](http://apache-spark-user-list.1001560.n3.nabble.com/spark-default-parallelism-bug-tp12820.html)

	Symposium: related to coGroup(), partition number
	Pattern: Improper data partition  
	Reproducible: No  
	Source code : Yes
	
200. [How to set Akka frame size](http://apache-spark-user-list.1001560.n3.nabble.com/How-to-set-Akka-frame-size-tp39.html)

	Symposium: Akka
	Pattern: Unknown
	Reproducible: No  
	Source code : No
	

204. [Spark Disk Usage](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-Disk-Usage-tp3706.html)

	Symposium: write it to memory first and then if it doesn't fit
	Pattern: Unknown
	Reproducible: No  
	Source code : No

207. [Folding an RDD in order](http://apache-spark-user-list.1001560.n3.nabble.com/Folding-an-RDD-in-order-tp16577.html) (Further study)

	Symposium: this map can be very large (say you have billions of users), then aggregate may OOM  
	Pattern: Large accumulated results  
	Reproducible: No  
	Source code : Yes
	
208. [GC Issues with randomSplit on large dataset](http://apache-spark-user-list.1001560.n3.nabble.com/GC-Issues-with-randomSplit-on-large-dataset-tp17695.html) (Further study)

	Symposium: cartesian on two large RDDs
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	

215. [Spark SQL Exception](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-SQL-Exception-tp14572.html)

	Sort-based Aggregation (SparkSQL only support the hash-based aggregation, which may cause OOM if too many identical keys in the input tuples.)

216. [OutOfMemory Error](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-Error-tp12275.html)

	a simple Map operation where a record is mapped to a new huge value, resulting in OutOfMemory Error
	
217. [OutOfMemory Error](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-Error-tp1746.html)

	Symposium: Unknown
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
218. [Cannot get rid of OutOfMemory](http://apache-spark-user-list.1001560.n3.nabble.com/Cannot-get-rid-of-OutOfMemory-tp17016.html) (Further study)

	Symposium: map().countByValue()  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
	
219. [OutOfMemory error in Spark Core](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-error-in-Spark-Core-tp21179.html) (Further study)

	Symposium: write() => serialization => Arrays.copyOf() 
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
220. [OutOfMemory : Java heap space error](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-Java-heap-space-error-tp9091.html)

	Symposium: unknown
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
221. [OutofMemory: Failed on spark/examples/bagel/WikipediaPageRank.scala](http://apache-spark-user-list.1001560.n3.nabble.com/OutofMemory-Failed-on-spark-examples-bagel-WikipediaPageRank-scala-tp6040.html)

	Symposium: WikipediaPageRank in Bagel
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
222. [mllib svd gives: Java OutOfMemory Error](http://apache-spark-user-list.1001560.n3.nabble.com/mllib-svd-gives-Java-OutOfMemory-Error-tp21982.html) (Further study)

	Symposium: Compute SVD (has stack trace)  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

223. [Scala PCA OutOfMemory error on small number of columns](http://apache-spark-user-list.1001560.n3.nabble.com/Scala-PCA-OutOfMemory-error-on-small-number-of-columns-tp22479.html) (Further study)

	Symposium: Compute PCA (has stack trace)  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
224. [How to efficiently join this two complicated rdds](http://apache-spark-user-list.1001560.n3.nabble.com/How-to-efficiently-join-this-two-complicated-rdds-tp1665.html) (Further study)

	Symposium: Driver collect() gradually => OOM  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
225. [The running time of spark](http://apache-spark-user-list.1001560.n3.nabble.com/The-running-time-of-spark-tp12624.html)

	Symposium: a shortest path algorithm 
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
226. [broadcast: OutOfMemoryError](http://apache-spark-user-list.1001560.n3.nabble.com/broadcast-OutOfMemoryError-tp20633.html)

	Symposium: broadcasting a large array   
	Pattern: Broadcast large data  
	Reproducible: No  
	Source code : No

228. [java.lang.OutOfMemoryError: GC overhead limit exceeded](http://apache-spark-user-list.1001560.n3.nabble.com/java-lang-OutOfMemoryError-GC-overhead-limit-exceeded-tp10301.html) (Further study)

	Symposium: GraphLoad + partitionBy()   
	Pattern: Broadcast large data  
	Reproducible: No  
	Source code : No
	
229. [driver memory](http://apache-spark-user-list.1001560.n3.nabble.com/driver-memory-tp10486.html)

	Symposium: Driver broadcast large data, driver OOM    
	Pattern: Broadcast large data  
	Reproducible: No  
	Source code : No
	

233. [OutOfMemoryError with basic kmeans](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemoryError-with-basic-kmeans-tp1651.html) (Further study)

	Symposium: Basic Kmeans + cache + serialize, adjust spark.kryoserializer.buffer.mb  
	Pattern: Too big the model, too many features    
	Reproducible: No  
	Source code : No
	
	Not sure if you resolved this but I had a similar issue and resolved it. In my case, the problem was the ids of my items were of type Long and could be very large (even though there are only a small number of distinct ids... maybe a few hundred of them). KMeans will create a dense vector for the cluster centers so its important that the dimensionality not be huge.
	
238. [java.lang.StackOverflowError when calling count()](http://apache-spark-user-list.1001560.n3.nabble.com/java-lang-StackOverflowError-when-calling-count-tp5649.html)
	
	Symposium: Iteration => constantly cached    
	Pattern: Large data cached    
	Reproducible: No  
	Source code : No
	
	I think this is happening because how you are caching the output RDD 
that are being generated repeatedly. In every iteration, it is 
building this new union RDD which contains the data of the previous 
union RDD plus some new data. Since each of these union RDDs are 
cached, the underlying data is being cached repeatedly. quadratic increase 

239. [java.lang.OutOfMemoryError while running SVD MLLib example](http://apache-spark-user-list.1001560.n3.nabble.com/java-lang-OutOfMemoryError-while-running-SVD-MLLib-example-tp14972.html)

	Symposium: Driver collect large matrix   
	Pattern: Driver  collect  
	Reproducible: No  
	Source code : No
	
	7000x7000 is not tall-and-skinny matrix. Storing the dense matrix 
requires 784MB. The driver needs more storage for collecting result 
from executors as well as making a copy for LAPACK's dgesvd. So you 
need more memory

## Issues found by searching "Out of Memory" in Spark devloper mailing list

1. [Sorting partitions in Java](http://apache-spark-developers-list.1001551.n3.nabble.com/Sorting-partitions-in-Java-tp6715.html)
2. [Memory config issues](http://apache-spark-developers-list.1001551.n3.nabble.com/Memory-config-issues-tp10183.html)
3. [Fwd: Accumulator question](http://apache-spark-developers-list.1001551.n3.nabble.com/Fwd-Accumulator-question-tp8709.html)
4. [OOM when making bins in BinaryClassificationMetrics ?](http://apache-spark-developers-list.1001551.n3.nabble.com/OOM-when-making-bins-in-BinaryClassificationMetrics-tp9061.html)
5. [Storage of RDDs created via sc.parallelize](http://apache-spark-developers-list.1001551.n3.nabble.com/Storage-of-RDDs-created-via-sc-parallelize-tp11135.html)
6. [[GitHub] incubator-spark pull request: MLLIB-25: Implicit ALS runs out of m...](http://apache-spark-developers-list.1001551.n3.nabble.com/GitHub-incubator-spark-pull-request-MLLIB-25-Implicit-ALS-runs-out-of-m-tp2404.html)
7. [[GitHub] spark pull request: [WIP] [SPARK-1132] Persisting Web UI through r...](http://apache-spark-developers-list.1001551.n3.nabble.com/GitHub-spark-pull-request-WIP-SPARK-1132-Persisting-Web-UI-through-r-tp3173.html)
8. [Maximum size of vector that reduce can handle](http://apache-spark-developers-list.1001551.n3.nabble.com/Maximum-size-of-vector-that-reduce-can-handle-tp10256.html)
9. [[Graphx] some problem about using SVDPlusPlus](http://apache-spark-developers-list.1001551.n3.nabble.com/Graphx-some-problem-about-using-SVDPlusPlus-tp7896.html)
10. [TorrentBroadcast slow performance](http://apache-spark-developers-list.1001551.n3.nabble.com/TorrentBroadcast-slow-performance-tp8669.html)
11. [sparkSQL thread safe?](http://apache-spark-developers-list.1001551.n3.nabble.com/sparkSQL-thread-safe-tp7263.html)
12. [Low Level Kafka Consumer for Spark](http://apache-spark-developers-list.1001551.n3.nabble.com/Low-Level-Kafka-Consumer-for-Spark-tp7644.html)
13. [MLlib - logistic regression with GD vs LBFGS, sparse vs dense benchmark result](http://apache-spark-developers-list.1001551.n3.nabble.com/MLlib-logistic-regression-with-GD-vs-LBFGS-sparse-vs-dense-benchmark-result-tp6386.html)
14. [Too big data Spark SQL on Hive table on version 1.0.2 has some strange output](http://apache-spark-developers-list.1001551.n3.nabble.com/Too-big-data-Spark-SQL-on-Hive-table-on-version-1-0-2-has-some-strange-output-tp8662.html)
15. [test suite results in OOME](http://apache-spark-developers-list.1001551.n3.nabble.com/test-suite-results-in-OOME-tp40.html)
16. [oome from large map output status](http://apache-spark-developers-list.1001551.n3.nabble.com/oome-from-large-map-output-status-tp1851.html)
17. [Troubleshooting JVM OOM during Spark Unit Tests](http://apache-spark-developers-list.1001551.n3.nabble.com/Troubleshooting-JVM-OOM-during-Spark-Unit-Tests-tp9480.html)
18. [Spark master OOMs with exception stack trace stored in JobProgressListener (SPARK-4906)](http://apache-spark-developers-list.1001551.n3.nabble.com/Spark-master-OOMs-with-exception-stack-trace-stored-in-JobProgressListener-SPARK-4906-tp9857.html)
19. [take() reads every partition if the first one is empty](http://apache-spark-developers-list.1001551.n3.nabble.com/take-reads-every-partition-if-the-first-one-is-empty-tp7956.html)
20. [spark 1.3 sbt build seems to be broken](http://apache-spark-developers-list.1001551.n3.nabble.com/spark-1-3-sbt-build-seems-to-be-broken-tp10491.html)
21. [OutOfMemoryError when running sbt/sbt test](http://apache-spark-developers-list.1001551.n3.nabble.com/OutOfMemoryError-when-running-sbt-sbt-test-tp8056.html)
22. [Using memory mapped file for shuffle](http://apache-spark-developers-list.1001551.n3.nabble.com/Using-memory-mapped-file-for-shuffle-tp11576.html)
23. [Eliminate copy while sending data : any Akka experts here ?](http://apache-spark-developers-list.1001551.n3.nabble.com/Eliminate-copy-while-sending-data-any-Akka-experts-here-tp7127.html)
24. [Streaming partitions to driver for use in .toLocalIterator](http://apache-spark-developers-list.1001551.n3.nabble.com/Streaming-partitions-to-driver-for-use-in-toLocalIterator-tp10664.html)
25. [Apache spark on 27gb wikipedia data](http://apache-spark-developers-list.1001551.n3.nabble.com/Apache-spark-on-27gb-wikipedia-data-tp6487.html)
26. [[ANNOUNCE] Spark 1.2.0 Release Preview Posted](http://apache-spark-developers-list.1001551.n3.nabble.com/ANNOUNCE-Spark-1-2-0-Release-Preview-Posted-tp9400.html)
27. [Tests failed after assembling the latest code from github](http://apache-spark-developers-list.1001551.n3.nabble.com/Tests-failed-after-assembling-the-latest-code-from-github-tp6315.html)
28. [bug using kryo as closure serializer](http://apache-spark-developers-list.1001551.n3.nabble.com/bug-using-kryo-as-closure-serializer-tp6473.html)
29. [[VOTE] Release Apache Spark 1.3.1](http://apache-spark-developers-list.1001551.n3.nabble.com/VOTE-Release-Apache-Spark-1-3-1-tp11399.html)
30. [[RESULT] [VOTE] Release Apache Spark 1.3.1](http://apache-spark-developers-list.1001551.n3.nabble.com/RESULT-VOTE-Release-Apache-Spark-1-3-1-tp11470.html)
31. [[GitHub] spark pull request: Patch for SPARK-942](http://apache-spark-developers-list.1001551.n3.nabble.com/GitHub-spark-pull-request-Patch-for-SPARK-942-tp3311.html)
32. [[GitHub] spark pull request: [SPARK-1186] : Enrich the Spark Shell to suppo...](http://apache-spark-developers-list.1001551.n3.nabble.com/GitHub-spark-pull-request-SPARK-1186-Enrich-the-Spark-Shell-to-suppo-tp4000.html)