{

  "title": "分布式RPC系统框架Dubbo",
  "date": "2020-01-30",
  "description": "导读 Apache Dubbo是一款**高性能**、**轻量级**的**开源Java** **RPC框架**，它提供了三大核心能力；**面向接口**的**远程**方法**调用**，**智能容错**和**负载均衡**，以及**服务自动注册**和**发现**。 dubbo官网：点我直达 第一个Dubbo",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12199575.html"

}

# 导读

　　Apache Dubbo是一款**高性能**、**轻量级**的**开源Java** **RPC框架**，它提供了三大核心能力；**面向接口**的**远程**方法**调用**，**智能容错**和**负载均衡**，以及**服务自动注册**和**发现**。

dubbo官网：[点我直达](http://dubbo.apache.org/zh-cn/)

# 第一个Dubbo程序(小试牛刀)

## 创建业务接口工程

### 项目结构

![](./images/images/img_001_11caab9873b7.png)

### 创建包和接口类

![](./images/images/img_002_a62cdfff0d14.png)

### 安装项目

![](./images/images/img_003_0811dab8fae0.png)

## 创建提供者Provider工程

### 项目结构

![](./images/images/img_004_39d13e1f280f.png)

### pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.cyb</groupId>
    <artifactId>02-first-provider</artifactId>
    <version>1.0-SNAPSHOT</version>

    <!--编译器依赖-->
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>13</maven.compiler.source>
        <maven.compiler.target>13</maven.compiler.target>
        <!--自定义版本号-->
        <spring-version>4.3.16.RELEASE</spring-version>
    </properties>
    <dependencies>
        <!--自定义工程依赖-->
        <dependency>
            <groupId>org.cyb</groupId>
            <artifactId>01-common</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        <!--dubbo依赖-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>dubbo</artifactId>
            <version>2.6.7</version>
        </dependency>
        <!--netty-->
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-all</artifactId>
            <version>4.1.32.Final</version>
        </dependency>

        <!--spring依赖-->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-beans</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-expression</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aspects</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-tx</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-jdbc</artifactId>
            <version>${spring-version}</version>
        </dependency>
    </dependencies>
</project>
```

### 注意

![](./images/images/img_005_7590df98d26a.png)

### spring-dubbo-provider.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dubbo="http://code.alibabatech.com/schema/dubbo"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://code.alibabatech.com/schema/dubbo http://code.alibabatech.com/schema/dubbo/dubbo.xsd">
    <!--当前工程名称，该名称将在监控平台使用-->
    <dubbo:application name="02-first-provider"/>
    <!--注册Service，将来服务的提供者-->
    <bean id="someService" class="com.cyb.service.SomeServiceImpl"></bean>
    <!--暴露服务,采用直连的方式-->
    <dubbo:service interface="com.cyb.service.SomeService" ref="someService" registry="N/A"></dubbo:service>
</beans>
```

### SomeServiceImpl.java

```text
package com.cyb.service;

public class SomeServiceImpl implements SomeService{
    @Override
    public String hello(String name) {
        System.out.println("Dubbo World Welcome You"+name);
        return "chenyanbin";
    }
}
```

### RunProvider.java

```text
package com.cyb.run;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import java.io.IOException;

public class RunProvider {
    public static void main(String[] args) throws IOException {
        //创建spring容器
        ApplicationContext ac = new ClassPathXmlApplicationContext("spring-dubbo-provider.xml");
        //启动spring容器
        ((ClassPathXmlApplicationContext) ac).start();
        //将当前主线程阻塞
        System.in.read();
    }
}
```

## 创建消费者Consumer工程

### 项目结构图

![](./images/images/img_006_d14f3dabbda8.png)

### pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.cyb</groupId>
    <artifactId>02-first-consumer</artifactId>
    <version>1.0-SNAPSHOT</version>
    <!--编译器依赖-->
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>13</maven.compiler.source>
        <maven.compiler.target>13</maven.compiler.target>
        <!--自定义版本号-->
        <spring-version>4.3.16.RELEASE</spring-version>
    </properties>

    <dependencies>
        <!--自定义工程依赖-->
        <dependency>
            <groupId>org.cyb</groupId>
            <artifactId>01-common</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>
        <!--dubbo依赖-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>dubbo</artifactId>
            <version>2.6.7</version>
        </dependency>
        <!--netty-->
        <dependency>
            <groupId>io.netty</groupId>
            <artifactId>netty-all</artifactId>
            <version>4.1.32.Final</version>
        </dependency>
        <!--spring依赖-->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-beans</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-expression</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
            <version>${spring-version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aspects</artifactId>
            <version>${spring-version}</version>
        </dependency>
    </dependencies>
</project>
```

### spring-dubbo-consumer.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dubbo="http://code.alibabatech.com/schema/dubbo"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://code.alibabatech.com/schema/dubbo http://code.alibabatech.com/schema/dubbo/dubbo.xsd">
    <!--当前工程的名称，监控中心使用-->
    <dubbo:application name="02-first-consumer"/>
    <!--消费引用-->
    <dubbo:reference id="someSerivce" interface="com.cyb.service.SomeService" url="dubbo://localhost:20880"></dubbo:reference>
</beans>
```

**注：端口号20880固定**

### RunConsumer.java

```text
package com.cyb.run;

import com.cyb.service.SomeService;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class RunConsumer {
    public static void main(String[] args) {
        //创建Spring容器
        ApplicationContext ac=new ClassPathXmlApplicationContext("spring-dubbo-consumer.xml");
        SomeService service = (SomeService) ac.getBean("someSerivce");
        service.hello("tom");
    }
}
```

## 运行

![](./images/images/img_007_46127396c7d4.gif)

# Zookeeper注册中心&Zookeeper集群(Dubbo官网推荐)

## 拷贝生产者和消费者工程

![](./images/images/img_008_21b7e34bdb32.png)

## 注册中心其他方式

地址:[http://dubbo.apache.org/zh-cn/docs/user/references/registry/introduction.html](http://dubbo.apache.org/zh-cn/docs/user/references/registry/introduction.html)

![](./images/images/img_009_ab082df2a09d.png)

## Zookeeper工程搭建

配置参考地址：[点我直达](https://www.cnblogs.com/chenyanbin/p/12202048.html)

### 启动zookeeper服务

![](./images/images/img_010_caf6c7000807.png)

## 修改提供者工程

### pom.xml添加curator客户端依赖 

```text
        <!-- zk客户端依赖：curator-framework-->
        <dependency>
            <groupId>org.apache.curator</groupId>
            <artifactId>curator-framework</artifactId>
            <version>4.0.1</version>
        </dependency>
```

### 注意事项

![](./images/images/img_011_20901cdba3cc.png)

### 修改spring-dubbo-provider.xml

![](./images/images/img_012_8569cc4de7e8.png)

### 代码拷贝区

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dubbo="http://code.alibabatech.com/schema/dubbo"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://code.alibabatech.com/schema/dubbo http://code.alibabatech.com/schema/dubbo/dubbo.xsd">
    <!--当前工程名称，该名称将在监控平台使用-->
    <dubbo:application name="03-provider-zk"/>
    <!--注册Service，将来服务的提供者-->
    <bean id="someService" class="com.cyb.service.SomeServiceImpl"></bean>

    <!-- 声明zk服务中心 -->
    <!-- 单机版 -->
    <!-- 方式一 -->
    <dubbo:registry address="zookeeper://192.168.1.111:2181"/>
    <!-- 方式二 -->
    <!-- <dubbo:registry protocol="zookeeper" address=""/> -->

    <!-- 集群配置 -->
    <!-- 方式一 -->
    <!-- <dubbo:registry address="zookeeper://10.20.153.10:2181?backup=10.20.153.11:2181,10.20.153.12:2181" /> -->
    <!-- 方式二 -->
    <!-- <dubbo:registry protocol="zookeeper" address="10.20.153.10:2181,10.20.153.11:2181,10.20.153.12:2181" /> -->

    <!-- 同一Zookeeper，分成多组注册中心 -->
    <!-- <dubbo:registry id="chinaRegistry" protocol="zookeeper" address="10.20.153.10:2181" group="china" />
    <dubbo:registry id="intlRegistry" protocol="zookeeper" address="10.20.153.10:2181" group="intl" /> -->

    <!-- 暴露服务,将服务暴露给zk服务中心 -->
<!-- <dubbo:service interface="com.cyb.service.SomeService" ref="someService" registry="N/A"></dubbo:service> -->
    <dubbo:service interface="com.cyb.service.SomeService" ref="someService"></dubbo:service>

</beans>
```

## 修改消费者工程

### pom.xml添加curator客户端依赖

```text
        <!-- zk客户端依赖：curator-framework-->
        <dependency>
            <groupId>org.apache.curator</groupId>
            <artifactId>curator-framework</artifactId>
            <version>4.0.1</version>
        </dependency>
```

### 修改spring-dubbo-consumer.xml

![](./images/images/img_013_9f328e10714e.png)

### 代码拷贝区

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dubbo="http://code.alibabatech.com/schema/dubbo"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://code.alibabatech.com/schema/dubbo http://code.alibabatech.com/schema/dubbo/dubbo.xsd">
    <!--当前工程的名称，监控中心使用-->
    <dubbo:application name="03-consumer-zk"/>

    <!-- 声明zk服务中心 -->
    <!-- 单机版 -->
    <dubbo:registry address="zookeeper://192.168.1.111:2181"/>

    <!--消费引用-->
    <!-- <dubbo:reference id="someSerivce" interface="com.cyb.service.SomeService" url="dubbo://localhost:20880"></dubbo:reference> -->
    <dubbo:reference id="someSerivce" interface="com.cyb.service.SomeService"></dubbo:reference>
</beans>
```

## 运行

![](./images/images/img_014_0dd43b159f52.gif)

# Dubbo声明式缓存

**为**了进一步**提高消费者对用户的响应速度**，**减少**提供者的**压力**。**Dubbo提供**了**基于结果的声明式缓存**。该**缓存**是**基于消费者端**的，所以**使用很简单**，只需**修改消费者配置文件**，**与提供者无关**。

## 修改消费者配置文件

　　仅需在<dubbo:reference />中添加cache="true"即可

![](./images/images/img_015_5dec924ad28b.png)

## 修改RunConsumer.java

![](./images/images/img_016_a80565d54f11.png)

## 缓存VS无缓存

　　先不加缓存，发现提供者执行2次，加上缓存提供者只执行一次

![](./images/images/img_017_606ad9358e9f.gif)

![](./images/images/img_018_666383b86604.gif)

## dubbo提供了三种结果缓存机制

1. lru：服务级别缓存的默认机制。该机制默认可以缓存1000个结果。若超出1000，将采用最近最少使用原则来删除缓存，以保证最热的数据被缓存。
2. threadlocal：当前线程缓存。当多个线程要对当前线程进行某一操作时首先需要查询当前线程的某个信息，通过线程缓存，则可有效减少查询。
3. jcache：可以桥接各种缓存实现，即第三方缓存产品。

### spring-dubbo-consumer.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:dubbo="http://code.alibabatech.com/schema/dubbo"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://code.alibabatech.com/schema/dubbo http://code.alibabatech.com/schema/dubbo/dubbo.xsd">
    <!--当前工程的名称，监控中心使用-->
    <dubbo:application name="03-consumer-zk"/>

    <!-- 声明zk服务中心 -->
    <!-- 单机版 -->
    <dubbo:registry address="zookeeper://192.168.1.111:2181"/>

    <!-- <dubbo:reference id="someSerivce" interface="com.cyb.service.SomeService" url="dubbo://localhost:20880"></dubbo:reference> -->
    <!-- <dubbo:reference id="someSerivce" interface="com.cyb.service.SomeService"></dubbo:reference> -->

    <!--消费引用:基于服务级别的声明式缓存(结果缓存)-->
    <!--<dubbo:reference id="someSerivce" interface="com.cyb.service.SomeService" cache="true"></dubbo:reference>-->

    <!--消费引用:基于方法级别的声明式缓存(结果缓存)-->
    <dubbo:reference id="someSerivce" interface="com.cyb.service.SomeService" >
        <!--lru-->
        <dubbo:method name="hello" cache="lru"></dubbo:method>
        <!--threadlocal-->
        <dubbo:method name="hello" cache="threadlocal"></dubbo:method>
    </dubbo:reference>
</beans>
```

## 结果缓存的应用场景

**Dubbo的结果缓存**可以**应用**在**查询结果不变的场景**。即不能使用在如下场景：消费者A调用的业务方法后从DB查询到一个结果a，此后，消费者B对DB中的该结果相关数据进行了修改，已使该查询结果变为b，但由于使用了结果缓存，消费者A中调用业务方法后的查询结果将长时间为a，直到该结果由于缓存空间满而被消除，否则，永远无法得到更新过的结果b。

# 多版本控制

　　Dubbo的多版本控制指的是，**服务名称(接口名)相同的情况下提供不同的服务(实现类不同) **，然而消费者是通过服务名称(接口名)进行服务查询并进行消费的。提供者所提供的服务名称相同，如何让消费者通过名称进行服务查找呢？为服务添加一个版本号，使用“服务名称”+“版本号”的方式来唯一确定一个服务。

　　多版本控制主要的应用场景是：当一个接口的实现类需要升级时，可以使用版本号进行过渡(根据开闭原则，不能直接修改原实现类，只能添加新的实现类)。需要注意的是，版本号不同的服务间是不能互相引用的，因为新版本存在的目的是替换老版本。在生产环境中若存在多个提供者需要升级，一般不会一次性全部进行升级，而是会在低压力时间段先升级一部分，然后在下次再进行部分升级，直到全部升级完成。那么，这期间就需要使用版本号进行过渡。

## 项目准备

拷贝项目

![](./images/images/img_019_7020afe336de.png)

## 提供者(04-provider-version)

![](./images/images/img_020_2d404d0c4b1f.png)

### 修改配置文件

![](./images/images/img_021_1149c5097efb.png)

## 消费者(04-consumer-version)

![](./images/images/img_022_21f907ba205f.png)

## 执行

![](./images/images/img_023_b5a2ea4b90be.gif)

# 服务分组

**服务分组与多版本控制**的**使用方式几乎是相同**的，只要**将version替换为group即可**。但**使用目的不同**。使用**版本控制**的目的是**为了升级**，将原有老版本替换掉，将来不再提供老版本的服务，所以不同版本间不能出现相互调用。而**分组**的**目的则不同**，其也是**针对相同接口**，**给出了多种实现类**，但不同的是，**这些不同实现并没有替换掉谁的意思，是针对不同需求，或针对不同功能模块锁给出的实现**。**这些实现所提供的服务是并存的，所以他们间可以出现相互调用关系**。例如，支付服务的实现，可以有微信支付实现与支付宝实现等。

# 服务暴露延迟

　　如果我们的服务启动过程中需要warmup事件(预热事件，与JVM重启后的预热过程相似，在启动后一小段事件后性能才能达到最佳状态)。比如初始化缓存，等待相关资源就位等。可以使用deplay进行延迟暴露。

　　值需要在服务提供者的<dubbo:service/>标签中添加delay属性，其值若为整数，则单位为毫秒，表示在指定事件后再发布服务；若为-1，则表示在spring初始化完毕后再暴露服务。

![](./images/images/img_024_13694f8e5b8e.png)

# 多注册中心

　　很多时候一个项目中会有多个注册中心。

## 同一个服务注册到多个中心

**同一个服务**可以**注册**到**不同地域的多个注册中心**，以便为不同地域的服务消费者提供更为快捷的服务。

修改**服务提供者配置文件**。多个注册中心之间使用逗号分隔。

![](./images/images/img_025_579bcce215d7.png)

**注：不是集群！！！**

## 不同服务注册到不同中心

修改服务**提供者配置文件**

![](./images/images/img_026_dd8a139db6bc.png)

## 同一个服务引用自不同的中心

**同一个消费者**需要**调用两个不同中心服务**，而调用的该**服务的名称**(接口)、**版本等**都是**相同**的。不同中心的这个相同名称的服务调用时不同数据库中的数据，即相同服务最终执行的结果是不同的。

修改服务**消费者配置文件**

![](./images/images/img_027_6043c2cff1ea.png)

# 多协议支持

## 服务暴露协议

　　前面的示例中，服务提供者与服务消费者都是通过zookeeper连接协议连接上ZooKeeper注册中心的。

![](./images/images/img_028_667831651b4e.png)

　　提供者与消费者均连接上了注册中心，那么消费者就理所当然的可以享受提供者提供的服务了么？

　　实际情况并不是这样的。前述ZooKeeper协议，是消费者/提供者连接注册中心的连接协议，而非消费者与提供者间的连接协议。

　　当消费者连接上注册中心后，在消费服务之前，首先需要连接上这个服务提供者。虽然消费者通过注册中心可以获取到服务提供者，但提供者对于消费者来说却是透明的，消费者并不知道真正的服务提供者是谁。不过，无论提供者是谁，消费者都必须连接上提供者才可以获取到真正的服务，而这个连接也是需要专门的连接协议的。这个协议称为服务暴露协议。

　　可是我们之前的代码示例中并没有看到服务暴露协议的相关配置，但仍可正常运行项目，这是为什么呢？因为采用了默认的暴露协议：Dubbo服务暴露协议。处理Dubbo服务暴露协议外，Dubbo框架还支持另外七种服务暴露协议：Hessian协议、HTTP协议、RMI协议、WebService协议、Thrift协议、Memcached协议、Redis协议；但在实际生产中，使用最多的就是Dubbo服务暴露协议。

　　Dubbo服务暴露协议，适合于小数据量大并发的服务调用，以及服务消费者主机数远大于服务提供者主机数的情况。

## 服务暴露协议用法

　　在**服务提供者的spring配置文件**中首先需要注册暴露协议，然后在暴露服务时具体制定所使用的已注册的暴露协议。

![](./images/images/img_029_6428ae1fe68f.png)

**注：protocol属性用于指定当前服务所使用的暴露协议**

## 同一服务支持多种协议

　　直接修改**服务****提供者的配置文件**

![](./images/images/img_030_04a33d360f40.png)

## 不同服务使用不同协议

　　直接修改**服务提供者配置文件**

![](./images/images/img_031_5bfa2182dfc7.png)

# Dubbo的高级设置及使用建议

## 在提供者上尽量多配置消费者端属性

　　提供者上尽量多配置消费者端的属性，让提供者实现着一开始就思考提供者服务特点、服务质量等问题。因为作服务的提供者，比服务使用方更清楚服务性能参数，如调用的超时时间、合理的重试次数等。在提供者端配置后，消费者不配置则会使用提供者端的配置值，即提供者配置可以作为消费者的缺省值。否则，消费者会使用消费者端的全局设置，这对提供者是不可控的，并且往往不合理的。

![](./images/images/img_032_9ac8d0cab059.png)

　　以下属性在<dubbo:method/>上则是针对指定方法，配置在<dubbo:service/>上则是针对整个服务。

- timeout：远程服务调用超时时限。
- retries：失败重试次数，默认值是2。
- loadbalance：负载均衡算法，默认是随机的random。还可以有轮询roundrobin、最不活跃优先leastactive等。
- actives：消费者最大并发调用限制，即当Consumer对一个服务的并发调用到上限后，新调用会阻塞直到超时。

## 提供者上配置合理的提供者端属性

![](./images/images/img_033_1edf61b8ddbd.png)

- threads：用于指定服务线程池大小
- executes：一个服务提供者并行执行请求上限，即当提供者对一个服务的并发调用达到上限后，新调用会阻塞，此时消费者可能会超时，该属性配置在<dubbo:method/>上则是针对指定方法的，配置在<dubbo:service/>上则是针对整个服务

# Spring Boot中使用Dubbo

## 总步骤

　　一个Dubbo项目至少应该由三个工程构成：包含Service接口、实体类、常量类、工具类等的commons工程；包含Service实现类、Dao接口、Mapper映射文件的服务提供者serviceDao工程；包含SpringMVC的处理器类的服务消费者userWeb工程。其中commons工程就是一个普通的Maven-java工程，另外两个都是Spring Boot的web工程。

### 服务提供者工程定义

1. 添加zkClient依赖、Dubbo与Spring Boot整合依赖，以及commons工程依赖
2. 在入口类上加上@EnableDubboConfiguration注解，开启Dubbo自动配置
3. 在主配置文件中添加Spring.application.name属性，指定提供者应用名称；添加spring.dubbo.registry属性，指定注册中心
4. 在Service实现类上添加**Dubbo的@Service注解**，以及@Component注解

### 服务消费者工程定义

1. 添加zkClient依赖、Dubbo与Spring Boot整合依赖，及commons工程依赖
2. 在入口类上添加@EnableDubboConfiguration注解，开启Dubbo自动配置
3. 在主配置文件中添加spring.application.name属性，指定提供者应用名称；添加spring.dubbo.registry属性，指定注册中心

## 工程搭建

## 公共项目(4-common)

### 项目结构

![](./images/images/img_034_869067e3d00a.png)

### pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.cyb</groupId>
    <artifactId>4-common</artifactId>
    <version>1.0-SNAPSHOT</version>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <maven.compiler.source>13</maven.compiler.source>
        <maven.compiler.target>13</maven.compiler.target>
    </properties>
    <dependencies>
        <!--lombok依赖 -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.10</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>
</project>
```

### EmployeePo.java

```text
package com.cyb.bean;

import lombok.Data;

import java.io.Serializable;

@Data
public class EmployeePo implements Serializable {
    private Integer id;
    private String name;
    private Integer age;
}
```

### EmployeeService.java

```text
package com.cyb.service;

import com.cyb.bean.EmployeePo;

public interface EmployeeService {
    void addEmployee(EmployeePo employee);

    EmployeePo findEmployeeById(int id);

    int findEmployeeCount();
}
```

### Install

![](./images/images/img_035_5577c78d3d4c.png)

## 提供者(4-provider)

### 新建Spring Boot工程

![](./images/images/img_036_21b8c5ddbc31.png)

![](./images/images/img_037_8b887f7f8b28.png)

![](./images/images/img_038_3ead2cc0a159.png)

![](./images/images/img_039_f759514244c4.png)

### 项目结构

![](./images/images/img_040_9d33b82e3a9c.png)

### EmployeeDao.java

```text
package com.cyb.provider.dao;

import com.cyb.bean.EmployeePo;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface EmployeeDao {
    void insertEmployee(EmployeePo employeePo);
    EmployeePo selectEmployeeById(int id);
    int selectEmployeeCount();
}
```

### EmployeeDao.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.cyb.provider.dao.EmployeeDao">
    <insert id="insertEmployee">
    insert into employee (name,age) values (#{name},#{age})
</insert>
    <select id="selectEmployeeById" resultType="com.cyb.bean.EmployeePo">
        select id,name,age from employee where id=#{id}
    </select>
    <select id="selectEmployeeCount" resultType="int">
        select count(1) from employee
    </select>
</mapper>
```

### EmployeeServiceImpl.java

```text
package com.cyb.provider.service;

import com.alibaba.dubbo.config.annotation.Service;
import com.cyb.bean.EmployeePo;
import com.cyb.provider.dao.EmployeeDao;
import com.cyb.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.redis.core.BoundValueOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Component;
import org.springframework.transaction.annotation.Transactional;

import java.util.concurrent.TimeUnit;

@Service //dubbo的Service,表示Dubbo服务的提供者
@Component
public class EmployeeServiceImpl implements EmployeeService {

    @Autowired
    private EmployeeDao dao;

    @Autowired
    private RedisTemplate<Object, Object> redisTemplate;

    @CacheEvict(value = "realTimeCache", allEntries = true)
    // 清除缓存,实际生产环境就这样玩，因为每个实体类设置不同的缓存区空间，范围小，清除缓存好操作
    @Transactional
    @Override
    public void addEmployee(EmployeePo employee) {
        dao.insertEmployee(employee);
    }

    //@Cacheable(value = "realTimeCache", key = "'employee_'+#id")
    @Cacheable(value = "realTimeCache") //用了自动生成key，此处可以去掉key
    // 先会去缓存中查下key是否存在，存在：则直接拿缓存中的数据；不存在：去数据库中查，查完将结果放入缓存中
    @Override
    public EmployeePo findEmployeeById(int id) {
        return dao.selectEmployeeById(id);
    }

    //使用双重检测锁，解决热点缓存问题
    //双重检测锁，解决了高并发下，对数据库访问的压力！！！！
    //热点缓存脑补，请参考：https://www.jianshu.com/p/6e37a1a9c160
    @Override
    public int findEmployeeCount() {
        //获取Redis操作对象
        BoundValueOperations<Object, Object> ops = redisTemplate.boundValueOps("count");
        //从缓存中读取数据
        Object count = ops.get();
        if (count == null) {
            synchronized (this) {
                count = ops.get();
                if (count == null) {
                    //从DB中查询
                    count = dao.selectEmployeeCount();
                    //将查询的数据，写入Redis缓存，并设置到期时限
                    ops.set(count, 10, TimeUnit.SECONDS);
                }
            }
        }
        return (int) count;
    }
}
```

### ProviderApplication.java

```text
package com.cyb.provider;

import com.alibaba.dubbo.config.spring.context.annotation.EnableDubbo;
import com.alibaba.dubbo.config.spring.context.annotation.EnableDubboConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;
import org.springframework.transaction.annotation.EnableTransactionManagement;

@EnableTransactionManagement //开启事务
@SpringBootApplication
@EnableCaching //开启缓存
@EnableDubboConfig //开启Dubbo自动配置
@EnableDubbo
public class ProviderApplication {

    public static void main(String[] args) {

        SpringApplication.run(ProviderApplication.class, args);
    }
}
```

### application.properties

```text
server.port=8899

# 注册映射文件
mybatis.mapper-locations=classpath:com/cyb/provider/dao/EmployeeDao.xml
# 注册实体类别名
mybatis.type-aliases-package=com.cyb.bean.EmployeePo
# 注册数据源类型
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
# 数据库连接字符串
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://localhost:3306/cyb
spring.datasource.username=root
spring.datasource.password=root

# 控制日志显示格式
logging.pattern.console=%leven %msg%n
logging.level.root=warn
# 格式：logging.level.dao层命名空间
logging.level.com.cyb.provider.dao=debug

# 连接redis
spring.redis.host=192.168.1.108
spring.redis.port=6379
spring.redis.password=root
# 连接redis集群，redis利用哨兵机制实现高可用
# spring.redis.sentinel.master=mymaster
# spring.redis.sentinel.nodes=sentinel1:6370,sentinel2:6371,sentinel3:6372

# 指定缓存类型
spring.cache.type=redis
# 设置缓存名称
spring.cache.cache-names=realTimeCache

# 注册Dubbo相关配置
dubbo.application.name=provider
dubbo.registry.protocol=zookeeper
dubbo.registry.address=192.168.1.108:2181
dubbo.scan.base-packages=com.cyb.provider.service
```

### pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.5.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.cyb</groupId>
    <artifactId>4-servicedata-provider</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>4-servicedata-provider</name>
    <description>Demo project for Spring Boot</description>
    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>13</java.version>
    </properties>
    <dependencies>
        <!--自定义工程依赖-->
        <dependency>
            <groupId>com.cyb</groupId>
            <artifactId>4-common</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>

        <!--zkClient客户端依赖-->
        <dependency>
            <groupId>com.101tec</groupId>
            <artifactId>zkclient</artifactId>
            <version>0.11</version>
            <!--移除日志版本依赖-->
            <exclusions>
                <exclusion>
                    <groupId>org.slf4j</groupId>
                    <artifactId>slf4j-log4j12</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <!--spring boot与dubbo整合依赖-->
        <dependency>
            <groupId>com.alibaba.spring.boot</groupId>
            <artifactId>dubbo-spring-boot-starter</artifactId>
            <version>2.0.0</version>
        </dependency>

        <!--Spring Boot与redis依赖 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
        </dependency>

        <!--Druid连接池 -->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.10</version>
        </dependency>

        <!--mysql驱动 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>

        <!--Mybatis与Spring Boot整合依赖，必须要版本号 -->
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>1.3.2</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
        <resources>
            <!--注册dao包下mybatis映射文件为资源目录 -->
            <resource>
                <directory>src/main/java</directory>
                <includes>
                    <include>**/*.xml</include>
                </includes>
            </resource>
        </resources>
    </build>

</project>
```

## 消费者(4-consumer)

### 新建Spring Boot工程

![](./images/images/img_041_094669fa6848.png)

![](./images/images/img_042_93b5733ed124.png)

![](./images/images/img_043_9a9ef34778ec.png)

![](./images/images/img_044_87461f24812b.png)

### 项目结构

![](./images/images/img_045_427221592694.png)

### SomeController.java

```text
package com.cyb.consumer.controller;

import com.alibaba.dubbo.config.annotation.Reference;
import com.cyb.bean.EmployeePo;
import com.cyb.service.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class SomeController {

    @Reference
//    @Autowired
    private EmployeeService service;

    @RequestMapping("home")
    public String registerHandler(String name, int age, Model model) {
        model.addAttribute("name", name);
        model.addAttribute("age", age);
        return "home";
    }

    @RequestMapping("/rows")
    public String GetCountHandle(Model model)
    {
        model.addAttribute("rows",service.findEmployeeCount());
        return "/rows.jsp";
    }

    @RequestMapping("/find")
    @ResponseBody
    public EmployeePo findHandle(int id){
        return  service.findEmployeeById(id);
    }

    @RequestMapping("/count")
    @ResponseBody
    public int countHandle(Model model){
        int rec=service.findEmployeeCount();
        return rec;
    }
}
```

### ConsumerApplication.java

```text
package com.cyb.consumer;

import com.alibaba.dubbo.config.spring.context.annotation.EnableDubbo;
import com.alibaba.dubbo.config.spring.context.annotation.EnableDubboConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication(exclude = DataSourceAutoConfiguration.class)
@EnableDubboConfig
@EnableDubbo
public class ConsumerApplication {

    public static void main(String[] args) {

        SpringApplication.run(ConsumerApplication.class, args);
    }

}
```

### application.properties

```text
server.port=8800

# 视图的前缀后后缀
#spring.mvc.view.prefix=/
#spring.mvc.view.suffix=.jsp

# 注册Dubbo相关配置
dubbo.application.name=consumer
dubbo.registry.protocol=zookeeper
dubbo.registry.address=192.168.1.108:2181
dubbo.scan.base-packages=com.cyb.consumer.controller
```

### rows.jsp

```text
<%--
  Created by IntelliJ IDEA.
  User: chenyanbin
  Date: 2020/3/16
  Time: 1:22 下午
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
数据库行数:${rows}
</body>
</html>
```

### pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.2.5.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.cyb</groupId>
    <artifactId>4-web-consumer</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>4-web-consumer</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <java.version>13</java.version>
    </properties>

    <dependencies>
        <!--自定义工程依赖-->
        <dependency>
            <groupId>com.cyb</groupId>
            <artifactId>4-common</artifactId>
            <version>1.0-SNAPSHOT</version>
        </dependency>

        <!--zkClient客户端依赖-->
        <dependency>
            <groupId>com.101tec</groupId>
            <artifactId>zkclient</artifactId>
            <version>0.11</version>
            <exclusions>
                <exclusion>
                    <groupId>org.slf4j</groupId>
                    <artifactId>slf4j-log4j12</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <!--spring boot与dubbo整合依赖-->
        <dependency>
            <groupId>com.alibaba.spring.boot</groupId>
            <artifactId>dubbo-spring-boot-starter</artifactId>
            <version>2.0.0</version>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>org.apache.tomcat.embed</groupId>
            <artifactId>tomcat-embed-jasper</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
        <resources>
            <!--注册webapp目录为资源目录 -->
            <resource>
                <directory>src/main/webapp</directory>
                <targetPath>META-INF/resources</targetPath>
                <includes>
                    <include>**/*.*</include>
                </includes>
            </resource>
        </resources>
    </build>

</project>
```

## linux配置

### redis配置

[点我直达](https://www.cnblogs.com/chenyanbin/p/12073107.html)

### zookeeper配置

[点我直达](https://www.cnblogs.com/chenyanbin/p/12202048.html)

### linux启动服务

![](./images/images/img_046_5e98823ff659.png)

![](./images/images/img_047_9da8c2fc0a71.png)

## 数据库(Mysql)

![](./images/images/img_048_dcd853c0ed36.png)

## 项目演示

![](./images/images/img_049_28e021a41002.gif)

## 项目源码下载

链接:https://pan.baidu.com/s/1fii6As5638pwO_trZ6Bsjw  密码:xot2

# Dubbo监控平台的部署与使用

## 项目下载

官网地址：http://dubbo.apache.org/zh-cn/

![](./images/images/img_050_fcc7cd7e71af.gif)

百度云盘地址

```text
链接:https://pan.baidu.com/s/1P0QOhOz3-FeuPpR5fUjakw  密码:j0ek
```

　　下面需要使用控制台，演示用的mac电脑的终端，前期需在mac上安装maven，还不会的小伙伴，请看我另一篇博客，[点我直达](https://www.cnblogs.com/chenyanbin/p/12506889.html)

　　第一次打包会下载大量文件，安装过程中漫长，请耐心等待，请看我另一篇博客，[点我直达](https://www.cnblogs.com/chenyanbin/p/11706339.html)

## 控制台打包

**注意：打包前，需要改配置文件，修改zookeeper的ip地址！！！！！！**

![](./images/images/img_051_e559b1ca0bab.png)

![](./images/images/img_052_f5fcd8ee04cf.png)

![](./images/images/img_053_cc60dba1852b.gif)

**注：第一次打包，需下载很多包，耐心等待！！！！**

## 项目启动

### 将打包好的项目拖进linux

![](./images/images/img_054_465f4ac8c8fb.png)

### 启动

![](./images/images/img_055_b5715a3d4255.gif)

### 启动提供者和消费者项目

![](./images/images/img_056_c81e86dbb325.gif)
