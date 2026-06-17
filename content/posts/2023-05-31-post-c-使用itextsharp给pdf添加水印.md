---
title: "C#使用iTextSharp给PDF添加水印"
date: 2023-05-31
description: "昨天利用itextsharp、Spire配合使用为pdf文档每页添加水印&#160;发现公司的框架用的.netframework3.5。用上面那个方法，.netframework最低4.0，升级公司框架的版本，导致之前写过的代码报错地方比较多，所以网上找到了该方法，记录下来，支持.netframew"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11769534.html"
---

<p>　　昨天<a class="postTitle2" href="https://www.cnblogs.com/chenyanbin/p/11765213.html">利用itextsharp、Spire配合使用为pdf文档每页添加水印</a>&nbsp;发现公司的框架用的.netframework3.5。用上面那个方法，.netframework最低4.0，升级公司框架的版本，导致之前写过的代码报错地方比较多，所以网上找到了该方法，记录下来，支持.netframework3.5</p>
<h1>类库下载:</h1>
<p><a href="https://files-cdn.cnblogs.com/files/chenyanbin/itextsharp.rar" target="_blank">直接下载</a></p>
<h1>引入类库</h1>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191031094850280-415853851.png" alt="" /></p>
<p>&nbsp;</p>
<h1>&nbsp;引入命名空间</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> iTextSharp.text;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> iTextSharp.text.pdf;
</span><span style="color: rgba(0, 0, 255, 1)">using</span> System.IO;</pre>
