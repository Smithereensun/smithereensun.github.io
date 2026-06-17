---
title: "Java FastJson解析json字符串"
date: 2020-07-29
description: "json转map Map&lt;String, 实体类&gt; titleMap=JSON.parseObject(JSON字符串, new TypeReference&lt;HashMap&lt;String, 实体类&gt;&gt;() {}); json转对象 Student student"
tags:
  - "JSON"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13398632.html"
---

<h1>json转map</h1>
<div class="cnblogs_code">
<pre>Map&lt;String, 实体类&gt; titleMap=JSON.parseObject(JSON字符串, <span style="color: rgba(0, 0, 255, 1)">new</span> TypeReference&lt;HashMap&lt;String, 实体类&gt;&gt;() {});</pre>
