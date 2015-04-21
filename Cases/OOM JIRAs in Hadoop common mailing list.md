
## OOM related JIRAs
1. [jira] Created: (HADOOP-7121) Exceptions while serializing IPC call response are not handled well
1. [jira] [Created] (HADOOP-8851) Use -XX:+HeapDumpOnOutOfMemoryError JVM option in the forked tests
1. [jira] [Created] (HADOOP-10940) RPC client does poor bounds checking of responses
1. [jira] [Created] (HADOOP-9558) Opening many small files with Zlib compression results in Out of Memory Exception when using Combined Input File Format for many small files
1. [jira] [Commented] (HADOOP-10357) Memory Leak in UserGroupInformation.doAs for JDBC Connection to Hive
1. [jira] Created: (HADOOP-6088) Task stuck in cleanup with OutOfMemoryErrors
1. [jira] Created: (HADOOP-5269) TaskTracker.runningTasks holding FAILED_UNCLEAN and KILLED_UNCLEAN taskStatuses forever in some cases.
1. [jira] [Commented] (HADOOP-10759) Remove hardcoded JAVA_HEAP_MAX in hadoop-config.sh
1. [jira] [Created] (HADOOP-8763) Set group owner on Windows failed
1. [jira] [Updated] (HADOOP-6490) Path.normalize should use StringUtils.replace in favor of String.replace
1. [jira] Commented: (HADOOP-1338) Improve the shuffle phase by using the "connection: keep-alive" and doing batch transfers of files
1. [jira] Created: (HADOOP-4797) RPC Server can leave a lot of direct buffers
1. [jira] [Updated] (HADOOP-10987) Provide an iterator-based listing API for FileSystem
1. [jira] Created: (HADOOP-5881) Simplify configuration related to task-memory-monitoring and memory-based scheduling
1. [jira] [Commented] (HADOOP-6963) Fix FileUtil.getDU. It should not include the size of the directory or follow symbolic links
1. [jira] Created: (HADOOP-6858) Enable rotateable JVM garbage collection logs for Hadoop daemons
1. [jira] [Commented] (HADOOP-11526) Memory leak in Bzip2Compressor and Bzip2Decompressor
1. [jira] [Resolved] (HADOOP-3978) Using regular desktops as hadoop slaves
1. [jira] Created: (HADOOP-4219) [mapred] Change TaskMemoryManager to use JvmIDs instead of TaskIDs for memory-tracking.
1. [jira] [Commented] (HADOOP-9912) globStatus of a symlink to a directory does not report symlink as a directory
1. [jira] [Created] (HADOOP-10587) Use a thread-local cache in TokenIdentifier#getBytes to avoid creating many DataOutputBuffer objects
1. [jira] Created: (HADOOP-2887) Reducers throw oom exceptions during fetching map outputs
1. [jira] [Commented] (HADOOP-11368) Fix OutOfMemory caused due to leaked trustStore reloader thread in KMSClientProvider
1. [jira] Created: (HADOOP-4995) Offline Namenode fsImage verification
1. [jira] [Work started] (HADOOP-10624) Fix some minors typo and add more test cases for hadoop_err
1. [jira] Created: (HADOOP-2774) Add counters to show number of key/values that have been sorted and merged in the maps and reduces
1. [jira] Created: (HADOOP-3370) failed tasks may stay forever in TaskTracker.runningJobs
1. [jira] Created: (HADOOP-2955) ant test fail for TestCrcCorruption with OutofMemory.
1. [jira] [Commented] (HADOOP-10624) Fix some minors typo and add more test cases for hadoop_err
1. [jira] Created: (HADOOP-5467) Create an offline fsimage image viewer
1. [jira] Issue Comment Edited: (HADOOP-153) skip records that throw exceptions
1. [jira] [Commented] (HADOOP-10150) Hadoop cryptographic file system
1. [jira] [Created] (HADOOP-7404) Data Blocks Spliting should be record oriented or provided option for give the spliting locations (offsets) as input file
1. [jira] Resolved: (HADOOP-2206) Design/implement a general log-aggregation framework for Hadoop
1. [jira] Created: (HADOOP-6833) IPC leaks call parameters when exceptions thrown
1. [jira] Created: (HADOOP-3309) Unit test fails on Windows: org.apache.hadoop.mapred.TestMiniMRDFSSort.unknown
1. [jira] [Commented] (HADOOP-9253) Capture ulimit info in the logs at service start time
1. [jira] Created: (HADOOP-3746) A fair sharing job scheduler
1. [jira] Created: (HADOOP-3582) Improve how Hadoop gets configured
1. [jira] Created: (HADOOP-3604) Reduce stuck at shuffling phase
1. [jira] [Comment Edited] (HADOOP-10987) Provide an iterator-based listing API for FileSystem
1. [jira] [Created] (HADOOP-9654) IPC timeout doesn't seem to be kicking in
1. [jira] Created: (HADOOP-3644) TestLocalJobControl test gets OutOfMemoryError on 64-bit Java
1. [jira] [Updated] (HADOOP-6763) Remove verbose logging from the Groups class
1. [jira] Created: (HADOOP-4802) RPC Server send buffer retains size of largest response ever sent
1. [jira] Created: (HADOOP-5123) Ant tasks for job submission
1. [jira] Created: (HADOOP-4801) DFS read performance suboptimal when client co-located on nodes with data
1. [jira] [Created] (HADOOP-11829) Improve the vector size of Bloom Filter from int to long, and storage from memory to disk
1. [jira] Created: (HADOOP-4744) Wrong resolution of hostname and port
1. [jira] Created: (HADOOP-2910) Throttle IPC Client/Server during bursts of requests or server slowdown
1. [jira] Commented: (HADOOP-2148) Inefficient FSDataset.getBlockFile()
1. [jira] [Closed] (HADOOP-8507) Avoid OOM while deserializing DelegationTokenIdentifer
1. [jira] [Commented] (HADOOP-9890) single cluster setup docs don't work
1. [jira] [Commented] (HADOOP-9974) Trunk Build Failure at HDFS Sub-project
1. [jira] [Resolved] (HADOOP-10042) Heap space error during copy from maptask to reduce task
1. [jira] Created: (HADOOP-3865) SecondaryNameNode runs out of memory
1. [jira] [Updated] (HADOOP-9601) Support native CRC on byte arrays
1. [jira] [Assigned] (HADOOP-7755) Detect MapReduce PreCommit Trunk builds silently failing when running test-patch.sh
1. [jira] [Commented] (HADOOP-11110) JavaKeystoreProvider should not report a key as created if it was not flushed to the backing file
1. [jira] [Created] (HADOOP-9676) make maximum RPC buffer size configurable
1. [jira] [Commented] (HADOOP-11183) Memory-based S3AOutputstream
1. [jira] [Updated] (HADOOP-6732) Improve FsShell's heap consumption by switching to listStatus that returns an iterator
1. [jira] [Comment Edited] (HADOOP-10389) Native RPCv9 client
1. [jira] [Commented] (HADOOP-9196) Modify BloomFilter read() and write() to address memory concerns
1. [jira] Created: (HADOOP-3550) Reduce tasks failing with OOM
1. [jira] [Commented] (HADOOP-9601) Support native CRC on byte arrays
1. [jira] Created: (HADOOP-2751) Increase map/reduce child tasks' heapsize from current default of 200M to 512M
1. [jira] [Assigned] (HADOOP-6732) Improve FsShell's heap consumption by switching to listStatus that returns an iterator
1. [jira] Created: (HADOOP-3637) Support for snapshots
1. [jira] Created: (HADOOP-3553) Nested class TaskTracker.TaskInProgress needs additional synchronization
1. [jira] Created: (HADOOP-4575) An independent HTTPS proxy for HDFS
1. [jira] [Commented] (HADOOP-9974) Maven OutOfMemory exception when building with protobuf 2.5.0
1. [jira] Created: (HADOOP-2853) Add Writable for very large lists of key / value pairs
1. [jira] Created: (HADOOP-3022) Fast Cluster Restart
1. [jira] [Created] (HADOOP-8396) DataStreamer, OutOfMemoryError, unable to create new native thread
1. [jira] Updated: (HADOOP-6204) Implementing aspects development and fault injeciton framework for Hadoop
1. [jira] [Updated] (HADOOP-9902) Shell script rewrite
1. [jira] [Commented] (HADOOP-9676) make maximum RPC buffer size configurable
1. [jira] [Moved] (HADOOP-9974) Trunk Build Failure at HDFS Sub-project
1. [jira] Created: (HADOOP-6598) Remove verbose logging from the Groups class
1. [jira] [Updated] (HADOOP-11292) "mvm package" reports error when using Java 1.8
1. [jira] [Commented] (HADOOP-6858) Enable rotateable JVM garbage collection logs for Hadoop daemons
1. [jira] Commented: (HADOOP-1985) Abstract node to switch mapping into a topology service class used by namenode and jobtracker
1. [jira] Created: (HADOOP-4044) Create symbolic links in HDFS
1. [jira] [Updated] (HADOOP-10047) Allow Compressor/Decompressor APIs to expose a Direct ByteBuffer API
1. [jira] [Commented] (HADOOP-10624) Fix some minor typos and add more test cases for hadoop_err
1. [jira] Created: (HADOOP-5598) Implement a pure Java CRC32 calculator
1. [jira] [Assigned] (HADOOP-2209) SecondaryNamenode process should exit if it encounters Runtime exceptions
1. [jira] [Commented] (HADOOP-4890) shutdown method in DataNode.java could generate thousand of log entries with the same message in a very short time
1. [jira] [Commented] (HADOOP-10146) Workaround JDK7 Process fd close bug
1. [jira] Created: (HADOOP-2847) [HOD] Idle cluster cleanup does not work if the JobTracker becomes unresponsive to RPC calls
1. [jira] Commented: (HADOOP-2615) Add max number of mapfiles to compact at one time giveing us a minor & major compaction
1. [jira] [Commented] (HADOOP-8562) Enhancements to support Hadoop on Windows Server and Windows Azure environments
1. [jira] Created: (HADOOP-3581) Prevent memory intensive user tasks from taking down nodes
1. [jira] Commented: (HADOOP-2165) Augment JobHistory to store tasks' userlogs
1. [jira] [Commented] (HADOOP-8757) Metrics should disallow names with invalid characters
1. [jira] [Resolved] (HADOOP-3629) Document the metrics produced by hadoop
1. [jira] Created: (HADOOP-3514) Improve the map output handling at the tasktracker for shuffle
1. [jira] [Commented] (HADOOP-9672) Upgrade Avro dependency
1. [jira] [Created] (HADOOP-7591) JobHistory cleanup task causing JT going OOM
1. [jira] [Updated] (HADOOP-11292) "mvn package" reports error when using Java 1.8
1. [jira] [Updated] (HADOOP-11368) Fix OutOfMemory caused due to leaked trustStore reloader thread in KMSClientProvider
1. [jira] [Commented] (HADOOP-6763) Remove verbose logging from the Groups class
1. [jira] Created: (HADOOP-4707) Improvements to Hadoop Thrift bindings
1. [jira] Created: (HADOOP-5516) TaskMemoryManagerThread crashes in a corner case
1. [jira] Created: (HADOOP-4794) separate branch for HadoopVersionAnnotation
1. [jira] [Commented] (HADOOP-10587) Use a thread-local cache in TokenIdentifier#getBytes to avoid creating many DataOutputBuffer objects
1. [jira] [Commented] (HADOOP-9639) truly shared cache for jars (jobjar/libjar)
1. [jira] [Updated] (HADOOP-10624) Fix some minor typos and add more test cases for hadoop_err
1. [jira] [Created] (HADOOP-8468) Umbrella of enhancements to support different failure and locality topologies
1. [jira] Created: (HADOOP-4635) Memory leak
1. [jira] [Commented] (HADOOP-10926) Improve test-patch.sh to apply binary diffs
1. [jira] [Commented] (HADOOP-10158) SPNEGO should work with multiple interfaces/SPNs.
1. [jira] [Created] (HADOOP-8659) Native libraries must build with soft-float ABI for Oracle JVM
1. [jira] Created: (HADOOP-4129) Memory limits of TaskTracker and Tasks should be in kiloBytes.
1. [jira] Issue Comment Edited: (HADOOP-2095) Reducer failed due to Out ofMemory
1. [jira] Created: (HADOOP-5708) Configuration should provide a way to write only properties that have been set
1. [jira] Commented: (HADOOP-2721) Use job control for tasks (and therefore for pipes and streaming)
1. [jira] Created: (HADOOP-5318) Poor IO Performance due to AtomicLong operations
1. [jira] Created: (HADOOP-3707) Frequent DiskOutOfSpaceException on almost-full datanodes
1. [jira] [Updated] (HADOOP-6858) Enable rotateable JVM garbage collection logs for Hadoop daemons
1. [jira] Created: (HADOOP-5847) Streaming unit tests failing for a while on trunk
1. [jira] [Updated] (HADOOP-10603) Crypto input and output streams implementing Hadoop stream interfaces
1. [jira] [Assigned] (HADOOP-11446) S3AOutputStream should use shared thread pool to avoid OutOfMemoryError
1. [jira] [Created] (HADOOP-7456) Connection with RemoteException is not removed from cached HashTable and cause memory leak
1. [jira] [Created] (HADOOP-7659) fs -getmerge isn't guaranteed to work well over non-HDFS filesystems
1. [jira] [Created] (HADOOP-11292) "mvm package" reports error when using Java 1.8
1. [jira] Created: (HADOOP-2991) dfs.du.reserved not honored in 0.15/16 (regression from 0.14+patch for 2549)
1. [jira] [Created] (HADOOP-10146) Workaround JDK7 Process fd close bug
1. [jira] [Created] (HADOOP-8361) avoid out-of-memory problems when deserializing strings
1. [jira] Created: (HADOOP-3762) Task tracker died due to OOM
1. [jira] Updated: (HADOOP-2448) Improve Block report processing and name node restarts (Master Jira)
1. [jira] [Created] (HADOOP-11446) S3AOutputStream should use shared thread pool to avoid OutOfMemoryError
1. [jira] [Created] (HADOOP-9082) Select and document a platform-independent scripting language for use in Hadoop environment
1. [jira] Created: (HADOOP-3136) Assign multiple tasks per TaskTracker heartbeat
1. [jira] Created: (HADOOP-6532) Path objects are heavy
1. [jira] Assigned: (HADOOP-249) Improving Map -> Reduce performance and Task JVM reuse
1. [jira] Created: (HADOOP-3421) Requirements for a Resource Manager for Hadoop
1. [jira] [Commented] (HADOOP-10042) Heap space error during copy from maptask to reduce task
1. [jira] Created: (HADOOP-4766) Hadoop performance degrades significantly as more and more jobs complete
1. [jira] Updated: (HADOOP-1650) Upgrade Jetty to 6.x
1. [jira] Created: (HADOOP-4915) Out of Memory error in reduce shuffling phase when compression is turned on
1. [jira] Created: (HADOOP-5641) Possible NPE in CapacityScheduler's MemoryMatcher
1. [jira] [Updated] (HADOOP-10042) Heap space error during copy from maptask to reduce task
1. [jira] [Updated] (HADOOP-10940) RPC client does no bounds checking of responses
1. [jira] [Moved] (HADOOP-10987) Provide an iterator-based listing API for FileSystem
1. [jira] Created: (HADOOP-3315) New binary file format
1. [jira] [Commented] (HADOOP-9583) test-patch gives +1 despite build failure when running tests
1. [jira] [Commented] (HADOOP-9232) JniBasedUnixGroupsMappingWithFallback fails on Windows with UnsatisfiedLinkError
1. [jira] Created: (HADOOP-4584) Slow generation of blockReport at DataNode causes delay of sending heartbeat to NameNode
1. [jira] Created: (HADOOP-3999) Need to add host capabilites / abilities
1. [jira] Created: (HADOOP-5199) A proposal to merge common functionality of various Schedulers
1. [jira] Commented: (HADOOP-6858) Enable rotateable JVM garbage collection logs for Hadoop daemons
1. [jira] [Created] (HADOOP-8997) Upgrade of the .deb Packege removes Hadoop Users (hdfs and mapred) and the hadoop-group
1. [jira] [Commented] (HADOOP-11292) "mvn package" reports error when using Java 1.8
1. [jira] [Commented] (HADOOP-11387) Simplify NetUtils#canonicalizeHost()
1. [jira] [Created] (HADOOP-9182) the buffer used in hdfsRead seems leaks when the thread exits
1. [jira] Created: (HADOOP-3248) Improve Namenode startup performance
1. [jira] Created: (HADOOP-5270) Reduce task should stop shuffle-retrying in case of out-of-memory errors
1. [jira] [Resolved] (HADOOP-6156) Move map/reduce specific classes out of common
1. [jira] Commented: (HADOOP-249) Improving Map -> Reduce performance and Task JVM reuse
1. [jira] [Moved] (HADOOP-8507) avoid OOM while deserializing DelegationTokenIdentifer
1. [jira] [Updated] (HADOOP-3629) Document the metrics produced by hadoop
1. [jira] Commented: (HADOOP-2346) DataNode should have timeout on socket writes.
1. [jira] Updated: (HADOOP-2719) Corner case exists in detecting Java process deaths that might lead to orphan pipes processes lying around in memory
1. [jira] Created: (HADOOP-6732) Improve FsShell's heap consumption by switching to listStatus that returns an iterator
1. [jira] Created: (HADOOP-5561) Javadoc-dev ant target runs out of heap space
1. [jira] Created: (HADOOP-3994) There is little information provided when the TaskTracker kills a Task that has not reported with the timeout (600 sec) interval - this patch provides a stack trace of the task
1. [jira] Created: (HADOOP-3672) support for persistent connections to improve pread() performance.
1. [jira] Created: (HADOOP-6502) DistributedFileSystem#listStatus is very slow when listing a directory with a size of 1300
1. [jira] Created: (HADOOP-3638) Cache the iFile index files in memory to reduce seeks during map output serving
1. [jira] Updated: (HADOOP-2095) Reducer failed due to Out ofMemory
1. [jira] [Created] (HADOOP-7381) FindBugs OutOfMemoryError
1. [jira] [Commented] (HADOOP-10081) Client.setupIOStreams can leak socket resources on exception or error
1. [jira] [Commented] (HADOOP-9933) Augment Service model to support starting stopped services
1. [jira] Commented: (HADOOP-2676) Maintaining cluster information across multiple job submissions
1. [jira] Created: (HADOOP-3629) Document the metrics produced by hadoop
1. [jira] [Created] (HADOOP-8578) Provide a mechanism for cleaning config items from LocalDirAllocator which will not be used anymore
1. [jira] Created: (HADOOP-6490) Path.normalize should use StringUtils.replace in favor of String.replace
1. [jira] [Commented] (HADOOP-9211) HADOOP_CLIENT_OPTS default setting fixes max heap size at 128m, disregards HADOOP_HEAPSIZE
1. [jira] Created: (HADOOP-3687) Ability to pause/resume tasks
1. [jira] Created: (HADOOP-3946) TestMapRed fails on trunk
1. [jira] [Commented] (HADOOP-11363) Hadoop maven surefire-plugin uses must set heap size
1. [jira] [Updated] (HADOOP-10587) Use a thread-local cache in TokenIdentifier#getBytes to avoid creating many DataOutputBuffer objects
1. [jira] [Commented] (HADOOP-7755) Detect MapReduce PreCommit Trunk builds silently failing when running test-patch.sh
1. [jira] Created: (HADOOP-5330) Zombie tasks remain after jobs finish/fail/get killed
1. [jira] [Created] (HADOOP-8060) Add a capability to use of consistent checksums for append and copy
1. [jira] Created: (HADOOP-6349) Implement FastLZCodec for fastlz/lzo algorithm
1. [jira] [Updated] (HADOOP-9954) Hadoop 2.0.5 doc build failure - OutOfMemoryError exception
1. [jira] Commented: (HADOOP-2095) Reducer failed due to Out ofMemory
1. [jira] Updated: (HADOOP-5958) Use JDK 1.6 File APIs in DF.java wherever possible
1. [jira] [Created] (HADOOP-8929) Add toString for SampleQuantiles
1. [jira] Created: (HADOOP-5526) Provide an admin page displaying events in the cluster along with cluster status/health
1. [jira] [Created] (HADOOP-8942) Thundering herd of RPCs with large responses leads to OOM
1. [jira] [Updated] (HADOOP-10780) namenode throws java.lang.OutOfMemoryError upon DatanodeProtocol.versionRequest from datanode
1. [jira] Updated: (HADOOP-2206) Design/implement a general log-aggregation framework for Hadoop
1. [jira] [Updated] (HADOOP-9439) JniBasedUnixGroupsMapping: fix some crash bugs
1. [jira] Created: (HADOOP-4721) OOM in .TestSetupAndCleanupFailure
1. [jira] Commented: (HADOOP-5958) Use JDK 1.6 File APIs in DF.java wherever possible
1. [jira] Commented: (HADOOP-2636) [hbase] Make cache flush triggering less simplistic
1. [jira] [Updated] (HADOOP-7755) Detect MapReduce PreCommit Trunk builds silently failing when running test-patch.sh
1. [jira] Created: (HADOOP-3262) make Hadoop compile under Apache Harmony
1. [jira] [Commented] (HADOOP-6732) Improve FsShell's heap consumption by switching to listStatus that returns an iterator
1. [jira] [Commented] (HADOOP-9439) JniBasedUnixGroupsMapping: fix some crash bugs
1. [jira] Created: (HADOOP-5184) OOM in the TaskTracker while serving map outputs
1. [jira] [Commented] (HADOOP-9891) CLIMiniCluster instructions fail with MiniYarnCluster ClassNotFound
1. [jira] [Resolved] (HADOOP-10624) Fix some minors typo and add more test cases for hadoop_err
1. [jira] Updated: (HADOOP-249) Improving Map -> Reduce performance and Task JVM reuse
1. [jira] [Commented] (HADOOP-11320) Submitting a hadoop patch doesn't trigger jenkins test run
1. [jira] [Created] (HADOOP-9954) Hadoop 2.0.5 doc build failure - OutOfMemoryError exception
1. [jira] Created: (HADOOP-4810) Data lost at cluster startup time
1. [jira] [Updated] (HADOOP-9757) Har metadata cache can grow without limit
1. [jira] Created: (HADOOP-5883) TaskMemoryMonitorThread might shoot down tasks even if their processes momentarily exceed the requested memory
1. [jira] Created: (HADOOP-4976) Mapper runs out of memory
1. [jira] [Assigned] (HADOOP-6490) Path.normalize should use StringUtils.replace in favor of String.replace
1. [jira] Created: (HADOOP-5145) Balancer sometimes runs out of memory after days or weeks running
1. [jira] Created: (HADOOP-4513) Capacity scheduler should initialize tasks asynchronously
1. [jira] Created: (HADOOP-4018) limit memory usage in jobtracker
1. [jira] [Commented] (HADOOP-11446) S3AOutputStream should use shared thread pool to avoid OutOfMemoryError
1. [jira] Created: (HADOOP-5539) o.a.h.mapred.Merger not maintaining map out compression on intermediate files
1. [jira] Updated: (HADOOP-2721) Use job control for tasks (and therefore for pipes and streaming)
1. [jira] Created: (HADOOP-3670) JobTracker running out of heap space
1. [jira] Created: (HADOOP-3961) resource estimation works badly in some cases
1. [jira] Created: (HADOOP-6884) Add LOG.isDebugEnabled() guard for each LOG.debug("...")
1. [jira] Created: (HADOOP-5934) testHighRamJobWithSpeculativeExecution needs some changes
1. [jira] Updated: (HADOOP-6843) Entries in the FileSystem's Cache could be cleared when they are not used
1. [jira] [Updated] (HADOOP-11446) S3AOutputStream should use shared thread pool to avoid OutOfMemoryError
1. [jira] [Assigned] (HADOOP-10987) Provide an iterator-based listing API for FileSystem
1. [jira] [Commented] (HADOOP-9757) Har metadata cache can grow without limit
1. [jira] Created: (HADOOP-4435) The JobTracker should display the amount of heap memory used
1. [jira] Created: (HADOOP-2758) Reduce memory copies when data is read from DFS
1. [jira] [Updated] (HADOOP-10357) Memory Leak in UserGroupInformation.doAs for JDBC Connection to Hive
1. [jira] Created: (HADOOP-5069) add a Hadoop-centric junit test result listener
1. [jira] Created: (HADOOP-3412) Refactor the scheduler out of the JobTracker
1. [jira] Created: (HADOOP-4980) Cleanup the Capacity Scheduler code
1. [jira] Created: (HADOOP-5299) Reducer inputs should be spilled to HDFS rather than local disk.
1. [jira] Created: (HADOOP-4931) Document TaskTracker's memory management functionality and CapacityScheduler's memory based scheduling.
1. [jira] [Resolved] (HADOOP-2644) Remove the warning for attempting to override a final parameter
1. [jira] [Updated] (HADOOP-8507) Avoid OOM while deserializing DelegationTokenIdentifer
1. [jira] [Commented] (HADOOP-11029) FileSystem#Statistics uses volatile variables that must be updated on write or read calls.
1. [jira] [Updated] (HADOOP-11363) Hadoop maven surefire-plugin uses must set heap size
1. [jira] Created: (HADOOP-2719) Corner case exists in detecting Java process deaths that might lead to orphan pipes processes lying around in memory
1. [jira] [Updated] (HADOOP-10562) Namenode exits on exception without printing stack trace in AbstractDelegationTokenSecretManager
1. [jira] Commented: (HADOOP-4487) Security features for Hadoop
1. [jira] Created: (HADOOP-4773) namenode startup error, hadoop-user-namenode.pid permission denied.
1. [jira] Created: (HADOOP-4439) Cleanup memory related resource management
1. [jira] [Commented] (HADOOP-10940) RPC client does no bounds checking of responses
1. [jira] Created: (HADOOP-5632) Jobtracker leaves tasktrackers underutilized
1. [jira] Issue Comment Edited: (HADOOP-1188) processIOError() should update fstime file
1. [jira] Created: (HADOOP-5223) Refactor reduce shuffle code
1. [jira] [Updated] (HADOOP-9196) Modify BloomFilter read() and write() to address memory concerns
1. [jira] Created: (HADOOP-4906) TaskTracker running out of memory after running several tasks
1. [jira] Created: (HADOOP-3675) Provide more flexibility in the way tasks are run
1. [jira] Created: (HADOOP-5687) Hadoop NameNode throws NPE if fs.default.name is the default value
1. [jira] [Created] (HADOOP-10357) Memory Leak in UserGroupInformation.doAs for JDBC Connection to Hive
1. [jira] Created: (HADOOP-4845) Shuffle counter issues
1. [jira] [Commented] (HADOOP-6490) Path.normalize should use StringUtils.replace in favor of String.replace
1. [jira] [Created] (HADOOP-7333) Performance improvement in PureJavaCrc32
1. [jira] Created: (HADOOP-6678) Propose some changes to FileContext
1. [jira] Created: (HADOOP-4698) TestMapRed fails with 64bit JDK
1. [jira] Created: (HADOOP-3759) Provide ability to run memory intensive jobs without affecting other running tasks on the nodes
1. [jira] [Resolved] (HADOOP-9974) Trunk Build Failure at HDFS Sub-project
1. [jira] [Commented] (HADOOP-10607) Create an API to Separate Credentials/Password Storage from Applications
1. [jira] Created: (HADOOP-4298) File corruption when reading with fuse-dfs
1. [jira] [Created] (HADOOP-8632) Configuration leaking class-loaders
1. [jira] [Created] (HADOOP-8323) Revert HADOOP-7940
1. [jira] [Updated] (HADOOP-9974) Maven OutOfMemory exception when building with protobuf 2.5.0
1. [jira] Commented: (HADOOP-449) Generalize the SequenceFileInputFilter to apply to any InputFormat
1. [jira] Created: (HADOOP-2973) Unit test fails on Windows: org.apache.hadoop.dfs.TestLocalDFS.testWorkingDirectory
1. [jira] Created: (HADOOP-2837) JobTracker got stuck
1. [jira] [Commented] (HADOOP-11292) "mvm package" reports error when using Java 1.8
1. [jira] [Updated] (HADOOP-10146) Workaround JDK7 Process fd close bug
1. [jira] Created: (HADOOP-3779) limit concurrent connections(data serving thread) in one datanode
1. [jira] Created: (HADOOP-7020) establish a "Powered by Hadoop" logo
1. [jira] Created: (HADOOP-6717) Log levels in o.a.h.security.Groups too high
1. [jira] Commented: (HADOOP-1650) Upgrade Jetty to 6.x
1. [jira] Created: (HADOOP-5664) Use of ReentrantLock.lock() in MapOutputBuffer takes up too much cpu time
1. [jira] Created: (HADOOP-4981) Prior code fix in Capacity Scheduler prevents speculative execution in jobs
1. [jira] Commented: (HADOOP-2206) Design/implement a general log-aggregation framework for Hadoop
1. [jira] Created: (HADOOP-6460) Namenode runs of out of memory due to memory leak in ipc Server
1. [jira] [Commented] (HADOOP-6253) Add a Ceph FileSystem interface.
1. [jira] Created: (HADOOP-7116) raise contrib junit test jvm memory size to 512mb
1. [jira] Created: (HADOOP-5727) Faster, simpler id.hashCode() which does not allocate memory
1. [jira] Commented: (HADOOP-153) skip records that throw exceptions
1. [jira] [Commented] (HADOOP-8989) hadoop dfs -find feature
1. [jira] Commented: (HADOOP-1869) access times of HDFS files
1. [jira] Created: (HADOOP-4768) Dynamic Priority Scheduler that allows queue shares to be controlled dynamically by a currency
1. [jira] [Moved] (HADOOP-9419) CodecPool should avoid OOMs with buggy codecs
1. [jira] [Created] (HADOOP-7864) Building mvn site with Maven < 3.0.2 causes OOM errors
1. [jira] Created: (HADOOP-5083) Optionally a separate daemon should serve JobHistory
1. [jira] Created: (HADOOP-6474) Add a command-line diagnostics entry point
1. [jira] Created: (HADOOP-2907) dead datanodes because of OutOfMemoryError
1. [jira] Created: (HADOOP-4035) Modify the capacity scheduler (HADOOP-3445) to schedule tasks based on memory requirements and task trackers free memory
1. [jira] [Commented] (HADOOP-10987) Provide an iterator-based listing API for FileSystem
1. [jira] [Created] (HADOOP-9757) Har metadata cache can grow without limit
1. [jira] [Commented] (HADOOP-10968) hadoop native build fails to detect java_libarch on ppc64le
1. [jira] Created: (HADOOP-5906) Stream test TestStreamingExitStatus fails with Out of Memory
1. [jira] Created: (HADOOP-3025) ChecksumFileSystem needs to support the new delete method
1. [jira] Created: (HADOOP-7047) RPC client gets stuck
1. [jira] [Updated] (HADOOP-11368) Fix SSLFactory truststore reloader thread leak in KMSClientProvider
1. [jira] Created: (HADOOP-2878) Hama code contribution
1. [jira] [Updated] (HADOOP-11526) Memory leak in Bzip2Decompressor
1. [jira] Created: (HADOOP-3351) Fix history viewer
1. [jira] Created: (HADOOP-5059) 'whoami', 'topologyscript' calls failing with OOM
1. [jira] [Commented] (HADOOP-10641) Introduce Coordination Engine interface
1. [jira] [Commented] (HADOOP-10389) Native RPCv9 client
1. [jira] [Created] (HADOOP-10624) Fix some minors typo and add more test cases for hadoop_err
1. [jira] [Created] (HADOOP-9196) Modify BloomFilter.write() to address memory concerns
1. [jira] [Reopened] (HADOOP-9253) Capture ulimit info in the logs at service start time
1. [jira] Created: (HADOOP-3144) better fault tolerance for corrupted text files
1. [jira] [Resolved] (HADOOP-6843) Entries in the FileSystem's Cache could be cleared when they are not used
1. [jira] Created: (HADOOP-3104) MultithreadMapRunner keeps consuming records even if trheads are not available
1. [jira] Created: (HADOOP-3232) Datanodes time out
1. [jira] Created: (HADOOP-3462) reduce task failures during shuffling should not count against number of retry attempts
1. [jira] Created: (HADOOP-3455) IPC.Client synchronisation looks weak
1. [jira] [Resolved] (HADOOP-2837) JobTracker got stuck
1. [jira] Created: (HADOOP-6837) Support for LZMA compression
1. [jira] Commented: (HADOOP-1188) processIOError() should update fstime file
1. [jira] [Commented] (HADOOP-9954) Hadoop 2.0.5 doc build failure - OutOfMemoryError exception
1. [jira] [Commented] (HADOOP-11802) DomainSocketWatcher#watcherThread can encounter IllegalStateException in finally block when calling sendCallback
1. [jira] [Created] (HADOOP-10042) Heap space error during copy from maptask to reduce task
1. [jira] [Updated] (HADOOP-10624) Fix some minors typo and add more test cases for hadoop_err
1. [jira] [Resolved] (HADOOP-6732) Improve FsShell's heap consumption by switching to listStatus that returns an iterator
1. [jira] Created: (HADOOP-4164) Chinese translation of core docs
1. [jira] [Commented] (HADOOP-8507) Avoid OOM while deserializing DelegationTokenIdentifer
1. [jira] [Created] (HADOOP-8069) Enable TCP_NODELAY by default for IPC
1. [jira] Created: (HADOOP-3633) Uncaught exception in DataXceiveServer
1. [jira] Resolved: (HADOOP-1837) Insufficient space exception from InMemoryFileSystem after raising fs.inmemory.size.mb
1. [jira] Created: (HADOOP-3466) DataNode fails to deliver blocks, holds thousands of open socket connections
1. [jira] [Created] (HADOOP-7829) Delegation token manager should support token store abstraction
1. [jira] Created: (HADOOP-5001) Junit tests that time out don't write any test progress related logs
1. [jira] Commented: (HADOOP-2438) In streaming, jobs that used to work, crash in the map phase -- even if the mapper is /bin/cat
1. [jira] Created: (HADOOP-4656) Add a user to groups mapping service
1. [jira] Created: (HADOOP-7154) Should set MALLOC_ARENA_MAX in hadoop-env.sh
1. [jira] [Created] (HADOOP-11363) Hadoop maven surefire-plugin uses must set heap size
1. [jira] Created: (HADOOP-6723) unchecked exceptions thrown in IPC Connection orphan clients
1. [jira] Created: (HADOOP-4879) TestJobTrackerRestart fails on trunk
1. [jira] [Commented] (HADOOP-9654) IPC timeout doesn't seem to be kicking in
1. [jira] [Commented] (HADOOP-9312) JniBasedUnixGroupsMapping#getGroupForUser can potentially leak memory
1. [jira] Created: (HADOOP-5324) Reduce step hangs while recovering a block from bad datanode
1. [jira] [Commented] (HADOOP-9182) the buffer used in hdfsRead seems leaks when the thread exits
1. [jira] [Commented] (HADOOP-3629) Document the metrics produced by hadoop
1. [jira] [Moved] (HADOOP-7755) Detect MapReduce PreCommit Trunk builds silently failing when running test-patch.sh
1. [jira] [Resolved] (HADOOP-9419) CodecPool should avoid OOMs with buggy codecs
1. [jira] [Created] (HADOOP-8597) FsShell's Text command should be able to read avro data files
1. [jira] Created: (HADOOP-4472) Should we move out the creation of setup/cleanup tasks from JobInProgress.initTasks()?
1. [jira] [Commented] (HADOOP-9196) Modify BloomFilter.write() to address memory concerns
1. [jira] [Created] (HADOOP-11368) Fix OutOfMemory caused due to leaked trustStore reloader thread in KMSClientProvider
1. [jira] Created: (HADOOP-5459) CRC errors not detected reading intermediate output into memory with problematic length
1. [jira] Created: (HADOOP-3856) Asynchronous IO Handling in Hadoop and HDFS
1. [jira] Created: (HADOOP-4058) Transparent archival and restore of files from HDFS
1. [jira] [Updated] (HADOOP-9676) make maximum RPC buffer size configurable
1. [jira] Created: (HADOOP-4775) FUSE crashes reliably on 0.19.0
1. [jira] Created: (HADOOP-3842) There is a window where the JobTracker is in the RUNNING state (i.e ready to accept jobs) and never executes them.
1. [jira] Created: (HADOOP-3366) Shuffle/Merge improvements
1. [jira] Created: (HADOOP-6843) Entries in the FileSystem's Cache could be cleared when they are not used
1. [jira] [Created] (HADOOP-7989) [ec2] hadoop Could not create the Java virtual machine
1. [jira] [Commented] (HADOOP-10047) Add a directbuffer Decompressor API to hadoop
1. [jira] [Created] (HADOOP-7909) Implement Splittable Gzip based on a signature in a gzip header field
1. [jira] Created: (HADOOP-3150) Move task file promotion into the task
1. [jira] [Commented] (HADOOP-11488) Difference in default connection timeout for S3A FS
1. [jira] [Resolved] (HADOOP-5069) add a Hadoop-centric junit test result listener
1. [jira] Created: (HADOOP-4429) Misconfigured UNIX Groups Break Hadoop
1. [jira] Created: (HADOOP-4413) Capacity Scheduler to provide a scheduler history log to record actions taken and why
1. [jira] [Commented] (HADOOP-10725) Implement listStatus and getFileInfo in the native client
1. [jira] Updated: (HADOOP-2148) Inefficient FSDataset.getBlockFile()
1. [jira] [Reopened] (HADOOP-2837) JobTracker got stuck
1. [jira] [Resolved] (HADOOP-6858) Enable rotateable JVM garbage collection logs for Hadoop daemons
1. [jira] Created: (HADOOP-4912) dfs startup error, 0 datanodes in
1. [jira] Created: (HADOOP-3446) The reduce task should not flush the in memory file system before starting the reducer
1. [jira] Created: (HADOOP-2857) libhdfs: no way to set JVM args other than classpath
1. [jira] [Created] (HADOOP-7599) Improve hadoop setup conf script to setup secure Hadoop cluster
1. [jira] [Resolved] (HADOOP-1867) use single parameter to specify a node's available ram
