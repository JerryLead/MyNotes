# Experiments

## map phase
### 1. [Grep keyword](http://stackoverflow.com/questions/8464048/out-of-memory-error-in-hadoop/) (large buffer)

### 2. [MemWordCount](http://puffsun.iteye.com/blog/1902837) (large map-level objects)

- kv buffer = 500MB

- Rerun job :

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	| 1 | 0 |
	| 1885 | 92,036,792 |
	| 3769 | 174,789,544 |
	| 5653 | 259,954,488 |
	| 7537 | 345,406,000 | 
	| 9425 | 420,835,528 |
	| OOM => 9425 | 423,091,448 |

- Rerun job, only processes the last (9425th) record

	While processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	| 80,032  | 128,504 |

- Size of the last record (9425th record)

	| Key: LongWritable | Value: Text | 
	|----------------:|------------------:|
	| 24 B | 151,984 B |

### 3. [NLPLibrary](http://stackoverflow.com/questions/20247185/java-lang-outofmemoryerror-on-running-hadoop-job) (large intermediate computing results)

- kvbuffer: 500MB

- Rerun job :

	| begins to process i-th record | Size(uObjects) |  Object | 
	|----------------:|------------------:|----------------:|
	| 1 | 110,183,464 | edu.standord.nlp. pipeline.POSTaggerAnnotator |
	| 3  |110,184,720 | |
	| 5 | 110,184,720 | |
	| 7 | 110,184,720 | |
	| 9 | 110,184,720 | |
	| OOM => 9 | 402,918,776 |
	
- Rerun job, only processes the last (9st) record

	While processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	| 110,184,720 | 402,918,776 |

- Size of the last record (9th record)

	| Key: IntWritable | Value: org.apache.pig.data.BinSedesTuple | 
	|----------------:|------------------:|
	| 16 B | 9,076,048 B |
	
### 4. [PigMapJoin](http://mail-archives.apache.org/mod_mbox/pig-user/201202.mbox/%3CCAC3v_-opCCe8TipMfbOm0z7AK9ee0_rPgtGfC3gBXOz-s14J2A@mail.gmail.com%3E) (large external data)
	
- Rerun job :

	| Bytes read from disk | Size(uObjects) | 
	|----------------:|------------------:|
	| 63,746,048 | 521,211,128 | 
	| 135,704,576  | 693,551,104 | 
	| 206,819,328 | 1,028,338,784 | 
	| 244,887,552 | 1,186,304,896 | 
	| 251,080,704 | 1,221,481,328 | 

### 5. [Mahout classifier](http://stackoverflow.com/questions/10080800/outofmemory-error-when-running-the-wikipedia-bayes-example-on-mahout) (large external data)

- Rerun job :

	| Bytes read from disk | Size(uObjects) | 
	|----------------:|------------------:|
	| 30,193,493 | 99,259,664 | 
	| 32,565,153  |116,554,032 | 
	| 61,818,883 | 200,828,464 | 
	| 71,302,477| 219,277,040 | 
	| 104,461,660 | 393,230,760 | 
	| 116,007,939 | 426,268,640 |

## Spill

### 6. [Pig Count(distinct)](http://mail-archives.apache.org/mod_mbox/incubator-pig-user/201106.mbox/%3CC871EE502203224587F01DD2CF6634A6038A6DF4@TSHUSMNNADMBX03.ERF.THOMSON.COM%3E) (large group)

- kvbuffer: 600MB

- Rerun job in 263rd group:

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	| 1 | 0 |
	| 149,587 | 62,506,440 |
	| 299,173 | 114,967,480 |
	| 448,759 | 140,306,040 | 
	| 598,345 | 162,076,232 |
	| 747,932 | 186,186,928 |
	| OOM => 747,932 | 388,068,360 | 

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
### 7. [ShuffleOOM](https://issues.apache.org/jira/browse/MAPREDUCE-5580) (large buffer)
### 8. [Count(distinct 2)](http://mail-archives.apache.org/mod_mbox/incubator-pig-user/201201.mbox/%3CD570DEB688737C44A53497A16D0A7CAC4390DE@EAGF-ERFPMBX42.ERF.thomson.com%3E) (bad case, large group)

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

### 9. [ProcessFreebase](http://stackoverflow.com/questions/15541900/why-does-the-last-reducer-stop-with-java-heap-error-during-merge-step/) (large group)

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

- Rerun job, processing  the independent 6364863rd record

	while processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| begin to process the last record | while processing the last record | 
	|----------------:|------------------:|
	|  0 | 320 + 216 + 72 B |



- Size of the last record (21st record)

	| Key: reducer.ReducePhaseOOM$TextPair | Value: reducer.ReducePhaseOOM$TextPair| 
	|----------------:|------------------:|
	|   72 B | 216 B |

### 10. [CooccurMatrix](http://mail-archives.apache.org/mod_mbox/hadoop-common-user/201010.mbox/%3CAANLkTi=aNjiUezv-a9yFZpbXXWFsbjeKKyd2KmqCUAWc@mail.gmail.com%3E) (large group)

- Rerun job in 3,897,853rd group:

	| begins to process i-th record | Size(uObjects) | 
	|----------------:|------------------:|
	| 1 | 0 |
	| 4 | 89,160,424 |
	| 7 | 146,957,744 |
	| 10 | 184,394,120 | 
	| 13 | 219,994,928 |
	| 17 | 300,900,952 |
	| OOM => 17 | 422,184,304 | 

- Rerun job, processing  the independent 17th record

	while processing the last record means the time point when user code begins to output the record or the next record is read in. 

	| after read the last record | after processed the last record | 
	|----------------:|------------------:|
	| 31,806,544 B  | 31,806,944 B |

- Size of the last record (21st record)

	| Key: Text | Value: edu.umd.cloud9.io.fastuil.String2IntOpenHashMapWritable | 
	|----------------:|------------------:|
	|  760 B | 31,806,544 B |

