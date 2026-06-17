---
title: "新版SpringBoot-Spring-Mybatis事务控制"
date: 2020-07-15
description: "快速创建SpringBoot+Spring+Mybatis项目 https://start.spring.io 删除pom中mysql依赖的runtime pom.xml中添加druid依赖 &lt;dependency&gt; &lt;groupId&gt;com.alibaba&lt;/grou"
tags:
  - "ssm"
  - "Spring Boot"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13311267.html"
---

<h1 style="text-align: center">快速创建SpringBoot+Spring+Mybatis项目</h1>
<p>https://start.spring.io</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200715225724585-484408248.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h2>删除pom中mysql依赖的runtime</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200715230437286-1206038424.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h3>pom.xml中添加druid依赖</h3>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.alibaba<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>druid<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.1.23<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
