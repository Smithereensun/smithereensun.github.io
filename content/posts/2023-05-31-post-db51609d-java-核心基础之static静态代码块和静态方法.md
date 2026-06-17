---
title: "Java 核心基础之static静态代码块和静态方法"
date: 2023-05-31
description: "static静态代码块和静态方法 static关键字 static修饰的方法或变量，优先于对象执行，所以内存会先有static修饰的内容，后有对象的内容 可以用来修饰类的成员方法、类的成员变量，还可以编写static静态代码块 修饰变量就是类变量，修饰方法就是类方法 总结：类变量或者类方法，可以直接"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13376187.html"
---

<h1 style="text-align: center">static静态代码块和静态方法</h1>
<h2>static关键字</h2>
<ul>
<li>static修饰的方法或变量，优先于对象执行，所以内存会先有static修饰的内容，后有对象的内容</li>
<li>可以用来修饰类的成员方法、类的成员变量，还可以编写static静态代码块</li>
<li>修饰变量就是类变量，修饰方法就是类方法</li>
<li>总结：类变量或者类方法，可以直接通过类名.方法名或者变量名进行调用，不用经过对象</li>
</ul>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Student{
        </span><span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> age;
        </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> String name;
        </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> speak() {
            System.out.println(</span>"唱歌🎤"<span style="color: rgba(0, 0, 0, 1)">);
        }
    }</span></pre>
