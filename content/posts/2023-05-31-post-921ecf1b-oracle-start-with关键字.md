---
title: "Oracle Start With关键字"
date: 2023-05-31
description: "Start With (树查询) 问题描述: 在数据库中, 有一种比较常见得 设计模式, 层级结构 设计模式, 具体到 Oracle table中, 字段特点如下: ID, DSC, PID; 三个字段, 分别表示 当前标识的 ID(主键), DSC 当前标识的描述, PID 其父级ID, 比较典型"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12320742.html"
---

<h1 id="start-with-树查询" style="text-align: center"><span id="0001">Start With (树查询)</span></h1>
<h2>问题描述:</h2>
<p>在数据库中, 有一种比较常见得 设计模式, 层级结构 设计模式, 具体到 Oracle table中, 字段特点如下:</p>
<p>ID, DSC, PID;</p>
<p>三个字段, 分别表示 当前标识的 ID(主键), DSC 当前标识的描述, PID 其父级ID, 比较典型的例子 是 国家, 省, 市 这种层级结构;</p>
<p><span style="font-family: 微软雅黑">省份归属于国家, 因此 PID 为 国家的 ID, 以此类推;</span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">create</span> <span style="color: rgba(0, 0, 255, 1)">table</span><span style="color: rgba(0, 0, 0, 1)"> DEMO (
    ID </span><span style="color: rgba(0, 0, 255, 1)">varchar2</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">10</span>) <span style="color: rgba(0, 0, 255, 1)">primary</span> <span style="color: rgba(0, 0, 255, 1)">key</span><span style="color: rgba(0, 0, 0, 1)">,
    DSC </span><span style="color: rgba(0, 0, 255, 1)">varchar2</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">100</span><span style="color: rgba(0, 0, 0, 1)">),
    PID </span><span style="color: rgba(0, 0, 255, 1)">varchar2</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">10</span><span style="color: rgba(0, 0, 0, 1)">)
)
</span><span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">插入几条数据</span>

<span style="color: rgba(0, 0, 255, 1)">Insert</span> <span style="color: rgba(0, 0, 255, 1)">Into</span> DEMO <span style="color: rgba(0, 0, 255, 1)">values</span> (<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00001</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">中国</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">-1</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 0, 255, 1)">Insert</span> <span style="color: rgba(0, 0, 255, 1)">Into</span> DEMO <span style="color: rgba(0, 0, 255, 1)">values</span> (<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00011</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">陕西</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00001</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 0, 255, 1)">Insert</span> <span style="color: rgba(0, 0, 255, 1)">Into</span> DEMO <span style="color: rgba(0, 0, 255, 1)">values</span> (<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00012</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">贵州</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00001</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 0, 255, 1)">Insert</span> <span style="color: rgba(0, 0, 255, 1)">Into</span> DEMO <span style="color: rgba(0, 0, 255, 1)">values</span> (<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00013</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">河南</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00001</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 0, 255, 1)">Insert</span> <span style="color: rgba(0, 0, 255, 1)">Into</span> DEMO <span style="color: rgba(0, 0, 255, 1)">values</span> (<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00111</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">西安</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00011</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 0, 255, 1)">Insert</span> <span style="color: rgba(0, 0, 255, 1)">Into</span> DEMO <span style="color: rgba(0, 0, 255, 1)">values</span> (<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00112</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">咸阳</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00011</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 0, 255, 1)">Insert</span> <span style="color: rgba(0, 0, 255, 1)">Into</span> DEMO <span style="color: rgba(0, 0, 255, 1)">values</span> (<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00113</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">延安</span><span style="color: rgba(255, 0, 0, 1)">'</span>, <span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">00011</span><span style="color: rgba(255, 0, 0, 1)">'</span>);</pre>
