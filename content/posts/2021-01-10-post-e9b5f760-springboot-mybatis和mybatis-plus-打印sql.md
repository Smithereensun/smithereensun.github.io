---
title: "SpringBoot Mybatis和Mybatis plus 打印sql"
date: 2021-01-10
description: "mybatis plus 方式一 在logback-spring.xml中添加 &lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt; &lt;configuration scan=&quot;true&quot; scanP"
tags:
  - "Spring Boot"
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14006853.html"
---

<h1 style="text-align: center">mybatis plus</h1>
<h2>方式一</h2>
<p>　　在logback-spring.xml中添加</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;?</span><span style="color: rgba(255, 0, 255, 1)">xml version="1.0" encoding="UTF-8"</span><span style="color: rgba(0, 0, 255, 1)">?&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">configuration </span><span style="color: rgba(255, 0, 0, 1)">scan</span><span style="color: rgba(0, 0, 255, 1)">="true"</span><span style="color: rgba(255, 0, 0, 1)"> scanPeriod</span><span style="color: rgba(0, 0, 255, 1)">="10 seconds"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">logger </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="com.service.policy.mapper"</span><span style="color: rgba(255, 0, 0, 1)"> level</span><span style="color: rgba(0, 0, 255, 1)">="DEBUG"</span><span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">configuration</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
