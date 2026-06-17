---
title: "Python函数式编程"
date: 2019-06-26
description: "一、高阶函数 满足两个特性任何一个即为高阶函数 a.函数的传入参数是一个函数名 b.函数的返回值是一个函数名 1 #!/usr/bin/env python 2 # -*- coding:utf-8 -*- 3 num_1 = [1, 2, 10, 5, 7] 4 5 6 def map_test("
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10280141.html"
---

<p>一、高阶函数</p>
<p>　　满足两个特性任何一个即为高阶函数</p>
<p>　　　　a.函数的传入参数是一个函数名</p>
<p>　　　　b.函数的返回值是一个函数名</p>
<div class="cnblogs_code"><img id="code_img_closed_844bf367-4f75-42cf-95c9-7a6ec30345f5" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_844bf367-4f75-42cf-95c9-7a6ec30345f5" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_844bf367-4f75-42cf-95c9-7a6ec30345f5" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> num_1 = [1, 2, 10, 5, 7<span style="color: rgba(0, 0, 0, 1)">]
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> 
<span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> map_test(func, array):
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>     ret =<span style="color: rgba(0, 0, 0, 1)"> []
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>     <span style="color: rgba(0, 0, 255, 1)">for</span> i <span style="color: rgba(0, 0, 255, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> array:
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>         res =<span style="color: rgba(0, 0, 0, 1)"> func(i)
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">        ret.append(res)
</span><span style="color: rgba(0, 128, 128, 1)">11</span>     <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> ret
</span><span style="color: rgba(0, 128, 128, 1)">12</span> 
<span style="color: rgba(0, 128, 128, 1)">13</span> 
<span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> add_one(x):
</span><span style="color: rgba(0, 128, 128, 1)">15</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> x+1
<span style="color: rgba(0, 128, 128, 1)">16</span> 
<span style="color: rgba(0, 128, 128, 1)">17</span> 
<span style="color: rgba(0, 128, 128, 1)">18</span> <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> reduce_one(x):
</span><span style="color: rgba(0, 128, 128, 1)">19</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> x-1
<span style="color: rgba(0, 128, 128, 1)">20</span> 
<span style="color: rgba(0, 128, 128, 1)">21</span> 
<span style="color: rgba(0, 128, 128, 1)">22</span> <span style="color: rgba(0, 0, 255, 1)">print</span><span style="color: rgba(0, 0, 0, 1)">(map_test(add_one, num_1))
</span><span style="color: rgba(0, 128, 128, 1)">23</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(map_test(<span style="color: rgba(0, 0, 255, 1)">lambda</span> x: x-1<span style="color: rgba(0, 0, 0, 1)">, num_1))
</span><span style="color: rgba(0, 128, 128, 1)">24</span> 
<span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">内置函数:</span><span style="color: rgba(128, 0, 0, 1)">'</span>, list(map(<span style="color: rgba(0, 0, 255, 1)">lambda</span> x: x**2<span style="color: rgba(0, 0, 0, 1)">, num_1)))
</span><span style="color: rgba(0, 128, 128, 1)">26</span> 
<span style="color: rgba(0, 128, 128, 1)">27</span> msg = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">chenyanbin</span><span style="color: rgba(128, 0, 0, 1)">'</span>
<span style="color: rgba(0, 128, 128, 1)">28</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">匿名函数，小写转大写：</span><span style="color: rgba(128, 0, 0, 1)">'</span>, list(map(<span style="color: rgba(0, 0, 255, 1)">lambda</span> x: x.upper(), msg)))</pre>
