---
title: "oracle 利用序列与触发器实现列自增"
date: 2020-05-11
description: "实现步骤：先创建序列，后创建触发器 1、创建序列 create sequence 序列名 increment by 1 start with 1 maxvalue 999999999; 2、创建触发器 create or replace trigger 触发器名 before insert on 表"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10856975.html"
---

<p>实现步骤：先创建序列，后创建触发器</p>
<h2>1、创建序列</h2>
<div class="cnblogs_code">
<pre> <span style="color: rgba(0, 0, 255, 1)">create</span><span style="color: rgba(0, 0, 0, 1)"> sequence 序列名
 increment </span><span style="color: rgba(0, 0, 255, 1)">by</span> <span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span><span style="color: rgba(0, 0, 0, 1)">
 start </span><span style="color: rgba(0, 0, 255, 1)">with</span> <span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span><span style="color: rgba(0, 0, 0, 1)">
 maxvalue </span><span style="color: rgba(128, 0, 0, 1); font-weight: bold">999999999</span>;</pre>
