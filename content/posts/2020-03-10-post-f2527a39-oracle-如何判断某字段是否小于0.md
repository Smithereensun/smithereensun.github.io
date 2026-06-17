---
title: "ORACLE 如何判断某字段是否小于0"
date: 2020-03-10
description: "Oracle 自带的函数 SIGN 表达式的正 (+1)、零 (0) 或负 (-1) 号 SQL&gt; SELECT SIGN(-47.3), SIGN(0), SIGN(47.3) FROM dual; SIGN(-47.3) SIGN(0) SIGN(47.3) -1 0 1"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12456589.html"
---

<pre class="reply-text mb10">Oracle 自带的函数  SIGN 
表达式的正 (+1)、零 (0) 或负 (-1) 号 


SQL&gt; SELECT SIGN(-47.3), SIGN(0), SIGN(47.3) FROM dual;

SIGN(-47.3)    SIGN(0) SIGN(47.3)
----------- ---------- ----------
         -1          0          1</pre>
