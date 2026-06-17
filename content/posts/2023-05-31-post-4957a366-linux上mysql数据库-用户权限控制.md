---
title: "Linux上Mysql数据库 用户权限控制"
date: 2023-05-31
description: "导读 大家或许都听过程序员删库跑路，可想而知，如果对用户开放太多的数据库操作权限，操作不当，可能会造成意想不到的损失，通过本篇学习，可以熟练掌握mysql用户权限的控制。当然啦，数据被删掉，可以使用技术手段(binlog)恢复回去的，过几天更新~ Linux安装mysql 点我直达 Mysql限制r"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14003024.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　大家或许都听过程序员删库跑路，可想而知，如果对用户开放太多的数据库操作权限，操作不当，可能会造成意想不到的损失，通过本篇学习，可以熟练掌握mysql用户权限的控制。当然啦，数据被删掉，可以使用技术手段(binlog)恢复回去的，过几天更新~</p>
<h1 style="text-align: center">Linux安装mysql</h1>
<p>　　<a href="https://www.cnblogs.com/chenyanbin/p/13144042.html" target="_blank">点我直达</a></p>
<h1 style="text-align: center">Mysql限制root用户ip地址登录</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">修改mysql库里边的user表：
update mysql.user set host='localhost' where user='root';

刷新权限：
flush privileges;</span></pre>
