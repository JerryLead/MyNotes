# Spark Internals

Spark Version: 1.0.0  
Doc Version: 1.0.0.0

## Authors
 [@JerryLead](http://weibo.com/jerrylead) - Lijie Xu - 2014年7月10日 


## Introduction
本文主要讨论 Apache Spark 的设计与实现，重点关注其内部架构，附带讨论与 Hadoop MapReduce 设计与实现的区别。请不要将此文档称之为“源码分析”，因为该文档不仅仅解读实现代码，还会讨论其设计思想、性能、可靠性方面的问题。

本文档并不是面向 Spark 的普通用户，而是面向渴望对 Spark 内部设计与实现机制，以及大数据分布式处理系统深入了解的 Geeks。

因为 Spark 社区很活跃，更新速度很快，本文档也会尽量保持同步，文档号的命名与 Spark 版本一致，最后一位表示文档的更新版本号。

该文档目前由 JerryLead 撰写，由于实验条件、经验、技术水平等限制，当前只讨论 standalone 版本中的核心功能，而不是全部功能。希望更多的小伙伴们加入撰写队伍。

## Contents
本文档首先讨论 job 如何执行，然后讨论与 job 执行相关的一些数据存储、通信、调度等内容。具体内容如下：

1. 基本架构
2. Job 与 task 的执行
3. 数据存储
4. Job 与 task 调度
5. 性能分析
6. 可靠性分析

