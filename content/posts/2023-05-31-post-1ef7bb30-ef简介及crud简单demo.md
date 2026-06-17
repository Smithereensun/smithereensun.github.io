---
title: "EF简介及CRUD简单DEMO"
date: 2023-05-31
description: "一、实体框架(Entity FrameWork)简介 • 简称EF • 与Asp.Net MVC关系与ADO.NET关系 • ADO.NET Entity FrameWork是微软以ADO.NET为基础所发展出来的对象关系对应(O/R Mapping)解决方法，早期被称为ObjectSpace，最新"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11221490.html"
---

<h1>一、实体框架(Entity FrameWork)简介</h1>
<p>　　• 简称EF</p>
<p>　　• 与Asp.Net MVC关系与ADO.NET关系</p>
<p>　　• ADO.NET Entity FrameWork是微软以ADO.NET为基础所发展出来的对象关系对应(O/R Mapping)解决方法，早期被称为ObjectSpace，最新版本是EF6.0【CodeOnly功能得到了更好的支持】</p>
<p>　　• 实体框架Entity FrameWork 是ADO.NET中的一组支持开发面向数据的软件应用程序的技术。是微软的一个ORM框架。</p>
<h1>二、什么是O/R Mapping</h1>
<p>　　• 广义上：ORM指的是面向对象的对象模型和关系型数据库接口之间的相互转换。</p>
<p>　　• 狭义上，ORM可以被认为是，基于关系型数据库的数据存储，实现一个虚拟的面向对象的数据访问接口。理想情况下，基于这样一个面向对象的接口，持久化一个OO对象应该不需要了解任何关系型数据库存储数据的实现细节。</p>
<h2>EF简单演示</h2>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>第一步：右击--&gt;添加新项--&gt;ADO.NET 实体数据模型</strong></span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190721200417766-1019732367.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>第二步：实体数据模型向导，默认即可</strong></span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190721200441850-627063055.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>第三步：新建连接</strong></span></p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190721200532551-1353340432.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190721200618009-1278407818.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>第四步：勾上(是，在连接字符串中包含敏感数据)，下一步</strong></span></p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190721200751344-1998925069.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>第五步：选择模型中包括那些数据库表，完成即可</strong></span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190721200828395-74162882.png" alt="" /></p>
<div class="cnblogs_code"><img id="code_img_closed_4de17412-2719-4cb8-b1a8-31c30da4b474" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_4de17412-2719-4cb8-b1a8-31c30da4b474" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_4de17412-2719-4cb8-b1a8-31c30da4b474" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Collections.Generic;
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Linq;
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Text;
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Threading.Tasks;
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> 
<span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> EFDemoFirst
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>     <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Program
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)">11</span>         <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span> Main(<span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)">[] args)
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">13</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">添加一个添加操作
</span><span style="color: rgba(0, 128, 128, 1)">14</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">1、声明一个EF的上下文</span>
<span style="color: rgba(0, 128, 128, 1)">15</span>             DEMOEntities dbContext = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> DEMOEntities();
</span><span style="color: rgba(0, 128, 128, 1)">16</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">2、声明一个实体</span>
<span style="color: rgba(0, 128, 128, 1)">17</span>             T_Seats seats = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> T_Seats();
</span><span style="color: rgba(0, 128, 128, 1)">18</span>             seats.userName = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">test</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">19</span>             seats.pwdWord = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">test1123</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">20</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">3、告诉EF做一个插入操作</span>
<span style="color: rgba(0, 128, 128, 1)">21</span> <span style="color: rgba(0, 0, 0, 1)">            dbContext.T_Seats.Add(seats);
</span><span style="color: rgba(0, 128, 128, 1)">22</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">4、告诉上下文，把实体的变化保存到数据库里面去</span>
<span style="color: rgba(0, 128, 128, 1)">23</span> <span style="color: rgba(0, 0, 0, 1)">            dbContext.SaveChanges();
</span><span style="color: rgba(0, 128, 128, 1)">24</span>             Console.Write(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ok</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">            Console.ReadKey();
</span><span style="color: rgba(0, 128, 128, 1)">26</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">27</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">28</span> }</pre>
