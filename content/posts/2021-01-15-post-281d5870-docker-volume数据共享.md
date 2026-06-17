---
title: "Docker Volume数据共享"
date: 2021-01-15
description: "创建dockerfile FROM centos:7 VOLUME [&quot;/usr/local&quot;] 注意：在dockerfile里设置volume是无法修改宿主机的挂载路径的 构建 docker build -t centos:v1 . 演示"
tags:
  - "Docker"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14284660.html"
---

<h1 style="text-align: center">创建dockerfile</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">FROM centos:7
VOLUME ["/usr/local"]</span></pre>
