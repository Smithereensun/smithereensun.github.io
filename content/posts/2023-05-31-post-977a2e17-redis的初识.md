---
title: "Redis的初识"
date: 2023-05-31
description: "简介 已经有了Membercache和各种数据库，Redis为什么会产生?Redis纯粹为应用而产生，它是一个高性能的key-value数据库。Redis的出现，很大程序补偿了Memcached这类key-value存储的不足，解决了断电后数据库完全丢失的情况；在部分场合可以对关系数据库起到很好的补"
tags:
  - "分布式架构"
  - "NoSql"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11443421.html"
---

<h1>简介</h1>
<p>　　已经有了Membercache和各种数据库，Redis为什么会产生?Redis纯粹为应用而产生，它是一个高性能的key-value数据库。Redis的出现，很大程序补偿了Memcached这类key-value存储的不足，解决了断电后数据库完全丢失的情况；在部分场合可以对关系数据库起到很好的补偿作用。性能测试结果表示SET操作每秒钟可达110000，GET操作每秒81000次(当然不同的服务器配置性能不同)。</p>
<p>　　Redis是一种面向"键-值"对类型数据的分布式NoSQL数据库系统，特点是高性能，持久存储，适应高并发的应用场景。和Memcache类似，它支持存储的value类型相对更多，包括string(字符串)、list(链表)、set(集合)和zset(有序集合)。这些数据类型支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的，支持各种不同方式的排序。<span style="color: rgba(255, 153, 0, 1)"><strong>Redis与Memcache一样，为了保证效率，数据都是缓存在内存中，区别的是Redis会周期性的把更新的数据写入磁盘或者修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。</strong></span></p>
<p>　　Redis目前提供四种数据类型:string、list、set、zset</p>
<p>　　Redis的存储分为内存存储、磁盘存储和log文件三部分，配置文件中有三个参数对其进行配置。</p>
<p>　　　　1、save seconds updates：指出在多长时间内，有多少次更新操作，就将数据同步到数据文件。</p>
<p>　　　　2、appendonly yes/no：是否在每次更新操作后进行日志记录。如果不开启，可能会在断电时导致一段时间内的数据丢失。因为Redis本身数据同步文件是按上面save条件来同步的，所以有的数据会在一段时间内只存在内存中。</p>
<p>　　　　3、appendfsync no/always/everysec：数据缓存同步至磁盘的方式。no表示等操作系统进行数据缓存同步到磁盘，always表示每次更新操作后手动调用fsync()将数据写到磁盘，everysec表示每秒同步一次。</p>
<h1>&nbsp;安装及使用</h1>
<p>下载地址:https://github.com/microsoftarchive/redis/releases</p>
<p>百度云盘:</p>
<p>链接：https://pan.baidu.com/s/1ObkTyQ5hrCYoVGWkqanfFQ <br>提取码：d3yo</p>
<h2>第一步：下载后解压本地磁盘上(<span style="color: rgba(255, 0, 0, 1)">注：目录不能包括中文</span>)</h2>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201909/1504448-20190901213325350-2131820075.png" alt="" /></p>
<h2>第二步： 定位到解压redis目录下(cmd)</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201909/1504448-20190901213540020-1153591929.png" alt="" /></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(128, 0, 128, 1)">1</span>、redis-<span style="color: rgba(0, 0, 0, 1)">server.exe        redis服务器的daemon启动程序
</span><span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(128, 0, 128, 1)">2</span><span style="color: rgba(0, 0, 0, 1)">、redis.windows.conf        redis配置文件
</span><span style="color: rgba(0, 128, 128, 1)">3</span> <span style="color: rgba(128, 0, 128, 1)">3</span>、redis-<span style="color: rgba(0, 0, 0, 1)">cli.exe        redis命令行操作工具
</span><span style="color: rgba(0, 128, 128, 1)">4</span> <span style="color: rgba(128, 0, 128, 1)">4</span>、redis-check-<span style="color: rgba(0, 0, 0, 1)">dump.exe        本地数据库检查
</span><span style="color: rgba(0, 128, 128, 1)">5</span> <span style="color: rgba(128, 0, 128, 1)">5</span>、redis-check-<span style="color: rgba(0, 0, 0, 1)">aof.exe        更新日志检查
</span><span style="color: rgba(0, 128, 128, 1)">6</span> <span style="color: rgba(128, 0, 128, 1)">6</span>、redis-benchmark.exe        性能测试，用于模拟同时由N个客户端发送M个 SETs/GETs查询(类似于Apache ab工具)</pre>
