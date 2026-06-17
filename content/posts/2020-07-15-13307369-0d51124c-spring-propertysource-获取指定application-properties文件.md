{

  "title": "Spring PropertySource，获取指定application.properties文件",
  "date": "2020-07-15",
  "description": "@PropertySource注解的使用 @PropeertySource，指定加载配置文件 配置文件映射到实体类 使用@Value映射到具体的java属性 CustomConfig.java config.properties VideoOrder.java 验证",
  "tags": [
    "Spring",
    "Spring Boot"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13307369.html"

}

# @PropertySource注解的使用

- @PropeertySource，指定加载配置文件

  - 配置文件映射到实体类

- 使用@Value映射到具体的java属性

## CustomConfig.java

```text
package net.cybclass.sp.aop;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource(value = "classpath:config.properties")
public class CustomConfig {
    @Value("${server.host}")
    private String host;
    @Value("${server.port}")
    private int port;

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    @Override
    public String toString() {
        return "CustomConfig{" +
                "host='" + host + '\'' +
                ", port=" + port +
                '}';
    }
}
```

## config.properties

```text
server.host=128.0.0.1
server.port=8080
```

## VideoOrder.java

![](/imported/posts/2020-07-15-13307369-0d51124c-spring-propertysource-获取指定application-properties文件/images/img_001_ddc618c76e41.png)

## 验证

![](/imported/posts/2020-07-15-13307369-0d51124c-spring-propertysource-获取指定application-properties文件/images/img_002_73e7b5fe6dcb.png)
