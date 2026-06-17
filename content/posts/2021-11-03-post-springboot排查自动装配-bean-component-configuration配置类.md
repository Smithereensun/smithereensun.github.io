---
title: "SpringBoot排查自动装配、Bean、Component、Configuration配置类"
date: 2021-11-03
description: "排除自动装配AutoConfiguration @SpringBootApplication( exclude = { DataSourceAutoConfiguration.class, MybatisPlusAutoConfiguration.class } ) 配置Congfiguration"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15504669.html"
---

<h1 style="text-align: center">排除自动装配AutoConfiguration</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">@SpringBootApplication(
        exclude </span>=<span style="color: rgba(0, 0, 0, 1)"> {
                DataSourceAutoConfiguration.</span><span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)">,
                MybatisPlusAutoConfiguration.</span><span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)">
        }
)</span></pre>
