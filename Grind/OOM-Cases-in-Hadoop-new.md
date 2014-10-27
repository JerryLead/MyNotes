# OOM Cases in Hadoop

## Large framework buffer
1. [out of Memory Error in Hadoop](http://stackoverflow.com/questions/8464048/out-of-memory-error-in-hadoop)  [StackOverflow]

	Large spill buffer, map phase
	
2. [Out of memory error in Mapreduce shuffle phase](http://stackoverflow.com/questions/19298357/out-of-memory-error-in-mapreduce-shuffle-phase)   [StackOverflow]

	Large soft buffer, shuffle phase
	
3. [pig join gets OutOfMemoryError in reducer when mapred.job.shuffle.input.buffer.percent=0.70](http://stackoverflow.com/questions/17162679/pig-join-gets-outofmemoryerror-in-reducer-when-mapred-job-shuffle-input-buffer-p/18227433#18227433)   [StackOverflow]

	Large soft buffer, shuffle phase

4. [CDH 4.1: Error running child : java.lang.OutOfMemoryError: Java heap space](http://stackoverflow.com/questions/13674190/cdh-4-1-error-running-child-java-lang-outofmemoryerror-java-heap-space)   [StackOverflow]

	One could also try setting the mapred.job.shuffle.input.buffer.percent to 20%. By default, this is set to 70%, which could be a lot if you are working on a very large set of data.
	
## Improper data partition

1. [Reducer's Heap out of memory](http://stackoverflow.com/questions/8705911/reducers-heap-out-of-memory)     [StackOverflow]
	Large soft buffer, shuffle phase, add reducer number, there is not any hotspots with bad key distribution.

## HotSpot Key

1. [Building inverted index](http://lintool.github.io/MapReduceAlgorithms/MapReduce-book-final.pdf) at Page 77 [JimmyLin]
	
	Since some terms like 'the' occur in too many documents, its posting list is very long. The OOM occurs in reduce(term, list<docid>), which first store the long list<docid> and then sort it to produce a sorted posting list.
	
2. [Reducer's Heap out of memory-Join](http://stackoverflow.com/questions/8705911/reducers-heap-out-of-memory)  [StackOverflow]
	Hot spot key, reduce phase. For example, say you are doing some sort of join and one of those keys shows up 50% of the time. Whatever reducer gets lucky to handle that key is going to get clobbered. You may want to investigate which keys are causing hot spots and handle them accordingly. In my data, usually these hot spots are useless anyways. To find out what's hot, just do a GROUP BY and COUNT and figure out what's showing up a lot. Then, if it's not useful, just FILTER it out.

3. [Hot spot value in UDF](http://stackoverflow.com/questions/8705911/reducers-heap-out-of-memory)  [StackOverflow]
	Another source of this problem is a Java UDF that is aggregating way too much data. For example, if you have a UDF that goes through a data bag and collects the records into some sort of list data structure, you may be blowing your memory with a hot spot value.
	
4. [Efficient Sharded Positional Indexer](http://www.cs.cmu.edu/~lezhao/TA/2010/HW2/)  [Developer]
For frequent terms such as "the", the reducer output record may exceed the memory limit of the JVM, resulting in out of memory error. This is because Hadoop keeps the whole record (in this case the whole postings list for "the") in memory before sending it to disk. 

## Large external data

1. [Hive Map join : out of memory Exception](http://stackoverflow.com/questions/18913928/hive-map-join-out-of-memory-exception)  [StackOverflow]
	Large table cached in memory,  one big Table (10G) and small Table (230 MB). Is the small table in the join really the smaller table in your data? 

2. [hadoop mapper over consumption of memory(heap)](http://stackoverflow.com/questions/15316539/hadoop-mapper-over-consumption-of-memoryheap)  [StackOverflow]
	has source code, Large table cached in memory
	
3. [“GC overhead limit exceeded” when trying to run Mahout testclassifier on Hadoop](http://stackoverflow.com/questions/22227142/gc-overhead-limit-exceeded-when-trying-to-run-mahout-testclassifier-on-hadoop/22228003#22228003)  [StackOverflow]
	in setConf() in map phase, large training data (feature matrix) is read into the memory.
	
4. [Hive: Whenever it fires a map reduce it gives me this error “Can not create a Path from an empty string”, how do I debug?](http://stackoverflow.com/questions/24564357/hive-whenever-it-fires-a-map-reduce-it-gives-me-this-error-can-not-create-a-pa/24565151#24565151)  [StackOverflow]
	I looked up the log file and in my case the table is an external table referring to a directory located on hdfs. This directory contains more than 300000 files. So while reading the files it was throwing an out of memory exception and may be for this reason it was getting an empty string and throwing 'Can not create a Path from an empty string' exception.
	
5. [OutOfMemory Error when running the wikipedia bayes example on mahout](http://stackoverflow.com/questions/10080800/outofmemory-error-when-running-the-wikipedia-bayes-example-on-mahout/10082340#10082340)  [StackOverflow]
	map() reads feature matrix into memory.
	
6. [Why is my PIG script failing?](http://stackoverflow.com/questions/22387859/why-is-my-pig-script-failing)  [StackOverflow]
	map join,
	
		 I = JOIN D BY $0, T BY $0 USING 'replicated';


7. [Replicated Join]() at Page 122 [MapReducePatterns]

	During the setup phase of the mapper, the user data (a large table) is read from the DistributedCache and then stored in memory (HashMap) as a lookup table. The data will be inflated due to Java object overhead.
	
## Large intermediate results
1. [Word-Cooccurrence](http://lintool.github.io/MapReduceAlgorithms/MapReduce-book-final.pdf) at Page 54 [JimmyLin]
	
	Input pair: \<docid, docTerms\>. Each term has a in-memory associative array, which holds the neighbors of its term. Since there are too many different neighbors for some terms, OOM occurs while the neighbors are put into the associative array.

2. [million of map outputs for one map input. is it efficient?](http://stackoverflow.com/questions/12466527/million-of-map-outputs-for-one-map-input-is-it-efficient)  [StackOverflow]

	Too large the record, the user treats the whole file as a record and trigger the OOM error while processing it.

3. [Standford NLP: java.lang.OutOfMemoryError on running Hadoop job](http://stackoverflow.com/questions/20247185/java-lang-outofmemoryerror-on-running-hadoop-job)  [StackOverflow]

	map phase, lemmatize(value) generates too large objects.  
	
	The whole of the piece of text that you provide here will be tokenized and processed in memory. In tokenized and processed form, it is over an order of magnitude larger than its size on disk.
	
	the POS tagger (which precedes the lemmatization) is annotating a sentence at a time, and it uses large temporary dynamic programming data structures for tagging a sentence, which might be 3 orders of magnitude larger in size than the sentence.

4. [Am I spawning more threads then I think I am in my mapper?](http://stackoverflow.com/questions/17707883/am-i-spawning-more-threads-then-i-think-i-am-in-my-mapper)  [StackOverflow]

 	map phase, value of the record is a  URL, whlie map() generates 8 threads to crawl the new URLs and put them into the buffer (URLPile)
 	
## Large accumulated results

1. [In-mapper combining WordCount](http://lintool.github.io/MapReduceAlgorithms/MapReduce-book-final.pdf) at Page 45 [JimmyLin]

	In-memory HashMap in map() holds too many input key-value paris.

2. [Building inverted index](http://lintool.github.io/MapReduceAlgorithms/MapReduce-book-final.pdf) at Page 77 [JimmyLin]
	
	Since some terms like 'the' occur in too many documents, its posting list is very long. The OOM occurs in reduce(term, list<docid>), which first store the long list<docid> and then sort it to produce a sorted posting list.
	
3. [Nested DISTINCT is a killer](http://mail-archives.apache.org/mod_mbox/pig-user/201201.mbox/%3CD570DEB688737C44A53497A16D0A7CAC4390DE@EAGF-ERFPMBX42.ERF.thomson.com%3E)  [StackOverflow]

	Nested distincts are dangerous. They are not done in a distributed fashion, they have to be loaded into memory. So that is what is killing it, not the order/limit. The alternative is to do two groups, first group by (citeddocid,CitingDocids) to get the distinct and then by citeddocid. to get the count.
	
4. [ORDER ... LIMIT failing on large data](https://mail-archives.apache.org/mod_mbox/pig-user/201201.mbox/%3CCAKne9Z5unW03bk2qbyXNxBsevmLcBVY1Se8_7TsDmDMEdHKh8A@mail.gmail.com%3E)  [StackOverflow]

	Nested distincts are dangerous. They are not done in a distributed fashion, they have to be loaded into memory. So that is what is killing it, not the order/limit. The alternative is to do two groups, first group by (citeddocid,CitingDocids) to get the distinct and then by citeddocid. to get the count.

5. [Interesting: Out of memory due to hash maps used in map-side aggregation](http://stackoverflow.com/questions/16684712/out-of-memory-due-to-hash-maps-used-in-map-side-aggregation)  [StackOverflow]

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

6. [Hadoop map-reduce : Order of records while grouping](http://stackoverflow.com/questions/15144578/hadoop-map-reduce-order-of-records-while-grouping/15146314#15146314)  [StackOverflow]

	try to sort a group 
	
7. [How to replace one column with an alias using Hadoop?](http://stackoverflow.com/questions/20808044/how-to-replace-one-column-with-an-alias-using-hadoop)  [StackOverflow]

	All the value objects are cached in reducer before seeing the alias object.

8. [What is the most effective way to find distinct of columns in hadoop](http://stackoverflow.com/questions/15045753/what-is-the-most-effective-way-to-find-distinct-of-columns-in-hadoop/15070770#15070770)  [StackOverflow]

	use Java Set to deduplicate the records.
	
9. [Fail to join large groups](http://stackoverflow.com/questions/22281188/fail-to-join-large-groups)  [StackOverflow]

	reduce-join in reduce(), large group, source code
	
		data_1_group = group data_1 by $1.record1; 
		data_2_group = group data_2 by $1.record1; 
		jj = join data_1_group by group, data_2_group by group;

10. [Why does the last reducer stop with java heap error during merge step](http://stackoverflow.com/questions/15541900/why-does-the-last-reducer-stop-with-java-heap-error-during-merge-step)  [StackOverflow]

	reduce-join in reduce(), large group, source code
	
		ArrayList<Text> valuesList = new ArrayList<Text>();
		while(ite.hasNext()) {
			Text t = ite.next();
			Text txt = new Text();
			txt.set(t.toString());
			valuesList.add(txt);
		}
		
	I will have lots and lots of values associated with a single key inside the reducer. 
	
11. [OOM exception in Hadoop Reduce child](http://stackoverflow.com/questions/12831076/oom-exception-in-hadoop-reduce-child)   [StackOverflow]
	All values in a group are appended into a StringBuilder. 
	
		StringBuilder adjVertexStr = new StringBuilder();
		long itcount= 0;
		while(values.hasNext()) {
			adjVertexStr.append(values.next().toString()).append(" ");
			itcount++;
		}
	
	
### Span multiple groups

1. [Getting java heap space error while running a mapreduce code for large dataset](http://stackoverflow.com/questions/23042829/getting-java-heap-space-error-while-running-a-mapreduce-code-for-large-dataset) [StackOverflow]

	But the reducer number is only one.
2. [