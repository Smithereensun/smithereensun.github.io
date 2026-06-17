---
title: "Mybatis下划线自动映射驼峰字段"
date: 2020-07-09
description: "mybatis-config.xml &lt;!--下划线自动映射驼峰字段--&gt; &lt;settings&gt; &lt;setting name=&quot;mapUnderscoreToCamelCase&quot; value=&quot;true&quot;/&gt; &lt;/se"
tags:
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13273028.html"
---

<p>mybatis-config.xml</p>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">下划线自动映射驼峰字段</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">settings</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">setting </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="mapUnderscoreToCamelCase"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="true"</span><span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">settings</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
