---
title: "ExtJs 扩展类CheckColumn修改源码，支持按条件禁用启用下拉框功能"
date: 2023-05-31
description: "长话短说，具体的请看图 需求如图： 修改CheckColumn.js源码，添加鼠标点击改变事件 完整JS脚本 1 Ext.ns(&#39;Ext.ux.grid&#39;); 2 Ext.ux.grid.CheckColumn = Ext.extend(Ext.grid.Column, { 3 ed"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11762767.html"
---

<p>长话短说，具体的请看图</p>
<p>需求如图：</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191030082425686-140085107.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;修改CheckColumn.js源码，添加鼠标点击改变事件</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191030082529836-1999709049.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191030082607120-1620803462.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191030082747461-1458732568.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;完整JS脚本</p>
<div class="cnblogs_code"><img id="code_img_closed_93ed01ff-50cd-48c4-82c6-7c783e4b4ea4" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_93ed01ff-50cd-48c4-82c6-7c783e4b4ea4" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_93ed01ff-50cd-48c4-82c6-7c783e4b4ea4" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> Ext.ns(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">Ext.ux.grid</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> Ext.ux.grid.CheckColumn =<span style="color: rgba(0, 0, 0, 1)"> Ext.extend(Ext.grid.Column, {
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span>     editable: <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">    processEvent: function (name, e, grid, rowIndex, colIndex) {
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (name == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">mousedown</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>             prj.curGrid =<span style="color: rgba(0, 0, 0, 1)"> grid;
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>             <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.init(name, e, grid, rowIndex, colIndex);
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> record =<span style="color: rgba(0, 0, 0, 1)"> grid.store.getAt(rowIndex);
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>             <span style="color: rgba(0, 0, 255, 1)">this</span>.fireEvent(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">checkchange</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(0, 0, 255, 1)">this</span>, record.data[<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.dataIndex]);
</span><span style="color: rgba(0, 128, 128, 1)">10</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.editable) {
</span><span style="color: rgba(0, 128, 128, 1)">11</span>                 record.<span style="color: rgba(0, 0, 255, 1)">set</span>(<span style="color: rgba(0, 0, 255, 1)">this</span>.dataIndex, !record.data[<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.dataIndex]);
</span><span style="color: rgba(0, 128, 128, 1)">12</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">13</span>             } <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)">14</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> Ext.grid.ActionColumn.superclass.processEvent.apply(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, arguments);
</span><span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">16</span>         } <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)">17</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> Ext.grid.ActionColumn.superclass.processEvent.apply(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, arguments);
</span><span style="color: rgba(0, 128, 128, 1)">18</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">19</span> <span style="color: rgba(0, 0, 0, 1)">    },
</span><span style="color: rgba(0, 128, 128, 1)">20</span> <span style="color: rgba(0, 0, 0, 1)">    renderer: function (v, p, record) {
</span><span style="color: rgba(0, 128, 128, 1)">21</span>         p.css += <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)"> x-grid3-check-col-td</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">22</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> String.format(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">&lt;div class="x-grid3-check-col{0}"&gt;&amp;#160;&lt;/div&gt;</span><span style="color: rgba(128, 0, 0, 1)">'</span>, v ? <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">-on</span><span style="color: rgba(128, 0, 0, 1)">'</span> : <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">23</span> <span style="color: rgba(0, 0, 0, 1)">    },
</span><span style="color: rgba(0, 128, 128, 1)">24</span> <span style="color: rgba(0, 0, 0, 1)">    init: Ext.emptyFn,
</span><span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">    setEditable: function (f) {
</span><span style="color: rgba(0, 128, 128, 1)">26</span>         <span style="color: rgba(0, 0, 255, 1)">this</span>.editable =<span style="color: rgba(0, 0, 0, 1)"> f;
</span><span style="color: rgba(0, 128, 128, 1)">27</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">28</span> <span style="color: rgba(0, 0, 0, 1)">});
</span><span style="color: rgba(0, 128, 128, 1)">29</span> 
<span style="color: rgba(0, 128, 128, 1)">30</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> register ptype. Deprecate. Remove in 4.0</span>
<span style="color: rgba(0, 128, 128, 1)">31</span> Ext.preg(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">checkcolumn</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, Ext.ux.grid.CheckColumn);
</span><span style="color: rgba(0, 128, 128, 1)">32</span> 
<span style="color: rgba(0, 128, 128, 1)">33</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> backwards compat. Remove in 4.0</span>
<span style="color: rgba(0, 128, 128, 1)">34</span> Ext.grid.CheckColumn =<span style="color: rgba(0, 0, 0, 1)"> Ext.ux.grid.CheckColumn;
</span><span style="color: rgba(0, 128, 128, 1)">35</span> 
<span style="color: rgba(0, 128, 128, 1)">36</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> register Column xtype</span>
<span style="color: rgba(0, 128, 128, 1)">37</span> Ext.grid.Column.types.checkcolumn = Ext.ux.grid.CheckColumn;</pre>
