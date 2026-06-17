---
title: "Java 从入门到精通-反射机制"
date: 2023-05-31
description: "导读 Java反射机制是开发者迈向结构化开发的重要一步，同时掌握了反射机制也就掌握了所有框架的核心实现思想。 认识反射机制 简单例子 通过以上的程序就会发现，除了对象的正向处理操作之外，还可以通过getClass()方法来获取一个类对应的完整的信息的结构，而这就是反射的开始。 Class类对象实例化"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13030159.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　Java反射机制是开发者迈向结构化开发的重要一步，同时掌握了反射机制也就掌握了所有框架的核心实现思想。</p>
<h1 style="text-align: center">认识反射机制</h1>
<h2>简单例子</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200602112535899-231393929.png" alt="" /></p>
<p>　　通过以上的程序就会发现，除了对象的正向处理操作之外，还可以通过getClass()方法来获取一个类对应的完整的信息的结构，而这就是反射的开始。</p>
<h1 style="text-align: center">Class类对象实例化</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200602135656549-1177738822.png" alt="" /></p>
<p>　　在整个反射机制之中，Class类是整个反射操作的源头所在，如果现在可以获取Class类的对象，那么就可以进行所有的更加深层次的反射操作(上面案例仅仅是根据实例化对象的Class获取了类的基本名称)。</p>
<p>　　在Java的处理机制之中，实际上会有三种方式可以获取Class类的实例化对象。</p>
<p>方式一、</p>
<p>　　由于在Object类中提供有getClass()方法，所以任意的实例化对象都可以通过此方法来获取Class类的对象实例。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200602131955231-522803024.png" alt="" /></p>
<p>方式二、</p>
<p>　　在Java处理过程之中，可以直接使用“<span style="color: rgba(255, 0, 0, 1)"><strong>类名称.class</strong></span>”的形式直接在没有产生实例化对象的时候获取Class类的实例。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200602132950924-1498301999.png" alt="" /></p>
<p>　　这个时候输出会直接通过toString()方法来获取相关的对象完整信息。</p>
<p>方式三、</p>
<p>　　在Class类的内部提供一个根据“类名称”字符串实现类反射加载的处理方法</p>
<div class="cnblogs_code">
<pre> <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> Class&lt;?&gt; forName(String className) <span style="color: rgba(0, 0, 255, 1)">throws</span> ClassNotFoundException {}</pre>
