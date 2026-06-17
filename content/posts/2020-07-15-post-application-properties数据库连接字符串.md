---
title: "application.properties数据库连接字符串"
date: 2020-07-15
description: "spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver spring.datasource.url=jdbc:mysql://localhost:3306/cybclass?useUnicode=true&amp;characterE"
tags:
  - "配置文件"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13308835.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/cybclass?useUnicode=true</span><span style="color: rgba(255, 0, 0, 1)">&amp;characterEncoding</span>=UTF-8<span style="color: rgba(255, 0, 0, 1)">&amp;serverTimezone</span><span style="color: rgba(0, 0, 0, 1)">=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=root
# 使用阿里巴巴druid数据源，默认使用自带
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
#开启控制台打印sql
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl</span></pre>
