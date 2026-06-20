{

  "title": "Kafka - 入门",
  "has_date": true,
  "description": "Kafka基础架构 在Kafka2.8版本前，Zookeeper的Consumer文件中存放消息被消费的记录（offset） 在Kafka2.8版本后，消息被消费的记录（offset）存放在Kafka中。 （1）Producer：消息生产者，就是向 Kafka broker 发消息的客户端。 （2）",
  "tags": [
    "微服务",
    "消息队列",
    "Kafka"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/message-queue/kafka-basic - Kafka - 入门.md",
  "date": "2026-01-27"

}

## [Kafka基础架构](#kafka基础架构)
![](/imported/markdown/2026-01-27-markdown-421d333b-kafka-入门/images/7f7699e343f3-202405182232939.gif)
在Kafka2.8版本前，Zookeeper的Consumer文件中存放消息被消费的记录（offset）

在Kafka2.8版本后，消息被消费的记录（offset）存放在Kafka中。

（1）Producer：消息生产者，就是向 Kafka broker 发消息的客户端。

（2）Consumer：消息消费者，向 Kafka broker 取消息的客户端。

（3）Consumer Group（CG）：消费者组，由多个 consumer 组成。消费者组内每个消费者负责消费不同分区的数据，一个分区只能由一个组内消费者消费；消费者组之间互不影响。所有的消费者都属于某个消费者组，即消费者组是逻辑上的一个订阅者。

（4）Broker：一台 Kafka 服务器就是一个 broker。一个集群由多个 broker 组成。一个broker 可以容纳多个 topic。

（5）Topic：可以理解为一个队列，生产者和消费者面向的都是一个 topic。

（6）Partition：为了实现扩展性，一个非常大的 topic 可以分布到多个 broker（即服务器）上，一个 topic 可以分为多个 partition，每个 partition 是一个有序的队列。

（7）Replica：副本。一个 topic 的每个分区都有若干个副本，一个 Leader 和若干个Follower。

（8）Leader：每个分区多个副本的“主”，生产者发送数据的对象，以及消费者消费数据的对象都是 Leader。

（9）Follower：每个分区多个副本中的“从”，实时从 Leader 中同步数据，保持和Leader 数据的同步。Leader 发生故障时，某个 Follower 会成为新的 Leader。

## [安装部署](#安装部署)

### [集群规划](#集群规划)
![](/imported/markdown/2026-01-27-markdown-421d333b-kafka-入门/images/0747805022e7-202405182233888.gif)
### [集群部署](#集群部署)

0）官方下载地址：[http://kafka.apache.org/downloads.html](http://kafka.apache.org/downloads.html)

1）解压安装包

2)修改解压后的文件名称

3）进入到/opt/module/kafka 目录，修改配置文件

输入以下内容：

4）分发安装包

5）分别在 hadoop103 和 hadoop104 上修改配置文件/opt/module/kafka/config/server.properties中的 broker.id=1、broker.id=2

注：[broker.id](http://broker.id) 不得重复，整个集群中唯一。

修改：

6）配置环境变量

（1）在/etc/profile.d/my_env.sh 文件中增加 kafka 环境变量配置

刷新环境变量

### [启动](#启动)

（1） Zookeeper启动 (默认守护进程)

Zookeeper状态

Zookeeper停止

Zookeeper客户端-常⽤命令

(2) 启动Kafka

Kafka 守护方式 (环境变量配置前提下)

Kafka关闭

注意：停止 Kafka 集群时，一定要等 Kafka 所有节点进程全部停止后再停止 Zookeeper集群。因为 Zookeeper 集群当中记录着 Kafka 集群相关信息，Zookeeper 集群一旦先停止，Kafka 集群就没有办法再获取停止进程的信息，只能手动杀死 Kafka 进程了。

## [Kafka命令行操作](#kafka命令行操作)
![](/imported/markdown/2026-01-27-markdown-421d333b-kafka-入门/images/04c859102106-202405182238618.gif)
### [主题命令行操作](#主题命令行操作)

查看操作主题命令参数
![](/imported/markdown/2026-01-27-markdown-421d333b-kafka-入门/images/cb78bbe180f4-202405182238777.jpg)
2）查看当前服务器中的所有 topic

3）创建 first topic

选项说明：

4）查看 first 主题的详情

5）修改分区数（注意：分区数只能增加，不能减少）

6）再次查看 first 主题的详情

7）删除 topic(需要配置信息)

### [生产者命令行操作](#生产者命令行操作)

1）查看操作生产者命令参数

连接kafka生产者

参数 描述

2）发送消息

### [消费者命令行操作](#消费者命令行操作)

1）查看操作消费者命令参数

连接kafka消费者

参数 描述

2）消费消息

（1）消费 first 主题中的数据。

（2）把主题中所有的数据都读取出来（包括历史数据）。

## [SpringBoot 整合Kafka](#springboot-整合kafka)
![](/imported/markdown/2026-01-27-markdown-421d333b-kafka-入门/images/bd9b5f1e5586-202406161834850.png)
### [引入依赖](#引入依赖)

### [SpringBoot生产者](#springboot生产者)

修改 SpringBoot核心配置文件 application.propeties, 添加生产者相关信息

创建 controller从浏览器接收数据 , 并写入指定的 topic

### [SpringBoot消费者](#springboot消费者)

修改 SpringBoot核心配置文件 application.propeties

创建类消费 Kafka中指定 topic的数据
