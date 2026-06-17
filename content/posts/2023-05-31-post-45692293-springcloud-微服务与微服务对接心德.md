---
title: "SpringCloud 微服务与微服务对接心德"
date: 2023-05-31
description: "导读 先简单介绍下背景，公司里的项目，有一块需要与公司里的其他项目组对接。我们这边用的注册中心Nacos，对方用的eureka，之前都是自己写接口，然后服务中引入这个接口工程，都是注册到同一个注册中心中，百度查了下，可以使用@FeignClient远程调用人家服务。 首先 对方已经提供好一个API文"
tags:
  - "Spring Cloud"
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13880521.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　先简单介绍下背景，公司里的项目，有一块需要与公司里的其他项目组对接。我们这边用的注册中心Nacos，对方用的eureka，之前都是自己写接口，然后服务中引入这个接口工程，都是注册到同一个注册中心中，百度查了下，可以使用@FeignClient远程调用人家服务。</p>
<h2>首先</h2>
<p>　　对方已经提供好一个API文档，然后传一堆传输，返回给我一些信息。如下</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201026191328356-1886340527.png" alt="" loading="lazy" /></p>
<h2>然后</h2>
<p>　　我这边创建实体类，返回值这些东西，如下</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201026191832210-562279817.gif" alt="" loading="lazy" /></p>
<p>　　接口如下</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201026192425867-599214457.png" alt="" loading="lazy" /></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">@FeignClient还有以下标签

name：指定FeignClient的名称，如果项目使用了Ribbon，name属性会作为微服务的名称，用于服务发现
url: url一般用于调试，可以手动指定@FeignClient调用的地址
decode404:当发生http 404错误时，如果该字段位true，会调用decoder进行解码，否则抛出FeignException
configuration: Feign配置类，可以自定义Feign的Encoder、Decoder、LogLevel、Contract
fallback: 定义容错的处理类，当调用远程接口失败或超时时，会调用对应接口的容错逻辑，fallback指定的类必须实现@FeignClient标记的接口
fallbackFactory: 工厂类，用于生成fallback类示例，通过这个属性我们可以实现每个接口通用的容错逻辑，减少重复的代码
path: 定义当前FeignClient的统一前缀</span></pre>
