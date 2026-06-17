---
title: "ElasticSearch 7.8.1集群搭建"
date: 2023-05-31
description: "通往集群的大门 集群由什么用? 高可用 高可用(High Availability)是分布式系统架构设计中必须考虑的因素之一，它通常是指，通过设计减少系统不能提供服务的时间。如果系统每运行100个时间单位，会有1个时间单位无法提供服务，我们说系统的可用性是99%。 负载均衡 将流量均衡的分布在不同的"
tags:
  - "技术干货"
  - "ElasticSearch7.8.1"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13493920.html"
---

<h1 style="text-align: center">通往集群的大门</h1>
<h2>集群由什么用?</h2>
<h3>高可用</h3>
<p>　　高可用(High Availability)是分布式系统架构设计中必须考虑的因素之一，它通常是指，通过设计减少系统不能提供服务的时间。如果系统每运行100个时间单位，会有1个时间单位无法提供服务，我们说系统的可用性是99%。</p>
<h3>负载均衡</h3>
<p>　　将流量均衡的分布在不同的节点上，每个节点都可以处理一部分负载，并且可以在节点之间动态分配负载，以实现平衡。</p>
<h3>高性能</h3>
<p>　　将流量分发到不同机器，充分利用多机器多CPU，从串行计算到并行计算提供系统性能。</p>
<h1 style="text-align: center">ES集群的基本核心概念</h1>
<h2>Cluster集群</h2>
<p>　　一个ElasticSearch集群由一个或多个节点(Node)组成，每个集群都有一个共同的集群名称作为标识。</p>
<h2>Node节点</h2>
<p>　　一个ElasticSearch实例即一个Node，一台机器可以有多个实例，正常使用下每个实例应该会部署在不同机器上。ElasticSearch的配置文件中可以通过node.master、node.data来设置节点类型。</p>
<p>　　node.master：表示节点是否具有称为主节点的资格</p>
<p>　　　　true代表的是有资格竞选主节点</p>
<p>　　　　false代表的是没有资格竞选主节点</p>
<p>　　node.data：表示节点是否存储数据</p>
<h2>Node节点组合</h2>
<h3>主节点+数据节点(master+data)</h3>
<p>　　　　节点<strong><span style="color: rgba(255, 0, 0, 1)">即有称为主节点的资格，又存储数据</span></strong></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">node.master: true
node.data: true</span></pre>
