---
title: "JAVA 基础篇"
date: 2019-09-28
description: "一、数组 1、 什么是数组？ 数组和变量差不多，也是可以存放数据的，但是数组可以存放多个数据，而且多个数据的数据类型统一&#160;格式&#160;数据类型 [] 数组名称;&#160;还有一种等效的写法，不推荐&#160;数据类型 数组名称[];&#160;变量如果定义好了之后，要想使用，一定要赋"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11543927.html"
---

<h1>一、数组&nbsp;</h1>
<h2>1、 什么是数组？</h2>
<p>&nbsp;数组和变量差不多，也是可以存放数据的，但是数组可以存放多个数据，而且多个数据的数据类型统一<br>&nbsp;格式<br>&nbsp;数据类型 [] 数组名称;<br>&nbsp;还有一种等效的写法，不推荐<br>&nbsp;数据类型 数组名称[];<br>&nbsp;变量如果定义好了之后，要想使用，一定要赋值<br>&nbsp;数组如果定义好了之后，要想使用一定要初始化<br>&nbsp;初始化：就是在内存当中开辟数组的空间，并且赋值一些默认值(准备工作)<br>&nbsp;数组的初始化方式有两种：<br>&nbsp;1、动态初始化，指定数组的长度<br>&nbsp;2、静态初始化，指定数组的内容<br><br>&nbsp;动态初始化：直接指定数组的长度，也就是数组当中到底可以存放多少个数据<br>&nbsp;格式一、<br>&nbsp;数据类型[] 数组名称=new 数据类型[数组长度];<br>&nbsp;解析：<br>&nbsp;左侧数据类型：也就是数组当中存放的元素全部都是统一的什么类型<br>&nbsp;左侧的[]：代表这个一种数组类型<br>&nbsp;数组名称：就是一个自定义的标识符，通过名称，可以使用数组当中的数据<br>&nbsp;右侧的new：代表创建动作，内存当中开辟空间，创建数组<br>&nbsp;右侧数据类型：一定要和左侧的数据类型一样<br>&nbsp;右侧[]当中的数组长度：也就是到底能存放多少个数据<br>&nbsp;格式二、<br>&nbsp;数据类型[] 数组名称;<br>&nbsp;数组名称=new 数据类型[数组长度];</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> main(String[] args) {
</span><span style="color: rgba(0, 128, 128, 1)">2</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">格式一</span>
<span style="color: rgba(0, 128, 128, 1)">3</span>         <span style="color: rgba(0, 0, 255, 1)">int</span>[] array1=<span style="color: rgba(0, 0, 255, 1)">new</span> <span style="color: rgba(0, 0, 255, 1)">int</span>[<span style="color: rgba(128, 0, 128, 1)">2</span><span style="color: rgba(0, 0, 0, 1)">];        
</span><span style="color: rgba(0, 128, 128, 1)">4</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">格式二</span>
<span style="color: rgba(0, 128, 128, 1)">5</span>         <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)">[] arrar2;
</span><span style="color: rgba(0, 128, 128, 1)">6</span>         arrar2=<span style="color: rgba(0, 0, 255, 1)">new</span> <span style="color: rgba(0, 0, 255, 1)">int</span>[<span style="color: rgba(128, 0, 128, 1)">2</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)">7</span>     }</pre>
