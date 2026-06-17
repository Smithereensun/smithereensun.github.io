---
title: "Spring.Net 依赖注入"
date: 2023-05-31
description: "一、Spring.Net概念 编程模型(Ioc，DI方式) IoC：控制反转 原来创建对象的权利由程序来控制就是new实例，IoC就是改由容器来创建，相当于一个工厂， DI：依赖注入 没有IoC就没有DI，DI：容器在创建对象时，通过读取配置文件（一般是xml）设置的默认值，使其在创建时就拥有了某些"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11343146.html"
---

<h1>一、Spring.Net概念</h1>
<h2>　　编程模型(Ioc，DI方式)</h2>
<p>IoC：控制反转 <br>原来创建对象的权利由程序来控制就是new实例，IoC就是改由容器来创建，相当于一个工厂， <br>DI：依赖注入 <br>没有IoC就没有DI，DI：容器在创建对象时，通过读取配置文件（一般是xml）设置的默认值，使其在创建时就拥有了某些注入的值。　　</p>
<h2>　　什么是Spring.net？</h2>
<p>spring是一个依赖注入的设计框架，使项目层与层之间解耦达到更灵活的使用。Spring.net是Spring中支持.net开发的框架。 <br>Spring.net是一个企业级的重型依赖注入框架应用框架。Spring.Net会让应用性能下降，不过它的灵活的优点远大于缺点。适合用来做企业的oa系统之类的。<br>Spring.net能够干什么？ <br>在core（核心）和AOP（模型支持，属性反转，接受注入）之上支持： <br>1， MSQ（消息队列） <br>2， MVC <br>3， WEB <br>4， Quartz.net <br>Spring.net能做到的不止如此。</p>
<h1>&nbsp;二、DEMO示例</h1>
<p>新建一个控制台程序，程序比较简单，直接上代码</p>
<h2><span style="color: rgba(255, 0, 255, 1)"><strong>老方法</strong></span></h2>
<p>Program.cs</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> 
<span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> Spring.Net.DEMO
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>     <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Program
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>         <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span> Main(<span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)">[] args)
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>             IUserInfoDal UserInfo = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> UserInfoDal();
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">            UserInfo.Show();
</span><span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">            Console.ReadKey();
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">14</span> }</pre>
