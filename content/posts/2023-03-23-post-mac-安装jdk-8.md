---
title: "Mac 安装jdk 8"
date: 2023-03-23
description: "下载jdk 链接一（网速慢，不推荐）：https://www.oracle.com/cn/java/technologies/downloads/ 链接二（国内镜像，速度快）：http://www.codebaoku.com/jdk/jdk-index.html 注意这里下载：jdk-8u351-m"
tags:
  - "JAVA"
  - "Mac系统"
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/jdk_8.html"
---

<h1 style="text-align: center">下载jdk</h1>
<p>链接一（网速慢，不推荐）：https://www.oracle.com/cn/java/technologies/downloads/</p>
<p>链接二（国内镜像，速度快）：http://www.codebaoku.com/jdk/jdk-index.html</p>
<p>　　注意这里下载：jdk-8u351-macosx-x64.dmg</p>
<h1 style="text-align: center">安装</h1>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202303/1504448-20230323110241446-1763962344.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1 style="text-align: center">设置环境变量</h1>
<p>查看jdk安装目录：<span style="color: rgba(255, 0, 0, 1)"><strong>/usr/libexec/java_home -V</strong></span></p>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202303/1504448-20230323110507824-1925423640.png" alt="" loading="lazy" /></p>
<p>设置环境变量</p>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202303/1504448-20230323110437273-1931162056.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)"># 编辑
sudo vi ~/.bash_profile

# 添加环境变量
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_351.jdk/Contents/Home

# 环境变量生效
source ~/.bash_profile</span></pre>
