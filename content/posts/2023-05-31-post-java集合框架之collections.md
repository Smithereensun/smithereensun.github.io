---
title: "Java集合框架之Collections"
date: 2023-05-31
description: "Collections工具类 Java里关于聚合的工具类，包含有各种有关集合操作的静态多态方法，不能实例化(把构造函数私有化) public class Collections { // Suppresses default constructor, ensuring non-instantiabi"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13401255.html"
---

<h1 style="text-align: center">Collections工具类</h1>
<ul>
<li>Java里关于聚合的工具类，包含有各种有关集合操作的静态多态方法，不能实例化(把构造函数私有化)</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Collections {
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Suppresses default constructor, ensuring non-instantiability.</span>
    <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> Collections() {
    }
}</span></pre>
