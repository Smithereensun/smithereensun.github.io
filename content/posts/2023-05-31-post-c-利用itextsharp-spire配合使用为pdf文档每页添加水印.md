---
title: "C# 利用itextsharp、Spire配合使用为pdf文档每页添加水印"
date: 2023-05-31
description: "下载类库： 直接下载 引入类库 功能实现 using iTextSharp.text.pdf; using Spire.Pdf; using Spire.Pdf.Graphics; using System; using System.Drawing; using System.Windows.Fo"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11765213.html"
---

<h2>下载类库：</h2>
<p><a href="https://files-cdn.cnblogs.com/files/chenyanbin/dll.rar" target="_blank">直接下载</a></p>
<h2>引入类库</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191030152129231-2022890600.png" alt="" /></p>
<h2>功能实现</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> iTextSharp.text.pdf;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> Spire.Pdf;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> Spire.Pdf.Graphics;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Drawing;
</span><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Windows.Forms;
</span><span style="color: rgba(0, 0, 255, 1)">using</span> PdfDocument =<span style="color: rgba(0, 0, 0, 1)"> Spire.Pdf.PdfDocument;
</span><span style="color: rgba(0, 0, 255, 1)">using</span> PdfFont =<span style="color: rgba(0, 0, 0, 1)"> Spire.Pdf.Graphics.PdfFont;

</span><span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> ProcessPdfDemo
{
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">partial</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Form1 : Form
    {
        </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Form1()
        {
            InitializeComponent();
        }

        </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> Button1_Click(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> sender, EventArgs e)
        {
            </span><span style="color: rgba(0, 0, 255, 1)">string</span> fileName = <span style="color: rgba(128, 0, 0, 1)">@"</span><span style="color: rgba(128, 0, 0, 1)">C:\Users\Administrator\Desktop\图纸\WH440-H111-F01_111分段结构图.pdf</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建一个新的PDF实例,导入PDF文件            </span>
            PdfDocument pdf = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> PdfDocument();
            pdf.LoadFromFile(fileName);
            PdfPageBase pb </span>= pdf.Pages.Add(); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">新增一页</span>
            pdf.Pages.Remove(pb); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">去除第一页水印</span>
            <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = <span style="color: rgba(128, 0, 128, 1)">0</span>; i &lt; GetPdfPageNum(fileName); i++<span style="color: rgba(0, 0, 0, 1)">)
            {
                PdfPageBase page </span>=<span style="color: rgba(0, 0, 0, 1)"> pdf.Pages[i];                
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">添加文本水印到文件的第一页，设置文本格式</span>
                PdfTilingBrush brush = <span style="color: rgba(0, 0, 255, 1)">new</span> PdfTilingBrush(<span style="color: rgba(0, 0, 255, 1)">new</span> SizeF(page.Canvas.ClientSize.Width / <span style="color: rgba(128, 0, 128, 1)">3</span>, page.Canvas.ClientSize.Height / <span style="color: rgba(128, 0, 128, 1)">3</span>)); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">设置每行每列几个水印</span>
                brush.Graphics.SetTransparency(<span style="color: rgba(128, 0, 128, 1)">0.2f</span>); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">透明度</span>
<span style="color: rgba(0, 0, 0, 1)">                brush.Graphics.Save();
                brush.Graphics.TranslateTransform(brush.Size.Width </span>/ <span style="color: rgba(128, 0, 128, 1)">2</span>, brush.Size.Height / <span style="color: rgba(128, 0, 128, 1)">2</span><span style="color: rgba(0, 0, 0, 1)">);
                brush.Graphics.RotateTransform(</span>-<span style="color: rgba(128, 0, 128, 1)">45</span>); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">旋转角度</span>
                brush.Graphics.DrawString(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Draft Version</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(0, 0, 255, 1)">new</span> PdfFont(PdfFontFamily.Helvetica, <span style="color: rgba(128, 0, 128, 1)">40</span>), PdfBrushes.Blue, <span style="color: rgba(128, 0, 128, 1)">0</span>, <span style="color: rgba(128, 0, 128, 1)">0</span>, <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> PdfStringFormat(PdfTextAlignment.Center));
                brush.Graphics.Restore();
                brush.Graphics.SetTransparency(</span><span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">);
                page.Canvas.DrawRectangle(brush, </span><span style="color: rgba(0, 0, 255, 1)">new</span> RectangleF(<span style="color: rgba(0, 0, 255, 1)">new</span> PointF(<span style="color: rgba(128, 0, 128, 1)">0</span>, <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">), page.Canvas.ClientSize));
            }
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">保存文件</span>
            pdf.SaveToFile(<span style="color: rgba(128, 0, 0, 1)">@"</span><span style="color: rgba(128, 0, 0, 1)">C:\Users\Administrator\Desktop\图纸\2222.pdf</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
            MessageBox.Show(</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ok</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
        }
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 获取pdf页数
        </span><span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="pdfFile"&gt;&lt;/param&gt;</span>
        <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span> GetPdfPageNum(<span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> pdfFile)
        {
            PdfReader reader </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> PdfReader(pdfFile);
            </span><span style="color: rgba(0, 0, 255, 1)">int</span> iPageNum =<span style="color: rgba(0, 0, 0, 1)"> reader.NumberOfPages;
            reader.Close(); </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">不关闭会一直占用pdf资源，对接下来的操作会有影响</span>
            <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> iPageNum;
        }
    }
}</span></pre>
