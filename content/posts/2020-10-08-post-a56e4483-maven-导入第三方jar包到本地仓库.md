---
title: "maven 导入第三方jar包到本地仓库"
date: 2020-10-08
description: "第一步 进入cmd命令界面 第二步 输入指令如下，然后回车 mvn install:install-file -Dfile=xxxxxx -DgroupId=com.alibaba -DartifactId=fastjson -Dversion=1.0 -Dpackaging=jar -Dgener"
tags:
  - "Maven"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13782024.html"
---

<h1 style="text-align: center">第一步</h1>
<p>进入cmd命令界面</p>
<h1 style="text-align: center">第二步</h1>
<p>输入指令如下，然后回车</p>
<div class="cnblogs_code">
<pre>mvn install:install-file -Dfile=xxxxxx -DgroupId=com.alibaba -DartifactId=fastjson -Dversion=1.0 -Dpackaging=jar -DgeneratePom=true -DcreateChecksum=true</pre>
