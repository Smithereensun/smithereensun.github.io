---
title: "MySQL 性能优化细节"
date: 2023-05-31
description: "服务器层面优化（了解） 将数据保存在内存中，保证从内存读取数据 设置足够大的innodb_buffer_pool_size，将数据读取到内存中。 建议innodb_buffer_pool_size设置为总内存大小的3/4或者4/5。 怎样确定innodb_buffer_pool_size足够大，数据"
tags:
  - "SQL优化"
  - "SQL"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13138251.html"
---

<h1 style="text-align: center">服务器层面优化（<span style="color: rgba(255, 0, 0, 1)">了解</span>）</h1>
<h2>将数据保存在内存中，保证从内存读取数据</h2>
<ul>
<li>设置足够大的innodb_buffer_pool_size，将数据读取到内存中。
<ul>
<li>建议innodb_buffer_pool_size设置为总内存大小的3/4或者4/5。</li>
</ul>
</li>
<li>怎样确定innodb_buffer_pool_size足够大，数据是从内存读取而不是硬盘？</li>
</ul>
<div class="cnblogs_code">
<pre>show global status <span style="color: rgba(128, 128, 128, 1)">like</span> <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">innodb_buffer_pool_pages_%</span><span style="color: rgba(255, 0, 0, 1)">'</span>;</pre>
