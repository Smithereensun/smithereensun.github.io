---
title: "Linux MySQL Proxy 读写分离"
date: 2023-05-31
description: "导读 因为读写分离是建立在MySQL集群主从复制的基础上，还不了解的，先看我另一篇博客：点我直达 MySQL-Proxy简介 mysql-proxy是mysql官方提供的mysql中间件服务，上游可接入若干个mysql-client，后端可连接若干个mysql-server。它使用mysql协议，任"
tags:
  - "SQL"
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13157763.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　因为<span style="color: rgba(255, 0, 0, 1)"><strong>读写分离</strong></span>是<span style="color: rgba(255, 0, 0, 1)"><strong>建立在MySQL集群主从复制的基础上</strong></span>，还不了解的，先看我另一篇博客：<a href="https://www.cnblogs.com/chenyanbin/p/13154225.html" target="_blank">点我直达</a></p>
<h1 style="text-align: center">MySQL-Proxy简介</h1>
<p>　　mysql-proxy是mysql官方提供的mysql中间件服务，上游可接入若干个mysql-client，后端可连接若干个mysql-server。它使用mysql协议，任何使用mysql-client的上游无需修改任何代码，即可迁移至mysql-proxy上。mysql-proxy最基本的用法，就是作为一个请求拦截，请求中转的中间层：</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200618152104672-629555438.png" alt="" loading="lazy" />&nbsp;</p>
<p>　　进一步的，mysql-proxy可以分析与修改请求。拦截查询和修改结果，需要通过编写Lua脚本来完成。mysql-proxy允许用户指定Lua脚本对请求进行拦截，对请求进行分析与修改，它还允许用户指定Lua脚本对服务器的返回结果进行修改，加入一些结果集或者去除一些结果集均可。</p>
<p>　　根本上，mysql-proxy是一个官方提供的框架，具备良好的扩展性，可以用来完成：</p>
<ol>
<li>sql拦截与修改</li>
<li>性能分析与监控</li>
<li>读写分离</li>
<li>请求路由</li>
</ol>
<h2>下载</h2>
<p>官网链接：<a href="https://downloads.mysql.com/archives/proxy/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<div class="cnblogs_code">
<pre>百度云盘地址：https:<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">pan.baidu.com/s/1Aw1laIWYJVvHYshHXw4p_Q  密码: 9qif</span></pre>
