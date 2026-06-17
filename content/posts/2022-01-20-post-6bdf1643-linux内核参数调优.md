---
title: "Linux内核参数调优"
date: 2022-01-20
description: "(单个进程)查看最大文件句柄数 调参 vi /etc/security/limits.conf # End of file root soft nofile 1000000 root hard nofile 1000000 * soft nofile 1000000 * hard nofile 10"
tags:
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15827980.html"
---

<h1 style="text-align: center">(单个进程)查看最大文件句柄数</h1>
<p><img src="https://img2022.cnblogs.com/blog/1504448/202201/1504448-20220120201620108-1903706546.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h2>调参</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">vi /etc/security/limits.conf





# End of file
root soft nofile 1000000
root hard nofile 1000000
* soft nofile 1000000
* hard nofile 1000000</span></pre>
