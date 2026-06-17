---
title: "Spring Cloud 整合分布式链路追踪系统Sleuth和ZipKin实战，分析系统瓶颈"
date: 2023-05-31
description: "导读 微服务架构中，是否遇到过这种情况，服务间调用链过长，导致性能迟迟上不去，不知道哪里出问题了，巴拉巴拉....，回归正题，今天我们使用SpringCloud组件，来分析一下微服务架构中系统调用的瓶颈问题~ SpringCloud链路追踪组件Sleuth实战 官网 主要功能：做日志埋点 什么是Sl"
tags:
  - "技术干货"
  - "Spring Cloud"
  - "分布式架构"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/zipkin.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　微服务架构中，是否遇到过这种情况，<span style="color: rgba(255, 0, 0, 1)"><strong>服务间调用链过长</strong></span>，导致<span style="color: rgba(255, 0, 0, 1)"><strong>性能</strong></span>迟迟<span style="color: rgba(255, 0, 0, 1)"><strong>上不去</strong></span>，不知道哪里出问题了，巴拉巴拉....，回归正题，今天我们使用SpringCloud组件，来分析一下微服务架构中系统调用的瓶颈问题~</p>
<h1 style="text-align: center">SpringCloud链路追踪组件Sleuth实战</h1>
<h2>官网</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202011/1504448-20201113000642215-1834452298.gif" alt="" loading="lazy" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202011/1504448-20201113000726273-2072565519.gif" alt="" loading="lazy" /></p>
<p>　　主要功能：做日志埋点</p>
<h2>什么是Sleuth</h2>
<p>　　专门用于追踪每个请求的完整调用链路。</p>
<p>　　例如：【order-service,f674cc8202579a50,4727309367e0b514,false】</p>
<ul>
<li style="list-style-type: none">
<ul>
<li>第一个值：spring.application.name</li>
<li>第二个值，sleuth生成的一个ID，交Trace ID，用来标识一条请求链路，一条请求链路中包含一个Trace ID，多个Span ID</li>
<li>第三个值：spanid基本的工作单元，获取元数据，如发送一个http请求</li>
<li>第四个值：false，是否要将该信息输出到zipkin服务中来收集和展示</li>
</ul>
</li>
</ul>
<h2>添加依赖</h2>
<p>　　牵扯到的服务都得加这个依赖！(我这里是在order-service、product-service加的依赖)</p>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.springframework.cloud<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>spring-cloud-starter-sleuth<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
