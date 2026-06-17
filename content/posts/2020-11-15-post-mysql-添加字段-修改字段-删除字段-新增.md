---
title: "Mysql 添加字段、修改字段、删除字段、新增"
date: 2020-11-15
description: "导读 Mysql数据类型，点我直达 创建表 语法： create table 表名( 字段名1 字段类型2 约束条件1 说明1, 字段名2 字段类型2 约束条件2 说明2 ) 约束条件: comment 说明解释 not null 不为空 default 默认值 unsigned 无符号(即正数)"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13408944.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　Mysql数据类型，<a href="https://www.cnblogs.com/chenyanbin/p/13975117.html" target="_blank">点我直达</a></p>
<h2>创建表</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">语法：

create table 表名(
    字段名1  字段类型2  约束条件1 说明1,
    字段名2  字段类型2  约束条件2 说明2
)

约束条件:

comment -------说明解释
not null    -------不为空
default     -------默认值
unsigned  --------无符号(即正数)
auto_increment  ------自增
zerofill         ------自动填充
unique key ------唯一值

-------------------------------------


create table student(
     id  tinyint(5)  zerofill auto_increment not null comment '主键',
     name  varchar(20) default null comment '姓名'
)</span></pre>
