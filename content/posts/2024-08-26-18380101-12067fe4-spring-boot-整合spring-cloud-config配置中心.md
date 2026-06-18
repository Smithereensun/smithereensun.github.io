{

  "title": "spring boot 整合spring cloud config配置中心",
  "date": "2024-08-26",
  "description": "创建2个项目 springboot-cloud-config（作配置中心） springboot-cloud-client（客户端） springboot-cloud-config（工程） 注意：2个项目springboot版本：2.4.0** 添加依赖 配置文件 启动配置中心服务 启动类上加：@E",
  "tags": [
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/18380101/spring-cloud-config"

}

# 创建2个项目

- springboot-cloud-config（作配置中心）
- springboot-cloud-client（客户端）

# springboot-cloud-config（工程）

**注意：2个项目springboot版本：2.4.0**

## 添加依赖

```text
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-config-server</artifactId>
            <version>3.0.0</version>
        </dependency>
```

## 配置文件

```text
spring.application.name=springboot-cloud-config
server.port=13000

# 对应gitee上的项目
spring.cloud.config.server.git.uri=https://gitee.com/xxxxx/cloud-config
# 扫码路径
spring.cloud.config.server.git.search-paths=/**
# 默认分支
spring.cloud.config.server.git.default-label=master
# 账号
spring.cloud.config.server.git.username=137XXXX1710
# 密码
spring.cloud.config.server.git.password=XXXX
```

![](/imported/posts/2024-08-26-18380101-12067fe4-spring-boot-整合spring-cloud-config配置中心/images/img_001_08ef4dbcd54d.png)

## 启动配置中心服务

　　启动类上加：@EnableConfigServer

![](/imported/posts/2024-08-26-18380101-12067fe4-spring-boot-整合spring-cloud-config配置中心/images/img_002_86316c3862b1.png)

# springboot-config-client（客户端）

## 添加依赖

```text
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-config</artifactId>
            <version>3.0.0</version>
        </dependency>

        <!-- bootstrap.yml不生效问题 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-bootstrap</artifactId>
            <version>3.1.3</version>
        </dependency>
```

## 配置文件

```text
# bootstrap.yml

spring:
  application:
    name: app
  cloud:
    config:
#      label: master
      # gitee中的配置文件环境名称
      profile: dev
      # spring cloud config的地址
      uri: http://localhost:13000
      # 对应服务应用名
      name: app
# 上述配置去到gitee中找：app-dev.properties文件
server:
  port: 9999
```

## 接口

```text
@RestController
public class HiController {
    @Value("${sso.name}")
    private String ssoName;

    @GetMapping("hi")
    public Object hi(){
        System.out.println(System.currentTimeMillis());
        return ssoName;
    }
}
```

## 请求接口

```text
127.0.0.1:10086/hi
```

# 项目源码地址

```text
https://gitee.com/yenbin_chen/spring-cloud-config
```
