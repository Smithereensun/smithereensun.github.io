---
title: "Python 反射"
date: 2019-06-26
description: "一 反射 什么是反射？ 反射的概念由smith在1982年首次提出的，主要是指程序可以访问、检测和修改它本身状态或行为的一种能力。这一概念的提出很快引发了计算机科学领域关于应用反射性的研究。它首先被程序语言的设计领域所采用，并在List和面向对象方面取得了成绩。 4个可以实现反射的函数 下列方法适用"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10362857.html"
---

<h2>一 反射</h2>
<p>什么是反射？</p>
<p>　　反射的概念由smith在1982年首次提出的，主要是指程序可以访问、检测和修改它本身状态或行为的一种能力。这一概念的提出很快引发了计算机科学领域关于应用反射性的研究。它首先被程序语言的设计领域所采用，并在List和面向对象方面取得了成绩。</p>
<p>4个可以实现反射的函数</p>
<p>下列方法适用于类和对象</p>
<div class="cnblogs_code"><img id="code_img_closed_57ede0d0-8c6d-4895-8c4e-5d8e4994244c" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_57ede0d0-8c6d-4895-8c4e-5d8e4994244c" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_57ede0d0-8c6d-4895-8c4e-5d8e4994244c" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> 
<span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 判断object中有没有一个name字符串对应的方法或属性</span>
<span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> BlackMedium:
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>     feture = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">Ugly</span><span style="color: rgba(128, 0, 0, 1)">'</span>
<span style="color: rgba(0, 128, 128, 1)"> 8</span> 
<span style="color: rgba(0, 128, 128, 1)"> 9</span>     <span style="color: rgba(0, 0, 255, 1)">def</span> <span style="color: rgba(128, 0, 128, 1)">__init__</span><span style="color: rgba(0, 0, 0, 1)">(self, name, addr):
</span><span style="color: rgba(0, 128, 128, 1)">10</span>         self.name =<span style="color: rgba(0, 0, 0, 1)"> name
</span><span style="color: rgba(0, 128, 128, 1)">11</span>         self.addr =<span style="color: rgba(0, 0, 0, 1)"> addr
</span><span style="color: rgba(0, 128, 128, 1)">12</span> 
<span style="color: rgba(0, 128, 128, 1)">13</span>     <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> sell_hourse(self):
</span><span style="color: rgba(0, 128, 128, 1)">14</span>         <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">【%s】正在卖房子</span><span style="color: rgba(128, 0, 0, 1)">'</span> %<span style="color: rgba(0, 0, 0, 1)"> self.name)
</span><span style="color: rgba(0, 128, 128, 1)">15</span> 
<span style="color: rgba(0, 128, 128, 1)">16</span>     <span style="color: rgba(0, 0, 255, 1)">def</span><span style="color: rgba(0, 0, 0, 1)"> rent_hourse(self):
</span><span style="color: rgba(0, 128, 128, 1)">17</span>         <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">【%s】正在租房子</span><span style="color: rgba(128, 0, 0, 1)">'</span> %<span style="color: rgba(0, 0, 0, 1)"> self.name)
</span><span style="color: rgba(0, 128, 128, 1)">18</span> 
<span style="color: rgba(0, 128, 128, 1)">19</span> 
<span style="color: rgba(0, 128, 128, 1)">20</span> b1 = BlackMedium(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">alex</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">雪峰路</span><span style="color: rgba(128, 0, 0, 1)">'</span>)  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> bl.name---&gt;b1.__dic['name']</span>
<span style="color: rgba(0, 128, 128, 1)">21</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(hasattr(b1, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">name</span><span style="color: rgba(128, 0, 0, 1)">'</span>))  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> True</span></pre>
