---
title: "Evaluation Warning : The document was created with Spire.PDF for .NET."
date: 2019-10-30
description: "由于使用 Spire.Pdf 生成的书签带有&#160;Evaluation Warning : The document was created with Spire.PDF for .NET. 字样 但是它只在第一页头部有显示，我们可以新增一页，并删掉第一页即可"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11765113.html"
---

<p>由于使用&nbsp; Spire.Pdf 生成的书签带有&nbsp;Evaluation Warning : The document was created with Spire.PDF for .NET. 字样</p>
<p>但是它只在第一页头部有显示，我们可以新增一页，并删掉第一页即可</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">string</span> fileName = <span style="color: rgba(128, 0, 0, 1)">@"</span><span style="color: rgba(128, 0, 0, 1)">C:\Users\Administrator\Desktop\图纸\WH440-H111-F01_111分段结构图.pdf</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建一个新的PDF实例,导入PDF文件            </span>
PdfDocument pdf = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> PdfDocument();
pdf.LoadFromFile(fileName);
PdfPageBase pb </span>= pdf.Pages.Add(); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">新增一页</span>
pdf.Pages.Remove(pb); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">去除第一页水印</span></pre>
