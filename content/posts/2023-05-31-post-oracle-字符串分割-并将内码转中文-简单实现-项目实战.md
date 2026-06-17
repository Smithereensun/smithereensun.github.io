---
title: "Oracle 字符串分割，并将内码转中文(简单实现)，项目实战"
date: 2023-05-31
description: "导读 实际项目开发过程中，可能会遇到这种情况，A表中A1字段存储B表中的内码如(1，2，3)，此时需要将A表中的A1字段转中文，为了方便理解，我们这里创建学生表和老师表，一个学生对应N个老师。 创建表 学生表 --学生表 CREATE TABLE S_STUDENT ( S_ID NUMBER, S"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12988702.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　实际项目开发过程中，可能会遇到这种情况，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>A表中A1字段存储B表中的内码如(1，2，3)</strong></span>，此时需要<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>将A表中的A1字段转中文</strong></span>，为了方便理解，我们这里创建学生表和老师表，一个学生对应N个老师。</p>
<h2>创建表</h2>
<h3>学生表</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">学生表</span>
<span style="color: rgba(0, 0, 255, 1)">CREATE</span> <span style="color: rgba(0, 0, 255, 1)">TABLE</span><span style="color: rgba(0, 0, 0, 1)"> S_STUDENT
(
S_ID </span><span style="color: rgba(0, 0, 255, 1)">NUMBER</span><span style="color: rgba(0, 0, 0, 1)">,
S_NAME </span><span style="color: rgba(0, 0, 255, 1)">VARCHAR2</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">50</span><span style="color: rgba(0, 0, 0, 1)">),
T_ID </span><span style="color: rgba(0, 0, 255, 1)">VARCHAR2</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">50</span><span style="color: rgba(0, 0, 0, 1)">)
)
</span><span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">插入一条数据</span>
<span style="color: rgba(0, 0, 255, 1)">INSERT</span> <span style="color: rgba(0, 0, 255, 1)">INTO</span> S_STUDENT <span style="color: rgba(0, 0, 255, 1)">VALUES</span> (<span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span>,<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">陈彦斌</span><span style="color: rgba(255, 0, 0, 1)">'</span>,<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">1,2,3</span><span style="color: rgba(255, 0, 0, 1)">'</span>)</pre>
