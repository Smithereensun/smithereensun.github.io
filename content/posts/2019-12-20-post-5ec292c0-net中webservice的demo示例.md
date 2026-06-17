---
title: ".Net中WebService的Demo示例"
date: 2019-12-20
description: "一、创建一个Web服务 1.新建一个项目WebserverDemo 2.在项目处添加新建项，添加一个web服务 3.编辑TestServer.asmx文件 3.1 TestServer.asmx默认的代码是这样 1 /// &lt;summary&gt; 2 /// TestServer 的摘要说明"
tags:
  - "WebService"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11114944.html"
---

<h1>一、创建一个Web服务</h1>
<h3>1.新建一个项目WebserverDemo</h3>
<h3>&nbsp;2.在项目处添加新建项，添加一个web服务</h3>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190701163130122-688682503.png" alt="" /></p>
<h3>&nbsp;&nbsp;3.编辑TestServer.asmx文件</h3>
<h4>3.1 TestServer.asmx默认的代码是这样</h4>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span>     <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> TestServer 的摘要说明
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span>     <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 4</span>     [WebService(Namespace = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">http://tempuri.org/</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">)]
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>     [WebServiceBinding(ConformsTo =<span style="color: rgba(0, 0, 0, 1)"> WsiProfiles.BasicProfile1_1)]
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>     [System.ComponentModel.ToolboxItem(<span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">)]
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 若要允许使用 ASP.NET AJAX 从脚本中调用此 Web 服务，请取消注释以下行。 
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> [System.Web.Script.Services.ScriptService]</span>
<span style="color: rgba(0, 128, 128, 1)"> 9</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> TestServer : System.Web.Services.WebService
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)">11</span> 
<span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">        [WebMethod]
</span><span style="color: rgba(0, 128, 128, 1)">13</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> HelloWorld()
</span><span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">15</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Hello World</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">17</span>         
<span style="color: rgba(0, 128, 128, 1)">18</span>     }</pre>
