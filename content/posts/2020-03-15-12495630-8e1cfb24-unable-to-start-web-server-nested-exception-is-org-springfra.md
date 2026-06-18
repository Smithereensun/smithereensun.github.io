{

  "title": "Unable to start web server; nested exception is org.springframework.context.ApplicationContextException",
  "date": "2020-03-15",
  "description": "项目报错：Unable to start web server; nested exception is org.springframework.context.ApplicationContextException 解决方案一 解决方案二 出现了这个异常， 只要再pom文件里加上对应的 conta",
  "tags": [
    "Spring",
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12495630.html"

}

项目报错：Unable to start web server; nested exception is org.springframework.context.ApplicationContextException

## 解决方案一

```text
<!-- 使用嵌入式Jetty作为web container -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-tomcat</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
```

## 解决方案二

出现了这个异常，
只要再pom文件里加上对应的 container deps: 

```text
<dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-jetty</artifactId>
</dependency>
```
