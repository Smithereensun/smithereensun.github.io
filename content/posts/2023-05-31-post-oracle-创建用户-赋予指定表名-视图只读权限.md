---
title: "Oracle 创建用户，赋予指定表名/视图只读权限"
date: 2023-05-31
description: "步骤指南 创建用户 格式：create user TEST identified by 123456; 语法：create user 用户名 identified by 密码; 注：密码不行的话，前后加(单引号):&#39; create user TEST identified by &#39;1"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12027897.html"
---

<h1 style="text-align: center">步骤指南</h1>
<h2>创建用户</h2>
<div class="cnblogs_code">
<pre>格式：<span style="color: rgba(0, 0, 255, 1)">create</span> <span style="color: rgba(255, 0, 255, 1)">user</span>  TEST identified <span style="color: rgba(0, 0, 255, 1)">by</span> <span style="color: rgba(128, 0, 0, 1); font-weight: bold">123456</span><span style="color: rgba(0, 0, 0, 1)">;

语法：</span><span style="color: rgba(0, 0, 255, 1)">create</span> <span style="color: rgba(255, 0, 255, 1)">user</span>  用户名 identified <span style="color: rgba(0, 0, 255, 1)">by</span><span style="color: rgba(0, 0, 0, 1)"> 密码;

注：密码不行的话，前后加(单引号):</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">
create user  TEST identified by </span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1); font-weight: bold">123456</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">;</span></pre>
