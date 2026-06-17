---
title: "Mac brew install特别慢的问题"
date: 2023-06-26
description: "切换到 Homebrew路径 cd &quot;$(brew --repo)&quot; 查看远程仓库： git remote -v #默认的使用的github。 删除远程： git remote rm origin 添加阿里源 ：git remote add origin https://mirr"
tags:
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/17504648.html"
---

<h1 style="text-align: center">切换到 Homebrew路径</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">cd "$(brew --repo)"
<br>查看远程仓库： git remote -v  #默认的使用的github。
<br>删除远程： git remote rm origin 
<br>添加阿里源 ：git remote add origin https://mirrors.aliyun.com/homebrew/brew.git
<br>切换成阿里源: git remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git</span></pre>
