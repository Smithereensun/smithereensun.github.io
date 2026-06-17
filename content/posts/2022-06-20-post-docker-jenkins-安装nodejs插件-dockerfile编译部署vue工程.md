---
title: "Docker Jenkins 安装NodeJS插件，dockerfile编译部署vue工程"
date: 2022-06-20
description: "Jenkins下载nodeJS插件 下载插件 全局配置 下载node # 进入docker容器镜像 docker exec -it 480061b40bd7 /bin/bash #官网地址：https://nodejs.org/dist/ #下载 wget https://nodejs.org/di"
tags:
  - "自动化部署"
  - "Docker"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/16392960.html"
---

<h1 style="text-align: center">Jenkins下载nodeJS插件</h1>
<h2>下载插件</h2>
<p><img src="https://img2022.cnblogs.com/blog/1504448/202206/1504448-20220620134349081-696571031.png" alt="" loading="lazy" /></p>
<h2>全局配置</h2>
<p><img src="https://img2022.cnblogs.com/blog/1504448/202206/1504448-20220620134257716-654087610.png" alt="" loading="lazy" /></p>
<h1 style="text-align: center">下载node</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)"># 进入docker容器镜像
docker exec -it 480061b40bd7 /bin/bash

#官网地址：https://nodejs.org/dist/
#下载
wget https://nodejs.org/dist/v18.4.0/node-v18.4.0-linux-x64.tar.gz

#解压到指定目录
tar zxvf node-v18.4.0-linux-x64.tar.gz -C /usr/local/

# 重命名
cd /usr/local
mv node-v18.4.0-linux-x64/ node18</span></pre>
