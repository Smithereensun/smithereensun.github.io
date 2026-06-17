---
title: ".Net进程外session配置"
date: 2023-05-31
description: "目前ASP的开发人员都正在使用Session这一强大的功能，但是在他们使用的过程中却发现了ASP Session有以下缺陷： 进程依赖性：ASP Session状态存于IIS的进程中，也就是inetinfo.exe这个程序。所以当inetinfo.exe进程崩溃时，这些信息也就丢失。另外，重起或者关"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11178876.html"
---

<p>目前ASP的开发人员都正在使用Session这一强大的功能，但是在他们使用的过程中却发现了ASP Session有以下缺陷：</p>
<ul>
<li>进程依赖性：ASP Session状态存于IIS的进程中，也就是inetinfo.exe这个程序。所以当inetinfo.exe进程崩溃时，这些信息也就丢失。另外，重起或者关闭IIS服务都会造成信息的丢失。</li>
<li>Session状态使用范围的局限性：刚一个用户从一个网站访问到另外一个网站时，这些Session信息并不会随之迁移过去。例如：facebook网站的WWW服务器可能不止一个，一个用户登录之后要去各个频道浏览，但是每个频道都在不同的服务器上，如果想在这些WWW服务器共享Session信息怎么办呢？</li>
<li>Cookie的依赖性：实际上客户端的Session信息是存储与Cookie中的，如果客户端完全禁用掉了Cookie功能，他也就不能享受到了Session提供的功能了。</li>
</ul>
<p>鉴于ASP Session的以上缺陷，微软的设计者们在设计开发 ASP.NET Session时进行了相应的改进，完全克服了以上缺陷，使得ASP.NET Session成为了一个更加强大的功能。</p>
<p>解决方案：</p>
<h3>将服务器Session信息存储在进程外</h3>
<p>配置步骤：</p>
<p>　　1、开启 ASP.NET状态服务：cmd状态下：services.msc</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190712224845751-47262257.png" alt="" /></p>
<p>　　2、配置web.config文件，在system.web下加入如下配置</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">sessionState </span><span style="color: rgba(255, 0, 0, 1)">mode</span><span style="color: rgba(0, 0, 255, 1)">="StateServer"</span><span style="color: rgba(255, 0, 0, 1)"> stateConnectionString</span><span style="color: rgba(0, 0, 255, 1)">="tcpip=127.0.0.1:42424"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
