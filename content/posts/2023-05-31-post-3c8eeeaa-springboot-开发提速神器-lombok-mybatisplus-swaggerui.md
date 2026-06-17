---
title: "SpringBoot 开发提速神器 Lombok+MybatisPlus+SwaggerUI"
date: 2023-05-31
description: "导读 Lombok：可以让你的POJO代码特别简洁，不止简单在BO/VO/DTO/DO等大量使用，还有设计模式，对象对比等 MybatisPlus：增加版Mybatis，基础的数据库CRUD、分页等可以直接生成使用，避免了大量的重复低效代码，还有数据库自动Java类，sql文件等等，比传统的更贱简介"
tags:
  - "Spring Boot"
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/mybatis-plus.html"
---

<h1 style="text-align: center">导读</h1>
<ul>
<li>Lombok：可以让你的POJO代码特别简洁，不止简单在BO/VO/DTO/DO等大量使用，还有设计模式，对象对比等</li>
<li>MybatisPlus：增加版Mybatis，基础的数据库CRUD、分页等可以直接生成使用，避免了大量的重复低效代码，还有数据库自动Java类，sql文件等等，比传统的更贱简介易用</li>
<li>SwaggerUI：接口文档自动生成，对接前端和测试更加方便，基于业界的OpennApi规范，采用Swagger3.x版本。</li>
</ul>
<h2>技术栈</h2>
<p>　　SpringBoot2.4+ MybatisPlus+Lombok+Swagger3.x+jdk8+IDEA</p>
<h1 style="text-align: center">在线构建项目</h1>
<p><a href="https://start.spring.io/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202103/1504448-20210302213523790-114668314.png" alt="" loading="lazy" /></p>
<h1 style="text-align: center">什么是lombok</h1>
<h2>官网</h2>
<p><a href="https://projectlombok.org/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p>　　一个优秀的Java代码库，简化了Java的编码，为Java代码的精简提供了一种方式</p>
<h2>添加依赖</h2>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">lombok</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.projectlombok<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>lombok<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.18.16<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">scope=provided，说明它是在编译阶段生效，不需要打入包中，Lombok在编译期将带Lombok注解的Java文件正确编译为完整的Class文件</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">scope</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>provided<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">scope</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
