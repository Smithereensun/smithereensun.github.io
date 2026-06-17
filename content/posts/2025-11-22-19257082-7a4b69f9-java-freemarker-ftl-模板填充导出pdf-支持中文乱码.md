{

  "title": "java freemarker（ftl）模板填充导出PDF，支持中文乱码",
  "date": "2025-11-22",
  "description": "添加依赖 java代码 ftl模板使用字体库 文件名：xxx.ftl ps：处理中文乱码** 字体库 更多字体库：https://www.mianfeiziti.com/thread-491.htm",
  "tags": [
    "JAVA",
    "Spring Boot"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/19257082"

}

# 添加依赖

```text
        <dependency>
            <groupId>org.freemarker</groupId>
            <artifactId>freemarker</artifactId>
            <version>2.3.32</version>
        </dependency>

        <dependency>
            <groupId>com.openhtmltopdf</groupId>
            <artifactId>openhtmltopdf-pdfbox</artifactId>
            <version>1.0.10</version>
        </dependency>
```

# java代码

```text
    public void exportPdf(String html, String outputPath) throws Exception {

        PdfRendererBuilder builder = new PdfRendererBuilder();
        builder.useFastMode();
        // 注册思源宋体——关键点
        builder.useFont(() -> getClass().getClassLoader()
                .getResourceAsStream("xxx/siyuansongti.ttf"), "Source Han Serif CN");
        builder.useFont(() -> getClass().getClassLoader()
                .getResourceAsStream("xxx/DejaVuSans-7.ttf"), "DejaVu Sans");

        builder.withHtmlContent(html, null);
        builder.toStream(new FileOutputStream(outputPath));
        builder.run();
    }

    @GetMapping("test")
    public void test() throws Exception{
        Configuration cfg = new Configuration(Configuration.VERSION_2_3_32);
        cfg.setDefaultEncoding("UTF-8");

        cfg.setClassLoaderForTemplateLoading(
                this.getClass().getClassLoader(),
                "templates"
        );

        Template tpl = cfg.getTemplate("xxx/index.ftl");

        StringWriter writer = new StringWriter();
        tpl.process(buildDto(), writer);

        exportPdf(writer.toString(), "D:/xxx.pdf");
    }
```

# ftl模板使用字体库

文件名：xxx.ftl

**ps：处理中文乱码**

```text
        body {
            font-family: "Source Han Serif CN", "DejaVu Sans";
            font-size: 12px;
            margin: 0;
            padding: 0;
        }
```

# 字体库

```text
https://chenyanbin-software.oss-cn-guangzhou.aliyuncs.com/%E5%AD%97%E4%BD%93%E5%BA%93/DejaVuSans-7.ttf

https://chenyanbin-software.oss-cn-guangzhou.aliyuncs.com/%E5%AD%97%E4%BD%93%E5%BA%93/siyuansongti.ttf
```

更多字体库：[https://www.mianfeiziti.com/thread-491.htm](https://www.mianfeiziti.com/thread-491.htm)
