{

  "title": "ActiveMQ  事务、集群、持久订阅者、ActiveMQ监控",
  "date": "2020-05-11",
  "description": "JMS介绍 JMS是什么? JMS的全称**Java Message Service**，既Java消息服务。 JMS是SUN提供的旨在统一各种MOM(Message-Oriented Middleware)系统接口的规范，它包含**点对点(Point to Point,PTP)**和**发布/订阅",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12841966.html"

}

# JMS介绍

## JMS是什么?

　　JMS的全称**Java Message Service**，既Java消息服务。

　　JMS是SUN提供的旨在统一各种MOM(Message-Oriented Middleware)系统接口的规范，它包含**点对点(Point to Point,PTP)**和**发布/订阅(Publish/Subscribe，pub/sub)**两种消息模型，提供可靠**消息传输、事务和消息过滤**等机制。

　　ActiveMQ是Apache出品的开源项目，他是JMS规范的一个实现。

## MOM是什么？

**MOM(Message-Oriented Middleware)**：**面向消息的中间件**，使用**消息中间件**来协调消息传输操作。

MOM需要提供API和管理工具

- **客户端**调用API，把消息发送到**消息中间件**指定的目的地。在消息发送之后，客户端会继续执行其他的工作。
- **接收方**收到这个消息确认之前，**消息中间件**一直保留该消息。

## JMS的作用是什么？

　　在不同应用之间进行通信或者从一个系统传输数据到另外一个系统。两个应用程序之间，或分布式系统中发送消息，进行**异步通信，程序或应用之间解耦**。

　　它主要用于在生产者和消费者之间进行消息传递，生产者负责产生消息，而消费者负责接收消息。把它应用到实际的业务需求中的话我们可以在特定的时候利用生产者生成-消息，并进行发送，对应的消费者在接收到对应的消息后去完成对应的业务逻辑。

## JMS的应用场景

主要可以应用于规模和复杂度较高的分布式系统：

- **异步通信**：客户发出调用后，不用等待服务对象完成处理并返回结果后就能继续执行；
- **客户和服务对象的生命周期解耦合**：客户进行和服务对象进行不需要都正常运行；如果由于服务对象崩溃或网络故障导致客户的请求不可达，不会影响客户端正常响应；
- **一对一或一对多通信**：客户的一次调用可以发送给一个或多个目标对象；

## JMS中的角色

三种角色：**生产者(Java应用程序)、消费者(Java应用程序)、消息中间件(MQ)**

## JMS消息模型

### 点对点模型(基于队列)

- 消息的生产者和消费者之间没有时间上的相关性。
- 生产者把消息发送到队列中(**Queue**)，可以有多个发送者，但只能被一个消费者消费。一个消息只能被一个消费者消费一次。
- 消费者无需订阅，当消费者未消费到消息时就会处于阻塞状态

### 发布者/订阅者模型(基于主题的)

- 生产者和消费者之间有时间上的相关性，订阅一个主题的消费者只能消费自它订阅之后发布的消息
- 生产者将消息发送到主题上(**Topic**)
- 消费者必须先订阅，JMS规范允许提供客户端创建持久订阅

## JMS消息组成

### 消息头

### 消息正文

　　JMS定义了五种不同的消息正文格式，以及调用的消息类型，允许你发送并接收一些不同形式的数据，提供现有消息格式的一些级别的兼容性。

- StreamMessage --Java原始值得数据流
- MapMessage --一套名称-值对
- TextMessage --一个字符串对象
- ObjectMessage --一个序列化的Java对象
- BytesMessage --一个字节的数据流

### 消息属性

## 总结

1、JMS是什么？是指定消息发送和接收的一套标准

2、JMS的角色：生产者、消费者、MOM消息中间件

3、JMS消息模型：点对点、发布订阅模型

4、JMS消息正文：Stream、Map、Text、Byte、Object

# ActiveMQ介绍

## 什么是ActiveMQ

　　MQ，既Message Queue，就是消息队列的意思。

　　ActiveMQ是Apache出品，最流行，能力强劲的开源消息总线。ActiveMQ是一个完全支持JMS1.1和J2EE 1.4规范的JMS Provider实现，尽管JMS规范出台已经是很久的事情了，但是JMS在当今的J2EE应用中间仍然扮演着特殊地位。

## ActiveMQ主要特点

1. 多种语言和协议编写客户端，语言：[C](https://baike.baidu.com/item/C)、[C++](https://baike.baidu.com/item/C%2B%2B)、[C#](https://baike.baidu.com/item/C%23)、[Delphi](https://baike.baidu.com/item/Delphi)、[Erlang](https://baike.baidu.com/item/Erlang)、[Adobe Flash](https://baike.baidu.com/item/Adobe%20Flash)、[Haskell](https://baike.baidu.com/item/Haskell)、[Java](https://baike.baidu.com/item/Java)、[JavaScript](https://baike.baidu.com/item/JavaScript)、[Perl](https://baike.baidu.com/item/Perl)、[PHP](https://baike.baidu.com/item/PHP)、[Pike](https://baike.baidu.com/item/Pike)、[Python](https://baike.baidu.com/item/Python)和[Ruby](https://baike.baidu.com/item/Ruby)
2. 支持[Java消息服务](https://baike.baidu.com/item/Java%E6%B6%88%E6%81%AF%E6%9C%8D%E5%8A%A1)(JMS) 1.1 版本
3. 对Srping的支持，ActiveMQ可以很容易内嵌到使用Spring的系统里面去，而且也支持Spring2.0的特性
4. 协议支持包括：OpenWire、[REST](https://baike.baidu.com/item/REST)、STOMP、WS-Notification、MQTT、[XMPP](https://baike.baidu.com/item/XMPP)以及AMQP
5. 集群

## ActiveMQ下载安装

### 下载

```text
http://activemq.apache.org/components/classic/download/
```

下载版本(**我使用的版本最新**)：5.15.12

![](./images/images/img_001_0aa50578fc70.png)

### 安装jdk(必须要安装)

1、先卸载系统自带的jdk

```text
1、查看安装的jdk
rpm -qa | grep java

2、卸载系统自带jdk
rpm -e --nodeps 包名
```

2、安装JDK，ActiveMQ是使用Java开发的

```text
　　当前最新版本下载地址：http://www.oracle.com/technetwork/java/javase/downloads/index.html

　　历史版本下载地址：　　http://www.oracle.com/technetwork/java/javase/archive-139210.html
```

我下载的是1.8，[点我直达](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)[
](https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html)

```text
链接: https://pan.baidu.com/s/1DZGsJuLUrhpEQm7jaSKTwg  密码: baa5
```

3、解压到指定位置

```text
tar -zxvf jdk-8u202-linux-x64.tar.gz
```

4、修改/etc/profile文件

在最下面添加两行代码

```text
 export JAVA_HOME=/cyb/soft/jdk1.8.0_202
 export PATH=$JAVA_HOME/bin:$PATH
```

5、执行source操作

```text
source /etc/profile
```

6、检查是否安装成功

```text
java -version
```

### 安装ActiveMQ

1、解压缩

```text
tar -zxvf apache-activemq-5.15.12-bin.tar.gz
```

2、启动ActiveMQ

```text
cd apache-activemq-5.15.12/bin/

./activemq start
```

3、访问ActiveMQ后台

```text
地址：http://192.168.191.132:8161/admin/
账户：admin
密码：admin
```

4、访问测试

![](./images/images/img_002_dc47320f7938.png)

**注：为什么端口是8161，因为ActiveMQ用的内嵌web服务器jetty，端口可以修改，配置文件在/conf/jetty.xml**

### 补充

**ActiveMQ与jdk是有版本对应关系的！！！！！**

# ActiveMQ使用

## 创建Demo工程

- 消息生产者：activemq-producer-demo工程(jar)
- 消息消费者：activemq-consumer-demo工程(jar)

## 添加Maven依赖

　　生产者和消费者都要加入以下依赖

```text
    <dependencies>
        <!--activemq依赖-->
        <dependency>
            <groupId>org.apache.activemq</groupId>
            <artifactId>activemq-all</artifactId>
            <version>5.15.12</version>
        </dependency>
        <!--junit依赖-->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
        </plugins>
    </build>
```

## 点对点模式演示

### 提供者(activemq-producer-demo)

```text
package com.cyb.activemq.producer;

import org.apache.activemq.ActiveMQConnection;
import org.apache.activemq.ActiveMQConnectionFactory;
import org.apache.activemq.command.ActiveMQTextMessage;
import org.junit.Test;

import javax.jms.*;

public class Producer {
    @Test
    public void testQueueProducer() throws Exception {
        Connection connection = null;
        MessageProducer producer = null;
        Session session = null;
        try {
            //第一步：创建ConnectionFactory，用于连接broker
            String brokerURL = "tcp://192.168.1.106:61616";
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
            //设置消息发送为同步发送
            ((ActiveMQConnectionFactory) connectionFactory).setUseAsyncSend(true);
            //设置
            ((ActiveMQConnectionFactory) connectionFactory).setProducerWindowSize(1000);
            //第二步：通过工厂，创建Connection
            connection = connectionFactory.createConnection();
            ((ActiveMQConnection) connection).setUseAsyncSend(true);
            //第三步：连接启动
            connection.start();
            //第四步：通过连接获取session会话
            //第一个参数：是否启用ActiveMQ事务，如果为true，第二个参数无用
            //第二个参数：应答模式，AUTO_ACKNOWLEDGE为自动应答
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            //第五步：通过session创建destination，两种目的地：Queue、Topic
            //参数：消息队列的名称，在后台管理系统中可以看到
            Queue queue = session.createQueue("cyb-queue");
            //第六步：通过session创建MessageProducer
            producer = session.createProducer(queue);
            producer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
            //第七步：创建Message
            //方式一
            //TextMessage message=new ActiveMQTextMessage();
            //message.setText("queue test");
            //方式二
            TextMessage message1 = session.createTextMessage("博客园地址:https://www.cnblogs.com/chenyanbin/");
            //第八步：通过producer发送消息
            producer.send(message1);
            //session.commit();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            //第九步：关闭资源
            producer.close();
            session.close();
            connection.close();
        }
    }
}
```

### 消费者(activemq-consumer-demo)

```text
package com.cyb.activemq.consumer;

import org.apache.activemq.ActiveMQConnectionFactory;
import org.junit.Test;

import javax.jms.*;

public class Consumer {
    @Test
    public void testQueueConsumer() throws Exception{
        //第一步：创建ConnectionFactory
        String brokerURL="tcp://192.168.1.106:61616";
        ConnectionFactory connectionFactory=new ActiveMQConnectionFactory(brokerURL);
        //第二步：通过工厂，创建Connection
        Connection connection=connectionFactory.createConnection();
        //第三步：打开链接
        connection.start();
        //第四步：通过Connection创建session
        Session session=connection.createSession(Boolean.FALSE, Session.AUTO_ACKNOWLEDGE);
        //第五步：通过session创建Consumer
        Queue queue=session.createQueue("cyb-queue");
        MessageConsumer consumer=session.createConsumer(queue);
        //第六步：通过consumer接收信息(两种方式：1、receive方法接收(同步)；2、通过监听器接收(异步))
        //方式1、receive方法接收信息
        Message message=consumer.receive(100000);
        //第七步：处理信息
        if (message!=null&&message instanceof TextMessage){
            TextMessage tm=(TextMessage)message;
            System.out.println(tm.getText());
        }

        //方式2：监听器接收信息
//        consumer.setMessageListener(new MessageListener() {
//            @Override
//            public void onMessage(Message message) {
//                //第七步：处理信息
//                if (message instanceof TextMessage){
//                    TextMessage tm=(TextMessage)message;
//                    try{
//                        System.out.println(tm.getText());
//                    }
//                    catch (Exception e){
//                        e.printStackTrace();
//                    }
//                }
//            }
//        });
        //session.commit();
        //第八步：关闭资源
        consumer.close();
        session.close();
        connection.close();
    }

}
```

### 测试

![](./images/images/img_003_c65df78e48a1.gif)

## 发布订阅模式演示

### 提供者(activemq-producer-demo)

```text
    @Test
    public void testTopicProducer() throws Exception {
        Connection connection = null;
        MessageProducer producer = null;
        Session session = null;
        try {
            //第一步：创建ConnectionFactory，用于连接broker
            String brokerURL = "tcp://192.168.1.106:61616";
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
            //设置消息发送为同步发送
            ((ActiveMQConnectionFactory) connectionFactory).setUseAsyncSend(true);
            //设置
            ((ActiveMQConnectionFactory) connectionFactory).setProducerWindowSize(1000);
            //第二步：通过工厂，创建Connection
            connection = connectionFactory.createConnection();
            ((ActiveMQConnection) connection).setUseAsyncSend(true);
            //第三步：连接启动
            connection.start();
            //第四步：通过连接获取session会话
            //第一个参数：是否启用ActiveMQ事务，如果为true，第二个参数无用
            //第二个参数：应答模式，AUTO_ACKNOWLEDGE为自动应答
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            //第五步：通过session创建destination，两种目的地：Queue、Topic
            //参数：消息队列的名称，在后台管理系统中可以看到
            Topic topic=session.createTopic("cyb-topic");
            //第六步：通过session创建MessageProducer
            producer = session.createProducer(topic);
            producer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
            //第七步：创建Message
            //方式一
            //TextMessage message=new ActiveMQTextMessage();
            //message.setText("queue test");
            //方式二
            TextMessage message1 = session.createTextMessage("topic->博客园地址:https://www.cnblogs.com/chenyanbin/");
            //第八步：通过producer发送消息
            producer.send(message1);
            //session.commit();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            //第九步：关闭资源
            producer.close();
            session.close();
            connection.close();
        }
    }
```

### 消费者(activemq-consumer-demo)

```text
    @Test
    public void testTopicProducer() throws Exception {
        Connection connection = null;
        MessageProducer producer = null;
        Session session = null;
        try {
            //第一步：创建ConnectionFactory，用于连接broker
            String brokerURL = "tcp://192.168.1.106:61616";
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
            //设置消息发送为同步发送
            ((ActiveMQConnectionFactory) connectionFactory).setUseAsyncSend(true);
            //设置
            ((ActiveMQConnectionFactory) connectionFactory).setProducerWindowSize(1000);
            //第二步：通过工厂，创建Connection
            connection = connectionFactory.createConnection();
            ((ActiveMQConnection) connection).setUseAsyncSend(true);
            //第三步：连接启动
            connection.start();
            //第四步：通过连接获取session会话
            //第一个参数：是否启用ActiveMQ事务，如果为true，第二个参数无用
            //第二个参数：应答模式，AUTO_ACKNOWLEDGE为自动应答
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            //第五步：通过session创建destination，两种目的地：Queue、Topic
            //参数：消息队列的名称，在后台管理系统中可以看到
            Topic topic=session.createTopic("cyb-topic");
            //第六步：通过session创建MessageProducer
            producer = session.createProducer(topic);
            producer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
            //第七步：创建Message
            //方式一
            //TextMessage message=new ActiveMQTextMessage();
            //message.setText("queue test");
            //方式二
            TextMessage message1 = session.createTextMessage("topic->博客园地址:https://www.cnblogs.com/chenyanbin/");
            //第八步：通过producer发送消息
            producer.send(message1);
            //session.commit();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            //第九步：关闭资源
            producer.close();
            session.close();
            connection.close();
        }
    }
```

### 测试

　　先启动消费者，在启动提供者

![](./images/images/img_004_09018b673d73.gif)

## 自定义BrokerServer

```text
package com.cyb.activemq;

import org.apache.activemq.broker.BrokerService;

public class MyBrokerServer {
    public static void main(String[] args) {
        BrokerService brokerService=new BrokerService();
        String bindAddress="tcp://localhost:61616";
        try
        {
            brokerService.setUseJmx(true);
            brokerService.addConnector(bindAddress);
            brokerService.start();
        }
        catch (Exception e){
            e.printStackTrace();
        }
    }
}
```

# JMS事务

## 创建事务

创建事务的方法：createSession(paramA,paramB);

- paramA是设置事务的，paramB设置acknowledgment mode(应答模式)
- paramA设置为**true**时，paramB的值忽略，acknowledgment mode被jms服务器设置Session.SESSION_TRANSACTED。
- paramA设置为**false**时，paramB的值可为Session.AUTO_ACKNOWLEDGE，Session.CLTENT_ACKNOWLEDGE，Session.DUPS_OK_ACKNOWLEDGE其中一个。

## 事务的应答模式

- JMS消息被应答确认后，才会认为是被成功消费，broker才会将消息清除掉
- 消息的消费包含三个阶段：客户端接收消息、客户端处理消息、消息被确认

### SESSION_TRANSACTED(开启事务，默认)：

　　当一个事务被commit的时候，消息确认就会自动发生。如果开启了事务，最后没有执行commit方法，那么消费者会**重复消费该消息**。

### AUTO_ACKNOWLEDGE：

　　自动确认，当客户成功的从receive方法返回的时候，或者从MessageListener.onMessage方法成功返回的时候，会话自动确认客户收到的消息。

### CLIENT_ACKNOWLEDGE(针对消费者)：

　　客户端确认。客户端接收到消息后，必须调用 javax.jmx.Message的acknowledge方法，broker才会删除消息。(默认是批量确认)

```text
Message.acknowledge();
```

### DUPS_OK_ACKNOWLEDGE：

　　允许副本的确认模式。一旦接收方应用程序的方法调用从处理消息处返回，会话对象就会确认消息的接收，而且允许重复确认。如果是重复的消息，那么JMS provider必须将消息头的JMSRedelivered字段设置为true。

![](./images/images/img_005_390cefff5d68.png)

## 事务的作用

　　在一个JMS客户端，可以使用本地事务来组合消息的发送和接收，JMS Session接口提供了commit和rollback方法。

　　开启事务之后，JMS Provider会缓存每个生产者当前生产的所有消息，直到commit或rollback。在事务未提交之前，消息时不会被持久化存储的，也不会被消费者消费。

- **commit**：操作将会导致生产者事务中所有的消息被持久存储，消费者的所有消息都被确认。
- **rollback**：操作将会导致生产者事务中所有的消息被清除，消费者的所有消息不被确认。

# 消息生产者处理

## 消息的持久化和非持久化

　　ActiveMQ支持两种传输模式：**持久传输和非持久传输，默认情况下使用的是持久传输**。

### 两者差异

- 采用**持久传输**时，**传输的消息会保存到磁盘**中，既“存储转发”模式，先把消息存储到磁盘中，然后再将消息“转发”给订阅者。**当Borker宕机恢复后，消息还在**。
- 采用**非持久传输**时，发送的**消息不会存储到磁盘**中。**当Borker宕机重启后，消息丢失**。

### 通过MessageProducer类的setDeliveryMode设置传输模式

```text
producer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
```

## 消息同步发送和异步发送

producer **发送消息有同步和异步两种模式**，可以通过以下方式设置

1、设置ConnectionFactory时指定使用异步

```text
ConnectionFactory connectionFactory = new ActiveMQConnectionFactory("tcp://192.168.1.109:61616?jms.useAsyncSend=true");
```

2、不在构造函数中指定，而是修改ConnectionFactory配置

```text
            //第一步：创建ConnectionFactory，用于连接broker
            String brokerURL = "tcp://192.168.1.109:61616";
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
            //设置消息发送为异步发送
            ((ActiveMQConnectionFactory) connectionFactory).setUseAsyncSend(true);
```

3、在实例化后的ActiveMQConnection对象中设置异步发送

```text
String brokerURL = "tcp://192.168.1.109:61616";
ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
Connection connection = connectionFactory.createConnection();
((ActiveMQConnection) connection).setUseAsyncSend(true);
```

在不考虑事务的情况下：

- producer发送持久化消息是同步发送，发送是阻塞的，直到收到确认。
- producer发送非持久化消息时异步发送，异步发送不会等待broker的确认，不阻塞。

　　消息生产者使用持久传递模式发送消息的时候，producer.send(message)方法会被阻塞，直到broker发送一个确认消息给生产者，这个确认消息暗示broker已经成功接收消息并把消息保存到二级存储中。这个过程通常称为同步发送。

　　如果应用程序能容忍一些消息的丢失，那么可以使用异步发送。异步发送不会受到broker的确认之前一直阻塞Producer.send方法。

## 生产者流量控制

### ProducerWindowSize

　　在ActiveMQ5.0版本中，我们可以分别一个共享连接上的各个生产者进行流量控制，而不需要挂起整个连接。“**流量控制”意味着当代理(broker)检测目标(destination)的内存，或临时文件空间或文件存储空间超过了限制，消息的流量可以被减慢**。生产者将会被阻塞直至资源可用，或者受到一个JMSException异常

- **同步发送的消息将会自动对每一个生产者使用流量控制**；除非你使用了 useAsynSend标志，否则这将对同步发送的持久性消息都适用。
- 适用**异步发送**的生产者不需要等待来自代理的任何确认消息；所以，如果**内存限制被超过了，你不会被通知**。如果你真的想知道什么时候代理的限制被超过了，你需要配置ProducerWindowSize这一连接选项，这样就算是异步消息也会对每一个生产者进行流量控制。

3种方式设置ProducerWindowSize

方式一、

```text
            String brokerURL = "tcp://192.168.1.109:61616";
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
            ((ActiveMQConnectionFactory) connectionFactory).setProducerWindowSize(1000);
```

方式二、

　　在**brokerURL**中设置:"tcp://192.168.1.109:61616?jms.produceWindowSize=1000"，这种设置将会对所有的produce生效。

方式三、

　　在**destinationUrl**中设置"cyb-queue?producer.windowSize=1000"，此参数只会对使用此Destination实例的producer生效，将**会覆盖brokerUrl中的producerWindowSize值**

![](./images/images/img_006_4afc0e57947a.png)

配置说明：

　　ProducerWindowSize是一个生产者在等到确认消息之前，可以发送给代理的数据最大byte，这个确认消息用来告诉生产者，代理已经收到之前发送的消息了。

　　它主要用来约束在异步发送时producer端允许异步发送的(尚未ACK)的消息尺寸，且**只对异步发送有意义**。

**值越大，意味着消耗Broker服务器的内存就越大**。

### alwaysSyncSend

　　如果你要发送非持久化的消息(消息默认是异步发送的)，并且想要每次都得到队列或者主题的内存限制是否达到，你只需将连接工厂配置为“alwaysSyncSend”，虽然这样会变得稍微慢一点，但是这将保证当出现内存问题时，你的消息生产者能够及时得到通知。

```text
((ActiveMQConnection) connection).setAlwaysSyncSend(true);
```

## 如何提升消息发送效率？(背)

- 在某些场景下，我们的Producer的个数非常有限的，可能只有几个，比如基于Queue的“订单接入网管”(生成订单原始信息并负责传递)，但是响应的Consumer的个数相对较多，在整体上Producer效能小于Consumer。
- 还有一些场景，Producer的数量非常多，消息量也很大，但是Consumer的个数或者效能相对较低，比如“用户点击流”、“用户消息Push系统”等

### 消息持久化

1、持久化类型的消息，对broker端性能消耗远远大于非持久化类型

2、这归结于ActiveMQ本身对持久化消息确保“最终一致性”，持久化意味着“消息不丢失”，即当broker接收到消息后需要一次强制性磁盘同步

3、对于Consumer在消费消息后，也会触发磁盘写入

4、通常broker端还会开启相关的“过期消息检测”线程，将存储器中的数据载入内存并检测，这个过程也是内存，磁盘IO消耗的。由此可见，持久化类型的消息从始至终，都在“拖累”系统的性能和吞吐能力。

### 消息属性

1、通过Producer发送消息(Message)中，除了消息本身的负荷体之外(Consumer)，还有大量的JMS属性和Properties可以设置，因为JMS中，支持对JMS属性和properties使用selector，那么这些内容将会加大和复杂化message header，我们尽可能的在properties中携带更少

### 异步发送

1、如果消息是非持久性的，或者Session是基于事务的，建议开发者不要关闭异步发送；这是提升Producer发送效率的重要的策略。

2、设置合适的windowSize，开启Broker端“Flow Control”等

### 事务

对于Producer而言，使用事务并不会消耗Broker太多的性能,主要会占用内存，所有未提交的事务消息，都会保存在内存中，有些基于日志的存储器，事务类型的持久化消息暂存在额外的文件中，直到日志提交或回滚后清除。所以，Producer端不要在事务中，积压太多的消息，尽可能早的提交事务。

### 提升Consumer消费速率

无论是Queue还是Topic，快速的Consumer，无疑是提升整体效能的最好手段。

### 选择合适的存储器

　　activeMQ目前支持JDBC、kahadb、LevelDB三种存储器。

　　JDBC主要面向基于RDBMS方向，通常如果消息不仅面向ActiveMQ，还可能被用于第三方平台的操作，JDBC的特点就是透明度高，可扩展方案较多(扩展成本高)。

　　kahadb和LevelDB，同属于日志存储+BTree索引，性能很高，对于消息较多(单位尺寸较小)，消费速度较快的应用，是最好的选择，这两种存储器也最常用，推荐LevelDB

# Broker Server处理

## 导读

**　　以下内容都是修改：vim /cyb/soft/apache-activemq-5.15.12/conf/activemq.xml**

## 流量控制

### 设置指定队列和主题失效

　　可以通过在代理配置中，将适当的目的地(destination)的策略(policy)中的producerFlowControl标志设置为false，使代理商特定的JMS队列和主题不适用流量控制

```text
<destinationPolicy>
  <policyMap>
    <policyEntries>
      <policyEntry topic="FOO.>" producerFlowControl="false"/>
    </policyEntries>
  </policyMap>
</destinationPolicy>
```

### 生存内存限制

　　注意，在ActiveMQ 5.x中引入了新的file cursor，非持久化消息会被刷到临时文件存储中来减少内存使用量。所以，你会发现queue的memoryLimit永远达不到，因为file cursor花不了多少内存，如果你真的要把所有非持久化消息保存在内存中，并且当memoryLimit达到时停止producer，你应该配置<vmQueueCursor>。

```text
<policyEntry queue=">" producerFlowControl="true" memoryLimit="1mb">
    <pendingQueuePolicy>
        <vmQueueCursor/>
    </pendingQueuePolicy>
</policyEntry>
```

上面的片段能保证，所有的消息保存在内存中，并且每一个队列只有1Mb的限制。

## 配置生产者客户端的异常

　　应对Broker代理空间不足，而导致不确定的阻塞send()操作的一种替代方案，就是将其配置成客户端抛出一个异常。通过将sendFailIfNoSpace属性设置为true，代理将会引起send()方法失败，并抛出javax.jmx.ResourceAllocationException异常，传播到客户端

```text
<systemUsage>
 <systemUsage sendFailIfNoSpace="true">
   <memoryUsage>
     <memoryUsage limit="20 mb"/>
   </memoryUsage>
 </systemUsage>
</systemUsage>
```

这个属性的好处是，客户端可以捕获javax.jms.ResourceAllocationException异常，稍等一下，并重试send()操作，而不是无限期地傻等下去。

 从5.3.1版本之后，sendFailIfNoSpaceAfterTimeout 属性被加了进来。这个属性同样导致send()方法失败，并在客户端抛出异常，但仅当等待了指定时间之后才触发。如果在配置的等待时间过去之后，代理上的空间仍然没有被释放，仅当这个时候send()方法才会失败，并且在客户端抛出异常。下面是一个示例：

```text
<systemUsage>
 <systemUsage sendFailIfNoSpaceAfterTimeout="3000">
   <memoryUsage>
     <memoryUsage limit="20 mb"/>
   </memoryUsage>
 </systemUsage>
</systemUsage>
```

定义超时的单位是毫秒，所以上面的例子将会在使send()方法失败并对客户端抛出异常之前，等待三秒。这个属性的优点是，它仅仅阻塞配置指定的时间，而不是立即另发送失败，或者无限期阻塞。这个属性不仅在代理端提供了一个改进，还对客户端提供了一个改进，使得客户端能捕获异常，等待一下并重试send()操作。

## 使用流量控制无效

　　一个普通的需求是使流量控制无效，使得消息分布能够持续，直到所有可用的磁盘被挂起的消息耗尽。要这样做，你可以使用消息游标。

### ActiveMQ的消息游标分为三种类型

- Store-based
- VM
- File-based

## 系统占用(重要)

你还可以通过<systemUsage>元素的一些属性来减慢生产者。来看一眼下面的例子：

```text
<systemUsage>
  <systemUsage>
    <memoryUsage>
      <memoryUsage limit="64 mb" />
    </memoryUsage>
    <storeUsage>
      <storeUsage limit="100 gb" />
    </storeUsage>
    <tempUsage>
      <tempUsage limit="10 gb" />
    </tempUsage>
  </systemUsage>
</systemUsage>
```

你可以为非持久化的消息（NON_PERSISTENT messages）设置内存限制，为持久化消息（PERSISTENT messages）设置磁盘空间，以及为临时消息设置总的空间，代理将在减慢生产者之前使用这些空间。使用上述的默认设置，代理将会一直阻塞sen()方法的调用，直至一些消息被消费，并且代理有了可用空间。默认值如上例所述，你可能需要根据你的环境增加这些值。

## 解决消费缓慢及无法消费的问题(重要)

　　其中broker中还以单独设置生产者使用的 producerSystemUsage和消费者使用 consumerSystemUsage，格式跟systemUsage一样。

　　默认情况下，没有配置 producerSystemUsage 和consumerSystemUsage，则生产者和消费者都使用 systemUsage。

### 问题：

　　可能会因为生产者线程把内存用完，导致消费者线程处理缓慢甚至无法消费的问题。这种情况下，添加消费端的机器和消费者数量可能都无法增加消费的速度。

### 解决办法：

　　在broker上设置 **splitSystemUsageForProducersConsumers="true"**，使得生产者线程和消费者线程各使用各的内存。

　　默认是 **生产者线程内存：消费者线程内存 => 6：4**

　　也可以通过如下两个参数设置生产者线程内存和消费者内存各一半：

```text
producerSystemUsagePortion = "50"
consumerSystemUsagePortion = "50"
```

```text
<broker xmlns="http://activemq.apache.org/schema/core" brokerName="localhost" dataDirectory="${activemq.data}" splitSystemUsageForProducersConsumers="true" producerSystemUsagePortion = "50" consumerSystemUsagePortion = "50">
```

## 消息定时删除(重要)

```text
<broker xmlns="http://activemq.apache.org/schema/core" schedulePeriodForDestinationPurge="10000">
    <destinationPolicy>
       <policyMap>
          <policyEntries>
             <policyEntry topic=">" gcInactiveDestinations="true" inactiveTimoutBeforeGC="30000"/>
          </policyEntries>
       </policyMap>
    </destinationPolicy>
  </broker>
```

实现定时自动清除无效的Topic和Queue需要设置三个属性

- **schedulePeriodForDestinationPurge**：执行清理任务的周期，单位是毫秒
- **gclnactiveDestinations="true"**：启动清理功能
- **inactiveTiomoutBeforeGC="3000"**：Topic或Queue超时时间，在规定的时间内，无有效订阅，没有入队记录，超时就会被清理。

## 持久化存储方式

### KahaDB基于文件的存储(默认)

　　KahaDB是从ActiveMQ 5.4开始 默认的持久化插件，也是我们项目现在使用的持久化方式。KahaDB恢复时间远远小于其前身AMQ并且使用更少的数据文件，所以可以完全替代AMQ。KahaDB的持久化机制同样是基于日志文件，索引和缓存。

```text
        <persistenceAdapter>
            <kahaDB directory="${activemq.data}/kahadb" journalMaxFileLength="16mb"/>
        </persistenceAdapter>
```

　　directory：指定持久化消息的存储目录

　　journalMaxFileLength：指定保存消息的日志文件大小，具体根据你的实际应用配置

### KahaDB主要特性

1. 日志形式存储消息
2. 消息索引以B-Tree结构存储，可以快速更新；
3. 完全支持JMS事务
4. 支持多种恢复机制

### AMQ 基于文件的存储

　　性能高于JDBC，写入消息时，会将消息写入日志文件，由于很高。为了提升性能，创建消息主键索引，并且提供缓存机制，进一步提升性能。每个日志文件的大小都是有限制的(默认32m，可配置)。

　　当超过这个大小，系统会重新建立一个文件。当所有的消息都消费完成，系统会删除这个文件或者归档

**主要的缺点是：**

- AMQ Message会为每一个Destination创建一个索引，如果使用了大量的Queue，索引文件的大小会占用很多磁盘空间
- 由于索引巨大，一旦Broker崩溃，重建索引的速度会非常慢

```text
        <persistenceAdapter>
               <amqPersistenceAdapter directory="${activemq.data}/activemq-data" maxFileLength="32mb"/>
        </persistenceAdapter>
```

###  JDBC基于数据库的存储

1、首先将以下驱动放到lib目录下，驱动包和ActiveMQ我已上传至百度云，下面有连接供下载

![](./images/images/img_007_cb6ac9d0b79f.png)

![](./images/images/img_008_51edcfb168da.png)

```text
驱动包，百度云盘地址：https://pan.baidu.com/s/1veqFD2k49x5m97FA6CAwJA  密码: gea6
```

2、修改配置文件:conf/activemq.xml

```text
        <persistenceAdapter>
           <!-- <kahaDB directory="${activemq.data}/kahadb"/> -->
        <jdbcPersistenceAdapter dataSource="#activemq-db" createTablesOnStartup="true" />
        </persistenceAdapter>
```

![](./images/images/img_009_e67de4fbdd52.png)

dataSource指定持久化数据库的bean，createTablesOnStartup是否在启动的时候创建数据表，默认使用true，这样每次启动都会去创建数据表了，**一般第一次启动的时候设置为true，之后改成false**

3、在配置文件中的broker节点外增加以下内容

```text
   <bean id="activemq-db" class="org.apache.commons.dbcp.BasicDataSource">
      <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
      <property name="url" value="jdbc:mysql://192.168.31.206:3306/activemq"/>
      <property name="username" value="root"/>
      <property name="password" value="root"/>
      <property name="maxActive" value="200"/>
      <property name="poolPreparedStatements" value="true"/>
    </bean>
```

![](./images/images/img_010_a899f4a016c9.png)

4、从配置中可以看出数据库的名称是activemq，需要手动在mysql中增加这个库，然后**重启消息队列**，你会发现多了三张表

- activeme_acks ->存储持久订阅的信息
- activemq_lock ->锁表(用来做集群的时候，实现master选举的表)
- activemq_msgs ->消息表

###  补充：

**　　mysql必须支持远程连接！！！！**

```text
控制台：
1、mysql -uroot -proot

2、GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
```

### Memory基于内存

　　基于内存的消息存储，就是消息存储在内存中。persistent="false"：表示不设置持久化存储，直接存储到内存中

```text
<broker xmlns="http://activemq.apache.org/schema/core" brokerName="localhost" dataDirectory="${activemq.data}" persistent="false">
```

# 消息消费者处理

## prefetch机制

　　prefetch即在activemq中消费者预获取消息数量，重要的调优参数之一。当消费者存活时，broker将会批量push prefetchSize条消息给消费者，消费者也可以配合optimizeAcknowledge来批量确认它们。由于broker批量push消息给消费者，提高了网络传输效率，默认为1000。

　　broker端将会根据consumer指定的prefetchSize来决定pendingBuffer的大小，prefetchSize越大，broker批量发送的消息就会越多，如果消费者消费速度较快，再配合optimizeAck，这将是相对完美的消息传送方案。

　　不过，prefetchSize也会带来一定的问题，在Queue中(Topic中没有效果)，broker将使用“轮询”方式来平衡多个消费者之间的消息传送数量，如果消费者消费速度较慢，而prefetchSize较大，这将不利于消息量在多个消费者之间平衡。通常情况下，如果consumer数量较多，或者消费速度较慢，或者消息量较少时，我们应该设定prefetchSize为较小的值。

设置prefetchSize的方式如下：

```text
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            Queue queue = session.createQueue("cyb-queue?customer.prefetchSize=100");
```

prefetch值建议在destinationUrl中指定，因为在brokerUrl中指定比较繁琐；在brokerUrl中，queuePrefetchSize和topicPrefetchSize都需要单独设置："&jms.prefetchPolicy.queuePrefetch=12&jms.prefetchPolicy.topicPrefetch=12"等逐个指定。

## optimizeACK机制

**optimizeACK，可优化的消息ACK策略，关系到是否批量确认消息的策略**，这个是Consumer端最重要的调优参数之一。optimizeAcknowledge表示是否开启“优化ACK选项”，当开启optimizeACK策略后，**只有当optimizeACK为true，也只会当session的ACK_MODE为AUTO_ACKNOWLEDGE时才会生效。**

该参数的具体含义和消费端的处理如下：

- 当consumer.optimizeACK有效时，如果客户端已经消费但尚未确认的消息（deliveredMessage）达到prefetch*0.65，从consumer端将会自动进行ACK。
- 同事如果离上一次ACK的时间间隔，已经超过“optimizeAcknowledgeTimeout”毫秒，也会导致自动进行ACK。

```text
            String brokerURL = "tcp://192.168.31.215:61616?jms.optimizeAcknowledge=true&jms.optimizeAcknowledgeTimeOut=30000";
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
```

## ACK模型和类型介绍

### ACK模型

　　ACK模型是确定应答的时机

- AUTO_ACKNOWLEDGE = 1 ->自动确认
- CLIENT_ACKNOWLEDGE = 2 ->客户端手动确认
- DUPS_OK_ACKNOWLEDGE = 3 ->自动批量确认
- SESSION_TRANSACTED = 0 ->事务提交并确认

### ACK类型

　　ACK类型是确定应答的类型，客户端根据ACK类型的不同，需要不同的处理，比如消息重发。

　　Client端指定了ACK模式，但是在Client与broker在交换ACK指令的时候，还需要告知ACK_TYPE，ACK_TYPE表示此确认指定的类型，不同的ACK_TYPE将传递着消息的状态，broker可以根据不同的ACK_TYPE对消息进行不同的操作。

　　比如Consumer消费消息时出现异常,就需要向broker发送ACK指定，ACK_TYPE为“REDELIVERED_ACK_TYPE”

,那么broker就会重新发送此消息。在JMS API中并没有定义ACK_TYPE，因为它通常是一种内部机制，并不会面向开发者。ActiveMQ中定义了如下几种ACK_TYPE

- DELIVERED_ACK_TYPE = 0 消息“已接收”，但尚未处理结束
- STANDARD_ACK_TYPE = 2 “标准”类型，通常表示为消息“处理成功”，broker端可以删除消息了
- POSION_ACK_TYPE = 1 消息“错误”，通常表示“抛弃”此消息，比如消息重发多次后，都无法正常处理时，消息将会被删除或DLQ(死信队列)
- REDELIVERED_ACK_TYPE = 3 消息需“重发”，比如consumer处理消息时抛出异常，broker稍后会重新发送此消息
- INDIVIDUAL_ACK_TYPE = 4 表示只确认“单条消息”，无论在任何ACK_MODE下
- UNMATCHED_ACK_TYPE = 5  在Topic中，如果一条消息在转发给“订阅者”时，发现此消息不合符Selector过滤条件，那么此消息将不会转发给订阅者，消息将会被存储引擎删除

## 重发机制

　　可以在brokerUrl中配置“redelivery”策略，比如当一条消息处理异常时，broker端还可以重发的最大次数。当消息需要broker端重发时，consumer会首先在本地的“deliveredMessage队列”(Consumer已经接收但未确认的消息队列)删除它,善后向broker发送“REDELIVERED_ACK_TYPE”类型的确认指令，broker将会把指令中指定的消息重新添加到pendingQueue中，直到合适的时机，再次push给client。

## 持久化订阅和非持久化订阅

注意事项：

1. 持久化订阅和非持久化订阅针对的消息模型是Pub/Sub，而不是P2P
2. 持久化订阅需要消费者先执行订阅，然后生产者再发送消息
3. 如果消费者宕机，而又不想丢失它宕机期间的消息，就需要开启持久订阅。如果对于同一个消息有多个消费者需要开启持久订阅的情况，则设置的clientID不能相同

### 消费者

```text
    public void testTopicConsumer2() throws Exception {
        //第一步：创建ConnectionFactory
        String brokerURL = "tcp://192.168.31.215:61616";
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
        //第二步：通过工厂，创建Connection
        Connection connection = connectionFactory.createConnection();
        //设置持久订阅的客户端ID
        String clientId = "10086";
        connection.setClientID(clientId);
        //第三步：打开链接
        connection.start();
        //第四步：通过Connection创建session
        Session session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
        //第五步：通过session创建Consumer
        Topic topic = session.createTopic("cyb-topic");

        //创建持久订阅的消费者客户端
        //第一个参数是指定Topic
        //第二个参数是自定义的ClientId
        MessageConsumer consumer = session.createDurableSubscriber(topic, "client1-sub");
        consumer.setMessageListener(new MessageListener() {
            @Override
            public void onMessage(Message message) {
                //第七步：处理信息
                if (message instanceof TextMessage){
                    TextMessage tm=(TextMessage)message;
                    try{
                        System.out.println(tm.getText());
                    }
                    catch (Exception e){
                        e.printStackTrace();
                    }
                }
            }
        });
        //session.commit();
        //第八步：关闭资源
        consumer.close();
        session.close();
        connection.close();
    }
```

### 提供者

```text
    public void testTopicProducer() throws Exception {
        Connection connection = null;
        MessageProducer producer = null;
        Session session = null;
        try {
            //第一步：创建ConnectionFactory，用于连接broker
            String brokerURL = "tcp://192.168.31.215:61616";
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
            //设置消息发送为同步发送
            ((ActiveMQConnectionFactory) connectionFactory).setUseAsyncSend(false);
            //设置
            //((ActiveMQConnectionFactory) connectionFactory).setProducerWindowSize(1000);
            //第二步：通过工厂，创建Connection
            connection = connectionFactory.createConnection();
            ((ActiveMQConnection) connection).setUseAsyncSend(false);
            //第三步：连接启动
            connection.start();
            //第四步：通过连接获取session会话
            //第一个参数：是否启用ActiveMQ事务，如果为true，第二个参数无用
            //第二个参数：应答模式，AUTO_ACKNOWLEDGE为自动应答
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            //第五步：通过session创建destination，两种目的地：Queue、Topic
            //参数：消息队列的名称，在后台管理系统中可以看到
            Topic topic = session.createTopic("cyb-topic");
            //第六步：通过session创建MessageProducer
            producer = session.createProducer(topic);
            //producer.setDeliveryMode(DeliveryMode.PERSISTENT);
            //第七步：创建Message
            //方式一
            //TextMessage message=new ActiveMQTextMessage();
            //message.setText("queue test");
            //方式二
            TextMessage message1 = session.createTextMessage("topic->博客园地址:https://www.cnblogs.com/chenyanbin/");
            //第八步：通过producer发送消息
            producer.send(message1,DeliveryMode.PERSISTENT,1,1000*60*5);
            //session.commit();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            //第九步：关闭资源
            producer.close();
            session.close();
            connection.close();
        }
    }
```

### 测试

　　此处就不测试了，因为当初测试时候，踩了一次坑，测试结果，已经记录到另一篇博客：[ActiveMQ 持久订阅者，执行结果与初衷相违背，验证离线订阅者无效，问题解决](https://www.cnblogs.com/chenyanbin/p/12866452.html)

# ActiveMQ集群

## ActiveMQ集群配置

### 删除一些不用的端口

![](./images/images/img_011_17b583b2a398.png)

### 修改activemq.xml配置文件

方式一：

在任意一台Linux机器上，activemq.xml的broker 标签下，添加以下内容，然后重启即可

![](./images/images/img_012_f78e46b77308.png)

方式二

　　还在修改activemq.xml，在broker标签下，加入以下内容，去掉duplex="true"，配置对方的ip地址，若有多个逗号隔开即可“,” 然后重启

![](./images/images/img_013_39e2ac778f61.png)

### 测试

提供者端代码，brokerUrl中加入容错机制，若果第一个没连上，就连接第一个，默认先连接第一个

```text
failover:(tcp://192.168.1.108:61616,tcp://192.168.1.109:61616)
```

```text
    public void testQueueProducer() throws Exception {
        Connection connection = null;
        MessageProducer producer = null;
        Session session = null;
        try {
            //第一步：创建ConnectionFactory，用于连接broker
            String brokerURL = "failover:(tcp://192.168.1.108:61616,tcp://192.168.1.109:61616)";
            ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
            //设置消息发送为同步发送
            //((ActiveMQConnectionFactory) connectionFactory).setUseAsyncSend(true);
            //设置
            ((ActiveMQConnectionFactory) connectionFactory).setProducerWindowSize(1000);
            //第二步：通过工厂，创建Connection
            connection = connectionFactory.createConnection();

            //((ActiveMQConnection) connection).setUseAsyncSend(true);
            //第三步：连接启动
            connection.start();
            //第四步：通过连接获取session会话
            //第一个参数：是否启用ActiveMQ事务，如果为true，第二个参数无用
            //第二个参数：应答模式，AUTO_ACKNOWLEDGE为自动应答
            session = connection.createSession(false, Session.AUTO_ACKNOWLEDGE);
            //第五步：通过session创建destination，两种目的地：Queue、Topic
            //参数：消息队列的名称，在后台管理系统中可以看到
            Queue queue = session.createQueue("cyb-queue");
            //第六步：通过session创建MessageProducer
            producer = session.createProducer(queue);
            //producer.setDeliveryMode(DeliveryMode.NON_PERSISTENT);
            //第七步：创建Message
            //方式一
            //TextMessage message=new ActiveMQTextMessage();
            //message.setText("queue test");
            //方式二
            TextMessage message1 = session.createTextMessage("博客园地址:https://www.cnblogs.com/chenyanbin/");
            //第八步：通过producer发送消息
            producer.send(message1);
            //session.commit();
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            //第九步：关闭资源
            producer.close();
            session.close();
            connection.close();
        }
    }
```

消费者端代码

```text
    public void testQueueConsumer() throws Exception {
        //第一步：创建ConnectionFactory
        String brokerURL = "tcp://192.168.1.109:61616";
        ConnectionFactory connectionFactory = new ActiveMQConnectionFactory(brokerURL);
        //第二步：通过工厂，创建Connection
        Connection connection = connectionFactory.createConnection();
        //第三步：打开链接
        connection.start();
        //第四步：通过Connection创建session
        Session session = connection.createSession(Boolean.FALSE, Session.CLIENT_ACKNOWLEDGE);
        //第五步：通过session创建Consumer
        Queue queue = session.createQueue("cyb-queue");
        MessageConsumer consumer = session.createConsumer(queue);
        //第六步：通过consumer接收信息(两种方式：1、receive方法接收(同步)；2、通过监听器接收(异步))
        //方式1、receive方法接收信息
        Message message = consumer.receive(100000);
        //第七步：处理信息
        if (message != null && message instanceof TextMessage) {
            TextMessage tm = (TextMessage) message;
            System.out.println(tm.getText());
            message.acknowledge();
        }

        //方式2：监听器接收信息
//        consumer.setMessageListener(new MessageListener() {
//            @Override
//            public void onMessage(Message message) {
//                //第七步：处理信息
//                if (message instanceof TextMessage){
//                    TextMessage tm=(TextMessage)message;
//                    try{
//                        System.out.println(tm.getText());
//                    }
//                    catch (Exception e){
//                        e.printStackTrace();
//                    }
//                }
//            }
//        });
        //session.commit();
        //第八步：关闭资源
        consumer.close();
        session.close();
        connection.close();
    }
```

演示

　　这里我们可以看到，提供者先连接192.168.1.108这台机器，消费者去消费192.168.1.109，照样可以消费成功，监控平台上，也可以看到响应信息

![](./images/images/img_014_3cee7f50a47b.gif)
