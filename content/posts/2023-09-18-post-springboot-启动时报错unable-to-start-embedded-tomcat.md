---
title: "SpringBoot 启动时报错Unable to start embedded Tomcat"
date: 2023-09-18
description: "导读 最近公司有个gradle构建的工程，需要改造成maven方式构建（点我直达）。转为maven后，启动时一直报tomcat错误，最终排查是因为servlet-api这个包导致的依赖冲突，将这个依赖排除即可启动 解决 排除依赖，检查项目是否包含：javax.servlet-api &lt;excl"
tags:
  - "Spring Boot"
  - "Maven"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/17712976.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　最近公司有个gradle构建的工程，需要改造成maven方式构建（<a href="https://www.cnblogs.com/chenyanbin/p/gradle.html" target="_blank">点我直达</a>）。转为maven后，启动时一直报tomcat错误，最终排查是因为servlet-api这个包导致的依赖冲突，将这个依赖排除即可启动</p>
<h2>解决</h2>
<p>排除依赖，检查项目是否包含：<strong><span style="color: rgba(255, 0, 0, 1)">javax.servlet-api</span></strong></p>
<div class="cnblogs_code">
<pre>   <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">exclusions</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">exclusion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>javax.servlet<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>javax.servlet-api<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">exclusion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">exclusions</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
