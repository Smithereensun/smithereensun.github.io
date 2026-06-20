{

  "title": "Feign远程调用",
  "has_date": true,
  "description": "基于Netflix Feign 实现，整合了Spring Cloud Ribbon 与Spring Cloud Hystrix， 它提供了一种声明式服务调用的方式。 先来看我们以前利用RestTemplate发起远程调用的代码： 存在下面的问题： 代码可读性差，编程体验不统一 参数复杂URL难以维护",
  "tags": [
    "微服务"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/springcloud/feign - Feign远程调用.md",
  "date": "2025-03-29"

}

基于Netflix Feign 实现，整合了Spring Cloud Ribbon 与Spring Cloud Hystrix， 它提供了一种声明式服务调用的方式。

先来看我们以前利用RestTemplate发起远程调用的代码：
![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/96c1f6545598-202501011141062.png)
存在下面的问题：

- 代码可读性差，编程体验不统一

- 参数复杂URL难以维护

Feign是一个声明式的http客户端，官方地址：[https://github.com/OpenFeign/feign](https://github.com/OpenFeign/feign)

其作用就是帮助我们优雅的实现http请求的发送，解决上面提到的问题。

**什么是声明式，有什么作用，解决什么问题**？声明式调用就像调用本地方法一样调用远程方法;无感知远程 http 请求。

1. Spring Cloud 的声明式调用, 可以做到使用 HTTP 请求远程服务时能就像调用本地方法一样的体验，开发者完全感知不到这是远程方法，更感知不到这是个 HTTP 请求。

1. 它像 Dubbo 一样，consumer 直接调用接口方法调用 provider，而不需要通过常规的Http Client 构造请求再解析返回数据。

1. 它解决了让开发者调用远程接口就跟调用本地方法一样，无需关注与远程的交互细节，更无需关注分布式环境开发。

## [Feign替代RestTemplate](#feign替代resttemplate)

Fegin的使用步骤如下：

### [引入依赖](#引入依赖)

我们在order-service服务的pom文件中引入feign的依赖：

### [添加注解](#添加注解)

在order-service的启动类添加注解开启Feign的功能，@EnableFeignClients

### [编写Feign的客户端](#编写feign的客户端)

在order-service中新建一个接口，内容如下：

这个客户端主要是基于SpringMVC的注解来声明远程调用的信息，比如：

- 服务名称：userservice

- 请求方式：GET

- 请求路径：/user/{id}

- 请求参数：Long id

- 返回值类型：User

这样，Feign就可以帮助我们发送http请求，无需自己使用RestTemplate来发送了。

### [测试](#测试)

修改order-service中的OrderService类中的queryOrderById方法，使用Feign客户端代替RestTemplate：
![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/d5143e8864f6-202501011143736.png)
是不是看起来优雅多了。

### [总结](#总结)

使用Feign的步骤：

1. 引入依赖

1. 添加@EnableFeignClients注解

1. 编写FeignClient接口

1. 使用FeignClient中定义的方法代替RestTemplate

## [自定义配置](#自定义配置)

Feign可以支持很多的自定义配置，如下表所示：
类型作用说明feign.Logger.Level修改日志级别包含四种不同的级别：NONE、BASIC、HEADERS、FULLfeign.codec.Decoder响应结果的解析器http远程调用的结果做解析，例如解析json字符串为java对象feign.codec.Encoder请求参数编码将请求参数编码，便于通过http请求发送feign. Contract支持的注解格式默认是SpringMVC的注解feign. Retryer失败重试机制请求失败的重试机制，默认是没有，不过会使用Ribbon的重试
一般情况下，默认值就能满足我们使用，如果要自定义时，只需要创建自定义的@Bean覆盖默认Bean即可。

下面以日志为例来演示如何自定义配置。

### [配置文件方式](#配置文件方式)

基于配置文件修改feign的日志级别可以针对单个服务：

也可以针对所有服务：

而日志的级别分为四种：

- NONE：不记录任何日志信息，这是默认值。

- BASIC：仅记录请求的方法，URL以及响应状态码和执行时间

- HEADERS：在BASIC的基础上，额外记录了请求和响应的头信息

- FULL：记录所有请求和响应的明细，包括头信息、请求体、元数据。

### [Java代码方式](#java代码方式)

也可以基于Java代码来修改日志级别，先声明一个类，然后声明一个Logger.Level的对象：

如果要**全局生效**，将其放到启动类的@EnableFeignClients这个注解中：

如果是**局部生效**，则把它放到对应的@FeignClient这个注解中：

## [Feign使用优化](#feign使用优化)

Feign底层发起http请求，依赖于其它的框架。其底层客户端实现包括：

- URLConnection：默认实现，不支持连接池

- Apache HttpClient ：支持连接池

- OKHttp：支持连接池

因此提高Feign的性能主要手段就是使用**连接池**代替默认的URLConnection。

这里我们用Apache的HttpClient来演示。

### [引入依赖](#引入依赖-1)

在order-service的pom文件中引入Apache的HttpClient依赖：

### [配置连接池](#配置连接池)

在order-service的application.yml中添加配置：

接下来，在FeignClientFactoryBean中的loadBalance方法中打断点：
![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/d984c4ff512b-202501011143731.png)
Debug方式启动order-service服务，可以看到这里的client，底层就是Apache HttpClient：
![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/6a31729a5e02-202501011143728.png)
总结，Feign的优化：

1. 日志级别尽量用basic

1. 使用HttpClient或OKHttp代替URLConnection

  1. 引入feign-httpClient依赖

  1. 配置文件开启httpClient功能，设置连接池参数

## [最佳实践](#最佳实践)

所谓最佳实践，就是使用过程中总结的经验，最好的一种使用方式。

Feign的客户端与服务提供者的controller代码非常相似：

feign客户端：
![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/60b42a02a5f7-202501011143747.png)
UserController：
![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/c8d65d2450e0-202501011143749.png)
有没有一种办法简化这种重复的代码编写呢？

### [继承方式](#继承方式)

一样的代码可以通过继承来共享：

1. 定义一个API接口，利用定义方法，并基于SpringMVC注解做声明。

1. Feign客户端和Controller都集成改接口

![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/e9627152d5a3-202501011143756.png)
优点：

- 简单

- 实现了代码共享

缺点：

- 服务提供方、服务消费方紧耦合

- 参数列表中的注解映射并不会继承，因此Controller中必须再次声明方法、参数列表、注解

### [抽取方式](#抽取方式)

将Feign的Client抽取为独立模块，并且把接口有关的POJO、默认的Feign配置都放到这个模块中，提供给所有消费者使用。

例如，将UserClient、User、Feign的默认配置都抽取到一个feign-api包中，所有微服务引用该依赖包，即可直接使用。
![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/b5b8d9d8977a-202501011143329.png)
#### [抽取](#抽取)

首先创建一个module，命名为feign-api，

项目结构：
![](/imported/markdown/2025-03-29-markdown-4636d94f-feign远程调用/images/0ba741d768c9-202501011144035.png)
在feign-api中然后引入feign的starter依赖

然后，order-service中编写的UserClient、User、DefaultFeignConfiguration都复制到feign-api项目中

#### [在order-service中使用feign-api](#在order-service中使用feign-api)

首先，删除order-service中的UserClient、User、DefaultFeignConfiguration等类或接口。

在order-service的pom文件中中引入feign-api的依赖：

修改order-service中的所有与上述三个组件有关的导包部分，改成导入feign-api中的包

#### [重启测试](#重启测试)

重启后，发现服务报错了

这是因为UserClient现在在cn..feign.clients包下，

而order-service的@EnableFeignClients注解是在cn..order包下，不在同一个包，无法扫描到UserClient。

#### [解决扫描包问题](#解决扫描包问题)

方式一：

指定Feign应该扫描的包：

方式二：

指定需要加载的Client接口：
