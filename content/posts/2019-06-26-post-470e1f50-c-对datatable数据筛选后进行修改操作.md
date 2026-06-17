---
title: "c# 对DataTable数据筛选后进行修改操作"
date: 2019-06-26
description: "记录一次对DataTable中的数据筛选去重后，然后对数据进行修改！"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10906310.html"
---

<h3>记录一次对DataTable中的数据筛选去重后，然后对数据进行修改！</h3>
<div class="cnblogs_code">
<pre>                <span style="color: rgba(0, 0, 255, 1)">foreach</span> (DataRow dr <span style="color: rgba(0, 0, 255, 1)">in</span> dt.Rows) <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 便利dt</span>
<span style="color: rgba(0, 0, 0, 1)">                {
                    </span><span style="color: rgba(0, 0, 255, 1)">if</span> (StringUtil.isNotNullOrBlank(dr[<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">GEN_REST_CODE</span><span style="color: rgba(128, 0, 0, 1)">"</span>]))<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">判断是否有产生余料编号，存在继续执行</span>
<span style="color: rgba(0, 0, 0, 1)">                    {
                        DataRow[] tmpDrs </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
                        tmpDrs </span>= dt.Select(<span style="color: rgba(0, 0, 255, 1)">string</span>.Format(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">GEN_REST_CODE='{0}'</span><span style="color: rgba(128, 0, 0, 1)">"</span>, dr[<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">GEN_REST_CODE</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">].ToString()));<span style="color: rgba(255, 0, 0, 1)"><strong> //筛选数据
                        </strong></span></span><span style="color: rgba(0, 0, 255, 1)">if</span> (tmpDrs.Length != <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">)
                        {
                            DataRow[] tmpDrs2 </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
                            tmpDrs2 </span>= dt.Select(<span style="color: rgba(0, 0, 255, 1)">string</span>.Format(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">NEST_NAME='{0}'</span><span style="color: rgba(128, 0, 0, 1)">"</span>, tmpDrs[<span style="color: rgba(128, 0, 128, 1)">0</span>].ItemArray[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">]));
                            </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = <span style="color: rgba(128, 0, 128, 1)">0</span>; i &lt; tmpDrs2.Length-<span style="color: rgba(128, 0, 128, 1)">1</span>; i++) <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 修改产生余料编号</span>
<span style="color: rgba(0, 0, 0, 1)">                            {
                                DataRow dRow </span>=<span style="color: rgba(0, 0, 0, 1)"> tmpDrs2[i];
                                dRow.BeginEdit(); <span style="color: rgba(255, 0, 0, 1)"><strong>//开始编辑</strong></span>
                                dRow[</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">GEN_REST_CODE</span><span style="color: rgba(128, 0, 0, 1)">"</span>] = tmpDrs[<span style="color: rgba(128, 0, 128, 1)">0</span>].ItemArray[<span style="color: rgba(128, 0, 128, 1)">5</span><span style="color: rgba(0, 0, 0, 1)">];
                                dRow.EndEdit(); <span style="color: rgba(255, 0, 0, 1)"><strong>//结束编辑</strong></span>
                               <span style="color: rgba(255, 0, 0, 1)"><strong> dt.AcceptChanges(); </strong></span></span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 保存修改的结果</span>
<span style="color: rgba(0, 0, 0, 1)">                            }
                        }
                    }
                }</span></pre>
