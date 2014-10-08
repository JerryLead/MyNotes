# Experiments

## map phase
1. [Grep keyword](http://stackoverflow.com/questions/8464048/out-of-memory-error-in-hadoop/) (large buffer)

2. [MemWordCount](http://puffsun.iteye.com/blog/1902837) (large map-level objects)



3. [NLPLibrary](http://stackoverflow.com/questions/20247185/java-lang-outofmemoryerror-on-running-hadoop-job) (large intermediate computing results)

- kvbuffer: 500MB

- Rerun job :

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	| 1 | 0 |
	| 3  |0 |
	| 5 | 0 |
	| 7 | 0 | 
	| 9 | 0 |
	| OOM => 9 | 402,918,776 |
	
- Rerun job, only processes the last (747,932nd) record

	While processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	| 52,428,928 | 402,918,776 |

- Size of the last record (747,932nd record)

	| Key: IntWritable | Value: org.apache.pig.data.BinSedesTuple | 
	|----------------:|------------------:|
	| 16 B | 304 B |
	
4. [Mahout classifier](http://stackoverflow.com/questions/10080800/outofmemory-error-when-running-the-wikipedia-bayes-example-on-mahout) (large external data)

## Spill

1. [Pig Count(distinct)](http://mail-archives.apache.org/mod_mbox/incubator-pig-user/201106.mbox/%3CC871EE502203224587F01DD2CF6634A6038A6DF4@TSHUSMNNADMBX03.ERF.THOMSON.COM%3E) (large group)

- kvbuffer: 600MB

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

- Rerun job, only processes the last (747,932nd) record

	While processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	| 94,328 (PigCombine$Combine) | 94,408 (PigCombiner$Combine) |

- Size of the last record (747,932nd record)

	| Key: IntWritable | Value: org.apache.pig.data.BinSedesTuple | 
	|----------------:|------------------:|
	| 16 B | 304 B |

## Shuffle
1. [ShuffleOOM](https://issues.apache.org/jira/browse/MAPREDUCE-5580) (large buffer)
2. [Count(distinct 2)](http://mail-archives.apache.org/mod_mbox/incubator-pig-user/201201.mbox/%3CD570DEB688737C44A53497A16D0A7CAC4390DE@EAGF-ERFPMBX42.ERF.thomson.com%3E) (bad case, large group)

- In-memory intermedaite data:  
918,931,848
- Rerun job in 1st group:

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	|1 | 0 |
	| 5 |  101,259,576 |
	|  9 |  246,406,095| 
	| 13 | 298,697,037 | 
	| 17| 408,942,349 | 
	| 21| 503,025,192 | 
	| OOM => 21| 1,050,166,065 | 

- Rerun job, processing  the independent 21st record

	while processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	|  32,234,256  (PigCombine$Combine) | 37,021,312 (PigCombiner$Combine) |

- Size of the last record (21st record)

	| Key: IntWritable | Value: org.apache.pig.data.BinSedesTuple | 
	|----------------:|------------------:|
	| 16 B | 120,457,968 B |
	
## Reduce
1. [TextProcessor](http://stackoverflow.com/questions/15541900/why-does-the-last-reducer-stop-with-java-heap-error-during-merge-step/) (large group)
2. [PigReduceJoin](http://stackoverflow.com/questions/22281188/fail-to-join-large-groups) (large group)

- Rerun job in 1st group:

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	| 1 | 0 |
	| 1068023 | 184,549,440 |
	| 2136045 | 366,073,088 |
	| 3204067 | 549,082,552 | 
	| 4272089 | 734,379,208 |
	| 5340116 | 922,989,280|
	| 6364863 | 1,094,168,776 | 
	| OOM => 6364863 | 1,094,241,536 |

- Rerun job, processing  the independent 21st record

	while processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	|  0 | 320 + 216 + 72 B |



- Size of the last record (21st record)

	| Key: reducer.ReducePhaseOOM$TextPair | Value: reducer.ReducePhaseOOM$TextPair| 
	|----------------:|------------------:|
	|   72 B | 216 B |

3. [CooccurMatrix](http://mail-archives.apache.org/mod_mbox/hadoop-common-user/201010.mbox/%3CAANLkTi=aNjiUezv-a9yFZpbXXWFsbjeKKyd2KmqCUAWc@mail.gmail.com%3E) (large group)

- Rerun job in 3,897,853rd group:

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	| 1 | 0 |
	| 4 | 89,160,424 |
	| 7 | 146,957,744 |
	| 10 | 184,394,120 | 
	| 13 | 219,994,928 |
	| 17 | 300,900,952 |
	| OOM => 17 | 376,398,384 | 

- Rerun job, processing  the independent 21st record

	while processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| after read the last record | after processed the last record | 
	|----------------:|------------------:|
	|  41,976,800 B  | 41,977,200 B |

- Size of the last record (21st record)

	| Key: Text | Value: edu.umd.cloud9.io.fastuil.String2IntOpenHashMapWritable | 
	|----------------:|------------------:|
	|  760 B | 41,976,800 B |

