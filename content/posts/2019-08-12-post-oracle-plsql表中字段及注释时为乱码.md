---
title: "Oracle PLSQL表中字段及注释时为乱码"
date: 2019-08-12
description: "1、添加系统环境变量 2、新建系统变量 3、重启PLSQL 搞定！！！"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11342373.html"
---

<h1 class="title-article">1、添加系统环境变量</h1>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190812202643940-1539393872.png" alt="" /></p>
<h1>2、新建系统变量</h1>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190812202728619-26953396.png" alt="" /></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">变量名:NLS_LANG
变量值:SIMPLIFIED CHINESE_CHINA.ZHS16GBK</span></pre>
