---
title: "Maven pom.xml文件"
date: 2020-01-15
description: "pom.xml 版本依赖 &lt;!--编译器依赖--&gt; &lt;properties&gt; &lt;project.build.sourceEncoding&gt;UTF-8&lt;/project.build.sourceEncoding&gt; &lt;maven.compiler.s"
tags:
  - "配置文件"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12196744.html"
---

<h1 style="text-align: center">pom.xml</h1>
<h2>版本依赖</h2>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">编译器依赖</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">properties</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">project.build.sourceEncoding</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>UTF-8<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">project.build.sourceEncoding</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">maven.compiler.source</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>13<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">maven.compiler.source</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">maven.compiler.target</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>13<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">maven.compiler.target</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">properties</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
