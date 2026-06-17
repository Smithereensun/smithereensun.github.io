---
title: "Spring Cloud Gateway接口限流处理"
date: 2023-03-21
description: "添加依赖 &lt;!-- 令牌桶限流 --&gt; &lt;dependency&gt; &lt;groupId&gt;com.github.vladimir-bukhtoyarov&lt;/groupId&gt; &lt;artifactId&gt;bucket4j-core&lt;/artifa"
tags:
  - "Spring Boot"
  - "Spring Cloud"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/17240960.html"
---

<h1 style="text-align: center">添加依赖</h1>
<div class="cnblogs_code">
<pre>       <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 令牌桶限流 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.github.vladimir-bukhtoyarov<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>bucket4j-core<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>7.5.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
