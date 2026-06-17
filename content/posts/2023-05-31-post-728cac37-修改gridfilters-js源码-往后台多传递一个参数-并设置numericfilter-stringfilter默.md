---
title: "修改gridfilters.js源码，往后台多传递一个参数，并设置NumericFilter、StringFilter默认提示信息"
date: 2023-05-31
description: "创作不易，转载请注明出处！！！ 效果 修改：ext-extend.js源码 在最后面添加3行，重写方法 代码拷贝区 Ext.override(Ext.ux.grid.GridFilters, { menuFilterText: &quot;筛选&quot; }); Ext.override(Ext."
tags:
  - "JavaScript"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12431909.html"
---

<p style="text-align: left">　　创作不易，转载请注明出处！！！</p>
<h1 style="text-align: center">效果</h1>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200306235957785-12874299.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200307000009104-91470629.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1 style="text-align: center">修改：ext-extend.js源码</h1>
<p>　　在最后面添加3行，重写方法</p>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200307000313772-1153537598.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>代码拷贝区</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">Ext.override(Ext.ux.grid.GridFilters, {
    menuFilterText: </span>"筛选"<span style="color: rgba(0, 0, 0, 1)">
});

Ext.override(Ext.ux.grid.filter.DateFilter, {
    afterText: </span>"大于"<span style="color: rgba(0, 0, 0, 1)">,
    beforeText: </span>"小于"<span style="color: rgba(0, 0, 0, 1)">,
    onText: </span>"等于"<span style="color: rgba(0, 0, 0, 1)">
});
Ext.override(Ext.ux.grid.filter.String, {
    emptyText: </span>'Enter Filter Text...'<span style="color: rgba(0, 0, 0, 1)">
});</span></pre>
