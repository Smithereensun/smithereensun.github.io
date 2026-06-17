---
title: "Mybatis模糊查询"
date: 2020-07-08
description: "VideoMapper.java /** * 根据评分和标题模糊查询 * @param point * @param title * @return */ List&lt;Video&gt; selectByPointAndTitleLike(@Param(&quot;point&quot;) do"
tags:
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13269479.html"
---

<p>VideoMapper.java</p>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 根据评分和标题模糊查询
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> point
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> title
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    List</span>&lt;Video&gt; selectByPointAndTitleLike(@Param("point") <span style="color: rgba(0, 0, 255, 1)">double</span> point,@Param("title") String title);</pre>
