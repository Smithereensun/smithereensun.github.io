---
title: "mysql调整最大连接数"
date: 2022-01-18
description: "mysql设置连接数调整 #连接数配置 show variables like &#39;%max_connections%&#39;; set GLOBAL max_connections=5000; set GLOBAL mysqlx_max_connections=5000;"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15818458.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">mysql设置连接数调整
#连接数配置
show variables like '%max_connections%';
set GLOBAL max_connections=5000;
set GLOBAL mysqlx_max_connections=5000;</span></pre>
