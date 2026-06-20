{

  "title": "Tomcat - 组件管理源码详解",
  "has_date": true,
  "description": "生命周期管理：LifeCycle 我从以下几方面，帮助你构建基于上下文的知识体系和理解为什么要理解组件的生命周期管理（LifeCycle) Server及其它组件 Server后续组件生命周期及初始化 Server的依赖结构 LifeCycle接口 理解Lifecycle主要有两点：第一是三类接口方",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-lifecycle - Tomcat - 组件管理源码详解.md",
  "date": "2026-04-19"

}

## [生命周期管理：LifeCycle](#生命周期管理-lifecycle)

我从以下几方面，帮助你构建基于上下文的知识体系和理解为什么要理解组件的生命周期管理（LifeCycle)

- Server及其它组件

![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/8f842360d4a7-202603081058757.png)

- Server后续组件生命周期及初始化

![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/858701b0c014-202603081100344.png)

- Server的依赖结构

![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/a11d013e66f5-202603081100692.png)
### [LifeCycle接口](#lifecycle接口)

理解Lifecycle主要有两点：第一是三类接口方法；第二是状态机。

### [一个标准的LifeCycle有哪些方法？](#一个标准的lifecycle有哪些方法)

分三类去看：

#### [LifeCycle状态机有哪些状态？](#lifecycle状态机有哪些状态)

Tomcat 给各个组件定义了一些生命周期中的状态

- 在枚举类 LifecycleState 里

- 它们之间的关系是怎么样的呢？

在Lifecycle.java源码中有相关的注释：
![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/a05375abe107-202603081101459.png)
看不太清楚的可以看下图：
![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/9abffea56ce5-202603081101303.jpeg)
### [LifecycleBase - LifeCycle的基本实现](#lifecyclebase-lifecycle的基本实现)

LifecycleBase是Lifecycle的基本实现。

#### [监听器相关](#监听器相关)

生命周期监听器保存在一个线程安全的**CopyOnWriteArrayList**中。所以add和remove都是直接调用此List的相应方法。 findLifecycleListeners返回的是一个数组，为了线程安全，所以这儿会生成一个新数组。

#### [生命周期相关](#生命周期相关)

- init

我们再来看看invalidTransition方法，该方法直接抛出异常。

setStateInternal方法用于维护状态，同时在状态转换成功之后触发事件。为了状态的可见性，所以state声明为volatile类型的。

设置完 state 的状态之后，就触发该状态的事件了，通知事件监听器

这里的 LifecycleListener 对象是在 Catalina 对象解析 server.xml 文件时就已经创建好并加到 lifecycleListeners 里的。这个不是特别重要就不细讲了。

- start

- stop

- destory

#### [用了什么设计模式？](#用了什么设计模式)

从上述源码看得出来，LifecycleBase是使用了**状态机**+**模板模式**来实现的。模板方法有下面这几个：

## [组件拓展管理：MX和MBean](#组件拓展管理-mx和mbean)

### [为什么要了解JMX](#为什么要了解jmx)

我们在上文中讲Lifecycle和相关组件时，你会发现其实还设计一块就是左侧的JMX和MBean的实现，即LifecycleMBeanBase.
![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/8b67af91cf95-202603081103963.jpeg)
### [什么是JMX和MBean](#什么是jmx和mbean)

JMX是java1.5中引入的新特性。JMX全称为“Java Management Extension”，即Java管理扩展。

JMX(Java Management Extensions)是一个为应用程序植入管理功能的框架。JMX是一套标准的代理和服务，实际上，用户可以在任何Java应用程序中使用这些代理和服务实现管理。它使用了最简单的一类javaBean，使用有名的MBean，其内部包含了数据信息，这些信息可能是程序配置信息、模块信息、系统信息、统计信息等。MBean可以操作可读可写的属性、直接操作某些函数。

**应用场景**：中间件软件WebLogic的管理页面就是基于JMX开发的，而JBoss则整个系统都基于JMX构架，我们今天讲的Tomcat也是基于JMX开发而来的。

我们看下**JMX的结构**
![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/bc7518784c3c-202603081104343.png)

- **Probe Level** 负责资源的检测（获取信息），包含MBeans，通常也叫做Instrumentation Level。MX管理构件（MBean）分为四种形式，分别是标准管理构件（Standard MBean）、动态管理构件（Dynamic MBean）、开放管理构件(Open Mbean)和模型管理构件(Model MBean)。

- **The Agent Level** 或者叫做MBean Server（代理服务器），是JMX的核心，连接Mbeans和远程监控程序。

- **Remote Management Level** 通过connectors和adaptors来远程操作MBean Server。

### [JMX使用案例](#jmx使用案例)

上节只是引入和相关概念，这是不够的，你依然需要一个案例来帮助你理解JMX是如何工作的。

#### [基于JMX的监控例子](#基于jmx的监控例子)

- ServerImpl - 我们模拟的某个服务器ServerImpl状态

- 由于MXBean规定，标准MBean也要实现一个接口，其所有向外界公开的方法都要在该接口中声明，否则管理系统就不能从中获取信息。此外，该接口的命名有一定的规范：在标准MBean类名后加上MBean后缀。这里的标准MBean类就是ServerMonitor，所以其对应的接口就应该是ServerMonitorMBean。因此ServerMonitorMBean的实现如下

- 使用ServerMonitor类来监测ServerImpl的状态，实现如下

- 对于管理系统来讲，这些MBean中公开的方法，最终会被JMX转换为属性（Attribute）、监听（Listener）和调用（Invoke）的概念。下面代码中Main类的manage方法就模拟了管理程序是如何获取监测到的属性，并表现监测结果。

- 整体流程

![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/9784de6f973f-202603081105965.jpeg)

如上步骤就能让你理解常见的Jconsole是如何通过JMX获取属性，对象等监控信息的了。

#### [基于JMX的HTMLAdapter案例](#基于jmx的htmladapter案例)

上面例子，还没有体现adapter展示，比如上述信息在HTML页面中展示出来，再看一个例子

- 我们的管理目标

- 根据标准MBean类抽象出符合规范的MBean类的接口，并修改标准MBean类实现该接口。

- 根据需求，创建管理（目标程序）的类，其中包含操纵和获取（目标程序）特性的方法。这个类就是标准MBean类。

- 创建MBean的代理类，代理中包含创建MBeanServer、生成ObjectName、注册MBean、表现MBean

- 打开相关页面

PS：相关Adapter可以通过这里下载[https://download.csdn.net/download/com_ma/10379741](https://download.csdn.net/download/com_ma/10379741)
![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/9d710fe571d9-202603081105848.jpeg)
点击最后一个链接
![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/bcefc8b2cf4b-202603081106051.jpeg)
### [Tomcat如何通过JMX实现组件管理](#tomcat如何通过jmx实现组件管理)

在简单理解了JMX概念和案例之后，我们便可以开始学习Tomcat基于JMX的实现了。

![](/imported/markdown/2026-04-19-markdown-504c74c5-tomcat-组件管理源码详解/images/f946b7e82b5e-202603081106913.jpeg)
上述图中，我们看下相关的类的用途

- `MBeanRegistration`：Java JMX框架提供的注册MBean的接口，引入此接口是为了便于使用JMX提供的管理功能；

- `JmxEnabled`: 此接口由组件实现，这些组件在创建时将注册到MBean服务器，在销毁时将注销这些组件。它主要是由实现生命周期的组件来实现的，但并不是专门为它们实现的。

- `LifecycleMBeanBase`：Tomcat提供的对MBeanRegistration的抽象实现类，运用抽象模板模式将所有容器统一注册到JMX；

此外，ContainerBase、StandardServer、StandardService、WebappLoader、Connector、StandardContext、StandardEngine、StandardHost、StandardWrapper等容器都继承了LifecycleMBeanBase，因此这些容器都具有了同样的生命周期并可以通过JMX进行管理。

#### [MBeanRegistration](#mbeanregistration)

理解MBeanRegistration主要在于:

- 两块内容：registered 和 unregistered

- 两类方法：before和after

#### [JmxEnabled](#jmxenabled)

理解JmxEnabled：在设计上它引一个域（Domain）对注册的MBeans进行隔离，这个域类似于MBean上层的命名空间一样。

#### [LifecycleMBeanBase](#lifecyclembeanbase)

这样理解LifecycleMBeanBase时，你便知道它包含两块，一个是Lifecycle的接口实现，一个是Jmx接口封装实现。

从它实现的类继承和实现关系便能看出：

##### [JmxEnabled的接口实现](#jmxenabled的接口实现)

- Domain和mBeanName相关，代码很简单，不做详解

- 注册和卸载的相关方法

##### [LifecycleBase相关接口](#lifecyclebase相关接口)

这样你就知道这里抽象出的LifecycleBase如下两个方法的用意，就是为了注册和卸载MBean
