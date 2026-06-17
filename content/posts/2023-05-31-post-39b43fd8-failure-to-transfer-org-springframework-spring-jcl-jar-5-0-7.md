---
title: "Failure to transfer org.springframework:spring-jcl:jar:5.0.7.RELEASE from"
date: 2023-05-31
description: "错误信息： Failure to transfer org.springframework.boot:spring-boot-maven-plugin:pom:1.5.4.RELEASE from https://repo.maven.apache.org/maven2 was cached in"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11706243.html"
---

<p>错误信息：</p>
<p>Failure to transfer org.springframework.boot:spring-boot-maven-plugin:pom:1.5.4.RELEASE from https://repo.maven.apache.org/maven2 was cached in the local repository, resolution will not be reattempted until the update interval of central has elapsed or updates are forced. Original error: Could not transfer artifact&nbsp;<br>org.springframework.boot:spring-boot-maven-plugin:pom:1.5.4.RELEASE from/to central (https://repo.maven.apache.org/maven2): repo.maven.apache.org&nbsp;pom.xml</p>
<p>　　原本代码并没出错，但是在导入项目到新环境下后，出现了这种错误。发生的问题根本原因 在于 网络环境导致 依赖的包在下载的过程中出现的异常中断，导致引用资源损坏</p>
<p>解决办法：</p>
<p>cmd中：</p>
<div class="cnblogs_code">
<pre>cd %userprofile%<span style="color: rgba(0, 0, 0, 1)">\.m2\repository
</span><span style="color: rgba(0, 0, 255, 1)">for</span> /r %i <span style="color: rgba(0, 0, 255, 1)">in</span> (*.lastUpdated) <span style="color: rgba(0, 0, 255, 1)">do</span> del %i</pre>
