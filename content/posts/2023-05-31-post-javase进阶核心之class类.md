---
title: "JavaSE进阶核心之class类"
date: 2023-05-31
description: "Java顶级对象之Object 什么是Object类 Object类位于java.lang包中，java.lang包包含着Java最基础和核心的类，在编译时会自动导入 Object类是所有java类的祖先，每个类都使用Object作为超类 常见方法 public final native Class"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13417358.html"
---

<h1 style="text-align: center">Java顶级对象之Object</h1>
<h2>什么是Object类</h2>
<ul>
<li>Object类位于java.lang包中，java.lang包包含着Java最基础和核心的类，在编译时会自动导入</li>
<li>Object类是所有java类的祖先，每个类都使用Object作为超类</li>
</ul>
<h2>常见方法</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">final</span> <span style="color: rgba(0, 0, 255, 1)">native</span> Class&lt;?&gt;<span style="color: rgba(0, 0, 0, 1)"> getClass()
讲解：获取对象的运⾏时class对象，class对象就是描述对象所属类的对象, 类的对象可以获取这个
类的基本信息，如名、包、字段、⽅法等
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">native</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> hashCode()
讲解：获取对象的散列值，集合框架中应⽤，去除，⽐如HashMap
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">boolean</span><span style="color: rgba(0, 0, 0, 1)"> equals(Object obj)
讲解：⽐较两个对象，如果这两个对象引⽤指向的是同⼀个对象，那么返回true，否则返回false
集合框架中有讲
</span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String toString()
讲解：⽤于返回⼀个可代表对象的字符串，看源码可以得知，默认返回格式如下：对象的class名称 </span>+<span style="color: rgba(0, 0, 0, 1)">
@ </span>+ hashCode的⼗六进制字符串,所以前⾯课程写对象时候，需要重写这个⽅法，⽅便调试</pre>
