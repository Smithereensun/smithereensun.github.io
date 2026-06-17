---
title: "SpringBoot启动方式"
date: 2020-07-03
description: "IDEA开发中启动 本地开发中常用 外置Tomcat中启动 接近淘汰 tomcat版本兼容问题复杂 微服务容器化部署复杂 Jar方式打包启动 官方推荐，工作中最陈昌勇 步骤：pom文件新增maven插件 &lt;build&gt; &lt;plugins&gt; &lt;plugin&gt; &lt"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13232882.html"
---

<h1>IDEA开发中启动</h1>
<ul>
<li>本地开发中常用</li>
</ul>
<h1>外置Tomcat中启动</h1>
<ul>
<li>接近淘汰</li>
<li>tomcat版本兼容问题复杂</li>
<li>微服务容器化部署复杂</li>
</ul>
<h1>Jar方式打包启动</h1>
<ul>
<li>官方推荐，工作中最陈昌勇</li>
<li>步骤：pom文件新增maven插件</li>
</ul>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">build</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">plugins</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">plugin</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.springframework.boot<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>spring-boot-maven-plugin<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">plugin</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">plugins</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">build</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span><span style="color: rgba(0, 0, 0, 1)">


如果没有，则执行jar包，会报错
执行：java -jar spring-boot-demo-0.0.1-SNAPSHOT.jar <br>报错：no main manifest attribute, in spring-boot-demo-0.0.1-SNAPSHOT.jar</span></pre>
