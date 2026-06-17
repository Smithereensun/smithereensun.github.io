---
title: "Spring的AOP快速实现通用日志打印"
date: 2020-07-15
description: "需求分析 针对VideoService接口实现日志打印 三个核心包 spring-aop：AOP核心功能，例如代理工厂 aspectjweaver：简单理解，支持切入点表达式 aspectjrt：简单理解，支持aop相关注解 定义Service接口和实现类 VideoService.java pac"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13306527.html"
---

<h1 style="text-align: center">需求分析</h1>
<p>　　针对VideoService接口实现日志打印</p>
<h1 style="text-align: center">三个核心包</h1>
<ul>
<li>spring-aop：AOP核心功能，例如代理工厂</li>
<li>aspectjweaver：简单理解，支持切入点表达式</li>
<li>aspectjrt：简单理解，支持aop相关注解</li>
</ul>
<h1 style="text-align: center">定义Service接口和实现类</h1>
<p>VideoService.java</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.servicce;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.domain.Video;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">interface</span><span style="color: rgba(0, 0, 0, 1)"> VideoService {
    </span><span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> save(Video video);
    Video findById(</span><span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> id);
}</span></pre>
