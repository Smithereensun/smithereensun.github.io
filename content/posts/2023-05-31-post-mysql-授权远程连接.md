---
title: "mysql 授权远程连接"
date: 2023-05-31
description: "解决方案 改表法 可能是你的帐号不允许从远程登陆，只能在localhost。这个时候只要在localhost的那台电脑，登入mysql后，更改 &quot;mysql&quot; 数据库里的 &quot;user&quot; 表里的 &quot;host&quot; 项，从&quot;localho"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12860334.html"
---

<h1 style="text-align: center">解决方案</h1>
<h2>改表法</h2>
<p>可能是你的帐号不允许从远程登陆，只能在localhost。这个时候只要在localhost的那台电脑，登入mysql后，更改 "mysql" 数据库里的 "user" 表里的 "host" 项，从"localhost"改称"%"<br>　　mysql -u root -pvmwaremysql&gt;use mysql;<br>　　mysql&gt;update user set host = '%' where user = 'root';<br>　　mysql&gt;select host, user from user;</p>
<h2>搜权命令</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">grant</span> 权限 <span style="color: rgba(0, 0, 255, 1)">on</span> 数据库对象 <span style="color: rgba(0, 0, 255, 1)">to</span> 用户</pre>
