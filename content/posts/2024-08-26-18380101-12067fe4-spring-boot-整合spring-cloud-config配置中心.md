---
title: "spring boot 整合spring cloud config配置中心"
date: 2024-08-26
description: "创建2个项目 springboot-cloud-config（作配置中心） springboot-cloud-client（客户端） springboot-cloud-config（工程） 注意：2个项目springboot版本：2.4.0 添加依赖 &lt;dependency&gt; &lt;g"
tags:
  - "Spring Boot"
  - "Spring Cloud"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/18380101/spring-cloud-config"
---

<h1 style="text-align: center">创建2个项目</h1>
<ul>
<li>springboot-cloud-config（作配置中心）</li>
<li>springboot-cloud-client（客户端）</li>
</ul>
<h1 style="text-align: center">springboot-cloud-config（工程）</h1>
<p><strong><span style="color: rgba(255, 0, 0, 1)">注意：2个项目springboot版本：2.4.0</span></strong></p>
<h2>添加依赖</h2>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.springframework.cloud<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>spring-cloud-config-server<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>3.0.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
