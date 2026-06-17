---
title: "ORA-06502:at \"WMSYS.WM_CONCAT_IMPL\",line 30 解决方法整理"
date: 2019-07-09
description: "之前数据量少的时候，用:select&#160;wm_concat(字段) from 表 拼接数据量小的话，没有问题，数据量超出4000个就会爆以下错误信息： 解决方法(Oracle 函数xmlagg拼接): 效果图： 1 select xmlagg(xmlparse(content SECTION"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11156228.html"
---

<p><strong>　　之前数据量少的时候，用:select&nbsp;wm_concat(字段) from 表 拼接数据量小的话，没有问题，数据量超出4000个就会爆以下错误信息：</strong></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190709111741535-1693527405.png" alt="" /></p>
<h2>解决方法(Oracle 函数xmlagg拼接):</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> 语法格式：<span style="color: rgba(0, 0, 255, 1)">SELECT</span> xmlagg(xmlparse(content 合并字段<span style="color: rgba(128, 128, 128, 1)">||</span>’,’ wellformed) <span style="color: rgba(0, 0, 255, 1)">order</span> <span style="color: rgba(0, 0, 255, 1)">by</span> 排序字段).getclobval() <span style="color: rgba(0, 0, 255, 1)">FROM</span> 表名</pre>
