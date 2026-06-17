---
title: "设置Docker容器里的时间"
date: 2023-05-31
description: "启动容器时，添加环境变量 docer run -e TZ=Asia/Shanghai --rm myalpine date -e TZ=Asia/Shanghai"
tags:
  - "Docker"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15403053.html"
---

<p>启动容器时，添加环境变量</p>
<div class="cnblogs_code">
<pre>docer run -e TZ=Asia/Shanghai --rm myalpine date</pre>
