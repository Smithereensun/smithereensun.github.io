---
title: "Mysql的merge into 插入数据，有就更新，无则新增"
date: 2022-02-16
description: "INSERT ... ON DUPLICATE KEY UPDATE语句。 如果有唯一索引或主键 且数据重复 就执行后面的update INSERT INTO table (a,b,c) VALUES (1,2,3) ON DUPLICATE KEY UPDATE c=c+1; 上面语句 如果a是唯"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15898974.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">INSERT</span> ... <span style="color: rgba(0, 0, 255, 1)">ON</span> DUPLICATE <span style="color: rgba(0, 0, 255, 1)">KEY</span><span style="color: rgba(0, 0, 0, 1)"> UPDATE语句。
如果有唯一索引或主键  且数据重复  就执行后面的update

</span><span style="color: rgba(0, 0, 255, 1)">INSERT</span> <span style="color: rgba(0, 0, 255, 1)">INTO</span> <span style="color: rgba(0, 0, 255, 1)">table</span> (a,b,c) <span style="color: rgba(0, 0, 255, 1)">VALUES</span> (<span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span>,<span style="color: rgba(128, 0, 0, 1); font-weight: bold">2</span>,<span style="color: rgba(128, 0, 0, 1); font-weight: bold">3</span>)  <span style="color: rgba(0, 0, 255, 1)">ON</span> DUPLICATE <span style="color: rgba(0, 0, 255, 1)">KEY</span> <span style="color: rgba(0, 0, 255, 1)">UPDATE</span> c<span style="color: rgba(128, 128, 128, 1)">=</span>c<span style="color: rgba(128, 128, 128, 1)">+</span><span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span><span style="color: rgba(0, 0, 0, 1)">;  
  
上面语句  如果a是唯一索引且表里已经有a</span><span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(0, 0, 0, 1)">1的记录  则上面语句等同于下面：

</span><span style="color: rgba(0, 0, 255, 1)">UPDATE</span> <span style="color: rgba(0, 0, 255, 1)">table</span> <span style="color: rgba(0, 0, 255, 1)">SET</span> c<span style="color: rgba(128, 128, 128, 1)">=</span>c<span style="color: rgba(128, 128, 128, 1)">+</span><span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span> <span style="color: rgba(0, 0, 255, 1)">WHERE</span> a<span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span>;</pre>
