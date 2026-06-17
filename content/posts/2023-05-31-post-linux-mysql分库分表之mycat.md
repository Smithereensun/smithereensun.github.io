---
title: "Linux MySQL分库分表之Mycat"
date: 2023-05-31
description: "介绍 背景 当表的个数达到了几百千万张表时，众多的业务模块都访问这个数据库，压力会比较大，考虑对其进行分库 当表的数据达到几千万级别，在做很多操作都比较吃力，考虑对其进行分库或分表 数据切分(sharding)方案 数据的切分（Sharding）根据其切分规则的类型，可以分为两种切分模式： 垂直切分"
tags:
  - "Linux"
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13159469.html"
---

<h1 style="text-align: center">介绍</h1>
<h2>背景</h2>
<ul>
<li>当<span style="color: rgba(255, 0, 0, 1)"><strong>表的个数达到了几百千万张表</strong></span>时，众多的业务模块都访问这个数据库，压力会比较大，考虑对其进行分库</li>
<li>当<span style="color: rgba(255, 0, 0, 1)"><strong>表的数据达到几千万级别</strong></span>，在做很多操作都比较吃力，考虑对其进行分库或分表</li>
</ul>
<h2>数据切分(sharding)方案</h2>
<p>　　数据的切分（Sharding）根据其切分规则的类型，可以分为两种切分模式：</p>
<ul>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>垂直切分</strong></span>：按照业务模块进行切分，将不同模块的表切分到不同的数据库中</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>水平切分</strong></span>，将一张大表按照一定的切分规则，按照行切分成不同的表或者切分到不同的库中</li>
</ul>
<h3>如何理解垂直切分？</h3>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>垂直分库</strong></span>：主要<span style="color: rgba(255, 0, 0, 1)"><strong>解决</strong></span>的问题是单个数据库中[<span style="color: rgba(255, 0, 0, 1)"><strong>数据表</strong></span>]<span style="color: rgba(255, 0, 0, 1)"><strong>过多问题</strong></span>。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>垂直分表</strong></span>：主要<span style="color: rgba(255, 0, 0, 1)"><strong>解决</strong></span>的问题是单个<span style="color: rgba(255, 0, 0, 1)"><strong>表</strong></span>中[<strong><span style="color: rgba(255, 0, 0, 1)">过多</span></strong>问题(将一张大表，拆分不同的关联表)。</p>
<h3>如何理解水平切分？</h3>
<p>　　水平切分主要<span style="color: rgba(255, 0, 0, 1)"><strong>解决</strong></span>的问题就是对于[<span style="color: rgba(255, 0, 0, 1)"><strong>单表数据量过大</strong></span>]的问题(1000W以上数据性能会有所下降)</p>
<h3>切分原则</h3>
<ol>
<li>能不切尽量不要切分</li>
<li>如果要切分一定要选择合适的切分规则，提前规划好</li>
<li>数据切分尽量通过冗余或表分组(Table Group)来降低跨库Join的可能</li>
<li>由于数据库中间件对数据Join实现的优劣难以把握，而且实现高性能难度极大，业务读取尽量少使用多表Join</li>
</ol>
<h3>分库分表之后带来问题？</h3>
<ol>
<li>跨库Join：订单表需要关联会员信息(订单表和会员表拆分为两个库的表)<ol>
<li>应用层由一个查询拆分为多个</li>
<li>全局表，每个库都存储相同的数据，比如字典表、地址表</li>
<li>字段冗余</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>Mycat技术可以实现跨库Join，只能实现2张表跨库Join</strong></span></li>
</ol></li>
<li>分布式事务(Mycat没有很好实现分布式事务)<ol>
<li>强一致性(互联网项目不推荐，性能不好)</li>
<li>最终一致性(异步方式去实现，需要通过日志信息)</li>
</ol></li>
<li>主键问题(保证ID的连续性和唯一性)<ol>
<li>UUID(性能不好)</li>
<li>redis incr命令</li>
<li>zookeeper</li>
<li>雪花算法</li>
</ol></li>
<li>跨库进行排序问题<ol>
<li>在应用层进行排序</li>
</ol></li>
</ol>
<h1 style="text-align: center">Mycat应用</h1>
<h2>官网链接</h2>
<p><a href="http://www.mycat.org.cn/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<h2>Mycat核心概念</h2>
<ul>
<li><strong>Schema</strong>：由它制定逻辑数据库(相当于MySQL的database数据库)</li>
<li><strong>Table</strong>：逻辑表(相当于MySQL的table表)</li>
<li><strong>DataNode</strong>：真正存储数据的物理节点</li>
<li><strong>DataHost</strong>：存储节点所在的数据库主机(指定MySQL数据库的连接信息)</li>
<li><strong>User</strong>：MyCat的用户(类似于MySQL的用户，支持多用户)</li>
</ul>
<h2>MyCat主要解决的问题</h2>
<ul>
<li>海量数据存储</li>
<li>查询优化</li>
</ul>
<h2>Mycat对数据库的支持</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200619151137867-1309609552.png" alt="" loading="lazy" /></p>
<h2>Mycat安装</h2>
<h3>安装要求</h3>
<ul>
<li>
<h4>jdk：要求jdk必须是1.7及以上版本 （<span style="color: rgba(255, 0, 0, 1)">我使用的是jdk 1.8</span>）</h4>
</li>
<li>
<h4>Mysql：推荐mysql是5.5以上版本（<strong><span style="color: rgba(255, 0, 0, 1)">我使用的是mysql 5.7</span></strong>）</h4>
</li>
</ul>
<h3>安装jdk</h3>
<p>具体教程：<a href="https://www.cnblogs.com/chenyanbin/p/12843149.html" target="_blank">点我直达</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200619150705902-954523072.png" alt="" loading="lazy" /></p>
<h3>Mcat下载</h3>
<p>下载链接：<a href="https://github.com/MyCATApache/Mycat-download" target="_blank" rel="noopener nofollow">点我直达</a></p>
<div class="cnblogs_code">
<pre>百度云盘地址：https://pan.baidu.com/s/14A3BAwnBRGZppc3AicF5Hw  密码: gkrp</pre>
