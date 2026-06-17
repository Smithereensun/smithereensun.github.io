---
title: "阿里云服务器安装Docker"
date: 2021-09-18
description: "安装 yum update yum install epel-release -y yum clean all yum list yum install docker-io -y systemctl start docker systemctl start docker #运行Docker守护进程"
tags:
  - "Docker"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14757439.html"
---

<h1 style="text-align: center">安装</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">yum update
yum install epel-release -y
yum clean all
yum list


yum install docker-io -y
systemctl start docker

systemctl start docker     #运行Docker守护进程
systemctl stop docker      #停止Docker守护进程
systemctl restart docker   #重启Docker守护进程</span></pre>
