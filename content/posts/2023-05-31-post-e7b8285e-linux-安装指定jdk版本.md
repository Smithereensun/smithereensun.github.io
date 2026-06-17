---
title: "Linux 安装指定jdk版本"
date: 2023-05-31
description: "操作步骤 卸载系统自带jdk版本 1、查看安装的jdk rpm -qa | grep java 2、卸载系统自带jdk rpm -e --nodeps 包名 下载jdk 当前最新版本下载地址：http://www.oracle.com/technetwork/java/javase/download"
tags:
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12843149.html"
---

<h1 style="text-align: center">操作步骤</h1>
<h2>卸载系统自带jdk版本</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">1、查看安装的jdk
rpm -qa | grep java

2、卸载系统自带jdk
rpm -e --nodeps 包名</span></pre>
