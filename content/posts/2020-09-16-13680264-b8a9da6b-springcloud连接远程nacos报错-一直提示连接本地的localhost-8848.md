{

  "title": "SpringCloud连接远程nacos报错，一直提示连接本地的localhost:8848",
  "date": "2020-09-16",
  "description": "application.properties bootstrap.properties 在resources下创建:bootstrap.properties",
  "tags": [
    "Spring Cloud",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13680264.html"

}

# application.properties

```text
spring.cloud.nacos.discovery.server-addr=xxx.xxx.xxx.xxx:8848
spring.application.name=服务名
```

# bootstrap.properties

在resources下创建:bootstrap.properties

```text
#nacos config
spring.cloud.nacos.config.server-addr=xxx.xxx.xxx.xxx:8848
spring.application.name=服务名
```
