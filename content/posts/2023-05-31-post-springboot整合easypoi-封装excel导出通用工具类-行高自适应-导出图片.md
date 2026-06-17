---
title: "SpringBoot整合EasyPoi 封装Excel导出通用工具类，行高自适应，导出图片"
date: 2023-05-31
description: "导读 下午抽空封装一个通用导出Excel工具类。之前还写过一篇EasyPoi导入参数校验，批注导出，点我直达 添加依赖 &lt;!-- easy poi --&gt; &lt;dependency&gt; &lt;groupId&gt;cn.afterturn&lt;/groupId&gt; &lt"
tags:
  - "Spring Boot"
  - "Easy Poi"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/easypoiexcel.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　下午抽空封装一个通用导出Excel工具类。之前还写过一篇EasyPoi导入参数校验，批注导出，<a href="https://www.cnblogs.com/chenyanbin/p/easypoi.html" target="_blank">点我直达</a></p>
<h1 style="text-align: center">添加依赖</h1>
<div class="cnblogs_code">
<pre> <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> easy poi </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>cn.afterturn<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>easypoi-spring-boot-starter<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>4.1.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
