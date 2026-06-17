---
title: "C# Memcache集群原理、客户端配置详细解析"
date: 2023-05-31
description: "概述 memcache是一套开放源的分布式高速缓存系统。由服务端和客户端组成，以守护程序(监听)方式运行于一个或多个服务器中，随时会接收客户端的连接和操作。memcache主要把数据对象缓存到内存中，通过在内存里维护一个统一的巨大的hash表。简单的说就是将数据调用到内存中，然后从内存中读取，从而大"
tags:
  - "分布式架构"
  - "NoSql"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11441490.html"
---

<h1>概述</h1>
<p>　　memcache是一套开放源的分布式高速缓存系统。由服务端和客户端组成，以守护程序(监听)方式运行于一个或多个服务器中，随时会接收客户端的连接和操作。memcache主要把数据对象缓存到内存中，通过在内存里维护一个统一的巨大的hash表。简单的说就是将数据调用到内存中，然后从内存中读取，从而大大提高读取速度。memcache基于一个存储键/值对的hashmap进行存储对象到内存中。memcache是用C写的，但是客户端可以用任何语言来编写，并通过memcached协议与守护进程通信。</p>
<p>特性：　　<br>　　•在 Memcached中可以保存的item数据量是没有限制的，只要内存足够 。<br>　　•Memcached单进程在32位系统中最大使用内存为2G，若在64位系统则没有限制,这是由于32位系统限制单进程最多可使用2G内存,要使用更多内存，可以分多个端口开启多个Memcached进程 。<br>　　•最大30天的数据过期时间,设置为永久的也会在这个时间过期，常量REALTIME_MAXDELTA<br>　　•单个item最大数据是1MB，超过1MB数据不予存储，常量POWER_BLOCK 1048576进行控制</p>
<h1>Memcache集群原理</h1>
<p>　　Memcache：通过客户端驱动实现集群。Redis、MongoDb：通过服务器端实现集群；Memcache初始化驱动的时候，可以给定一个集合，如</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 0, 255, 1)">string</span>[] servers = { <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">172.20.10.7:11211</span><span style="color: rgba(128, 0, 0, 1)">"</span>,<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">172.20.10.8:11211</span><span style="color: rgba(128, 0, 0, 1)">"</span>};</pre>
