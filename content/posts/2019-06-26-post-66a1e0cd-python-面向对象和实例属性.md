---
title: "Python 面向对象和实例属性"
date: 2019-06-26
description: "一、三大编程范式 编程范式即编程的方法论，标识一种编程风格。 我们学习完Python语法后，就可以写python代码了，然后每个人写代码的风格不同，这些不同的风格就代表了不同的流派。 如果把python的基本语法比作无数的基本功，那么不同的编程风格就好比不同的武林门派。 虽然大家风格不同，但是都可以"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10354830.html"
---

<h2>一、三大编程范式</h2>
<p>　　编程范式即编程的方法论，标识一种编程风格。</p>
<p>　　我们学习完Python语法后，就可以写python代码了，然后每个人写代码的风格不同，这些不同的风格就代表了不同的流派。</p>
<p>　　如果把python的基本语法比作无数的基本功，那么不同的编程风格就好比不同的武林门派。</p>
<p>　　虽然大家风格不同，但是都可以完成你的编程需求，Python是一门面向对象编程语言，但是到目前为止，你从未接触面向对象编程，然而你已经可以解决很多问题了，在Python中并没有人强制你使用哪一种固定的风格。</p>
<p>　　根本就没有什么门派是天下无敌的，不同的风格在不同的场景下都有各自的牛逼之处。</p>
<h3>编程范式：</h3>
<p>　　a.面向过程编程</p>
<p>　　b.函数式编程：函数式 = 编程语言定义的函数+数学意义的函数；通俗来讲，函数式就是用编程语言去实现数学函数。这种函数内对象是永恒不变的，要么参数是函数，要么返回值是函数，没有for和while循环，所有的循环都由递归去实现，无变量的赋值（即不用变量去保存状态），无赋值即不改变。</p>
<p>　　c.面向对象编程：定义类+实例对象的方式去实现面向对象的设计</p>
<div class="cnblogs_code"><img id="code_img_closed_d3826c5e-e4e7-4e9b-8958-7e5ff91d0a1b" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_d3826c5e-e4e7-4e9b-8958-7e5ff91d0a1b" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_d3826c5e-e4e7-4e9b-8958-7e5ff91d0a1b" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Dog:
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span>     <span style="color: rgba(0, 0, 255, 1)">def</span> <span style="color: rgba(128, 0, 128, 1)">__init__</span><span style="color: rgba(0, 0, 0, 1)">(self, name, gender, type):
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>         self.name =<span style="color: rgba(0, 0, 0, 1)"> name
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>         self.gender =<span style="color: rgba(0, 0, 0, 1)"> gender
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>         self.type =<span style="color: rgba(0, 0, 0, 1)"> type
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>     <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> bark(self):
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>         <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">一条名字为[%s]的[%s]，狂吠不止</span><span style="color: rgba(128, 0, 0, 1)">'</span> %<span style="color: rgba(0, 0, 0, 1)">(self.name, self.type))
</span><span style="color: rgba(0, 128, 128, 1)">10</span>     <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> eat(self):
</span><span style="color: rgba(0, 128, 128, 1)">11</span>         <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">[%s]正在啃骨头</span><span style="color: rgba(128, 0, 0, 1)">'</span> %<span style="color: rgba(0, 0, 0, 1)"> self.name)
</span><span style="color: rgba(0, 128, 128, 1)">12</span> 
<span style="color: rgba(0, 128, 128, 1)">13</span> 
<span style="color: rgba(0, 128, 128, 1)">14</span> dog1 = Dog(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">alex</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">female</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">京巴</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 128, 1)">15</span> dog1.bark()  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 一条名字为[alex]的[京巴]，狂吠不止</span></pre>
