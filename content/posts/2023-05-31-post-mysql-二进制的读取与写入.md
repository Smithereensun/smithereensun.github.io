---
title: "mysql 二进制的读取与写入"
date: 2023-05-31
description: "插入语句 用binary转换函数可将字符串转为二进制 insert into mytable (id, bin) values(1, binary(&#39;abcdef&#39;)) 查询语句 用cast进行类型转换 select id, cast(bin as char) as bintext"
tags:
  - "SQL"
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12861132.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">插入语句 用binary转换函数可将字符串转为二进制

insert into mytable (id, bin) values(1, binary('abcdef'))



查询语句 用cast进行类型转换

select id, cast(bin as char) as bintext from mytable</span></pre>
