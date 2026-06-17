---
title: "Mac 每次都要执行source ~/.bash_profile 配置的环境变量才生效"
date: 2020-04-21
description: "自己在 ~/.bash_profile 中配置环境变量, 可是每次重启终端后配置的不生效.需要重新执行 : $source ~/.bash_profile 发现zsh加载的是 ~/.zshrc文件，而 ‘.zshrc’ 文件中并没有定义任务环境变量。 解决办法 编辑~/.zshrc文件并在最后增加一"
tags:
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12748597.html"
---

<p>自己在 ~/.bash_profile 中配置环境变量, 可是每次重启终端后配置的不生效.需要重新执行 : $source ~/.bash_profile</p>
<p>发现zsh加载的是 ~/.zshrc文件，而 ‘.zshrc’ 文件中并没有定义任务环境变量。</p>
<p>解决办法</p>
<p>编辑~/.zshrc文件并在最后增加一行： <br>source ~/.bash_profile<br><img src="https://img2020.cnblogs.com/blog/1504448/202004/1504448-20200421224629701-1439620409.png" alt="" /></p>
<p>&nbsp;</p>
<p>　　搞定~</p>
