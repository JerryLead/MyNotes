# OOM Cases in Hadoop

## Large framework buffer

1. [out of Memory Error in Hadoop](http://stackoverflow.com/questions/8464048/out-of-memory-error-in-hadoop)  
	Large spill buffer, map phase
2. [Out of memory error in Mapreduce shuffle phase](http://stackoverflow.com/questions/19298357/out-of-memory-error-in-mapreduce-shuffle-phase)  
	Large soft buffer, shuffle phase
3. [Shuffle In Memory OutOfMemoryError](http://hadoop-common.472056.n3.nabble.com/Shuffle-In-Memory-OutOfMemoryError-td433197.html)  
	Large soft buffer, shuffle phase
4. [Reducer's Heap out of memory](http://stackoverflow.com/questions/8705911/reducers-heap-out-of-memory)  
	Large soft buffer, shuffle phase, add reducer number, there is not any hotspots with bad key distribution.
5. [Why the identity mapper can get out of memory?](http://stackoverflow.com/questions/12302708/why-the-identity-mapper-can-get-out-of-memory)  
	shuffle phase, I realized that looking deep at the OOM traces. The exceptions were raised in functions of Hadoop related with shuffling.
6. [hive error run select query](http://stackoverflow.com/questions/16152726/hive-error-run-select-query/16153533#16153533)
	large hard buffer, map phase
7. [pig join gets OutOfMemoryError in reducer when mapred.job.shuffle.input.buffer.percent=0.70](http://stackoverflow.com/questions/17162679/pig-join-gets-outofmemoryerror-in-reducer-when-mapred-job-shuffle-input-buffer-p/18227433#18227433)  
	Large soft buffer, shuffle phase
	
8. [CDH 4.1: Error running child : java.lang.OutOfMemoryError: Java heap space](http://stackoverflow.com/questions/13674190/cdh-4-1-error-running-child-java-lang-outofmemoryerror-java-heap-space)  
	One could also try setting the mapred.job.shuffle.input.buffer.percent to 20%. By default, this is set to 70%, which could be a lot if you are working on a very large set of data.

## Hot spot of  a particular key
1. [Reducer's Heap out of memory-Join](http://stackoverflow.com/questions/8705911/reducers-heap-out-of-memory)  
	Hot spot key, reduce phase. For example, say you are doing some sort of join and one of those keys shows up 50% of the time. Whatever reducer gets lucky to handle that key is going to get clobbered. You may want to investigate which keys are causing hot spots and handle them accordingly. In my data, usually these hot spots are useless anyways. To find out what's hot, just do a GROUP BY and COUNT and figure out what's showing up a lot. Then, if it's not useful, just FILTER it out.

2. [Hot spot value in UDF](http://stackoverflow.com/questions/8705911/reducers-heap-out-of-memory)  
	Another source of this problem is a Java UDF that is aggregating way too much data. For example, if you have a UDF that goes through a data bag and collects the records into some sort of list data structure, you may be blowing your memory with a hot spot value.
	
	
## Large external data
1. [Hive Map join : out of memory Exception](http://stackoverflow.com/questions/18913928/hive-map-join-out-of-memory-exception)  
	Large table cached in memory,  one big Table (10G) and small Table (230 MB). Is the small table in the join really the smaller table in your data? 

2. [hadoop mapper over consumption of memory(heap)](http://stackoverflow.com/questions/15316539/hadoop-mapper-over-consumption-of-memoryheap)  
	has source code, Large table cached in memory
	
3. [“GC overhead limit exceeded” when trying to run Mahout testclassifier on Hadoop](http://stackoverflow.com/questions/22227142/gc-overhead-limit-exceeded-when-trying-to-run-mahout-testclassifier-on-hadoop/22228003#22228003)  
	in setConf() in map phase, large training data (feature matrix) is read into the memory.
	
4. [Hive: Whenever it fires a map reduce it gives me this error “Can not create a Path from an empty string”, how do I debug?](http://stackoverflow.com/questions/24564357/hive-whenever-it-fires-a-map-reduce-it-gives-me-this-error-can-not-create-a-pa/24565151#24565151)  
	I looked up the log file and in my case the table is an external table referring to a directory located on hdfs. This directory contains more than 300000 files. So while reading the files it was throwing an out of memory exception and may be for this reason it was getting an empty string and throwing 'Can not create a Path from an empty string' exception.
	
5. [OutOfMemory Error when running the wikipedia bayes example on mahout](http://stackoverflow.com/questions/10080800/outofmemory-error-when-running-the-wikipedia-bayes-example-on-mahout/10082340#10082340)  
	map() reads feature matrix into memory.
	
6. [Why is my PIG script failing?](http://stackoverflow.com/questions/22387859/why-is-my-pig-script-failing)  
	map join,
	
		 I = JOIN D BY $0, T BY $0 USING 'replicated';
		 
		 
## Large intermediate computing results
1. [million of map outputs for one map input. is it efficient?](http://stackoverflow.com/questions/12466527/million-of-map-outputs-for-one-map-input-is-it-efficient)  
	treat the whole file as a record and trigger the OOM error while processing it.

2. [Standford NLP: java.lang.OutOfMemoryError on running Hadoop job](http://stackoverflow.com/questions/20247185/java-lang-outofmemoryerror-on-running-hadoop-job)  
	map phase, lemmatize(value) generates too large objects.  
	
	The whole of the piece of text that you provide here will be tokenized and processed in memory. In tokenized and processed form, it is over an order of magnitude larger than its size on disk.
	
	the POS tagger (which precedes the lemmatization) is annotating a sentence at a time, and it uses large temporary dynamic programming data structures for tagging a sentence, which might be 3 orders of magnitude larger in size than the sentence. 
	
3. [Am I spawning more threads then I think I am in my mapper?](http://stackoverflow.com/questions/17707883/am-i-spawning-more-threads-then-i-think-i-am-in-my-mapper)  
 	map phase, value of the record is a  URL, whlie map() generates 8 threads to crawl the new URLs and put them into the buffer (URLPile)
 	
## Large accumulated computing results
1. [Nested DISTINCT is a killer](http://mail-archives.apache.org/mod_mbox/pig-user/201201.mbox/%3CD570DEB688737C44A53497A16D0A7CAC4390DE@EAGF-ERFPMBX42.ERF.thomson.com%3E)  
	Nested distincts are dangerous. They are not done in a distributed fashion, they have to be loaded into memory. So that is what is killing it, not the order/limit. The alternative is to do two groups, first group by (citeddocid,CitingDocids) to get the distinct and then by citeddocid. to get the count.
	
2. [ORDER ... LIMIT failing on large data](https://mail-archives.apache.org/mod_mbox/pig-user/201201.mbox/%3CCAKne9Z5unW03bk2qbyXNxBsevmLcBVY1Se8_7TsDmDMEdHKh8A@mail.gmail.com%3E)  
	Nested distincts are dangerous. They are not done in a distributed fashion, they have to be loaded into memory. So that is what is killing it, not the order/limit. The alternative is to do two groups, first group by (citeddocid,CitingDocids) to get the distinct and then by citeddocid. to get the count.

3. [Interesting: Out of memory due to hash maps used in map-side aggregation](http://stackoverflow.com/questions/16684712/out-of-memory-due-to-hash-maps-used-in-map-side-aggregation)  
	large hash map used in map-side aggregation, map phase, Currently `hive.map.aggr.hash.percentmemory` is set to 0.5. Try setting it to a lower value. i.e `set hive.map.aggr.hash.percentmemory = 0.25`;
	
	    select 
	        uri, 
	        count(*) as hits 
	    from
	        iislog
	    where 
	        substr(cs_cookie,instr(cs_Cookie,'cwc'),30) like '%CWC%'
	    and uri like '%.aspx%' 
	    and logdate = '2013-02-07' 
	    group by uri 
	    order by hits Desc;
	    
	if mapper is not sorting: consider bumping the hash aggregate memory % as indicated in the log to a higher number. If mapper is sorting - just bump up task memory to a larger number. 

	I tried to debug the problem and it comes out that my mapper was using 5.5 gb of RAM.

4. [Hadoop map-reduce : Order of records while grouping](http://stackoverflow.com/questions/15144578/hadoop-map-reduce-order-of-records-while-grouping/15146314#15146314)  
	try to sort a group
	
5. [How to replace one column with an alias using Hadoop?](http://stackoverflow.com/questions/20808044/how-to-replace-one-column-with-an-alias-using-hadoop)  
	All the value objects are cached in reducer before seeing the alias object.

6. [What is the most effective way to find distinct of columns in hadoop](http://stackoverflow.com/questions/15045753/what-is-the-most-effective-way-to-find-distinct-of-columns-in-hadoop/15070770#15070770)  
	use Java Set to deduplicate the records.
	
7. [Fail to join large groups](http://stackoverflow.com/questions/22281188/fail-to-join-large-groups)  
	reduce-join in reduce(), large group, source code
	
		data_1_group = group data_1 by $1.record1; 
		data_2_group = group data_2 by $1.record1; 
		jj = join data_1_group by group, data_2_group by group;

8. [Fail to join large groups](http://stackoverflow.com/questions/22281188/fail-to-join-large-groups)  
	reduce-join in reduce(), large group, source code
	
	
## Unknown
1. [Will reducer out of java heap space](http://stackoverflow.com/questions/16116022/will-reducer-out-of-java-heap-space)  
	every reducer needs large sparse whole matrix, and I am not allowed to change this logic. Yet every reducer will receive an entry with column id as key, and column vector as value.Is there any way I can get out of this dilemma?
	
	K-means clustering also has same heap space problems, if the value of K is increasing.

	I've heard canopy-center vectors and k-center vectors are held in memory on every mapper and reducer. That would be num of `canopy center(or k) x sparsevector(300000 size)` = enough for 4g memory things, which doesn't seem too bad.

2. [Interesting: Mahout Canopy Clustering, K-means Clustering : Java Heap Space - out of memory](http://stackoverflow.com/questions/17058327/mahout-canopy-clustering-k-means-clustering-java-heap-space-out-of-memory)  
	reduce phase, data structure expansion, the jobs keep failing with a "Error: Java heap space" message at 67% of reduce phase.
	
3. [Interesting: How to run large Mahout fuzzy kmeans clustering without running out of memory?](http://stackoverflow.com/questions/16113102/how-to-run-large-mahout-fuzzy-kmeans-clustering-without-running-out-of-memory)
	map phase, data structure expansion, So 4 * (100000 entries) * (20 bytes/entry) * (128 clusters) = 1.024G. This algorithm is a memory hog.
	
4. [top-k in mapreduce when k elements do not fit in memory](http://stackoverflow.com/questions/24691990/top-k-in-mapreduce-when-k-elements-do-not-fit-in-memory)  
  only one reducer that holds all the top-k elements.
	
5. [org.apache.hadoop.mapred.TaskTracker: Error running child : java.lang.OutOfMemoryError: Java heap space](http://stackoverflow.com/questions/11140750/org-apache-hadoop-mapred-tasktracker-error-running-child-java-lang-outofmemor)  
	I am running a simple join query

		select count(*) from t1 join t2 on t1.sno=t2.sno
		
6. [hive query taking too long on external table](http://stackoverflow.com/questions/20362757/hive-query-taking-too-long-on-external-table)   
	CREATE EXTERNAL TABLE, and count(*)
	
7. [Maximum length of select statement in Hive](http://stackoverflow.com/questions/10992143/maximum-length-of-select-statement-in-hive)  
	running the following script
	
		select
		  count(distinct(col_name1  )),
		  count(distinct(col_name2  )),
		  count(distinct(col_name3  )),
		      .......... 
		  count(distinct(col_name804))
		from 
		  tab_name;
  
 8. [Out of heap error when creating Index in Apache Hive](http://stackoverflow.com/questions/25501502/out-of-heap-error-when-creating-index-in-apache-hive)  
	In order to speed up other types of queries we would however have liked to try adding an index to the table but when we execute the “alter” statement to actually build it this fails with "java.lang.OutOfMemoryError.
	
	
## Solutions:
1. for large group, if user code aggregate the large group for sort, they can redesign the key and then let it done with the help of MapReduce sort such as secondary sort.


## Interesting problems:
1. [How to select suitable value type in map function in hadoop?](http://stackoverflow.com/questions/15991855/how-to-select-suitable-value-type-in-map-function-in-hadoop/15993225#15993225)  
	I stored the value as text, but it gets 1 byte for each character.if the number of digits in id becomes large, it occupies a lot of space. do i store the value as text type? 

2. Dynamic partition

3. [Memory-efficient distributed approach to determining unique values?](http://stackoverflow.com/questions/23007984/memory-efficient-distributed-approach-to-determining-unique-values)

4. [Hadoop searching words from one file in another file](http://stackoverflow.com/questions/2128209/hadoop-searching-words-from-one-file-in-another-file)

5. [Hadoop: Heap space and gc problems](http://stackoverflow.com/questions/9703436/hadoop-heap-space-and-gc-problems)  
	I can say that i dont need more than 600MB of memory for every map task. But the thing is that after a while i have java heap space problems or gc overhead limit. I don't know how can this be possible.

6. [Records proactively spilled in Hadoop Pig?](http://stackoverflow.com/questions/12378925/records-proactively-spilled-in-hadoop-pig/12448040#12448040)  
	Pig's advance memory manager - Spillable Memory Manager

7. [Hadoop UniqValueCount Map and Aggregate Reducer for Large Dataset (1 billion records)](http://stackoverflow.com/questions/14404263/hadoop-uniqvaluecount-map-and-aggregate-reducer-for-large-dataset-1-billion-rec)  
	reducer receives too many values, <k, list(v)> group is too large
	
8. [Efficient way to delete multiple rows in HBase](http://stackoverflow.com/questions/4618980/efficient-way-to-delete-multiple-rows-in-hbase/22249241#22249241)  
			
		 List<Delete> deletes = new ArrayList<Delete>();
   		 int bufferSize = 10000000; // this is needed so I don't run out of memory as I have a huge amount of data ! so this is a simple in memory buffer
 
 9. [How to increase number of reducer in canopy clustering algorithm](http://stackoverflow.com/questions/25993572/how-to-increase-number-of-reducer-in-canopy-clustering-algorithm/25996314#25996314)  
	A single reducer is used to return canopy centers away from each other. Using more reducers would give wrong results.

10. [Hadoop Pipes: how to pass large data records to map/reduce tasks](http://stackoverflow.com/questions/4021828/hadoop-pipes-how-to-pass-large-data-records-to-map-reduce-tasks/4027315#4027315)  
	Talking about Hadoop pipeline.

11. [Detailed dataflow in hadoop's mapreduce?](http://stackoverflow.com/questions/19490723/detailed-dataflow-in-hadoops-mapreduce)  
	Talking about the dataflow which may cause OOM.

12. [In-depth understanding of internal working of map phase in a Map reduce job in hadoop?](http://stackoverflow.com/questions/24917886/in-depth-understanding-of-internal-working-of-map-phase-in-a-map-reduce-job-in-h/24918188#24918188)  
	Talking about the implementation of map phase.
	
13. [Hadoop Pig save each line of a file to S3](http://stackoverflow.com/questions/14065593/hadoop-pig-save-each-line-of-a-file-to-s3)  
	There are a lot of phone numbers (approximate 20,000), to store each phone number into different S3 buckets is very very slow and the program is even out of memory.

14. [Limit CPU / Stack for Java method call?](http://stackoverflow.com/questions/1081466/limit-cpu-stack-for-java-method-call)  
 	still about NLP library (Standford NER)
