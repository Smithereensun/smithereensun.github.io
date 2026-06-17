---
title: "Oracle 日期减年数、两日期相减"
date: 2020-06-05
description: "-- 日期减年数 SELECT add_months(DEF_DATE,12*USEFUL_LIFE) FROM S_USER --两日期相减 SELECT round(sysdate-PEI.STARTED_USE_DATE) FROM S_USER"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13047624.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)"> 日期减年数</span>
<span style="color: rgba(0, 0, 255, 1)">SELECT</span> add_months(DEF_DATE,<span style="color: rgba(128, 0, 0, 1); font-weight: bold">12</span><span style="color: rgba(128, 128, 128, 1)">*</span>USEFUL_LIFE) <span style="color: rgba(0, 0, 255, 1)">FROM</span><span style="color: rgba(0, 0, 0, 1)"> S_USER

</span><span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">两日期相减</span>
<span style="color: rgba(0, 0, 255, 1)">SELECT</span> <span style="color: rgba(255, 0, 255, 1)">round</span>(sysdate<span style="color: rgba(128, 128, 128, 1)">-</span>PEI.STARTED_USE_DATE) <span style="color: rgba(0, 0, 255, 1)">FROM</span> S_USER</pre>
