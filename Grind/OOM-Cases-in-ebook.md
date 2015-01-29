# OOM cases in Ebooks
## OOM in MapReduce Design Patterns

### 1. Median and standard deviation

**[Pattern] Accumulated results and hotspot key**
The easiest way to perform these operations involves copying the list of values into a temporary list in order to find the median or iterating over the set again to determine the standard deviation. With large data sets, this implementation may result in Java heap space issues, because each value is copied into memory for every input group. 

Any sort of memory growth in the reducer has the possibility of blowing through the Java virtual machine’s memory. For example, if you are collecting all of the values into an ArrayList to perform a median, that ArrayList can get very big. This will not be a particular problem if you’re really looking for the top ten items, but if you want to extract a very large number you may run into memory limits.

With source code at  Page 25.

### 2. Replicated Join 

**[Pattern] Large external data**

A replicated join is an extremely useful, but has a strict size limit on all but one of the data sets to be joined. All the data sets except the very large one are essentially read into memory during the setup phase of each map task, which is limited by the JVM heap.

With source code at Page 119.

### 3. Cogroup in Pig [Page 75]

**[Pattern] Accumulated results and hotspot key**

The next major concern is the possibility of **hot spots in the data that could result in an obscenely large record.** With large data sets, it is conceivable that a particular output record is going to have a lot of data associated with it. Imagine that for some reason a post on StackOverflow has a million comments associated with it. That would be extremely rare and unlikely, but not in the realm of the impossible.  

With source code at Page 75.
### 4. Sort XML Object 

**[Pattern] Accumulated results**

**If you are building some sort of XML object, all of those comments at one point might be stored in memory before writing the object out.** This can cause you to blow out the heap of the Java Virtual Machine, which obviously should be avoided.

No source code, just error discription and root cause at Page 75.

### 5. ParserUserData

**[Pattern] Large external data**

During the setup phase of the mapper, the user data is read from the DistributedCache and stored in memory. Each record is parsed and the user ID is pulled out of the record. Then, the user ID and record are added to a HashMap for retrieval in the map method. This is where an out of memory error could occur, as the entire contents of the file is stored, with additional overhead of the data structure itself. If it does, you will either have to increase the JVM size or use a plain reduce side join.



## OOM in Data-Intensive Text Processing with MapReduce

### 1. Reduce-side Join

**[Pattern] Accumulated results**

All the tuples from S with the same join key will be encountered first, which the reducer can buffer in memory. As the reducer processes each tuple from T, it is crossed with all the tuples from S. Of course, we are assuming that the tuples from S (with the same join key) will fit into memory, which is a limitation of this algorithm (and why we want to control the sort order so that the smaller dataset comes first).

Without source code at Page 66. 

### 2. BuildInvertedIndex

**[Pattern] Accumulated results**

The inverted indexing algorithm presented in the previous section serves as a reasonable baseline. However, there is a significant scalability bottleneck: the algorithm assumes that there is sufficient memory to hold all postings associated with the same term. Since the basic MapReduce execution framework makes no guarantees about the ordering of values associated with the same key, the reducer first buffers all postings (line 5 of the reducer pseudo-code in Figure 4.2) and then performs an in-memory sort before writing the postings to disk.7 For efficient retrieval, postings need to be sorted by document id. However, as collections become larger, postings lists grow longer, and at some point in time, reducers will run out of memory.

inverted indexing is nothing but a very large distributed sort and group by operation! We began with a baseline implementation of an inverted indexing algorithm, but quickly noticed a scalability bottleneck that stemmed from having to buffer postings in memory. Application of the value-to-key conversion design pattern (Section 3.4) addressed the issue by offloading the task of sorting postings by document id to the MapReduce execution framework.

A two-pass solution that involves first buffering the postings (in memory) would suffer from the memory bottleneck we’ve been trying to avoid in the first place.

With source code at Page 77.
### 3. One-to-man join

**[Pattern] Accumulated results**

one-to-many join. Assume that tuples in S have unique join keys (i.e., k is the primary key in S), so that S is the “one” and T is the “many”. The above algorithm will still work, but when processing each key in the reducer, we have no idea when the value corresponding to the tuple from S will be encountered, since values are arbitrarily ordered. The easiest solution is to buffer all values in memory, pick out the tuple from S, and then cross it with every tuple from T to perform the join. However, as we have seen several times already, this creates a scalability bottleneck since we may not have sufficient memory to hold all the tuples with the same join key.


### 4. word co-occurrence

The computation of the word co-occurrence matrix is quite simple if the entire matrix fits into memory—however, in the case where the matrix is too big to fit in memory, a na ̈ıve implementation on a single machine can be very slow as memory is paged to disk. Although compression techniques can increase the size of corpora for which word co-occurrence matrices can be constructed on a single machine, it is clear that there are inherent scalability limitations. We describe two MapReduce algorithms for this task that can scale to large corpora.

This algorithm will indeed work, but it suffers from the same drawback as the stripes approach: as the size of the corpus grows, so does that vocabulary size, and at some point there will not be sufficient memory to store all co-occurring words and their counts for the word we are conditioning on. 

With source code at Page 59.

### 5. SortByKey

**[Pattern] Accumulated results**

However, since MapReduce makes no guarantees about the ordering of values associated with the same key, the sensor readings will not likely be in temporal order. The most obvious solution is to buffer all the readings in memory and then sort by timestamp before additional processing. However, it should be apparent by now that any in-memory buffering of data introduces a potential scalability bottleneck. What if we are working with a high frequency sensor or sensor readings over a long period of time? What if the sensor readings themselves are large complex objects? This approach may not scale in these cases—the reducer would run out of memory trying to buffer all values associated with the same key.

Without source code at Page 61.


### 6. In-memory combining

**[Pattern] Accumulated results, hotspot key**

For both algorithms, the in-mapper combining optimization discussed in the pre- vious section can also be applied; the modification is sufficiently straightforward that we leave the implementation as an exercise for the reader. However, the above caveats remain: there will be far fewer opportunities for partial aggregation in the pairs ap- proach due to the sparsity of the intermediate key space. The sparsity of the key space also limits the effectiveness of in-memory combining, since the mapper may run out of memory to store partial counts before all documents are processed, necessitating some mechanism to periodically emit key-value pairs (which further limits opportunities to perform partial aggregation). Similarly, for the stripes approach, memory management will also be more complex than in the simple word count example. **For common terms, the associative array may grow to be quite large**, necessitating some mechanism to periodically flush in-memory structures.

Without source code at Page 54.


## OOM in Mahout in action

### 1. GenericDataModel
**[Pattern] Large external data**

Run this code, and the first thing you’ll likely encounter is an OutOfMemoryError. Ah, a first sighting of issues of scale. 

The simplest DataModel implementation available is an in-memory implementation, GenericDataModel. It’s appropriate when you want to construct your data representa- tion in memory, programmatically, rather than base it on an existing external source of data, such as a file or relational database.

With source code at Page 46.

### 2. Canopy Clustering

Canopy clustering is a good approximate clustering technique, but it suffers from memory problems. If the distance thresholds are close, too many canopies are generated, and this increases memory usage in the mapper. This might exceed available memory while running on a large data set with a bad set of thresholds. The parame- ters need to be tuned to fit the data set and the clustering problem,

