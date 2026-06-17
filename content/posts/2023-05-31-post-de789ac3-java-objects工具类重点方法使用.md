---
title: "Java Objects工具类重点方法使用"
date: 2023-05-31
description: "Objects工具类 jdk 1.7引进的工具类，都是静态调用的方法，jdk 1.8新增了部分方法 重点方法 equals 用于字符串和包装对象的比较，先比较内存地址，再比较值 deepEquals 数组的比较，先比较内存地址，再比较值，如String、char、byte、int数组，或者包装类型I"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13407269.html"
---

<p>&nbsp;</p>
<h1 style="text-align: center">Objects工具类</h1>
<ul>
<li>jdk 1.7引进的工具类，都是静态调用的方法，jdk 1.8新增了部分方法</li>
<li>重点方法
<ul>
<li>equals
<ul>
<li>用于字符串和包装对象的比较，先比较内存地址，再比较值</li>
</ul>
</li>
<li>deepEquals
<ul>
<li>数组的比较，先比较内存地址，再比较值，如String、char、byte、int数组，或者包装类型Integer等数组</li>
</ul>
</li>
<li>hashCode
<ul>
<li>返回对象的hashCode，若传入的为null，则返回0</li>
</ul>
</li>
<li>hash
<ul>
<li>传入可变参数的所有值得hashCode的总和，底层用Arrays.hashCode</li>
</ul>
</li>
<li>可变参数</li>
</ul>
</li>
</ul>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200730232751795-2080401081.png" alt="" loading="lazy" /></p>
<h1 style="text-align: center">重写HashCode和Equals</h1>
<h2>HashCode方法</h2>
<p>　　顶级类Object里面的方法，所有类都是继承Object的，返回值int类型</p>
<p>　　根据一定的hash规则(存储地址，字段，或者长度等)，映射成一个数值，即散列值</p>
<h2>Equals方法</h2>
<p>　　顶级类Object里面的方法，所有类都是继承Object的，返回值boolean类型</p>
<p>　　根据自定义的匹配规则，用于匹配两个对象是否一样，一般逻辑</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">判断地址是否⼀样
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">⾮空判断和class类型判断
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">强转
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">对象⾥⾯的字段⼀⼀匹配</span></pre>
