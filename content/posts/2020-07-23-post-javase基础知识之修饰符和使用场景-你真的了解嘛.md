---
title: "JavaSE基础知识之修饰符和使用场景，你真的了解嘛"
date: 2020-07-23
description: "修饰符的作用是啥？ 用来定义类、方法或者变量的访问权限 两大类 访问修饰符 限定类、属性或方法是否可以被程序里的其他部分访问和调用的修饰符 private&lt;default&lt;protected&lt;public 非访问修饰符 例如static、final、abstract、synchro"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13363531.html"
---

<h1 style="text-align: center">修饰符的作用是啥？</h1>
<p>　　用来定义类、方法或者变量的访问权限</p>
<h2>两大类</h2>
<h3>访问修饰符</h3>
<ul>
<li>限定类、属性或方法是否可以被程序里的其他部分访问和调用的修饰符
<ul>
<li>private&lt;default&lt;protected&lt;public</li>
</ul>
</li>
</ul>
<h3>非访问修饰符</h3>
<ul>
<li>例如static、final、abstract、synchronized等</li>
</ul>
<h2>死记硬背</h2>
<ul>
<li>外部类修饰符：public或者为默认(default)</li>
<li>方法、属性修饰符：private、default、protected、public
<ul>
<li>public -&gt;公开对外部可见</li>
<li>protected -&gt;对包和所有子类可见</li>
<li>private -&gt;仅对类内部可见</li>
</ul>
</li>
</ul>
<h2>方法级别&nbsp;</h2>
<table border="0">
<tbody>
<tr>
<td>修饰符</td>
<td>当前类</td>
<td>同一包内</td>
<td>不同包中的子类</td>
<td>不同包中的非子类</td>
</tr>
<tr>
<td>public</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
</tr>
<tr>
<td>protected</td>
<td>Y</td>
<td>Y</td>
<td>Y</td>
<td>N</td>
</tr>
<tr>
<td>default</td>
<td>Y</td>
<td>Y</td>
<td>N</td>
<td>N</td>
</tr>
<tr>
<td>private</td>
<td>Y</td>
<td>N</td>
<td>N</td>
<td>N</td>
</tr>
</tbody>
</table>
<p>我们主要来验证下，不熟悉的default，<span style="color: rgba(255, 0, 0, 1)"><strong>什么修饰符都不加，默认为default，必须要在同一包下，才能访问的到！！！！</strong></span></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200722224005353-1644145763.gif" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
