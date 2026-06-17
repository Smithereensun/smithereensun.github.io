---
title: "Mac 安装Nacos"
date: 2020-11-21
description: "导读 Nacos是阿里巴巴集团开源的一个易于使用的平台，专为动态服务发现，配置和服务管理而设计。可用于替代netfix的eureka。 下载 点我直达 解压并启动访问 启动： sh startup.sh -m standalone 关闭： sh shutdown.sh 查看端口占用情况： lsof"
tags:
  - "Spring Cloud"
  - "Spring Boot"
  - "分布式架构"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14017230.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　Nacos是阿里巴巴集团开源的一个易于使用的平台，专为动态服务发现，配置和服务管理而设计。可用于替代netfix的eureka。</p>
<h1 style="text-align: center">下载</h1>
<p><a href="https://github.com/alibaba/nacos/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202011/1504448-20201121202750444-219832208.gif" alt="" loading="lazy" /></p>
<h1 style="text-align: center">解压并启动访问</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">启动：
sh startup.sh -m standalone

关闭：
sh shutdown.sh

查看端口占用情况：
lsof -i:8848

杀死进程：
kill -9 pid

访问：
ip:8848/nacos
账户/密码：nacos/nacos</span></pre>
