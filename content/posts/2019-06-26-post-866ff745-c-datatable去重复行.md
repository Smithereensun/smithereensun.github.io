---
title: "C# Datatable去重复行"
date: 2019-06-26
description: "原数据 去重 去重成功！~"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11086576.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> DataView dv = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> DataView(dt);
</span><span style="color: rgba(0, 128, 128, 1)">2</span> dt = dv.ToTable(<span style="color: rgba(0, 0, 255, 1)">true</span>,<span style="color: rgba(0, 0, 255, 1)">new</span> <span style="color: rgba(0, 0, 255, 1)">string</span>[] { <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">NEST_NAME</span><span style="color: rgba(128, 0, 0, 1)">"</span>,<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">RAW_QUA</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">RAW_DENSITY</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">RAW_THICK</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">RAW_WIDTH</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">RAW_LENGTH</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">CUTT_LEN</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">MARK_LEN</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">IDLE_LEN</span><span style="color: rgba(128, 0, 0, 1)">"</span> });  <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第二个参数：去重字段</span></pre>
