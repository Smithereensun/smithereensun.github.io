---
title: "SpringBoot 整合EasyExcel 获取动态Excel列名"
date: 2023-05-31
description: "导读 最近负责消息网关，里面有个短信模板导入功能，因为不同模板编号对应不同参数，导入后的数据定时发送，涉及到Excel中列名不固定问题，于是想根据列名+值，组合成一个大JSON，具体代码如下。 引入依赖 &lt;dependency&gt; &lt;groupId&gt;com.alibaba&lt"
tags:
  - "Spring Boot"
  - "Easy Excel"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14715074.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　最近负责消息网关，里面有个短信模板导入功能，因为不同模板编号对应不同参数，导入后的数据定时发送，涉及到Excel中列名不固定问题，于是想根据列名+值，组合成一个大JSON，具体代码如下。</p>
<h2>引入依赖</h2>
<div class="cnblogs_code">
<pre>        &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
            &lt;artifactId&gt;easyexcel&lt;/artifactId&gt;
            &lt;version&gt;2.2.6&lt;/version&gt;
        &lt;/dependency&gt;
        &lt;!--fastjson--&gt;
        &lt;dependency&gt;
            &lt;groupId&gt;com.alibaba&lt;/groupId&gt;
            &lt;artifactId&gt;fastjson&lt;/artifactId&gt;
            &lt;version&gt;1.2.76&lt;/version&gt;
        &lt;/dependency&gt;</pre>
