---
title: "Centos 7 永久关闭防火墙"
date: 2020-10-11
description: "查看防火墙状态 systemctl status firewalld 出现：Active: inactive (dead)，代表防火墙已关闭 临时关闭防火墙 重启后，防火墙会重新开启 systemctl stop firewalld.service 永久关闭防火墙 systemctl disable"
tags:
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13799842.html"
---

<h1>查看防火墙状态</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">systemctl status firewalld

出现：Active: inactive (dead)，代表防火墙已关闭</span></pre>
