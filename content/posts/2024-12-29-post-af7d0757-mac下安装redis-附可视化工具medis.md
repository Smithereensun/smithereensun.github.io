---
title: "Mac下安装Redis，附可视化工具Medis"
date: 2024-12-29
description: "导读 我之前写过很多相关的redis的博文，有时候，为了开发，还得去虚拟机上搭建一个redis，感觉太麻烦了，为了做个demo，直接在自己mac本上安装一个即可。 Redis 从入门到精通：点我直达 Redis 微信抢红包，电商场景下秒杀系统设计：点我直达 Redis 高级项目实战：点我直达 安装"
tags:
  - "Redis"
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14227488.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　我之前写过很多相关的redis的博文，有时候，为了开发，还得去虚拟机上搭建一个redis，感觉太麻烦了，为了做个demo，直接在自己mac本上安装一个即可。</p>
<ul>
<li>Redis <span style="color: rgba(255, 0, 0, 1)"><strong>从入门到精通</strong></span>：<a href="https://www.cnblogs.com/chenyanbin/p/12073107.html" target="_blank">点我直达</a></li>
<li>Redis <span style="color: rgba(255, 0, 0, 1)"><strong>微信抢红包</strong></span>，电商场景下<span style="color: rgba(255, 0, 0, 1)"><strong>秒杀系统设计</strong></span>：<a href="https://www.cnblogs.com/chenyanbin/p/13587508.html" target="_blank">点我直达</a></li>
<li>Redis <span style="color: rgba(255, 0, 0, 1)"><strong>高级</strong></span>项目<span style="color: rgba(255, 0, 0, 1)"><strong>实战</strong></span>：<a href="https://www.cnblogs.com/chenyanbin/p/13506946.html" target="_blank">点我直达</a></li>
</ul>
<h1 style="text-align: center">安装</h1>
<h2>下载</h2>
<p><a href="https://redis.io/download" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202101/1504448-20210103233102736-1067113453.png" alt="" loading="lazy" /></p>
<h2>编译安装</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">解压:　　
    tar zxvf redis-4.0.14.tar.gz

移动到:　　
    mv redis-4.0.14.tar.gz /Users/chenyanbin/plus/

切换到:　　
    cd /Users/chenyanbin/plus/redis-6.0.9　　

编译测试: 
    sudo make test

编译安装:　　
    sudo make install

启动
    redis-server&amp;

测试
    redis-cli

停止
    redis-cli shutdown

查看是否启动
     ps axu|grep redis
登录指定redis
    redis-cli -h 127.0.0.1 -p 6379</span></pre>
