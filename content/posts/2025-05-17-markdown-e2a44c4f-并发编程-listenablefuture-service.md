{

  "title": "并发编程 - ListenableFuture&Service",
  "has_date": true,
  "description": "MoreExecutors directExecutor 执行 callback 的线程池这里指定为 ，那么这里执行打印 result 的线程是**主线程** 在 中，可以看到定义是这样的： 以及 其实是一个假的线程池，表示直接执行。 再看下面这个例子： 那么这里清晰了： 如果 future 已经完",
  "tags": [
    "工具库"
  ],
  "source": "local-markdown-library",
  "source_path": "tool-library/guava/guava-cocurrent - 并发编程 - ListenableFuture&Service.md",
  "date": "2025-05-17"

}

## [MoreExecutors](#moreexecutors)

### [directExecutor](#directexecutor)

执行 callback 的线程池这里指定为 `MoreExecutors#directExecutor`，那么这里执行打印 result 的线程是**主线程**
![](/imported/markdown/2025-05-17-markdown-e2a44c4f-并发编程-listenablefuture-service/images/e0f4363a551c-202407181438115.png)
在 `MoreExecutors#directExecutor` 中，可以看到定义是这样的：

以及

`MoreExecutors#directExecutor` 其实是一个假的线程池，表示直接执行。

再看下面这个例子：
![](/imported/markdown/2025-05-17-markdown-e2a44c4f-并发编程-listenablefuture-service/images/c609081f2170-202407181438160.png)
那么这里清晰了：

- 如果 future 已经完成，那么 `MoreExecutor#directExecutor` 表示当前线程；

- 如果 future 未完成，那么 `MoreExecutor#directExecutor` 就是未来完成 future 的线程。

因此其实具体执行回调的线程某种程度上是不确定的

## [ListenableFuture](#listenablefuture)

### [引言](#引言)

jdk原生的future已经提供了异步操作，但是不能直接回调。guava对future进行了增强，核心接口就是ListenableFuture。JDK8从guava中吸收了精华新增的类CompletableFuture，也可以直接看这个类的学习。

JUC 的 Future 接口提供了一种异步获取任务执行结果的机制，表示一个异步计算的结果。

Executor 实际返回的是实现类 FutureTask，它同时实现了 Runnable 接口，因此可以手动创建异步任务。

而 Guava 提供的 ListenableFuture 更进一步，允许注册回调，在任务完成后自动执行，实际也是使用它的实现类 ListenableFutureTask。

### [回调源码剖析](#回调源码剖析)

先看下ListenableFuture接口定义：

可以看到，这个接口在Future接口的基础上增加了addListener方法，允许我们注册回调函数。当然，在编程时可能不会直接使用这个接口，因为这个接口只能传Runnable实例。

#### [addListener方法](#addlistener方法)

这里其实就是在添加listener的方法中首先检查Future是否已经完成：

- 如果Future已经完成，那么就没有必要添加新的监听器，直接executeListener。

- 如果future没有完成，那么会新建一个Listener节点，并插入到链表头部（Listener就是一个链表）

如果已经完成，会直接执行executeListner 方法

那么如果没有完成呢，在listener链表中的什么时候会执行？看后续的回调函数的触发内容

#### [addCallback方法](#addcallback方法)

Futures类还提供了另一个回调方法：addCallback方法

这里调用了ListenableFuture接口的addListener方法，传入了一个CallbackListener实例。而这个实例由需要传入future和一个Callback实例，所以这个回调是可以拿到返回值的。本质上是guava基于Runnable封了一个回调接口。

看下这个CallbackListener接口：

那么这个回调函数什么时候会执行？看后续的回调函数的触发内容

#### [回调函数的触发](#回调函数的触发)

那么这些回调方法什么时候会触发呢？

那哪些方法会来调用这个complete方法呢？
![](/imported/markdown/2025-05-17-markdown-e2a44c4f-并发编程-listenablefuture-service/images/3cf2d21da538-202407171818459.png)
## [Service](#service)

Guava 的 Service 框架是一个用于管理服务生命周期的轻量级框架，可以帮助我们把异步操作封装成一个Service服务。让这个服务有了运行状态(也可以理解成生命周期)，这样可以实时了解当前服务的运行状态。同时还可以添加监听器来监听服务运行状态之间的变化。

Guava里面的服务有五种状态，如下所示：

- Service.State.NEW: 服务创建状态

- Service.State.STARTING: 服务启动中

- Service.State.RUNNING：服务启动完成，正在运行中

- Service.State.STOPPING: 服务停止中

- Service.State.TERMINATED: 服务停止完成，结束

所有的服务都需要实现Service接口，里面包括了服务需要实现的一些基本方法，以下是Service接口：

那应该怎么来使用Service，需要实现的异步逻辑包装成服务呢．Guava里面已经给提供了三个基础实现类：

- AbstractService

- AbstractExecutionThreadService

- AbstractScheduledService

### [AbstractExecutionThreadService](#abstractexecutionthreadservice)

AbstractExecutionThreadService可以把一个具体的异步操作封装成Service服务。说白了就是把之前在线程的实现逻辑封装成服务，把之前线程的具体实现逻辑搬到AbstractExecutionThreadService的实现方法run()方法去执行。

#### [常用方法介绍](#常用方法介绍)

首先AbstractExecutionThreadService实现了Service，Service的方法在AbstractExecutionThreadService里面都有，AbstractExecutionThreadService新加了一些方法。如下所示：

AbstractExecutionThreadService类里面最重要的就是run()方法了，这个方法是服务需要具体实现的方法，服务需要处理的具体逻辑在这个方法里面做。

#### [具体使用](#具体使用)

### [AbstractScheduledService](#abstractscheduledservice)

AbstractScheduledService可以把周期性的任务封装成一个服务。线程池也有一个周期性的线程池么，两者是一一对应的．

#### [常用方法介绍](#常用方法介绍-1)

AbstractScheduledService也是一个服务所以Service里面的方法AbstractScheduledService也都有，同时，AbstractScheduledService也新增了一些其它方法

#### [具体使用](#具体使用-1)

自定义一个类继承AbstractScheduledService，实现一个非常简单的周期性任务．

### [ServiceManager](#servicemanager)

ServiceManager是用来管理多个服务的，让对多个服务的操作变的更加方便，比如可以同时去启动多个服务，同时去停止多个服务等等。

#### [常用方法介绍](#常用方法介绍-2)

#### [具体使用](#具体使用-2)
