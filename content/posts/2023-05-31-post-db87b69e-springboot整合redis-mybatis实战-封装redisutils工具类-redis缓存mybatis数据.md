---
title: "SpringBoot整合Redis、mybatis实战，封装RedisUtils工具类，redis缓存mybatis数据 附源码"
date: 2023-05-31
description: "导读 Redis不了解的小伙伴，先去脑补下Redis从入门到精通，点我直达。在看下面的东西哟~ 创建SpringBoot项目 在线创建方式 网址：https://start.spring.io/ 然后创建Controller、Mapper、Service包 SpringBoot整合Redis 引入R"
tags:
  - "技术干货"
  - "Spring Boot"
  - "NoSql"
  - "Redis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13515268.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　Redis不了解的小伙伴，先去脑补下Redis从入门到精通，<a href="https://www.cnblogs.com/chenyanbin/p/12073107.html" target="_blank">点我直达</a>。在看下面的东西哟~</p>
<h1 style="text-align: center">创建SpringBoot项目</h1>
<h2>在线创建方式</h2>
<p>网址：<a href="https://start.spring.io/" target="_blank" rel="noopener nofollow">https://start.spring.io/</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200816234343715-1015667708.png" alt="" loading="lazy" /></p>
<h2>然后创建Controller、Mapper、Service包</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200816232800559-1389541947.png" alt="" loading="lazy" /></p>
<h1 style="text-align: center">SpringBoot整合Redis</h1>
<h2>引入Redis依赖</h2>
<div class="cnblogs_code">
<pre>        &lt;!--SpringBoot与Redis整合依赖--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
            &lt;artifactId&gt;spring-boot-starter-data-redis&lt;/artifactId&gt;
        &lt;/dependency&gt;</pre>
