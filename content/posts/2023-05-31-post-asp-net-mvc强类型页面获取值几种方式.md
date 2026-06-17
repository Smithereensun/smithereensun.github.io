---
title: "Asp.Net MVC强类型页面获取值几种方式"
date: 2023-05-31
description: "方式一 (V:视图) 1 @{ 2 Layout = null; 3 } 4 5 &lt;!DOCTYPE html&gt; 6 &lt;html&gt; 7 &lt;head&gt; 8 &lt;meta name=&quot;viewport&quot; content=&quot;width="
tags:
  - "MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11260627.html"
---

<h1>方式一</h1>
<h3><span style="color: rgba(255, 0, 255, 1)">(V:视图)</span></h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)">@{
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">    Layout = null;
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 0, 1)">}
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 255, 1)">&lt;!</span><span style="color: rgba(255, 0, 255, 1)">DOCTYPE html</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">html</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">head</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 8</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">meta </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="viewport"</span><span style="color: rgba(255, 0, 0, 1)"> content</span><span style="color: rgba(0, 0, 255, 1)">="width=device-width"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 9</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">title</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>ShowCustomer<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">title</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">head</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">body</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">12</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">div</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">13</span>         <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">table</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">14</span>             <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">tr</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">15</span>                 <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">td</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>姓名:<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">td</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">16</span>                 <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">td</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>@Model.Age<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">td</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">17</span>             <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">tr</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">18</span>             <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">tr</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">19</span>                 <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">td</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>年龄:<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">td</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">20</span>                 <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">td</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>@Model.SName<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">td</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">21</span>             <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">tr</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">22</span>         <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">table</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">23</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">div</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">24</span> <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">body</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">html</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
