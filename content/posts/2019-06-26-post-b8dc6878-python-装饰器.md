---
title: "Python 装饰器"
date: 2019-06-26
description: "装饰器：本质就是函数，功能是为其他函数添加附加功能 原则： a.不修改被修饰函数的源代码 b.不修改被修饰函数的调用方式 公式： 装饰器=高阶函数+函数嵌套+闭包 高阶函数的定义： a.函数接收的参数是一个函数名 b.函数的返回值是一个函数名 c.满足上述条件任意一个，都可称之为高阶函数 1 #!/"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10332168.html"
---

<p>装饰器：本质就是函数，功能是为其他函数添加附加功能</p>
<p>原则：</p>
<p>　　a.不修改被修饰函数的源代码</p>
<p>　　b.不修改被修饰函数的调用方式</p>
<p>公式：</p>
<p>　　装饰器=高阶函数+函数嵌套+闭包</p>
<p>高阶函数的定义：</p>
<p>　　a.函数接收的参数是一个函数名</p>
<p>　　b.函数的返回值是一个函数名</p>
<p>　　c.满足上述条件任意一个，都可称之为高阶函数</p>
<div class="cnblogs_code"><img id="code_img_closed_ba49b1da-a81b-4b68-b79c-778a4e0b05a6" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_ba49b1da-a81b-4b68-b79c-778a4e0b05a6" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_ba49b1da-a81b-4b68-b79c-778a4e0b05a6" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> 
<span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> foo():
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>     <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">你好呀！</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> 
<span style="color: rgba(0, 128, 128, 1)"> 8</span> 
<span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> test(func):
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">    func()
</span><span style="color: rgba(0, 128, 128, 1)">11</span> 
<span style="color: rgba(0, 128, 128, 1)">12</span> 
<span style="color: rgba(0, 128, 128, 1)">13</span> test(foo)</pre>
