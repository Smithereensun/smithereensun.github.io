---
title: "Docker 实战"
date: 2023-05-31
description: "Docker入门 概述 Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。 容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。 Docker 从 17"
tags:
  - "Docker"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/docker.html"
---

<h1 style="text-align: center">Docker入门</h1>
<h2>概述</h2>
<p>　　Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。</p>
<p>　　容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。</p>
<p>　　Docker 从 17.03 版本之后分为 <span style="color: rgba(255, 0, 0, 1)"><strong>CE</strong></span>（Community Edition: 社区版） 和 <span style="color: rgba(255, 0, 0, 1)"><strong>EE</strong></span>（Enterprise Edition: 企业版），我们用社区版就可以了。</p>
<h2>注意事项</h2>
<ul>
<li>Linux内核版本必须大于：<span style="color: rgba(255, 0, 0, 1)"><strong>3.8.+</strong></span></li>
<li>查看内核版本：uname -r</li>
</ul>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202101/1504448-20210109114503119-841827368.gif" alt="" loading="lazy" /></p>
<h2>Docker下载及安装</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">1、关闭防火墙
systemctl stop firewalld.service


2、修改为SELINUX=disabled
vim /etc/selinux/config
SELINUX=disabled


3、安装wget
 yum -y install wget



4、查看docker版本
yum list|grep docker

5、安装docker
yum install -y docker.x86_64


6、安装docker ce社区版
cd /etc/yum.repos.d/
wget http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo


7、下载社区版本
yum -y install docker-ce-cli.x86_64

8、设置开机启动
systemctl enable docker

9、更新xfsprogs<br>yum update xfsprogs<br><br>10、启动docker服务<br>systemctl start docker<br><br>11、查看docker版本<br>docker version<br><br>12、查看docker详细信息<br>docker info</span></pre>
