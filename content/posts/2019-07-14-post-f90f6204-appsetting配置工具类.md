---
title: "AppSetting配置工具类"
date: 2019-07-14
description: "1 &lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt; 2 &lt;!-- 3 有关如何配置 ASP.NET 应用程序的详细信息，请访问 4 http://go.microsoft.com/fwlink/?LinkId=1"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11184405.html"
---

<div class="cnblogs_code"><img id="code_img_closed_781db711-6814-4757-84d1-bed56ba9583e" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_781db711-6814-4757-84d1-bed56ba9583e" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_781db711-6814-4757-84d1-bed56ba9583e" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> &lt;?xml version=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">1.0</span><span style="color: rgba(128, 0, 0, 1)">"</span> encoding=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">utf-8</span><span style="color: rgba(128, 0, 0, 1)">"</span>?&gt;
<span style="color: rgba(0, 128, 128, 1)"> 2</span> &lt;!--
<span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 0, 1)">  有关如何配置 ASP.NET 应用程序的详细信息，请访问
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span>   http:<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">go.microsoft.com/fwlink/?LinkId=169433</span>
<span style="color: rgba(0, 128, 128, 1)"> 5</span>   --&gt;
<span style="color: rgba(0, 128, 128, 1)"> 6</span> &lt;configuration&gt;
<span style="color: rgba(0, 128, 128, 1)"> 7</span>   &lt;appSettings&gt;
<span style="color: rgba(0, 128, 128, 1)"> 8</span>     &lt;add key=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">key1</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">value1</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)"> 9</span>   &lt;/appSettings&gt;
<span style="color: rgba(0, 128, 128, 1)">10</span> &lt;/configuration&gt;</pre>
