---
title: "什么是RESTful？RESTfule风格"
date: 2023-05-31
description: "导读 理解什么是REST之前，先去脑补以下什么是HTTP，参考【Http协议】 什么是REST? REST(英文：Representational State Transfer，简称REST，意思：表述性状态转换，描述了一个架构样式的网络系统，比如web应用)。 它是一种软件架构风格、设计风格，而不"
tags:
  - "JAVA"
  - "MVC"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12040880.html"
---

<h1 style="text-align: center">导读</h1>
<p>理解什么是REST之前，先去脑补以下什么是HTTP，参考【<a class="entrylistItemTitle" href="https://www.cnblogs.com/chenyanbin/p/12033469.html">Http协议</a>】</p>
<h1 style="text-align: center">什么是REST?</h1>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>REST</strong></span>(英文：Representational State Transfer，简称<span style="color: rgba(255, 0, 0, 1)"><strong>REST</strong></span>，意思：表述性状态转换，描述了一个<span style="color: rgba(255, 0, 0, 1)"><strong>架构</strong></span>样式的网络系统，比如web应用)。</p>
<p>　　它是一种软件架构风格、设计风格，而不是标准，只是提供了一组设计原则和约束条件，它主要用于<span style="color: rgba(255, 0, 0, 1)"><strong>客户端和服务端</strong></span>交互类的软件。基于这个风格设计的软件可以更简介，更有层次，更易于实现缓存等机制。</p>
<p>　　它本身并没有什么使用性，其核心价值在于如何设计出符合REST风格的网络接口。</p>
<h1 style="text-align: center">什么是RESTful？</h1>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>REST</strong></span>：指的是一组架构约束条件和原则。满足这些约束条件和原则的应用程序或设计就是<span style="color: rgba(255, 0, 0, 1)"><strong>RESTful</strong></span>。</p>
<h2>RESTful的特性</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>资源(Resources)</strong></span>：网络上的一个实体，或者说是网络上的一个具体信息。它可以是一段文本、一张图片、一首歌曲、一种服务，总之就是一个具体的存在。可以用一个URI（统一资源定位符）指向它，每种资源对应一个特性的URI。要获取这个资源，访问它的URI就可以，因此URI即为每一个资源的独一无二的识别符。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>表现层(Representation)</strong></span>：把资源具体呈现出来的形式，叫做它的表现层(Representation)。比如，文本可以用txt格式表现，也可以用HTML格式、XML格式、JSON格式表现，甚至可以采用二进制格式。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>状态转换(State Transfer)</strong></span>：每发出一个请求，就代表了客户端和服务器的一次交互过程。HTTP协议，是一个无状态协议，即所有的状态都保存在服务器端。因此，如果客户端想要操作服务器，必须通过某种手段，让服务器端发生“状态转换”(State Transfer)。而这种转换是建立在表现层之上的，所以就是“表现层状态转换”。具体说，就是HTTP协议里面，四个表示操作方式的动词：<span style="color: rgba(255, 0, 0, 1)"><strong>GET、POST、PUT、DELETE</strong></span>。他们分别对应四种基本操作：GET用来获取资源，POST用来新建资源，PUT用来更新资源，DELETE用来删除资源。</p>
<h1 style="text-align: center">如何设计RESTful应用程序的API?</h1>
<p>　　<strong>路径设计</strong>：数据库设计完毕之后，基本上就可以确定有哪些资源要进行操作，相对应的路径也可以设计出来。</p>
<p>　　<strong>动词设计</strong>：也就是针对资源的具体操作类型，有HTTP动词表示，常用的HTTP动词如下：POST、DELETE、PUT、GET</p>
<h2>RESTful示例</h2>
<ol>
<li>/account/1 HTTP GET：得到id=1的account</li>
<li>/account/1 HTTP DELETE：删除id=1的account</li>
<li>/account/1 HTTP PUT：更新id=1的account</li>
</ol>
<h1 style="text-align: center">SpringMvc对RESTful的支持</h1>
<h2>RESTful的URL路径变量</h2>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>URL-PATTERN</strong></span>：设置为<span style="color: rgba(255, 0, 0, 1)"><strong>/</strong></span>，方便拦截RESTful请求。</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>@PathVariable</strong></span>：可以解析出来URL中的模板变量(<span style="color: rgba(255, 0, 0, 1)"><strong>{id}/{name}</strong></span>)</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">URL：http://localhost:8080/ssm/cyb/item/1/chenyanbin


Controller层：
@RequestMapping("{id}/{name}")
@ResponseBody
public Item queryItemById(@PathVariable Integer id,@PathVariable String name){
.............
}</span></pre>
