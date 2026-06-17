---
title: "Mybatis 懒加载"
date: 2020-07-13
description: "什么是懒加载 按需加载，先从单表查询，需要时再从关联表去关联查询，能大大提高数据库性能，并不是所有场景下使用懒加载都能提高性能 Mybatis懒加载：resultMap里面的association、collection都有延迟加载功能 全局配置文件 &lt;!--全局配置--&gt; &lt;set"
tags:
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13296396.html"
---

<h1 style="text-align: center">什么是懒加载</h1>
<p>　　按需加载，先从单表查询，需要时再从关联表去关联查询，能大大提高数据库性能，并不是所有场景下使用懒加载都能提高性能</p>
<p>Mybatis懒加载：resultMap里面的association、collection都有延迟加载功能</p>
<p>全局配置文件</p>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">全局配置</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">settings</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">延迟加载总开关</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">setting </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="lazyLoadingEnabled"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="true"</span><span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">将aggressiveLazyLoading设置为false表示按需加载，默认为true</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">setting </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="aggressiveLazyLoading"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="false"</span><span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">settings</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
