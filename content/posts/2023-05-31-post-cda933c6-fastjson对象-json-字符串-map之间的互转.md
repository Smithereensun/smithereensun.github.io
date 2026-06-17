---
title: "fastjson对象，JSON，字符串，map之间的互转"
date: 2023-05-31
description: "对象与字符串之间的互转 将对象转换成为字符串 String str = JSON.toJSONString(infoDo); 字符串转换成为对象 InfoDo infoDo = JSON.parseObject(strInfoDo, InfoDo.class); 字符串转对象 List&lt;Nba"
tags:
  - "JSON"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13476152.html"
---

<h1>对象与字符串之间的互转</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">将对象转换成为字符串
String str = JSON.toJSONString(infoDo);
字符串转换成为对象
InfoDo infoDo = JSON.parseObject(strInfoDo, InfoDo.class);</span></pre>
