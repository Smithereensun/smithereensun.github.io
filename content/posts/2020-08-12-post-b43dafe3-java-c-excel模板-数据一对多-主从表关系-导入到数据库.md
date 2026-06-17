---
title: "Java 、C# Excel模板，数据一对多，主从表关系，导入到数据库"
date: 2020-08-12
description: "思路 单表导入的比较容易，但是有的时候，可能会出现，一对多数据导入的，这个情况怎么办呢？先理解上面的图，后台获取数据的时候，除了“风险防控措施”外，其他字段先分组，“黄色背景”、“蓝色背景”、“绿色背景”，此时，一条“黄色背景”对应3条防控措施，一条“蓝色背景”对应1条防控措施，一条“绿色背景”对应"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13489363.html"
---

<h1>思路</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200812104512010-1791052673.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>　　单表导入的比较容易，但是有的时候，可能会出现，一对多数据导入的，这个情况怎么办呢？<span style="color: rgba(255, 0, 0, 1)"><strong>先理解上面的图</strong></span>，后台获取数据的时候，<span style="color: rgba(255, 0, 0, 1)"><strong>除</strong></span>了“<span style="color: rgba(255, 0, 0, 1)"><strong>风险防控措施</strong></span>”<span style="color: rgba(255, 0, 0, 1)"><strong>外</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>其他字段先分组</strong></span>，“<span style="color: rgba(255, 0, 0, 1)"><strong>黄色背景</strong></span>”、“<span style="color: rgba(255, 0, 0, 1)"><strong>蓝色背景</strong></span>”、“<span style="color: rgba(255, 0, 0, 1)"><strong>绿色背景</strong></span>”，此时，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>一条“<span style="color: rgba(255, 255, 0, 1)">黄色背景</span>”对应<span style="color: rgba(255, 255, 0, 1)">3条防控措施</span>，一条“<span style="color: rgba(255, 255, 0, 1)">蓝色背景</span>”对应<span style="color: rgba(255, 255, 0, 1)">1条防控措施</span>，一条“<span style="color: rgba(255, 255, 0, 1)">绿色背景</span>”对应<span style="color: rgba(255, 255, 0, 1)">1条防控措施</span></strong></span>。</p>
