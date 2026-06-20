{

  "title": "RocketMQ - 入门",
  "has_date": true,
  "description": "RocketMQ快速入门 RocketMQ是阿里巴巴2016年MQ中间件，使用Java语言开发，在阿里内部，RocketMQ承接了例如“双11”等高并发场景的消息流转，能够处理万亿级别的消息。 准备工作 下载RocketMQ RocketMQ 下载地址 环境要求 Linux64位系统 JDK1.8(",
  "tags": [
    "微服务",
    "消息队列",
    "RocketMQ"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/message-queue/rocketMQ-basic - RocketMQ - 入门.md",
  "date": "2025-05-17"

}

## [RocketMQ快速入门](#rocketmq快速入门)

RocketMQ是阿里巴巴2016年MQ中间件，使用Java语言开发，在阿里内部，RocketMQ承接了例如“双11”等高并发场景的消息流转，能够处理万亿级别的消息。

### [准备工作](#准备工作)

#### [下载RocketMQ](#下载rocketmq)

RocketMQ [下载地址](https://www.apache.org/dyn/closer.cgi?path=rocketmq/4.5.1/rocketmq-all-4.5.1-bin-release.zip)

#### [环境要求](#环境要求)

- Linux64位系统

- JDK1.8(64位)

- 源码安装需要安装Maven 3.2.x

### [安装RocketMQ](#安装rocketmq)

#### [安装步骤](#安装步骤)

本教程以二进制包方式安装

1. 解压安装包

1. 进入安装目录

#### [目录介绍](#目录介绍)

- bin：启动脚本，包括shell脚本和CMD脚本

- conf：实例配置文件，包括broker配置文件、logback配置文件等

- lib：依赖jar包，包括Netty、commons-lang、FastJSON等

#### [启动RocketMQ](#启动rocketmq)

1. 启动NameServer

1. 启动Broker

- 问题描述：

RocketMQ默认的虚拟机内存较大，启动Broker如果因为内存不足失败，需要编辑如下两个配置文件，修改JVM内存大小

- 参考设置：

`JAVA_OPT="${JAVA_OPT} -server -Xms256m -Xmx256m -Xmn128m -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=320m"`

### [测试RocketMQ](#测试rocketmq)

#### [发送消息](#发送消息)

#### [接收消息](#接收消息)

### [关闭RocketMQ](#关闭rocketmq)

## [RocketMQ集群搭建](#rocketmq集群搭建)

### [各角色介绍](#各角色介绍)

- Producer：消息的发送者；举例：发信者

- Consumer：消息接收者；举例：收信者

- Broker：暂存和传输消息；举例：邮局

- NameServer：管理Broker；举例：各个邮局的管理机构

- Topic：区分消息的种类；一个发送者可以发送消息给一个或者多个Topic；一个消息的接收者可以订阅一个或者多个Topic消息

- Message Queue：相当于是Topic的分区；用于并行发送和接收消息

![](/imported/markdown/2025-05-17-markdown-c8891f08-rocketmq-入门/images/f9d73ea16305-202405182121170.jpg)
### [集群搭建方式](#集群搭建方式)

#### [集群特点](#集群特点)

- NameServer是一个几乎无状态节点，可集群部署，节点之间无任何信息同步。

- Broker部署相对复杂，Broker分为Master与Slave，一个Master可以对应多个Slave，但是一个Slave只能对应一个Master，Master与Slave的对应关系通过指定相同的BrokerName，不同的BrokerId来定义，BrokerId为0表示Master，非0表示Slave。Master也可以部署多个。每个Broker与NameServer集群中的所有节点建立长连接，定时注册Topic信息到所有NameServer。

- Producer与NameServer集群中的其中一个节点（随机选择）建立长连接，定期从NameServer取Topic路由信息，并向提供Topic服务的Master建立长连接，且定时向Master发送心跳。Producer完全无状态，可集群部署。

- Consumer与NameServer集群中的其中一个节点（随机选择）建立长连接，定期从NameServer取Topic路由信息，并向提供Topic服务的Master、Slave建立长连接，且定时向Master、Slave发送心跳。Consumer既可以从Master订阅消息，也可以从Slave订阅消息，订阅规则由Broker配置决定。

#### [集群模式](#集群模式)

##### [单Master模式](#单master模式)

这种方式风险较大，一旦Broker重启或者宕机时，会导致整个服务不可用。不建议线上环境使用,可以用于本地测试。

##### [多Master模式](#多master模式)

一个集群无Slave，全是Master，例如2个Master或者3个Master，这种模式的优缺点如下：

- 优点：配置简单，单个Master宕机或重启维护对应用无影响，在磁盘配置为RAID10时，即使机器宕机不可恢复情况下，由于RAID10磁盘非常可靠，消息也不会丢（异步刷盘丢失少量消息，同步刷盘一条不丢），性能最高；

- 缺点：单台机器宕机期间，这台机器上未被消费的消息在机器恢复之前不可订阅，消息实时性会受到影响。

##### [多Master多Slave模式（异步）](#多master多slave模式-异步)

每个Master配置一个Slave，有多对Master-Slave，HA采用异步复制方式，主备有短暂消息延迟（毫秒级），这种模式的优缺点如下：

- 优点：即使磁盘损坏，消息丢失的非常少，且消息实时性不会受影响，同时Master宕机后，消费者仍然可以从Slave消费，而且此过程对应用透明，不需要人工干预，性能同多Master模式几乎一样；

- 缺点：Master宕机，磁盘损坏情况下会丢失少量消息。

##### [多Master多Slave模式（同步）](#多master多slave模式-同步)

每个Master配置一个Slave，有多对Master-Slave，HA采用同步双写方式，即只有主备都写成功，才向应用返回成功，这种模式的优缺点如下：

- 优点：数据与服务都无单点故障，Master宕机情况下，消息无延迟，服务可用性与数据可用性都非常高；

- 缺点：性能比异步复制模式略低（大约低10%左右），发送单个消息的RT会略高，且目前版本在主节点宕机后，备机不能自动切换为主机。

### [双主双从集群搭建](#双主双从集群搭建)

#### [总体架构](#总体架构)

消息高可用采用2m-2s（同步双写）方式
![](/imported/markdown/2025-05-17-markdown-c8891f08-rocketmq-入门/images/5d34c450f7ac-202405182122927.png)
#### [集群工作流程](#集群工作流程)

1. 启动NameServer，NameServer起来后监听端口，等待Broker、Producer、Consumer连上来，相当于一个路由控制中心。

1. Broker启动，跟所有的NameServer保持长连接，定时发送心跳包。心跳包中包含当前Broker信息(IP+端口等)以及存储所有Topic信息。注册成功后，NameServer集群中就有Topic跟Broker的映射关系。

1. 收发消息前，先创建Topic，创建Topic时需要指定该Topic要存储在哪些Broker上，也可以在发送消息时自动创建Topic。

1. Producer发送消息，启动时先跟NameServer集群中的其中一台建立长连接，并从NameServer中获取当前发送的Topic存在哪些Broker上，轮询从队列列表中选择一个队列，然后与队列所在的Broker建立长连接从而向Broker发消息。

1. Consumer跟Producer类似，跟其中一台NameServer建立长连接，获取当前订阅Topic存在哪些Broker上，然后直接跟Broker建立连接通道，开始消费消息。

#### [服务器环境](#服务器环境)
**序号****IP****角色****架构模式**1192.168.25.135nameserver、brokerserverMaster1、Slave22192.168.25.138nameserver、brokerserverMaster2、Slave1
#### [Host添加信息](#host添加信息)

配置如下:

配置完成后, 重启网卡

#### [防火墙配置](#防火墙配置)

宿主机需要远程访问虚拟机的rocketmq服务和web服务，需要开放相关的端口号，简单粗暴的方式是直接关闭防火墙

或者为了安全，只开放特定的端口号，RocketMQ默认使用3个端口：9876 、10911 、11011 。如果防火墙没有关闭的话，那么防火墙就必须开放这些端口：

- `nameserver` 默认使用 9876 端口

- `master` 默认使用 10911 端口

- `slave` 默认使用11011 端口

执行以下命令：

#### [环境变量配置](#环境变量配置)

在profile文件的末尾加入如下命令

输入:wq! 保存并退出， 并使得配置立刻生效：

#### [创建消息存储路径](#创建消息存储路径)

#### [broker配置文件](#broker配置文件)

1. master1

服务器：192.168.25.135

修改配置如下：

1. slave2

服务器：192.168.25.135

修改配置如下：

1. master2

服务器：192.168.25.138

修改配置如下：

1. slave1

服务器：192.168.25.138

修改配置如下：

#### [修改启动脚本文件](#修改启动脚本文件)

- [runbroker.sh](http://runbroker.sh)

需要根据内存大小进行适当的对JVM参数进行调整：

- [runserver.sh](http://runserver.sh)

#### [服务启动](#服务启动)

1. 启动NameServe集群

分别在192.168.25.135和192.168.25.138启动NameServer

1. 启动Broker集群

- 在192.168.25.135上启动master1和slave2

master1：

slave2：

- 在192.168.25.138上启动master2和slave2

master2

slave1

#### [查看进程状态](#查看进程状态)

启动后通过JPS查看启动进程
![](/imported/markdown/2025-05-17-markdown-c8891f08-rocketmq-入门/images/d0ed2a6f3dc9-202405182127695.png)
#### [查看日志](#查看日志)

### [mqadmin管理工具](#mqadmin管理工具)

#### [使用方式](#使用方式)

进入RocketMQ安装位置，在bin目录下执行`./mqadmin {command} {args}`

#### [命令介绍](#命令介绍)

##### [Topic相关](#topic相关)
名称含义命令选项说明updateTopic创建更新Topic配置-bBroker 地址，表示 topic 所在 Broker，只支持单台Broker，地址为ip:port-ccluster 名称，表示 topic 所在集群（集群可通过 clusterList 查询）-h-打印帮助-nNameServer服务地址，格式 ip:port-p指定新topic的读写权限( W=2|R=4|WR=6 )-r可读队列数（默认为 8）-w可写队列数（默认为 8）-ttopic 名称（名称只能使用字符 ^[a-zA-Z0-9_-]+$ ）deleteTopic删除Topic-ccluster 名称，表示删除某集群下的某个 topic （集群 可通过 clusterList 查询）-h打印帮助-nNameServer 服务地址，格式 ip:port-ttopic 名称（名称只能使用字符 ^[a-zA-Z0-9_-]+$ ）topicList查看 Topic 列表信息-h打印帮助-c不配置-c只返回topic列表，增加-c返回clusterName, topic, consumerGroup信息，即topic的所属集群和订阅关系，没有参数-nNameServer 服务地址，格式 ip:porttopicRoute查看 Topic 路由信息-ttopic 名称-h打印帮助-nNameServer 服务地址，格式 ip:porttopicStatus查看 Topic 消息队列offset-ttopic 名称-h打印帮助-nNameServer 服务地址，格式 ip:porttopicClusterList查看 Topic 所在集群列表-ttopic 名称-h打印帮助-nNameServer 服务地址，格式 ip:portupdateTopicPerm更新 Topic 读写权限-ttopic 名称-h打印帮助-nNameServer 服务地址，格式 ip:port-bBroker 地址，表示 topic 所在 Broker，只支持单台Broker，地址为ip:port-p指定新 topic 的读写权限( W=2|R=4|WR=6 )-ccluster 名称，表示 topic 所在集群（集群可通过 clusterList 查询），-b优先，如果没有-b，则对集群中所有Broker执行命令updateOrderConf从NameServer上创建、删除、获取特定命名空间的kv配置，目前还未启用-h打印帮助-nNameServer 服务地址，格式 ip:port-ttopic，键-vorderConf，值-mmethod，可选get、put、deleteallocateMQ以平均负载算法计算消费者列表负载消息队列的负载结果-ttopic 名称-h打印帮助-nNameServer 服务地址，格式 ip:port-iipList，用逗号分隔，计算这些ip去负载Topic的消息队列statsAll打印Topic订阅关系、TPS、积累量、24h读写总量等信息-h打印帮助-nNameServer 服务地址，格式 ip:port-a是否只打印活跃topic-t指定topic ##### 集群相关 名称含义命令选项说明clusterList查看集群信息，集群、BrokerName、BrokerId、TPS等信息-m打印更多信息 (增加打印出如下信息 #InTotalYest, #OutTotalYest, #InTotalToday ,#OutTotalToday)-h打印帮助-nNameServer 服务地址，格式 ip:port-i打印间隔，单位秒clusterRT发送消息检测集群各Broker RT。消息发往${BrokerName} Topic。-aamount，每次探测的总数，RT = 总时间 / amount-s消息大小，单位B-c探测哪个集群-p是否打印格式化日志，以|分割，默认不打印-h打印帮助-m所属机房，打印使用-i发送间隔，单位秒-nNameServer 服务地址，格式 ip:port ##### Broker相关 名称含义命令选项说明updateBrokerConfig更新 Broker 配置文件，会修改Broker.conf-bBroker 地址，格式为ip:port-ccluster 名称-kkey 值-vvalue 值-h打印帮助-nNameServer 服务地址，格式 ip:portbrokerStatus查看 Broker 统计信息、运行状态（你想要的信息几乎都在里面）-bBroker 地址，地址为ip:port-h打印帮助-nNameServer 服务地址，格式 ip:portbrokerConsumeStatsBroker中各个消费者的消费情况，按Message Queue维度返回Consume Offset，Broker Offset，Diff，TImestamp等信息-bBroker 地址，地址为ip:port-t请求超时时间-ldiff阈值，超过阈值才打印-o是否为顺序topic，一般为false-h打印帮助-nNameServer 服务地址，格式 ip:portgetBrokerConfig获取Broker配置-bBroker 地址，地址为ip:port-nNameServer 服务地址，格式 ip:portwipeWritePerm从NameServer上清除 Broker写权限-bBroker 地址，地址为ip:port-nNameServer 服务地址，格式 ip:port-h打印帮助cleanExpiredCQ清理Broker上过期的Consume Queue，如果手动减少对列数可能产生过期队列-nNameServer 服务地址，格式 ip:port-h打印帮助-bBroker 地址，地址为ip:port-c集群名称cleanUnusedTopic清理Broker上不使用的Topic，从内存中释放Topic的Consume Queue，如果手动删除Topic会产生不使用的Topic-nNameServer 服务地址，格式 ip:port-h打印帮助-bBroker 地址，地址为ip:port-c集群名称sendMsgStatus向Broker发消息，返回发送状态和RT-nNameServer 服务地址，格式 ip:port-h打印帮助-bBrokerName，注意不同于Broker地址-s消息大小，单位B-c发送次数 ##### 消息相关 名称含义命令选项说明queryMsgById根据offsetMsgId查询msg，如果使用开源控制台，应使用offsetMsgId，此命令还有其他参数，具体作用请阅读QueryMsgByIdSubCommand。-imsgId-h打印帮助-nNameServer 服务地址，格式 ip:portqueryMsgByKey根据消息 Key 查询消息-kmsgKey-tTopic 名称-h打印帮助-nNameServer 服务地址，格式 ip:portqueryMsgByOffset根据 Offset 查询消息-bBroker 名称，（这里需要注意 填写的是 Broker 的名称，不是 Broker 的地址，Broker 名称可以在 clusterList 查到）-iquery 队列 id-ooffset 值-ttopic 名称-h打印帮助-nNameServer 服务地址，格式 ip:portqueryMsgByUniqueKey根据msgId查询，msgId不同于offsetMsgId，区别详见常见运维问题。-g，-d配合使用，查到消息后尝试让特定的消费者消费消息并返回消费结果-h打印帮助-nNameServer 服务地址，格式 ip:port-iuniqe msg id-gconsumerGroup-dclientId-ttopic名称checkMsgSendRT检测向topic发消息的RT，功能类似clusterRT-h打印帮助-nNameServer 服务地址，格式 ip:port-ttopic名称-a探测次数-s消息大小sendMessage发送一条消息，可以根据配置发往特定Message Queue，或普通发送。-h打印帮助-nNameServer 服务地址，格式 ip:port-ttopic名称-pbody，消息体-kkeys-ctags-bBrokerName-iqueueIdconsumeMessage消费消息。可以根据offset、开始&结束时间戳、消息队列消费消息，配置不同执行不同消费逻辑，详见ConsumeMessageCommand。-h打印帮助-nNameServer 服务地址，格式 ip:port-ttopic名称-bBrokerName-o从offset开始消费-iqueueId-g消费者分组-s开始时间戳，格式详见-h-d结束时间戳-c消费多少条消息printMsg从Broker消费消息并打印，可选时间段-h打印帮助-nNameServer 服务地址，格式 ip:port-ttopic名称-c字符集，例如UTF-8-ssubExpress，过滤表达式-b开始时间戳，格式参见-h-e结束时间戳-d是否打印消息体printMsgByQueue类似printMsg，但指定Message Queue-h打印帮助-nNameServer 服务地址，格式 ip:port-ttopic名称-iqueueId-aBrokerName-c字符集，例如UTF-8-ssubExpress，过滤表达式-b开始时间戳，格式参见-h-e结束时间戳-p是否打印消息-d是否打印消息体-f是否统计tag数量并打印resetOffsetByTime按时间戳重置offset，Broker和consumer都会重置-h打印帮助-nNameServer 服务地址，格式 ip:port-g消费者分组-ttopic名称-s重置为此时间戳对应的offset-f是否强制重置，如果false，只支持回溯offset，如果true，不管时间戳对应offset与consumeOffset关系-c是否重置c++客户端offset
##### [消费者、消费组相关](#消费者、消费组相关)
名称含义命令选项说明consumerProgress查看订阅组消费状态，可以查看具体的client IP的消息积累量-g消费者所属组名-s是否打印client IP-h打印帮助-nNameServer 服务地址，格式 ip:portconsumerStatus查看消费者状态，包括同一个分组中是否都是相同的订阅，分析Process Queue是否堆积，返回消费者jstack结果，内容较多，使用者参见ConsumerStatusSubCommand-h打印帮助-nNameServer 服务地址，格式 ip:port-gconsumer group-iclientId-s是否执行jstackgetConsumerStatus获取 Consumer 消费进度-g消费者所属组名-t查询主题-iConsumer 客户端 ip-nNameServer 服务地址，格式 ip:port-h打印帮助updateSubGroup更新或创建订阅关系-nNameServer 服务地址，格式 ip:port-h打印帮助-bBroker地址-c集群名称-g消费者分组名称-s分组是否允许消费-m是否从最小offset开始消费-d是否是广播模式-q重试队列数量-r最大重试次数-i当slaveReadEnable开启时有效，且还未达到从slave消费时建议从哪个BrokerId消费，可以配置备机id，主动从备机消费-w如果Broker建议从slave消费，配置决定从哪个slave消费，配置BrokerId，例如1-a当消费者数量变化时是否通知其他消费者负载均衡deleteSubGroup从Broker删除订阅关系-nNameServer 服务地址，格式 ip:port-h打印帮助-bBroker地址-c集群名称-g消费者分组名称cloneGroupOffset在目标群组中使用源群组的offset-nNameServer 服务地址，格式 ip:port-h打印帮助-s源消费者组-d目标消费者组-ttopic名称-o暂未使用
##### [连接相关](#连接相关)
名称含义命令选项说明consumerConnec tion查询 Consumer 的网络连接-g消费者所属组名-nNameServer 服务地址，格式 ip:port-h打印帮助producerConnec tion查询 Producer 的网络连接-g生产者所属组名-t主题名称-nNameServer 服务地址，格式 ip:port-h打印帮助
##### [NameServer相关](#nameserver相关)
名称含义命令选项说明updateKvConfig更新NameServer的kv配置，目前还未使用-s命名空间-kkey-vvalue-nNameServer 服务地址，格式 ip:port-h打印帮助deleteKvConfig删除NameServer的kv配置-s命名空间-kkey-nNameServer 服务地址，格式 ip:port-h打印帮助getNamesrvConfig获取NameServer配置-nNameServer 服务地址，格式 ip:port-h打印帮助updateNamesrvConfig修改NameServer配置-nNameServer 服务地址，格式 ip:port-h打印帮助-kkey-vvalue
##### [其他](#其他)
名称含义命令选项说明startMonitoring开启监控进程，监控消息误删、重试队列消息数等-nNameServer 服务地址，格式 ip:port-h打印帮助
#### [注意事项](#注意事项)

- 几乎所有命令都需要配置-n表示NameServer地址，格式为ip:port

- 几乎所有命令都可以通过-h获取帮助

- 如果既有Broker地址（-b）配置项又有clusterName（-c）配置项，则优先以Broker地址执行命令；如果不配置Broker地址，则对集群中所有主机执行命令

### [集群监控平台搭建](#集群监控平台搭建)

#### [概述](#概述)

`RocketMQ`有一个对其扩展的开源项目[incubator-rocketmq-externals](https://github.com/apache/rocketmq-externals)，这个项目中有一个子模块叫`rocketmq-console`，这个便是管理控制台项目了，先将[incubator-rocketmq-externals](https://github.com/apache/rocketmq-externals)拉到本地，因为我们需要自己对`rocketmq-console`进行编译打包运行。

#### [下载并编译打包](#下载并编译打包)

注意：打包前在`rocketmq-console`中配置`namesrv`集群地址：

启动rocketmq-console：

启动成功后，就可以通过浏览器访问`http://localhost:8080`进入控制台界面了，如下图：
![](/imported/markdown/2025-05-17-markdown-c8891f08-rocketmq-入门/images/2cfa00c69b82-202405182128643.png)
集群状态：
![](/imported/markdown/2025-05-17-markdown-c8891f08-rocketmq-入门/images/54f6de92d707-202405182128074.png)
## [消息发送样例](#消息发送样例)

- 导入MQ客户端依赖

- 消息发送者步骤分析r

- 消息消费者步骤分析

### [基本样例](#基本样例)

#### [消息发送](#消息发送)

##### [发送同步消息](#发送同步消息)

这种可靠性同步地发送方式使用的比较广泛，比如：重要的消息通知，短信通知。

##### [发送异步消息](#发送异步消息)

异步消息通常用在对响应时间敏感的业务场景，即发送端不能容忍长时间地等待Broker的响应。

##### [单向发送消息](#单向发送消息)

这种方式主要用在不特别关心发送结果的场景，例如日志发送。

#### [消费消息](#消费消息)

##### [负载均衡模式](#负载均衡模式)

消费者采用负载均衡方式消费消息，多个消费者共同消费队列消息，每个消费者处理的消息不同

##### [广播模式](#广播模式)

消费者采用广播的方式消费消息，每个消费者消费的消息都是相同的

### [顺序消息](#顺序消息)

消息有序指的是可以按照消息的发送顺序来消费(FIFO)。RocketMQ可以严格的保证消息有序，可以分为分区有序或者全局有序。

顺序消费的原理解析，在默认的情况下消息发送会采取Round Robin轮询方式把消息发送到不同的queue(分区队列)；而消费消息的时候从多个queue上拉取消息，这种情况发送和消费是不能保证顺序。但是如果控制发送的顺序消息只依次发送到同一个queue中，消费的时候只从这个queue上依次拉取，则就保证了顺序。当发送和消费参与的queue只有一个，则是全局有序；如果多个queue参与，则为分区有序，即相对每个queue，消息都是有序的。

下面用订单进行分区有序的示例。一个订单的顺序流程是：创建、付款、推送、完成。订单号相同的消息会被先后发送到同一个队列中，消费时，同一个OrderId获取到的肯定是同一个队列。

#### [顺序消息生产](#顺序消息生产)

#### [顺序消费消息](#顺序消费消息)

### [延时消息](#延时消息)

比如电商里，提交了一个订单就可以发送一个延时消息，1h后去检查这个订单的状态，如果还是未付款就取消订单释放库存。

#### [启动消息消费者](#启动消息消费者)

#### [发送延时消息](#发送延时消息)

#### [验证](#验证)

将会看到消息的消费比存储时间晚10秒

#### [使用限制](#使用限制)

现在RocketMq并不支持任意时间的延时，需要设置几个固定的延时等级，从1s到2h分别对应着等级1到18

### [批量消息](#批量消息)

批量发送消息能显著提高传递小消息的性能。限制是这些批量消息应该有相同的topic，相同的waitStoreMsgOK，而且不能是延时消息。此外，这一批消息的总大小不应超过4MB。

如果您每次只发送不超过4MB的消息，则很容易使用批处理，样例如下：

如果消息的总长度可能大于4MB时，这时候最好把消息进行分割

### [过滤消息](#过滤消息)

在大多数情况下，TAG是一个简单而有用的设计，其可以来选择您想要的消息。例如：

消费者将接收包含TAGA或TAGB或TAGC的消息。但是限制是一个消息只能有一个标签，这对于复杂的场景可能不起作用。在这种情况下，可以使用SQL表达式筛选消息。SQL特性可以通过发送消息时的属性来进行计算。在RocketMQ定义的语法下，可以实现一些简单的逻辑。下面是一个例子：

#### [SQL基本语法](#sql基本语法)

RocketMQ只定义了一些基本语法来支持这个特性。你也可以很容易地扩展它。

- 数值比较，比如：**&gt;，&gt;=，&lt;，&lt;=，BETWEEN，=；**

- 字符比较，比如：**=，&lt;&gt;，IN；**

- **IS NULL** 或者 **IS NOT NULL；**

- 逻辑符号 **AND，OR，NOT；**

常量支持类型为：

- 数值，比如：**123，3.1415；**

- 字符，比如：**'abc'，必须用单引号包裹起来；**

- **NULL**，特殊的常量

- 布尔值，**TRUE** 或 **FALSE**

只有使用push模式的消费者才能用使用SQL92标准的sql语句，接口如下：

#### [消息生产者](#消息生产者)

发送消息时，你能通过`putUserProperty`来设置消息的属性

#### [消息消费者](#消息消费者)

用MessageSelector.bySql来使用sql筛选消息

### [事务消息](#事务消息)

#### [流程分析](#流程分析)
![](/imported/markdown/2025-05-17-markdown-c8891f08-rocketmq-入门/images/9f2e1883769c-202405182128143.png)
上图说明了事务消息的大致方案，其中分为两个流程：正常事务消息的发送及提交、事务消息的补偿流程。

##### [事务消息发送及提交](#事务消息发送及提交)

(1) 发送消息（half消息）。

(2) 服务端响应消息写入结果。

(3) 根据发送结果执行本地事务（如果写入失败，此时half消息对业务不可见，本地逻辑不执行）。

(4) 根据本地事务状态执行Commit或者Rollback（Commit操作生成消息索引，消息对消费者可见）

##### [事务补偿](#事务补偿)

(1) 对没有Commit/Rollback的事务消息（pending状态的消息），从服务端发起一次“回查”

(2) Producer收到回查消息，检查回查消息对应的本地事务的状态

(3) 根据本地事务状态，重新Commit或者Rollback

其中，补偿阶段用于解决消息Commit或者Rollback发生超时或者失败的情况。

##### [事务消息状态](#事务消息状态)

事务消息共有三种状态，提交状态、回滚状态、中间状态：

- TransactionStatus.CommitTransaction: 提交事务，它允许消费者消费此消息。

- TransactionStatus.RollbackTransaction: 回滚事务，它代表该消息将被删除，不允许被消费。

- TransactionStatus.Unknown: 中间状态，它代表需要检查消息队列来确定状态。

#### [发送事务消息](#发送事务消息)

##### [创建事务性生产者](#创建事务性生产者)

使用 `TransactionMQProducer`类创建生产者，并指定唯一的 `ProducerGroup`，就可以设置自定义线程池来处理这些检查请求。执行本地事务后、需要根据执行结果对消息队列进行回复。回传的事务状态在请参考前一节。

##### [实现事务的监听接口](#实现事务的监听接口)

当发送半消息成功时，我们使用 `executeLocalTransaction` 方法来执行本地事务。它返回前一节中提到的三个事务状态之一。`checkLocalTranscation` 方法用于检查本地事务状态，并回应消息队列的检查请求。它也是返回前一节中提到的三个事务状态之一。

#### [使用限制](#使用限制-1)

1. 事务消息不支持延时消息和批量消息。

1. 为了避免单个消息被检查太多次而导致半队列消息累积，我们默认将单个消息的检查次数限制为 15 次，但是用户可以通过 Broker 配置文件的 `transactionCheckMax`参数来修改此限制。如果已经检查某条消息超过 N 次的话（ N = `transactionCheckMax` ） 则 Broker 将丢弃此消息，并在默认情况下同时打印错误日志。用户可以通过重写 `AbstractTransactionCheckListener` 类来修改这个行为。

1. 事务消息将在 Broker 配置文件中的参数 transactionMsgTimeout 这样的特定时间长度之后被检查。当发送事务消息时，用户还可以通过设置用户属性 CHECK_IMMUNITY_TIME_IN_SECONDS 来改变这个限制，该参数优先于 `transactionMsgTimeout` 参数。

1. 事务性消息可能不止一次被检查或消费。

1. 提交给用户的目标主题消息可能会失败，目前这依日志的记录而定。它的高可用性通过 RocketMQ 本身的高可用性机制来保证，如果希望确保事务消息不丢失、并且事务完整性得到保证，建议使用同步的双重写入机制。

1. 事务消息的生产者 ID 不能与其他类型消息的生产者 ID 共享。与其他类型的消息不同，事务消息允许反向查询、MQ服务器能通过它们的生产者 ID 查询到消费者。
