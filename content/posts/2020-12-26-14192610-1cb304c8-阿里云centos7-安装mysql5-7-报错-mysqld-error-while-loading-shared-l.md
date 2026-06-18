{

  "title": "阿里云Centos7 安装mysql5.7 报错：./mysqld: error while loading shared libraries: libaio.so.1: cannot open shared object file: No such file or directory",
  "date": "2020-12-26",
  "description": "在阿里云服务器Centos7中安装mysql5.7，解压数据库初始化后，报错 检查是否安装libaio 若不存在，安装这个包即可",
  "tags": [
    "MySQL",
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/14192610.html"

}

在阿里云服务器Centos7中安装mysql5.7，解压数据库初始化后，报错

```text
./mysqld: error while loading shared libraries: libaio.so.1: cannot open shared object file: No such file or directory
```

![](/imported/posts/2020-12-26-14192610-1cb304c8-阿里云centos7-安装mysql5-7-报错-mysqld-error-while-loading-shared-l/images/img_001_56b2513802b5.png)

检查是否安装libaio

```text
rpm -qa|grep libaio
```

若不存在，安装这个包即可

```text
yum install  libaio-devel.x86_64
```

![](/imported/posts/2020-12-26-14192610-1cb304c8-阿里云centos7-安装mysql5-7-报错-mysqld-error-while-loading-shared-l/images/img_002_3362e5f5cdf1.png)
