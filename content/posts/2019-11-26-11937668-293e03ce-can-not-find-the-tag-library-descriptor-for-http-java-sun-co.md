{

  "title": "Can not find the tag library descriptor for “http://java.sun.com/jstl/core\"",
  "date": "2019-11-26",
  "description": "此文原博文地址：https://blog.csdn.net/kolamemo/article/details/51407467 按照查到的资料，JSTL taglib需要jstl.jar来支持。在1.0和1.1版本的时候，还需要standard.jar来配合。但从1.2版本开始，jar文件名字变成了",
  "tags": [
    "JAVA",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11937668.html"

}

此文原博文地址：https://blog.csdn.net/kolamemo/article/details/51407467

　　按照查到的资料，JSTL taglib需要jstl.jar来支持。在1.0和1.1版本的时候，还需要standard.jar来配合。但从1.2版本开始，jar文件名字变成了jstl-1.2.jar，也不再需要standard.jar了。另外，servlet 版本需要2.4以上。所以正确的做法是把jstl-1.2.jar放到WEB-INF/lib里面就可以了。或者通过maven来配置，如下：

```text
        <dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>jstl</artifactId>
            <version>1.2</version>
        </dependency>
```

然后在运行时看到这个错误：

**org.apache.jasper.JasperException: The absolute uri: http://java.sun.com/jstl/core cannot be resolved in either web.xml or the jar files deployed with this application**
这是uri错误。在jstl.jar版本1.0和1.1的时候，名字里面没有“jsp”。但是1.2版本后变成了http://java.sun.com/jsp/jstl/core了，改好后解决。
