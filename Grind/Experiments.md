# Experiments

## map phase
1. [Grep keyword](http://stackoverflow.com/questions/8464048/out-of-memory-error-in-hadoop/) (large buffer)

2. [MemWordCount](http://puffsun.iteye.com/blog/1902837) (large map-level objects)
3. [NLPLibrary](http://stackoverflow.com/questions/20247185/java-lang-outofmemoryerror-on-running-hadoop-job) (large intermediate computing results)


4. [Mahout classifier](http://stackoverflow.com/questions/10080800/outofmemory-error-when-running-the-wikipedia-bayes-example-on-mahout) (large external data)

## Spill
1. [Pig Count(distinct)](http://mail-archives.apache.org/mod_mbox/incubator-pig-user/201106.mbox/%3CC871EE502203224587F01DD2CF6634A6038A6DF4@TSHUSMNNADMBX03.ERF.THOMSON.COM%3E) (large group)


- Rerun job in 263rd group:

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	| 1 | 0 |
	| 149,587 | 31,506,440 |
	| 299,173 | 57,967,480 |
	| 448,759 | 70,306,040 | 
	| 598,345 | 81,076,232 |
	| 747,932 | 93,186,928 |
	| OOM => 747,932 | 194,068,360 | 

- Rerun job, processing  the independent 747,932nd record

	while processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	| 94,328 (PigCombine$Combine) | 94,408 (PigCombiner$Combine) |

- Size of the last record (747,932nd record)

	| Key: IntWritable | Value: org.apache.pig.data.BinSedesTuple | 
	|----------------:|------------------:|
	| 16 B | 248 B |

## Shuffle
1. [ShuffleOOM](https://issues.apache.org/jira/browse/MAPREDUCE-5580) (large buffer)
2. [Count(distinct 2)](http://mail-archives.apache.org/mod_mbox/incubator-pig-user/201201.mbox/%3CD570DEB688737C44A53497A16D0A7CAC4390DE@EAGF-ERFPMBX42.ERF.thomson.com%3E) (bad case, large group)

- In-memory intermedaite data:  
918,931,848
- Rerun job in 1st group:

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	| 1 | 0 |
	| 5 | 76,259,576 |
	| 9 | 130,406,095 |
	| 13 | 230,697,037 | 
	| 17 | 270,942,349 |
	| 21 | 353,025,192 |
	| OOM => 21 | 750,166,065 | 

- Rerun job, processing  the independent 21st record

	while processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	| 94,328 (PigCombine$Combine) | 94,408 (PigCombiner$Combine) |

- Size of the last record (21st record)

	| Key: IntWritable | Value: org.apache.pig.data.BinSedesTuple | 
	|----------------:|------------------:|
	| 16 B | 248 B |
	
## Reduce
1. [TextProcessor](http://stackoverflow.com/questions/15541900/why-does-the-last-reducer-stop-with-java-heap-error-during-merge-step/) (large group)
2. [PigReduceJoin](http://stackoverflow.com/questions/22281188/fail-to-join-large-groups) (large group)
3. [CooccurMatrix](http://mail-archives.apache.org/mod_mbox/hadoop-common-user/201010.mbox/%3CAANLkTi=aNjiUezv-a9yFZpbXXWFsbjeKKyd2KmqCUAWc@mail.gmail.com%3E) (large group)