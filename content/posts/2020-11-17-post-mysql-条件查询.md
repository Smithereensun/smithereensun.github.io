---
title: "Mysql 条件查询"
date: 2020-11-17
description: "group 作用 把行按字段分组 语法 group by 列1,列2 select deptnu,job,count(deptnu) from employee group by deptnu,job 适用场景 常用于统计场合，一般和聚合函数连用 having 作用 对查询的结果进行筛选操作 语法"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13991607.html"
---

<h1 style="text-align: center">group</h1>
<h2>作用</h2>
<p>　　把行按字段分组</p>
<h2>语法</h2>
<p>　　group by 列1,列2</p>
<div class="cnblogs_code">
<pre>select deptnu,job,count(deptnu) from employee group by deptnu,job</pre>
