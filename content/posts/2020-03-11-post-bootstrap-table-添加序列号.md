---
title: "BootStrap Table 添加序列号"
date: 2020-03-11
description: "js $(&#39;#table&#39;).bootstrapTable({ striped: true,//隔行换色 columns: [ { field: &#39;&#39;, title: &#39;序号&#39;, sortable: true, align: &quot;center&"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12461394.html"
---

<p>js</p>
<div class="cnblogs_code">
<pre>            $('#table'<span style="color: rgba(0, 0, 0, 1)">).bootstrapTable({
                striped: </span><span style="color: rgba(0, 0, 255, 1)">true</span>,<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">隔行换色</span>
<span style="color: rgba(0, 0, 0, 1)">                columns: [
                    {
                        field: </span>''<span style="color: rgba(0, 0, 0, 1)">,
                        title: </span>'序号'<span style="color: rgba(0, 0, 0, 1)">,
                        sortable: </span><span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">,
                        align: </span>"center"<span style="color: rgba(0, 0, 0, 1)">,
                        width: </span>40<span style="color: rgba(0, 0, 0, 1)">,
                        formatter: </span><span style="color: rgba(0, 0, 255, 1)">function</span><span style="color: rgba(0, 0, 0, 1)"> (value, row, index) {
                            </span><span style="color: rgba(0, 0, 255, 1)">return</span> index + 1<span style="color: rgba(0, 0, 0, 1)">;
                        }
                    },
                    { field: </span>'ID', title: '内码', visible: <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)"> },
                    { field: </span>'TIID', title: '任务明细状态表内码', visible: <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)"> },
                    { field: </span>'TASK_ID', title: '任务内码', visible: <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)"> },
                    { field: </span>'PROJ_ID', title: '船号',width:100,align:'center'<span style="color: rgba(0, 0, 0, 1)"> },
                    { field: </span>'SECTION_NO', title: '分段号',width:150,align:'center'<span style="color: rgba(0, 0, 0, 1)"> },
                    { field: </span>'NEST_NAME', title: '切割版图号',width:200,align:'center'<span style="color: rgba(0, 0, 0, 1)"> }
                ],
                pagination: </span><span style="color: rgba(0, 0, 255, 1)">true</span>, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">分页</span>
                pageNumber: 1, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">首页码</span>
                pageSize: 10, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">页面大小</span>
                pageList:[10,20,50<span style="color: rgba(0, 0, 0, 1)">],
                onClickRow: </span><span style="color: rgba(0, 0, 255, 1)">function</span><span style="color: rgba(0, 0, 0, 1)"> (row) {
                    curRow </span>=<span style="color: rgba(0, 0, 0, 1)"> row;
                    $(</span>"#infoPanel").popup();<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">显示明细面板</span>
<span style="color: rgba(0, 0, 0, 1)">                    LoadInfoTable(row.ID);
                }
            })</span></pre>
