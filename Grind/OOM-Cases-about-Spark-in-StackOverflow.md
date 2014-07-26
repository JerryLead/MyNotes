#OOM Cases about Spark in StackOverflow

## Interesting questions
1. [How to monitor different blocks of memory in Spark and know what is running out on OOM?](http://stackoverflow.com/questions/24189822/how-to-monitor-different-blocks-of-memory-in-spark-and-know-what-is-running-out)

	every few seconds I get an update like:

	- Cache: 40% use (40/100 GB)
	- Shuffle: 90% use (45/50 GB)
	- Heap: 10% use (1/10 GB)
	
	here is `SparkContext.getExecutorMemoryStatus` and `SparkContext.getExecutorStorageStatus`. Calling them periodically would get you some of the way there.
	
2. [Spark runs out of memory when grouping by key](http://stackoverflow.com/questions/22637518/spark-runs-out-of-memory-when-grouping-by-key)

	I am attempting to perform a simple transformation of common crawl data using Spark host on an EC2 using this guide, my code looks like this:

	So my basic question is, what is necessary to write a Spark task that can group by key with an almost unlimited amount of input without running out of memory?
	
	The most common cause of java.lang.OutOfMemoryError exceptions in shuffle tasks (such as groupByKey, reduceByKey, etc.) is low level of parallelism.
	
3. [Running a function against every item in collection](http://stackoverflow.com/questions/23574379/running-a-function-against-every-item-in-collection)

	Since what you are trying to implement is actually some operation over a cartesian product, you might want to try just calling the `RDD#cartesian`.  Cartesian in user code.
	
4. [Spark OutOfMemory error on small text data](http://stackoverflow.com/questions/24394637/spark-outofmemory-error-on-small-text-data/24395160#24395160)

	I am working on implementing an algorithm and testing it on medium-sized data in Spark (the Scala interface) on a local node. I am starting with very simple processing and I'm getting java.lang.OutOfMemoryError: Java heap space even though I'm pretty sure the data isn't big enough for such an error to be reasonable. 
	
		val censusDataPreprocessed = censusData.map { row =>
  				val separators: Array[Char] = ":,".toCharArray
 				row.split(separators)
		}


		