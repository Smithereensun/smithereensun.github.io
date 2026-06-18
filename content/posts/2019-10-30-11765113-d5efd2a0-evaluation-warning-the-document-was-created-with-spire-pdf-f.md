{

  "title": "Evaluation Warning : The document was created with Spire.PDF for .NET.",
  "date": "2019-10-30",
  "description": "由于使用 Spire.Pdf 生成的书签带有 Evaluation Warning : The document was created with Spire.PDF for .NET. 字样 但是它只在第一页头部有显示，我们可以新增一页，并删掉第一页即可",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11765113.html"

}

由于使用  Spire.Pdf 生成的书签带有 Evaluation Warning : The document was created with Spire.PDF for .NET. 字样

但是它只在第一页头部有显示，我们可以新增一页，并删掉第一页即可

```text
string fileName = @"C:\Users\Administrator\Desktop\图纸\WH440-H111-F01_111分段结构图.pdf";
//创建一个新的PDF实例,导入PDF文件
PdfDocument pdf = new PdfDocument();
pdf.LoadFromFile(fileName);
PdfPageBase pb = pdf.Pages.Add(); //新增一页
pdf.Pages.Remove(pb); //去除第一页水印
```
