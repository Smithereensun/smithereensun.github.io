{

  "title": "Nacos - 实现原理",
  "has_date": true,
  "description": "Nacos介绍 现在微服务架构是目前开发的一个趋势。服务消费者要去调用多个服务提供者组成的集群。这里需要做到以下几点： 服务消费者**需要在本地配置文件中维护服务提供者集群的每个节点的请求地址**。 服务提供者集群中如果某个节点宕机，**服务消费者的本地配置中需要同步删除这个节点的请求地址**，防止",
  "tags": [
    "微服务",
    "Nacos"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/service-registration-and-discovery/nacos-sourcecode - Nacos - 实现原理.md",
  "date": "2025-05-17"

}

## [Nacos介绍](#nacos介绍)

现在微服务架构是目前开发的一个趋势。服务消费者要去调用多个服务提供者组成的集群。这里需要做到以下几点：

1. 服务消费者**需要在本地配置文件中维护服务提供者集群的每个节点的请求地址**。

1. 服务提供者集群中如果某个节点宕机，**服务消费者的本地配置中需要同步删除这个节点的请求地址**，防止请求发送到已经宕机的节点上造成请求失败。

因此需要引入服务注册中心，它具有以下几个功能：

1. 服务地址的管理。

1. 服务注册。

1. 服务动态感知。

而Nacos致力于解决微服务中的统一配置，服务注册和发现等问题。**Nacos集成了注册中心和配置中心**。其相关特性包括：

1.
服务发现和服务健康监测：Nacos支持基于DNS和RPC的服务发现，即**服务消费者可以使用DNS或者HTTP的方式来查找和发现服务**。Nacos提供对服务的实时的健康检查，阻止向不健康的主机或者服务实例发送请求。**Nacos支持传输层（Ping/TCP）、应用层（HTTP、Mysql）的健康检查。**

1.
动态配置服务：动态配置服务可以**以中心化、外部化和动态化的方式管理所有环境的应用配置和服务配置。**

1.
动态DNS服务：支持权重路由，让开发者更容易的实现中间层的负载均衡、更灵活的路由策略、流量控制以及DNS解析服务。

1.
服务和元数据管理：Nacos允许开发者从微服务平台建设的视角来管理数据中心的所有服务和元数据。如：服务的生命周期、静态依赖分析、服务的健康状态、服务的流量管理、路由和安全策略等。

## [Nacos注册中心实现原理分析](#nacos注册中心实现原理分析)

### [Nacos架构图](#nacos架构图)

以下是Nacos的架构图：

![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/44df2ca2afb2-202410041142045.webp)其中分为这么几个模块：

-
**Provider APP**：服务提供者。

-
**Consumer APP**：服务消费者。

-
**Name Server**：通过Virtual IP或者DNS的方式实现Nacos高可用集群的服务路由。

-
**Nacos Server**：Nacos服务提供者。

-

  - OpenAPI：功能访问入口

  - Config Service：Nacos提供的配置服务模块

  - Naming Service：Nacos提供的名字服务模块

  - Consistency Protocol：一致性协议，用来实现Nacos集群节点的数据同步，使用Raft算法实现。

-
**Nacos Console**：Nacos控制台。

小总结：

- 服务提供者通过VIP（Virtual IP）访问Nacos Server高可用集群，基于OpenAPI完成服务的注册和服务的查询。

- Nacos Server的底层则通过数据一致性算法（Raft）来完成节点的数据同步。

### [注册中心的原理](#注册中心的原理)

首先，服务注册的功能体现在：

- 服务实例启动时注册到服务注册表、关闭时则注销（**服务注册**）。

- 服务消费者可以通过查询服务注册表来获得可用的实例（**服务发现**）。

- 服务注册中心需要调用服务实例的健康检查API来验证其是否可以正确的处理请求（**健康检查**）。

Nacos服务注册和发现的实现原理的图如下：
![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/63087a3499a0-202410041143101.webp)
## [Nacos服务注册源码](#nacos服务注册源码)

首先看下一个包：`spring-cloud-commons`

![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/3af6c8daf740-202410041143736.webp)**这个ServiceRegistry接口是SpringCloud提供的服务注册的标准，集成到SpringCloud中实现服务注册的组件，都需要实现这个接口。**来看下它的结构：

那么对于Nacos而言，该接口的实现类是`NacosServiceRegistry`，该类在这个pom包下：
![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/4c9c31e7e586-202410041143476.webp)
再回过头来看`spring-cloud-commons`包:
![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/03959b120abc-202410041143451.webp)
`spring.factories`**主要是包含了自动装配的配置信息**，如图：
![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/6a31599f6658-202410041143094.webp)
在spring.factories中配置EnableAutoConfiguration的内容后，项目在启动的时候，会导入相应的自动配置类，那么也就允许对该类的相关属性进行一个自动装配。那么显然，在这里导入了`AutoServiceRegistrationAutoConfiguration`这个类，而这个类顾名思义是**服务注册相关的配置类**。

该类的完整代码如下：

这里做一个分析，`AutoServiceRegistrationAutoConfiguration`中注入了`AutoServiceRegistration`实例，该类的关系图如下：![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/eaaf0945eabe-202405242005376.webp)

先来看一下这个抽象类`AbstractAutoServiceRegistration`：

这里实现了`ApplicationListener`接口，并且传入了`WebServerInitializedEvent`作为泛型，意思是：

- `NacosAutoServiceRegistration`监听`WebServerInitializedEvent`事件。

- **也就是WebServer初始化完成后**，会调用对应的事件绑定方法，调用`onApplicationEvent（）`，该方法最终调用`NacosServiceRegistry`的`register（）`方法（`NacosServiceRegistry`实现了Spring的一个服务注册标准接口）。

对于`register（）`方法，主要调用的是Nacos Client SDK中的**NamingService下的registerInstance（）方法完成服务的注册**。

再来看一下心跳监测的方法`addBeatInfo（）`：

心跳检查如果正常，即代表这个需要注册的服务是健康的，那么执行下面的注册方法`registerInstance（）`：

### [案例1：用Debug来理解Nacos服务注册流程](#案例1-用debug来理解nacos服务注册流程)

下面直接Debug走一遍：

- 启动一个Nacos服务。

- 搞一个Maven项目，集成Nacos。

1.
项目初始化后，根据上文说法，会执行抽象类`AbstractAutoServiceRegistration`下面的`onApplicationEvent（）`方法，**即事件被监听到。**![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/ca55e171b53c-202405242005418.webp)

1.
作为抽象类的子类实现`NacosAutoServiceRegistration`，监听到Web服务启动后， 开始执行`super.register（）`方法。![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/e1e4628b80bb-202405242005344.webp)

1.
执行`NacosServiceRegistry`下的`register（）`方法（**super**)，前面说过，集成到SpringCloud中实现服务注册的组件，都需要实现`ServiceRegistry`这个接口，而对于Nacos而言，`NacosServiceRegistry`就是具体的实现子类。执行注册方法需要传入的三个参数：

- 实例名称serviceId。

- 实例归属的组。

- 具体实例

![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/adaf440fb26f-202405242005354.webp)
而`registerInstance（）`主要做两件事：

- 检查服务的健康（`this.beatReactor.addBeatInfo（）`）。

- 执行服务的注册（`this.serverProxy.registerService（）`）。

![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/77df16311a67-202405242005430.webp)
服务健康的检查：![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/04e0b8b54dc3-202405242005400.webp)

检查通过后，发送OpenAPI进行服务的注册：![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/290b88188671-202405242005178.webp)

### [服务注册小结](#服务注册小结)

通过问答的形式来进行总结

1.
**Nacos的服务注册为什么和spring-cloud-commons这个包扯上关系？**

  1. 首先，Nacos的服务注册肯定少不了pom包：spring-cloud-starter-alibaba-nacos-discovery吧。这个包下面包括了spring-cloud-commons包，那么这个包有什么用？

  1. spring-cloud-commons中有一个接口叫做ServiceRegistry，而集成到SpringCloud中实现服务注册的组件，都需要实现这个接口。

  1. 因此对于需要注册到Nacos上的服务，也需要实现这个接口，那么具体的实现子类为NacosServiceRegistry。

1.
**为什么项目加了这几个依赖，服务启动时依旧没有注册到Nacos中？**

  1. 进行Nacos服务注册的时候，会有一个事件的监听过程，而监听的对象是WebServer，因此，这个项目需要是一个Web项目

  1. 因此需要查看pom文件中是否有依赖：spring-boot-starter-web

1.
**spring-cloud-commons这个包还有什么作用？**

  1. 这个包下的spring.factories文件中，配置了相关的服务注册的置类，即支持其自动装配。

  1. 这个配置类叫做AutoServiceRegistrationAutoConfiguration。其注入了类AutoServiceRegistration，而NacosAutoServiceRegistration是该类的一个具体实现。

  1. 当WebServer初始化的时候，通过绑定的事件监听器，会实现监听，执行服务的注册逻辑。

说白了：

1. 第一件事情：引入一个Spring监听器，当容器初始化后，执行Nacos服务的注册。

1. 第二件事情：而Nacos服务注册的方法的实现，其需要实现的接口来自于该包下的`ServiceRegistry`接口。

接下来就对Nacos注册的流程进行一个总结：

1. 服务（项目）启动时，根据`spring-cloud-commons`中`spring.factories`的配置，自动装配了类`AutoServiceRegistrationAutoConfiguration`。

1. `AutoServiceRegistrationAutoConfiguration`类中注入了类`AutoServiceRegistration`，其最终实现子类实现了Spring的监听器。

1. 根据监听器，执行了服务注册方法。而这个服务注册方法则是调用了`NacosServiceRegistry`的`register（）`方法。

1. 该方法主要调用的是Nacos Client SDK中的`NamingService`下的`registerInstance（）`方法完成服务的注册。

1. `registerInstance（）`方法主要做两件事：**服务实例的健康监测和实例的注册。**

1. 通过`schedule（）`方法**定时的发送数据包，检测实例的健康。**

1. 若健康监测通过，调用`registerService（）`方法，通过OpenAPI方式执行服务注册，其中将实例Instance的相关信息存储到HashMap中。

## [Nacos服务发现源码](#nacos服务发现源码)

有一点我们需要清楚：Nacos服务的发现发生在什么时候。例如：微服务发生远程接口调用的时候。一般我们在使用OpenFeign进行远程接口调用时，都需要用到对应的微服务名称，而这个名称就是用来进行服务发现的。

举个例子：

接下来直接开始讲重点，Nacos在进行服务发现的时候，会调用`NacosServerList`类下的`getServers()`方法：

接下来来看一下`NacosNamingService.selectInstances（）`方法：

该方法最终会调用到其**重载方法**：

这里应该重点关注`this.hostReactor`这个对象，它里面比较重要的是几个Map类型的存储结构：

再看一看它的`getServiceInfo（）`方法：

来看下`scheduleUpdateIfAbsent（）`方法：

### [案例2：用Debug来理解Nacos服务发现流程](#案例2-用debug来理解nacos服务发现流程)

1.
进行远程接口调用，触发服务的发现，调用`NacosServerList`的`getServers（）`方法。**传入的serviceId和对应Feign接口上的接口@FeignClient中的名称一致。**![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/efc2e883702e-202405242005207.webp)

1.
例如，这里调用的Feign接口是：

这里可以看出来，返回的是一个Instance类型的List，对应的服务也发现并返回了。![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/42a41a7743e5-202405242036082.webp)

1.
这里则调用了`NacosNamingService`的`selectInstances（）`方法，我这里的subscribe值是true，**即代表我这个消费者直接订阅了这个服务，因此最终的信息是从本地Map中获取，即Nacos维护了一个注册列表。**!

1.
再看下`HostReactor的getServiceInfo（）`方法：最终所需要的结果是从serviceInfoMap中获取，并且**通过多个Map进行维护服务实例，若存在数据的变化，还会通过强制睡眠5秒钟的方式来等待数据的更新。**![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/ca7087f0634a-202405242005382.webp)

1.
无论怎样都会调用`this.scheduleUpdateIfAbsent(serviceName, clusters)`方法：![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/24234489b540-202405242005461.webp)

1.
通过`scheduleUpdateIfAbsent（）`方法定时的获取实时的实例数据，并且负责维护本地的服务注册列表，若服务发生更新，则更新本地的服务数据。![](/imported/markdown/2025-05-17-markdown-2b90f0a1-nacos-实现原理/images/38270053861a-202405242005517.webp)

### [服务发现小结：](#服务发现小结)

经常有人说过，Nacos有个好处，就是当一个服务挂了之后，短时间内不会造成影响，因为有个本地注册列表，在服务不更新的情况下，服务还能够正常的运转，其原因如下：

1. Nacos的服务发现，一般是**通过订阅的形式来获取服务数据**。

1. 而通过订阅的方式，**则是从本地的服务注册列表中获取（可以理解为缓存）**。相反，如果不订阅，那么服务的信息将会从Nacos服务端获取，这时候就需要对应的服务是健康的。（宕机就不能使用了）

1. **在代码设计上，通过Map来存放实例数据，key为实例名称，value为实例的相关信息数据（ServiceInfo对象）。**

最后，服务发现的流程就是：

1.
以调用远程接口（OpenFeign）为例，当执行远程调用时，需要经过服务发现的过程。

1.
服务发现先执行`NacosServerList`类中的`getServers()`方法，根据远程调用接口上@FeignClient中的属性作为serviceId传入`NacosNamingService.selectInstances（）`方法中进行调用。

1.
**根据subscribe的值来决定服务是从本地注册列表中获取还是从Nacos服务端中获取。**

1.
以本地注册列表为例，通过调用`HostReactor.getServiceInfo（）`来获取服务的信息（serviceInfo），Nacos本地注册列表由3个Map来共同维护。

  1. 本地Map–&gt;serviceInfoMap，

  1. 更新Map–&gt;updatingMap

  1. 异步更新结果Map–&gt;futureMap,

  1. 最终的结果从serviceInfoMap当中获取。

1.
HostReactor类中的`getServiceInfo（）`方法通过`this.scheduleUpdateIfAbsent()` 方法和`updateServiceNow（）`方法实现服务的**定时更新和立刻更新。**

1.
而对于**scheduleUpdateIfAbsent（）方法，则通过线程池来进行异步的更新**，将回调的结果（Future）保存到futureMap中，并且发生提交线程任务时，还负责更新本地注册列表中的数据。
