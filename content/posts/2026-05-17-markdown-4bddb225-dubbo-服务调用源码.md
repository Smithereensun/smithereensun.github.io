{

  "title": "dubbo - 服务调用源码",
  "has_date": true,
  "description": "调用过程 dubbo的服务调用方是在xml配置了类似于 的配置，意味着后续在spring中通过 就可以获取到远程代理对象。 本身映射成为的bean是ReferenceBean，其会存储整个dubbo需要的各种信息，例如控制中心的注册地址，服务端的具体IO和端口等。 如上图就是ReferenceBea",
  "tags": [
    "微服务",
    "Dubbo"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/rpc/dubbo-servicenvocation-sourcecode - dubbo - 服务调用源码.md",
  "date": "2026-05-17"

}

## [调用过程](#调用过程)

dubbo的服务调用方是在xml配置了类似于 `&lt;dubbo:reference interface="com.jwfy.dubbo.product.ProductService" id="productService" /&gt;`的配置，意味着后续在spring中通过 `getBean('productService')` 就可以获取到远程代理对象。`dubbo:reference` 本身映射成为的bean是ReferenceBean，其会存储整个dubbo需要的各种信息，例如控制中心的注册地址，服务端的具体IO和端口等。
![](/imported/markdown/2026-05-17-markdown-4bddb225-dubbo-服务调用源码/images/efe3489232e4-202605161138358.png)
如上图就是ReferenceBean的类图，根据以往对spring的学习了解，有如下总结：

- 很清楚的认识到其是一个工厂Bean，后续需要getObject方法得到真正的对象（其实在这里不看源码，我们就应该能猜到常规做法是通过动态代理生成`interface="com.jwfy.dubbo.product.ProductService`中接口对应的proxy对象），如果想获取ReferenceBean对象本身，则需要使用`getBean("&productService")`

- 通过InitializingBean的afterPropertiesSet 方法去为当前的bean注入注册中心、均衡负责的方式、使用的协议等属性数据。

在这里生成代理对象是通过Java的动态代理方式，因为指明的是接口，（**spring中默认的是如果通过接口生成代理对象，是使用JDK动态代理，否则是使用cglib**），那么根据对动态代理知识点的了解，InvocationHandler肯定是跑不掉的，通过invoke去调用执行函数的。

## [生成ReferenceBean的代理对象](#生成referencebean的代理对象)

在getObject方法为入口打断点，最后可以追踪到ReferenceConfig类的createProxy方法为真正的生成代理对象的操作。

**JavassistProxyFactory 类**
![](/imported/markdown/2026-05-17-markdown-4bddb225-dubbo-服务调用源码/images/3a4a3573cb4b-202605161147196.webp)
## [生成Invoker](#生成invoker)

Invoker是对可执行对象的引用，需要明确可引用的具体位置（服务端的明确IP和端口等信息）

现在已经拿到了当前服务的注册中心的配置，那么接下来就需要连接到注册中心，并获取到可以调用的机器情况（现实开发中，分布式系统基本上都存在多个机器信息），并组合成为需要的invoker。

下面这个代码段就是生产具体的Invoke操作，接下来好好分析一下

在分析源码之前，如果换成我们，我们会完成什么操作呢？

- 向注册中心订阅消费者，这样通过dubbo-admin就可以观察现有的生产者和消费者

- 从注册中心 获取 生产者的信息

- 类似均衡负责的操作，选择合适的生产者

- 直连生产者，获取结果

**RegistryProtocol 类**

**Cluster$Adpative 类**

### [doRefer](#dorefer)

经过上面的操作，现在来到了doRefer函数操作，其结果返回的就是invoker对象

在上面一笔带过了如何注册、订阅、生成invoke的，接下来依次拆分各个细节

### [注册到注册中心](#注册到注册中心)

- registry是ZookeeperRegistry对象

- subscribeUrl是`consumer://192.168.10.123/com.jwfy.dubbo.product.ProductService?application=dubbo-consume&default.check=false&dubbo=2.5.3&interface=com.jwfy.dubbo.product.ProductService&methods=print,getStr&owner=jwfy&pid=1196&side=consumer×tamp=1526204222984`

表示是一个消费者

进入到FailbackRegistry类

在doRegister操作中，是利用zk的API存储如下的path

`/dubbo-jwfy/com.jwfy.dubbo.product.ProductService/consumers/consumer%3A%2F%2F192.168.10.123%2Fcom.jwfy.dubbo.product.ProductService%3Fapplication%3Ddubbo-consume%26category%3Dconsumers%26check%3Dfalse%26default.check%3Dfalse%26dubbo%3D2.5.3%26interface%3Dcom.jwfy.dubbo.product.ProductService%26methods%3Dprint%2CgetStr%26owner%3Djwfy%26pid%3D1196%26side%3Dconsumer%26timestamp%3D1526204222984`

如下图，在调用doRegister前后zk注册中心节点的情况，很明显已经注册成功
![](/imported/markdown/2026-05-17-markdown-4bddb225-dubbo-服务调用源码/images/d640e8a49394-202605161146807.webp)
### [订阅服务](#订阅服务)

服务订阅说通俗些就是获取zk中需要的节点信息，本例中是**获取生产者的连接信息**

- url是consumer://192.168.10.123/com.jwfy.dubbo.product.ProductService?application=dubbo-consume&category=providers,configurators,routers&default.check=false&dubbo=2.5.3&interface=com.jwfy.dubbo.product.ProductService&methods=print,getStr&owner=jwfy&pid=1196&side=consumer×tamp=1526204222984

- directory 是RegistryDirectory，**其中参数registry就是上面的注册中心ZookeeperRegistry的配置**

**FailbackRegistry 类**

来到了doSubscribe方法,在这里我们将会了解到如何从注册中心获取到生产者的连接信息的

**AbstractZookeeperClient 类**

现在完成了和注册中心的操作了，通过path顺利拿到生产者的信息，如果仔细观察上述的参数信息，会发现pid是1081，再看看jps显示的进程号,如下图，恰好说明获取到的生产者信息是对的
![](/imported/markdown/2026-05-17-markdown-4bddb225-dubbo-服务调用源码/images/fe6bea238d96-202605161141517.png)
接着来到toUrlsWithEmpty函数，如果有仔细观察这个方法会发现，参数列表都改成了(URL consumer, String path, List&lt;String&gt; providers)这已经很明确的告诉我们，第一个参数是消费者的url，第二个是当前zk的path信息，第三个是获取到的生产者列表信息（为啥是列表呢？因为生产者可以是多个，而且存在多个的情况下，后续均衡负责还需要选择一个可用的生产者进行网络信息交互操作）

当然toUrlsWithEmpty函数主要是进行生产者和消费者的url信息对比操作，如果没有合适的url则添加一个empty协议的url信息（**后期就是通过这个empty判断是否存在有用的生产者，日常开发中的无效黑白名单的错误就产生在这里**）

### [刷新invoker](#刷新invoker)

紧接着来到了notify方法，如下图的具体各个参数具体值
![](/imported/markdown/2026-05-17-markdown-4bddb225-dubbo-服务调用源码/images/de4ce01a0286-202605161140760.png)
紧接着来到了**AbstractRegistry类**

**RegistryDirectory 类**

这个函数具体的操作包含了

1. 更新ZookeeperRegistry中的notify参数信息（**把生产者、配置、路由等url信息存入其中**）

1. 保存节点信息文档到dubbo的cache文件中

1. 刷新生成invoke的数据信息

到此整个的订阅服务的操作就完成了

### [生成Invoker](#生成invoker-1)

现在就剩下最关键的一句话cluster.join(directory)，会层层包装，最后形成的invoker如图所示
![](/imported/markdown/2026-05-17-markdown-4bddb225-dubbo-服务调用源码/images/bd619b67885b-202605161139802.png)
在directory中包含了所有的注册信息，在后面的真正的函数调用其实也是通过invoker.invoker去调用执行

#### [InvokerInvocationHandler 入口](#invokerinvocationhandler-入口)

被包装的类通过动态代理反射时，内嵌入的InvocationHandler类，具体方法调用则会进入到invoke方法中
![](/imported/markdown/2026-05-17-markdown-4bddb225-dubbo-服务调用源码/images/3d962267f57e-202605161148659.webp)
来到了MockClusterInvoker类，此时需要注意到MockClusterInvoker类的invoke是FailoverClusterInvoker

FailoverClusterInvoker类可以进行重试操作，**如果有印象的可以知道在一个reference的xml配置中，可以加上重试次数retries属性字段的值，默认是3次，如果设置了小于0的数字，则为1次，重试次数0位的意思就是只进行一次操作**

#### [MockClusterInvoker mock入口](#mockclusterinvoker-mock入口)

#### [AbstractClusterInvoker 负载均衡](#abstractclusterinvoker-负载均衡)

进入到FailoverClusterInvoker类之前先进入到AbstractClusterInvoker类中

#### [FailoverClusterInvoker 重试机制](#failoverclusterinvoker-重试机制)

上面已经说了，这个类的主要作用是**重试操作**

#### [DubboInvoker invoke](#dubboinvoker-invoke)

上面说的Result result = invoker.invoke(invocation);，经过层层转发，来到了FutureFilter类

来到了MonitorFilter过滤器查看是否需要进行监控（通过查看url是否存在monitor字段，如果为true，则是需要监控）

再来到了AbstractInvoker类的invoke方法,本身是DubboInvoker

**DubboInvoker 类**

#### [NettyChannel netty请求](#nettychannel-netty请求)

上述的request以及send方法，都被转发到HeaderExchangeChannel类中，这个类有一个非常关键的字段是channel，是NettyClient类，包含了服务提供方的IP：PORT信息

其实仔细看request方法和send方法最后的实现差不太多，只是request需要检测连接的channel是否存在，而send单独本身是不需要进行这个操作的。

**NettyChannel 类**

#### [Future 结果处理 & 超时检测](#future-结果处理-超时检测)

看看异步拿到结果，判断是否超时等检测操作

**DefaultFuture 类**

**至此整个的远程调用就全部结束了**

## [总结整体流程](#总结整体流程)

1. 结合spring配置好bean信息以及各种协议

1. 连接并注册到注册中心

1. 订阅消息，获取到服务提供方IP:PROT列表（具体得看服务提供方有多少）

1. 根据IP:PROT 生成对应的Invoker（Invoker是调用的实体，其中包含了所具备的信息）

1. 动态代理执行invoke反射执行方法

1. 是否会进行mock测试

1. 负载均衡选择合适的某一具体服务提供方

1. 加入重试机制，如果出现类似timeout等情况会进行重试操作（有一点需要注意，biz异常是不再进行重试，而直接上抛异常）

1. 服务异步调用或者有无返回值

服务提供者的集群集群⾥⾯有⼏个服务提供者，就有⼏个invoker，invoker理解成调⽤⼀个服务提供者需要的完整的细节，封装成的对象

那集群是怎么知道有⼏个服务提供者——从注册中⼼获得，注册中⼼获得的数据封装在RegistryDirectory对象中。那么RegistryDirectory怎么得到注册中⼼中的url地址呢？必须有⼀个zk客户端：ZookeeperRegistry

RegistryDirectory⾥包含了ZookeeperRegistry，RegistryDirectory维护了所有的invoker调⽤器，调⽤器通过RegsitryDirectory（ZookeeperRegistry）的⽅法获得的。

AbstractClusterInvoker⾥包含了RegistryDirectory，换句话说，RegistryDirectory被AbstractClusterInvoker所使⽤。真正执⾏的是AbstractClusterInvoker中的invoker⽅法，负载均衡也在⾥⾯。

proxy是由JavassistProxyFactory⽣成的，拼装代码来⽣成的。代理对象通过JavassistProxyFactory中的InvokerInvocationHandler ⽣成⼀个代理对象，来发起对集群的调⽤。

InvokerInvocationHandler⾥封装了RpcInvocation，RpcInvocation⾥封装的是这⼀次请求所需要的所有参数。

这个invoker如果⽤的是dubbo协议，那么就是DubboInvoker（还有http RMI等协议）

源码中的invoker.invoke()中的invoker，如果是dubbo协议，那么就是DubboInvoker。
