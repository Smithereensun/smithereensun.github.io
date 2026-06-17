---
title: "nginx 反向代理服务器端口转发问题"
date: 2023-05-23
description: "导读 先介绍一下项目背景，公司里有个外包Saas项目，这里假设为A项目(前后端不分离)；项目架构大概如下；但是项目部署到生产环境时，那台服务器80端口被其他应用占用了(我尼玛...)，nginx监听端口那边只能监听其他端口了，比如监听：18000，通过nginx反向代理将18000端口转发到9001"
tags:
  - "Nginx"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/17401237.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　先介绍一下项目背景，公司里有个外包Saas项目，这里假设为A项目(<strong>前后端不分离</strong>)；项目架构大概如下；但是项目部署到生产环境时，那台服务器80端口被其他应用占用了(我尼玛...)，nginx监听端口那边只能监听其他端口了，比如监听：18000，通过nginx反向代理将18000端口转发到9001上，转发到9001上时，由于后端校验了是否登录，直接将请求跳转至登录页比如：47.55.x.x，但是这台服务器上的80端口被其他web应用占用了，导致找不到页面报404。。。</p>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202305/1504448-20230515104308419-511040863.png" alt="" loading="lazy" /></p>
<h1 style="text-align: center">解决办法</h1>
<p>　　需要在nginx配置文件中，指定：<strong><span style="color: rgba(255, 0, 0, 1)">proxy_set_header Host $host:端口号</span></strong></p>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202305/1504448-20230515105502979-2012538948.png" alt="" loading="lazy" /></p>
