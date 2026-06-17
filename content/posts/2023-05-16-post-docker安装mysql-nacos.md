---
title: "Docker安装mysql、nacos"
date: 2023-05-16
description: "docker run --name ybchen_mysql --restart=always -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0 docker run --env MODE=standalone --name ybchen-n"
tags:
  - "Docker"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/16397162.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">docker run --name ybchen_mysql --restart=always -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:8.0

docker run --env MODE=standalone --name ybchen-nacos1 --restart=always -d -p 8848:8848 nacos/nacos-server:2.0.3</span></pre>
