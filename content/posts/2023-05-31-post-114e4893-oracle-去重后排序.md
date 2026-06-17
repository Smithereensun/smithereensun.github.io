---
title: "Oracle 去重后排序"
date: 2023-05-31
description: "因项目需求，需要将查询结果，去重后，在按照主键(自增列)排序，百度一番，记录下来 DEMO 1 SELECT * FROM (SELECT ROW_NUMBER() OVER(PARTITION BY STATION_NAME ORDER BY ID DESC) RNO,STATION_NAME,I"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11277151.html"
---

<h2>　　因项目需求，需要将查询结果，去重后，在按照主键(自增列)排序，百度一番，记录下来</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190731161631187-1813889080.png" alt="" /></p>
<h3><span style="color: rgba(255, 0, 255, 1)">DEMO</span></h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> SELECT * FROM (SELECT ROW_NUMBER() OVER(PARTITION BY STATION_NAME ORDER BY ID DESC) RNO,STATION_NAME,ID FROM  EMES_MAC) WHERE RNO=<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)"> ORDER BY ID DESC
</span><span style="color: rgba(0, 128, 128, 1)">2</span> 
<span style="color: rgba(0, 128, 128, 1)">3</span> 
<span style="color: rgba(0, 128, 128, 1)">4</span> 格式:SELECT * FROM (SELECT ROW_NUMBER() OVER(PARTITION BY 去重字段 ORDER BY 排序字段 DESC) RNO,去重字段,排序字段 FROM  表名) WHERE RNO=<span style="color: rgba(128, 0, 128, 1)">1</span> ORDER BY 排序字段 DESC</pre>
