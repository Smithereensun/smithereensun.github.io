---
title: "从入门到精通-Redis，图文并茂、分布式锁、主从复制、哨兵机制、Cluster集群、缓存击穿、缓存雪崩、持久化方案、缓存淘汰策略 附案例源码"
date: 2020-08-31
description: "导读 篇幅较长，干货十足，阅读需要花点时间，全部手打出来的字，难免出现错别字，敬请谅解。珍惜原创，转载请注明出处，谢谢~！ 学习之前，先附上一张知识脑图，百度上找哒~~~ NoSql介绍与Redis介绍 什么是Redis? Redis是用C语言开发的一个开源的高性能键值对(key-value)内存数"
tags:
  - "分布式架构"
  - "NoSql"
  - "Linux"
  - "技术干货"
  - "Redis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12073107.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　篇幅较长，干货十足，阅读需要花点时间，全部手打出来的字，难免出现错别字，敬请谅解。珍惜原创，转载请注明出处，谢谢~！</p>
<p>　　学习之前，先附上一张知识脑图，百度上找哒~~~</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200712082343707-1585142980.jpg" alt="" loading="lazy" /></p>
<p><img src="https://img2018.cnblogs.com/common/1504448/201912/1504448-20191220151557735-825180793.png" alt="" style="display: block; margin-left: auto; margin-right: auto" /></p>
<h1 style="text-align: center">NoSql介绍与Redis介绍</h1>
<h2>什么是Redis?</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>Redis</strong></span>是用<span style="color: rgba(255, 0, 0, 1)"><strong>C语言</strong></span>开发的一个<span style="color: rgba(255, 0, 0, 1)"><strong>开源</strong></span>的高性能<span style="color: rgba(255, 0, 0, 1)"><strong>键值对</strong></span>(key-value)<span style="color: rgba(255, 0, 0, 1)"><strong>内存数据库</strong></span>。</p>
<p>　　它提供<span style="color: rgba(255, 0, 0, 1)"><strong>五种数据类型</strong></span>来存储值：<span style="color: rgba(255, 0, 0, 1)"><strong>字符串类型、散列类型、列表类型、集合类型、有序类型</strong></span>。</p>
<p>　　它是一种<span style="color: rgba(255, 0, 0, 1)"><strong>NoSql</strong></span>数据库。</p>
<h2>什么是NoSql？</h2>
<ul>
<li>NoSql，即Not-Only Sql(不仅仅是SQL)，泛指<span style="color: rgba(255, 0, 0, 1)"><strong>非关系型的数据库</strong></span>。</li>
<li>什么是关系型数据库？数据结构是一种有行有列的数据库。</li>
<li>NoSql数据库是为了解决<span style="color: rgba(255, 0, 0, 1)"><strong>高并发、高可用、高可扩展、大数据存储</strong></span>问题而产生的数据库解决方案。</li>
<li>NoSql可以作为关系型数据库的良好补充，但是<span style="color: rgba(255, 0, 0, 1)"><strong>不能替代关系型数据库</strong></span>。</li>
</ul>
<h2>NoSql数据库分类</h2>
<h3>键值(key-value)存储数据库</h3>
<ul>
<li>相关产品：Tokyo Cabinet/Tyrant、<strong><span style="color: rgba(255, 0, 0, 1)">Redis</span></strong>、Voldemort、Berkeley Db等</li>
<li>典型应用：内存缓存，主要用于处理大量数据的高访问负载</li>
<li>数据模型：一系列键值对</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>优势：快速查询</strong></span></li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>劣势：存储的数据缺少结构化</strong></span></li>
</ul>
<h3>列存储数据库</h3>
<ul>
<li>相关产品：Cassandra、<span style="color: rgba(255, 0, 0, 1)"><strong>Hbase</strong></span>、Riak</li>
<li>典型应用：分布式的文件系统</li>
<li>数据模型：以列簇式存储，将同一列数据存在一起</li>
<li>优势：查找速度快，可扩展性强，更容易进行分布式扩展</li>
<li>劣势：功能相对局限</li>
</ul>
<h3>文档型数据库</h3>
<ul>
<li>相关产品：CouchDB、<span style="color: rgba(255, 0, 0, 1)"><strong>MongoDB</strong></span></li>
<li>典型应用：web应用(与key-value类似，value是结构化的)</li>
<li>数据模型：一系列键值对</li>
<li>优势：数据结构要求不严格</li>
<li>劣势</li>
</ul>
<h3>图形(Graph)数据库</h3>
<ul>
<li>相关数据库：Neo4J、InfoGrid、Infinite、Graph</li>
<li>典型应用：社交网络</li>
<li>数据模型：图结构</li>
<li>优势：利用图结构先关算法</li>
<li>劣势：需要对整个图做计算才能得出结果，不容易做分布式的集群方案。</li>
</ul>
<h1 style="text-align: center">Redis历史发展</h1>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>2008年</strong></span>，意大利的一家创业公司Merzia推出了一款给予MySql的网站实时统计系统LLOOGG，然而没过多久该公司的创始人<span style="color: rgba(255, 0, 0, 1)"><strong>Salvatore Sanfilippo</strong></span>便对MySql的性能感到失望，于是他决定亲力为LLOOGG量身<span style="color: rgba(255, 0, 0, 1)"><strong>定做一个数据库</strong></span>，并<span style="color: rgba(255, 0, 0, 1)"><strong>于2009年开发完成，这个数据库就是Redis</strong></span>。</p>
<p>　　不过<span style="color: rgba(255, 0, 0, 1)"><strong>Salvatore Sanfilippo</strong></span>并<span style="color: rgba(255, 0, 0, 1)"><strong>不满足</strong></span>只<span style="color: rgba(255, 0, 0, 1)"><strong>将Redis</strong><strong>用</strong></span>于<span style="color: rgba(255, 0, 0, 1)"><strong>LLOOGG</strong></span>这一款产品，而是<span style="color: rgba(255, 0, 0, 1)"><strong>希望更多的人使用它</strong></span>，于是<span style="color: rgba(255, 0, 0, 1)"><strong>在同一年Salvatore Sanfilippo将Redis开源发布</strong></span>。</p>
<p>　　并<span style="color: rgba(255, 0, 0, 1)"><strong>开始</strong><strong>和Redis</strong></span>的另一名<span style="color: rgba(255, 0, 0, 1)"><strong>主要</strong></span>的代码<span style="color: rgba(255, 0, 0, 1)"><strong>贡献者</strong></span>Pieter Noordhuis一起<span style="color: rgba(255, 0, 0, 1)"><strong>继续</strong></span>着<span style="color: rgba(255, 0, 0, 1)"><strong>Redis</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>开发</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>直到今天</strong></span>。</p>
<p>　　Salvatore Sanfilippo自己也没有想到，短短的几年时间，Redis就拥有了庞大的用户群体。Hacker News在2012年发布一份数据库的使用请款调查，结果显示有近12%的公司在使用Redis。<span style="color: rgba(255, 0, 0, 1)"><strong>国内如新浪微博、街旁网、知乎网、国外如GitHub、Stack、Overflow、Flickr等都是Redis的用户</strong></span>。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>VmWare</strong></span>公司从<span style="color: rgba(255, 0, 0, 1)"><strong>2010年</strong></span>开始赞助Redis的开发，Salvatore Sanfilippo和Pieter Noordhuis也分别<span style="color: rgba(255, 0, 0, 1)"><strong>在3月和5月</strong><strong>加入VMware</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>全职开发Redis</strong></span>。</p>
<h1 style="text-align: center">Redis的应用场景</h1>
<ul>
<li>内存数据库(登录信息、购物车信息、用户浏览记录等)</li>
<li>缓存服务器(商品数据、广告数据等等)(最多使用)</li>
<li>解决分布式集群架构中的Session分离问题(Session共享)</li>
<li>任务队列。(秒杀、抢购、12306等等)</li>
<li>支持发布订阅的消息模式</li>
<li>应用排行榜</li>
<li>网站访问统计</li>
<li>数据过期处理(可以精确到毫秒)</li>
</ul>
<h1 style="text-align: center">Redis安装及配置</h1>
<ul>
<li>官网地址：https://redis.io/</li>
<li>中文官网地址：http://www.redis.cn</li>
<li>下载地址：http://download.redis.io/releases/</li>
</ul>
<h2>Linux环境下安装Redis</h2>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>注：将下载后的Redis拖进Linux需要安装下，VMware Tools，<a href="https://www.cnblogs.com/gucb/p/11525557.html" target="_blank">参考链接</a></strong></span></p>
<h3>将下载后的Redis拖进linux</h3>
<p><img src="https://img2018.cnblogs.com/common/1504448/201912/1504448-20191222002115544-1123107779.jpg" alt="" /></p>
<h3>安装C语言需要的GCC环境</h3>
<div class="cnblogs_code">
<pre>yum install gcc-c++</pre>
