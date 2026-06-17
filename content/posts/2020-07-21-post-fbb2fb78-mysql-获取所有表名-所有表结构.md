---
title: "MySQL 获取所有表名、所有表结构"
date: 2020-07-21
description: "获取所有表名 SELECT A.TABLE_SCHEMA &#39;数据库&#39;, A.TABLE_NAME &#39;表名&#39;, A.TABLE_ROWS &#39;表记录行数&#39;, A.CREATE_TIME &#39;创表时间&#39;, A.TABLE_COMMENT &#3"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13353770.html"
---

<h1>获取所有表名</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">SELECT</span><span style="color: rgba(0, 0, 0, 1)">
    A.TABLE_SCHEMA </span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">数据库</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,
    A.TABLE_NAME </span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">表名</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,
    A.TABLE_ROWS </span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">表记录行数</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,
    A.CREATE_TIME </span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">创表时间</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,
    A.TABLE_COMMENT </span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">表备注</span><span style="color: rgba(255, 0, 0, 1)">'</span>
<span style="color: rgba(0, 0, 255, 1)">FROM</span><span style="color: rgba(0, 0, 0, 1)"> INFORMATION_SCHEMA.TABLES A
</span><span style="color: rgba(0, 0, 255, 1)">WHERE</span><span style="color: rgba(0, 0, 0, 1)">
    A.TABLE_SCHEMA </span><span style="color: rgba(128, 128, 128, 1)">=</span> <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">数据库</span><span style="color: rgba(255, 0, 0, 1)">'</span></pre>
