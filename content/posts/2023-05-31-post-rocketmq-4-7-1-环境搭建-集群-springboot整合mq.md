---
title: "RocketMQ 4.7.1 环境搭建、集群、SpringBoot整合MQ"
date: 2023-05-31
description: "导读 之前学过ActiveMQ但是并发量不是很大点我直达，所以又学阿里开源的RocketMQ，据说队列可以堆积亿级别。下面是网上找的消息队列对比图，仅供参考 部署 官网 点我直达 前置条件 推荐使用64位操作系统，建议使用Linux / Unix / Mac； 64位JDK 1.8+; Maven"
tags:
  - "技术干货"
  - "MQ"
  - "Spring Boot"
  - "分布式架构"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13798952.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　之前学过ActiveMQ但是并发量不是很大<a href="https://www.cnblogs.com/chenyanbin/p/12841966.html" target="_blank">点我直达</a>，所以又学阿里开源的RocketMQ，据说队列可以堆积<span style="color: rgba(255, 0, 0, 1)"><strong>亿级别</strong></span>。下面是网上找的消息队列对比图，仅供参考</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201015001549671-432898679.png" alt="" loading="lazy" /></p>
<h1 style="text-align: center">部署</h1>
<h2>官网</h2>
<p><a href="http://rocketmq.apache.org/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<h2>前置条件</h2>
<ol>
<li><span>推荐使用64位操作系统，建议使用Linux / Unix / Mac；</span></li>
<li><span>64位JDK 1.8+;</span></li>
<li><span>Maven 3.2.x;</span></li>
<li><span>Git;</span></li>
<li><span>适用于Broker服务器的内存4G +可用磁盘</span></li>
</ol>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201011194313128-1455126295.gif" alt="" loading="lazy" /></p>
<h2>下载</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201011194924233-621417411.gif" alt="" loading="lazy" /></p>
<p>地址：<a href="https://downloads.apache.org/rocketmq/4.7.1/rocketmq-all-4.7.1-source-release.zip" rel="noopener nofollow">https://downloads.apache.org/rocketmq/4.7.1/rocketmq-all-4.7.1-source-release.zip</a>&nbsp;</p>
<p>百度云盘：</p>
<div class="cnblogs_code">
<pre>链接: https://pan.baidu.com/s/1luq_MwxSn8k_bugrnQSJWg  密码: varj</pre>
