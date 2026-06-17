---
title: "SpringBoot整合easyexcel，导入参数校验，批注导出"
date: 2022-02-16
description: "思路 导入时，数据全部读取完，进行参数校验 如果参数校验失败后，将Excel导入的数据和校验错误信息，存到Redis中，最后将数据导出 添加依赖 &lt;dependency&gt; &lt;groupId&gt;com.alibaba&lt;/groupId&gt; &lt;artifactId&"
tags:
  - "Spring Boot"
  - "Easy Excel"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14366596.html"
---

<h1 style="text-align: center">思路</h1>
<ul>
<li>导入时，数据全部读取完，进行参数校验</li>
<li>如果参数校验失败后，将Excel导入的数据和校验错误信息，存到Redis中，最后将数据导出</li>
</ul>
<h1 style="text-align: center">添加依赖</h1>
<div class="cnblogs_code">
<pre>        &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
            &lt;artifactId&gt;easyexcel&lt;/artifactId&gt;
            &lt;version&gt;2.2.6&lt;/version&gt;
        &lt;/dependency&gt;
         &lt;dependency&gt;
            &lt;groupId&gt;com.google.code.gson&lt;/groupId&gt;
            &lt;artifactId&gt;gson&lt;/artifactId&gt;
            &lt;version&gt;2.8.6&lt;/version&gt;
         &lt;/dependency&gt;</pre>
