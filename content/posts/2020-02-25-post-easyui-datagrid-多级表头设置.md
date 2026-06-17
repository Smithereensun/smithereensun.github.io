---
title: "EasyUI DataGrid 多级表头设置"
date: 2020-02-25
description: "使用EasyUI做一个报表统计，需要合并表头为多级表头，核心代码如下: $(&#39;#dg&#39;).datagrid({ url:&#39;datagrid_data.action&#39;, fit : true, fitColumns : false, columns: [ [ {&quo"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12360823.html"
---

<p>使用EasyUI做一个报表统计，需要合并表头为多级表头，核心代码如下:</p>
<div class="cnblogs_code">
<pre>$('#dg'<span style="color: rgba(0, 0, 0, 1)">).datagrid({  
    url:</span>'datagrid_data.action'<span style="color: rgba(0, 0, 0, 1)">,  
    fit : </span><span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">,
    fitColumns : </span><span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">,
    columns:
         [
             [
                {</span>"title":"网格员考核测评表","colspan":9<span style="color: rgba(0, 0, 0, 1)">}
             ],
             [
                {</span>"field":"ORGNAME","title":"网格","rowspan":3,width:"80"<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"field":"USERZH","title":"网格员","rowspan":3,width:"80"<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"title":"工作纪律","rowspan":2<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"title":"民主互评","rowspan":2<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"title":"志愿者","rowspan":2<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"title":"加分项","colspan":2<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"title":"总分","rowspan":2<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"title":"平均分","rowspan":2<span style="color: rgba(0, 0, 0, 1)">}
             ],
             [
                {</span>"title":"信息上报","rowspan":1<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"title":"简报采纳","rowspan":1<span style="color: rgba(0, 0, 0, 1)">}
             ],
             [
                {</span>"field":"YW1","title":"5分","rowspan":1<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"field":"YW2","title":"5分","rowspan":1<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"field":"YW3","title":"6分","rowspan":1<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"field":"YW4","title":"8分","rowspan":1<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"field":"YW5","title":"5分","rowspan":1<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"field":"TOTAL","title":"","rowspan":1<span style="color: rgba(0, 0, 0, 1)">},
                {</span>"field":"AVG","title":"","rowspan":1<span style="color: rgba(0, 0, 0, 1)">}
             ]
         ]
}); </span></pre>
