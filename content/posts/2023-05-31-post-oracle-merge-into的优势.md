---
title: "Oracle merge into的优势"
date: 2023-05-31
description: "简介 Oracle merge into命令，顾名思义就是“有则更新，无则插入”，这个也是merge into 命令的核心思想，在实际开发过程中，我们会经常遇到这种通过两表互相关联匹配更新其中一个表的某些字段的业务，有时还要处理不匹配的情况下的业务。这个时候你会发现随着表的数据量增加，类似这种业务场"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11718089.html"
---

<h1>简介</h1>
<p>　　Oracle merge into命令，顾名思义就是“有则更新，无则插入”，这个也是merge into 命令的核心思想，在实际开发过程中，我们会经常遇到这种通过两表互相关联匹配更新其中一个表的某些字段的业务，有时还要处理不匹配的情况下的业务。这个时候你会发现随着表的数据量增加，类似这种业务场景的执行效率会比较慢，那是因为你需要多次重复查询两表中的数据，而通过merge into命令，只需要一次关联即可完成“有则更新，无则插入”的业务场景，大大提高语句的执行效率。</p>
<h1>语法</h1>
<div class="cnblogs_code">
<pre> merge into A表 <span style="color: rgba(0, 0, 255, 1)">using</span> B表 on (A表.id =<span style="color: rgba(0, 0, 0, 1)"> B表.id)
</span> when matched then --<span style="color: rgba(0, 0, 0, 1)">匹配到，则更新A表数据
</span> update <span style="color: rgba(0, 0, 255, 1)">set</span> A.col=<span style="color: rgba(0, 0, 0, 1)">B.col
</span> when not matched then --<span style="color: rgba(0, 0, 0, 1)">没匹配到，往A表插入数据
</span>  insert (a,b,c) values (<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">a</span><span style="color: rgba(128, 0, 0, 1)">'</span>,<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">b</span><span style="color: rgba(128, 0, 0, 1)">'</span>,<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">c</span><span style="color: rgba(128, 0, 0, 1)">'</span>);</pre>
