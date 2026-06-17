{

  "title": "新版SpringBoot-Spring-Mybatis事务控制",
  "date": "2020-07-16",
  "description": "快速创建SpringBoot+Spring+Mybatis项目 https://start.spring.io 删除pom中mysql依赖的runtime pom.xml中添加druid依赖 数据库连接配置文件 application.properties 启动类上添加扫描注解 UserContro",
  "tags": [
    "ssm",
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13311267.html"

}

# 快速创建SpringBoot+Spring+Mybatis项目

https://start.spring.io

![](/imported/posts/2020-07-16-13311267-340b3bcd-新版springboot-spring-mybatis事务控制/images/img_001_6f3355d030cb.png)

## 删除pom中mysql依赖的runtime

![](/imported/posts/2020-07-16-13311267-340b3bcd-新版springboot-spring-mybatis事务控制/images/img_002_eb64dffe5bf4.png)

### pom.xml中添加druid依赖

```text
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.23</version>
        </dependency>
```

## 数据库连接配置文件

application.properties

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

## 启动类上添加扫描注解

![](/imported/posts/2020-07-16-13311267-340b3bcd-新版springboot-spring-mybatis事务控制/images/img_003_8d7804e9189c.png)

### UserController.java

```text
package net.ybclass.demo.controller;

import net.ybclass.demo.domain.User;
import net.ybclass.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/user")
public class UserController {
    @Autowired(required = false)
    private UserService userService;
    @RequestMapping("save")
    public Object save(){
        User user=new User();
        user.setId(11);
        user.setName("cyb");
        user.setPwd("423");
        user.setPhone("123456789");
        userService.save(user);
        return user;
    }
}
```

### User.java

```text
package net.ybclass.demo.domain;

public class User {
    private int id;
    private String name;
    private String pwd;
    private String phone;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getPwd() {
        return pwd;
    }

    public void setPwd(String pwd) {
        this.pwd = pwd;
    }
}
```

### UserMapper.java

```text
package net.ybclass.demo.mapper;

import net.ybclass.demo.domain.User;
import org.apache.ibatis.annotations.Insert;
import org.springframework.stereotype.Repository;

@Repository //让spring扫描到
public interface UserMapper {
    @Insert("INSERT INTO user (name,pwd,phone) VALUES (#{name},#{pwd},#{phone})")
    int save(User user);
}
```

### UserService.java

```text
package net.ybclass.demo.service;

import net.ybclass.demo.domain.User;

public interface UserService {
    int save(User user);
}
```

### UserServicceImpl.java

```text
package net.ybclass.demo.service.impl;

import net.ybclass.demo.domain.User;
import net.ybclass.demo.mapper.UserMapper;
import net.ybclass.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service //给Spring扫描
public class UserServiceImpl implements UserService {
    @Autowired(required = false)
    private UserMapper userMapper;
    @Override
    public int save(User user) {

        return userMapper.save(user);
    }
}
```

## 演示

![](/imported/posts/2020-07-16-13311267-340b3bcd-新版springboot-spring-mybatis事务控制/images/img_004_b963f0829675.png)

## 开始事务

在启动类上加注解：@EnableTransactionManagement

![](/imported/posts/2020-07-16-13311267-340b3bcd-新版springboot-spring-mybatis事务控制/images/img_005_f5caa9f49f28.png)

在业务类上加：@Transactional

![](/imported/posts/2020-07-16-13311267-340b3bcd-新版springboot-spring-mybatis事务控制/images/img_006_8f8f275a1974.png)
