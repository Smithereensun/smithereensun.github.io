{

  "title": "解决Maven无法下载fastdfs-client-java依赖，Dependency 'org.csource:fastdfs-client-java:1.27-SNAPSHOT' not found.",
  "date": "2020-05-05",
  "description": "因为fastdfs-client-java-1.27-SNAPSHOT.jar这个依赖包在maven中央仓库是没有的， 需要自己编译源码成jar本地安装到maven 的本地仓库，安装完以后就能正常引用了（注意：本地必须安装了Maven，并配置好Maven环境变量） 下载fastdfs-client-",
  "tags": [
    "cnblogs"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12831553.html"

}

因为fastdfs-client-java-1.27-SNAPSHOT.jar这个依赖包在maven中央仓库是没有的，

需要自己编译源码成jar本地安装到maven 的本地仓库，安装完以后就能正常引用了（注意：本地必须安装了Maven，并配置好Maven环境变量）

```text
<dependency>
      <groupId>org.csource</groupId>
      <artifactId>fastdfs-client-java</artifactId>
      <version>1.27-SNAPSHOT</version>
</dependency>
```

### 1.下载fastdfs-client-java开发工具包

**https://github.com/happyfish100/fastdfs-client-java**

![](/imported/posts/2020-05-05-12831553-dc9c0607-解决maven无法下载fastdfs-client-java依赖-dependency-org-csource-fast/images/img_001_4d8cea0dc967.png)

### 2.需要把fastdfs-client-java开发工具包打包到本地的Maven仓库

　　2.1解压fastdfs-client-java-master

　　2.2进入fastdfs-client-java目录，在此处打开命令窗口 cmd 

![](/imported/posts/2020-05-05-12831553-dc9c0607-解决maven无法下载fastdfs-client-java依赖-dependency-org-csource-fast/images/img_002_3761b6b90b47.png)

　　2.3输入 mvn clean install

![](/imported/posts/2020-05-05-12831553-dc9c0607-解决maven无法下载fastdfs-client-java依赖-dependency-org-csource-fast/images/img_003_c44342fe986b.png)

### 3.构建一小会，如出现以下。则成功把fastdfs-client-java打包到本地的Maven仓库

![](/imported/posts/2020-05-05-12831553-dc9c0607-解决maven无法下载fastdfs-client-java依赖-dependency-org-csource-fast/images/img_004_b62150bbe681.png)

![](/imported/posts/2020-05-05-12831553-dc9c0607-解决maven无法下载fastdfs-client-java依赖-dependency-org-csource-fast/images/img_005_37e65ff22fa9.png)

至此，更新项目Maven，pom.xml文件就不会出现找不到fastdfs-client-java依赖了。（成功导入fastdfs-client-java依赖）

![](/imported/posts/2020-05-05-12831553-dc9c0607-解决maven无法下载fastdfs-client-java依赖-dependency-org-csource-fast/images/img_006_249bfa1fe01d.png)
