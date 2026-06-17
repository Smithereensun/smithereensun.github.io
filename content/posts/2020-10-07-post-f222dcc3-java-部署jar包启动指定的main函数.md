---
title: "java 部署jar包启动指定的main函数"
date: 2020-10-07
description: "方法一 语法：java -cp test.jar com.hk.app.Application 解释：java -cp jar包 启动包路径 注：这种方法我是没启动成功，使用的是第二种 方法二 修改pom.xml &lt;build&gt; &lt;plugins&gt; &lt;plugin&gt"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13780007.html"
---

<h1>方法一</h1>
<div class="cnblogs_code">
<pre>语法：java -<span style="color: rgba(0, 0, 0, 1)">cp test.jar com.hk.app.Application

解释：java </span>-cp jar包 启动包路径</pre>
