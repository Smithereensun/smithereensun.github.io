{

  "title": "RabbitMQ - 入门",
  "has_date": true,
  "description": "RabbitMQ介绍 RabbitMQ是基于Erlang语言开发的开源消息通信中间件，官网地址： Messaging that just works — RabbitMQ 接下来，我们就学习它的基本概念和基础用法。 安装 在安装命令中有两个映射的端口： ：RabbitMQ提供的管理控制台的端口 ：R",
  "tags": [
    "微服务",
    "消息队列",
    "RabbitMQ"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/message-queue/rabbitMQ-basic - RabbitMQ - 入门.md",
  "date": "2025-05-17"

}

## [RabbitMQ介绍](#rabbitmq介绍)

RabbitMQ是基于Erlang语言开发的开源消息通信中间件，官网地址：
[Messaging that just works — RabbitMQ](https://www.rabbitmq.com/)
 接下来，我们就学习它的基本概念和基础用法。

### [安装](#安装)

在安装命令中有两个映射的端口：

- 15672：RabbitMQ提供的管理控制台的端口

- 5672：RabbitMQ的消息发送处理接口

安装完成后，访问 http://127.0.0.1:15672即可看到管理控制台。首次访问需要登录，默认的用户名和密码在配置文件中已经指定了。
 登录后即可看到管理控制台总览页面：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/1f8917fd0f29-202405181721086.png)

RabbitMQ对应的架构如图：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/450c44ac8f8e-202405181722947.png)
 其中包含几个概念：

- `publisher`：生产者，也就是发送消息的一方

- `consumer`：消费者，也就是消费消息的一方

- `queue`：队列，存储消息。生产者投递的消息会暂存在消息队列中，等待消费者处理

- `exchange`：交换机，负责消息路由。生产者发送的消息由交换机决定投递到哪个队列。

- `virtual host`：虚拟主机，起到数据隔离的作用。每个虚拟主机相互独立，有各自的exchange、queue

上述这些东西都可以在RabbitMQ的管理控制台来管理，下一节我们就一起来学习控制台的使用。

### [收发消息](#收发消息)

#### [交换机](#交换机)

打开Exchanges选项卡，可以看到已经存在很多交换机：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/d518085f479c-202405181723116.png)
 点击任意交换机，即可进入交换机详情页面。仍然会利用控制台中的publish message 发送一条消息：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/23532800a20b-202405181724145.png)
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/d519509c8a8b-202405181724722.png)
 这里是由控制台模拟了生产者发送的消息。由于没有消费者存在，最终消息丢失了，这样说明交换机没有存储消息的能力。

#### [队列](#队列)

打开`Queues`选项卡，新建一个队列：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/6c73d680b536-202405181724939.png)
 命名为`hello.queue1`：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/d0ecaad1f29c-202405181724287.png)
 再以相同的方式，创建一个队列，密码为`hello.queue2`，最终队列列表如下：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/e05de8f825d1-202405181724003.png)
 此时，再次向`amq.fanout`交换机发送一条消息。会发现消息依然没有到达队列！！
 怎么回事呢？
 发送到交换机的消息，只会路由到与其绑定的队列，因此仅仅创建队列是不够的，还需要将其与交换机绑定。

#### [绑定关系](#绑定关系)

点击`Exchanges`选项卡，点击`amq.fanout`交换机，进入交换机详情页，然后点击`Bindings`菜单，在表单中填写要绑定的队列名称：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/2e72c2bc8cdb-202405181724889.png)
 相同的方式，将hello.queue2也绑定到改交换机。
 最终，绑定结果如下：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/359478b732cb-202405181724636.png)

#### [发送消息](#发送消息)

再次回到exchange页面，找到刚刚绑定的`amq.fanout`，点击进入详情页，再次发送一条消息：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/bc8c73389577-202405181724058.png)
 回到`Queues`页面，可以发现`hello.queue`中已经有一条消息了：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/1b7c391538fd-202405181724136.png)
 点击队列名称，进入详情页，查看队列详情，这次我们点击get message：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/8e4f0ba5cca5-202405181724246.png)
 可以看到消息到达队列了：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/441625f4b543-202405181724080.png)
 这个时候如果有消费者监听了MQ的`hello.queue1`或`hello.queue2`队列，自然就能接收到消息了。

### [数据隔离](#数据隔离)

#### [用户管理](#用户管理)

点击`Admin`选项卡，首先会看到RabbitMQ控制台的用户管理界面：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/c53d58dea555-202405181725968.png)
 这里的用户都是RabbitMQ的管理或运维人员。目前只有安装RabbitMQ时添加的`itheima`这个用户。仔细观察用户表格中的字段，如下：

- `Name`：`itheima`，也就是用户名

- `Tags`：`administrator`，说明`itheima`用户是超级管理员，拥有所有权限

- `Can access virtual host`： `/`，可以访问的`virtual host`，这里的`/`是默认的`virtual host`

对于小型企业而言，出于成本考虑，我们通常只会搭建一套MQ集群，公司内的多个不同项目同时使用。这个时候为了避免互相干扰， 我们会利用`virtual host`的隔离特性，将不同项目隔离。一般会做两件事情：

- 给每个项目创建独立的运维账号，将管理权限分离。

- 给每个项目创建不同的`virtual host`，将每个项目的数据隔离。

#### [virtual host](#virtual-host)

先退出登录：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/57d431a9db5f-202405181725334.png)
 切换到刚刚创建的 用户登录，然后点击`Virtual Hosts`菜单，进入`virtual host`管理页：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/8cabcee58e62-202405181725434.png)
 可以看到目前只有一个默认的`virtual host`，名字为 `/`。
 我们可以给项目创建一个单独的`virtual host`，而不是使用默认的`/`。
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/f2619f8d88b7-202405181725750.png)
 创建完成后如图：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/6a993e3fb0d8-202405181726916.png)
 由于是登录`hmall`账户后创建的`virtual host`，因此回到`users`菜单，你会发现当前用户已经具备了对`/hmall`这个`virtual host`的访问权限了：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/39938e30aa25-202405181726299.png)

此时，点击页面右上角的`virtual host`下拉菜单，切换`virtual host`为 `/hmall`：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/f1958772ca44-202405181726193.png)
 然后再次查看queues选项卡，会发现之前的队列已经看不到了：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/dcf05cfc7a6f-202405181727365.png)
 这就是基于`virtual host `的隔离效果。

## [SpringAMQP](#springamqp)

将来我们开发业务功能的时候，肯定不会在控制台收发消息，而是应该基于编程的方式。由于`RabbitMQ`采用了AMQP协议，因此它具备跨语言的特性。任何语言只要遵循AMQP协议收发消息，都可以与`RabbitMQ`交互。并且`RabbitMQ`官方也提供了各种不同语言的客户端。
 但是，RabbitMQ官方提供的Java客户端编码相对复杂，一般生产环境下我们更多会结合Spring来使用。而Spring的官方刚好基于RabbitMQ提供了这样一套消息收发的模板工具：SpringAMQP。并且还基于SpringBoot对其实现了自动装配，使用起来非常方便。

SpringAmqp的官方地址：[Spring AMQP](https://spring.io/projects/spring-amqp)

SpringAMQP提供了三个功能：

- 自动声明队列、交换机及其绑定关系

- 基于注解的监听器模式，异步接收消息

- 封装了RabbitTemplate工具，用于发送消息

这一章我们就一起学习一下，如何利用SpringAMQP实现对RabbitMQ的消息收发。

### [配置依赖](#配置依赖)

配置SpringAMQP相关的依赖：

### [快速入门](#快速入门)

在之前的案例中，我们都是经过交换机发送消息到队列，不过有时候为了测试方便，我们也可以直接向队列发送消息，跳过交换机。如图：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/bc54f516c188-202405181728806.jpeg)
 也就是：

- publisher直接发送消息到队列

- 消费者监听并处理队列中的消息

**注意**：这种模式一般测试使用，很少在生产中使用。

为了方便测试，我们现在控制台新建一个队列：simple.queue
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/e7f578eab88a-202405181728591.png)
 添加成功：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/0b10117b72fe-202405181728607.png)
 接下来，我们就可以利用Java代码收发消息了。

#### [消息发送](#消息发送)

首先配置MQ地址，在`publisher`服务的`application.yml`中添加配置：

然后在`publisher`服务中编写测试类`SpringAmqpTest`，并利用`RabbitTemplate`实现消息发送：

打开控制台，可以看到消息已经发送到队列中：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/58eb00775515-202405181729879.png)
 接下来，我们再来实现消息接收。

#### [消息接收](#消息接收)

首先配置MQ地址，在`consumer`服务的`application.yml`中添加配置：

然后在`consumer`服务的`com.itheima.consumer.listener`包中新建一个类`SpringRabbitListener`，代码如下：

#### [测试](#测试)

启动consumer服务，然后在publisher服务中运行测试代码，发送MQ消息。最终consumer收到消息：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/aea5ae050328-202405181729511.png)

### [WorkQueues模型](#workqueues模型)

Work queues，任务模型。简单来说就是**让多个消费者绑定到一个队列，共同消费队列中的消息**。
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/f8efaf14197a-202405181729322.jpeg)

当消息处理比较耗时的时候，可能生产消息的速度会远远大于消息的消费速度。长此以往，消息就会堆积越来越多，无法及时处理。
 此时就可以使用work 模型，**多个消费者共同处理消息处理，消息处理的速度就能大大提高**了。

接下来，我们就来模拟这样的场景。
 首先，我们在控制台创建一个新的队列，命名为`work.queue`：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/1c99eaa84a7e-202405181729775.png)

#### [消息发送](#消息发送-1)

这次我们循环发送，模拟大量消息堆积现象。
 在publisher服务中的SpringAmqpTest类中添加一个测试方法：

#### [消息接收](#消息接收-1)

要模拟多个消费者绑定同一个队列，我们在consumer服务的SpringRabbitListener中添加2个新的方法：

注意到这两消费者，都设置了`Thead.sleep`，模拟任务耗时：

- 消费者1 sleep了20毫秒，相当于每秒钟处理50个消息

- 消费者2 sleep了200毫秒，相当于每秒处理5个消息

#### [测试](#测试-1)

启动ConsumerApplication后，在执行publisher服务中刚刚编写的发送测试方法testWorkQueue。
 最终结果如下：

可以看到消费者1和消费者2竟然每人消费了25条消息：

- 消费者1很快完成了自己的25条消息

- 消费者2却在缓慢的处理自己的25条消息。

也就是说消息是平均分配给每个消费者，并没有考虑到消费者的处理能力。导致1个消费者空闲，另一个消费者忙的不可开交。没有充分利用每一个消费者的能力，最终消息处理的耗时远远超过了1秒。这样显然是有问题的。

#### [能者多劳](#能者多劳)

在spring中有一个简单的配置，可以解决这个问题。我们修改consumer服务的application.yml文件，添加配置：

再次测试，发现结果如下：

可以发现，由于消费者1处理速度较快，所以处理了更多的消息；消费者2处理速度较慢，只处理了6条消息。而最终总的执行耗时也在1秒左右，大大提升。
 正所谓能者多劳，这样充分利用了每一个消费者的处理能力，可以有效避免消息积压问题。

#### [总结](#总结)

Work模型的使用：

- 多个消费者绑定到一个队列，同一条消息只会被一个消费者处理

- 通过设置prefetch来控制消费者预取的消息数量

### [交换机类型](#交换机类型)

在之前的两个测试案例中，都没有交换机，生产者直接发送消息到队列。而一旦引入交换机，消息发送的模式会有很大变化：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/ed56308c2a59-202405181729455.jpeg)
 可以看到，在订阅模型中，多了一个exchange角色，而且过程略有变化：

- **Publisher**：生产者，不再发送消息到队列中，而是发给交换机

- **Exchange**：交换机，一方面，接收生产者发送的消息。另一方面，知道如何处理消息，例如递交给某个特别队列、递交给所有队列、或是将消息丢弃。到底如何操作，取决于Exchange的类型。

- **Queue**：消息队列也与以前一样，接收消息、缓存消息。不过队列一定要与交换机绑定。

- **Consumer**：消费者，与以前一样，订阅队列，没有变化

**Exchange（交换机）只负责转发消息，不具备存储消息的能力**，因此如果没有任何队列与Exchange绑定，或者没有符合路由规则的队列，那么消息会丢失！

交换机的类型有四种：

- **Fanout**：广播，将消息交给所有绑定到交换机的队列。我们最早在控制台使用的正是Fanout交换机

- **Direct**：订阅，基于RoutingKey（路由key）发送给订阅了消息的队列

- **Topic**：通配符订阅，与Direct类似，只不过RoutingKey可以使用通配符

- **Headers**：头匹配，基于MQ的消息头匹配，用的较少。

这里主要讲解前面的三种交换机模式。

#### [Fanout交换机](#fanout交换机)

Fanout，英文翻译是扇出，我觉得在MQ中叫广播更合适。

在广播模式下，消息发送流程是这样的：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/6edd3e9cd3b3-202405181730342.png)

- 1） 可以有多个队列

- 2） 每个队列都要绑定到Exchange（交换机）

- 3） 生产者发送的消息，只能发送到交换机

- 4） 交换机把消息发送给绑定过的所有队列

- 5） 订阅队列的消费者都能拿到消息

我们的计划是这样的：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/896a698df3d7-202405181730444.png)

- 创建一个名为` hmall.fanout`的交换机，类型是`Fanout`

- 创建两个队列`fanout.queue1`和`fanout.queue2`，绑定到交换机`hmall.fanout`

##### [声明队列和交换机](#声明队列和交换机)

在控制台创建队列`fanout.queue1`:
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/95a5a0641dad-202405181730019.png)
 在创建一个队列`fanout.queue2`：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/a0fec3b58088-202405181730160.png)
 然后再创建一个交换机：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/f22f45db60fb-202405181730806.png)
 然后绑定两个队列到交换机：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/6e4740b95dd3-202405181730703.png)
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/5d5597cb52fb-202405181730237.png)

##### [消息发送](#消息发送-2)

在publisher服务的SpringAmqpTest类中添加测试方法：

##### [消息接收](#消息接收-2)

在consumer服务的SpringRabbitListener中添加两个方法，作为消费者：

##### [总结](#总结-1)

交换机的作用是什么？

- 接收publisher发送的消息

- 将消息按照规则路由到与之绑定的队列

- 不能缓存消息，路由失败，消息丢失

- FanoutExchange的会将消息路由到每个绑定的队列

#### [Direct交换机](#direct交换机)

在Fanout模式中，一条消息，会被所有订阅的队列都消费。但是，在某些场景下，我们希望不同的消息被不同的队列消费。这时就要用到Direct类型的Exchange。
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/c38ae5ebf636-202405181730102.png)
 在Direct模型下：

- 队列与交换机的绑定，不能是任意绑定了，而是要指定一个`RoutingKey`（路由key）

- 消息的发送方在 向 Exchange发送消息时，也必须指定消息的 `RoutingKey`。

- Exchange不再把消息交给每一个绑定的队列，而是根据消息的`Routing Key`进行判断，只有队列的`Routingkey`与消息的 `Routing key`完全一致，才会接收到消息

**案例需求如图**：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/52b61a8fca20-202405181730970.png)

1. 声明一个名为`hmall.direct`的交换机

1. 声明队列`direct.queue1`，绑定`hmall.direct`，`bindingKey`为`blud`和`red`

1. 声明队列`direct.queue2`，绑定`hmall.direct`，`bindingKey`为`yellow`和`red`

1. 在`consumer`服务中，编写两个消费者方法，分别监听direct.queue1和direct.queue2

1. 在publisher中编写测试方法，向`hmall.direct`发送消息

##### [声明队列和交换机](#声明队列和交换机-1)

首先在控制台声明两个队列`direct.queue1`和`direct.queue2`，这里不再展示过程：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/6adbd63c2095-202405181731363.png)
 然后声明一个direct类型的交换机，命名为`hmall.direct`:
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/3daf89178290-202405181731928.png)
 然后使用`red`和`blue`作为key，绑定`direct.queue1`到`hmall.direct`：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/7c28fb964637-202405181731372.png)
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/44d625e131ac-202405181731495.png)

同理，使用`red`和`yellow`作为key，绑定`direct.queue2`到`hmall.direct`，步骤略，最终结果：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/2de8354b947f-202405181731224.png)

##### [消息接收](#消息接收-3)

在consumer服务的SpringRabbitListener中添加方法：

##### [消息发送](#消息发送-3)

在publisher服务的SpringAmqpTest类中添加测试方法：

由于使用的red这个key，所以两个消费者都收到了消息：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/93c863fdba65-202405181731746.png)
 我们再切换为blue这个key：

你会发现，只有消费者1收到了消息：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/820fc1fe495b-202405181731238.png)

##### [总结](#总结-2)

描述下Direct交换机与Fanout交换机的差异？

- Fanout交换机将消息路由给每一个与之绑定的队列

- Direct交换机根据RoutingKey判断路由给哪个队列

- 如果多个队列具有相同的RoutingKey，则与Fanout功能类似

#### [Topic交换机](#topic交换机)

##### [说明](#说明)

`Topic`类型的`Exchange`与`Direct`相比，都是可以根据`RoutingKey`把消息路由到不同的队列。
 只不过`Topic`类型`Exchange`可以让队列在绑定`BindingKey` 的时候使用通配符！

`BindingKey` 一般都是有一个或多个单词组成，多个单词之间以`.`分割，例如： `item.insert`

通配符规则：

- `#`：匹配一个或多个词

- `*`：匹配不多不少恰好1个词

举例：

- `item.#`：能够匹配`item.spu.insert` 或者 `item.spu`

- `item.*`：只能匹配`item.spu`

图示：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/7ff4914e1562-202405181732455.png)
 假如此时publisher发送的消息使用的`RoutingKey`共有四种：

- `china.news `代表有中国的新闻消息；

- `china.weather` 代表中国的天气消息；

- `japan.news` 则代表日本新闻

- `japan.weather` 代表日本的天气消息；

解释：

- `topic.queue1`：绑定的是`china.#`，凡是以 `china.`开头的`routing key` 都会被匹配到，包括：

  - `china.news`

  - `china.weather`

- `topic.queue2`：绑定的是`#.news`，凡是以 `.news`结尾的 `routing key` 都会被匹配。包括:

  - `china.news`

  - `japan.news`

接下来，我们就按照上图所示，来演示一下Topic交换机的用法。
 首先，在控制台按照图示例子创建队列、交换机，并利用通配符绑定队列和交换机。此处步骤略。最终结果如下：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/584d19d4c1cd-202405181732051.png)

##### [消息发送](#消息发送-4)

在publisher服务的SpringAmqpTest类中添加测试方法：

##### [消息接收](#消息接收-4)

在consumer服务的SpringRabbitListener中添加方法：

##### [总结](#总结-3)

描述下Direct交换机与Topic交换机的差异？

- Topic交换机接收的消息RoutingKey必须是多个单词，以 `**.**` 分割

- Topic交换机与队列绑定时的bindingKey可以指定通配符

- `#`：代表0个或多个词

- `*`：代表1个词

### [声明队列和交换机](#声明队列和交换机-2)

在之前我们都是基于RabbitMQ控制台来创建队列、交换机。但是在实际开发时，队列和交换机是程序员定义的，将来项目上线，又要交给运维去创建。那么程序员就需要把程序中运行的所有队列和交换机都写下来，交给运维。在这个过程中是很容易出现错误的。
 因此推荐的做法是由程序启动时检查队列和交换机是否存在，如果不存在自动创建。

#### [基本API](#基本api)

SpringAMQP提供了一个Queue类，用来创建队列：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/69cb6aa48486-202405181732782.png)

SpringAMQP还提供了一个Exchange接口，来表示所有不同类型的交换机：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/96f8b42f6fc1-202405181732490.png)
 我们可以自己创建队列和交换机，不过SpringAMQP还提供了ExchangeBuilder来简化这个过程：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/3ca7a3e3759e-202405181733210.png)
 而在绑定队列和交换机时，则需要使用BindingBuilder来创建Binding对象：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/801955589398-202405181733570.png)

#### [fanout示例](#fanout示例)

在consumer中创建一个类，声明队列和交换机：

#### [direct示例](#direct示例)

direct模式由于要绑定多个KEY，会非常麻烦，每一个Key都要编写一个binding：

#### [基于注解声明](#基于注解声明)

基于@Bean的方式声明队列和交换机比较麻烦，Spring还提供了基于注解方式来声明。

例如，我们同样声明Direct模式的交换机和队列：

是不是简单多了。
 再试试Topic模式：

### [消息转换器](#消息转换器)

Spring的消息发送代码接收的消息体是一个Object：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/4f10d8e51cac-202405181734921.png)
 而在数据传输时，它会把你发送的消息序列化为字节发送给MQ，接收消息的时候，还会把字节反序列化为Java对象。
 只不过，默认情况下Spring采用的序列化方式是JDK序列化。众所周知，JDK序列化存在下列问题：

- 数据体积过大

- 有安全漏洞

- 可读性差

我们来测试一下。

#### [测试默认转换器](#测试默认转换器)

1）创建测试队列
 首先，我们在consumer服务中声明一个新的配置类：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/079966f43989-202405181735641.png)
利用@Bean的方式创建一个队列，具体代码：

注意，这里我们先不要给这个队列添加消费者，我们要查看消息体的格式。

重启consumer服务以后，该队列就会被自动创建出来了：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/af5fdd047ef3-202405181735148.png)

2）发送消息
 我们在publisher模块的SpringAmqpTest中新增一个消息发送的代码，发送一个Map对象：

发送消息后查看控制台：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/1bb94c86752e-202405181735790.png)
 可以看到消息格式非常不友好。

#### [配置JSON转换器](#配置json转换器)

显然，JDK序列化方式并不合适。我们希望消息体的体积更小、可读性更高，因此可以使用JSON方式来做序列化和反序列化。

在`publisher`和`consumer`两个服务中都引入依赖：

注意，如果项目中引入了`spring-boot-starter-web`依赖，则无需再次引入`Jackson`依赖。

配置消息转换器，在`publisher`和`consumer`两个服务的启动类中添加一个Bean即可：

消息转换器中添加的messageId可以便于我们将来做幂等性判断。

此时，我们到MQ控制台**删除**`object.queue`中的旧的消息。然后再次执行刚才的消息发送的代码，到MQ的控制台查看消息结构：
![](/imported/markdown/2025-05-17-markdown-b8b7afc5-rabbitmq-入门/images/dd43235af357-202405181735163.png)

#### [消费者接收Object](#消费者接收object)

我们在consumer服务中定义一个新的消费者，publisher是用Map发送，那么消费者也一定要用Map接收，格式如下：

## [常用的 RabbitMQ 插件](#常用的-rabbitmq-插件)

RabbitMQ 支持许多插件，这些插件可以扩展 RabbitMQ 的功能和特性。以下是一些常用的 RabbitMQ 插件：

- Management Plugin： RabbitMQ 管理插件提供了一个 Web 管理界面，用于监控和管理 RabbitMQ 服务器。可以查看队列、交换机、连接、通道等的状态，并进行配置和操作。

- Shovel Plugin： Shovel 插件用于将消息从一个 RabbitMQ 服务器传递到另一个 RabbitMQ 服务器，实现消息复制和跨集群通信。它可以用于实现数据复制、故障恢复、数据中心间同步等。

- Federation Plugin： Federation 插件允许不同 RabbitMQ 集群之间建立联合，实现消息的跨集群传递。这对于构建分布式系统、将消息从一个地理位置传递到另一个地理位置非常有用。

- STOMP Plugin： STOMP插件允许使用 STOMP 协议与 RabbitMQ 进行通信。这对于使用非 AMQP 协议的客户端与 RabbitMQ 交互非常有用，例如使用 WebSocket 的 Web 应用程序。

- Prometheus Plugin： Prometheus 插件用于将 RabbitMQ 的性能指标导出到 Prometheus 监控系统，以便进行性能监控和警报。

- Delayed Message Plugin： 延迟消息插件允许发布延迟交付的消息，使你能够在稍后的时间点将消息传递给消费者。这对于实现定时任务、延迟重试等场景非常有用。
