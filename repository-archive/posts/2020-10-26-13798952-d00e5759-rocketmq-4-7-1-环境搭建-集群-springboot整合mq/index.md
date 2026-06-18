{

  "title": "RocketMQ 4.7.1 环境搭建、集群、SpringBoot整合MQ",
  "date": "2020-10-26",
  "description": "导读 之前学过ActiveMQ但是并发量不是很大点我直达，所以又学阿里开源的RocketMQ，据说队列可以堆积**亿级别**。下面是网上找的消息队列对比图，仅供参考 部署 官网 点我直达 前置条件 推荐使用64位操作系统，建议使用Linux / Unix / Mac； 位JDK 1.8+; Mave",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13798952.html"

}

# 导读

　　之前学过ActiveMQ但是并发量不是很大[点我直达](https://www.cnblogs.com/chenyanbin/p/12841966.html)，所以又学阿里开源的RocketMQ，据说队列可以堆积**亿级别**。下面是网上找的消息队列对比图，仅供参考

![](./images/images/img_001_74c122a29c8a.png)

# 部署

## 官网

[点我直达](http://rocketmq.apache.org/)

## 前置条件

1. 推荐使用64位操作系统，建议使用Linux / Unix / Mac；
2. 64位JDK 1.8+;
3. Maven 3.2.x;
4. Git;
5. 适用于Broker服务器的内存4G +可用磁盘

![](./images/images/img_002_1ad6a220e9f8.gif)

## 下载

![](./images/images/img_003_0323fa3875b0.gif)

地址：[https://downloads.apache.org/rocketmq/4.7.1/rocketmq-all-4.7.1-source-release.zip](https://downloads.apache.org/rocketmq/4.7.1/rocketmq-all-4.7.1-source-release.zip)

百度云盘：

```text
链接: https://pan.baidu.com/s/1luq_MwxSn8k_bugrnQSJWg  密码: varj
```

## 安装依赖项

1. jdk：[点我直达](https://www.cnblogs.com/chenyanbin/p/12843149.html)
2. maven：[点我直达](https://www.cnblogs.com/chenyanbin/p/13662849.html)
3. git安装：**yum install -y git**

```text
export JAVA_HOME=/opt/soft/jdk1.8.0_202
export PATH=$JAVA_HOME/bin:$PATH
export CLASPATH=.:$JAVA_home/lib/dt.jar:$JAVA_HOME/lib/tools.jar
export JAVA_HOME PATH CLASSPATH
export MAVEN_HOME=/opt/soft/apache-maven-3.6.3
export PATH=$PATH:$MAVEN_HOME/bin
```

## mq上传至linux

![](./images/images/img_004_dd5d30bdb4b1.png)

## 解压

![](./images/images/img_005_abef819a112a.png)

### maven编译

![](./images/images/img_006_1ce86cc21d78.png)

## 启动NameServer

![](./images/images/img_007_3ee1f9fdd249.png)

### 后台启动方式

```text
nohup sh bin/mqnamesrv &
```

### NameServer启动时内存不足(问题解决)

```text
找到runserver.sh 修改JAVA_OPT

vim /bin/runserver.sh配置
```

![](./images/images/img_008_632f72deb5e3.gif)

## 启动Broker

```text
nohup sh bin/mqbroker -n localhost:9876 &

语法：nohup sh bin/mqbroker -n NameServer服务ip地址
```

![](./images/images/img_009_cf5064280ced.png)

### Broker内存不足（问题解决）

```text
找到runbroker.sh 修改JAVA_OPT

vim /bin/runbroker.sh配置
```

![](./images/images/img_010_caddf8d64cfd.gif)

## 服务都启动成功

![](./images/images/img_011_112ed3f496cb.png)

## 模拟消费

```text
export NAMESRV_ADDR=localhost:9876

sh bin/tools.sh org.apache.rocketmq.example.quickstart.Producer

sh bin/tools.sh org.apache.rocketmq.example.quickstart.Consumer
```

开2个控制台，连接通一台linux

![](./images/images/img_012_a91b2cae3797.gif)

## 注意

**NameServer默认端口号：9876；broker默认端口号：10911**

## 可视化控制台

### 官网地址

[点我直达](https://github.com/apache/rocketmq-externals)

百度云盘

```text
链接: https://pan.baidu.com/s/1mdEGkq-JBTy1wtNmFPkmDg  密码: v6bq
```

### 解压

![](./images/images/img_013_7ea7080f80cb.gif)

### 安装编译

```text
进入：/opt/soft/rocketmq-externals-master/rocketmq-console
编译： mvn clean package -Dmaven.test.skip=true
```

**修改appliccation.properties的rocketmq.config.namesrvAddr**

![](./images/images/img_014_faa820b2518b.gif)

**编译打包**

![](./images/images/img_015_2fd2da08cb4f.gif)

### 启动

　　进入target目录，启动java -jar

```text
守护进程启动： nohup java -jar rocketmq-console-ng-2.0.0.jar &
```

![](./images/images/img_016_5b891ada6098.gif)

# SpringBoot整合RocketMQ(生产者)

## 创建SpringBoot项目

[点我直达](https://start.spring.io/)

![](./images/images/img_017_ed2696427887.gif)

### 项目结构

![](./images/images/img_018_3fbe41bce515.png)

### 加入依赖

pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.3.1.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.ybchen</groupId>
    <artifactId>ybchen-mq</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>ybchen-mq</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.junit.vintage</groupId>
                    <artifactId>junit-vintage-engine</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <!--注意： 这里的版本,要和部署在服务器上的版本号一致-->
        <dependency>
            <groupId>org.apache.rocketmq</groupId>
            <artifactId>rocketmq-client</artifactId>
            <version>4.7.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.rocketmq</groupId>
            <artifactId>rocketmq-common</artifactId>
            <version>4.7.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

### PayProducer.java

```text
package com.ybchen.ybchenmq.jms;

import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.client.producer.DefaultMQProducer;
import org.springframework.stereotype.Component;

/**
 * 消息生产者
 */
@Component
public class PayProducer {
    /**
     * 生产者所属的组
     */
    private String producerGroup = "pay_group";
    /**
     * MQ的地址，注意需开放端口号或者关闭防火墙
     */
    private String nameServerAddr = "192.168.199.100:9876";
    private DefaultMQProducer producer;

    public PayProducer() {
        producer = new DefaultMQProducer(producerGroup);
        //指定NameServer地址，多个地址以;隔开
        //如 producer.setNamesrvAddr("192.168.199.100:9876;192.168.199.101:9876;192.168.199.102:9876")
        producer.setNamesrvAddr(nameServerAddr);
        start();
    }

    /**
     * 获取生产者
     * @return
     */
    public DefaultMQProducer getProducer() {
        return this.producer;
    }

    /**
     * 开启，对象在使用之前必须要调用一次，只能初始化一次
     */
    public void start() {
        try {
            this.producer.start();
        } catch (MQClientException e) {
            e.printStackTrace();
        }
    }

    /**
     * 关闭，一般在应用上下文，使用上下文监听器，进行关闭
     */
    public void shutdown() {
        this.producer.shutdown();
    }
}
```

### PayController.java

```text
package com.ybchen.ybchenmq.controller;

import com.ybchen.ybchenmq.jms.PayProducer;
import org.apache.rocketmq.client.exception.MQBrokerException;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.client.producer.SendResult;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.remoting.exception.RemotingException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @ClassName：PayController
 * @Description：支付
 * @Author：chenyb
 * @Date：2020/10/18 2:47 下午
 * @Versiion：1.0
 */
@RestController
@RequestMapping("/api/v1")
public class PayController {
    @Autowired
    private PayProducer payProducer;

    private static final String TOPIC = "ybchen_pay_topic";

    /**
     * 支付回调
     *
     * @param text
     * @return
     */
    @RequestMapping("pay_cb")
    public Object callback(String text) {
        /**
         * String topic：话题
         * String tags：二级分类
         * byte[] body：body消息字节数组
         */
        Message message = new Message(TOPIC,"tag_a",("hello ybchen ==>"+text).getBytes());
        try {
            SendResult send = payProducer.getProducer().send(message);
            System.out.println("send------>"+send);
        } catch (MQClientException e) {
            e.printStackTrace();
        } catch (RemotingException e) {
            e.printStackTrace();
        } catch (MQBrokerException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return "ok";
    }
}
```

### 测试

![](./images/images/img_019_c46310d8e4af.gif)

## 常见错误

### 错误一

```text
org.apache.rocketmq.remoting.exception.RemotingTooMuchRequestException:
sendDefaultImpl call timeout
```

```text
原因：阿里云存在多网卡，rocketmq会根据当前网卡选择一个IP使用，当你的机器有多块网卡时，很可能会有问题，比如，机器上有两个ip，一个公网ip，一个私网ip，因此需要配置broker.conf指定当前公网的ip，然后重启broker

修改配置：/opt/soft/rocketmq-all-4.7.1-source-release/distribution/target/rocketmq-4.7.1/rocketmq-4.7.1/conf/broker.conf
新增这个配置：brokerIP1=xxx.xxx.xxx.xxx

启动命令：nohup sh bin/mqbroker -n localhost:9876 -c ./conf/broker.conf &
```

### 错误2

```text
MQClientException: No route info of this topic, TopicTest1

原因：Broker 紧追自动创建Topic，且用户没有通过手工方式创建此Topic，或者broker和Nameserver网络不通

解决：
    通过sh bin/mqbroker -m 查看配置
    autoCreateTopicEnable=true 则自动创建Topic

Centos 7 关闭防火墙：systemctl stop firewalld
```

### 错误3

```text
控制台查看不了数据，提示连接10909错误

原因：Rocket默认开启了VIP通道，VPI通道端口号为10911-2=10909

解决：阿里云安全组添加一个端口：10909
```

### 错误4

　　无法自动创建topic：客户端版本要和服务端版本保持一致

```text
服务器上装的是4.7.1

引入依赖项时
        <!--注意： 这里的版本,要和部署在服务器上的版本号一致-->
        <dependency>
            <groupId>org.apache.rocketmq</groupId>
            <artifactId>rocketmq-client</artifactId>
            <version>4.7.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.rocketmq</groupId>
            <artifactId>rocketmq-common</artifactId>
            <version>4.7.1</version>
        </dependency>
```

## 检索消息发送

![](./images/images/img_020_8982656f183d.gif)

# SpringBoot整合RocketMQ(消费者)

## 创建SpringBoot项目

![](./images/images/img_021_cc85476c4979.png)

### 项目结构

![](./images/images/img_022_910e2e3ebc90.png)

### 加入依赖

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.3.1.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.ybchen</groupId>
    <artifactId>ybchen-mq</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>ybchen-mq</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.junit.vintage</groupId>
                    <artifactId>junit-vintage-engine</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <!--注意： 这里的版本,要和部署在服务器上的版本号一致-->
        <dependency>
            <groupId>org.apache.rocketmq</groupId>
            <artifactId>rocketmq-client</artifactId>
            <version>4.7.1</version>
        </dependency>
        <dependency>
            <groupId>org.apache.rocketmq</groupId>
            <artifactId>rocketmq-common</artifactId>
            <version>4.7.1</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

### PayConsumer.java

```text
package com.ybchen.ybchenmqconsumer.jms;

import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyContext;
import org.apache.rocketmq.client.consumer.listener.ConsumeConcurrentlyStatus;
import org.apache.rocketmq.client.consumer.listener.MessageListenerConcurrently;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.consumer.ConsumeFromWhere;
import org.apache.rocketmq.common.message.Message;
import org.apache.rocketmq.common.message.MessageExt;
import org.springframework.stereotype.Component;

import java.io.UnsupportedEncodingException;
import java.util.List;

/**
 * @ClassName：PayConsumer
 * @Description：消费者
 * @Author：chenyb
 * @Date：2020/10/18 4:13 下午
 * @Versiion：1.0
 */
@Component
public class PayConsumer {
    /**
     * 生产者所属的组
     */
    private String producerGroup = "pay_consumer_group";
    /**
     * MQ的地址，注意需开放端口号或者关闭防火墙
     */
    private String nameServerAddr = "192.168.199.100:9876";
    /**
     * 订阅主题
     */
    private String topic = "ybchen_pay_topic";
    private DefaultMQPushConsumer consumer;

    public PayConsumer() throws MQClientException {
        consumer = new DefaultMQPushConsumer(producerGroup);
        //指定NameServer地址，多个地址以;隔开
        //如 producer.setNamesrvAddr("192.168.199.100:9876;192.168.199.101:9876;192.168.199.102:9876")
        consumer.setNamesrvAddr(nameServerAddr);
        //设置消费地点，从最后一个开始消费
        consumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_LAST_OFFSET);
        //订阅主题，监听主题下的那些标签
        consumer.subscribe(topic, "*");
        //注解一个监听器
        //lambda方式
//        consumer.registerMessageListener((MessageListenerConcurrently) (msg, context) -> {
//            try {
//                Message message = msg.get(0);
//                System.out.printf("%s Receive New Messages: %s %n",
//                        Thread.currentThread().getName(), new String(msg.get(0).getBody()));
//                //主题
//                String topic = message.getTopic();
//                //消息内容
//                String body = null;
//                body = new String(message.getBody(), "utf-8");
//                //二级分类
//                String tags = message.getTags();
//                //键
//                String keys = message.getKeys();
//                System.out.println("topic=" + topic + ", tags=" + tags + ", keys=" + keys + ", msg=" + body);
//                return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
//            } catch (UnsupportedEncodingException e) {
//                e.printStackTrace();
//                return ConsumeConcurrentlyStatus.RECONSUME_LATER;
//            }
//        });

        //一般方式
        consumer.registerMessageListener(new MessageListenerConcurrently() {
            @Override
            public ConsumeConcurrentlyStatus consumeMessage(List<MessageExt> list, ConsumeConcurrentlyContext consumeConcurrentlyContext) {
                try {
                    Message message = list.get(0);
                    System.out.printf("%s Receive New Messages: %s %n",
                            Thread.currentThread().getName(), new String(list.get(0).getBody(),"utf-8"));
                    //主题
                    String topic = message.getTopic();
                    //消息内容
                    String body = null;
                    body = new String(message.getBody(), "utf-8");
                    //二级分类
                    String tags = message.getTags();
                    //键
                    String keys = message.getKeys();
                    System.out.println("topic=" + topic + ", tags=" + tags + ", keys=" + keys + ", msg=" + body);
                    return ConsumeConcurrentlyStatus.CONSUME_SUCCESS;
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                    return ConsumeConcurrentlyStatus.RECONSUME_LATER;
                }
            }
        });
        consumer.start();
        System.out.println("consumer start ..........");
    }
}
```

### application.properties

```text
server.port=8081
```

# 测试生产者消费者

![](./images/images/img_023_5b35b55e6d49.gif)

![](./images/images/img_024_6b74fec29943.gif)

# MQ集群架构模式分析

## 单节点

### 优点

　　本地开发测试，配置简单，同步刷盘消息一条都不会丢

### 缺点

　　不可靠，如果宕机，会导致服务不可用

## 主从(异步、同步双写)

### 优点

　　同步双写消息不丢失，异步复制存在少量丢失你，主节点宕机，从节点可以对外提供消息的消费，但是不支持写入

### 缺点

　　主备有短暂消息延迟，毫秒级，目前不支持自动切换，需要脚本或者其他程序进行检测然后停止broker，重启让从节点成为主节点

## 双主

### 优点

　　配置简单，可以靠配置RAID磁盘阵列保证消息可靠，异步刷盘丢失少量消息

### 缺点

　　master宕机期间，未被消费的消息在机器恢复之前不可消息，实时性会受到影响

## 双主双从，多主多从模式(异步复制)

### 优点

　　磁盘损坏，消息丢失的非常小，消息实时性不会受影响，Master宕机后，消费者仍然可以从Slave消费

### 缺点

　　主备有短暂消息延迟，毫秒级，如果Master宕机，磁盘损坏情况，会丢失你少量消息

## 双主双从，多主多从模式(同步双写)

### 优点

　　同步双写方式，主备都写成功，才向应用返回成功，服务可用性与数据可用性非常高

### 缺点

　　性能比异步复制模式略低，主宕机后，备机不能自动切换为主机

## 推荐

1. 主从(异步、同步双写)
2. 双主双从，多主多从模式(异步复制)
3. 双主双从，多主多从模式(同步双写)

# 主从集群搭建

## 准备工作

　　准备2台机器，ip地址分别为：192.168.199.100；192.168.199.101；

　　环境：RocketMQ4.7.1+jdk8+Maven+Centos 7

## 启动两台nameserver

　　启动两个机器的nameserver

```text
路径：/opt/soft/rocketmq-all-4.7.1-source-release/distribution/target/rocketmq-4.7.1/rocketmq-4.7.1

启动：nohup sh bin/mqnamesrc &
```

## 编辑并启动roccketmq

```text
主节点

进入：/opt/soft/rocketmq-all-4.7.1-source-release/distribution/target/rocketmq-4.7.1/rocketmq-4.7.1/conf/2m-2s-async

编辑并修改如下：vim broker-a.properties
namesrvAddr=192.168.199.100:9876;192.168.199.101:9876
brokerClusterName=YbChenCluster
brokerName=broker-a
brokerId=0
deleteWhen=04
fileReservedTime=48
brokerRole=ASYNC_MASTER
flushDiskType=ASYNC_FLUSH

启动：nohup sh bin/mqbroker -c conf/2m-2s-async/broker/broker-a.properties &
```

![](./images/images/img_025_aa81916c0172.gif)

```text
从节点

进入：/opt/soft/rocketmq-all-4.7.1-source-release/distribution/target/rocketmq-4.7.1/rocketmq-4.7.1/conf/2m-2s-async

编辑并修改如下：vim broker-a-s.properties
namesrvAddr=192.168.199.100:9876;192.168.199.101:9876
brokerClusterName=YbChenCluster
brokerName=broker-a
brokerId=1
deleteWhen=04
fileReservedTime=48
brokerRole=SLAVE
flushDiskType=ASYNC_FLUSH

启动：nohup sh bin/mqbroker -c conf/2m-2s-async/broker/broker-a-s.properties &
```

### 注意事项

1. namesrvAddr：相同
2. brokerClusterName：相同
3. brokerName：相同
4. brokerId：**不同**，0是主节点
5. deleteWhen：相同
6. fileReservedTime：相同
7. brokerRole：**不同**，分ASYNC_MASTER、SLAVE
8. flushDiskType：相同

## 启动broker

![](./images/images/img_026_0858dfa937be.gif)

## 使用管控台

　　使用192.168.199.100这台服务器，修改配置

```text
192.168.199.100这台服务器

进入：/opt/soft/rocketmq-externals-master/rocketmq-console/src/main/resources

修改配置文件：vim application.properties

rocketmq.config.namesrvAddr=192.168.199.100:9876;192.168.199.101:9876

编译

切换到：/opt/soft/rocketmq-externals-master/rocketmq-console
打包：
mvn clean
mvn install -Dmaven.test.skip=true

启动

进入：/opt/soft/rocketmq-externals-master/rocketmq-console/target
守护进程方式启动：nohup java -jar rocketmq-console-ng-2.0.0.jar &
```

![](./images/images/img_027_274e46af9dce.gif)

## 集群测试

![](./images/images/img_028_fed8dd683345.gif)

## 故障演练

　　模拟主挂了，但是从还可以被消费，此时不能写入，等主重启后，可以继续写入(数据不会被重复消费)，以下内容是连续的

![](./images/images/img_029_d19c10ef140a.gif)

![](./images/images/img_030_5b8373377bef.gif)

![](./images/images/img_031_ecaa72d47e8d.gif)

## 总结

　　好了，到目前为止，主从已经搭建完成了。

**Broker分**为**Master和Slave**，**一个Master可以对应多个Slave**，但**一个Slave只能对应一个Master**，Master与Slave**通过相同的Broker Name来匹配**，不同的**Broker id来定义时Master还是Slave**

　　　　Broker向所有的NameServer节点建立长连接，定时注册Topic和发送元数据信息

　　　　NameServer定时扫描(默认2分钟)所有存活Broker的连接，如果超过时间没响应，则断开连接(心跳检测)，但是Consumer客户端不能感知，Consumer定时(30秒)从NameServer获取topic的最新信息，所以broker不可用时，Consumer最多需要30秒才能发现

**只有Master才能进行写入操作**，**Slave不允许写入只能同步**，同步策略取决于Master配置

**客户端消费可以从Master和Slave消费，默认消费者都从Master消费**，如果在Master挂了之后，客户端从NameServer中感知Broker宕机，就会从Slave消费，感知非实时，存在一定的滞后性，Slave不能保证Master的100%都同步过来，会有少量的消息丢失。一旦Master恢复，未同步过去的消息会被最终消费掉。

　　如果Consumer实例的数量比Message Queue的总数量还多的话，多出来的Consumer实例将无法分到Queue，也就无法消费到消息，也就无法起到分摊负载的作用，所以需要控制让Queue的总数量大于Consumer的数量。

# 场景模拟

## 生产和消费重试及处理

### 生产者重试

- 消息重试(保证数据的高可靠性)，本身内部支持重试，默认次数是2
- 如果网络情况较差，或者跨集群则建议多改几次

生产者设置重试次数，并设置唯一的key(一般唯一标识符)

![](./images/images/img_032_2b26e32a507a.png)

![](./images/images/img_033_8196d017e504.gif)

### 消费者重试

- 原因：消息处理异常，broker端到consumer端各种问题，如网络原因闪断，消费处理失败，ACK返回失败等
- 注意

  - 重试间隔时间配置，默认每条消息**最多重试16次**
  - 超过重试次数人工补偿
  - 消费端去重
  - 一条消息无论重试多少次，这些重试消息的**Message ID，key不会改变**
  - 消费重试只针对集群消费方式生效；广播方式不提供失败重试特性，即消费失败后，失败消息不再重试，继续消费新的消息

![](./images/images/img_034_64bc85abec5d.png)

设置广播方式

![](./images/images/img_035_c8304924317b.png)

### 模拟消息重发

![](./images/images/img_036_36c5fe064291.gif)

![](./images/images/img_037_8cc5f475321b.gif)

## 异步发送消息和回调实战

### 应用场景

　　比如12306付完钱💰后，异步出票，对性能要求高，可以支持更高的并发，回调成功后触发相应的业务(onSuccess)

### 官方例子

[点我直达](http://rocketmq.apache.org/docs/simple-example/)

![](./images/images/img_038_9ae1219014c5.gif)

### 改造生产者

![](./images/images/img_039_15d2bd71c362.png)

### 演示

![](./images/images/img_040_68d1f2620e1e.gif)

```text
onSuccess：因为是异步方式，这里可以记录日志啥的
onException：补偿机制，根据实际情况使用，看是否进行重试
```

## OneWay(无需等待)

### 应用场景

　　主要做日志收集，适用于对性能要求高，但可靠性并不高的场景。

![](./images/images/img_041_e6dde3487bbd.png)

## 延迟消息实战

### 什么是延迟消息

- Producer将消息发送到消息队列RocketMQ服务端，但并不期望这条消息立马投递，而是推迟在当前时间点之后的某一个时间投递到Consumer进行消费，该消息即定时消息，目前支持固定精度的消息
- 延迟消息级别，1....18

```text
1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h
```

![](./images/images/img_042_7c5795b63046.png)

### 应用场景

- 通过消息触发一些定时任务，比如在某一固定时间点向用户发送提醒消息
- 消息生产和消费有时间窗口要求：比如在天猫电商交易中超时未支付关闭订单的场景，在订单创建时会发送一条延迟消息。这条消息将会在30分钟以后投递给消费者，消费者收到此消息后需要判断对应的订单是否已完成支付。如支付未完成，则关闭订单。如已完成支付则忽略。

### 改生产者

![](./images/images/img_043_605cc93fdfcf.png)

## 生产者MessageQueueSelector实战

### 简介

　　生产消息使用MessageQueueSelector投递到Topic下指定的Queue

### 应用场景

- 顺序消息
- 分摊负载

默认topic下的queue数量是4，可以配置

支持同步，异步发送指定的MessageQueue

选择的queue数量必须小于配置的，否则会出错

### 好处

　　如果队列中某个产品，流量暴增，随机分配的话，会导致整个Topic都不能使用，指定到队列的话，如果这个队列坏了，其他队列不影响使用。

### 改造生产者

#### 同步发送

![](./images/images/img_044_4fd216a70e3a.png)

```text
发送结果=SEND_OK，msg=SendResult [sendStatus=SEND_OK, msgId=AC1068013E3F18B4AAC276723EAC0000, offsetMsgId=C0A8C76400002A9F000000000009B536, messageQueue=MessageQueue [topic=ybchen_pay_topic, brokerName=broker-a, queueId=0], queueOffset=1]
发送结果=SEND_OK，msg=SendResult [sendStatus=SEND_OK, msgId=AC1068013E3F18B4AAC27672BCD50001, offsetMsgId=C0A8C76400002A9F000000000009B602, messageQueue=MessageQueue [topic=ybchen_pay_topic, brokerName=broker-a, queueId=0], queueOffset=2]
发送结果=SEND_OK，msg=SendResult [sendStatus=SEND_OK, msgId=AC1068013E3F18B4AAC27672CAA20002, offsetMsgId=C0A8C76400002A9F000000000009B6CF, messageQueue=MessageQueue [topic=ybchen_pay_topic, brokerName=broker-a, queueId=0], queueOffset=3]
```

　　可以看到打印出来的，queueId=0

#### 异步发送

生产者端代码修改

```text
    @Autowired
    private PayProducer payProducer;

    private static final String TOPIC = "ybchen_pay_topic";

    /**
     * 支付回调
     *
     * @param text
     * @return
     */
    @RequestMapping("pay_cb")
    public Object callback(String text) {
        /**
         * String topic：话题
         * String tags：二级分类
         * byte[] body：body消息字节数组
         */
        Message message = new Message(TOPIC, "tag_a", text.getBytes());
        //生产者使用MessageQueueSelector投递到Topic下指定的Queue，arg只能小于等于4
//        try {
//            SendResult sendResult = payProducer.getProducer().send(message, new MessageQueueSelector() {
//                @Override
//                public MessageQueue select(List<MessageQueue> list, Message message, Object o) {
//                    int queueNum=Integer.parseInt(o.toString());
//                    return list.get(queueNum);
//                }
//            }, 0);
//            System.out.printf("发送结果=%s，msg=%s",sendResult.getSendStatus(),sendResult);
//        } catch (MQClientException e) {
//            e.printStackTrace();
//        } catch (RemotingException e) {
//            e.printStackTrace();
//        } catch (MQBrokerException e) {
//            e.printStackTrace();
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//        }
        //异步发送到指定的queue
        try {
            payProducer.getProducer().send(message, new MessageQueueSelector() {
                @Override
                public MessageQueue select(List<MessageQueue> list, Message message, Object o) {
                    int queueNum = Integer.parseInt(o.toString());
                    return list.get(queueNum);
                }
            }, 3, new SendCallback() {
                @Override
                public void onSuccess(SendResult sendResult) {
                    System.out.printf("发送结果=%s，msg=%s", sendResult.getSendStatus(), sendResult);
                }

                @Override
                public void onException(Throwable e) {
                    e.printStackTrace();
                }
            });
        } catch (MQClientException e) {
            e.printStackTrace();
        } catch (RemotingException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        //1s 5s 10s 30s 1m 2m 3m 4m 5m 6m 7m 8m 9m 10m 20m 30m 1h 2h
        //message.setDelayTimeLevel(2);
//        try {
//            SendResult send = payProducer.getProducer().send(message);
//            System.out.println("send------>"+send);
//        } catch (MQClientException e) {
//            e.printStackTrace();
//        } catch (RemotingException e) {
//            e.printStackTrace();
//        } catch (MQBrokerException e) {
//            e.printStackTrace();
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//        }
        //异步发送
//        try {
//            payProducer.getProducer().send(message, new SendCallback() {
//                @Override
//                public void onSuccess(SendResult sendResult) {
//                    System.out.printf("发送结果=%s，msg=%s",sendResult.getSendStatus(),sendResult);
//                }
//
//                @Override
//                public void onException(Throwable e) {
//                    e.printStackTrace();
//                    //补偿机制，根据实际情况使用，看是否进行重试
//                }
//            });
//        } catch (MQClientException e) {
//            e.printStackTrace();
//        } catch (RemotingException e) {
//            e.printStackTrace();
//        } catch (InterruptedException e) {
//            e.printStackTrace();
//        }
        return "ok";
    }
```

## 顺序消息的应用场景

## 简介

　　顺序消息可以应用到电商和证券系统，订单系统。

## 什么是顺序系统？

　　消息的生产和消费顺序一致

### 全局顺序

　　topic下面全部消息都要有序(很少用)

1. 性能要求不高，所有的消息严格按照FIFO(先进先出)原则进行消息发布和消费的场景，并行度成为消息系统的瓶颈，吞吐量不够
2. 在证券处理中，以人民币兑换美元为例，在价格相同的情况下，先出价者优先处理，则可以通过全局顺序的方式进行发布和消费

### 局部顺序

　　只要保证一组消息被顺序消费即可(RocketMQ中使用)

1. 性能要求高
2. 电商的订单创建，同一订单相关的创建订单消息、订单支付消息、订单退款消息、订单物流消息、订单交易成功消息都会按照先后顺序来发布和消费

### 顺序发布

　　对于指定的一个Topic，客户端按照一定的先后顺序发送消息

### 顺序消费

　　对于指定的一个Topic，按照一定的先后顺序接收消息，即先发送的消息一定先会被客户端接收到

### 注意事项

1. **顺序消息不支持异步发送**，否则将无法保证顺序消费
2. 顺序消息暂不支持广播模式

### 官方例子

[点我直达](http://rocketmq.apache.org/docs/order-example/)

### 改造生产者代码

创建ProductOrder.java

![](./images/images/img_045_316e0767046e.png)

```text
package com.ybchen.ybchenmq.entity;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

/**
 * @ClassName：ProductOrder
 * @Description：订单
 * @Author：chenyb
 * @Date：2020/10/25 12:56 下午
 * @Versiion：1.0
 */
public class ProductOrder implements Serializable {
    /**
     * 订单id
     */
    private long orderIdl;
    /**
     * 订单操作类型
     */
    private String type;

    public long getOrderIdl() {
        return orderIdl;
    }

    public void setOrderIdl(long orderIdl) {
        this.orderIdl = orderIdl;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public ProductOrder() {

    }

    public ProductOrder(long orderIdl, String type) {
        this.orderIdl = orderIdl;
        this.type = type;
    }

    @Override
    public String toString() {
        return "ProductOrder{" +
                "orderIdl=" + orderIdl +
                ", type='" + type + '\'' +
                '}';
    }

    /**
     * 模拟批量创建实体类
     * @return
     */
    public static List<ProductOrder> getOrderList(){
        List<ProductOrder> list=new ArrayList<>();
        list.add(new ProductOrder(111L,"创建订单"));
        list.add(new ProductOrder(222L,"创建订单"));
        list.add(new ProductOrder(333L,"创建订单"));
        list.add(new ProductOrder(111L,"支付订单"));
        list.add(new ProductOrder(222L,"支付订单"));
        list.add(new ProductOrder(111L,"完成订单"));
        list.add(new ProductOrder(222L,"完成订单"));
        list.add(new ProductOrder(333L,"支付订单"));
        list.add(new ProductOrder(333L,"完成订单"));
        return list;
    }
}
```

控制层：PayController.java

![](./images/images/img_046_d9ce87e7c435.png)

```text
    @Autowired
    private PayProducer payProducer;

    private static final String TOPIC = "ybchen_pay_topic";
    private static final String TOPIC_ORDER = "ybchen_pay_order_topic";

    @RequestMapping("pay_order")
    public Object payOrder() throws Exception{
        //获取订单号
        List<ProductOrder> list=ProductOrder.getOrderList();
        for (int i = 0; i < list.size(); i++) {
            ProductOrder order=list.get(i);
            Message message=new Message(TOPIC_ORDER,
                    "",
                    order.getOrderIdl()+"",
                    order.toString().getBytes());
            //发送，同一个订单id进入同一个队列中
           SendResult sendResult =payProducer.getProducer().send(message, new MessageQueueSelector() {
                @Override
                public MessageQueue select(List<MessageQueue> mqs, Message message, Object arg) {
                    Long id=(Long)arg;
                    long index=id%mqs.size();
                    return mqs.get((int) index);
                }
            },order.getOrderIdl());
           //打印输出结果
            System.out.printf("发送结果=%s，sendResult=%s，orderId=%s，type=%s\n",
                    sendResult.getSendStatus(),
                    sendResult.toString(),
                    order.getOrderIdl(),
                    order.getType());

        }
        return "ok";
    }
```

### 改造消费者

![](./images/images/img_047_876f701cb39c.png)

```text
package com.ybchen.ybchenmqconsumer.jms;

import org.apache.rocketmq.client.consumer.DefaultMQPushConsumer;
import org.apache.rocketmq.client.consumer.listener.*;
import org.apache.rocketmq.client.exception.MQClientException;
import org.apache.rocketmq.common.consumer.ConsumeFromWhere;
import org.apache.rocketmq.common.message.MessageExt;
import org.apache.rocketmq.common.protocol.heartbeat.MessageModel;
import org.springframework.stereotype.Component;

import java.util.List;

/**
 * @ClassName：PayOrderConsumer
 * @Description：消费者-订单
 * @Author：chenyb
 * @Date：2020/10/18 4:13 下午
 * @Versiion：1.0
 */
@Component
public class PayOrderConsumer {
    /**
     * 生产者所属的组
     */
    private String producerGroup = "pay_order_consumer_group";
    /**
     * MQ的地址，注意需开放端口号或者关闭防火墙
     */
    private String nameServerAddr = "192.168.199.100:9876;192.168.199.101:9876";
    /**
     * 订阅主题，订单
     */
    private static final String TOPIC_ORDER = "ybchen_pay_order_topic";
    private DefaultMQPushConsumer consumer;

    public PayOrderConsumer() throws MQClientException {
        consumer = new DefaultMQPushConsumer(producerGroup);
        //指定NameServer地址，多个地址以;隔开
        //如 producer.setNamesrvAddr("192.168.199.100:9876;192.168.199.101:9876;192.168.199.102:9876")
        consumer.setNamesrvAddr(nameServerAddr);
        //设置消费地点，从最后一个开始消费
        consumer.setConsumeFromWhere(ConsumeFromWhere.CONSUME_FROM_LAST_OFFSET);
        //订阅主题，监听主题下的那些标签
        consumer.subscribe(TOPIC_ORDER, "*");
        //默认是集群方式，广播方式不支持重试
        consumer.setMessageModel(MessageModel.CLUSTERING);
        //注解一个监听器
        consumer.registerMessageListener(new MessageListenerOrderly() {
            @Override
            public ConsumeOrderlyStatus consumeMessage(List<MessageExt> list,
                                                       ConsumeOrderlyContext consumeOrderlyContext) {
                MessageExt msg=list.get(0);
                System.out.printf("%s Receive New Messages: %s %n",Thread.currentThread().getName(),
                        new String(msg.getBody()));
                return ConsumeOrderlyStatus.SUCCESS;
            }
        });
        consumer.start();
        System.out.println("consumer order start ..........");
    }
}
```

### 测试顺序消息

#### 一个生产者一个消费者

　　可以看到消费的时候，有点慢，因为我本地安装了2个虚拟机做一主一从，消费的顺序是正确的，都是按照：创建订单、支付订单、完成订单

![](./images/images/img_048_2786c7705c90.gif)

```text
2020-10-25 13:52:31.822  INFO 1473 --- [nio-8080-exec-1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2020-10-25 13:52:31.822  INFO 1473 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2020-10-25 13:52:31.825  INFO 1473 --- [nio-8080-exec-1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 3 ms
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D46F0000, offsetMsgId=C0A8C76400002A9F000000000009C8B2, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=3], queueOffset=6]，orderId=111，type=创建订单
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D4930001, offsetMsgId=C0A8C76400002A9F000000000009C9A5, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=2], queueOffset=6]，orderId=222，type=创建订单
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D4A90002, offsetMsgId=C0A8C76400002A9F000000000009CA98, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=1], queueOffset=6]，orderId=333，type=创建订单
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D4C00003, offsetMsgId=C0A8C76400002A9F000000000009CB8B, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=3], queueOffset=7]，orderId=111，type=支付订单
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D4CC0004, offsetMsgId=C0A8C76400002A9F000000000009CC7E, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=2], queueOffset=7]，orderId=222，type=支付订单
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D4D00005, offsetMsgId=C0A8C76400002A9F000000000009CD71, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=3], queueOffset=8]，orderId=111，type=完成订单
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D4D30006, offsetMsgId=C0A8C76400002A9F000000000009CE64, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=2], queueOffset=8]，orderId=222，type=完成订单
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D4DE0007, offsetMsgId=C0A8C76400002A9F000000000009CF57, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=1], queueOffset=7]，orderId=333，type=支付订单
发送结果=SEND_OK，sendResult=SendResult [sendStatus=SEND_OK, msgId=AC10680105C118B4AAC27E92D4F80008, offsetMsgId=C0A8C76400002A9F000000000009D04A, messageQueue=MessageQueue [topic=ybchen_pay_order_topic, brokerName=broker-a, queueId=1], queueOffset=8]，orderId=333，type=完成订单
```

```text
ConsumeMessageThread_1 Receive New Messages: ProductOrder{orderIdl=333, type='创建订单'}
ConsumeMessageThread_1 Receive New Messages: ProductOrder{orderIdl=333, type='支付订单'}
ConsumeMessageThread_1 Receive New Messages: ProductOrder{orderIdl=333, type='完成订单'}
ConsumeMessageThread_2 Receive New Messages: ProductOrder{orderIdl=222, type='创建订单'}
ConsumeMessageThread_2 Receive New Messages: ProductOrder{orderIdl=222, type='支付订单'}
ConsumeMessageThread_2 Receive New Messages: ProductOrder{orderIdl=222, type='完成订单'}
ConsumeMessageThread_3 Receive New Messages: ProductOrder{orderIdl=111, type='创建订单'}
ConsumeMessageThread_3 Receive New Messages: ProductOrder{orderIdl=111, type='支付订单'}
ConsumeMessageThread_3 Receive New Messages: ProductOrder{orderIdl=111, type='完成订单'}
```

#### 一个生产者3个消费者

**消费者会平均分配queue的数量，消费者数量小于等于4！！！**

　　本地在线模拟，一个生产者、3个消费者场景，看看消费的顺序，内容较长，被分割3块

![](./images/images/img_049_923bff310fb8.gif)

![](./images/images/img_050_6e9de325a729.gif)

![](./images/images/img_051_eed3bf0957b6.gif)

# 消费者核心配置

## setConsumeFromWhere

1. CONSUME_FORM_FIRST_OFFSET：初次从消息队列头部开始消费，即历史消息(还存储在broker的)全部消费一遍，后续在启动接着上次消费的进度开始消费
2. CONSUME_FROM_LAST_OFFSET：默认策略，初次从该队列尾开始消费，即跳过历史小心，后续在启动接着上次消费的进度开始消费
3. CCONSUME_FROM_TIMESTAMP：从某个时间点开始消费，默认是半小时以前，后续在启动接着上次消费的进度开始消费

## setAllocateMessageQueueStrategy

- 负载均衡策略算法，即消费者分配到queue的算法，默认值AllocateMessageQueueAveragely即取模平均分配

## setOffsetStore

- 消息消费进度存储器，2个策略

  - LocalFileOffsetStore(广播模式默认使用)
  - RemoteBrokerOffsetStore(集群模式默认使用)

## setConsumeThreadMin

- 最小消费线程池数量

## setConsumeThreadMax

- 最大消费线程池数量

## setPullBatchSize

- 消费者去broker拉取消息时，一次次拉取多少条

## setConsumeMessageBatchMaxSize

- 单次消费时一次性消费多少条消息

## setMessageModel

- 消费者消费模式

  - CLUSTERING：默认是集群模式
  - BROADCASTING：广播模式

## Topic下队列的奇偶数会影响Customer个数里面的消费数量

- 如果是4个队列(默认队列为4)，8个消息，4个节点则各会消费2条，如果不对等，则负载均衡会分配不均匀
- 如果consumer实例数量比message queue的总数量还多的话，多出来的consumer实例将无法分到queue，也就无法消费达到消息，也就无法起到分摊负载的作用，所以需要控制让queue的总数量大于consumer的数量

## 集群模式(默认)

- Consumer实例平均分摊消费生产者发送的消息
- 例如：订单消息，只能被消费一次

## 广播模式

- 广播模式下消费消息，投递到Broker的消息会被每个Consumer进行消费，一条消息被多个Consumer消费，广播消费中ConsumerGroup暂时无用
- 例如：QQ群，群主发一条消息，所有人都可以看到

# 消息存储

## ConsumeQueue

　　逻辑队列，默认存储位置：/root/store/consumequeue

## CommitLog

　　真正存储消息文件的，默认存储位置：/root/store/commitlog

# 常见面试题

## 为什么消息队列？

### 优点

1. 异步：例如秒杀，可以使用，[点我直达](https://www.cnblogs.com/chenyanbin/p/13587508.html)
2. 解耦
3. 削峰：秒杀情况下，一个个入队，一个个出队，有序进行

### 缺点

1. 系统可用性越低：外部依赖越多，依赖越多，出问题风险越大
2. 系统复杂性提高：需要考虑多种场景，比如消息重复消费、消息丢失
3. 需要更多的机器和人力：消息队列一般集群部署，需要运维和监控

## 如何避免重复消费？

　　RocketMQ不保证消息不重复，如果业务保证严格的不能重复消费，需要自己去业务端去重

### 数据库表去重

　　指定某个字段唯一值

![](./images/images/img_052_291438cbd096.gif)

### setNX

　　利用Redis的特性分布式锁，下面是我之前的代码，待改造

```text
package com.cyb.redis.utils;

import redis.clients.jedis.Jedis;
import redis.clients.jedis.JedisPool;

public class jedisUtils {
    private static String ip = "192.168.31.200";
    private static int port = 6379;
    private static JedisPool pool;
    static {
        pool = new JedisPool(ip, port);
    }
    public static Jedis getJedis() {
        return pool.getResource();
    }
    public static boolean getLock(String lockKey, String requestId, int timeout) {
        //获取jedis对象，负责和远程redis服务器进行连接
        Jedis je=getJedis();
        //参数3：NX和XX
        //参数4：EX和PX
        String result = je.set(lockKey, requestId, "NX", "EX", timeout);
        if (result=="ok") {
            return true;
        }
        return false;
    }

    public static synchronized boolean getLock2(String lockKey, String requestId, int timeout) {
        //获取jedis对象，负责和远程redis服务器进行连接
        Jedis je=getJedis();
        //参数3：NX和XX
        //参数4：EX和PX
        Long result = je.setnx(lockKey, requestId);
        if (result==1) {
            je.expire(lockKey, timeout); //设置有效期
            return true;
        }
        return false;
    }
}
```

### Redis原子递增

　　利用Redis的incr特性，如果大于0说明消费过了(**需要设置过期时间**)

## 如何保证消息的可靠性传输？

### producer端

1. 不采用oneway发送，使用同步或者一部方式发送，做好重试，但是重试的Message key必须唯一
2. 投递的日志需要保存，关键字段、投递时间、投递状态、重试次数、请求体、响应体等

### broker端

1. 双主双从架构，NameServer需要多节点
2. 同步双写，异步刷盘

### consumer端

1. 消息消费保存日志文件中

## 大量堆积到broker里面，如何处理？

1. 临时topic队列扩容，提高消费者能力
2. 编写临时处理分发程序，从旧topic快速读取到临时新topic中，新topic的queue数量扩容多倍，然后再启动更多consumer进行临时新的topic消费

## RocketMQ高性能的原因？

### MQ架构配置

1. 顺序写
2. 随机读
3. 零拷贝

### 发送端高可用

1. 双主双从架构：创建Topic的时候，MessageQueue创建在多个Broker上，即相同的Broker名称，不同brokerid；当一个Master不可用时，组内其他的Master仍然可用

### 消费高可用

1. 主从架构：Broker角色，Master提供读写，Slave只支持读
2. Consumer不用配置，当Master不可用或者繁忙的时候，Consumer会自动切换到Slave节点进行读取

### 提升消息的消费能力

1. 增加多个消费者
2. 修改消费者的线程池最小/大数量

# 项目源码

## 案例源码

```text
链接: https://pan.baidu.com/s/1Q8iL0lH-bdFEycYGq61hQg  密码: rww2
```

## Linux下RocketMQ安装包

```text
链接: https://pan.baidu.com/s/1dkE7sAs9E4TjwDQ38Pv4_A  密码: mkjm
```

# 双主双从集群搭建

[点我直达](https://www.cnblogs.com/chenyanbin/p/13894216.html)
