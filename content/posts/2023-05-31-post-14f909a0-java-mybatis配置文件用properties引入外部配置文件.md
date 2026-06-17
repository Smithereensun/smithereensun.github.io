---
title: "JAVA MyBatis配置文件用properties引入外部配置文件"
date: 2023-05-31
description: "方式一：通过properties 元素的子元素来传递数据 例如： 1 &lt;properties&gt; 2 &lt;property name=&quot;driver&quot; value=&quot;com.mysql.jdbc.Driver&quot; /&gt; &lt;!-- 驱动类"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11655095.html"
---

<h2>方式一：通过properties 元素的子元素来传递数据</h2>
<p>例如：</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span>     &lt;properties&gt;
<span style="color: rgba(0, 128, 128, 1)">2</span>         &lt;property name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">driver</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">com.mysql.jdbc.Driver</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt; &lt;!-- 驱动类型 --&gt;
<span style="color: rgba(0, 128, 128, 1)">3</span>         &lt;property name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">url</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">jdbc:mysql://localhost:3306/sam</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt; &lt;!-- 连接字符串 --&gt;
<span style="color: rgba(0, 128, 128, 1)">4</span>         &lt;property name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">username</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">root</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt; &lt;!-- 用户名 --&gt;
<span style="color: rgba(0, 128, 128, 1)">5</span>         &lt;property name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">password</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">root</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt; &lt;!-- 密码 --&gt;
<span style="color: rgba(0, 128, 128, 1)">6</span>     &lt;/properties&gt;</pre>
