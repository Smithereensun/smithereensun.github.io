{

  "title": "SpirngBoot整合MybatisPlus 附源码",
  "date": "2020-09-24",
  "description": "项目搭建 目录结构 pom.xml application.properties 注入分页 MybatisPlusConfig.java dao层 NbaTestDao.java 实体类 NbaTest.java 启动类上扫描dao 数据库表字段 测试类 搞定~",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13722629.html"

}

# 项目搭建

## 目录结构

![](/imported/posts/2020-09-24-13722629-adc287a1-spirngboot整合mybatisplus-附源码/images/img_001_69070e7c84a1.png)

## pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.3.4.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.cyb</groupId>
    <artifactId>springboot-mybatisplus</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springboot-mybatisplus</name>
    <description>springboot整合mybatisplus</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <!--SpringBoot依赖开始-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.junit.vintage</groupId>
                    <artifactId>junit-vintage-engine</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <!--SpringBoot依赖结束-->
        <!--mysql依赖开始-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!--mysql依赖结束-->
        <!--MybatisPlus依赖开始-->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.4.0</version>
        </dependency>
        <!--MybatisPlus依赖结束-->
        <!--Junit测试依赖开始-->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
        </dependency>
        <!--Junit测试依赖结束-->
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

## application.properties

```text
server.port=8080

#mysql
spring.datasource.url=jdbc:mysql://localhost:3306/nba?useUnicode=true&characterEncoding=utf8
spring.datasource.username=root
spring.datasource.password=root
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
#mybatis-plus
mybatis-plus.mapper-locations=classpath:com/mht/springbootmybatisplus/mapper/xml/*.xml
mybatis-plus.type-aliases-package=com.mht.springbootmybatisplus.entity
mybatis-plus.configuration.map-underscore-to-camel-case: true
```

## 注入分页

MybatisPlusConfig.java

```text
package com.cyb.config;

import com.baomidou.mybatisplus.extension.plugins.PaginationInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.springframework.boot.autoconfigure.condition.ConditionalOnClass;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @ClassName：MybatisPlusConfig
 * @Description：分页配置
 * @Author：chenyb
 * @Date：2020/9/24 9:31 上午
 * @Versiion：1.0
 */
@Configuration
@ConditionalOnClass(value = PaginationInnerInterceptor.class)
public class MybatisPlusConfig {
    @Bean
    public PaginationInterceptor paginationInterceptor() {
        PaginationInterceptor paginationInterceptor = new PaginationInterceptor();
        return paginationInterceptor;
    }
}
```

## dao层

NbaTestDao.java

```text
package com.cyb.dao;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.cyb.entity.NbaTest;

public interface NbaTestDao extends BaseMapper<NbaTest> {
}
```

## 实体类

NbaTest.java

```text
package com.cyb.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;

import java.util.Date;

/**
 * @ClassName：NbaPlayer
 * @Description：实体类
 * @Author：chenyb
 * @Date：2020/9/23 4:29 下午
 * @Versiion：1.0
 */
//表名
@TableName("nba_test")
public class NbaTest {
    //表字段与实体类对应关系
    @TableField("id")
    @TableId
    private int id;
    @TableField("name")
    private String name;
    @TableField("age")
    private int age;
    @TableField("create_date")
    private Date createDate;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public Date getCreateDate() {
        return createDate;
    }

    public void setCreateDate(Date createDate) {
        this.createDate = createDate;
    }

    @Override
    public String toString() {
        return "NbaTest{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", age=" + age +
                ", createDate=" + createDate +
                '}';
    }
}
```

![](/imported/posts/2020-09-24-13722629-adc287a1-spirngboot整合mybatisplus-附源码/images/img_002_af621cf0a6f3.png)

## 启动类上扫描dao

![](/imported/posts/2020-09-24-13722629-adc287a1-spirngboot整合mybatisplus-附源码/images/img_003_67dd2b0bf8a1.png)

## 数据库表字段

![](/imported/posts/2020-09-24-13722629-adc287a1-spirngboot整合mybatisplus-附源码/images/img_004_cee98326a88c.png)

## 测试类

```text
package com.cyb;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.cyb.dao.NbaTestDao;
import com.cyb.entity.NbaTest;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import java.util.Date;
import java.util.List;

@RunWith(SpringRunner.class)
@SpringBootTest(classes = StartApplication.class)
public class Test01 {
    @Autowired
    private NbaTestDao nbaTestDao;

    /**
     * 添加
     */
    @Test
    public void add() {
        for (int x=0;x<100;x++){
            NbaTest nbaTest=new NbaTest();
            nbaTest.setAge(25+x);
            nbaTest.setCreateDate(new Date());
            nbaTest.setName("陈彦斌===="+x);
            nbaTestDao.insert(nbaTest);
        }
        System.out.println("ok~~~~~~~~~");
    }

    /**
     * 更新
     */
    @Test
    public void update(){
        NbaTest nbaTest=new NbaTest();
        nbaTest.setId(2);
        nbaTest.setName("修改");
        nbaTest.setAge(0);
        nbaTestDao.updateById(nbaTest);
        System.out.println("update=====");
    }

    /**
     * 删除
     */
    @Test
    public void delete(){
        nbaTestDao.deleteById(2);
        System.out.println("delete==========");
    }

    /**
     * 查询
     */
    @Test
    public void selete(){
        QueryWrapper<NbaTest> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("name","陈彦斌====6");
        List<NbaTest> nbaTests = nbaTestDao.selectList(queryWrapper);
        System.out.println(nbaTests);
    }

    /**
     * 分页查询
     */
    @Test
    public void seleteByPage(){
        int start=2;
        int end=5;
        IPage<NbaTest> userPage=new Page<>(start,end);
        QueryWrapper<NbaTest> queryWrapper = new QueryWrapper<>();
        List<NbaTest> records = nbaTestDao.selectPage(userPage, queryWrapper).getRecords();
        for (NbaTest nt:records){
            System.out.println(nt);
        }
    }
}
```

搞定~
