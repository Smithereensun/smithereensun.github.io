---
title: "mac 安装homebrew 报443"
date: 2020-10-14
description: "描述 macOS安装Homebrew时总是报错（Failed to connect to raw.githubusercontent.com port 443: Connection refused） 原因 由于某些你懂的因素，导致GitHub的raw.githubusercontent.com域名"
tags:
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13814274.html"
---

<h1>描述</h1>
<p>　　macOS安装Homebrew时总是报错（Failed to connect to raw.githubusercontent.com port 443: Connection refused）</p>
<h1>原因</h1>
<p>　　由于某些<code>你懂的因素</code>，导致GitHub的<code>raw.githubusercontent.com</code>域名解析被污染了。</p>
<p>解决</p>
<ol>
<li>https://www.ipaddress.com/，通过该网站查询raw.githubusercontent.com的真实IP。</li>
<li>修改hosts</li>
</ol>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">sudo vim /etc/hosts


xxx.xxx.xxx.xxx  raw.githubusercontent.com</span></pre>
