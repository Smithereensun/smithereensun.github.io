---
title: "Aspose Excel 单元格合并后边框显示不全"
date: 2020-02-26
description: "/// &lt;summary&gt; /// 解决合并后的单元格没有边框,设置合并单元格格式,让合并过的单元格中每一个单元格上都添加上加边框的样式 /// &lt;/summary&gt; /// &lt;param name=&quot;cells&quot;&gt;单元格&lt;/param&"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12369067.html"
---

<div class="cnblogs_code">
<pre>        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 解决合并后的单元格没有边框,设置合并单元格格式,让合并过的单元格中每一个单元格上都添加上加边框的样式
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="cells"&gt;</span><span style="color: rgba(0, 128, 0, 1)">单元格</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="firstRow"&gt;</span><span style="color: rgba(0, 128, 0, 1)">起始行</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="firstColumn"&gt;</span><span style="color: rgba(0, 128, 0, 1)">起始列</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="rowNumber"&gt;</span><span style="color: rgba(0, 128, 0, 1)">行偏移量</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="columnNumber"&gt;</span><span style="color: rgba(0, 128, 0, 1)">列偏移量</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="style"&gt;</span><span style="color: rgba(0, 128, 0, 1)">样式</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> SetCellStyle(Cells cells, <span style="color: rgba(0, 0, 255, 1)">int</span> firstRow, <span style="color: rgba(0, 0, 255, 1)">int</span> firstColumn, <span style="color: rgba(0, 0, 255, 1)">int</span> rowNumber, <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> columnNumber, Style style)
        {
            </span><span style="color: rgba(0, 0, 255, 1)">int</span> totalRow = firstRow +<span style="color: rgba(0, 0, 0, 1)"> rowNumber;
            </span><span style="color: rgba(0, 0, 255, 1)">int</span> totalColumn = firstColumn +<span style="color: rgba(0, 0, 0, 1)"> columnNumber;
            </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = firstRow; i &lt; totalRow; i++<span style="color: rgba(0, 0, 0, 1)">)
            {
                </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> j = firstColumn; j &lt; totalColumn; j++<span style="color: rgba(0, 0, 0, 1)">)
                {
                    cells[i, j].Style </span>=<span style="color: rgba(0, 0, 0, 1)"> style;
                }
            }
        }</span></pre>
