# Experiments

## map phase
1. [Grep keyword](http://stackoverflow.com/questions/8464048/out-of-memory-error-in-hadoop/) (large buffer)

2. [MemWordCount](http://puffsun.iteye.com/blog/1902837) (large map-level objects)
3. [NLPLibrary](http://stackoverflow.com/questions/20247185/java-lang-outofmemoryerror-on-running-hadoop-job) (large intermediate computing results)
4. [Mahout classifier](http://stackoverflow.com/questions/10080800/outofmemory-error-when-running-the-wikipedia-bayes-example-on-mahout) (large external data)

## Spill
1. [Pig Count(distinct)](http://mail-archives.apache.org/mod_mbox/incubator-pig-user/201106.mbox/%3CC871EE502203224587F01DD2CF6634A6038A6DF4@TSHUSMNNADMBX03.ERF.THOMSON.COM%3E) (large group)

## Shuffle
1. [ShuffleOOM](https://issues.apache.org/jira/browse/MAPREDUCE-5580) (large buffer)
2. [Count(distinct 2)](http://mail-archives.apache.org/mod_mbox/incubator-pig-user/201201.mbox/%3CD570DEB688737C44A53497A16D0A7CAC4390DE@EAGF-ERFPMBX42.ERF.thomson.com%3E) (bad case, large group)

## Reduce
1. [TextProcessor](http://stackoverflow.com/questions/15541900/why-does-the-last-reducer-stop-with-java-heap-error-during-merge-step/) (large group)
2. [PigReduceJoin](http://stackoverflow.com/questions/22281188/fail-to-join-large-groups) (large group)
3. [CooccurMatrix](http://mail-archives.apache.org/mod_mbox/hadoop-common-user/201010.mbox/%3CAANLkTi=aNjiUezv-a9yFZpbXXWFsbjeKKyd2KmqCUAWc@mail.gmail.com%3E) (large group)