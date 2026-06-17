---
title: "PLSQL 编码设置"
date: 2020-04-22
description: "1、先查询plsql编码格式 select userenv(&#39;language&#39;)from dual 2、新建用户变量，变量名=NLS_LANG，变量值，刚才sql查询的结果 保存后，重启plsql即可"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12330068.html"
---

<p>1、先查询plsql编码格式</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">select</span> userenv(<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">language</span><span style="color: rgba(255, 0, 0, 1)">'</span>)<span style="color: rgba(0, 0, 255, 1)">from</span> dual</pre>
