---
title: "Linux MySQL集群搭建之主从复制"
date: 2023-05-31
description: "前期准备 准备两台Linux，一主，一从，具体Linux安装MySQL操作步骤：点我直达 集群搭建 注意事项 一主可以多从 一从只能一主 Linux之间要能ping通！！ 关闭主从机器的防火墙策略 chkconfig iptables off service iptables stop 主服务器配置"
tags:
  - "Linux"
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13154225.html"
---

<h1 style="text-align: center">前期准备</h1>
<p>　　准备两台Linux，一主，一从，具体Linux安装MySQL操作步骤：<a href="https://www.cnblogs.com/chenyanbin/p/13144042.html" target="_blank">点我直达</a></p>
<h1 style="text-align: center">集群搭建</h1>
<h2>注意事项</h2>
<ul>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>一主可以多从</strong></span></li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>一从只能一主</strong></span></li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>Linux之间要能ping通！！</strong></span></li>
</ul>
<h2>关闭主从机器的防火墙策略</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">chkconfig iptables off

service iptables stop</span></pre>
