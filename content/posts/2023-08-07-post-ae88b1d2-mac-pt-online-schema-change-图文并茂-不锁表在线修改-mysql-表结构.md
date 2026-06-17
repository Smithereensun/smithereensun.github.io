---
title: "Mac pt-online-schema-change 图文并茂、不锁表在线修改 MySQL 表结构"
date: 2023-08-07
description: "导读 percona-toolkit 源自 Maatkit 和 Aspersa 工具，这两个工具是管理 MySQL 的最有名的工具，但 Maatkit 已经不维护了，全部归并到 percona-toolkit。Percona Toolkit 是一组高级的命令行工具，用来管理 MySQL 和系统任务，"
tags:
  - "SQL"
  - "Mac系统"
  - "pt-online-schema-change"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/17505226.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　percona-toolkit 源自 Maatkit 和 Aspersa 工具，这两个工具是管理 MySQL 的最有名的工具，但 Maatkit 已经不维护了，全部归并到 percona-toolkit。Percona Toolkit 是一组高级的命令行工具，用来管理 MySQL 和系统任务，主要包括：</p>
<ul>
<li>验证主节点和复制数据的一致性</li>
<li>有效的对记录行进行归档</li>
<li>找出重复的索引</li>
<li>总结 MySQL 服务器</li>
<li>从日志和 tcpdump 中分析查询</li>
<li>问题发生时收集重要的系统信息</li>
<li>在线修改表结构</li>
</ul>
<h1 style="text-align: center">工作原理</h1>
<ul>
<li>如果存在外键，根据&nbsp;<code class="language-plaintext highlighter-rouge">alter-foreign-keys-method</code>&nbsp;参数的值，检测外键相关的表，做相应设置的处理。没有使用 alter-foreign-keys-method 指定特定的值，该工具不予执行</li>
<li>创建一个新的空表，其命名规则是：下划线 + 原表名 +<code class="language-plaintext highlighter-rouge">_new</code></li>
<li>根据 alter 语句，更新新表的表结构；</li>
<li>创建触发器，用于记录从拷贝数据开始之后，对源数据表继续进行数据修改的操作记录下来，用于数据拷贝结束后，执行这些操作，保证数据不会丢失。如果表中已经定义了触发器这个工具就不能工作了。</li>
<li>拷贝数据，从源数据表中拷贝数据到新表中。</li>
<li>修改外键相关的子表，根据修改后的数据，修改外键关联的子表。</li>
<li>rename 源数据表为 old 表，把新表 rename 为源表名，其通过一个 RENAME TABLE 同时处理两个表，实现原子操作。（RENAME TABLE dbteamdb.user TO dbteamdb._user_old, dbteamdb._user_new TO dbteamdb.user）</li>
<li>将 old 表删除、删除触发器。</li>
</ul>
<h1 style="text-align: center">mac安装</h1>
<div class="cnblogs_code">
<pre>brew install percona-toolkit</pre>
