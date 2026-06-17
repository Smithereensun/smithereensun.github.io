---
title: "MySQL 并发控制（锁得使用）"
date: 2020-06-14
description: "导读 并发问题：同一时刻进行读写，并发问题回引发数据不一致问题。 解决并发问题：MySQL采用了锁定机制去解决并发问题 锁的分类 MySQL使用两种锁机制去解决问题：共享锁和排他锁，也叫读锁或者写锁。 共享锁、读锁：不影响其他连接的读，写会受影响 排他锁、写锁：会不让其他连接进行读写 MySQL针对"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13126960.html"
---

<h1 style="text-align: center">导读</h1>
<p>并发问题：同一时刻进行读写，并发问题回引发数据不一致问题。</p>
<p>解决并发问题：MySQL采用了锁定机制去解决并发问题</p>
<h1 style="text-align: center">锁的分类</h1>
<p>　　MySQL使用两种锁机制去解决问题：<strong><span style="color: rgba(255, 0, 0, 1)">共享锁</span></strong>和<span style="color: rgba(255, 0, 0, 1)"><strong>排他锁</strong></span>，也叫读锁或者写锁。</p>
<ul>
<li style="list-style-type: none">
<ul>
<li>共享锁、读锁：不影响其他连接的读，写会受影响</li>
<li>排他锁、写锁：会不让其他连接进行读写</li>
</ul>
</li>
</ul>
<p>　　MySQL针对不同的数据粒度，又分别使用<span style="color: rgba(255, 0, 0, 1)"><strong>表锁</strong></span>和<span style="color: rgba(255, 0, 0, 1)"><strong>行锁</strong></span>进行锁定。</p>
<h1 style="text-align: center">锁的实现</h1>
<p>　　MySQL是使用MVCC(Multi-Version Concurrency Control)实现的（性能很好，其实并没有真正上锁）。</p>
<ul>
<li style="list-style-type: none">
<ul>
<li>悲观锁（真正上锁）</li>
<li>乐观锁（通过一些递增的字段来控制逻辑上锁）</li>
</ul>
</li>
</ul>
<p>　　MVCC这种机制是通过对一行数据的几个隐藏列进行操作实现的。</p>
<p>　　B+树的数据行，其实每一行都要加上几个隐藏列（版本号，一条记录可能对应几个版本号，差不多可以这样理解，一个版本号，对应一个快照）</p>
<h2>服务层和存储引擎层</h2>
<p>　　服务层只是实现了表锁：</p>
<p>　　　　<strong><span style="color: rgba(255, 0, 0, 1)">加锁</span></strong>：lock table 表名 read(write),表名2 read(write)</p>
<p>　　　　<span style="color: rgba(255, 0, 0, 1)"><strong>解锁</strong></span>：unlock tables;</p>
<p>　　存储引擎层实现行锁(只有InnoDB和extraDB实现了行锁)</p>
<p>　　存储引擎层和服务器层可能都实现了行锁，但是实现逻辑不一样，优先使用存储引擎层的实现。</p>
<p>　　事务部分会隐式的去加行锁和表锁，其中这个表锁不是服务器层实现的表锁。</p>
<h2>行锁和表锁对比</h2>
<p>　　表级锁：开销小，加锁快；不会出现死锁；锁定粒度大，发生锁冲突的概率最高，并发度最低</p>
<p>　　行级锁：开销大，加锁慢；回出现死锁；锁定粒度最小，发生锁冲突的概率最低，并发度最大</p>
<h1 style="text-align: center">MVCC并发控制，读操作分类</h1>
<p>　　在MVCC并发控制中，读操作可以分成两类：<span style="color: rgba(255, 0, 0, 1)"><strong>快照读(snapshot read)与当前读(current read)</strong></span>。</p>
<p>　　快照读，读取的记录的可见版本(有可能是历史版本)，不用加锁。</p>
<p>　　当前读，读取的是记录的最新版本，并且，当前读返回的记录，都会加上锁，保证其他事务不会再并发修改这条记录。</p>
<p><strong><span style="color: rgba(255, 0, 0, 1)">快照读</span></strong>：简单的select操作，属于快照读，不加锁。</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">select</span> <span style="color: rgba(128, 128, 128, 1)">*</span> <span style="color: rgba(0, 0, 255, 1)">from</span> table_name <span style="color: rgba(0, 0, 255, 1)">where</span> ?;</pre>
