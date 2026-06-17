---
title: "Python module和包的总结"
date: 2020-08-19
description: "模块：为了编写可维护的代码，我们将很多函数分组，分别放到不同的文件里，这样，代码的可利用率提高，代码量减少。在Python中，一个 .py文件就称之为一个模块（module）。 模块有以下几种方式： a.Python标准库 b.第三方模块 c.引用程序自定义模块 引入模块方式： 1、import 模"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10339885.html"
---

<p>　　模块：为了编写可维护的代码，我们将很多函数分组，分别放到不同的文件里，这样，代码的可利用率提高，代码量减少。<strong><span style="color: rgba(255, 0, 0, 1)">在Python中，一个 .py文件就称之为一个模块（module）</span></strong>。</p>
<p><span style="color: rgba(0, 0, 0, 1)">　　模块有以下几种方式：</span></p>
<p><span style="color: rgba(0, 0, 0, 1)">　　　　a.Python标准库</span></p>
<p><span style="color: rgba(0, 0, 0, 1)">　　　　b.第三方模块</span></p>
<p><span style="color: rgba(0, 0, 0, 1)">　　　　c.引用程序自定义模块</span></p>
<p><span style="color: rgba(0, 0, 0, 1)">　　引入模块方式：</span></p>
<p><span style="color: rgba(0, 0, 0, 1)">　　　　1、import 模块名1,模块名2（调用：模块名1.函数名）</span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> 
<span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> add(x, y):
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> x+<span style="color: rgba(0, 0, 0, 1)">y
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> 
<span style="color: rgba(0, 128, 128, 1)"> 8</span> 
<span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> sub(x, y):
</span><span style="color: rgba(0, 128, 128, 1)">10</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> x-y</pre>
