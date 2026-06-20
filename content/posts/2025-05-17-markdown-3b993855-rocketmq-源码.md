{

  "title": "RocketMQ - 源码",
  "has_date": true,
  "description": "环境搭建 依赖工具 JDK ：1.8+ Maven IntelliJ IDEA 源码拉取 从官方仓库 https://github.com/apache/rocketmq 或者 源码。 源码目录结构：** broker: broker 模块（broke 启动进程） client ：消息客户端，包含消",
  "tags": [
    "微服务",
    "消息队列",
    "RocketMQ"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/message-queue/rocketMQ-sourcecode - RocketMQ - 源码.md",
  "date": "2025-05-17"

}

## [环境搭建](#环境搭建)

依赖工具

- JDK ：1.8+

- Maven

- IntelliJ IDEA

### [源码拉取](#源码拉取)

从官方仓库 [https://github.com/apache/rocketmq](https://github.com/apache/rocketmq)`clone`或者`download`源码。

**源码目录结构：**

- broker: broker 模块（broke 启动进程）

- client ：消息客户端，包含消息生产者、消息消费者相关类

- common ：公共包

- dev ：开发者信息（非源代码）

- distribution ：部署实例文件夹（非源代码）

- example: RocketMQ 例代码

- filter ：消息过滤相关基础类

- filtersrv：消息过滤服务器实现相关类（Filter启动进程）

- logappender：日志实现相关类

- namesrv：NameServer实现相关类（NameServer启动进程）

- openmessageing：消息开放标准

- remoting：远程通信模块，给予Netty

- srcutil：服务工具类

- store：消息存储实现相关类

- style：checkstyle相关实现

- test：测试相关类

- tools：工具类，监控命令相关实现类

### [导入IDEA](#导入idea)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/c3cfea80fd91-202404291952373.png)
**执行安装**

### [调试](#调试)

创建`conf`配置文件夹,从`distribution`拷贝`broker.conf`和`logback_broker.xml`和`logback_namesrv.xml`
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/09c1e06ea969-202404291953702.png)
1）启动NameServer

- 展开namesrv模块，右键NamesrvStartup.java

![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/aeed997a84ec-202404291953256.png)

- 配置**ROCKETMQ_HOME**

![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/ad0f64bc05cf-202404291953863.png)![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/6830215d4c2e-202404291953749.png)

- 重新启动

控制台打印结果

2）启动Broker

- `broker.conf`配置文件内容

- 创建数据文件夹`dataDir`

- 启动`BrokerStartup`,配置`broker.conf`和`ROCKETMQ_HOME`

![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/170c1b130dc2-202404291953984.png)![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/e13518f62c8a-202404291953090.png)
3）发送消息

- 进入example模块的`org.apache.rocketmq.example.quickstart`

- 指定Namesrv地址

- 运行`main`方法，发送消息

4）消费消息

- 进入example模块的`org.apache.rocketmq.example.quickstart`

- 指定Namesrv地址

- 运行`main`方法，消费消息

## [NameServer](#nameserver)

### [架构设计](#架构设计)

消息中间件的设计思路一般是基于主题订阅发布的机制，消息生产者（Producer）发送某一个主题到消息服务器，消息服务器负责将消息持久化存储，消息消费者（Consumer）订阅该兴趣的主题，消息服务器根据订阅信息（路由信息）将消息推送到消费者（Push模式）或者消费者主动向消息服务器拉去（Pull模式），从而实现消息生产者与消息消费者解耦。为了避免消息服务器的单点故障导致的整个系统瘫痪，通常会部署多台消息服务器共同承担消息的存储。那消息生产者如何知道消息要发送到哪台消息服务器呢？如果某一台消息服务器宕机了，那么消息生产者如何在不重启服务情况下感知呢？

NameServer就是为了解决以上问题设计的。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/ea74a015e665-202404292011284.jpg)

1. Broker消息服务器在启动的时向所有NameServer注册

1. 消息生产者（Producer）在发送消息时之前先从NameServer获取Broker服务器地址列表，然后根据负载均衡算法从列表中选择一台服务器进行发送。

1. NameServer与每台Broker保持长连接，并间隔30S检测Broker是否存活，如果检测到Broker宕机，则从路由注册表中删除。但是路由变化不会马上通知消息生产者。这样设计的目的是为了降低NameServer实现的复杂度，在消息发送端提供容错机制保证消息发送的可用性。

NameServer本身的高可用是通过部署多台NameServer来实现，但彼此之间不通讯，也就是NameServer服务器之间在某一个时刻的数据并不完全相同，但这对消息发送并不会造成任何影响，这也是NameServer设计的一个亮点，总之，RocketMQ设计追求简单高效。

### [启动流程](#启动流程)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/aa4c3e266c9b-202404291954063.png)
启动类：`org.apache.rocketmq.namesrv.NamesrvStartup`

#### [步骤一](#步骤一)

解析配置文件，填充NameServerConfig、NettyServerConfig属性值，并创建NamesrvController

***代码：NamesrvController#createNamesrvController***

**NamesrvConfig属性**

**rocketmqHome：**rocketmq主目录

**kvConfig：**NameServer存储KV配置属性的持久化路径

**configStorePath：**nameServer默认配置文件路径

**orderMessageEnable：**是否支持顺序消息

**NettyServerConfig属性**

**listenPort：**NameServer监听端口，该值默认会被初始化为9876
 **serverWorkerThreads：**Netty业务线程池线程个数
 **serverCallbackExecutorThreads：**Netty public任务线程池线程个数，Netty网络设计，根据业务类型会创建不同的线程池，比如处理消息发送、消息消费、心跳检测等。如果该业务类型未注册线程池，则由public线程池执行。
 **serverSelectorThreads：**IO线程池个数，主要是NameServer、Broker端解析请求、返回相应的线程个数，这类线程主要是处理网路请求的，解析请求包，然后转发到各个业务线程池完成具体的操作，然后将结果返回给调用方;
 **serverOnewaySemaphoreValue：**send oneway消息请求并发读（Broker端参数）;
 **serverAsyncSemaphoreValue：**异步消息发送最大并发度;
 **serverChannelMaxIdleTimeSeconds ：**网络连接最大的空闲时间，默认120s。
 **serverSocketSndBufSize：**网络socket发送缓冲区大小。
**serverSocketRcvBufSize：** 网络接收端缓存区大小。
 **serverPooledByteBufAllocatorEnable：**ByteBuffer是否开启缓存;
 **useEpollNativeSelector：**是否启用Epoll IO模型。

#### [步骤二](#步骤二)

根据启动属性创建NamesrvController实例，并初始化该实例。NameServerController实例为NameServer核心控制器

***代码：NamesrvController#initialize***

#### [步骤三](#步骤三)

在JVM进程关闭之前，先将线程池关闭，及时释放资源

***代码：NamesrvStartup#start***

### [路由管理](#路由管理)

NameServer的主要作用是为消息的生产者和消息消费者提供关于主题Topic的路由信息，那么NameServer需要存储路由的基础信息，还要管理Broker节点，包括路由注册、路由删除等。

#### [路由元信息](#路由元信息)

**代码：RouteInfoManager**
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/e98c1d620145-202404291954000.png)
**topicQueueTable：**Topic消息队列路由信息，消息发送时根据路由表进行负载均衡

**brokerAddrTable：**Broker基础信息，包括brokerName、所属集群名称、主备Broker地址

**clusterAddrTable：**Broker集群信息，存储集群中所有Broker名称

**brokerLiveTable：**Broker状态信息，NameServer每次收到心跳包是会替换该信息

**filterServerTable：**Broker上的FilterServer列表，用于类模式消息过滤。

RocketMQ基于定于发布机制，一个Topic拥有多个消息队列，一个Broker为每一个主题创建4个读队列和4个写队列。多个Broker组成一个集群，集群由相同的多台Broker组成Master-Slave架构，brokerId为0代表Master，大于0为Slave。BrokerLiveInfo中的lastUpdateTimestamp存储上次收到Broker心跳包的时间。

![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/0ccffbbd63d0-202404291954399.png)![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/6919d92fc9b1-202404291954083.png)
#### [路由注册](#路由注册)

##### [发送心跳包](#发送心跳包)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/25139f47fabc-202404291954144.png)
RocketMQ路由注册是通过Broker与NameServer的心跳功能实现的。Broker启动时向集群中所有的NameServer发送心跳信息，每隔30s向集群中所有NameServer发送心跳包，NameServer收到心跳包时会更新brokerLiveTable缓存中BrokerLiveInfo的lastUpdataTimeStamp信息，然后NameServer每隔10s扫描brokerLiveTable，如果连续120S没有收到心跳包，NameServer将移除Broker的路由信息同时关闭Socket连接。

***代码：BrokerController#start***

***代码：BrokerOuterAPI#registerBrokerAll***

***代码：BrokerOutAPI#registerBroker***

##### [处理心跳包](#处理心跳包)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/7f30af45bf2c-202404291955718.png)
`org.apache.rocketmq.namesrv.processor.DefaultRequestProcessor`网路处理类解析请求类型，如果请求类型是为***REGISTER_BROKER***，则将请求转发到`RouteInfoManager#regiesterBroker`

***代码：DefaultRequestProcessor#processRequest***

***代码：DefaultRequestProcessor#registerBroker***

***代码：RouteInfoManager#registerBroker***

维护路由信息

***代码：RouteInfoManager#createAndUpdateQueueData***

#### [路由删除](#路由删除)

`Broker`每隔30s向`NameServer`发送一个心跳包，心跳包包含`BrokerId`，`Broker`地址，`Broker`名称，`Broker`所属集群名称、`Broker`关联的`FilterServer`列表。但是如果`Broker`宕机，`NameServer`无法收到心跳包，此时`NameServer`如何来剔除这些失效的`Broker`呢？`NameServer`会每隔10s扫描`brokerLiveTable`状态表，如果`BrokerLive`的**lastUpdateTimestamp**的时间戳距当前时间超过120s，则认为`Broker`失效，移除该`Broker`，关闭与`Broker`连接，同时更新`topicQueueTable`、`brokerAddrTable`、`brokerLiveTable`、`filterServerTable`。

**RocketMQ有两个触发点来删除路由信息**：

- NameServer定期扫描brokerLiveTable检测上次心跳包与当前系统的时间差，如果时间超过120s，则需要移除broker。

- Broker在正常关闭的情况下，会执行unregisterBroker指令

这两种方式路由删除的方法都是一样的，就是从相关路由表中删除与该broker相关的信息。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/3b34d841f2de-202404291955317.png)
***代码：NamesrvController#initialize***

***代码：RouteInfoManager#scanNotActiveBroker***

***代码：RouteInfoManager#onChannelDestroy***

#### [路由发现](#路由发现)

RocketMQ路由发现是非实时的，当Topic路由出现变化后，NameServer不会主动推送给客户端，而是由客户端定时拉取主题最新的路由。

***代码：DefaultRequestProcessor#getRouteInfoByTopic***

### [小结](#小结)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/9fe17c445315-202404291956941.png)
## [Producer](#producer)

消息生产者的代码都在client模块中，相对于RocketMQ来讲，消息生产者就是客户端，也是消息的提供者。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/0469d59f1874-202404291956349.png)
### [方法和属性](#方法和属性)

1）主要方法介绍
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/4eda9174ae78-202404291956183.png)![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/79566f296dbb-202404291956897.png)
2）属性介绍
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/aad934d9d1c8-202404291956575.png)
### [启动流程](#启动流程-1)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/f309cf08e261-202404291956371.png)
***代码：DefaultMQProducerImpl#start***

整个JVM中只存在一个MQClientManager实例，维护一个MQClientInstance缓存表

ConcurrentMap&lt;String/* clientId */, MQClientInstance&gt; factoryTable = new ConcurrentHashMap&lt;String,MQClientInstance&gt;();

同一个clientId只会创建一个MQClientInstance。

MQClientInstance封装了RocketMQ网络处理API，是消息生产者和消息消费者与NameServer、Broker打交道的网络通道

***代码：MQClientManager#getAndCreateMQClientInstance***

***代码：DefaultMQProducerImpl#start***

### [消息发送](#消息发送)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/69d0e3074b92-202404291956341.png)
***代码：DefaultMQProducerImpl#send(Message msg)***

***代码：DefaultMQProducerImpl#send(Message msg,long timeout)***

***代码：DefaultMQProducerImpl#sendDefaultImpl***

#### [1）验证消息](#_1-验证消息)

***代码：Validators#checkMessage***

#### [2）查找路由](#_2-查找路由)

***代码：DefaultMQProducerImpl#tryToFindTopicPublishInfo***
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/300af5fb5751-202404291957084.png)
***代码：TopicPublishInfo***

***代码：MQClientInstance#updateTopicRouteInfoFromNameServer***

***代码：MQClientInstance#updateTopicRouteInfoFromNameServer***

***代码：MQClientInstance#updateTopicRouteInfoFromNameServer***

***代码：MQClientInstance#topicRouteData2TopicPublishInfo***

#### [3）选择队列](#_3-选择队列)

- 默认不启用Broker故障延迟机制

***代码：TopicPublishInfo#selectOneMessageQueue(lastBrokerName)***

***代码：TopicPublishInfo#selectOneMessageQueue()***

- 启用Broker故障延迟机制

![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/a136996a684f-202404291957623.png)

- 延迟机制接口规范

- FaultItem：失败条目

- 消息失败策略

***原理分析***

***代码：DefaultMQProducerImpl#sendDefaultImpl***

如果上述发送过程出现异常，则调用`DefaultMQProducerImpl#updateFaultItem`

***代码：MQFaultStrategy#updateFaultItem***

***代码：MQFaultStrategy#computeNotAvailableDuration***

***代码：LatencyFaultToleranceImpl#updateFaultItem***

#### [4）发送消息](#_4-发送消息)

消息发送API核心入口***DefaultMQProducerImpl#sendKernelImpl***

***代码：DefaultMQProducerImpl#sendKernelImpl***

***代码：SendMessageHook***

***代码：DefaultMQProducerImpl#sendKernelImpl***

### [批量消息发送](#批量消息发送)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/9176fbe52b60-202404291957930.png)
批量消息发送是将同一个主题的多条消息一起打包发送到消息服务端，减少网络调用次数，提高网络传输效率。当然，并不是在同一批次中发送的消息数量越多越好，其判断依据是单条消息的长度，如果单条消息内容比较长，则打包多条消息发送会影响其他线程发送消息的响应时间，并且单批次消息总长度不能超过DefaultMQProducer#maxMessageSize。

批量消息发送要解决的问题是如何将这些消息编码以便服务端能够正确解码出每条消息的消息内容。

***代码：DefaultMQProducer#send***

***代码：DefaultMQProducer#batch***

## [消息存储](#消息存储)

### [消息存储核心类](#消息存储核心类)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/2f69aec1d151-202404291957288.png)
### [消息存储流程](#消息存储流程)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/c3f6c9378790-202404291958625.png)
***消息存储入口：DefaultMessageStore#putMessage***

***代码：CommitLog#putMessage***

***代码：MappedFile#appendMessagesInner***

***代码：CommitLog#doAppend***

***代码：CommitLog#calMsgLength***

***代码：CommitLog#doAppend***

***代码：CommitLog#putMessage***

### [存储文件](#存储文件)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/85bb33e4fc0d-202404291958763.png)

- commitLog：消息存储目录

- config：运行期间一些配置信息

- consumerqueue：消息消费队列存储目录

- index：消息索引文件存储目录

- abort：如果存在改文件寿命Broker非正常关闭

- checkpoint：文件检查点，存储CommitLog文件最后一次刷盘时间戳、consumerquueue最后一次刷盘时间，index索引文件最后一次刷盘时间戳。

### [存储文件内存映射](#存储文件内存映射)

RocketMQ通过使用内存映射文件提高IO访问性能，无论是CommitLog、ConsumerQueue还是IndexFile，单个文件都被设计为固定长度，如果一个文件写满以后再创建一个新文件，文件名就为该文件第一条消息对应的全局物理偏移量。

#### [1）MappedFileQueue](#_1-mappedfilequeue)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/ac341cb32eef-202404291958272.png)

- 根据存储时间查询MappedFile

- 根据消息偏移量offset查找MappedFile

- 获取存储文件最小偏移量

- 获取存储文件最大偏移量

- 返回存储文件当前写指针

#### [2）MappedFile](#_2-mappedfile)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/4de26eb99546-202404291958173.png)
***MappedFile初始化***

- 未开启`transientStorePoolEnable`。`transientStorePoolEnable=true`为`true`表示数据先存储到堆外内存，然后通过`Commit`线程将数据提交到内存映射Buffer中，再通过`Flush`线程将内存映射`Buffer`中数据持久化磁盘。

开启`transientStorePoolEnable`

***MappedFile提交***

提交数据到FileChannel，commitLeastPages为本次提交最小的页数，如果待提交数据不满commitLeastPages，则不执行本次提交操作。如果writeBuffer如果为空，直接返回writePosition指针，无需执行commit操作，表名commit操作主体是writeBuffer。

***MappedFile#isAbleToCommit***

判断是否执行commit操作，如果文件已满返回true；如果commitLeastpages大于0，则比较writePosition与上一次提交的指针commitPosition的差值，除以OS_PAGE_SIZE得到当前脏页的数量，如果大于commitLeastPages则返回true，如果commitLeastpages小于0表示只要存在脏页就提交。

***MappedFile#commit0***

具体提交的实现，首先创建WriteBuffer区共享缓存区，然后将新创建的position回退到上一次提交的位置（commitPosition），设置limit为wrotePosition（当前最大有效数据指针），然后把commitPosition到wrotePosition的数据写入到FileChannel中，然后更新committedPosition指针为wrotePosition。commit的作用就是将MappedFile的writeBuffer中数据提交到文件通道FileChannel中。

***MappedFile#flush***

刷写磁盘，直接调用MappedByteBuffer或fileChannel的force方法将内存中的数据持久化到磁盘，那么flushedPosition应该等于MappedByteBuffer中的写指针；如果writeBuffer不为空，则flushPosition应该等于上一次的commit指针；因为上一次提交的数据就是进入到MappedByteBuffer中的数据；如果writeBuffer为空，数据时直接进入到MappedByteBuffer，wrotePosition代表的是MappedByteBuffer中的指针，故设置flushPosition为wrotePosition。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/3d373a234de9-202404291958670.jpg)
***MappedFile#getReadPosition***

获取当前文件最大可读指针。如果writeBuffer为空，则直接返回当前的写指针；如果writeBuffer不为空，则返回上一次提交的指针。在MappedFile设置中,只有提交了的数据（写入到MappedByteBuffer或FileChannel中的数据）才是安全的数据

***MappedFile#selectMappedBuffer***

查找pos到当前最大可读之间的数据，由于在整个写入期间都未曾改MappedByteBuffer的指针，如果mappedByteBuffer.slice()方法返回的共享缓存区空间为整个MappedFile，然后通过设置ByteBuffer的position为待查找的值，读取字节长度当前可读最大长度，最终返回的ByteBuffer的limit为size。整个共享缓存区的容量为（MappedFile#fileSize-pos）。故在操作SelectMappedBufferResult不能对包含在里面的ByteBuffer调用filp方法。

***MappedFile#shutdown***

MappedFile文件销毁的实现方法为public boolean destory(long intervalForcibly)，intervalForcibly表示拒绝被销毁的最大存活时间。

#### [3）TransientStorePool](#_3-transientstorepool)

短暂的存储池。RocketMQ单独创建一个MappedByteBuffer内存缓存池，用来临时存储数据，数据先写入该内存映射中，然后由commit线程定时将数据从该内存复制到与目标物理文件对应的内存映射中。RocketMQ引入该机制主要的原因是提供一种内存锁定，将当前堆外内存一直锁定在内存中，避免被进程将内存交换到磁盘。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/1cb8893dad04-202404291958479.png)
***初始化***

### [实时更新消息消费队列与索引文件](#实时更新消息消费队列与索引文件)

消息消费队文件、消息属性索引文件都是基于CommitLog文件构建的，当消息生产者提交的消息存储在CommitLog文件中，ConsumerQueue、IndexFile需要及时更新，否则消息无法及时被消费，根据消息属性查找消息也会出现较大延迟。RocketMQ通过开启一个线程ReputMessageService来准实时转发CommitLog文件更新事件，相应的任务处理器根据转发的消息及时更新ConsumerQueue、IndexFile文件。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/d2c9524ae6ca-202404291958072.png)![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/3a48f5e6a5b4-202404291958904.png)
***代码：DefaultMessageStore：start***

***代码：DefaultMessageStore：run***

***代码：DefaultMessageStore：deReput***

***DispatchRequest***
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/6a7c7df0d821-202404291959014.png)
#### [1）转发到ConsumerQueue](#_1-转发到consumerqueue)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/6566c46b385d-202404291959055.png)
***代码：DefaultMessageStore#putMessagePositionInfo***

***代码：DefaultMessageStore#putMessagePositionInfo***

#### [2）转发到Index](#_2-转发到index)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/1c05856c68f1-202404291959449.png)
***代码：DefaultMessageStore#buildIndex***

### [消息队列和索引文件恢复](#消息队列和索引文件恢复)

由于RocketMQ存储首先将消息全量存储在CommitLog文件中，然后异步生成转发任务更新ConsumerQueue和Index文件。如果消息成功存储到CommitLog文件中，转发任务未成功执行，此时消息服务器Broker由于某个愿意宕机，导致CommitLog、ConsumerQueue、IndexFile文件数据不一致。如果不加以人工修复的话，会有一部分消息即便在CommitLog中文件中存在，但由于没有转发到ConsumerQueue，这部分消息将永远复发被消费者消费。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/0ff3e8c2b959-202404291959331.png)
#### [1）存储文件加载](#_1-存储文件加载)

***代码：DefaultMessageStore#load***

判断上一次是否异常退出。实现机制是Broker在启动时创建abort文件，在退出时通过JVM钩子函数删除abort文件。如果下次启动时存在abort文件。说明Broker时异常退出的，CommitLog与ConsumerQueue数据有可能不一致，需要进行修复。

***代码：DefaultMessageStore#load***

***代码：MappedFileQueue#load***

加载CommitLog到映射文件

***代码：DefaultMessageStore#loadConsumeQueue***

加载消息消费队列

***代码：IndexService#load***

加载索引文件

***代码：DefaultMessageStore#recover***

文件恢复，根据Broker是否正常退出执行不同的恢复策略

***代码：DefaultMessageStore#recoverTopicQueueTable***

恢复ConsumerQueue后，将在CommitLog实例中保存每隔消息队列当前的存储逻辑偏移量，这也是消息中不仅存储主题、消息队列ID、还存储了消息队列的关键所在。

#### [2）正常恢复](#_2-正常恢复)

***代码：CommitLog#recoverNormally***

***代码：MappedFileQueue#truncateDirtyFiles***

#### [3）异常恢复](#_3-异常恢复)

Broker异常停止文件恢复的实现为CommitLog#recoverAbnormally。异常文件恢复步骤与正常停止文件恢复流程基本相同，其主要差别有两个。首先，正常停止默认从倒数第三个文件开始进行恢复，而异常停止则需要从最后一个文件往前走，找到第一个消息存储正常的文件。其次，如果CommitLog目录没有消息文件，如果消息消费队列目录下存在文件，则需要销毁。

***代码：CommitLog#recoverAbnormally***

### [刷盘机制](#刷盘机制)

RocketMQ的存储是基于JDK NIO的内存映射机制（MappedByteBuffer）的，消息存储首先将消息追加到内存，再根据配置的刷盘策略在不同时间进行刷写磁盘。

#### [同步刷盘](#同步刷盘)

消息追加到内存后，立即将数据刷写到磁盘文件
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/73ea8c1febc2-202404291959664.png)
***代码：CommitLog#handleDiskFlush***

***GroupCommitRequest***
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/055685ddea1b-202404291959483.png)
***代码：GroupCommitService#run***

***代码：GroupCommitService#doCommit***

#### [异步刷盘](#异步刷盘)

在消息追加到内存后，立即返回给消息发送端。如果开启transientStorePoolEnable，RocketMQ会单独申请一个与目标物理文件（commitLog）同样大小的堆外内存，该堆外内存将使用内存锁定，确保不会被置换到虚拟内存中去，消息首先追加到堆外内存，然后提交到物理文件的内存映射中，然后刷写到磁盘。如果未开启transientStorePoolEnable，消息直接追加到物理文件直接映射文件中，然后刷写到磁盘中。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/94c555b36803-202404291959881.png)
开启transientStorePoolEnable后异步刷盘步骤:

1. 将消息直接追加到ByteBuffer（堆外内存）

1. CommitRealTimeService线程每隔200ms将ByteBuffer新追加内容提交到MappedByteBuffer中

1. MappedByteBuffer在内存中追加提交的内容，wrotePosition指针向后移动

1. commit操作成功返回，将committedPosition位置恢复

1. FlushRealTimeService线程默认每500ms将MappedByteBuffer中新追加的内存刷写到磁盘

***代码：CommitLog$CommitRealTimeService#run***

提交线程工作机制

***代码：CommitLog$FlushRealTimeService#run***

刷盘线程工作机制

### [过期文件删除机制](#过期文件删除机制)

由于RocketMQ操作CommitLog、ConsumerQueue文件是基于内存映射机制并在启动的时候回加载CommitLog、ConsumerQueue目录下的所有文件，为了避免内存与磁盘的浪费，不可能将消息永久存储在消息服务器上，所以要引入一种机制来删除已过期的文件。RocketMQ顺序写CommitLog、ConsumerQueue文件，所有写操作全部落在最后一个CommitLog或者ConsumerQueue文件上，之前的文件在下一个文件创建后将不会再被更新。RocketMQ清除过期文件的方法时：如果当前文件在在一定时间间隔内没有再次被消费，则认为是过期文件，可以被删除，RocketMQ不会关注这个文件上的消息是否全部被消费。默认每个文件的过期时间为72小时，通过在Broker配置文件中设置fileReservedTime来改变过期时间，单位为小时。

***代码：DefaultMessageStore#addScheduleTask***

***代码：DefaultMessageStore#cleanFilesPeriodically***

***代码：DefaultMessageStore#deleteExpiredFiles***

删除文件操作的条件

1. 指定删除文件的时间点，RocketMQ通过deleteWhen设置一天的固定时间执行一次删除过期文件操作，默认4点

1. 磁盘空间如果不充足，删除过期文件

1. 预留，手工触发。

***代码：CleanCommitLogService#isSpaceToDelete***

当磁盘空间不足时执行删除过期文件

***代码：MappedFileQueue#deleteExpiredFileByTime***

执行文件销毁和删除

### [小结](#小结-1)

RocketMQ的存储文件包括消息文件（Commitlog）、消息消费队列文件（ConsumerQueue）、Hash索引文件（IndexFile）、监测点文件（checkPoint）、abort（关闭异常文件）。单个消息存储文件、消息消费队列文件、Hash索引文件长度固定以便使用内存映射机制进行文件的读写操作。RocketMQ组织文件以文件的起始偏移量来命令文件，这样根据偏移量能快速定位到真实的物理文件。RocketMQ基于内存映射文件机制提供了同步刷盘和异步刷盘两种机制，异步刷盘是指在消息存储时先追加到内存映射文件，然后启动专门的刷盘线程定时将内存中的文件数据刷写到磁盘。

CommitLog，消息存储文件，RocketMQ为了保证消息发送的高吞吐量，采用单一文件存储所有主题消息，保证消息存储是完全的顺序写，但这样给文件读取带来了不便，为此RocketMQ为了方便消息消费构建了消息消费队列文件，基于主题与队列进行组织，同时RocketMQ为消息实现了Hash索引，可以为消息设置索引键，根据所以能够快速从CommitLog文件中检索消息。

当消息达到CommitLog后，会通过ReputMessageService线程接近实时地将消息转发给消息消费队列文件与索引文件。为了安全起见，RocketMQ引入abort文件，记录Broker的停机是否是正常关闭还是异常关闭，在重启Broker时为了保证CommitLog文件，消息消费队列文件与Hash索引文件的正确性，分别采用不同策略来恢复文件。

RocketMQ不会永久存储消息文件、消息消费队列文件，而是启动文件过期机制并在磁盘空间不足或者默认凌晨4点删除过期文件，文件保存72小时并且在删除文件时并不会判断该消息文件上的消息是否被消费。

## [Consumer](#consumer)

### [消息消费概述](#消息消费概述)

消息消费以组的模式开展，一个消费组内可以包含多个消费者，每一个消费者组可订阅多个主题，消费组之间有ff式和广播模式两种消费模式。集群模式，主题下的同一条消息只允许被其中一个消费者消费。广播模式，主题下的同一条消息，将被集群内的所有消费者消费一次。消息服务器与消费者之间的消息传递也有两种模式：推模式、拉模式。所谓的拉模式，是消费端主动拉起拉消息请求，而推模式是消息达到消息服务器后，推送给消息消费者。RocketMQ消息推模式的实现基于拉模式，在拉模式上包装一层，一个拉取任务完成后开始下一个拉取任务。

集群模式下，多个消费者如何对消息队列进行负载呢？消息队列负载机制遵循一个通用思想：一个消息队列同一个时间只允许被一个消费者消费，一个消费者可以消费多个消息队列。

RocketMQ支持局部顺序消息消费，也就是保证同一个消息队列上的消息顺序消费。不支持消息全局顺序消费，如果要实现某一个主题的全局顺序消费，可以将该主题的队列数设置为1，牺牲高可用性。

### [消息消费初探](#消息消费初探)

**消息推送模式**
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/c2ac2a07b7b1-202404292000947.png)
**消息消费重要方法**

**DefaultMQPushConsumer**
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/4e26eeaac2e4-202404292000727.png)
### [消费者启动流程](#消费者启动流程)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/068be6825ebf-202404292000152.png)
***代码：DefaultMQPushConsumerImpl#start***

### [消息拉取](#消息拉取)

消息消费模式有两种模式：广播模式与集群模式。广播模式比较简单，每一个消费者需要拉取订阅主题下所有队列的消息。本文重点讲解集群模式。在集群模式下，同一个消费者组内有多个消息消费者，同一个主题存在多个消费队列，消费者通过负载均衡的方式消费消息。

消息队列负载均衡，通常的作法是一个消息队列在同一个时间只允许被一个消费消费者消费，一个消息消费者可以同时消费多个消息队列。

#### [1）PullMessageService实现机制](#_1-pullmessageservice实现机制)

从MQClientInstance的启动流程中可以看出，RocketMQ使用一个单独的线程PullMessageService来负责消息的拉取。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/ffd7f646af63-202404292000467.png)
***代码：PullMessageService#run***

**PullRequest**
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/58d84cbe098d-202404292012645.png)
***代码：PullMessageService#pullMessage***

#### [2）ProcessQueue实现机制](#_2-processqueue实现机制)

ProcessQueue是MessageQueue在消费端的重现、快照。PullMessageService从消息服务器默认每次拉取32条消息，按照消息的队列偏移量顺序存放在ProcessQueue中，PullMessageService然后将消息提交到消费者消费线程池，消息成功消费后从ProcessQueue中移除。
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/1f5f22e624d0-202404292000935.png)
**属性**

**方法**

#### [3）消息拉取基本流程](#_3-消息拉取基本流程)

##### [客户端发起拉取请求](#客户端发起拉取请求)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/fc5636cb359b-202404292000119.png)
***代码：DefaultMQPushConsumerImpl#pullMessage***

##### [消息服务端Broker组装消息](#消息服务端broker组装消息)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/e0b4524f24c4-202404292013510.png)
***代码：PullMessageProcessor#processRequest***

***代码：DefaultMessageStore#getMessage***

***代码：PullMessageProcessor#processRequest***

##### [消息拉取客户端处理消息](#消息拉取客户端处理消息)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/96589fe8de26-202404292013690.png)
***代码：MQClientAPIImpl#processPullResponse***

**PullResult类**
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/429ea034b5a6-202404292001004.png)
***代码：DefaultMQPushConsumerImpl$PullCallback#OnSuccess***

##### [消息拉取总结](#消息拉取总结)
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/8f5d74fc5bda-202404292001128.png)
#### [4）消息拉取长轮询机制分析](#_4-消息拉取长轮询机制分析)

RocketMQ未真正实现消息推模式，而是消费者主动向消息服务器拉取消息，RocketMQ推模式是循环向消息服务端发起消息拉取请求，如果消息消费者向RocketMQ拉取消息时，消息未到达消费队列时，如果不启用长轮询机制，则会在服务端等待shortPollingTimeMills时间后（挂起）再去判断消息是否已经到达指定消息队列，如果消息仍未到达则提示拉取消息客户端PULL—NOT—FOUND（消息不存在）；如果开启长轮询模式，RocketMQ一方面会每隔5s轮询检查一次消息是否可达，同时一有消息达到后立马通知挂起线程再次验证消息是否是自己感兴趣的消息，如果是则从CommitLog文件中提取消息返回给消息拉取客户端，否则直到挂起超时，超时时间由消息拉取方在消息拉取是封装在请求参数中，PUSH模式为15s，PULL模式通过DefaultMQPullConsumer#setBrokerSuspendMaxTimeMillis设置。RocketMQ通过在Broker客户端配置longPollingEnable为true来开启长轮询模式。

***代码：PullMessageProcessor#processRequest***

**PullRequestHoldService方式实现长轮询**

***代码：PullRequestHoldService#suspendPullRequest***

***代码：PullRequestHoldService#run***

***代码：PullRequestHoldService#checkHoldRequest***

***代码：PullRequestHoldService#notifyMessageArriving***

如果开启了长轮询机制，PullRequestHoldService会每隔5s被唤醒去尝试检测是否有新的消息的到来才给客户端响应，或者直到超时才给客户端进行响应，消息实时性比较差，为了避免这种情况，RocketMQ引入另外一种机制：当消息到达时唤醒挂起线程触发一次检查。

**DefaultMessageStore$ReputMessageService机制**

***代码：DefaultMessageStore#start***

***代码：DefaultMessageStore$ReputMessageService#run***

***代码：DefaultMessageStore$ReputMessageService#deReput***

***代码：NotifyMessageArrivingListener#arriving***

### [消息队列负载与重新分布机制](#消息队列负载与重新分布机制)

RocketMQ消息队列重新分配是由RebalanceService线程来实现。一个MQClientInstance持有一个RebalanceService实现，并随着MQClientInstance的启动而启动。

***代码：RebalanceService#run***

***代码：MQClientInstance#doRebalance***

***代码：RebalanceImpl#doRebalance***

***代码：RebalanceImpl#rebalanceByTopic***

RocketMQ默认提供5中负载均衡分配算法

注意：消息队列的分配遵循一个消费者可以分配到多个队列，但同一个消息队列只会分配给一个消费者，故如果出现消费者个数大于消息队列数量，则有些消费者无法消费消息。

### [消息消费过程](#消息消费过程)

PullMessageService负责对消息队列进行消息拉取，从远端服务器拉取消息后将消息存储ProcessQueue消息队列处理队列中，然后调用ConsumeMessageService#submitConsumeRequest方法进行消息消费，使用线程池来消费消息，确保了消息拉取与消息消费的解耦。ConsumeMessageService支持顺序消息和并发消息，核心类图如下：
![](/imported/markdown/2025-05-17-markdown-3b993855-rocketmq-源码/images/211df36c60da-202404292002642.png)
**并发消息消费**

***代码：ConsumeMessageConcurrentlyService#submitConsumeRequest***

***代码：ConsumeMessageConcurrentlyService$ConsumeRequest#run***

### [定时消息机制](#定时消息机制)

定时消息是消息发送到Broker后，并不立即被消费者消费而是要等到特定的时间后才能被消费，RocketMQ并不支持任意的时间精度，如果要支持任意时间精度定时调度，不可避免地需要在Broker层做消息排序，再加上持久化方面的考量，将不可避免的带来巨大的性能消耗，所以RocketMQ只支持特定级别的延迟消息。消息延迟级别在Broker端通过messageDelayLevel配置，默认为“1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h”，delayLevel=1表示延迟消息1s,delayLevel=2表示延迟5s,依次类推。

RocketMQ定时消息实现类为ScheduleMessageService，该类在DefaultMessageStore中创建。通过在DefaultMessageStore中调用load方法加载该类并调用start方法启动。

***代码：ScheduleMessageService#load***

***代码：ScheduleMessageService#start***

**调度机制**

ScheduleMessageService的start方法启动后，会为每一个延迟级别创建一个调度任务，每一个延迟级别对应SCHEDULE_TOPIC_XXXX主题下的一个消息消费队列。定时调度任务的实现类为DeliverDelayedMessageTimerTask，核心实现方法为executeOnTimeup

***代码：ScheduleMessageService$DeliverDelayedMessageTimerTask#executeOnTimeup***

### [顺序消息](#顺序消息)

顺序消息实现类是org.apache.rocketmq.client.impl.consumer.ConsumeMessageOrderlyService

***代码：ConsumeMessageOrderlyService#start***

***代码：ConsumeMessageOrderlyService#submitConsumeRequest***

***代码：ConsumeMessageOrderlyService$ConsumeRequest#run***

### [小结](#小结-2)

RocketMQ消息消费方式分别为集群模式、广播模式。

消息队列负载由RebalanceService线程默认每隔20s进行一次消息队列负载，根据当前消费者组内消费者个数与主题队列数量按照某一种负载算法进行队列分配，分配原则为同一个消费者可以分配多个消息消费队列，同一个消息消费队列同一个时间只会分配给一个消费者。

消息拉取由PullMessageService线程根据RebalanceService线程创建的拉取任务进行拉取，默认每次拉取32条消息，提交给消费者消费线程后继续下一次消息拉取。如果消息消费过慢产生消息堆积会触发消息消费拉取流控。

并发消息消费指消费线程池中的线程可以并发对同一个消息队列的消息进行消费，消费成功后，取出消息队列中最小的消息偏移量作为消息消费进度偏移量存储在于消息消费进度存储文件中，集群模式消息消费进度存储在Broker（消息服务器），广播模式消息消费进度存储在消费者端。

RocketMQ不支持任意精度的定时调度消息，只支持自定义的消息延迟级别，例如1s、2s、5s等，可通过在broker配置文件中设置messageDelayLevel。

顺序消息一般使用集群模式，是指对消息消费者内的线程池中的线程对消息消费队列只能串行消费。并并发消息消费最本质的区别是消息消费时必须成功锁定消息消费队列，在Broker端会存储消息消费队列的锁占用情况。
