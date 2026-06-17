---
title: "C#NPOI对Excel的操作、导入导出时异常处理、最全的NPOI资料在这里~"
date: 2023-05-31
description: "一、Excel理论知识 最新版NPOI2.4.1链接：https://pan.baidu.com/s/1iTgJi2hGsRQHyw2S_4dIUw 提取码：adnq • 整个Excel表格叫做工作簿：WorkBook • 工作簿由以下几部分组成 a.页(Sheet); b.行(Row); c.单元"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10832614.html"
---

<h1>一、Excel理论知识</h1>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>最新版NPOI2.4.1链接</strong></span>：https://pan.baidu.com/s/1iTgJi2hGsRQHyw2S_4dIUw&nbsp;&nbsp;提取码：adnq&nbsp;</p>
<h2><span style="font-size: 18px">• 整个Excel表格叫做工作簿：WorkBook</span></h2>
<h2><span style="font-size: 18px">• 工作簿由以下几部分组成</span></h2>
<p><span style="font-size: 18px">　　a.页(Sheet);</span></p>
<p><span style="font-size: 18px">　　b.行(Row);</span></p>
<p><span style="font-size: 18px">　　c.单元格(Cell);</span></p>
<h1>二、处理Excel的技术</h1>
<h3>•OLE Automation：程序启动一个Excel进程，然后和Excel进程进行通讯来运行Excel的操作。</h3>
<p>　　优点：强大，Excel能实现的功能，都可以实现</p>
<p>　　缺点：必须装Excel</p>
<h3>•把Excel当成数据库，使用Microsoft.Jet.OleDb访问Excel，只适合二维结构，功能少，不用装Excel</h3>
<h3>•OpenXML，微软提供的读写Excel的技术，只能处理xlsx格式文件</h3>
<h3>•NPOI、MyXls，能够分析Excel文件的格式，能够进行常用Excel操作，<span style="color: rgba(255, 0, 0, 1)">不依赖于Excel，节省资源</span>，没有安全性和性能的问题。只能处理xls格式文件、不能处理xlsx这样的新版本Excel文件格式。处理xlsx用OpenXML</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 0, 0, 1)">描述工作簿的类：IWorkbook(接口)、HSSFWorkbook(具体实现类)
</span><span style="color: rgba(0, 128, 128, 1)">2</span> 
<span style="color: rgba(0, 128, 128, 1)">3</span> 描述工作表的类：ISheet(接口)、HSSFSheet(具体实现类)</pre>
