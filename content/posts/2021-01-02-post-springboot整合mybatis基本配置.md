---
title: "SpringBoot整合Mybatis基本配置"
date: 2021-01-02
description: "application.properties # 数据库 spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver spring.datasource.url=jdbc:mysql://127.0.0.1:3306/shiro_2?us"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14224466.html"
---

<h1>application.properties</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">#============数据库=================
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/shiro_2?useUnicode=true</span><span style="color: rgba(255, 0, 0, 1)">&amp;characterEncoding</span>=utf-8<span style="color: rgba(255, 0, 0, 1)">&amp;useSSL</span><span style="color: rgba(0, 0, 0, 1)">=false
spring.datasource.username=root
spring.datasource.password=root
# 使用阿里巴巴druid数据源，默认使用自带的
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
# 开启控制台打印sql
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
# mybatis下划线转驼峰配置
mybatis.configuration.map-underscore-to-camel-case=true</span></pre>
