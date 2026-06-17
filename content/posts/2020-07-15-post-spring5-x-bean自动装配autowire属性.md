---
title: "Spring5.X bean自动装配Autowire属性"
date: 2020-07-15
description: "属性注入 set方法、构造函数、POJO、list、map、ref，属于手工注入，点我直达 Spring自动注入 使用&lt;bean&gt;元素的autowire属性为一个bean定义指定自动装配模式 autowire设置值 no：没有开启 byName：根据bean的id名称，注入到对应的属性里"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13304762.html"
---

<h1>属性注入</h1>
<ul>
<li>set方法、构造函数、POJO、list、map、ref，属于手工注入，<a href="https://www.cnblogs.com/chenyanbin/p/13303091.html" target="_blank">点我直达</a></li>
</ul>
<h1>Spring自动注入</h1>
<ul>
<li>使用&lt;bean&gt;元素的autowire属性为一个bean定义指定自动装配模式</li>
<li>autowire设置值
<ul>
<li>no：没有开启</li>
<li>byName：根据bean的id名称，注入到对应的属性里面</li>
<li>byType：根据bean需要注入的类型，注入到对应的属性里面
<ul>
<li>如果按照类型注入，存在2个以上bean的话会抛异常</li>
<li>expected single matching bean but found 2</li>
</ul>
</li>
<li>construcctor：通过构造函数注入，需要这个类型的构造函数</li>
</ul>
</li>
</ul>
<h2>byName演示</h2>
<p>applicationContext.xml</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;?</span><span style="color: rgba(255, 0, 255, 1)">xml version="1.0" encoding="UTF-8"</span><span style="color: rgba(0, 0, 255, 1)">?&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">beans </span><span style="color: rgba(255, 0, 0, 1)">xmlns</span><span style="color: rgba(0, 0, 255, 1)">="http://www.springframework.org/schema/beans"</span><span style="color: rgba(255, 0, 0, 1)">
       xmlns:xsi</span><span style="color: rgba(0, 0, 255, 1)">="http://www.w3.org/2001/XMLSchema-instance"</span><span style="color: rgba(255, 0, 0, 1)">
       xsi:schemaLocation</span><span style="color: rgba(0, 0, 255, 1)">="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">bean </span><span style="color: rgba(255, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">="video"</span><span style="color: rgba(255, 0, 0, 1)"> class</span><span style="color: rgba(0, 0, 255, 1)">="net.cybclass.sp.domain.Video"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="id"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="8"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="title"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="SpringBoot课程专题"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">bean</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">bean </span><span style="color: rgba(255, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">="videoOrder"</span><span style="color: rgba(255, 0, 0, 1)"> class</span><span style="color: rgba(0, 0, 255, 1)">="net.cybclass.sp.domain.VideoOrder"</span><span style="color: rgba(255, 0, 0, 1)"> autowire</span><span style="color: rgba(0, 0, 255, 1)">="byName"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="id"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="8"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="outTradeNo"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="12312"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">bean</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">beans</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
