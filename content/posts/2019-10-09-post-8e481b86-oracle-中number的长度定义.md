---
title: "Oracle 中Number的长度定义"
date: 2019-10-09
description: "Number可以通过如下格式来指定：Field_NAME Number（precision ，scale），其中precision指Number可以存储的最大数字长度（不包括左右两边的0），scale指在小数点右边的最大数字长度（包括左侧0）。也就是说，"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11639433.html"
---

<p>Number可以通过如下格式来指定：Field_NAME Number（precision ，scale），其中precision指Number可以存储的最大数字长度（不包括左右两边的0），scale指在小数点右边的最大数字长度（包括左侧0）。也就是说，</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> p是总长度，s是小数，整数部分长度是p-<span style="color: rgba(0, 0, 0, 1)">s
</span><span style="color: rgba(0, 128, 128, 1)">2</span> 
<span style="color: rgba(0, 128, 128, 1)">3</span> <span style="color: rgba(0, 0, 0, 1)">例如：
</span><span style="color: rgba(0, 128, 128, 1)">4</span> Number(<span style="color: rgba(128, 0, 128, 1)">8</span>,<span style="color: rgba(128, 0, 128, 1)">2</span>)表示有效数字长度是8，能存储的最大数值是999999.<span style="color: rgba(128, 0, 128, 1)">99</span>
<span style="color: rgba(0, 128, 128, 1)">5</span> 
<span style="color: rgba(0, 128, 128, 1)">6</span> Number(<span style="color: rgba(128, 0, 128, 1)">8</span>)表示有效数字长度也是8，能存储的最大数值是99999999</pre>
