---
title: "WebService跨域配置、Ajax跨域请求、附开发过程源码"
date: 2023-05-31
description: "项目开发过程中需要和其他公司的数据对接，当时我们公司提供的是WebService，本地测试，都是好的，Ajax跨域请求，就报错，配置WebService过程中，花了不少功夫，入不少坑，不过最终问题还是解决啦~~~特意将完整开发步骤记录下来，以备下次勿犯，废话不多说，直接上源码！ 第一步，右键，新建项"
tags:
  - "WebService"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11125758.html"
---

<p><span style="font-family: 仿宋">　　项目开发过程中需要和其他公司的数据对接，当时我们公司提供的是WebService，本地测试，都是好的，Ajax跨域请求，就报错，配置WebService过程中，花了不少功夫，入不少坑，不过最终问题还是解决啦~~~特意将完整开发步骤记录下来，以备下次勿犯，废话不多说，直接上源码！</span></p>
<h2><span style="font-family: 仿宋">第一步，右键，新建项，添加"web服务"</span></h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190703122921496-674877766.png" alt="" /></p>
<h2><span style="font-family: 仿宋">第二步：在webservice项目的web.config中添加如下配置，缺一不可：</span></h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> &lt;system.web&gt;
<span style="color: rgba(0, 128, 128, 1)"> 2</span>    &lt;webServices&gt;
<span style="color: rgba(0, 128, 128, 1)"> 3</span>       &lt;protocols&gt;
<span style="color: rgba(0, 128, 128, 1)"> 4</span>         &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">HttpGet</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)"> 5</span>         &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">HttpPost</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)"> 6</span>         &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">HttpSoap</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)"> 7</span>         &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Documentation</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)"> 8</span>       &lt;/protocols&gt;
<span style="color: rgba(0, 128, 128, 1)"> 9</span>     &lt;/webServices&gt;
<span style="color: rgba(0, 128, 128, 1)">10</span>   &lt;/system.web&gt;
<span style="color: rgba(0, 128, 128, 1)">11</span>   &lt;system.webServer&gt;
<span style="color: rgba(0, 128, 128, 1)">12</span>     &lt;httpProtocol&gt;
<span style="color: rgba(0, 128, 128, 1)">13</span>       &lt;customHeaders&gt;
<span style="color: rgba(0, 128, 128, 1)">14</span>         &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Access-Control-Allow-Methods</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">OPTIONS,POST,GET</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)">15</span>         &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Access-Control-Allow-Headers</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">x-requested-with,content-type</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)">16</span>         &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Access-Control-Allow-Origin</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">*</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)">17</span>       &lt;/customHeaders&gt;
<span style="color: rgba(0, 128, 128, 1)">18</span>     &lt;/httpProtocol&gt;
<span style="color: rgba(0, 128, 128, 1)">19</span>   &lt;/system.webServer&gt;</pre>
