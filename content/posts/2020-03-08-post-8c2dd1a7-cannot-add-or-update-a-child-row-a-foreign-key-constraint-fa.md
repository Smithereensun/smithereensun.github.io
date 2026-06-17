---
title: "Cannot add or update a child row: a foreign key constraint fails"
date: 2020-03-08
description: "在使用Django添加用户时出现报错： 1 django.db.utils.IntegrityError: (1452, &#39;Cannot add or update a child row: a foreign key constraint fai 2 ls (`cms`.`app01_bo"
tags:
  - "Django"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10633297.html"
---

<p>在使用Django添加用户时出现报错：</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 0, 0, 1)">django.db.utils.IntegrityError: (1452, 'Cannot add or update a child row: a foreign key constraint fai
</span><span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(0, 0, 0, 1)">ls (`cms`.`app01_book_author`, CONSTRAINT `app01_book_author_book_id_df0ca405_fk_app01_book_id` FOREIG
</span><span style="color: rgba(0, 128, 128, 1)">3</span> <span style="color: rgba(0, 0, 0, 1)">N KEY (`book_id`) REFERENCES `app01_book` (`id`))')
</span><span style="color: rgba(0, 128, 128, 1)">4</span> [31/Mar/2019 21:20:45] "GET /addbook/ HTTP/1.1" 500 216210</pre>
