{

  "title": "application.properties数据库连接字符串",
  "date": "2020-07-15",
  "description": "application.properties数据库连接字符串",
  "tags": [
    "配置文件"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13308835.html"

}

```text
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/cybclass?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=root
# 使用阿里巴巴druid数据源，默认使用自带
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
#开启控制台打印sql
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```
