---
title: "Mac SpringBoot项目 Gradle 7.3 转 Maven 手把手教学，包学会~"
date: 2023-09-10
description: "导读 最近我手上有个使用Gradle构建的项目，国内使用Gradle的人相对较少。而且我也觉得Gradle的依赖管理方式有些复杂，让我感到有些困惑。因此，我想将项目转换为Maven构建方式。Maven构建的SpringBoot的方式，想必大家都不陌生了吧~我特地记录下来，以备将来可能还会用到。 这里"
tags:
  - "Gradle"
  - "Spring Boot"
  - "Spring Cloud"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/gradle.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　最近我手上有个使用Gradle构建的项目，国内使用Gradle的人相对较少。而且我也觉得Gradle的依赖管理方式有些复杂，让我感到有些困惑。因此，我想将项目转换为Maven构建方式。Maven构建的SpringBoot的方式，想必大家都不陌生了吧~我特地记录下来，以备将来可能还会用到。</p>
<p>　　这里为了演示方便，我快速创建一个SpringBoot用Gradle构建的项目，将他改成Maven方式构建项目~~~~~</p>
<h1 style="text-align: center">本地安装Gradle</h1>
<h2>下载地址</h2>
<p><a href="https://gradle.org/releases/" target="_blank" rel="noopener nofollow">https://gradle.org/releases/</a></p>
<div class="cnblogs_code">
<pre>https://downloads.gradle.org/distributions/gradle-7.3-all.zip</pre>
