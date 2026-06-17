---
title: "SpringCloud注册中心切换nacos"
date: 2023-10-29
description: "SpringBoot与nacos版本对应关系 https://github.com/alibaba/spring-cloud-alibaba/wiki/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E 导读 因为种种原因，现在很多公司微服务的注册中心不在使用eureka，纷纷"
tags:
  - "Spring Cloud"
  - "Spring Boot"
  - "Nacos"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14193595.html"
---

<h1 style="text-align: center">&nbsp;SpringBoot与nacos版本对应关系</h1>
<p><a href="https://github.com/alibaba/spring-cloud-alibaba/wiki/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E" target="_blank" rel="noopener nofollow">https://github.com/alibaba/spring-cloud-alibaba/wiki/%E7%89%88%E6%9C%AC%E8%AF%B4%E6%98%8E</a></p>
<h1 style="text-align: center">导读</h1>
<p>　　因为种种原因，现在很多公司微服务的注册中心不在使用eureka，纷纷转向阿里的nacos，公司早就在使用nacos，但是是别人搭建的，出于好奇，今天自己手动创建项目，完整搭建一遍...自己动手丰衣足食</p>
<h1 style="text-align: center">搭建nacos</h1>
<p><a href="https://www.cnblogs.com/chenyanbin/p/14017230.html" target="_blank">点我直达</a></p>
<h1 style="text-align: center">创建项目</h1>
<h2>api-product</h2>
<h3>项目结构</h3>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202012/1504448-20201226172530454-1205058284.png" alt="" loading="lazy" /></p>
<h3>pom.xml</h3>
<div class="cnblogs_code"><img src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" id="code_img_closed_2063c8e6-4071-487b-91c2-188044588a9f" class="code_img_closed" /><img src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" id="code_img_opened_2063c8e6-4071-487b-91c2-188044588a9f" class="code_img_opened" style="display: none" />
<div id="cnblogs_code_open_2063c8e6-4071-487b-91c2-188044588a9f" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;?</span><span style="color: rgba(255, 0, 255, 1)">xml version="1.0" encoding="UTF-8"</span><span style="color: rgba(0, 0, 255, 1)">?&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">project </span><span style="color: rgba(255, 0, 0, 1)">xmlns</span><span style="color: rgba(0, 0, 255, 1)">="http://maven.apache.org/POM/4.0.0"</span><span style="color: rgba(255, 0, 0, 1)">
         xmlns:xsi</span><span style="color: rgba(0, 0, 255, 1)">="http://www.w3.org/2001/XMLSchema-instance"</span><span style="color: rgba(255, 0, 0, 1)">
         xsi:schemaLocation</span><span style="color: rgba(0, 0, 255, 1)">="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">modelVersion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>4.0.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">modelVersion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>

    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.ybchen<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>api-product<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.0-SNAPSHOT<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependencies</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.springframework.cloud<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>spring-cloud-starter-openfeign<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>2.2.0.RELEASE<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>

    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependencies</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>

<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">project</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
