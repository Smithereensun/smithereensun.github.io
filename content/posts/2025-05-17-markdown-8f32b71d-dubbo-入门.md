{

  "title": "dubbo - 入门",
  "has_date": true,
  "description": "什么是Dubbo Dubbo是一个分布式、高性能、透明化的RPC服务框架，提供服务自动注册、自动发现等高效服务治理方案，可以和Spring框架无缝集成。Dubbo最常用的应用就是远程调用。 Dubbo中服务端最核心的对象有四个： ApplicationConfig**：配置当前应用信息 Protoc",
  "tags": [
    "微服务",
    "Dubbo"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/rpc/dubbo-basic - dubbo - 入门.md",
  "date": "2025-05-17"

}

## [什么是Dubbo](#什么是dubbo)

Dubbo是一个分布式、高性能、透明化的RPC服务框架，提供服务自动注册、自动发现等高效服务治理方案，可以和Spring框架无缝集成。Dubbo最常用的应用就是远程调用。

Dubbo中服务端最核心的对象有四个：

- **ApplicationConfig**：配置当前应用信息

- **ProtocolConfig**：配置提供服务的协议信息

- **RegistryConfig**：配置注册相关信息

- **ServiceConfig**：配置暴露的服务信息

Dubbo客户端中核心的对象有两个：

- **ApplicationConfig**：配置当前应用信息

- **ReferenceConfig**：配置引用的服务信息

## [Dubbo的主要应用场景](#dubbo的主要应用场景)

透明化的远程方法调用，就像调用本地方法一样调用远程方法，只需简单配置，没有任何API侵入。

软负载均衡及容错机制，可在内网替代F5等硬件负载均衡器，降低成本，减少单点。（F5负载均衡器我也是百度来的）。

服务自动注册与发现，不再需要写死服务提供方地址，注册中心基于接口名查询服务提供者的IP地址，并且能够平滑添加或删除服务提供者。

## [Dubbo的使用](#dubbo的使用)

接下来通过四种方式入门Dubbo。首先会通过原生API直接展示dubbo的直连和注册中心实现方式，接着使用Spring、注解和SpringBoot的方式分别展示如何使用Dubbo。

案例源码[点击这里](https://github.com//SpringBoot-Demo/tree/master/A11-spring-springboot-dubbo)

在写dubbo相关代码前，首先要定义一个**公共的api服务**，这个服务里存放的是service接口。服务提供者引入这个工程，写实现类，提供dubbo接口；服务消费者引入这个工程，通过这个工程的service接口调用。

User类：

UserService：

### [原生API](#原生api)

通过原生API的方式生成一个dubbo服务，并且用另外一个类去调用这个dubbo服务：

- 引入依赖

核心依赖就两个，一个dubbo的依赖，另外一个上面的公共接口方法，服务提供方和消费者都需要引入这两个依赖

- 服务提供者

服务提供者主要配置以下几个属性：

1. application：设置应用的名称等信息

1. protocol ：设置服务的协议

1. register：设置服务的连接方式

1. service：将需要暴露的服务注册出来

- 服务消费者

消费者的实现主要就三步：

1. 配置application：设置应用的名称等信息

1. 配置reference：主要配置要引用的信息

1. 获取到接口，调用服务。

先启动提供者，再启动消费者，如果user信息打印出来了就说明调用成功。

- 使用zookeeper作为注册中心

上面的Register使用的是直连的方式，也可以使用**注册中心**，这里以zookeeper为例。首先在项目中引入zookeeper相关依赖：

服务提供者修改一处地方，将RegistryConfig修改为zookeeper的连接方式

消费者同样修改一处位置，将referenceConfig中的setUrl方法替换为zookeeper：

### [Spring集成dubbo](#spring集成dubbo)

通过Spring的方式只不过是把上面写在Java中的代码拿到配置文件中去，并把接口注入到Bean容器中

- 引入spring相关依赖

在provider和consumer的模块下额外引入spring相关依赖

- 在resource文件夹下新建两个配置文件

provider.xml

consumer.xml

- 启动类

这里的配置文件和上方的代码均一一对应。服务的提供者和消费者：

SpringDubboProvider：

SpringDubboConsumer

### [纯注解版](#纯注解版)

注解的方式就是不在xml文件中注入bean，xml文件中只需要写包名即可

- provider修改
 provider.xml

UserService实现类

- consumer修改
 consumer.xml

controller类

### [SpringBoot集成dubo](#springboot集成dubo)

引入dubbo和springboot的核心依赖

- 服务提供者provider
 这里的配置都写在application.properties中：

服务提供者需要写服务的实现类，这里需要注意@Service注解采用的是dubbo包下：

接着在启动类上添加一个@EnableDubbo注解即可。

- 服务的消费者consumer

配置文件：

接着通过@Reference注解将service对象引进来

## [dubbo的常用配置](#dubbo的常用配置)

- xml配置

- springboot配置

更加具体的配置信息可以参考：[配置项参考手册 | Apache Dubbo](https://cn.dubbo.apache.org/zh-cn/overview/mannual/java-sdk/reference-manual/config/properties/)

## [企业中如何通过dubbo实现分布式调用](#企业中如何通过dubbo实现分布式调用)

在企业中，如果消费者直接通过RPC去调用提供者，理论上需要把提供者的整个Jar包引入到项目中。但是这样的话服务提供这种的其他无关代码也会被引入其中，导致代码污染。

因此实际开发过程中，**服务提供者和调用者之间会增加一层API模块**。这个API中主要写的是Service的接口定义，接口的返回实例对象以及接口的请求实例对象。简单来讲，**所有的定义都在API中完成**。

使用时，服务提供者引入这个API，然后写实现方法，服务消费者引入这个API，然后通过dubbo直接调用即可。

另外企业开发中，可能会出现多个接口实现，这种情况下可以给Service设定group、version等进行区分。
