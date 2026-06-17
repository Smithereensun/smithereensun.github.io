---
title: "Mac 重启docker服务"
date: 2021-01-29
description: "通过 launchctl 查看 docker server, 记住docker server 名 launchctl list | grep docker 111117 0 com.docker.docker.2388 然后关闭和启动它 launchctl stop com.docker.docke"
tags:
  - "Docker"
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14343261.html"
---

<p>通过 launchctl 查看 docker server, 记住docker server 名</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">launchctl list | grep docker

111117   0       com.docker.docker.2388</span></pre>
