{

  "title": "微服务框架-Spring Cloud",
  "date": "2020-04-18",
  "description": "Spring Cloud入门 微服务与微服务架构 微服务架构是一种新型的系统架构。其设计思路是，将单体架构系统拆分为多个可以相互调用、配合的独立运行的小程序。这每个小程序对整体系统所提供的功能就称为微服务。 由于每个微服务都具有独立运行的，所以每个微服务都独立占用一个进程。微服务间采用轻量级的HTT",
  "tags": [
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12608621.html"

}

# Spring Cloud入门

## 微服务与微服务架构

　　微服务架构是一种新型的系统架构。其设计思路是，将单体架构系统拆分为多个可以相互调用、配合的独立运行的小程序。这每个小程序对整体系统所提供的功能就称为微服务。

　　由于每个微服务都具有独立运行的，所以每个微服务都独立占用一个进程。微服务间采用轻量级的HTTP RESTFUL协议通信。每个微服务程序不受编程语言的限制，整个系统关心的是微服务程序所提供的具体服务，并不关心其具体的实现。每个微服务可以有自己独立的数据库。即可以操作自己的独立数据，也可以操作整体系统的数据库。

## Spring Cloud简介

### 百度百科介绍

　　Spring Cloud是一系列框架的有序集合。它利用Spring Boot的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中心、消息总线、负载均衡、断路器、数据监控等，都可以用Spring Boot的开发风格做到一键启动和部署。Spring Cloud并没有重复制造轮子，它只是将各家公司开发的比较成熟、经得起实际考验的服务框架组合起来，通过Spring Boot风格进行再封装屏蔽了复杂的配置和实现原理，最终给开发者流出了一套简单易懂、易部署和易维护的分布式系统开发工具包。

### Spring Cloud中文网

https://www.springcloud.cc/

### Spring Cloud中国社区

http://www.springcloud.cn/

## 服务提供者项目

　　本示例使用Spring的RestTemplate实现消费者对提供者的调用，并未使用到Spring Cloud，但其为后续Spring Cloud的运行测试环境。使用MySql数据库，使用Spring Data JPA作为持久层技术。

### 创建工程

![](./images/images/img_001_785d5a9993ff.png)

![](./images/images/img_002_7d25f6c3c687.png)

![](./images/images/img_003_ef1f87788ba3.png)

### 添加Druid依赖

pom.xml

```text
        <!--Druid依赖-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.10</version>
        </dependency>
```

### 定义bean包(存放实体类)

　　Controller处理器方法的返回值是作为JSON数据响应给浏览器的；这个数据转换工作是由SpringMvc的HttpMessageConverter接口完成的。

　　注意，**默认情况**下，**Hibernate**对所有对象的查询**采用了延迟加载策略**，这里要添加**@JsonIgnoreProperties注解**，将延迟加载及相关的属性忽略，**即不采用延迟加载策略**。若需要延迟加载，可在spring boot配置文件中专门配置。

Depart.java

```text
package com.cyb.provider.bean;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Data
@Entity(name = "t_depart") //实体类和"t_depart"映射关系；不写代表实体类和同名表映射
@JsonIgnoreProperties({"hibernateLazyInitializer","handler","fieldHandler"}) //延迟加载；第一个参数，延迟加载初始化器；第2、3，处理属性和字段
public class Depart {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) //自动生成数据库，自增ID
    private Integer id;
    private String name;
    private String dbase;
}
```

### 定义repository包(存放dao)

DepartRepository.java

```text
package com.cyb.provider.repository;

import com.cyb.provider.bean.Depart;
import org.springframework.data.jpa.repository.JpaRepository;

//泛型：第一个指明操作实体类是谁；第二个当前数据表的自增列类型
public interface DepartRepository extends JpaRepository<Depart,Integer> {

}
```

**注意：定义的是接口**

### 定义service包

DepartService.java(业务接口)

```text
package com.cyb.provider.Service;

import com.cyb.provider.bean.Depart;
import java.util.List;

/**
 * 业务接口
 */
public interface DepartService {
    /**
     * 增加
     * @param depart
     * @return
     */
    boolean saveDepart(Depart depart);

    /**
     * 删除
     * @param id
     * @return
     */
    boolean removeDepartById(int id);

    /**
     * 修改
     * @param depart
     * @return
     */
    boolean modifyDepart(Depart depart);

    /**
     * 查询id
     * @param id
     * @return
     */
    Depart getDepartById(int id);

    /**
     * 查询所有
     * @return
     */
    List<Depart> listAllDeparts();
}
```

DepartServiceImpl.java(业务接口实现类)

```text
package com.cyb.provider.Service;

import com.cyb.provider.bean.Depart;
import com.cyb.provider.repository.DepartRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
@Service
public class DepartServiceImpl implements DepartService {
    @Autowired
    private DepartRepository repository;

    @Override
    public boolean saveDepart(Depart depart) {
        //返回结果有值，操作成功；没值失败，操作失败
        return repository.save(depart) == null ? false : true;
    }

    @Override
    public boolean removeDepartById(int id) {
        //对于deleteById方法，若DB中存在该id，一定能删除；不存在该id，抛异常
        if (repository.existsById(id)) {
            repository.deleteById(id);
            return true;
        }
        return false;
    }

    @Override
    public boolean modifyDepart(Depart depart) {
        //返回结果有值，操作成功；没值失败，操作失败
        return repository.save(depart) == null ? false : true;
    }

    @Override
    public Depart getDepartById(int id) {
        //getOne()方法：若其指定的id不存在，该方法将抛出异常
        if (repository.existsById(id)){
            return repository.getOne(id);
        }
        Depart depart=new Depart();
        depart.setName("not this depart");
        return depart;
    }

    @Override
    public List<Depart> listAllDeparts() {
        return repository.findAll();
    }
}
```

### 定义controller包(控制器)

DepartController.java

```text
package com.cyb.provider.controller;

import com.cyb.provider.Service.DepartService;
import com.cyb.provider.bean.Depart;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("/provider/depart")
@RestController
public class DepartController {

    @Autowired
    private DepartService service;

    @PostMapping("/save")
    public boolean saveHandle(@RequestBody Depart depart) {
        return service.saveDepart(depart);
    }

    @DeleteMapping("/del/{id}")
    public boolean deleteHandle(@PathVariable("id") int id) {
        return service.removeDepartById(id);
    }

    @PutMapping("/update")
    public boolean updateHandle(@RequestBody Depart depart) {
        return service.modifyDepart(depart);
    }

    @GetMapping("/get/{id}")
    public Depart getHandle(@PathVariable("id") int id) {
        return service.getDepartById(id);
    }

    @GetMapping("/list")
    public List<Depart> listHandle() {
        return service.listAllDeparts();
    }
}
```

补充：

```text
1、@PathVariable：获取请求路径中的占位符
2、@RestController=@ResponseBody ＋ @Controller
    2.1 如果只是使用@RestController注解Controller，则Controller中的方法无法返回jsp页面，或者html，配置的视图解析器 InternalResourceViewResolver不起作用，返回的内容就是Return 里的内容。
    2.2 如果需要返回到指定页面，则需要用 @Controller配合视图解析器InternalResourceViewResolver才行。
    如果需要返回JSON，XML或自定义mediaType内容到页面，则需要在对应的方法上加上@ResponseBody注解。
```

### 配置文件

application.properties

```text
# 端口号
server.port=8081
# 应用启动是否自动创建表，默认为false
spring.jpa.generate-ddl=true
# 是否在控制台显示sql语句，默认为false
spring.jpa.show-sql=true
# 应用启动时设置不重新建表
spring.jpa.hibernate.ddl-auto=none
# 数据类型
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
spring.datasource.url=jdbc:mysql://localhost:3306/demo?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=root

# 设置日志输出格式
logging.pattern.console=level-%level%msg%n
# Spring Boot启动时的日志级别
logging.level.root=info
# hibernate运行时的日志级别
logging.level.org.hibernate=info
# 在show-sql为true时显示sql中的动态参数值
logging.level.org.hibernate.type.descriptor.sql.BasicBinder=trace
# 在show-sql为true时显示查询结果
logging.level.org.hibernate.type.descriptor.sql.BasicExtractor=trace
# 控制自己代码运行时显示的日志级别
logging.level.com.cyb.provider=debug
```

### 项目结构图

![](./images/images/img_004_e8e61d42ea48.png)

## 服务消费者项目

### 创建工程

![](./images/images/img_005_4905accaa9d7.png)

![](./images/images/img_006_d5008208c4b4.png)

### 定义bean包

Depart.java

```text
package com.com.consumer.bean;

import lombok.Data;

@Data
public class Depart {
    private Integer id;
    private String name;
    private String dbase;
}
```

### 定义codeconfig包

DepartCodeConfig.java

```text
package com.com.consumer.codeconfig;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class DepartCodeConfig {
    @Bean
    public RestTemplate restTemplate(){
        return new RestTemplate();
    }
}
```

### 定义controller包

DepartController.java

```text
package com.com.consumer.controller;

import com.com.consumer.bean.Depart;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@RestController
@RequestMapping("/consumer/depart")
public class DepartController {
    @Autowired
    private RestTemplate restTemplate;
    @PostMapping("/save")
    public boolean saveHandle(Depart depart) {
        String url="http://localhost:8081/provider/depart/save";
        return restTemplate.postForObject(url,depart,Boolean.class);
    }

    @DeleteMapping("/del/{id}")
    public void deleteHandle(@PathVariable("id") int id) {
        String url="http://localhost:8081/provider/depart/del/"+id;
        restTemplate.delete(url);
    }

    @PutMapping("/update")
    public void updateHandle(@RequestBody Depart depart) {
        String url="http://localhost:8081/provider/depart/update";
        restTemplate.put(url,depart);
    }

    @GetMapping("/get/{id}")
    public Depart getHandle(@PathVariable("id") int id) {
        String url="http://localhost:8081/provider/depart/get/"+id;
        return restTemplate.getForObject(url,Depart.class);
    }

    @GetMapping("/list")
    public List<Depart> listHandle() {
        String url="http://localhost:8081/provider/depart/list";
        return restTemplate.getForObject(url,List.class);
    }
}
```

### application.properties

![](./images/images/img_007_ea635a994cbb.png)

### 项目结构图

![](./images/images/img_008_a6e9cec39666.png)

## Restlet Client测试

安装教程：[点我直达](https://www.cnblogs.com/chenyanbin/p/12620116.html)

![](./images/images/img_009_0857c0cfb50e.png)

# 微服务中心Eureka

## github

[点我直达](https://github.com/Netflix/eureka)

## 创建Eureka服务中心

### 总步骤

1. 导入Eureka依赖
2. 在配置文件中配置EurekaServer
3. 在启动类中添加注解@EnableEurekaServer开启Eureka

### 创建工程

![](./images/images/img_010_aecbb65192fc.png)

![](./images/images/img_011_570567eb5e41.png)

![](./images/images/img_012_17254728e492.png)

### 导入依赖(注意)

　　注意，这里要导入的依赖并非Spring Cloud工程直接的依赖。而是由Eureka Server所依赖的，JDK9之前包含其所需要的依赖，JDK9之后，Eureka所需的依赖被踢出了,需要单独添加依赖。**JDK9之前的不需要以下依赖**，我这边**演示用的JDK13**，所以需要添加以下依赖。

pom.xml

```text
        <!--Eureka添加依赖开始-->
        <dependency>
            <groupId>javax.xml.bind</groupId>
            <artifactId>jaxb-api</artifactId>
            <version>2.3.0</version>
        </dependency>

        <dependency>
            <groupId>com.sun.xml.bind</groupId>
            <artifactId>jaxb-core</artifactId>
            <version>2.3.0</version>
        </dependency>

        <dependency>
            <groupId>com.sun.xml.bind</groupId>
            <artifactId>jaxb-impl</artifactId>
            <version>2.3.0</version>
        </dependency>

        <dependency>
            <groupId>javax.activation</groupId>
            <artifactId>activation</artifactId>
            <version>1.1.1</version>
        </dependency>
        <!--Eureka添加依赖结束-->
```

### 设置配置文件

application.properties

```text
server.port=8083
# 配置Eureka，开始
# 配置Eureka主机名
eureka.instance.hostname=localhost
# 指定当前主机是否需要向注册中心注册(不用，因为当前主机是Server，不是Client)
eureka.client.register-with-eureka=false
# 指定当前主机是否需要获取注册信息(不用，因为当前主机是Server，不是Client)
eureka.client.fetch-registry=false
# ${eureka.instance.hostname}和${server.port}，动态引入变量的值
# 暴露服务中心地址
eureka.client.service-url.defaultZone=http://${eureka.instance.hostname}:${server.port}/eureka
```

### 启动类上添加注解

![](./images/images/img_013_076a3d67b8f9.png)

### 项目启动测试

![](./images/images/img_014_21b785c64114.gif)

### 项目结构图

![](./images/images/img_015_64d00f09b35f.png)

## 创建提供者工程2

### 总步骤

1. 添加Eureka客户端依赖
2. 在配置文件中指定要注册的Eureka注册中心
3. 在启动类上添加@EnableEurekaClient注解

### 创建工程

　　拷贝一份：01-provider-8081，重命名为：02-provider-8081

![](./images/images/img_016_599fb430a996.gif)

![](./images/images/img_017_a11b092663aa.gif)

### 添加依赖

![](./images/images/img_018_b47ad730aa3f.png)

```text
    <dependencies>
        <!--Eureka客户端依赖-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
            <version>2.2.2.RELEASE</version>
        </dependency>
    </dependencies>

    <!-- Eureka依赖管理模块 -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Finchley.SR1</version>
                <type>pom</type>
            </dependency>
        </dependencies>
    </dependencyManagement>
```

### 修改配置文件

![](./images/images/img_019_cc7329d5a0b9.png)

![](./images/images/img_020_6e0ac86e6175.png)

### 修改客户端在注册中心名称(可忽略)

![](./images/images/img_021_f8cfe4b54c91.png)

## actuator完善微服务info

### 问题展示

![](./images/images/img_022_c87ba6c80006.gif)

　　可以看出，**点击**微服务状态的**超链接**，可以**看到404错误页**，是因为**在提供者配置文件中**，**未设置actuator的info监控终端所致**。

### 添加提供者依赖

![](./images/images/img_023_850a1c98bafb.png)

```text
        <!-- actuator依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
```

### 添加info配置文件

![](./images/images/img_024_6d1233214ac2.png)

### 测试

![](./images/images/img_025_2517d9265b9d.gif)

### 注意!!

　　这里需要修改提供者2里的pom.xml的版本(**我已经将上面的版本修改过，这里可忽略**)，由于依赖问题导致的，解决方法，请看我另外一篇博客：[点我直达](https://www.cnblogs.com/chenyanbin/p/12658016.html)，这里我们只需要此处的版本号即可

![](./images/images/img_026_695af3726a6f.png)

完整pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.6.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.cyb</groupId>
    <artifactId>02-provider-8081</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>02-provider-8081</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>

        <!-- actuator依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>

        <!--Druid依赖-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.10</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <optional>true</optional>
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
        <!--Eureka客户端依赖-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
            <version>2.2.2.RELEASE</version>
            <!-- 之前版本 -->
            <!-- <version>2.0.2.RELEASE</version> -->

        </dependency>

    </dependencies>

    <!-- Eureka依赖管理模块 -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Finchley.SR1</version>
                <type>pom</type>
            </dependency>
        </dependencies>
    </dependencyManagement>
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

## 创建消费者工程2

**消费者**将使**用提供者暴露的服务名称**(spring.application.name)**来消费**服务。

![](./images/images/img_027_0ba3d1ff2d64.png)

### 总步骤

1. 添加Eureka客户端依赖
2. 在配置文件中指定Eureka注册中心
3. 在DepartCodeConfig类中添加@LoadBalanced注解
4. 在启动类上添加@EnableEurekaClient注解

### 创建工程

　　复制01-consumer-8082，重复名为02-consumer-8082，具体步骤，详见上面提供者创建工程方式。

### 添加依赖

pom.xml

```text
        <!--Eureka客户端依赖-->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
            <version>2.2.2.RELEASE</version>
        </dependency>

    <!-- Eureka依赖管理模块 -->
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>org.springframework.cloud</groupId>
                <artifactId>spring-cloud-dependencies</artifactId>
                <version>Finchley.SR1</version>
                <type>pom</type>
            </dependency>
        </dependencies>
    </dependencyManagement>
```

![](./images/images/img_028_990c175f65ea.png)

```text
        <!-- 若配置info，需添加以下依赖，不配置可忽略，案例中我是加了！！！ -->
        <!-- actuator依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
```

### 修改配置文件

![](./images/images/img_029_15e02d4050a7.png)

```text
server.port=8082

# 指定当前微服务对外(消费者)暴露的名称
spring.application.name=cyb-consumer-depart

# 指定Eureka注册中心
eureka.client.service-url.defaultZone=http://localhost:8083/eureka
```

### 添加@LoadBalanced注解

![](./images/images/img_030_5092743b57b5.png)

### 启动类上添加注解

![](./images/images/img_031_97f84c2c2f2f.png)

### 项目启动

![](./images/images/img_032_49e01274edf9.gif)

## 服务发现Discovery

　　即通过“服务发现客户端”读取EurekaServer中的服务列表，获取指定名称的微服务详情。

### 修改处理器

　　在**任何**微服务的**提供者或消费者**处理器中，只要获取到“服务发现Client”，即可读取到Eureka Server的微服务列表。案例中修改02-provider-8081中的处理器类

![](./images/images/img_033_0ddfad30806a.png)

```text
    @GetMapping("/discovery")
    public Object discoveryHandle(){
        // 获取服务注册列表中所有的微服务名称
        List<String> springApplicationNames = client.getServices();
        for (String name:springApplicationNames){
            // 获取提供指定微服务名称的所有提供者主机
            List<ServiceInstance> instances = client.getInstances(name);
            for (ServiceInstance instance:instances){
                String host = instance.getHost();
                int port = instance.getPort();
                System.out.println(MessageFormat.format("host:{0},port:{1}",host,port));
            }
        }
        return springApplicationNames;
    }
```

### 测试

![](./images/images/img_034_49cee2d6e787.gif)

## EurekaServer集群

　　单个EurekaServer 不仅吞吐量有限，还存在单点问题，所以我们会使用EurekaServer集群，这里要搭建的EurekaServer集群中包含3个EurekaServer节点，其端口号分别为8123，8456，8789

### 设置域名

　　由于这些Eureka 在这里都是运行在当前的这一台主机，而Eureka管理页面中显示的仅仅是Eureka主机的域名，不显示端口号，所以为了在Eureka管理页面可以区分Eureka集群中各个主机，我们这里先为每一个Eureka节点设置一个不同的域名。

　　需要修改host文件，为了节点时间，不会的童鞋，请看我另一篇博客有讲解到如何设置host文件：[点我直达](https://www.cnblogs.com/chenyanbin/p/12521296.html)

![](./images/images/img_035_b70983166955.png)

###  复制并修改EurekaServer

　　复制3份01-eurekaserver-8083，并重命名，分别为：02-eurekaserver-8123；02-eurekaserver-8456；02-eurekaserver-8789；

![](./images/images/img_036_78962e4fbac7.png)

### 修改EurekaServer配置文件

![](./images/images/img_037_b22b02b0ca7d.png)

**注：“,”隔开的中间不能有空格！！！集群中3个项目都要相应修改！！！**

### 修改客户端配置

![](./images/images/img_038_d8fd22626e11.png)

### 运行访问

![](./images/images/img_039_d5a31355901e.png)

![](./images/images/img_040_e5103bff47f0.gif)

# 声明式REST客户端OpenFeign

## 创建消费者工程

　　这里无需修改提供者工程，只需修改消费者工程即可。

复制02-consumer-8082，并重命名为03-consumer-feign-8082

![](./images/images/img_041_02ed94227439.png)

## 总步骤

1. 添加openfeign依赖
2. 定义Service接口，并指定其所绑定的微服务
3. 修改处理器，通过Service接口消费微服务
4. 在启动类上添加@EnableFeignClients注解

## 添加依赖

pom.xml

```text
        <!-- openfeign依赖 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
            <version>2.2.2.RELEASE</version>
        </dependency>
```

## 定义Service

![](./images/images/img_042_92ddbf1f95f5.png)

```text
package com.com.consumer.service;

import com.com.consumer.bean.Depart;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * 业务接口
 */
// 指定当前Service所绑定的提供者微服务名称
@FeignClient("cyb-provider-depart")
@RequestMapping("/provider/depart")
public interface DepartService {
    /**
     * 增加
     * @param depart
     * @return
     */
    @PostMapping("/save")
    boolean saveDepart(Depart depart);

    /**
     * 删除
     * @param id
     * @return
     */
    @DeleteMapping("/del/{id}")
    boolean removeDepartById(@PathVariable("id") int id);

    /**
     * 修改
     * @param depart
     * @return
     */
    @PutMapping("/update")
    boolean modifyDepart(Depart depart);

    /**
     * 查询id
     * @param id
     * @return
     */
    @GetMapping("/get/{id}")
    Depart getDepartById(@PathVariable("id") int id);

    /**
     * 查询所有
     * @return
     */
    @GetMapping("/list")
    List<Depart> listAllDeparts();
}
```

## 修改处理器

![](./images/images/img_043_f5362b6ba871.png)

```text
package com.com.consumer.controller;

import com.com.consumer.bean.Depart;
import com.com.consumer.service.DepartService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/consumer/depart")
public class DepartController {

    @Autowired(required = false)
    private DepartService service;
    @PostMapping("/save")
    public boolean saveHandle(Depart depart) {
        return service.saveDepart(depart);
    }

    @DeleteMapping("/del/{id}")
    public boolean deleteHandle(@PathVariable("id") int id) {
        return service.removeDepartById(id);
    }

    @PutMapping("/update")
    public boolean updateHandle(@RequestBody Depart depart) {
        return service.modifyDepart(depart);
    }

    @GetMapping("/get/{id}")
    public Depart getHandle(@PathVariable("id") int id) {
        return service.getDepartById(id);
    }

    @GetMapping("/list")
    public List<Depart> listHandle() {
        return service.listAllDeparts();
    }
}
```

## 启动类上添加注解

![](./images/images/img_044_5f97310c5100.png)

## 测试

　　这里为了演示方便，不用eureka集群了，效果是一样的

![](./images/images/img_045_1f77340bcd59.png)

　　分别启动：01-eurekaserver-8083；02-provider-8081(**需修改eureka注册中心地址**)；03-consumer-feign-8082(**需修改eureka注册中心地址**)

![](./images/images/img_046_e454602ae7a5.gif)

# Ribbon负载均衡

　　上个例子通过OpenFeign接口来消费微服务，但没体现负载均衡的功能。

## Ribbo负载均衡演示

### 系统结构

　　负载均衡需要搭建出多个服务提供者，搭建系统如下：一个微服务由3个提供者提供，而消费者使用Ribbon对这3个提供者进行负载均衡访问。Ribbon首先会选择同一区域访问量较少的EurekaService，然后再从该EurekaServer中获取到服务列表，然后再根据用户指定的负载均衡策略选择一个服务提供者。

![](./images/images/img_047_810fef49f6b4.png)

### 创建3个数据库

　　分别为：demo1；demo2；demo3

![](./images/images/img_048_e6818873ac11.png)

三个库中，三个表，3条数据

![](./images/images/img_049_627245fbc97c.png)

### 创建3个提供者

　　复制02-provider-8081，并重命名：02-provider-8091；02-provider-8092；02-provider-8093，修改相应端口号，连接的数据库等信息

![](./images/images/img_050_739e96774f4d.png)

### 测试

　　启动依次启动：01-eurekaserver-8083；02-provider-8091；02-provider-8092；02-provider-8093；03-consumer-feign-8082

![](./images/images/img_051_6d237eacd819.gif)

![](./images/images/img_052_6057770015d9.gif)

　　我们发现调用消费者的时候，消费者依次调用提供者1、提供者2、提供者3，这是因为**默认采用负载均衡算法是轮询**，他还**支持其他的算法**。

## 负载均衡算法IRule

　　Ribbon提供了多种负载均衡策略算法，例如**轮询算法**、**随机算法**、**响应时间加权算法**等。默认采用的是轮询算法，也可以指定Ribbon默认算法。

### IRule接口

![](./images/images/img_053_97e5e50f5967.png)

#### choose()方法

　　Ribbon的负载均衡算法需要实现IRule接口，而该接口中的核心方法即choose()方法，即对提供者的选择方式就是在该方法中体现的。

### Ribbon自带算法

　　Ribbon的内置可用负载均衡算法有七种。

1、**RoundRobinRule**

　　轮询策略。Ribbon默认采用的策略

![](./images/images/img_054_1e885d1bdaa0.png)

2、**BestAvailableRule**

　　选择并发量最小的provider，即连接的消费者数量最少的provider。其会遍历服务列表中的每一个provider，选择当前连接数量minimalConcurrentConnections最小的provider。

![](./images/images/img_055_3d0e1bd48ada.png)

3、**AvailabilityFilteringRule**

　　过滤掉由于连续连接或读故障而处于短路器跳闸状态的provider，或已经超过连接极限的provider，对剩余provider采用轮询策略。

![](./images/images/img_056_3927f6caae52.png)

4、**ZoneAvoidanceRule**

　　复合判断provider所在区域的性能及provider的可用性选择服务器。

![](./images/images/img_057_f03ea059e79e.png)

![](./images/images/img_058_03870e7f0625.png)

5、**RandomRule**

　　随机策略，从所有可用的provider中随机选一个。

![](./images/images/img_059_f00a8e54d9d6.png)

6、**RetryRule**

　　先按照RoundRobinRule策略获取provider，若后去失败，则在指定的时限内重试。默认的时限为500毫秒。

![](./images/images/img_060_dae212d3d655.png)

7、**WeightedResponseTimeRule**

　　权重响应时间策略，根据每个provider的平均响应时间计算其权重，响应时间越快权重越大，被选中的几率就越高，在刚启动时采用轮询策略，后面就会根据权重重新进行选择。

![](./images/images/img_061_2aa92393cbdf.png)

## 更改默认策略

　　Ribbon默认采用的是RoundRobinRule，即轮询策略。只需要在启动类中添加如下代码即可

![](./images/images/img_062_face0b4bcb45.png)

## 自定义负载均衡策略

　　该负载均衡策略的思路是：从所有可用的provider中排出掉指定端口号的provider，剩余provider进行随机选择。

![](./images/images/img_063_b69a7a58d65c.png)

![](./images/images/img_064_55c474de77b1.png)

CustomRule.java

```text
package com.com.consumer.irule;

import com.netflix.loadbalancer.ILoadBalancer;
import com.netflix.loadbalancer.IRule;
import com.netflix.loadbalancer.Server;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

/**
 * 自定义负载均衡算法
 * 从所有可用provider中排出掉指定端口号的provider，剩余provider进行随机选择
 */
public class CustomRule implements IRule {
    private ILoadBalancer lb;
    /**
     * 要排除提供者端口号集合
     */
    private List<Integer> excludePorts;

    public CustomRule() {
    }

    public CustomRule(List<Integer> excludePorts) {
        this.excludePorts = excludePorts;
    }

    @Override
    public Server choose(Object key) {
        // 获取所有可用的提供者
        List<Server> servers = lb.getReachableServers();
        // 获取所有排出了指定端口号的提供者
        List<Server> availableServers = this.getAvailableServers(servers);
        // 从剩余的提供者中随机获取可用的提供者
        return this.getAvailableRandomServers(availableServers);
    }

    // 获取所有排出了指定端口号的提供者
    private List<Server> getAvailableServers(List<Server> servers) {
        // 没有要排除的Server，则直接将所有可用Servers返回
        if (excludePorts == null || excludePorts.size() == 0) return servers;
        // 定义一个集合，用于存放排出了指定端口号的Server
        List<Server> aservers = new ArrayList<>();
        boolean flag;
        for (Server server : servers) {
            flag = true;
            for (Integer port : excludePorts) {
                if (server.getPort() == port) {
                    flag = false;
                    break;
                }
            }
            // 若flag为false，说明上面的for循环执行了break，说明当前遍历的Server是要排除掉的
            if (flag) aservers.add(server);
        }
        return aservers;
    }

    // 从剩余的提供者中随机获取可用的提供者
    private Server getAvailableRandomServers(List<Server> availableServers) {
        // 获取一个[0，availableServers.size()]的随机整数
        int index = new Random().nextInt(availableServers.size());
        return availableServers.get(index);
    }

    @Override
    public void setLoadBalancer(ILoadBalancer lb) {
        this.lb = lb;
    }

    @Override
    public ILoadBalancer getLoadBalancer() {
        return lb;
    }
}
```

# Hystrix 熔断机制与服务降级

## 服务熔断简介

　　若要了解服务熔断，需要先了解雪崩效应与服务雪崩。

### 雪崩效应

　　分布式系统中很容易出现雪崩效应

　　在IO型服务中，假设服务A依赖服务B和服务C，而B服务和C服务有可能依赖其他的服务，继续下去会使得调用链路过长，技术上称1->N扇出。

![](./images/images/img_065_c02e8822c89c.png)

　　如果在A的链路上某个或几个被调用的子服务不可用或延迟较高，则会导致调用A服务的请求被堵住。

　　堵住的A请求会消耗占用系统的进程、IO等资源，当对A服务的请求越来越多，占用的计算机资源越来越多，会导致系统瓶颈出现，造成其他的请求同样不可用，最终导致业务系统崩溃，这种现象称为雪崩效应。

　　例如一个汽车生产线，生产不同的汽车，需要使用不同的零件。如果某个零件因为种种原因无法及时供给，而没有该零件，则后续的好多已经到货的零件也无法安装。一个零件的缺失造成整台车无法装配，陷入等待零件的状态，直到零件到位，才能继续组装。

　　此时如果有很多个车型都需要这个零件，那么整个工厂都将陷入等待的状态，而前述已经生成好多的汽车部件，暂不能安装的其他零件，将由于等待而占用大量资金、场地等资源。

　　一个零件最终导致所有生产陷入瘫痪，这就是雪崩效应。

### 服务雪崩

　　雪崩效应发生在分布式SOA(Service-Oriented Architecture，面向服务的架构)系统中，则称为服务雪崩。

　　大量用户请求出现异常全部陷入阻塞的情况，即服务发生雪崩的情况。

　　举个例子，一个依赖30个微服务的系统，每个服务99.99%可用。则整个系统的可用性为99.99%的30次方，约为99.7%。为什么是30次方呢？若系统依赖于2个微服务，一个微服务的可用率为99.99%，那么，两个微服务的组合的可用率为99.99%*99.99%，同理，30个微服务，每个微服务的可用率为99.99%，则这30个微服务组合后的可用性为99.99%的30次方。

　　也就是说，整个系统会存在0.3%的失败率。若存在一亿次请求，那么将会有30万次失败。随着服务依赖数量的增多，服务不稳定的概率会成指数升高。

### 熔断机制

　　熔断机制是服务雪崩的一种有效解决方案。当服务消费者所请求的提供者暂不能提供服务时，消费者会被阻塞，且长时间占用请求链路。为了防止这种情况的发生，当在设定阈值限制到达时，仍未获得提供者的服务，则系统将通过断路器直接将此请求链路断开。这种像熔断“保险丝”一样的解决方案称为熔断机制。

## Hystrix简介

### 官网地址

https://github.com/Netflix/Hystrix

## 服务降级简介

　　在访问分布式系统中，经常会发生以下两种情况：

1、当整个微服务架构整体的负载超出了预设的上限阈值，或即将到来的流量预计将会超过预设的阈值时，为了保证重要或基本的服务能正常运行，我们可以将一些不重要或不紧急的服务进行延迟使用或暂停使用。这就是服务熔断，类似于主动拉电闸的服务熔断。此时，若有消费者消费这些延迟/暂停使用的服务则会出现阻塞，等待提供者的响应。

2、当消费者访问某微服务时，由于网络或其他原因，提供者向消费者响应过慢，出现服务超时或根本就没有响应时，这也是一种服务熔断，类似于保险丝自动熔断的服务熔断。此时消费者会被迫阻塞，等待提供者的响应。

　　在发生服务熔断时，不仅用户体验很差，其还占用了大量的系统资源。为了解决这个问题，在编写消费者端代码时就设置了预案：在消费者端给出一种默认的、临时的预处理方案，能够给出消费者一个可以接受的结果。即，对于用户(指的是人，并非指消费者端)来说，其所消费的服务并非由应当提供服务的提供者端给出，而是由服务消费者临时给出，服务质量降级了。提供者端的“服务熔断”与消费者端的“本地服务”，共同构成了“服务降级”。

　　简单来说服务降级指的是，当服务的提供者无法正常提供服务时，为了增加用户体验，保证真个系统能够正常运行，由服务消费者端调用本地操作，暂时给出用户效应结果的情况。

## Hystrix服务降级

### 总步骤

1. 添加hystrix依赖
2. 修改处理器，在处理器方法上添加@HystrixCommond注解，并添加处理方法
3. 在启动类上添加@EnableCircuitBreaker注解

### 创建消费者工程

1、创建工程

　　复制02-consumer-8082，并重命名04-consumer-hystrix-8082

2、添加依赖

```text
        <!-- hystrix依赖 -->
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-hystrix</artifactId>
            <version>2.2.2.RELEASE</version>
        </dependency>
```

3、修改处理器

![](./images/images/img_066_f07e743cfb8f.png)

**注：实际中一个方法对应一个处理函数**

4、启动类上添加注解

![](./images/images/img_067_55bb5b6a397e.png)

### 测试

　　为了演示方法，只开启eureka注解中心和消费者

![](./images/images/img_068_29e7508dea01.png)

## Hystrix+Feign服务降级

### 总步骤

1. 在Feign接口所在包下定义降级处理类
2. 在Feign接口中指定要使用的降级处理类
3. 在配置文件中开启Feign对Hystrix的支持

### 创建消费者工程

　　复制03-consumer-feign-8082并重命名04-consumer-feign-hystrix-8082

### 定义降级处理类

　　降级处理类需要实现FallbackFactory接口，该接口的泛型为Feign接口。该类可以定义在任意包下，不过，一般会与Feign解口定义在同一包下。

　　该类需要使用@Component注解，表示要将其交给Spring容器来管理。

![](./images/images/img_069_676dc9b73280.png)

### 接口类上指定降级处理器类

![](./images/images/img_070_ad47f389d7d5.png)

### 修改配置文件

　　在配置文件中添加如下内容，没有自动提示

![](./images/images/img_071_3fbd2c09a9c6.png)

### 测试

![](./images/images/img_072_619ed921668c.png)

**注：方法级别的优先级小于类级别的优先级**

# 网关服务Zuul

## 官网地址

https://github.com/Netflix/zuul

## 简单概括

　　Zuul主要提供了对请求的路由有过滤功能。路由功能主要指，将外部请求转发到具体的微服务实例上，是外部访问微服务的统一入口。过滤功能主要指，对请求的处理过程进行干预，对请求进行校验、服务聚合等处理。

　　Zuul与Eureka进行整合，将Zuul自身注册为Eureka服务治理下的应用，从Eureka Server中获取到其他微服务信息，使外部对于微服务的访问都是通过Zull进行转发的。

![](./images/images/img_073_6e42ef7f95ae.png)

## 基本用法

### 创建zuul网关服务器

![](./images/images/img_074_e171ff8294ac.png)

![](./images/images/img_075_8611d720e3d0.png)

### 修改配置文件

![](./images/images/img_076_7e265a405b16.png)

### 修改启动类

![](./images/images/img_077_3f9559f44eaa.png)

### 启动测试

![](./images/images/img_078_e1993744f39d.png)

![](./images/images/img_079_bcc6ad5a8f44.png)

![](./images/images/img_080_c6a7ae32895c.png)

## 设置zull路由映射规则

　　上面测试，我们发现，直接将服务名称暴露给了消费者，为了保护和隐藏服务名称，可以为其配置一个映射路径，将这个映射路径暴露给消费者即可。

![](./images/images/img_081_890e248d29a8.png)

```text
server.port=9000
# 指定Eureka注册中心
eureka.client.service-url.defaultZone=http://localhost:8083/eureka

spring.application.name=cyb-zuul-depart

# zuul：设置zuul路由规则
# somedepart.service-id：指定要替换的微服务名称
zuul.routes.somedepart.service-id=cyb-consumer-depart
# 指定替换使用的路径
zuul.routes.somedepart.path=/cyb/**
```

　　对于该配置需要注意以下几点：

1. somedepart：可以随意命名，但service-id与path是关键字，不能更改
2. somedepart.service-id：指定要被替换掉的微服务名称
3. somedepart.path：指定用于替换指定微服务名称的路径

### 访问测试

![](./images/images/img_082_be4ebd2e4303.png)

![](./images/images/img_083_52706bef8091.png)

　　设置过zuul路由规则后，两种方式，一样可以访问。

## 忽略服务名称

　　以上配置虽然可以使用映射路径访问微服务，但是通过原来的服务名称仍可以访问到微服务，即以上配置并没有隐藏和保护了原来的微服务名称。可以在配置文件中设置忽略微服务属性，替换原有的微服务名称使用。两种方式：1、忽略指定微服务；2、忽略所有微服务

### 忽略指定微服务名称

　　在配置文件中指定要忽略的微服务

![](./images/images/img_084_ae8ae80d11ff.png)

![](./images/images/img_085_bc19413f8a0e.png)

![](./images/images/img_086_1c5190341288.png)

此时通过微服务名称已无法访问到微服务了，但通过映射路径是可以正常访问的

### 忽略所有微服务名称

![](./images/images/img_087_ea1d7671a593.png)

**注：效果和上面忽略指定的微服务是一样的！**

### 为映射路径配置统一前缀

　　一般情况下我们会在映射路径前添加一个前缀用于表示模块信息或公司名称等，而该前缀对于各个微服务来说一般都是需要的，所以我们可以为映射路径统一配置前缀。

```text
server.port=9000
# 指定Eureka注册中心
eureka.client.service-url.defaultZone=http://localhost:8083/eureka

spring.application.name=cyb-zuul-depart

# zuul：设置zuul路由规则
# somedepart.service-id：指定要替换的微服务名称
zuul.routes.somedepart.service-id=cyb-consumer-depart
# 指定替换使用的路径
zuul.routes.somedepart.path=/cyb/**
# 指定要忽略的微服务
# zuul.ignored-services=cyb-consumer-depart
# 忽略所有的微服务
zuul.ignored-services=*
# 指定访问的统一前缀
zuul.prefix=/test
```

![](./images/images/img_088_bdda29b24354.png)

# 练习源码下载

```text
百度云盘
链接:https://pan.baidu.com/s/1OYwtq9O-3dF5fEuADNcIhA  密码:pj5a
```
