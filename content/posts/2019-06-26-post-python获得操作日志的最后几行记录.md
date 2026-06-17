---
title: "Python获得操作日志的最后几行记录"
date: 2019-06-26
description: "该方法一般用于获得操作日志的最后几行记录 1 #!/usr/bin/env python 2 # -*- coding:utf-8 -*- 3 f = open(&#39;seek.txt&#39;, &#39;rb&#39;) 4 5 6 def get_file_last_line(accept"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10294682.html"
---

<p>该方法一般用于获得操作日志的最后几行记录</p>
<div class="cnblogs_code"><img id="code_img_closed_533a1947-2996-4353-8126-57dfe70ad979" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_533a1947-2996-4353-8126-57dfe70ad979" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_533a1947-2996-4353-8126-57dfe70ad979" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> #!/usr/bin/<span style="color: rgba(0, 0, 0, 1)">env python
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> # -*- coding:utf-<span style="color: rgba(128, 0, 128, 1)">8</span> -*-
<span style="color: rgba(0, 128, 128, 1)"> 3</span> f = open(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">seek.txt</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">rb</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> 
<span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">def get_file_last_line(accept_file):
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>     offs = -<span style="color: rgba(128, 0, 128, 1)">10</span>
<span style="color: rgba(0, 128, 128, 1)"> 8</span>     <span style="color: rgba(0, 0, 255, 1)">while</span><span style="color: rgba(0, 0, 0, 1)"> True:
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>         accept_file.seek(offs, <span style="color: rgba(128, 0, 128, 1)">2</span><span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 128, 1)">10</span>         data =<span style="color: rgba(0, 0, 0, 1)"> accept_file.readlines()
</span><span style="color: rgba(0, 128, 128, 1)">11</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> len(data) &gt; <span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">:
</span><span style="color: rgba(0, 128, 128, 1)">12</span>             print(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">文件最后一行:%s</span><span style="color: rgba(128, 0, 0, 1)">'</span> % (data[-<span style="color: rgba(128, 0, 128, 1)">1</span>].decode(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">utf-8</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">)))
</span><span style="color: rgba(0, 128, 128, 1)">13</span>             <span style="color: rgba(0, 0, 255, 1)">break</span>
<span style="color: rgba(0, 128, 128, 1)">14</span>         offs *= <span style="color: rgba(128, 0, 128, 1)">2</span>
<span style="color: rgba(0, 128, 128, 1)">15</span> 
<span style="color: rgba(0, 128, 128, 1)">16</span> 
<span style="color: rgba(0, 128, 128, 1)">17</span> get_file_last_line(f)</pre>
