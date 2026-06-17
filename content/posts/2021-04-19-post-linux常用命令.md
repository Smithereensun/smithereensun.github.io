---
title: "Linux常用命令"
date: 2021-04-19
description: "查看内存使用情况 ps -eo pid,ppid,%mem,%cpu,cmd --sort=-%mem | head 查看启动java项目 jps 查看内存 free"
tags:
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14678518.html"
---

<h1>查看内存使用情况</h1>
<div class="cnblogs_code">
<pre> ps -eo pid,ppid,%mem,%cpu,cmd --sort=-%mem | head</pre>
