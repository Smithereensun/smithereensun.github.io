---
title: "SpringBoot 2.5.5整合轻量级的分布式日志标记追踪神器TLog"
date: 2023-05-31
description: "TLog能解决什么痛点 随着微服务盛行，很多公司都把系统按照业务边界拆成了很多微服务，在排错查日志的时候。因为业务链路贯穿着很多微服务节点，导致定位某个请求的日志以及上下游业务的日志会变得有些困难。 这时候很多童鞋会开始考虑上SkyWalking，Pinpoint等分布式追踪系统来解决，基于Open"
tags:
  - "Spring Boot"
  - "配置文件"
  - "Spring Cloud"
  - "TLog"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/16804650.html"
---

<h1 style="text-align: center">TLog能解决什么痛点</h1>
<p>　　随着微服务盛行，很多公司都把系统按照业务边界拆成了很多微服务，在排错查日志的时候。因为业务链路贯穿着很多微服务节点，导致定位某个请求的日志以及上下游业务的日志会变得有些困难。</p>
<p>　　这时候很多童鞋会开始考虑上<a href="https://www.cnblogs.com/chenyanbin/p/16353771.html" target="_blank">SkyWalking</a>，Pinpoint等分布式追踪系统来解决，基于OpenTracing规范，而且通常都是无侵入性的，并且有相对友好的管理界面来进行链路Span的查询。</p>
<p>但是搭建分布式追踪系统，熟悉以及推广到全公司的系统需要一定的时间周期，而且当中涉及到链路span节点的存储成本问题，全量采集还是部分采集？如果全量采集，就以SkyWalking的存储来举例，ES集群搭建至少需要5个节点。这就需要增加服务器成本。况且如果微服务节点多的话，一天下来产生几十G上百G的数据其实非常正常。如果想保存时间长点的话，也需要增加服务器磁盘的成本。</p>
<p>当然分布式追踪系统是一个最终的解决方案，如果您的公司已经上了分布式追踪系统，那<a href="https://tlog.yomahub.com/" target="_blank" rel="noopener nofollow">TLog</a>并不适用。</p>
<h1 style="text-align: center">项目整合</h1>
<h2>项目结构</h2>
<p><img src="https://img2022.cnblogs.com/blog/1504448/202210/1504448-20221018230838317-55155903.png" alt="" loading="lazy" /></p>
<h2>添加依赖</h2>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 引入全量tlog依赖 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.yomahub<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>tlog-all-spring-boot-starter<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.5.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
