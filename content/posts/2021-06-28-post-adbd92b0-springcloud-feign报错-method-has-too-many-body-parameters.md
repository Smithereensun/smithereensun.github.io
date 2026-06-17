---
title: "SpringCloud Feign报错：Method has too many Body parameters"
date: 2021-06-28
description: "feign多参数问题 GET请求 错误写法 @RequestMapping(value=&quot;/test&quot;, method=RequestMethod.GET) void test(final String name, final int age); 正确写法 @RequestMap"
tags:
  - "Spring Cloud"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14944219.html"
---

<h1 id="h1_0" style="text-align: center">feign多参数问题</h1>
<h2>GET请求</h2>
<h3>错误写法</h3>
<div class="cnblogs_code">
<pre>@RequestMapping(value="/test", method=<span style="color: rgba(0, 0, 0, 1)">RequestMethod.GET)  
void test(</span><span style="color: rgba(0, 0, 255, 1)">final</span> String name,  <span style="color: rgba(0, 0, 255, 1)">final</span> <span style="color: rgba(0, 0, 255, 1)">int</span> age);  </pre>
