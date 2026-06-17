---
title: "sheel 脚本批量插数据"
date: 2021-11-02
description: "#!/bin/bash i=1 while [ $i -le 100000000 ] do mysql -uroot -proot -h127.0.0.1 test -e &quot;insert into student_test (name,createTime) values (&#39;st"
tags:
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15497305.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">#!/bin/bash
i=1
while [ $i -le 100000000 ]
do
    mysql -uroot -proot -h127.0.0.1 test -e "insert into student_test (name,createTime) values ('student$i',NOW());"
    i=$(($i+1))
done</span></pre>
