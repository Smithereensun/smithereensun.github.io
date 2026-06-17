---
title: "RocketMQ4.7.1双主双从集群搭建"
date: 2023-05-31
description: "导读 上一集我们已经学会了SpringBoot整合RocketMQ点我直达，今天我们来搭建双主双从高性能MQ服务集群。 简介 主从架构 Broker角色，Master提供读写，Slave只支持读，Consumer不用配置，当Master不可用或者繁忙的时候，Consumer会自动切换到Slave节点"
tags:
  - "MQ"
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13894216.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　上一集我们已经学会了SpringBoot整合RocketMQ<a href="https://www.cnblogs.com/chenyanbin/p/13798952.html" target="_blank">点我直达</a>，今天我们来搭建双主双从高性能MQ服务集群。</p>
<h1 style="text-align: center">简介</h1>
<h2>主从架构</h2>
<p>　　Broker角色，Master提供读写，Slave只支持读，Consumer不用配置，当Master不可用或者繁忙的时候，Consumer会自动切换到Slave节点进行读取。<span style="color: rgba(255, 0, 0, 1)"><strong>双主双从，同步复制，异步刷盘</strong></span>。</p>
<h2>集群配置(4台机器)</h2>
<ol>
<li>两台部署Broker-Master和NameServer</li>
<li>两台部署Broker-Slave和NameServer</li>
</ol>
<h2>前置条件</h2>
<ul>
<li>Maven</li>
<li>Git</li>
<li>Jdk1.8</li>
<li>RocketMQ 4.7.1</li>
<li>4台机器，ip分别为如下
<ul>
<li>192.168.199.110(<span style="color: rgba(255, 0, 0, 1)"><strong>主</strong></span>)</li>
<li>192.168.199.120(<span style="color: rgba(255, 0, 0, 1)"><strong>从</strong></span>)</li>
<li>192.168.199.130(<span style="color: rgba(255, 0, 0, 1)"><strong>主</strong></span>)</li>
<li>192.168.199.140(<span style="color: rgba(255, 0, 0, 1)"><strong>从</strong></span>)</li>
</ul>
</li>
</ul>
<h1 style="text-align: center">搭建</h1>
<h2>安装依赖项</h2>
<ol>
<li>jdk：<a href="https://www.cnblogs.com/chenyanbin/p/12843149.html" target="_blank">点我直达</a></li>
<li>maven：<a href="https://www.cnblogs.com/chenyanbin/p/13662849.html" target="_blank">点我直达</a></li>
<li>git安装：<strong><span style="color: rgba(255, 0, 0, 1)">yum install -y git</span></strong></li>
</ol>
<h2>上传相应文件及安装目录</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201029231733721-738735839.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201029233223018-1570503346.png" alt="" loading="lazy" /></p>
<h3>maven编译</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">cd /opt/soft/rocketmq-all-4.7.1-source-release


mvn -Prelease-all -DskipTests clean install -U</span></pre>
