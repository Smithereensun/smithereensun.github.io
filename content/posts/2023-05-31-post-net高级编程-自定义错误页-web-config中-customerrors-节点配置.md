---
title: ".Net高级编程-自定义错误页 web.config中<customErrors>节点配置"
date: 2023-05-31
description: "错误页 1、当页面发生错误的时候，ASP.Net会将错误信息展示出来(Sqlconnection的错误就能暴露连接字符串)，这样一来不好看，二来泄露网站的内部实现信息，给网站带来安全隐患，因此需要定制错误页，发生错误时显示开发人员定制的页面。404页面放点广告也好的嘛。 2、配置web.config"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11182387.html"
---

<h1>错误页</h1>
<p>　　1、当页面发生错误的时候，ASP.Net会将错误信息展示出来(Sqlconnection的错误就能暴露连接字符串)，这样一来不好看，二来泄露网站的内部实现信息，给网站带来安全隐患，因此需要定制错误页，发生错误时显示开发人员定制的页面。404页面放点广告也好的嘛。</p>
<p>　　2、配置web.config，配置customErrors区域：</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span>   &lt;system.web&gt;
<span style="color: rgba(0, 128, 128, 1)">2</span>     &lt;customErrors mode=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">on</span><span style="color: rgba(128, 0, 0, 1)">"</span> defaultRedirect=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">MyErrorPage.aspx</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)">3</span>       &lt;error statusCode=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">403</span><span style="color: rgba(128, 0, 0, 1)">"</span> redirect=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">NoAccess.html</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)">4</span>       &lt;error statusCode=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">404</span><span style="color: rgba(128, 0, 0, 1)">"</span> redirect=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">FileNotFound.html</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)">5</span>     &lt;/customErrors&gt;
<span style="color: rgba(0, 128, 128, 1)">6</span>   &lt;/system.web&gt;</pre>
