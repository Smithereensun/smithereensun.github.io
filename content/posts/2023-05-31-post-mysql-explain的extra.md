---
title: "mysql explain的extra"
date: 2023-05-31
description: "导读 extra主要有是那种情况：Using index、Using filesort、Using temporary、Using where Using where无需多说，就是使用了where筛选条件。 数据准备： CREATE TABLE `t_blog` ( `id` int(11) NOT"
tags:
  - "SQL优化"
  - "SQL"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13110056.html"
---

<h1 style="text-align: center">导读</h1>
<p>extra主要有是那种情况：Using index、Using filesort、Using temporary、Using where</p>
<p>Using where无需多说，就是使用了where筛选条件。</p>
<p>数据准备：</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">CREATE</span> <span style="color: rgba(0, 0, 255, 1)">TABLE</span><span style="color: rgba(0, 0, 0, 1)"> `t_blog` (
  `id` </span><span style="color: rgba(0, 0, 255, 1)">int</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">11</span>) <span style="color: rgba(128, 128, 128, 1)">NOT</span> <span style="color: rgba(0, 0, 255, 1)">NULL</span><span style="color: rgba(0, 0, 0, 1)"> auto_increment,
  `title` </span><span style="color: rgba(0, 0, 255, 1)">varchar</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">50</span>) <span style="color: rgba(0, 0, 255, 1)">default</span> <span style="color: rgba(0, 0, 255, 1)">NULL</span><span style="color: rgba(0, 0, 0, 1)">,
  `typeId` </span><span style="color: rgba(0, 0, 255, 1)">int</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">11</span>) <span style="color: rgba(0, 0, 255, 1)">default</span> <span style="color: rgba(0, 0, 255, 1)">NULL</span><span style="color: rgba(0, 0, 0, 1)">,
  `a` </span><span style="color: rgba(0, 0, 255, 1)">int</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">11</span>) <span style="color: rgba(0, 0, 255, 1)">default</span> <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">0</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,
  </span><span style="color: rgba(0, 0, 255, 1)">PRIMARY</span> <span style="color: rgba(0, 0, 255, 1)">KEY</span><span style="color: rgba(0, 0, 0, 1)">  (`id`),
  </span><span style="color: rgba(0, 0, 255, 1)">KEY</span><span style="color: rgba(0, 0, 0, 1)"> `index_1` (`title`,`typeId`)
) ENGINE</span><span style="color: rgba(128, 128, 128, 1)">=</span>InnoDB <span style="color: rgba(0, 0, 255, 1)">DEFAULT</span> CHARSET<span style="color: rgba(128, 128, 128, 1)">=</span>utf8</pre>
