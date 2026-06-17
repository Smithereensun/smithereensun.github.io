---
title: "attempted to return null from a method with a primitive return type (int)."
date: 2023-05-31
description: "java接口文件 package com.cyb.ms.mapper; import org.apache.ibatis.annotations.Param; public interface AccountMapper { void update(@Param(&quot;name&quot;)"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11927686.html"
---

<h1 style="text-align: center">java接口文件</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb.ms.mapper;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.apache.ibatis.annotations.Param;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">interface</span><span style="color: rgba(0, 0, 0, 1)"> AccountMapper {
    </span><span style="color: rgba(0, 0, 255, 1)">void</span> update(@Param("name") String name, @Param("money") <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> money);

    </span><span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> queryMoney(String name);
}</span></pre>
