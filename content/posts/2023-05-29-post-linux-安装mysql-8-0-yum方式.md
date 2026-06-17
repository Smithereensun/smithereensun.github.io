---
title: "linux 安装mysql 8.0(yum方式)"
date: 2023-05-29
description: "先卸载MariaDB # 检查有没有 mariadb rpm -qa | grep -i mariadb # 卸载mariadb rpm -e --nodeps mariadb-libs-5.5.52-1.el7.x86_64 检查是否有mysql残留 # 检查mysql是否有残留 rpm -qa"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/mysql8.html"
---

<h1 id="%E4%B8%80%E3%80%81%E5%85%88%E5%8D%B8%E8%BD%BDMariaDB" style="text-align: center">先卸载MariaDB</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)"># 检查有没有 mariadb
rpm -qa | grep -i mariadb

# 卸载mariadb
rpm -e --nodeps mariadb-libs-5.5.52-1.el7.x86_64</span></pre>
