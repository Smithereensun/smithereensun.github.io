{

  "title": "Tomcat - 线程池的设计与实现：StandardThreadExecutor",
  "has_date": true,
  "description": "理解思路 我们如下几个方面开始引入线程池的，这里主要从上文Service引入，保持上下文之间的衔接，会很好的构筑你的知识体系。 上文中我们了解到，Executor是包含在Service中的，Service中关于Executor的配置和相关代码如下： server.xml中service里包含Exec",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-executor - Tomcat - 线程池的设计与实现：StandardThreadExecutor.md",
  "date": "2026-04-19"

}

## [理解思路](#理解思路)

我们如下几个方面开始引入线程池的，这里主要从上文Service引入，保持上下文之间的衔接，会很好的构筑你的知识体系。

- 上文中我们了解到，Executor是包含在Service中的，Service中关于Executor的配置和相关代码如下：

server.xml中service里包含Executor的配置

Service中executors相关方法

- 和Server、Service实现一样，StandardThreadExecutor也是继承LifecycleMBeanBase；然后实现Executor的接口。

![](/imported/markdown/2026-04-19-markdown-bbc4f198-tomcat-线程池的设计与实现-standardthreadexecutor/images/70eefcbc201c-202603082033960.jpeg)

- Tomcat关于Executor相关的配置文档

[http://tomcat.apache.org/tomcat-9.0-doc/config/executor.html](http://tomcat.apache.org/tomcat-9.0-doc/config/executor.html)

## [Executor接口设计](#executor接口设计)

Executor的设计很简单，在理解的时候需要理解两点：

1. Tomcat希望将Executor也纳入Lifecycle**生命周期管理**，所以让它实现了Lifecycle接口

1. **引入超时机制**：也就是说当work queue满时，会等待指定的时间，如果超时将抛出RejectedExecutionException，所以这里增加了一个`void execute(Runnable command, long timeout, TimeUnit unit)`方法; 其实本质上，它构造了JUC中ThreadPoolExecutor，通过它调用ThreadPoolExecutor的`void execute(Runnable command, long timeout, TimeUnit unit)`方法。

找到Executor的实现类
![](/imported/markdown/2026-04-19-markdown-bbc4f198-tomcat-线程池的设计与实现-standardthreadexecutor/images/d6772ae68fc7-202603082035276.jpeg)
## [StandardThreadExecutor的实现](#standardthreadexecutor的实现)

接下来我们看下具体的实现类StandardThreadExecutor。

### [理解相关配置参数](#理解相关配置参数)

[Executor官方配置说明文档](http://tomcat.apache.org/tomcat-9.0-doc/config/executor.html)

- 公共属性

Executor的所有实现都 支持以下属性：
属性描述className实现的类。实现必须实现 org.apache.catalina.Executor接口。此接口确保可以通过其name属性引用对象并实现Lifecycle，以便可以使用容器启动和停止对象。className的默认值是org.apache.catalina.core.StandardThreadExecutorname用于在server.xml中的其他位置引用此池的名称。该名称是必需的，必须是唯一的。

- **StandardThreadExecutor属性**

默认实现支持以下属性：
属性描述threadPriority（int）执行程序中线程的线程优先级，默认为 5（Thread.NORM_PRIORITY常量的值）daemon（boolean）线程是否应该是守护程序线程，默认为 truenamePrefix（字符串）执行程序创建的每个线程的名称前缀。单个线程的线程名称将是namePrefix+threadNumbermaxThreads（int）此池中活动线程的最大数量，默认为 200minSpareThreads（int）最小线程数（空闲和活动）始终保持活动状态，默认为 25maxIdleTime（int）空闲线程关闭之前的毫秒数，除非活动线程数小于或等于minSpareThreads。默认值为60000（1分钟）maxQueueSize（int）在我们拒绝之前可以排队等待执行的可运行任务的最大数量。默认值是Integer.MAX_VALUEprestartminSpareThreads（boolean）是否应该在启动Executor时启动minSpareThreads，默认值为 falsethreadRenewalDelay（long）如果配置了ThreadLocalLeakPreventionListener，它将通知此执行程序有关已停止的上下文。上下文停止后，池中的线程将被更新。为避免同时更新所有线程，此选项在任意2个线程的续订之间设置延迟。该值以ms为单位，默认值为1000ms。如果值为负，则不会续订线程。
### [Lifecycle模板方法](#lifecycle模板方法)

先看核心变量：

- **initInternal**和**destroyInternal**默认父类实现

- **startInternal方法**

这个方法中，我们不难看出，就是初始化taskqueue，同时构造ThreadPoolExecutor的实例，后面Tomcat的StandardThreadExecutor的实现本质上通过ThreadPoolExecutor实现的。

- **stopInternal方法**

代码很简单，关闭线程池后置null, 方便GC回收。

### [核心executor方法](#核心executor方法)

本质上就是调用ThreadPoolExecutor的实例的相关方法。

### [动态调整线程池](#动态调整线程池)

我们还注意到StandardThreadExecutor还实现了ResizeableExecutor，从名称上我们就可知道它是希望实现对线程池的动态调整，所以呢，它封装了一个ResizeableExecutor的接口，看下接口。

前三个方法比较简单，我们看下后两个方法是如何实现的, 其实也很简单。

### [补充TaskQueue](#补充taskqueue)

我们知道工作队列是有TaskQueue保障的，它集成自LinkedBlockingQueue（一个阻塞的链表队列），来看下源代码吧。

TaskQueue这个任务队列是专门为线程池而设计的。优化任务队列以适当地利用线程池执行器内的线程。

如果你使用一个普通的队列，当有空闲线程executor将产生线程并且你不能强制将任务添加到队列。

### [为什么不是直接使用ThreadPoolExecutor](#为什么不是直接使用threadpoolexecutor)

这里你是否考虑过一个问题，为什么Tomcat会自己构造一个StandardThreadExecutor而不是直接使用ThreadPoolExecutor？

从上面的代码，你会发现这里只是使用executor只是使用了execute的两个主要方法，它希望让调用层屏蔽掉ThreadPoolExecutor的其它方法：

- 它体现的原则：**最少知识原则**: 只和你的密友谈话。也就是说客户对象所需要交互的对象应当尽可能少

- 它体现的设计模式：结构型 - 外观(Facade)：外观模式(Facade pattern)，它提供了一个统一的接口，用来访问子系统中的一群接口，从而让子系统更容易使用
