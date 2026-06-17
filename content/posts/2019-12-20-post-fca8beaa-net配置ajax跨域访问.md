---
title: ".Net配置Ajax跨域访问"
date: 2019-12-20
description: "1、在web.config文件中的 system.webServer 节点下 增加如下配置 1 &lt;httpProtocol&gt; 2 &lt;customHeaders&gt; 3 &lt;add name=&quot;Access-Control-Allow-Origin&quot; va"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11118489.html"
---

<p><strong>1、在web.config文件中的 system.webServer 节点下 增加如下配置</strong></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> &lt;httpProtocol&gt;
<span style="color: rgba(0, 128, 128, 1)">2</span>             &lt;customHeaders&gt;
<span style="color: rgba(0, 128, 128, 1)">3</span>                 &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Access-Control-Allow-Origin</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">*</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">4</span>                 &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Access-Control-Allow-Headers</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">*</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">5</span>                 &lt;add name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Access-Control-Allow-Methods</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">GET, POST, PUT, DELETE</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">6</span>             &lt;/customHeaders&gt;
<span style="color: rgba(0, 128, 128, 1)">7</span> &lt;/httpProtocol&gt;</pre>
