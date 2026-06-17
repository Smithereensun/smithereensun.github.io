---
title: "新版SpringBoot-Spring-Mybatis 数据库相关配置"
date: 2020-07-16
description: "application.properties server.port=8081 # 数据库相关配置 spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver spring.datasource.url=jdbc:mysql://loca"
tags:
  - "配置文件"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13321752.html"
---

<p>application.properties</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">server.port=8081
# ========================数据库相关配置=====================
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/online_ybclass?useUnicode=true</span><span style="color: rgba(255, 0, 0, 1)">&amp;characterEncoding</span>=UTF-8<span style="color: rgba(255, 0, 0, 1)">&amp;serverTimezone</span><span style="color: rgba(0, 0, 0, 1)">=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=root
# 使用阿里巴巴druid数据源，默认使用自带
# spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
#开启控制台打印sql
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
# mybatis 下划线转驼峰配置，两者都可以
# mybatis.configuration.mapUnderscoreToCamelCase=true
mybatis.configuration.map-underscore-to-camel-case=true
# 配置扫描
mybatis.mapper-locations=classpath:mapper/*.xml
#配置xml的结果别名
mybatis.type-aliases-package=net.ybclass.online_ybclass.domain</span></pre>
