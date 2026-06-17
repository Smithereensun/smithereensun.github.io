---
title: "Oracle中exists替代in语句"
date: 2023-05-31
description: "简介 大家都知道exists的速度要比in的速度快，也知道exists函数返回一个布尔值，也就是说exists函数里最后要是 a.id =b.id类似这种方式结束。 example: 常规方式 SELECT * FROM TBL_REBATE_DAY_COUNT WHERE ID IN (1, 2,"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11961340.html"
---

<h1 style="text-align: center">简介</h1>
<p>　　大家都知道exists的速度要比in的速度快，也知道exists函数返回一个布尔值，也就是说exists函数里最后要是 a.id =b.id类似这种方式结束。</p>
<h2>example:</h2>
<h3>常规方式</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">SELECT</span> <span style="color: rgba(128, 128, 128, 1)">*</span> <span style="color: rgba(0, 0, 255, 1)">FROM</span> TBL_REBATE_DAY_COUNT <span style="color: rgba(0, 0, 255, 1)">WHERE</span> ID <span style="color: rgba(128, 128, 128, 1)">IN</span> (<span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span>, <span style="color: rgba(128, 0, 0, 1); font-weight: bold">2</span>, <span style="color: rgba(128, 0, 0, 1); font-weight: bold">3</span>, <span style="color: rgba(128, 0, 0, 1); font-weight: bold">4</span>, <span style="color: rgba(128, 0, 0, 1); font-weight: bold">5</span>);</pre>
