---
title: "ASP.Net MVC过滤器"
date: 2023-05-31
description: "1、微软为ASP.Net MVC 提供4种过滤器 • Action过滤器(IAActionFilter):在Action执行之前和执行之后分别做一些操作 •&#160;View结果渲染过滤器(IResultFilter):在View结果渲染之前和View渲染之后分别做一些操作 • 全局异常过滤器:A"
tags:
  - "MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11279739.html"
---

<h1>1、微软为ASP.Net MVC 提供4种过滤器</h1>
<p>　　• Action过滤器(IAActionFilter):在Action执行之前和执行之后分别做一些操作</p>
<p>　　•&nbsp;View结果渲染过滤器(IResultFilter):在View结果渲染之前和View渲染之后分别做一些操作</p>
<p>　　• 全局异常过滤器:ActionFilterAttribute:当整个网站出现异常，做过滤器中的代码</p>
<p>　　• 身份验证过滤器</p>
<h1>2、DEMO示例(Action和View)</h1>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>第一步：在Models文件夹下创建一个类MyActionFilterAttribute.cs(<span style="color: rgba(255, 0, 0, 1)">注:Attribute结束</span>)</strong></span></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>第二步：继承筛选器特性的基类:ActionFilterAttribute，并重写基类下的4个方法</strong></span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Collections.Generic;
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Linq;
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Web;
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Web.Mvc;
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> 
<span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> MVCDemo2.Models
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> MyActionFilterAttribute:ActionFilterAttribute
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)">11</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">string</span> Name { <span style="color: rgba(0, 0, 255, 1)">get</span>; <span style="color: rgba(0, 0, 255, 1)">set</span><span style="color: rgba(0, 0, 0, 1)">; }
</span><span style="color: rgba(0, 128, 128, 1)">12</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">13</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 在Action执行之前先执行此方法
</span><span style="color: rgba(0, 128, 128, 1)">14</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">15</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="filterContext"&gt;</span><span style="color: rgba(0, 128, 0, 1)">筛选器上下文。</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">16</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">override</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> OnActionExecuted(ActionExecutedContext filterContext)
</span><span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">18</span>             <span style="color: rgba(0, 0, 255, 1)">base</span><span style="color: rgba(0, 0, 0, 1)">.OnActionExecuted(filterContext);
</span><span style="color: rgba(0, 128, 128, 1)">19</span>             filterContext.HttpContext.Response.Write(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">OnActionExecuted---</span><span style="color: rgba(128, 0, 0, 1)">"</span>+Name + <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">&lt;br /&gt;</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">20</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">21</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">22</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 在Action执行之后执行此方法
</span><span style="color: rgba(0, 128, 128, 1)">23</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">24</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="filterContext"&gt;</span><span style="color: rgba(0, 128, 0, 1)">筛选器上下文。</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">25</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">override</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> OnActionExecuting(ActionExecutingContext filterContext)
</span><span style="color: rgba(0, 128, 128, 1)">26</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">27</span>             <span style="color: rgba(0, 0, 255, 1)">base</span><span style="color: rgba(0, 0, 0, 1)">.OnActionExecuting(filterContext);
</span><span style="color: rgba(0, 128, 128, 1)">28</span>             filterContext.HttpContext.Response.Write(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">OnActionExecuting---</span><span style="color: rgba(128, 0, 0, 1)">"</span> + Name+<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">&lt;br /&gt;</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">29</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">30</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">31</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 在View渲染之前先执行此方法
</span><span style="color: rgba(0, 128, 128, 1)">32</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">33</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="filterContext"&gt;</span><span style="color: rgba(0, 128, 0, 1)">筛选器上下文。</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">34</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">override</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> OnResultExecuted(ResultExecutedContext filterContext)
</span><span style="color: rgba(0, 128, 128, 1)">35</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">36</span>             <span style="color: rgba(0, 0, 255, 1)">base</span><span style="color: rgba(0, 0, 0, 1)">.OnResultExecuted(filterContext);
</span><span style="color: rgba(0, 128, 128, 1)">37</span>             filterContext.HttpContext.Response.Write(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">OnResultExecuted---</span><span style="color: rgba(128, 0, 0, 1)">"</span> + Name + <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">&lt;br /&gt;</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">38</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">39</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">40</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 在View渲染之后执行此方法
</span><span style="color: rgba(0, 128, 128, 1)">41</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">42</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="filterContext"&gt;</span><span style="color: rgba(0, 128, 0, 1)">筛选器上下文。</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">43</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">override</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> OnResultExecuting(ResultExecutingContext filterContext)
</span><span style="color: rgba(0, 128, 128, 1)">44</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">45</span>             <span style="color: rgba(0, 0, 255, 1)">base</span><span style="color: rgba(0, 0, 0, 1)">.OnResultExecuting(filterContext);
</span><span style="color: rgba(0, 128, 128, 1)">46</span>             filterContext.HttpContext.Response.Write(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">OnResultExecuting---</span><span style="color: rgba(128, 0, 0, 1)">"</span> + Name + <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">&lt;br /&gt;</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">47</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">48</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">49</span> }</pre>
