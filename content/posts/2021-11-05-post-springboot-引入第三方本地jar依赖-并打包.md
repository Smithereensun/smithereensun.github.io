---
title: "SpringBoot 引入第三方本地jar依赖 并打包"
date: 2021-11-05
description: "引入本地jar 在项目路径下新建文件夹lib，并将jar放入 pom文件引入 &lt;dependency&gt; &lt;groupId&gt;com.aliyun.alicom&lt;/groupId&gt; &lt;artifactId&gt;alicom-mns-receive-sdk&lt"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14606668.html"
---

<h1 style="text-align: center">引入本地jar</h1>
<p>　　在项目路径下新建文件夹lib，并将jar放入</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202104/1504448-20210401154330529-716401778.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1 style="text-align: center">pom文件引入</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.aliyun.alicom<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>alicom-mns-receive-sdk<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>0.0.1-SNAPSHOT<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>jar<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">scope</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>system<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">scope</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">systemPath</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>${project.basedir}/lib/alicom-mns-receive-sdk-1.0.1.jar<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">systemPath</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.aliyun.mns<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>aliyun-sdk-mns<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.1.8<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>jar<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">scope</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>system<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">scope</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">systemPath</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>${project.basedir}/lib/aliyun-sdk-mns-1.1.8.jar<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">systemPath</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
