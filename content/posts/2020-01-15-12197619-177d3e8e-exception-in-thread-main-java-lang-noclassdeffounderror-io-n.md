{

  "title": "Exception in thread \"main\" java.lang.NoClassDefFoundError: io/netty/channel/EventLoopGroup",
  "date": "2020-01-15",
  "description": "最近在学习dubbo，跟着教程做，但是运行时报错，需要添加netty依赖",
  "tags": [
    "Java"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12197619.html"

}

最近在学习dubbo，跟着教程做，但是运行时报错，需要添加netty依赖

```text
<dependency>
             <groupId>io.netty</groupId>
            <artifactId>netty-all</artifactId>
            <version>4.1.32.Final</version>
        </dependency>
```
