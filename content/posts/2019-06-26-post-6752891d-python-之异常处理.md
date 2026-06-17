---
title: "Python 之异常处理"
date: 2019-06-26
description: "一&#160;错误和异常 •错误分两种： 1、语法错误 1 #!/usr/bin/env python 2 # -*- coding:utf-8 -*- 3 # 举列 4 print(&#39;hello world&#39; # 少) 5 6 def test: # 少() 7 print(&#3"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10404920.html"
---

<h2>一&nbsp;错误和异常</h2>
<h3>•错误分两种：</h3>
<p>1、语法错误</p>
<div class="cnblogs_code"><img id="code_img_closed_1c409a86-3ac9-496a-abd0-c5b4ded9cdb7" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_1c409a86-3ac9-496a-abd0-c5b4ded9cdb7" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_1c409a86-3ac9-496a-abd0-c5b4ded9cdb7" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)">3</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 举列</span>
<span style="color: rgba(0, 128, 128, 1)">4</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">hello world</span><span style="color: rgba(128, 0, 0, 1)">'</span>  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 少)</span>
<span style="color: rgba(0, 128, 128, 1)">5</span> 
<span style="color: rgba(0, 128, 128, 1)">6</span> <span style="color: rgba(0, 0, 255, 1)">def</span> test:  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 少()</span>
<span style="color: rgba(0, 128, 128, 1)">7</span>     <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">hello world</span><span style="color: rgba(128, 0, 0, 1)">'</span>)</pre>
