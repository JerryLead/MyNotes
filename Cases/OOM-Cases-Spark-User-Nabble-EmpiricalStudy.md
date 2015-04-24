## Issues that contain "Out of Memory" or "OOM" or "OutOfMemory" in Spark user mailing list

2. [Running out of memory Naive Bayes](http://apache-spark-user-list.1001560.n3.nabble.com/Running-out-of-memory-Naive-Bayes-tp4866.html)

	Symptom: Too many features stored in the driver  
	Pattern: Large data generated/collected at driver  
	Reproducible: No  

	Even the features are sparse, the conditional probabilities are stored 
in a dense matrix. With 200 labels and 2 million features, you need to 
store at least 4e8 doubles on the driver node. With multiple 
partitions, you may need more memory on the driver. Could you try 
reducing the number of partitions and giving driver more ram and see 
whether it can help
	

16. [Common crawl parsing has high fan out and runs out of memory](http://apache-spark-user-list.1001560.n3.nabble.com/Common-crawl-parsing-has-high-fan-out-and-runs-out-of-memory-tp21708.html) 


	Symptom: Large ArrayList in Java flatMap()  
	Pattern: Large accumulated results  
	Reproducible: Yes  
	
	The code works, but it requires almost 12G of memory per ParseWarc.call, because even though I know how to read one record a time from the gzip, and I can output one record a time, the flatMap api requires that the whole Iterable is created in memory before being returned. 
	
18. [distinct on huge dataset](http://apache-spark-user-list.1001560.n3.nabble.com/distinct-on-huge-dataset-tp3025.html) (Further study, distinct())

	Symptom: distinct.count(), out of memory error was caused by setting spark.spill to false  
	Pattern: Improper data partition   
	Reproducible: Yes
		
21. [Partitioning - optimization or requirement?](http://apache-spark-user-list.1001560.n3.nabble.com/Partitioning-optimization-or-requirement-tp3359.html)

	Symptom: Hotspot key (doing unbalanced joins (ie. cardinality of some joined elements much larger than others)  
	Pattern: Hotspot key
	Reproducible: No  
	
22. [tiers of caching](http://apache-spark-user-list.1001560.n3.nabble.com/tiers-of-caching-tp8927.html)

	Symptom: (graphx liberally cache RDDs for efficiency, however it can also leave a long trail of unused yet cached RDDs, that might push other RDDs out of memory.)  
	  
	Pattern: Too many rdds cached in memory  
	Reproducible: No   

	
37. [trouble with broadcast variables on pyspark](http://apache-spark-user-list.1001560.n3.nabble.com/trouble-with-broadcast-variables-on-pyspark-tp1301.html)

	Symptom: A ~1GB array seems to be blowing up beyond the size of the driver machine's memory when it's pickled. I've tried to get around this by broadcasting smaller chunks of it one at a time.   
	
	Pattern: Large data generated/broadcasted by driver    
	Reproducible: No  

	
49. [MLLib ALS question](http://apache-spark-user-list.1001560.n3.nabble.com/MLLib-ALS-question-tp15420.html) (Further study)

	Symptom: The current ALS 
implementation constructs all subproblems in memory. With rank=10, 
that means (6.5M + 2.5M) * 10^2 / 2 * 8 bytes = 3.5GB. The ratings 
need 2GB, not counting the overhead.   ALS still needs to load and deserialize the in/out blocks (one by one) 
from disk and then construct least squares subproblems. All happen in 
RAM. The final model is also stored in memory.  

	Pattern: Large data loaded into memory, intermediate computing results. 
	Reproducible: No  
	
50. [Accumulator question](http://apache-spark-user-list.1001560.n3.nabble.com/Accumulator-question-tp15715.html)

	Symptom: we're gathering data from repeated queries using some relatively sizable accumulators; at the moment, we're creating one per query, and running out of memory after far too few queries.  
	
	Pattern: Large accumulated results in Accumulators.   
	Reproducible: Yes   
	
51. [Lag function equivalent in an RDD](http://apache-spark-user-list.1001560.n3.nabble.com/Lag-function-equivalent-in-an-RDD-tp16448.html)

	Symptom: I have tried reduceByKey and then splitting the List of position in 
tuples.  one vehicle has a huge amount of data that could fail. 

	Pattern: Hotspot key  
	Reproducible:No  


56. [Memory allocation in the driver](http://apache-spark-user-list.1001560.n3.nabble.com/Memory-allocation-in-the-driver-tp8406.html)

	Symptom: call to "b.first" will cause the spark driver to allocate a VERY large piece of memory. The first item of the first partition is very small (less than 200 bytes). However, the size of the entire first partition was about 380 MB.  
	
	Pattern: large data collected by driver, although each partition is small.  
	Reproducible: No  
	
59. [Spark limitations question](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-limitations-question-tp3296.html) 

	Symptom:  join "Base" and "Skewed", works well on all but one of the nodes on the cluster  
	Pattern: Improper data partition, hotspot key  
	Reproducible: No 

60. [Kyro serialization slow and runs OOM](http://apache-spark-user-list.1001560.n3.nabble.com/Kyro-serialization-slow-and-runs-OOM-tp1073.html)
	
	Symptom: I load my dataset, transform it with some one to one transformations, and try to cache the eventual RDD - it runs really slow and then runs out of memory.   
	
	Pattern: Large  cached  RDD  
	Reproducible: No  

67. [advice on maintaining a production spark cluster?](http://apache-spark-user-list.1001560.n3.nabble.com/advice-on-maintaining-a-production-spark-cluster-tp5848.html)

	Symptom: Running out of memory on the driver side (esp. with large broadcast variables)   
	Pattern: Driver is going to broadcast large dataset  
	Reproducible: No  
	
73. [Understanding RDD.GroupBy OutOfMemory Exceptions](http://apache-spark-user-list.1001560.n3.nabble.com/Understanding-RDD-GroupBy-OutOfMemory-Exceptions-tp11427.html)  
	
	Symptom: OOM in groupByKey() but no error in reduceByKey()  
	Pattern:  Hotspot key, large input record  
	Reproducible: No  
	
	The groupBy operator in Spark is not an aggregation operator (e.g. in SQL where you do select sum(salary) group by age...) - there are separate more efficient operators for aggregations. Currently groupBy requires that all of the values for one key can fit in memory. In your case, it's possible you have a single key with a very large number of values, given that your count seems to be failing on a single task.

77. [Bulk-load to HBase](http://apache-spark-user-list.1001560.n3.nabble.com/Bulk-load-to-HBase-tp14667.html) 

	Symptom: OOM on mapPartitionsWithIndex() for splitKeys, I have to merge the byte[]s that have the same key.   
	Pattern:  Large accumulated results  
	Reproducible: Yes 
	
	The problem is that you will first collect and allocate many small byte[] in memory, and then merge them. If the total size of the byte[]s is very large, you run out of memory, 

81. [something about rdd.collect](http://apache-spark-user-list.1001560.n3.nabble.com/something-about-rdd-collect-tp16451.html)

	Symptom: collect 200 million words. It is a pretty large number and you can run out of memory on your driver  
	
	Pattern:  Large results collected by driver   
	Reproducible: Yes  
	
83. [MLLib /ALS : java.lang.OutOfMemoryError: Java heap space](http://apache-spark-user-list.1001560.n3.nabble.com/MLLib-ALS-java-lang-OutOfMemoryError-Java-heap-space-tp20584.html)
	
	Symptom: shuffle buffer + storage buffer > limit  
	Pattern:  Large shuffle buffer + Large storage buffer  
	Reproducible: Yes  


96. [OOM with groupBy + saveAsTextFile](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-with-groupBy-saveAsTextFile-tp17891.html) (Further study)
			
	Symptom: GroupBy + saveAsTextFile, The value after groupBy() (i.e., a single String) is too large,  the value in your key, value pair after group by is too long  
	
	Pattern:  Large single outputted <K, V> record  
	Reproducible: No  
	
98. [What should happen if we try to cache more data than the cluster can hold in memory?](http://apache-spark-user-list.1001560.n3.nabble.com/What-should-happen-if-we-try-to-cache-more-data-than-the-cluster-can-hold-in-memory-tp11175.html)
	
	Symptom: Individual partitions were too big to be cached in memory.    
	Pattern: Improper data partition, large data cached in memory    
	Reproducible: No  

102. [processing large number of files](http://apache-spark-user-list.1001560.n3.nabble.com/processing-large-number-of-files-tp15429.html)
	
	Symptom: large array/model in the driver   
	Pattern: Large data generated in the driver  
	Reproducible: No  
	
103. [RowMatrix PCA out of heap space error](http://apache-spark-user-list.1001560.n3.nabble.com/RowMatrix-PCA-out-of-heap-space-error-tp16305.html)
	
	Symptom:  The Gramian is 8000 x 8000, dense, and full of 8-byte doubles. It's 
symmetric so can get away with storing it in ~256MB in driver   

	Pattern: Large data generated in the driver   
	Reproducible : No
	
105. [Problems with broadcast large datastructure](http://apache-spark-user-list.1001560.n3.nabble.com/Problems-with-broadcast-large-datastructure-tp331.html)

	Symptom: Broadcast large data  
	Pattern:  Large data cached in memory  
	Reproducible: No  
	
	
107. [Spark streaming questions](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-streaming-questions-tp1494.html)

	Symptom: DStream.persist() constantly  
	Pattern:  Large data cached in memory  
	Reproducible: No  

114. [newbie : java.lang.OutOfMemoryError: Java heap space](http://apache-spark-user-list.1001560.n3.nabble.com/newbie-java-lang-OutOfMemoryError-Java-heap-space-tp365.html)

	Symptom: the driver program is dying trying to serialize and broadcast large data
	Pattern: Large data generated in memory   
	Reproducible: No  
	

128. [Help alleviating OOM errors](http://apache-spark-user-list.1001560.n3.nabble.com/Help-alleviating-OOM-errors-tp8534.html)'

	Symptom: (1) partition is too large => unroll the entire partition, (2) application is super memory-intensive (e.g., creates large data structures)  
	Pattern: Large accumulated results  
	Reproducible: No  

130. [serialization changes -- OOM](http://apache-spark-user-list.1001560.n3.nabble.com/serialization-changes-OOM-tp13843.html) (Further study)

	Symptom: 620MB serialization uses more than 10GB memory  
	Pattern: serialization  
	Reproducible: No  
	
132. [Driver OOM while using reduceByKey](http://apache-spark-user-list.1001560.n3.nabble.com/Driver-OOM-while-using-reduceByKey-tp6513.html) (Further study)

	Symptom: Too large MapStatus in the driver  
	Pattern: Large results collected by driver 
	Reproducible: No  
	
133. [OOM writing out sorted RDD](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-writing-out-sorted-RDD-tp11828.html)

	Symptom: groupByKey() + sortByKey(), partitions may be skewed as a result of the sort, with one or two paritions having upto 10% of all rows  
	
	Pattern: Improper data partition    
	Reproducible: No  
	
135. [GroupByKey results in OOM - Any other alternative](http://apache-spark-user-list.1001560.n3.nabble.com/GroupByKey-results-in-OOM-Any-other-alternative-tp7625.html)

	Symptom: groupByKey().map( x => (x_1, x._2.distinct)) ...map(x => (x_1, x._2.distinct.count))  
	Pattern: Hotspot key  
	Reproducible: Yes  
		
136. [Spark on Mesos cause mesos-master OOM](http://apache-spark-user-list.1001560.n3.nabble.com/Spark-on-Mesos-cause-mesos-master-OOM-tp12631.html)

	Symptom: large TaskStatus collected by driver 
	Pattern: Large results collected by driver  
	Reproducible: No  
	
137. [Beginner Question on driver memory issue (OOM).](http://apache-spark-user-list.1001560.n3.nabble.com/Beginner-Question-on-driver-memory-issue-OOM-tp21676.html)

	Symptom: Broadcast large table + select + rows.collect()    
	Pattern: Large results collected by driver   
	Reproducible: No   

	
143. [OOM when calling cache on RDD with big data](http://apache-spark-user-list.1001560.n3.nabble.com/OOM-when-calling-cache-on-RDD-with-big-data-tp1894.html)

	Symptom: RDD cache + serialization  
	Pattern: Large cached RDD  
	Reproducible: No  
	
144. [Running Wordcount on large file stucks and throws OOM exception](http://apache-spark-user-list.1001560.n3.nabble.com/Running-Wordcount-on-large-file-stucks-and-throws-OOM-exception-tp12747.html)

	Symptom: WordCount,  reduceByKey().saveAsTextFile()  
	Pattern: driver memory is not large enough to hold the whole result set of saveAsTextFile In-Memory   
	Reproducible: No  


150. [OutOfMemory in "cogroup"](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-in-cogroup-tp17349.html) (Further study)

	Symptom: join() => coGroup()  
	Pattern: Unbalanced partition => inaccurate size estimator (spill is inaccurate) => OOM AND Spilling data to disk helps nothing because cogroup() needs to read all values for a key into memory.  
	Reproducible: No   
	
154. [[0.9.0] MEMORY_AND_DISK_SER not falling back to disk](http://apache-spark-user-list.1001560.n3.nabble.com/0-9-0-MEMORY-AND-DISK-SER-not-falling-back-to-disk-tp1278.html)

	Symptom: I dropped down to 0.5 but still OOM'd, so sent it all the way to 0.1 and didn't get an OOM  
	Pattern: Large data buffered in memory    
	Reproducible: No  


159. [GroupBy Key and then sort values with the group](http://apache-spark-user-list.1001560.n3.nabble.com/GroupBy-Key-and-then-sort-values-with-the-group-tp14455.html)

	Symptom: I have a lot of data for a group & I cannot materialize the iterable into a List or Seq in memory    
	Pattern: Large accumulated results   
	Reproducible: No  
	Solution: repartitionAndSortWithinPartitions()
		
163. [Does foreach operation increase rdd lineage?](http://apache-spark-user-list.1001560.n3.nabble.com/Does-foreach-operation-increase-rdd-lineage-tp879.html)

	Symptom: foreach is an action, it will collect all data from workers to driver. You will get OOM complained by JVM  
	Pattern: Driver collect()   
	Reproducible: No  
	
169. [Memory footprint of Calliope: Spark -> Cassandra writes](http://apache-spark-user-list.1001560.n3.nabble.com/Memory-footprint-of-Calliope-Spark-Cassandra-writes-tp7674.html) (Further study)

	Symptom: Each record generates an Array[]  
	Pattern: Large accumulated results  
	Reproducible: No  


178. [Only master is really busy at KMeans training](http://apache-spark-user-list.1001560.n3.nabble.com/Only-master-is-really-busy-at-KMeans-training-tp12411.html)
	
	Symptom: vectors.repartition(100) => too large partitions   
	Pattern: Large data partition  
	Reproducible: No  
	
185. [Not getting it](http://apache-spark-user-list.1001560.n3.nabble.com/Not-getting-it-tp3316.html)

	Symptom: groupBy() => OOM  
	Pattern: Large data partition   
	Reproducible: No  
	

191. [closure serialization behavior driving me crazy](http://apache-spark-user-list.1001560.n3.nabble.com/closure-serialization-behavior-driving-me-crazy-tp18468.html)

	Symptom: Large array cached
	Pattern: Large data loaded  
	Reproducible: No  

192. [RDD Blocks skewing to just few executors](http://apache-spark-user-list.1001560.n3.nabble.com/RDD-Blocks-skewing-to-just-few-executors-tp19112.html)

	Symptom: These become a hotspot and eventually I start seeing OOM errors    
	Pattern: Unbalanced partitions   
	Reproducible: No  

	
196. [Using Spark on Data size larger than Memory size](http://apache-spark-user-list.1001560.n3.nabble.com/Using-Spark-on-Data-size-larger-than-Memory-size-tp6589.html)
	
	Symptom:  I'm using mapPartitions() but as you say, it requires that every partition fit in memory      
	Pattern: Large partition  
	Reproducible: No  
	
197. [RDD with a Map](http://apache-spark-user-list.1001560.n3.nabble.com/RDD-with-a-Map-tp6849.html)

	Symptom: groupByKey(Map())
	Pattern: Hotspot key
	Reproducible: No  
	
198. [spark.default.parallelism bug?](http://apache-spark-user-list.1001560.n3.nabble.com/spark-default-parallelism-bug-tp12820.html)

	Symptom: related to coGroup(), partition number
	Pattern: Improper data partition  
	Reproducible: No  

207. [Folding an RDD in order](http://apache-spark-user-list.1001560.n3.nabble.com/Folding-an-RDD-in-order-tp16577.html)

	Symptom: this map can be very large (say you have billions of users), then aggregate may OOM  
	Pattern: Large accumulated results  
	Reproducible: No  
	
208. [GC Issues with randomSplit on large dataset](http://apache-spark-user-list.1001560.n3.nabble.com/GC-Issues-with-randomSplit-on-large-dataset-tp17695.html) (Further study)

	Symptom: cartesian on two large RDDs  
	Pattern: Unknown  
	Reproducible: No  


216. [OutOfMemory Error](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-Error-tp12275.html)

	Symptom: a simple Map operation where a record is mapped to a new huge value, resulting in OutOfMemory Error   
	Pattern: Large record      
	Reproducible: No  

	
224. [How to efficiently join this two complicated rdds](http://apache-spark-user-list.1001560.n3.nabble.com/How-to-efficiently-join-this-two-complicated-rdds-tp1665.html) (Further study)

	Symptom: Driver collect() gradually => OOM  
	Pattern: Large results collected by driver    
	Reproducible: No  
	
226. [broadcast: OutOfMemoryError](http://apache-spark-user-list.1001560.n3.nabble.com/broadcast-OutOfMemoryError-tp20633.html)

	Symptom: broadcasting a large array   
	Pattern: Broadcast large data   
	Reproducible: No  

228. [java.lang.OutOfMemoryError: GC overhead limit exceeded](http://apache-spark-user-list.1001560.n3.nabble.com/java-lang-OutOfMemoryError-GC-overhead-limit-exceeded-tp10301.html) (Further study)

	Symptom: GraphLoad + partitionBy()   
	Pattern: Broadcast large data  
	Reproducible: No  
	
229. [driver memory](http://apache-spark-user-list.1001560.n3.nabble.com/driver-memory-tp10486.html)

	Symptom: Driver broadcast large data, driver OOM    
	Pattern: Broadcast large data  
	Reproducible: No  
	
233. [OutOfMemoryError with basic kmeans](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemoryError-with-basic-kmeans-tp1651.html) (Further study)

	Symptom: Basic Kmeans + cache + serialize, adjust spark.kryoserializer.buffer.mb  
	Pattern: Too big the model, too many features    
	Reproducible: No  

	Not sure if you resolved this but I had a similar issue and resolved it. In my case, the problem was the ids of my items were of type Long and could be very large (even though there are only a small number of distinct ids... maybe a few hundred of them). KMeans will create a dense vector for the cluster centers so its important that the dimensionality not be huge.
	
238. [java.lang.StackOverflowError when calling count()](http://apache-spark-user-list.1001560.n3.nabble.com/java-lang-StackOverflowError-when-calling-count-tp5649.html)
	
	Symptom: Iteration => constantly cached    
	Pattern: Large RDD cached    
	Reproducible: No  
	Source code : No
	
	I think this is happening because how you are caching the output RDD 
that are being generated repeatedly. In every iteration, it is 
building this new union RDD which contains the data of the previous 
union RDD plus some new data. Since each of these union RDDs are 
cached, the underlying data is being cached repeatedly. quadratic increase 

239. [java.lang.OutOfMemoryError while running SVD MLLib example](http://apache-spark-user-list.1001560.n3.nabble.com/java-lang-OutOfMemoryError-while-running-SVD-MLLib-example-tp14972.html)

	Symptom: Driver collect large matrix   
	Pattern: Driver  collect  
	Reproducible: No  
	
	7000x7000 is not tall-and-skinny matrix. Storing the dense matrix 
requires 784MB. The driver needs more storage for collecting result 
from executors as well as making a copy for LAPACK's dgesvd. So you 
need more memory


## Issues found by searching "Out of Memory" in Spark devloper mailing list

3. [Fwd: Accumulator question](http://apache-spark-developers-list.1001551.n3.nabble.com/Fwd-Accumulator-question-tp8709.html)

	Symptom: I've a case where we're gathering data from repeated queries using some   relatively sizable accumulators; at the moment, we're creating one per query, and running out of memory after far too few queries.     
	
	Pattern: Large accumulated results in Accumulators      
	Reproducible: No  
	
4. [OOM when making bins in BinaryClassificationMetrics ?](http://apache-spark-developers-list.1001551.n3.nabble.com/OOM-when-making-bins-in-BinaryClassificationMetrics-tp9061.html)

	Symptom: using 
BinaryClassificationMetrics to build an AUC curve for a classifier 
over a reasonably large number of points (~12M).  The computation does some operations by key, and this ran out of 
memory    

	Pattern: a key has many distinct values     
	Reproducible: No  

6. [[GitHub] incubator-spark pull request: MLLIB-25: Implicit ALS runs out of m...](http://apache-spark-developers-list.1001551.n3.nabble.com/GitHub-incubator-spark-pull-request-MLLIB-25-Implicit-ALS-runs-out-of-m-tp2404.html) (Further study)

	Symptom: It's computed as the sum of matrices; an f x f matrix is created for each of n user/item rows in a partition.     
	Pattern: Large intermedaite results  + large accumulated results     
	Reproducible: No  


8. [Maximum size of vector that reduce can handle](http://apache-spark-developers-list.1001551.n3.nabble.com/Maximum-size-of-vector-that-reduce-can-handle-tp10256.html) (Further study)

	Symptom: reduce() generates large taskResults, collected by the driver.     
	Pattern: Large results collected by the driver     
	Reproducible: No  
	
9. [[Graphx] some problem about using SVDPlusPlus](http://apache-spark-developers-list.1001551.n3.nabble.com/Graphx-some-problem-about-using-SVDPlusPlus-tp7896.html) (Further study)

	Symptom: which will also be cached to memory. However, as the iteration goes on, more and more graph will be cached and out of memory happens.  
	  
	Pattern: RDD cached in memory as the iteration goes       
	Reproducible: No  

11. [sparkSQL thread safe?](http://apache-spark-developers-list.1001551.n3.nabble.com/sparkSQL-thread-safe-tp7263.html)

	Symptom: I was getting out of memory doing a bunch of ops against medium(~1TB 
compressed) input sizes with simple things that should spill nicely 
(distinct, reduceByKey(_ + _) ). 
	Pattern: Too many buffers / large buffers
	Reproducible: No  

16. [oome from large map output status](http://apache-spark-developers-list.1001551.n3.nabble.com/oome-from-large-map-output-status-tp1851.html)

	Symptom: 70 of these 50mb byte[]s in RAM    
	Pattern: Too many small buffers    
	Reproducible: No  

19. [take() reads every partition if the first one is empty](http://apache-spark-developers-list.1001551.n3.nabble.com/take-reads-every-partition-if-the-first-one-is-empty-tp7956.html)

	Symptom: take() reads ALL partitions if the first one (or first k) are empty      
	Pattern: driver collect()    
	Reproducible: No  
	
23. [Eliminate copy while sending data : any Akka experts here ?](http://apache-spark-developers-list.1001551.n3.nabble.com/Eliminate-copy-while-sending-data-any-Akka-experts-here-tp7127.html) (Further study)

	Symptom: about the copy buffer, O(M*R)        
	Pattern: driver collect()    
	Reproducible: No  

## Further study

218. [Cannot get rid of OutOfMemory](http://apache-spark-user-list.1001560.n3.nabble.com/Cannot-get-rid-of-OutOfMemory-tp17016.html) (Further study)

	Symptom: map().countByValue()  
	Pattern: Unknown  
	Reproducible: No  
	
219. [OutOfMemory error in Spark Core](http://apache-spark-user-list.1001560.n3.nabble.com/OutOfMemory-error-in-Spark-Core-tp21179.html) (Further study)

	Symptom: write() => serialization => Arrays.copyOf() 
	Pattern: Unknown  
	Reproducible: No  
	
	
	
222. [mllib svd gives: Java OutOfMemory Error](http://apache-spark-user-list.1001560.n3.nabble.com/mllib-svd-gives-Java-OutOfMemory-Error-tp21982.html) (Further study)

	Symptom: Compute SVD (has stack trace)  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No

223. [Scala PCA OutOfMemory error on small number of columns](http://apache-spark-user-list.1001560.n3.nabble.com/Scala-PCA-OutOfMemory-error-on-small-number-of-columns-tp22479.html) (Further study)

	Symptom: Compute PCA (has stack trace)  
	Pattern: Unknown  
	Reproducible: No  
	Source code : No
	
1. [Sorting partitions in Java](http://apache-spark-developers-list.1001551.n3.nabble.com/Sorting-partitions-in-Java-tp6715.html)

	Symptom: sortByKey currently requires partitions to fit in memory    
	Pattern: SortByKey()    
	Reproducible: No  
	Source code : No
	
2. [Memory config issues](http://apache-spark-developers-list.1001551.n3.nabble.com/Memory-config-issues-tp10183.html)

	Symptom: SQL GROUP BY      
	Pattern: groupBy    
	Reproducible: No  
	