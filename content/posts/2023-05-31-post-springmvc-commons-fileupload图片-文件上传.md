---
title: "SpringMvc commons-fileupload图片/文件上传"
date: 2023-05-31
description: "简介 SpringMvc文件上传的实现，是由commons-fileupload这个jar包实现的。 需求 在修改商品页面，添加上传商品图片功能。 Maven依赖包 pom.xml &lt;!-- 文件上传 --&gt; &lt;dependency&gt; &lt;groupId&gt;commo"
tags:
  - "MVC"
  - "JAVA"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12023244.html"
---

<h1 style="text-align: center">简介</h1>
<p>　　SpringMvc文件上传的实现，是由commons-fileupload这个jar包实现的。</p>
<h1 style="text-align: center">需求</h1>
<p>在修改商品页面，添加上传商品图片功能。</p>
<h1 style="text-align: center">Maven依赖包</h1>
<h2>pom.xml</h2>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 文件上传 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>commons-fileupload<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>commons-fileupload<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.4<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
