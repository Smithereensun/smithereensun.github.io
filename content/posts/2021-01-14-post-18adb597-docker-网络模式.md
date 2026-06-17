---
title: "Docker 网络模式"
date: 2021-01-14
description: "三种网络模式 bridge：桥接模式 host：主机模式 none：无网络模式 查看网络模式 docker network ls 桥接模式 桥接模式是docker 的默认网络设置，当Docker服务启动时，会在主机上创建一个名为docker0的虚拟网桥，并 选择一个和宿主机不同的IP地址和子网分配给"
tags:
  - "Docker"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14279692.html"
---

<h1 style="text-align: center">三种网络模式</h1>
<ul>
<li><strong><span style="color: rgba(255, 0, 0, 1)">bridge</span></strong>：桥接模式</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>host</strong></span>：主机模式</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>none</strong></span>：无网络模式</li>
</ul>
<h2>查看网络模式</h2>
<div class="cnblogs_code">
<pre>docker network ls</pre>
