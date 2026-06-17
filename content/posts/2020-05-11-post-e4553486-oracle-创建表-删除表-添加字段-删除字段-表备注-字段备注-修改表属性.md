---
title: "oracle 创建表、删除表、添加字段、删除字段、表备注、字段备注、修改表属性"
date: 2020-05-11
description: "1、创建表 create table 表名( classid number(2) primary key, 表字段 数据类型 是否允许为空(not null:不为空/null:允许空) 默认值(default &#39;XXX&#39;) ); -- Create table create tabl"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11206021.html"
---

<h2>1、创建表</h2>
<div class="cnblogs_code">
<pre> <span style="color: rgba(0, 0, 0, 1)">create table 表名(
</span>        classid number(<span style="color: rgba(128, 0, 128, 1)">2</span><span style="color: rgba(0, 0, 0, 1)">) primary key,</span>
             表字段     数据类型    是否允许为空(not <span style="color: rgba(0, 0, 255, 1)">null</span>:不为空/<span style="color: rgba(0, 0, 255, 1)">null</span>:允许空)    默认值(<span style="color: rgba(0, 0, 255, 1)">default</span> <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">XXX</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">)
</span>       );</pre>
