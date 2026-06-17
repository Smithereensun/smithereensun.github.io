---
title: "Oracle 利用PLSQL一分钟将表结构(PROJ)，从A库移植到B库，一分钟将A库中表数据移植到B库中！！！"
date: 2023-05-31
description: "导读(苦恼) 做多个项目的时候，可能会有这样的需求，需要把A项目中的某些功能移植到B项目上；移植途中，牵扯到顺便把表也要一块移植过去，若表字段较少，那还好，可能耗费10分钟就搞完了，万一碰上几十个字段的，可就麻烦了。简直是费时费劲，于是乎，博主在这里发现了新大陆，利用该方法一分钟创建表结构，一分钟将"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12985414.html"
---

<h1 style="text-align: center">导读(<span style="color: rgba(255, 0, 0, 1)"><strong>苦恼</strong></span>)</h1>
<p>　　<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>做多个项目</strong></span>的时候，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>可能</strong></span>会<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>有这样</strong></span>的<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>需求</strong></span>，需要把<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>A项目</strong></span>中的<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>某些功能移植到B项目</strong></span>上；<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>移植途中</strong></span>，牵扯到顺便把<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>表也要一块移植过去</strong></span>，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>若表字段较少</strong></span>，那还好，可能耗<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>费10分钟就搞完了</strong></span>，万一碰上几十个字段的，可就麻烦了。简直是费时费劲，于是乎，博主在这里发现了新大陆，利用该方法一分钟创建表结构，一分钟将表数据一块移植过去，好啦，言归正传，开干！！！</p>
<h2>快速创建表</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200529085818770-1225849451.gif" alt="" /></p>
<h2>移植数据</h2>
<p>　　通过上一步骤，我们现在<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>已经拿到A库中(proj)表结构</strong></span>，只需要<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>在B库中执行创建表结构SQL语句</strong></span>即可，现在我们去<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>拿A库中(proj表中的数据)</strong></span>，然后<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>去B库中执行插入语句</strong></span>即可。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200529090439197-1464467709.gif" alt="" /></p>
