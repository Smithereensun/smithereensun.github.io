{

  "title": "dubbo - 服务暴露源码",
  "has_date": true,
  "description": "Dubbo 调用图解 dubbo的调用图（来自官网），如下图，共包含了5个模块 Provider 服务提供方 Registry 服务注册中心（**这里可以认为是zookeeper** Consumer 服务使用方 Container 服务提供方的容器 Monitor 服务监控中心 服务调用流程** ",
  "tags": [
    "微服务",
    "Dubbo"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/rpc/dubbo-serviceexposure-sourcecode - dubbo - 服务暴露源码.md",
  "date": "2025-05-17"

}

## [Dubbo 调用图解](#dubbo-调用图解)

dubbo的调用图（来自官网），如下图，共包含了5个模块
![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/f767f468df1c-202404301933480.png)

- Provider 服务提供方

- Registry 服务注册中心（**这里可以认为是zookeeper**

- Consumer 服务使用方

- Container 服务提供方的容器

- Monitor 服务监控中心

**服务调用流程**

1. 提供服务的容器启动之后，把该服务提交给服务提供方

1. 服务提供方把该服务细节以约定的协议（此处可认为是dubbo协议）把IP、端口、服务名等等上报给服务注册中心，由服务注册中心统一管理（另外存在心跳检测，便于及时了解服务健康情况；服务均衡负责等也由其管理）

1. 服务调用方从服务注册中心获取到一个可用的服务提供方的信息

1. 服务注册中心把合适的服务提供方的细节信息下发到调用方

1. 服务调用方持有服务提供方的调用信息，可直连服务提供方进行invoke调用操作

1. 服务提供方以及服务调用方的调用情况，在必备的情况下都可以定时上报到监控中心，从而了解服务调用的数据统计情况

接着把上述过程模块化，细化出来，如下图
![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/5f2075426af2-202404301933235.png)
## [引入](#引入)

从spring解析xml开始，我们能够很明显的查看到DubboNamespaceHandler文件

在为外界暴露服务的时候，常使用&lt;dubbo:service interface="[com.XXX](http://com.XXX)" ref="xXXX" /&gt;，再结合DubboBeanDefinitionParser类的parse细节，可知服务暴露，我们应该关注的类是**ServiceBean.class**

## [ServiceBean 介绍](#servicebean-介绍)

如下图，是ServiceBean类的继承关系图，右边圈出来的是关于dubbo的，下面底部的是和spring有关的。
![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/6e617f4c8990-202404301933709.png)
很清楚的看到serviceBean也是一个可由Spring管理的很普通的bean

- 通过BeanNameAware修改bean的名称

- ApplicationContextAware去获取Spring IOC的容器

- IntializingBean的afterPropertiesSet去自定义实现bean的实例对象

- ApplicationListener的onApplicationEvent接收各种事件

- DisposableBean的destroy去销毁bean

右侧则和dubbo有关，一层一层的config扩展实例化，包含了在xml配置中的各种参数配置。

### [属性](#属性)

属性是整个的服务暴露的这个ServiceBean包含的各种属性信息，xml配置信息都会合并到这个属性中

**ServiceConfig 类**

- 方法配置参数methods,一般情况下是没有设置的，也就意味着该接口下的所有的方法都会被暴露出去，如果设置了就意味着设置的方法才会被暴露出去。

- 提供方配置provider也是负责服务暴露方的一些熟悉信息，例如负载均衡等信息。

**AbstractServiceConfig 类**

其中protocols就是常说的dubbo协议了，这里指明list也就是意味着支持**可以同时多种协议对外暴露**

**AbstractInterfaceConfig 类**

注册中心registries应该是比较重要的属性信息了，包含了注册中心的数据，比如设置zk的相关属性信息，后期暴露也主要是把服务按照约定的协议推送给注册中心。

其他继承的类的属性更多的是涉及到系统管理、监控等层级的属性，在此不做过多介绍了

### [配置注入](#配置注入)

bean继承了IntializingBean，那肯定就使用了afterPropertiesSet方法

注意在运行到这个时候，servicebean实例化是已经完成了的。

在这一段代码中就是从Spring IOC容器中获取合适的bean注入到ServiceBean中，例如使用的服务信息、服务注册中心、使用的协议、均衡负责的方式（provider的loanBanance）、监控等。

## [暴露服务启动](#暴露服务启动)

服务暴露其实就是export函数，如果设置了延迟，则会在ApplicationListener的事件中去暴露服务。

**ServiceConfig 类**

在doExport方法中更多的是对一些数据的check操作，随后来到了doExportUrls方法

## [服务注册中心属性获取](#服务注册中心属性获取)

**AbstractInterfaceConfig 类**

最后生成的 registryList 数据可能为 registry://127.0.0.1:2182/com.alibaba.dubbo.registry.RegistryService?application=dubbo-demo&client=zkclient&dubbo=2.5.3&group=dubbo-demo&owner=jwfy&pid=2772®istry=zookeeper×tamp=1525276569763

仅仅是包含了一些注册的基本数据

## [服务暴露](#服务暴露)

现在来到了doExportUrlsFor1Protocol方法，当前protocolConfig为
![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/4bd4e85aba02-202404301934648.png)
### [本地服务暴露](#本地服务暴露)

本地服务暴露的入口是exportLocal(url);

现在应该是来到了真正服务暴露的入口了，`Exporter&lt;?&gt; exporter = protocol.export(proxyFactory.getInvoker(ref, (Class) interfaceClass, local))`;

### [protocol & proxyFactory](#protocol-proxyfactory)

根据之前对dubbo spi的学习和了解，到这里已经知道了protocol和proxyFactory指的具体是什么了。

**protocol 类**

**proxyFactory 类**

可以很明显的看出来默认的protocol是使用的dubbo协议，对应的实例是包装DubboProtocol后的实例，ProxyFactory使用的是javassist，对应的实例是JavassistProxyFactory

**暴露操作包含了两个部分，一个Invoke,另一个是export**

## [获取Invoke](#获取invoke)

### [JavassistProxyFactory获取Invoke](#javassistproxyfactory获取invoke)

proxyFactory.getInvoker(ref, (Class) interfaceClass, local) 方法获得具体的Invoke。

此时的ref是暴露的具体实现类，interfaceClass是对应的接口信息，local就是URL信息，具体内容是

registry://127.0.0.1:2182/com.alibaba.dubbo.registry.RegistryService?application=dubbo-demo&client=zkclient&dubbo=2.5.3&export=dubbo%3A%2F%2F172.16.109.110%3A20880%2Fcom.jwfy.dubbo.product.ProductService%3Fanyhost%3Dtrue%26application%3Ddubbo-demo%26default.loadbalance%3Drandom%26dubbo%3D2.5.3%26interface%3Dcom.jwfy.dubbo.product.ProductService%26methods%3Dprint%2CgetStr%26owner%3Djwfy%26pid%3D13859%26side%3Dprovider%26timestamp%3D1525772505371%26token%3Dfdfdf&group=dubbo-demo&owner=jwfy&pid=13859®istry=zookeeper×tamp=1525772500246

需要对外暴露的服务就是包含在URL信息中的ProductService信息

在本demo中，getInvoke操作获取到JavassistProxyFactory对象后执行他的getInvoke操作

**JavassistProxyFactory 类**

生产的invoke对象其实是个AbstractProxyInvoker，只不过在调用他的doInvoke操作时，最后会执行拼接生成的wrapper对象的invokeMethod方法上。

**getWrapper**

在获取wrapper操作，也同样是**动态拼接字符串生成**的，重点看其中的invokeMethod方法

现在应该就很清楚了，在执行invokeMethod的时候，**背后其实就是调用了实现类的对应方法**，只是这个wrapper本身是动态生成的

### [JdkProxyFactory获取Invoke](#jdkproxyfactory获取invoke)

上面说了在动态生成的代理工厂中默认实现的是JavassistProxyFactory，但是也可以使用java本身的协议，也就是JdkProxyFactory

完全就是通过java的反射去调用执行

### [Invoke是什么](#invoke是什么)

其实刚刚开始看源码的时候并不是非常的理解Invoke到底是个什么，现在可以说Invoke是**实现类的包装类，并包含了URL等信息**，后续可以通过invoke方法去调用具体服务方。
![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/a1567a5bd29a-202404301934939.png)
## [Invoke暴露为export](#invoke暴露为export)

### [获取真实的Protocol类](#获取真实的protocol类)

protocol.export(invoke),其中的invoke就是上面生成的抽象invoke类,**可是在单步调试的时候却发现并没有直接进入到我们设想的RegistryProtocol类中**

这个需要追踪到Dubbo SPI中的cachedWrapperClasses数据处理中
![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/6e6375f59676-202404301935300.png)
上述代码已经很清楚了，获取wrapper，首先不应该被Adaptive注解（未贴出），其次一定得存在包含了**参数为type的构造函数**，而如下文件则是protocol的spi文件，可以知道只有filter和listener符合操作
![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/ce2225240f9c-202404301935396.png)![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/19be942028c7-202404301935837.png)
这样就非常清楚了，在获取getExtension中，应该是获取到了RegistryProtocol对象，但是后续的cachedWrapperClasses操作又加上了包装操作，先后加入了ProtocolFilterWrapper、ProtocolListenerWrapper对象，使得在后续protocol.export操作不是进入到RegistryProtocol中，而是首先进入到ProtocolFilterWrapper

**ProtocolFilterWrapper 类**

**然后来到了ProtocolListenerWrapper类**

### [注册协议暴露](#注册协议暴露)

不经过任何处理，通过两个wrapper的转发，直接来到RegistryProtocol的export操作

#### [获取远程控制中心地址 getRegistry](#获取远程控制中心地址-getregistry)

registryFactory 同样是在RegistryProtocol实例完后注入的动态对象

对应实现的对象是ZookeeperRegistryFactory，调用其getRegistry方法，来到了AbstractRegistryFactory类

**AbstractRegistry 类**
![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/ed985f7e5ca6-202404301935660.png)![](/imported/markdown/2025-05-17-markdown-de057765-dubbo-服务暴露源码/images/243fb72bc3ad-202404301936156.png)
来到订阅notify方法

**FailbackRegistry 类**

链接失败时，进行重试的操作就是在这里进行的，retry就是获取当前registry中的failedRegistered等信息，如果failedRegistered中有URL信息存在，意味着之前存在链接失败的情况，现在执行retry进行重连操作

**ZookeeperRegistry 类**

通过上述操作得到的注册中心对象实例，并且其URL为zookeeper://127.0.0.1:2182/com.alibaba.dubbo.registry.RegistryService?application=dubbo-demo&client=zkclient&dubbo=2.5.3&group=dubbo-demo&interface=com.alibaba.dubbo.registry.RegistryService&owner=jwfy&pid=12663×tamp=1525733671009

#### [注册到注册中心](#注册到注册中心)

从invoke对错获取的注册URL是dubbo://192.168.10.123:20880/com.jwfy.dubbo.product.ProductService?anyhost=true&application=dubbo-demo&default.loadbalance=random&dubbo=2.5.3&interface=com.jwfy.dubbo.product.ProductService&methods=print,getStr&owner=jwfy&pid=12663&side=provider×tamp=1525733684167&token=fdfdf

其包含了当前bean的基本信息，把这些信息提交给注册中心，服务使用方就可以获取到这些数据，然后反转生成invoke去调用执行

**FailbackRegistry 类**

以下就是zk的输出日志，可以很清晰的看到确实创建了节点信息

到这里服务注册到注册中心就已经完成了，同时还伴随着从文件加载注册信息和保存注册信息，可自行通过zKcli命令去

#### [暴露服务之注册](#暴露服务之注册)

在上面的protocol.export操作中，protocol也不是DubboProtocol本身，而是包装了ProtocolFilterWrapper、ProtocolListenerWrapper，协议不是register，各种处理之后进入到DubboProtocol的export进行暴露操作。

#### [网络端口开启](#网络端口开启)

**DubboProtocol 类**

**Exchangers 类**

**HeaderExchanger 类**

其中Transporters.bind会先获取当前可用的其中Transporters，默认也是NettyTransporter对象，调用其bind方法

new NettyServer(url, listener)，来到了AbstractServer类

其最终返回一个NettyService,服务端已经开启了，客户端可以连接了，继续跳入到HeaderExchangeServer中

#### [开启心跳检测](#开启心跳检测)

**HeaderExchangeServer 类**

心跳检测最后真正执行的任务是如下代码

**HeartBeatTask 类**

到此整个的服务暴露就全部结束了

## [总结](#总结)

### [Spring](#spring)

基于spring开发，做到无缝对接spring，在使用上只有极少数的xml配置学习成本，在Dubbo内部继承了若干个类，自定义实现的xsd和配套的解析方法等。**如果以后需要接入自定义的NameSpaceContext，同样需要类似的处理**

- 通过BeanNameAware修改bean的名称

- ApplicationContextAware去获取Spring IOC的容器

- IntializingBean的afterPropertiesSet去自定义实现bean的实例对象

- ApplicationListener的onApplicationEvent接收各种事件

- DisposableBean的destroy去销毁bean

获取Spring IOC容器之后，在自定义实现dubbo的服务bean时，就可以获取到系统配置的注册中心、使用的协议、均衡负责等内容（对注册中心、协议等对Spring而言只是个普通的bean而言），这样就可以完成对ServiceBean的属性输入。

### [SPI](#spi)

虽然也介绍过SPI的整个的处理细节，在整个的dubbo中也确实大量使用中。可是真正的在调试服务暴露中还是有不少细节被忽略掉了。

- 基本上所有的类都有通过拼接代码字符串再编译生成其对象

- 动态生成的对象其实并没有做很多事情，只是根据配置的xml参数，动态决定选取合适的实现类，再调用其方法

- 参数注入和spring的参数注入方法不一样的是，dubbo是获取类的所有set开头同时参数只有1个的公共方法，通过SPI取到参数的值，然后反射invoke注入的

- Dubbo为了一些附加的功能，存在包装类的情况，每一个接口都有wrapper的存在，如果存在则最后返回的对象不是对象本身，而是经过层层包装产生的对象，例如Protocol

### [服务暴露流程](#服务暴露流程)

如果是我们去完成这个任务会怎么去做呢？有两点肯定是要实现的

- 注册中心，需要把服务提供方的信息推送给注册中心统一管理，服务调用方能够感知到存在这个服务

- 对外的网络端口，可通过套接字和外界（服务调用方）发生信息交换

服务调用方感知到服务的存在，然后获取其服务的套接字信息，然后直接通过网络IO完成信息交换

Dubbo其实也基本上按照这种思路来实现的，只是支持了多种协议，并且还有监控、统计等功能，层次分明。

#### [获取注册中心](#获取注册中心)

注册中心的基本配置就是在xml配置的**dubbo:registry**,生成的URL也是注册协议的URL，例如，registry://127.0.0.1:2182/com.alibaba.dubbo.registry.RegistryService?application=dubbo-demo&client=zkclient&dubbo=2.5.3&group=dubbo-demo&owner=jwfy&pid=2772®istry=zookeeper×tamp=1525276569763 会把一个dubbo的xml配置的基本信息给提取出去

#### [服务信息的组装](#服务信息的组装)

既然注册中心已经准备好了，那现在就需要处理我们对外暴露的service信息，对外暴露服务也需要配置的，这个配置就是从**dubbo:protocol**来的。

这个配置会告诉系统，所有对外暴露的IO读取协议是什么，默认的是dubbo，其实也支持redis、http等

**是处理IO数据流方式的协议**

不过，如果没有IP、端口等数据，则从**dubbo:provider**提取

再配置其他属性数据，生成的URL，例如dubbo://172.16.109.110:20880/com.jwfy.dubbo.product.ProductService?anyhost=true&application=dubbo-demo&default.loadbalance=random&dubbo=2.5.3&interface=com.jwfy.dubbo.product.ProductService&methods=print,getStr&owner=jwfy &pid=2772&side=provider×tamp=1525313423899

这个对外的服务使用的暴露的接口、具体可以被调用的函数 属于提供方

#### [服务IO端口提供](#服务io端口提供)

既然网络IO端的协议数据已经准备好了，那就可以开启，等待服务方的调用

这点可以直接跳到DubboProtocol类的export操作了（以Dubbo协议为例子）

针对每一个URL都提取出一个key，然后存储对应的invoker、url等信息

真正操作中取的是服务名+协议端口为key，DubboExporter为value的一个map，后续就可以通过key反取出invoke对象

接下来就是使用哪种Transporter操作了，默认是使用了netty的NettyTransporter（netty是一种基于java开发的异步的、事件驱动的高效的网络IO框架），如果需要使用其他的IO框架，则需要在**dubbo:provider**设置service字段

现在网络对外的协议Netty已经准备好了，服务信息也已经准备好了，那接下来就按照特定的格式decode操作，把数据转变为字节流，由netty向外开放出来即可

由此服务调用方就可以通过网络IO 链接到服务提供方上

#### [服务的注册](#服务的注册)

服务的注册是另一个操作，也就是把当前提供的服务告诉给注册中心，后续服务调用方就可以订阅注册中心，从而知道有哪些服务了，当前例子是使用了zookeeper作为注册中心

现在我们知道的是对外暴露服务的url信息（也就是invoke对象中的url）

所以操作也就很明显了，**先获取到注册中心的配置信息，然后把服务url信息转为zk协议的url信息，最后连接到注册中心，注册保存即可**

这里面就有使用zookeeper的jar包功能，需要和注册中心交互的操作

此外还有些附属的功能，例如超时重试、连接信息的保存和读取（如果注册中心突然出现问题，服务端和客户端还可以利用本地文件缓存继续工作，只是不能再实时获取最新的订阅信息罢了）

一般本地的连接信息存储在/Users/XXX/.dubbo中，如果出现了无法注册无法调用的情况，可以考虑删除该文件重启服务
