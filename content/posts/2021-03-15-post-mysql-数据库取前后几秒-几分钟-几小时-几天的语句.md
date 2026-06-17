---
title: "mysql 数据库取前后几秒 几分钟 几小时 几天的语句"
date: 2021-03-15
description: "取当前时间： 1 select current_timestamp; 输出：2016-06-16 16:12:52 1 select now(); 输出：2016-06-16 16:12:52 取当前时间的前一分钟： 1 select SUBDATE(now(),interval 60 second"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14536594.html"
---

<p>取当前时间：</p>
<div class="jb51code">
<div>
<div id="highlighter_277281" class="syntaxhighlighter  sql">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="gutter">
<div class="line number1 index0 alt2">1
