{

  "title": "Spring Cloud 整合分布式链路追踪系统Sleuth和ZipKin实战，分析系统瓶颈",
  "date": "2020-11-14",
  "description": "导读 微服务架构中，是否遇到过这种情况，**服务间调用链过长**，导致**性能**迟迟**上不去**，不知道哪里出问题了，巴拉巴拉....，回归正题，今天我们使用SpringCloud组件，来分析一下微服务架构中系统调用的瓶颈问题~ SpringCloud链路追踪组件Sleuth实战 官网 主要功能",
  "tags": [
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/zipkin.html"

}

# 导读

　　微服务架构中，是否遇到过这种情况，**服务间调用链过长**，导致**性能**迟迟**上不去**，不知道哪里出问题了，巴拉巴拉....，回归正题，今天我们使用SpringCloud组件，来分析一下微服务架构中系统调用的瓶颈问题~

# SpringCloud链路追踪组件Sleuth实战

## 官网

![](images/img_001_80c2157d4426.gif)

![](images/img_002_587e70472a2f.gif)

　　主要功能：做日志埋点

## 什么是Sleuth

　　专门用于追踪每个请求的完整调用链路。

　　例如：【order-service,f674cc8202579a50,4727309367e0b514,false】

-

  - 第一个值：spring.application.name
  - 第二个值，sleuth生成的一个ID，交Trace ID，用来标识一条请求链路，一条请求链路中包含一个Trace ID，多个Span ID
  - 第三个值：spanid基本的工作单元，获取元数据，如发送一个http请求
  - 第四个值：false，是否要将该信息输出到zipkin服务中来收集和展示

## 添加依赖

　　牵扯到的服务都得加这个依赖！(我这里是在order-service、product-service加的依赖)

```text
        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-sleuth</artifactId>
        </dependency>
```

## 启动整个微服务测试

![](images/img_003_8ff6f3a4c1f8.gif)

![](images/img_004_1e464555e0bd.gif)

# 部署可视化链路追踪Zipkin

## 简介

　　大规模分布式系统的APM工具，基于Google Dapper的基础实现，和Sleuth结合可以提供可视化web界面分析调用链路耗时情况。

## 官网

[点我直达](https://zipkin.io/)

## 部署

[点我直达](https://zipkin.io/pages/quickstart.html)

![](images/img_005_f4aff92a978d.gif)

　　这里我使用下载源码的方式

```text
# get the latest source
git clone https://github.com/openzipkin/zipkin
cd zipkin
# Build the server and also make its dependencies
./mvnw -DskipTests --also-make -pl zipkin-server clean install
# Run the server
java -jar ./zipkin-server/target/zipkin-server-*exec.jar
```

## 备注

　　因为种种原因，从github上下载这个源码包，非常慢，可以使用这种方式解决：[点我直达](https://www.cnblogs.com/chenyanbin/p/13972475.html)

```text
git clone https://gitee.com/mirrors/zipkin.git

cd zipkin

mvn -DskipTests clean package

java -jar ./zipkin-server/target/zipkin-server-*exec.jar
```

![](images/img_006_240a1b74fed0.png)

## 启动

　　地址：ip:9411

![](images/img_007_0badd26c9f32.gif)

# Zpikin+Sleuth整合

## 添加依赖

　　涉及到的服务都得加！(我这里是在order-service、product-service加的依赖)

```text
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-zipkin</artifactId>
</dependency>
```

![](images/img_008_7a6b8b453c70.gif)

![](images/img_009_04ec16ee10be.gif)

### 注意

　　之前加过Sleuth依赖，现在加zipkin依赖，2.x的zipkin已经包含sleuth了，这里可以把之前的sleuth依赖去掉

![](images/img_010_25d1a50f2cf3.gif)

## 修改配置文件

　　默认指向的zipkin地址为本机地址：**http://localhost:9411/**

　　默认收集百分比为：**10%**

application.properties

```text
# 指定zipkin地址
spring.zipkin.base-url=http://localhost:9411/
# 配置采样百分比，开发环境可以设置：1，也就是100%，生产环境可以设置小一点
spring.sleuth.sampler.probability=1
```

![](images/img_011_078355452cff.gif)

## 启动并分析数据

**通过这个分析**，我们可以知道，**微服务中那个服务耗时多**，可以在这个服务上做性能优化，可以考虑加：**缓存、异步、算法**等等~

![](images/img_012_90f9f50d574d.gif)

![](images/img_013_29a8c8724458.gif)

![](images/img_014_880d1a43b9b9.gif)

# 源码下载

　　好了，今天先到这，只可意会不可言传，自己体会他的好处~

```text
链接: https://pan.baidu.com/s/1c4ZWufjmDgzgAAiOOzRg9A  密码: or12
```
