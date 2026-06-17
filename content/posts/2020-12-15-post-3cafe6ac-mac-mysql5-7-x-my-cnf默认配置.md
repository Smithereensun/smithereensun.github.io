---
title: "Mac mysql5.7.x my.cnf默认配置"
date: 2020-12-15
description: "配置如下 [client] port = 3306 default-character-set=utf8 [mysqld] character_set_server=utf8 datadir=/usr/local/mysql/data log-error = /usr/local/mysql/dat"
tags:
  - "Mac系统"
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14138105.html"
---

<h1 style="text-align: center">配置如下</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">[client]
port = 3306
default-character-set=utf8

[mysqld]
character_set_server=utf8
datadir=/usr/local/mysql/data
log-error = /usr/local/mysql/data/error.log
pid-file = /usr/local/mysql/data/chenyanbindeMacBook-Pro.local.pid
port = 3306
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
symbolic-links=0
max_connections=400
innodb_file_per_table=1
#表名大小写不明感，敏感为
lower_case_table_names=1
#跳过权限表，添加该命令
# skip-grant-tables
# 开启binlog日志
# log-bin=/usr/local/mysql/log_bin_data/mysql-bin
# server-id=1
# 开启慢查询，是否开启
slow_query_log=ON
# 慢查询存放位置
slow_query_log_file=/usr/local/mysql/data/chenyanbindeMacBook-Pro-slow.log
# 慢查询耗时
long_query_time=1

[mysql]
# 允许通过 TAB 键提示
auto-rehash
# 数据库字符集
default-character-set = utf8 </span></pre>
