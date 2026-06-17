---
title: "C# List集合求：差集、并集、交集"
date: 2019-09-21
description: "1、差集 2、并集 3、交集"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11563842.html"
---

<h1>1、差集</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">需引入命名空间:using System.Linq;</span>
<span style="color: rgba(0, 128, 128, 1)">2</span> List&lt;<span style="color: rgba(0, 0, 255, 1)">int</span>&gt; listA = <span style="color: rgba(0, 0, 255, 1)">new</span> List&lt;<span style="color: rgba(0, 0, 255, 1)">int</span>&gt;<span style="color: rgba(0, 0, 0, 1)">();
</span><span style="color: rgba(0, 128, 128, 1)">3</span> List&lt;<span style="color: rgba(0, 0, 255, 1)">int</span>&gt; listB = <span style="color: rgba(0, 0, 255, 1)">new</span> List&lt;<span style="color: rgba(0, 0, 255, 1)">int</span>&gt;<span style="color: rgba(0, 0, 0, 1)">();
</span><span style="color: rgba(0, 128, 128, 1)">4</span> List&lt;<span style="color: rgba(0, 0, 255, 1)">int</span>&gt; listC = listA.Except(listB).ToList();</pre>
