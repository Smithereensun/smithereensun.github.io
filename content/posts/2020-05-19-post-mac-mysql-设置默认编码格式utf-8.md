---
title: "mac mysql 设置默认编码格式utf-8"
date: 2020-05-19
description: "导读 博主百度一番，发现更改mysql默认编码格式，归结以下几个步骤。 详细步骤 切换当前目录 cd / cd private/etc 新建my.cnf文件 在当前目录下：private/etc sudo vim my.cnf 然后输入当前电脑的登录密码 输入以下内容 注：进入到编辑界面，先按“a”"
tags:
  - "SQL"
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12159850.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　博主百度一番，发现更改mysql默认编码格式，归结以下几个步骤。</p>
<h1 style="text-align: center">详细步骤</h1>
<h2>切换当前目录</h2>
<div class="cnblogs_code">
<pre>cd /<span style="color: rgba(0, 0, 0, 1)">
cd </span><span style="color: rgba(0, 0, 255, 1)">private</span>/etc</pre>
