{

  "title": "Failure to transfer org.springframework:spring-jcl:jar:5.0.7.RELEASE from",
  "date": "2019-10-19",
  "description": "错误信息： Failure to transfer org.springframework.boot:spring-boot-maven-plugin:pom:1.5.4.RELEASE from https://repo.maven.apache.org/maven2 was cached in ",
  "tags": [
    "JAVA"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11706243.html"

}

错误信息：

Failure to transfer org.springframework.boot:spring-boot-maven-plugin:pom:1.5.4.RELEASE from https://repo.maven.apache.org/maven2 was cached in the local repository, resolution will not be reattempted until the update interval of central has elapsed or updates are forced. Original error: Could not transfer artifact 
org.springframework.boot:spring-boot-maven-plugin:pom:1.5.4.RELEASE from/to central (https://repo.maven.apache.org/maven2): repo.maven.apache.org pom.xml

　　原本代码并没出错，但是在导入项目到新环境下后，出现了这种错误。发生的问题根本原因 在于 网络环境导致 依赖的包在下载的过程中出现的异常中断，导致引用资源损坏

解决办法：

cmd中：

```text
cd %userprofile%\.m2\repository
for /r %i in (*.lastUpdated) do del %i
```

然后在eclipse中右键，选择Maven - >“Update Project”，确保勾选“Update Dependencies”，然后点确定

解决方法原文：

[https://stackoverflow.com/questions/5074063/maven-error-failure-to-transfer](https://stackoverflow.com/questions/5074063/maven-error-failure-to-transfer)
