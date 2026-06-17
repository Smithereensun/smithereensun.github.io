---
title: "SpringMVC 数据交互"
date: 2023-05-31
description: "为什么使用JSON进行数据交互？ JSON数据格式比较简单、解析比较方便，在接口调用及HTML页面Ajax调用时较常用。 JSON交互方式 请求是Key/Value，响应是JSON(推荐使用) 请求是JSON，响应是JSON 依赖包 &lt;dependency&gt; &lt;groupId&gt"
tags:
  - "JAVA"
  - "MVC"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12026903.html"
---

<h1 style="text-align: center">为什么使用JSON进行数据交互？</h1>
<p>　　JSON数据格式比较简单、解析比较方便，在接口调用及HTML页面Ajax调用时较常用。</p>
<h1 style="text-align: center">JSON交互方式</h1>
<ul>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>请求是Key/Value，响应是JSON(推荐使用)</strong></span></li>
<li><strong><span style="color: rgba(255, 0, 0, 1)">请求是JSON，响应是JSON</span></strong></li>
</ul>
<h1 style="text-align: center">依赖包</h1>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.fasterxml.jackson.core<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>jackson-databind<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>2.9.8<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
