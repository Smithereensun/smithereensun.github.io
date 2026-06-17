---
title: "Mysql binlog备份数据及恢复数据，学会这个，我在也不怕删库跑路啦~"
date: 2023-05-31
description: "导读 我一直都主张，技多不压身(没有学不会的技术，只有不学习的人)，多学一项技能，未来就少求人一次。网上经常听到xxx删库跑路，万一真的遇到了，相信通过今天的学习，也能将数据再恢复回来~~~ 当然啦，备份数据/还原数据也是挺重要的，可以看我另一篇：点我直达 如果感觉这样还不安全，可以考虑授予用户权限"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14022086.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　我一直都主张，技多不压身(<strong><span style="color: rgba(255, 0, 0, 1)">没有学不会的技术，只有不学习的人</span></strong>)，多学一项技能，未来就少求人一次。网上经常听到xxx删库跑路，万一真的遇到了，相信通过今天的学习，也能将数据再恢复回来~~~</p>
<p>　　当然啦，备份数据/还原数据也是挺重要的，可以看我另一篇：<a href="https://www.cnblogs.com/chenyanbin/p/14020293.html" target="_blank">点我直达</a></p>
<p>　　如果感觉这样还不安全，可以考虑授予用户权限：<a href="https://www.cnblogs.com/chenyanbin/p/14003024.html" target="_blank">点我直达</a></p>
<h1 style="text-align: center">介绍</h1>
<p>　　记录着mysql数据库中的一些增删改操作(<strong><span style="color: rgba(255, 0, 0, 1)">没有查询</span></strong>)</p>
<h2>功能</h2>
<ol>
<li>数据复制(<strong><span style="color: rgba(255, 0, 0, 1)">主从复制</span></strong>)</li>
<li>数据恢复</li>
</ol>
<h2>注意事项</h2>
<p>　　开启二进制日志会有性能的消耗！！！</p>
<h2>查看二进制日志是否开启</h2>
<div class="cnblogs_code">
<pre>查看是否开启：show variables like 'log_bin%';</pre>
