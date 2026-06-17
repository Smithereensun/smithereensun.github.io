---
title: "Java基本数学运算之Math类"
date: 2023-05-31
description: "什么是Math类 Java操作数学运算相关的类 构造函数被私有化，所以不允许创建对象 都是静态方法，使用是直接类名.方法名 常用API //计算平⽅根 System.out.println(Math.sqrt(16)); //计算⽴⽅根 System.out.println(Math.cbrt(8)"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13417364.html"
---

<h1 style="text-align: center">什么是Math类</h1>
<ul>
<li>Java操作数学运算相关的类</li>
<li>构造函数被私有化，所以不允许创建对象</li>
<li>都是静态方法，使用是直接类名.方法名</li>
</ul>
<h2>常用API</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">计算平⽅根</span>
System.out.println(Math.sqrt(16<span style="color: rgba(0, 0, 0, 1)">));
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">计算⽴⽅根</span>
 System.out.println(Math.cbrt(8<span style="color: rgba(0, 0, 0, 1)">));
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">两个数的最⼤，⽀持int, long, float,double</span>
 System.out.println(Math.max(2.9,4.5<span style="color: rgba(0, 0, 0, 1)">));
 System.out.println(Math.min(</span>2.9,4.5<span style="color: rgba(0, 0, 0, 1)">));
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">ceil向上取整，更⼤的值⽅向靠拢, 中⽂是天花板</span>
 System.out.println(Math.ceil(19.7<span style="color: rgba(0, 0, 0, 1)">));
 System.out.println(Math.ceil(</span>-20.1<span style="color: rgba(0, 0, 0, 1)">));
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">floor向下取整，更⼩的值⽅向靠拢，中⽂是地板意思</span>
 System.out.println(Math.floor(19.7<span style="color: rgba(0, 0, 0, 1)">));
 System.out.println(Math.floor(</span>-20.1<span style="color: rgba(0, 0, 0, 1)">));
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">随机数</span>
 System.out.println(Math.random()); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">⼩于1⼤于0的double类型的数
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">产⽣1到10的随机数，int⽅法进⾏转换它会去掉⼩数掉后⾯的数字即只获取整数部分,不是四舍</span>
<span style="color: rgba(0, 0, 0, 1)">五⼊
 </span><span style="color: rgba(0, 0, 255, 1)">int</span> random=(<span style="color: rgba(0, 0, 255, 1)">int</span>)(Math.random()*10+1);</pre>
