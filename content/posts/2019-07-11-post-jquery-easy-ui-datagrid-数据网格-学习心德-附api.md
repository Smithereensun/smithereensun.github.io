---
title: "jquery Easy UI Datagrid(数据网格)学习心德，附API"
date: 2019-07-11
description: "第一步，引入主要的css样式和js文件 1 &lt;meta http-equiv=&quot;Content-Type&quot; content=&quot;text/html; charset=utf-8&quot;/&gt; 2 &lt;title&gt;&lt;/title&gt; 3 &"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11173287.html"
---

<h2>&nbsp;</h2>
<h2>第一步，引入主要的css样式和js文件</h2>
<div class="cnblogs_code"><img id="code_img_closed_c05eaa20-0c96-4470-84dc-0ef02648d6f8" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_c05eaa20-0c96-4470-84dc-0ef02648d6f8" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_c05eaa20-0c96-4470-84dc-0ef02648d6f8" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">meta </span><span style="color: rgba(255, 0, 0, 1)">http-equiv</span><span style="color: rgba(0, 0, 255, 1)">="Content-Type"</span><span style="color: rgba(255, 0, 0, 1)"> content</span><span style="color: rgba(0, 0, 255, 1)">="text/html; charset=utf-8"</span><span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">2</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">title</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">title</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">3</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">meta </span><span style="color: rgba(255, 0, 0, 1)">charset</span><span style="color: rgba(0, 0, 255, 1)">="utf-8"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">4</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">link </span><span style="color: rgba(255, 0, 0, 1)">href</span><span style="color: rgba(0, 0, 255, 1)">="../../Script/jquery-easyui-1.7.0/themes/icon.css"</span><span style="color: rgba(255, 0, 0, 1)"> rel</span><span style="color: rgba(0, 0, 255, 1)">="stylesheet"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">5</span>     <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">引入图标css样式</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">6</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">link </span><span style="color: rgba(255, 0, 0, 1)">href</span><span style="color: rgba(0, 0, 255, 1)">="../../Script/jquery-easyui-1.7.0/themes/material/easyui.css"</span><span style="color: rgba(255, 0, 0, 1)"> rel</span><span style="color: rgba(0, 0, 255, 1)">="stylesheet"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">7</span>     <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">引入总的css样式</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">8</span> <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">head</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
