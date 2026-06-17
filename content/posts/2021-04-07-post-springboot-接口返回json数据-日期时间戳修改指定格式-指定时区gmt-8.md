---
title: "SpringBoot 接口返回json数据，日期时间戳修改指定格式，指定时区GMT+8"
date: 2021-04-07
description: "在实体类上添加 @JsonFormat(locale = &quot;zh&quot;, timezone = &quot;GMT+8&quot;, pattern = &quot;yyyy-MM-dd HH:mm:ss&quot;)"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14627076.html"
---

<p>在实体类上添加</p>
<div class="cnblogs_code">
<pre>@JsonFormat(locale = "zh", timezone = "GMT+8", pattern = "yyyy-MM-dd HH:mm:ss")</pre>
