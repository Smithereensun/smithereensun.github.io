---
title: "Python 添加环境变量"
date: 2019-06-26
description: "目录示例 •目的：在index中引入模块start下的方法 index.py start.py"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10398685.html"
---

<h2>目录示例</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201902/1504448-20190218234827848-1733553699.png" alt="" /></p>
<p>&nbsp;</p>
<p><span style="font-size: 18px">•</span>目的：在index中引入模块start下的方法</p>
<h2>index.py</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> 
<span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <strong><span style="color: rgba(255, 0, 0, 1)">import sys,os
</span></strong><span style="color: rgba(0, 128, 128, 1)"> 6</span> <strong><span style="color: rgba(255, 0, 0, 1)">BASE_DIR = os.path.dirname(os.path.dirname(__file__))
</span></strong><span style="color: rgba(0, 128, 128, 1)"> 7</span> <strong><span style="color: rgba(255, 0, 0, 1)">sys.path.append(BASE_DIR)
</span></strong><span style="color: rgba(0, 128, 128, 1)"> 8</span> 
<span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 255, 1)">from</span> conf <span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> start
</span><span style="color: rgba(0, 128, 128, 1)">10</span> start.Say_hi()  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> hello world</span></pre>
