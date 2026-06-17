---
title: "C# 获取pdf长宽，反推pdf图纸类型"
date: 2019-10-18
description: "业务需求：读取pdf每页的长宽，然后根据国际标准，反推出pdf图纸类型 第一步：下载类库，并引入到项目中 链接：https://pan.baidu.com/s/1ud4-xhfDvi9OKolEBPwy-w&amp;shfl=sharepset 提取码：bnfk 第二步：实现 第三步：实际图纸 反推"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11698858.html"
---

<p>业务需求：读取pdf每页的长宽，然后根据国际标准，反推出pdf图纸类型</p>
<h2>第一步：下载类库，并引入到项目中</h2>
<p>链接：https://pan.baidu.com/s/1ud4-xhfDvi9OKolEBPwy-w&amp;shfl=sharepset <br>提取码：bnfk </p>
<h2>第二步：实现</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span>             <span style="color: rgba(0, 0, 255, 1)">string</span> path = <span style="color: rgba(128, 0, 0, 1)">@"</span><span style="color: rgba(128, 0, 0, 1)">C:\Users\Administrator\Desktop\图纸\WH440-C322-F01_322分段涂装预留图.pdf</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span>             PdfReader reader = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> PdfReader(path);
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span>             iTextSharp.text.Rectangle rc = reader.GetPageSize(<span style="color: rgba(128, 0, 128, 1)">1</span>); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">pdf拿到第一页数据</span>
<span style="color: rgba(0, 128, 128, 1)"> 4</span>             <span style="color: rgba(0, 0, 255, 1)">float</span> height = rc.Height; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">pdf的长</span>
<span style="color: rgba(0, 128, 128, 1)"> 5</span>             <span style="color: rgba(0, 0, 255, 1)">float</span> width = rc.Width;<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">pdf的宽            </span>
<span style="color: rgba(0, 128, 128, 1)"> 6</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> v1 = height * <span style="color: rgba(128, 0, 128, 1)">25.4</span> / <span style="color: rgba(128, 0, 128, 1)">72</span>; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">换算后真实高</span>
<span style="color: rgba(0, 128, 128, 1)"> 7</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> v2 = width * <span style="color: rgba(128, 0, 128, 1)">25.4</span> / <span style="color: rgba(128, 0, 128, 1)">72</span>; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">换算后真实宽</span>
<span style="color: rgba(0, 128, 128, 1)"> 8</span>             <span style="color: rgba(0, 0, 255, 1)">int</span> ii = (<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)">)Math.Floor(v1);
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">int iPageNum = reader.NumberOfPages; </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">获取pdf总页数</span>
<span style="color: rgba(0, 128, 128, 1)">10</span>             reader.Close(); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">不关闭会一直占用pdf资源，对接下来的操作会有影响</span></pre>
