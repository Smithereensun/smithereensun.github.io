---
title: "mysql 表被锁了怎么办"
date: 2021-11-22
description: "select * from information_schema.innodb_trx # 干掉 trx_requested_lock_id kill 101"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15589478.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">select * from information_schema.innodb_trx

# 干掉 trx_requested_lock_id
kill 101</span></pre>
