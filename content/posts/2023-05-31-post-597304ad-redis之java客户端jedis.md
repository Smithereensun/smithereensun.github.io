---
title: "Redis之Java客户端Jedis"
date: 2023-05-31
description: "导读 Redis不仅使用命令客户端来操作，而且可以使用程序客户端操作。 现在基本上主流的语言都有客户端支持，比如Java、C、C#、C++、php、Node.js、Go等。 在官方网站里列一些Java的客户端，有Jedis、Redisson、Jredis、JDBC-Redis等，其中官方推荐使用Je"
tags:
  - "JAVA"
  - "分布式架构"
  - "NoSql"
  - "Redis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12088796.html"
---

<h1 style="text-align: center">导读</h1>
<ul>
<li>Redis不仅使用命令客户端来操作，而且可以使用程序客户端操作。</li>
<li>现在基本上主流的语言都有客户端支持，比如Java、C、C#、C++、php、Node.js、Go等。</li>
<li>在官方网站里列一些Java的客户端，有Jedis、Redisson、Jredis、JDBC-Redis等，其中官方推荐使用Jedis和Redisson。</li>
<li>在企业中用的最多的就是Jedis</li>
<li>Jedis同样也是托管在github上，地址：<span><a href="https://github.com/xetorthio/jedis" rel="noopener nofollow">https://github.com/xetorthio/jedis</a></span></li>
</ul>
<h1 style="text-align: center">linux 关闭防火墙</h1>
<p>具体在liunx上如何配置Redis，请参考：<a id="cb_post_title_url" class="postTitle2" href="https://www.cnblogs.com/chenyanbin/p/12073107.html">分布式架构-Redis 从入门到精通 完整案例 附源码</a></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)"> service iptables stop   命令关闭防火墙，但是系统重启后会开启

 chkconfig iptables off--关闭防火墙开机自启动</span></pre>
