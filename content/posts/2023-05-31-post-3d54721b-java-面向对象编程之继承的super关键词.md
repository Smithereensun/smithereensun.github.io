---
title: "Java 面向对象编程之继承的super关键词"
date: 2023-05-31
description: "java 继承里面的super关键词 super关键词 一个引用变量，用于引用父类对象 父类和子类都具有相同的命名属性，要调用父类中的属性时使用 super也是父类的构造函数，格式super(参数) 注意点，调用super()必须是类构造函数中的第一个语句，否则编译不通过 注意 每个子类构造方法的第"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13377491.html"
---

<h1 style="text-align: center">java 继承里面的super关键词</h1>
<h2>super关键词</h2>
<ul>
<li>一个引用变量，用于引用父类对象</li>
<li>父类和子类都具有相同的命名属性，要调用父类中的属性时使用</li>
<li>super也是父类的构造函数，格式super(参数)
<ul>
<li>注意点，调用super()必须是类构造函数中的第一个语句，否则编译不通过</li>
</ul>
</li>
<li>注意
<ul>
<li>每个子类构造方法的第一条语句，都是隐含地调用super()，如果父类没有这种形式的构造函数，那么在编译的时候就会报错</li>
</ul>
</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Father {
 </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Father(){
 System.out.println(</span>"father ⽆参构造函数"<span style="color: rgba(0, 0, 0, 1)">);
 }
}
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> Children <span style="color: rgba(0, 0, 255, 1)">extends</span><span style="color: rgba(0, 0, 0, 1)"> Father{
 </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Children(){
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">默认存在，写和不写都⾏</span>
 <span style="color: rgba(0, 0, 255, 1)">super</span><span style="color: rgba(0, 0, 0, 1)">();
 System.out.println(</span>"Child⽆参构造函数"<span style="color: rgba(0, 0, 0, 1)">);
 }
}</span></pre>
