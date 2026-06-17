---
title: "阿里云服务器安装Docker Compose"
date: 2023-05-31
description: "官网地址：https://docs.docker.com/compose/install/ 1、 sudo curl -L &quot;https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname"
tags:
  - "Docker"
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15478169.html"
---

<p>官网地址：<a href="https://docs.docker.com/compose/install/" target="_blank" rel="noopener nofollow">https://docs.docker.com/compose/install/</a></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">1、 sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


2、 sudo chmod +x /usr/local/bin/docker-compose


3、sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

4、 docker-compose --version</span></pre>
