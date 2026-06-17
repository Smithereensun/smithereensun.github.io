---
title: "Oracle 递归拼接字段"
date: 2020-06-04
description: "效果 sql SELECT LISTAGG(T.NAME, &#39; / &#39;) WITHIN GROUP(ORDER BY LEVEL DESC) AS RESULT FROM S_WORK_RESOURSE T START WITH T.WORK_RESOURCE_NO = 323 CO"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13045502.html"
---

<h2>效果</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200604190517971-1950310615.png" alt="" /></p>
<p>&nbsp;</p>
<h2>sql</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">SELECT</span> LISTAGG(T.NAME, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)"> / </span><span style="color: rgba(255, 0, 0, 1)">'</span>) WITHIN <span style="color: rgba(0, 0, 255, 1)">GROUP</span>(<span style="color: rgba(0, 0, 255, 1)">ORDER</span> <span style="color: rgba(0, 0, 255, 1)">BY</span> <span style="color: rgba(0, 0, 255, 1)">LEVEL</span> <span style="color: rgba(0, 0, 255, 1)">DESC</span>) <span style="color: rgba(0, 0, 255, 1)">AS</span><span style="color: rgba(0, 0, 0, 1)"> RESULT
  </span><span style="color: rgba(0, 0, 255, 1)">FROM</span><span style="color: rgba(0, 0, 0, 1)"> S_WORK_RESOURSE T
 START </span><span style="color: rgba(0, 0, 255, 1)">WITH</span> T.WORK_RESOURCE_NO <span style="color: rgba(128, 128, 128, 1)">=</span> <span style="color: rgba(128, 0, 0, 1); font-weight: bold">323</span><span style="color: rgba(0, 0, 0, 1)">
CONNECT </span><span style="color: rgba(0, 0, 255, 1)">BY</span> PRIOR T.PARENT_WORK_RESOURCE_NO <span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(0, 0, 0, 1)"> T.WORK_RESOURCE_NO
       </span><span style="color: rgba(128, 128, 128, 1)">and</span> T.PARENT_WORK_RESOURCE_NO <span style="color: rgba(0, 0, 255, 1)">is</span> <span style="color: rgba(128, 128, 128, 1)">not</span> <span style="color: rgba(0, 0, 255, 1)">null</span></pre>
