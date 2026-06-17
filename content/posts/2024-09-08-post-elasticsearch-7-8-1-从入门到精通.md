---
title: "ElasticSearch 7.8.1 从入门到精通"
date: 2024-09-08
description: "学前导读 ElasticSearch对电脑配置要求较高，内存至少4G以上，空闲2G内存，线程数4018+ 学习的时候，推荐将ElasticSearch安装到Linux或者mac上，极度不推荐装Windows上(坑太多，服务器部署的时候，也不会部署到Window上，学习用Windows上玩，不是耽误自"
tags:
  - "ElasticSearch7.8.1"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13419497.html"
---

<h1 style="text-align: center">学前导读</h1>
<ol>
<li><strong><span style="color: rgba(255, 0, 0, 1)">ElasticSearch</span></strong><span style="color: rgba(255, 0, 0, 1)"><strong>对电脑配置要求较高</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>内存至少4G以上，空闲2G内存，线程数4018+</strong></span></li>
<li>学习的时候，<span style="color: rgba(255, 0, 0, 1)"><strong>推荐将ElasticSearch安装到Linux或者mac上</strong></span>，极度<span style="color: rgba(255, 0, 0, 1)"><strong>不推荐装Windows上</strong></span>(坑太多，服务器部署的时候，也不会部署到Window上，学习用Windows上玩，不是耽误自个时间麽)。如果是Window用户想学这个，电脑自身至少16G，然后装虚拟机，在虚拟机上搞个Linux玩</li>
<li>Linux系统不建议装6/6.5版本的(启动的时候，会检查内核是否3.5+，当然可以忽略这个检查)，推荐装7+</li>
<li>自身电脑配置不高的话，怎么办呢？土豪做法，去买个云服务器叭，在云服务器上玩</li>
</ol>
<h2>注意事项</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>上面第1、2点未满足，又舍不得去买云服务器的小伙伴，就不要往下面看了，看了也白看，ElasticSearch对电脑配置要求较高，前置条件未满足的话，服务是起不来的。</strong></span></p>
<h2>演示环境说明</h2>
<p>　　我演示的时候，是用的mac系统，上面装了个虚拟机，虚拟机版本Centos6.5，jdk用的13，ElasticSearch用的版本是 7.8.1。这些<span style="color: rgba(255, 0, 0, 1)"><strong>我使用的包我下面也会提供</strong></span>，为了学习的话，尽量和我使用的版本一致，这样大家碰到的问题都一样，安装过程中，我也猜了不少坑，都总结出来了，仔细阅读文档就可以捣鼓出来。</p>
<h1 style="text-align: center">什么是搜索引擎？</h1>
<p>　　常用的搜索网站：百度、谷歌</p>
<h2>数据的分类</h2>
<h3>结构化数据</h3>
<p>　　指具有固定格式或有限长度的数据，如数据库，元数据等。对于结构化数据，我们一般都是可以通过<span style="color: rgba(255, 0, 0, 1)"><strong>关系型数据库</strong></span>（mysql、oracle）的table的<span style="color: rgba(255, 0, 0, 1)"><strong>方法存储和搜索</strong></span>，也可以建立索引。通过b-tree等数据结构快速搜索数据</p>
<h3>非结构化数据</h3>
<p>　　全文数据，指<span style="color: rgba(255, 0, 0, 1)"><strong>不定长或无固定格式的数据</strong></span>，如邮件，word等。对于非结构化数据，也即对全文数据的搜索主要有两种方式：<span style="color: rgba(255, 0, 0, 1)"><strong>顺序扫描法，全文搜索法</strong></span></p>
<h4>顺序扫描法</h4>
<p>　　我们可以了解它的大概搜索方式，就是按照顺序扫描的方式查找特定的关键字。比如让你在一篇篮球新闻中，找出“科比”这个名字在那些段落出现过。那你肯定需要从头到尾把文章阅读一遍，然后标出关键字在哪些地方出现过</p>
<p>　　这种方式毋庸置疑是最低效的，如果文章很长，有几万字，等你阅读完这篇新闻找到“科比”这个关键字，那得花多少时间</p>
<h4>全文搜索</h4>
<p>　　对非结构化数据进行顺序扫描很慢，我们是否可以进行优化？把非结构化数据想办法弄得有一定结构不就好了嘛？将非结构化数据中的一部分信息提取出来，重新组织，使其变得有一定结构，然后对这些有一定结构的数据进行搜索，从而达到搜索相对较快的目的。这种方式就构成了全文搜索的基本思路。这部分从非结构化数据提取出的然后重新组织的信息，就是索引。</p>
<h3>什么是全文搜索引擎</h3>
<p>　　根据百度百科中的定义，全文搜索引擎是目前广泛应用的主流搜索引擎。它的工作原理是计算机索引程序通过扫描文章中的每个词，对每个词建立一个索引，指明该词在文章中出现的次数和位置，当用户查询时，检索程序就根据事先建立的索引进行查找，并将查找的结果反馈给用户。</p>
<h2>常见的搜索引擎</h2>
<h3>Lucene</h3>
<ul>
<li>Lucene是一个<span style="color: rgba(255, 0, 0, 1)"><strong>Java全文搜索引擎</strong></span>，完全用<span style="color: rgba(255, 0, 0, 1)"><strong>Java编写</strong></span>。lucene<span style="color: rgba(255, 0, 0, 1)"><strong>不是一个完整的应用程序</strong></span>，而是一个代码库和API，可以很容易地用于向应用程序添加搜索功能</li>
<li>通过简单的API提供强大的功能
<ul>
<li>可扩展的高性能索引</li>
<li>强大，准确，高效的搜索算法</li>
<li>跨平台解决方案</li>
</ul>
</li>
<li>Apache软件基金会
<ul>
<li>在Apache软件基金会提供的开源软件项目的Apache社区的支持</li>
<li>但是Lucene只是一个框架，要充分利用它的功能，需要使用Java，并且在程序中集成Lucene。需要很多的学习了解，才能明白它是如何运行的，熟练运用Lucene确实非常复杂</li>
</ul>
</li>
</ul>
<h3>Solr</h3>
<ul>
<li>Solr是一个基于Lucene的Java库构建的开源搜索平台。它以友好的方式提供Apache Lucene的搜索功能。它是一个成熟的产品，拥有强大而广泛的用户社区。它能提供分布式索引，复制，负载均衡以及自动故障转移和恢复。如果它被正确部署然后管理的好，他就能够成为一个高可用，可扩展且容错的搜索引擎</li>
<li>强大功能
<ul>
<li>全文搜索</li>
<li>突出</li>
<li>分面搜索</li>
<li>实时索引</li>
<li>动态集群</li>
<li>数据库集成</li>
<li>NoSQL功能和丰富的文档处理</li>
</ul>
</li>
</ul>
<h3>ElasticSearch</h3>
<ul>
<li>ElasticSearch是一个开源，是一个机遇Apache Lucene库构建的Restful搜索引擎</li>
<li>ElasticSearch是Solr之后几年推出的。它提供了一个分布式，多租户能力的全文搜索引擎，具有HTTP Web页面和无架构JSON文档。ElasticSearch的官方客户端提供Java、Php、Ruby、Perl、Python、.Net和JavaScript</li>
<li>主要功能
<ul>
<li>分布式搜索</li>
<li>数据分析</li>
<li>分组和聚合</li>
</ul>
</li>
<li>应用场景
<ul>
<li>维基百科</li>
<li>Stack Overflow</li>
<li>GitHub</li>
<li>电商网站</li>
<li>日志数据分析</li>
<li>商品价格监控网站</li>
<li>BI系统</li>
<li>站内搜索</li>
<li>篮球论坛</li>
</ul>
</li>
</ul>
<h1 style="text-align: center">搜索引擎的快速搭建</h1>
<h2>环境准备</h2>
<p>　　注意，<span style="color: rgba(255, 0, 0, 1)"><strong>我使用的linux搭建的</strong></span>，当然Window(极度不推荐，坑太多)也能搭建，<span style="color: rgba(255, 0, 0, 1)"><strong>ElasticSearch安装前需要先安装jdk</strong></span>，这里<span style="color: rgba(255, 0, 0, 1)"><strong>我使用的是jdk13</strong></span>，因为linux自带jdk版本，需要先将之前的jdk版本卸载(<a href="https://www.cnblogs.com/chenyanbin/p/12843149.html" target="_blank">点我直达</a>)，在安装指定的jdk版本!!!</p>
<p>　　开发环境，建议关闭防火墙，避免不必要的麻烦！！！！生产环境，视情况开启端口号！！！！</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">service iptables stop   命令关闭防火墙，但是系统重启后会开启

chkconfig iptables off--关闭防火墙开机自启动</span></pre>
