---
title: "MySQL 性能优化之慢查询"
date: 2023-05-31
description: "性能优化的思路 首先需要使用慢查询功能，去获取所有查询时间比较长的SQL语句 其次使用explain命令去查询由问题的SQL的执行计划(脑补链接：点我直达1，点我直达2) 最后可以使用show profile[s] 查看由问题的SQL的性能使用情况 优化SQL语句 介绍 数据库查询快慢是影响项目性能"
tags:
  - "SQL优化"
  - "SQL"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13128593.html"
---

<h1 style="text-align: center">性能优化的思路</h1>
<ol>
<li>首先需要使用慢查询功能，去获取所有查询时间比较长的SQL语句</li>
<li>其次使用explain命令去查询由问题的SQL的执行计划(脑补链接：<a href="https://www.cnblogs.com/chenyanbin/p/13096937.html" target="_blank">点我直达1</a>，<a href="https://www.cnblogs.com/chenyanbin/p/13110056.html" target="_blank">点我直达2</a>)</li>
<li>最后可以使用show profile[s] 查看由问题的SQL的性能使用情况</li>
<li>优化SQL语句</li>
</ol>
<h1 style="text-align: center">介绍</h1>
<p>　　数据库查询快慢是影响项目性能的一大因素，对于数据库，我们除了要优化SQL，更重要的是得<span style="color: rgba(255, 0, 0, 1)"><strong>先找到需要优化的SQL语句</strong></span>。</p>
<p>　　MySQL数据库有一个“<span style="color: rgba(255, 0, 0, 1)"><strong>慢查询日志</strong></span>”功能，用来<span style="color: rgba(255, 0, 0, 1)"><strong>记录</strong></span>查询时间<span style="color: rgba(255, 0, 0, 1)"><strong>超过某个设定值的SQL</strong></span>，这将极大程度帮助我们<span style="color: rgba(255, 0, 0, 1)"><strong>快速定位到问题所在，以便对症下药</strong></span>。</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">至于查询时间的多少才算慢，每个项目、业务都有不同的要求。
    比如传统企业的软件允许查询时间高于某个值，但是把这个标准方在互联网项目或者访问量大的网站上，估计就是一个Bug，甚至可能升级为一个功能缺陷。</span></pre>
