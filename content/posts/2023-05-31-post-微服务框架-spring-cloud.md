---
title: "微服务框架-Spring Cloud"
date: 2023-05-31
description: "Spring Cloud入门 微服务与微服务架构 微服务架构是一种新型的系统架构。其设计思路是，将单体架构系统拆分为多个可以相互调用、配合的独立运行的小程序。这每个小程序对整体系统所提供的功能就称为微服务。 由于每个微服务都具有独立运行的，所以每个微服务都独立占用一个进程。微服务间采用轻量级的HTT"
tags:
  - "Spring Cloud"
  - "分布式架构"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12608621.html"
---

<h1 style="text-align: center">Spring Cloud入门</h1>
<h2>微服务与微服务架构</h2>
<p>　　微服务架构是一种新型的系统架构。其设计思路是，将单体架构系统拆分为多个可以相互调用、配合的独立运行的小程序。这每个小程序对整体系统所提供的功能就称为微服务。</p>
<p>　　由于每个微服务都具有独立运行的，所以每个微服务都独立占用一个进程。微服务间采用轻量级的HTTP RESTFUL协议通信。每个微服务程序不受编程语言的限制，整个系统关心的是微服务程序所提供的具体服务，并不关心其具体的实现。每个微服务可以有自己独立的数据库。即可以操作自己的独立数据，也可以操作整体系统的数据库。</p>
<h2>Spring Cloud简介</h2>
<h3>百度百科介绍</h3>
<p>　　Spring Cloud是一系列框架的有序集合。它利用Spring Boot的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中心、消息总线、负载均衡、断路器、数据监控等，都可以用Spring Boot的开发风格做到一键启动和部署。Spring Cloud并没有重复制造轮子，它只是将各家公司开发的比较成熟、经得起实际考验的服务框架组合起来，通过Spring Boot风格进行再封装屏蔽了复杂的配置和实现原理，最终给开发者流出了一套简单易懂、易部署和易维护的分布式系统开发工具包。</p>
<h3>Spring Cloud中文网</h3>
<p>https://www.springcloud.cc/</p>
<h3>Spring Cloud中国社区</h3>
<p>http://www.springcloud.cn/</p>
<h2>服务提供者项目</h2>
<p>　　本示例使用Spring的RestTemplate实现消费者对提供者的调用，并未使用到Spring Cloud，但其为后续Spring Cloud的运行测试环境。使用MySql数据库，使用Spring Data JPA作为持久层技术。</p>
<h3>创建工程</h3>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202003/1504448-20200331215248515-31669520.png" alt="" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202003/1504448-20200331215523116-639749625.png" alt="" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202003/1504448-20200331220158040-1770968957.png" alt="" /></p>
<h3>添加Druid依赖</h3>
<p>pom.xml</p>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">Druid依赖</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.alibaba<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>druid<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.1.10<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
