---
title: ".Net Mvc过滤器观察者模式记录网站报错信息"
date: 2023-05-31
description: "基本介绍： 观察者模式是一种对象行为模式。它定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。在观察者模式中，主题是通知的发布者，它发出通知时并不需要知道谁是它的观察者，可以有任意数目的观察者订阅并接收通知。观察者模式不仅被广泛应用于软件界面元素"
tags:
  - "MVC"
  - "设计模式"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11373817.html"
---

<h3>基本介绍：</h3>
<p>　　观察者模式是一种对象行为模式。它定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知并被自动更新。在观察者模式中，主题是通知的发布者，它发出通知时并不需要知道谁是它的观察者，可以有任意数目的观察者订阅并接收通知。观察者模式不仅被广泛应用于软件界面元素之间的交互，在业务对象之间的交互、权限管理等方面也有广泛的应用。</p>
<h1>第一步：自定义过滤器错误类(MyExceptionFilterAttribute.cs)</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> Sam.OA.Common;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Web.Mvc;
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> 
<span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> Sam.OA.WEBAPP.Models
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> MyExceptionFilterAttribute: HandleErrorAttribute
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">override</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> OnException(ExceptionContext filterContext)
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">10</span>             <span style="color: rgba(0, 0, 255, 1)">base</span><span style="color: rgba(0, 0, 0, 1)">.OnException(filterContext);
</span><span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">            LogHelper.WriteLog(filterContext.Exception.ToString());
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">14</span> }</pre>
