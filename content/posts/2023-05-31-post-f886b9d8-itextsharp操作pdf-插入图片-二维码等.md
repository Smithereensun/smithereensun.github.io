---
title: "itextsharp操作pdf——插入图片、二维码等"
date: 2023-05-31
description: "简单介绍 业务需求，需要往pdf图纸上添加二维码功能，将实现过程记录下来 下载类库 直接下载 添加引用 添加命名空间 using System.IO; using iTextSharp.text.pdf; 插入图片处理函数 /// &lt;summary&gt; /// 向pdf中添加图片 ///"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11775108.html"
---

<h1>简单介绍</h1>
<p>　　业务需求，需要往pdf图纸上添加二维码功能，将实现过程记录下来</p>
<h1>下载类库</h1>
<p><a href="https://files-cdn.cnblogs.com/files/chenyanbin/itextsharp.rar" target="_blank">直接下载</a></p>
<h1>添加引用</h1>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201911/1504448-20191101084954061-1143901726.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h1>添加命名空间</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.IO;
</span><span style="color: rgba(0, 0, 255, 1)">using</span> iTextSharp.text.pdf;</pre>
