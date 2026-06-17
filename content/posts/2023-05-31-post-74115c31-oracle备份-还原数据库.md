---
title: "Oracle备份、还原数据库"
date: 2023-05-31
description: "备份数据库 创建备份目录（用sys账号），若已创建备份目录，此步可忽略 create directory db_bak as &#39;D:\\ ECIMS_DB&#39; --查看创建的目录 select * from dba_directories --删除已创建的目录 drop director"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11812970.html"
---

<h1 style="text-align: center" align="left">备份数据库</h1>
<h2 align="left">创建备份目录（用sys账号），若已创建备份目录，此步可忽略</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">create</span> directory db_bak <span style="color: rgba(0, 0, 255, 1)">as</span> <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">D:\ ECIMS_DB</span><span style="color: rgba(255, 0, 0, 1)">'</span></pre>
