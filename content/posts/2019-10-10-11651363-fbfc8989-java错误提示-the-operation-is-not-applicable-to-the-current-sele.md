{

  "title": "JAVA错误提示:The operation is not applicable to the current selection.Select a field which is not declared as type variable or a type that declares such fields.",
  "date": "2019-10-10",
  "description": "平时没怎么注意，今天用Eclipse自动生成Set Get方法时提示错误，错误信息如下： The operation is not applicable to the current selection.Select a field which is not declared as type var",
  "tags": [
    "Java",
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11651363.html"

}

平时没怎么注意，今天用Eclipse自动生成Set Get方法时提示错误，错误信息如下：

The operation is not applicable to the current selection.Select a field which is not declared as type variable or a type that declares such fields.

![](/imported/posts/2019-10-10-11651363-fbfc8989-java错误提示-the-operation-is-not-applicable-to-the-current-sele/images/img_001_8fe6b9895100.png)

 原因：

![](/imported/posts/2019-10-10-11651363-fbfc8989-java错误提示-the-operation-is-not-applicable-to-the-current-sele/images/img_002_6f77db075d51.png)

解决方案：将光标定位到类内部自动生成Set、Get即可

![](/imported/posts/2019-10-10-11651363-fbfc8989-java错误提示-the-operation-is-not-applicable-to-the-current-sele/images/img_003_1b9aa477f7fb.png)
