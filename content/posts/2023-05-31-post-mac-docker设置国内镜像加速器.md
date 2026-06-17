---
title: "Mac Docker设置国内镜像加速器"
date: 2023-05-31
description: "安装docker 点我直达 设置国内加速镜像 { &quot;experimental&quot;: false, &quot;features&quot;: { &quot;buildkit&quot;: true }, &quot;registry-mirrors&quot;: [ &quot;"
tags:
  - "Docker"
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14254575.html"
---

<h1 style="text-align: center">安装docker</h1>
<p><a href="https://www.runoob.com/docker/macos-docker-install.html" target="_blank" rel="noopener nofollow">点我直达</a></p>
<h2>设置国内加速镜像</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202101/1504448-20210109121737505-327729242.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">{
    "experimental": false,
    "features": {
        "buildkit": true
    },
    "registry-mirrors": [
        "https://registry.docker-cn.com"
    ]
}</span></pre>
