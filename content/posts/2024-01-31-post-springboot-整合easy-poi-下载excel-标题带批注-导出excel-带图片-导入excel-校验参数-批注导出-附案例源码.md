---
title: "SpringBoot 整合Easy Poi 下载Excel(标题带批注)、导出Excel(带图片)、导入Excel(校验参数，批注导出)，附案例源码"
date: 2024-01-31
description: "导读 日常开发过程中，经常遇到Excel导入、导出等功能，其中导入逻辑相对麻烦些，还涉及到参数的校验，然后将错误信息批注导出。之前写过EasyExcel导入(参数校验，带批注)(点我直达1、点我直达2)、导出等功能。今天遇到一个需求是，导入、导出还需要带上图片，EasyExcel目前还不支持Exce"
tags:
  - "Spring Boot"
  - "Easy Poi"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/easypoi.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　日常开发过程中，经常遇到Excel导入、导出等功能，其中导入逻辑相对麻烦些，还涉及到参数的校验，然后将错误信息批注导出。之前写过EasyExcel导入(参数校验，带批注)(<strong><span style="color: rgba(255, 0, 0, 1)"><a href="https://www.cnblogs.com/chenyanbin/p/13957503.html" target="_blank"><span style="color: rgba(255, 0, 0, 1)">点我直达1</span></a></span></strong>、<strong><span style="color: rgba(255, 0, 0, 1)"><a href="https://www.cnblogs.com/chenyanbin/p/14366596.html" target="_blank"><span style="color: rgba(255, 0, 0, 1)">点我直达2</span></a></span></strong>)、导出等功能。今天遇到一个需求是，导入、导出还需要带上图片，EasyExcel目前还不支持Excel中带图片的。Easy Poi支持带图片导入、导出，批注等功能，好啦~废话不多说，下面开始叭~<span style="color: rgba(255, 0, 255, 1)"><strong>EasyPoi官网</strong></span>，<a href="http://easypoi.mydoc.io/#" target="_blank" rel="noopener nofollow">点我直达</a>&nbsp;<a href="http://doc.wupaas.com/docs/easypoi/easypoi-1c2cp5rf3hnqv" target="_blank" rel="noopener nofollow">点我直达(新地址)</a></p>
<h1 style="text-align: center">项目源码</h1>
<h2>添加依赖</h2>
<div class="cnblogs_code">
<pre>            <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> easy poi </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>cn.afterturn<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>easypoi-spring-boot-starter<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>4.1.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> JSR 303 规范验证包 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.hibernate<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>hibernate-validator<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>5.2.4.Final<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
