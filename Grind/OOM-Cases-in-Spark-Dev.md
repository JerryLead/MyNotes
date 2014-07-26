# OOM Cases in Spark-dev
## [Apache Spark Developers List](http://apache-spark-developers-list.1001551.n3.nabble.com/)

Found 24 matching posts for oom in Apache Spark Developers [List](http://apache-spark-developers-list.1001551.n3.nabble.com/template/NamlServlet.jtp?macro=search_page&node=1&query=oom).

Labels:

- Driver (Dr): error occurs in driver
- Executor (Ex): error occurs in executor
- Solved (S): this problem has been solved
- Unsolved (U):
	- R: we can reproduce the problem for further study  
	- D: just description which cannot be reproduced
- V: valuable 

## Spark-dev 
1. [oome from large map output status](http://apache-spark-developers-list.1001551.n3.nabble.com/oome-from-large-map-output-status-td1851.html)

	It's sent via an Akka message, so, a) 49mb is over the default 
Akka frame size of 10mb (we'd already upped ours) and b) the byte[] 
gets copied into a new byte[] for each slave/executor asking for it. 
Plus a few more copies seem to have in the Netty/NIO stack. 
2. [Eliminate copy while sending data : any Akka experts here ?](http://apache-spark-developers-list.1001551.n3.nabble.com/Eliminate-copy-while-sending-data-any-Akka-experts-here-td7127.html)

	While sending map output tracker result, the same serialized byte 
array is sent multiple times - but the akka implementation copies it 
to a private byte array within ByteString for each send. 
3. [Apache spark on 27gb wikipedia data](http://apache-spark-developers-list.1001551.n3.nabble.com/Apache-spark-on-27gb-wikipedia-data-td6487.html#a6488)

	Although it runs fne for around 300Mb data set, it runs in to issues when I try to execute the same code using the 27gb data from hdfs. 
The error thrown is given below: 
14/05/05 07:15:22 WARN scheduler.TaskSetManager: Loss was due to java.lang.OutOfMemoryError 

## Related questions
1. [bug using kryo as closure serializer](http://apache-spark-developers-list.1001551.n3.nabble.com/bug-using-kryo-as-closure-serializer-td6473.html#a6477)

	Particularly given the bugs Patrick and I had looked into in past 
along flush, etc I was always skeptical about using kyro. 
But given the pretty nasty issues with OOM's via java serialization we 
are seeing, wanted to know your thoughts on use of kyro with spark. 