---
title: "SqlServer 复制表结构及数据"
date: 2019-06-26
description: "SqlServer中： 目标表存在： INSERT INTO 目标表 SELECT * FROM 原表; 目标表不存在：SELECT * INTO 目标表 FROM 原表; Oracle中： 目标表存在：INSERT INTO 目标表 SELECT * FROM 原表; 目标表不存在：CREATE"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10503914.html"
---

<h1>SqlServer中：</h1>
<p>　　目标表存在： INSERT INTO 目标表 SELECT * FROM 原表;</p>
<p>　　目标表不存在：SELECT * INTO 目标表 FROM 原表;</p>
<h1>Oracle中：</h1>
<p>　　目标表存在：INSERT INTO 目标表 SELECT * FROM 原表;</p>
<p>　　目标表不存在：CREATE TABLE 目标表 AS SELECT * FROM 原表;</p>
