---
title: "PLSQL 无法查询带中文的WHERE条件"
date: 2019-06-26
description: "今天遇到一个坑爹的问题，plsql无法查询带where条件的语句，是因为plsql中Oracle的客户端字符集和服务器上的不一样造成的，需要新增系统环境变量，特意记录下解决办法。 第一步：查询服务器上Oracle使用的字符集 第二步：设置环境变量(我的电脑--&gt;属性--&gt;更改设置--&g"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10929003.html"
---

<h3>　　今天遇到一个坑爹的问题，plsql无法查询带where条件的语句，<span style="color: rgba(255, 0, 0, 1)"><strong>是因为plsql中Oracle的客户端字符集和服务器上的不一样造成的</strong></span>，需要新增系统环境变量，特意记录下解决办法。</h3>
<h3>第一步：查询服务器上Oracle使用的字符集</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">select</span> <span style="color: rgba(128, 128, 128, 1)">*</span> <span style="color: rgba(0, 0, 255, 1)">from</span> v$nls_parameters <span style="color: rgba(0, 0, 255, 1)">where</span> parameter <span style="color: rgba(128, 128, 128, 1)">like</span> <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">NLS_CH%</span><span style="color: rgba(255, 0, 0, 1)">'</span>;</pre>
