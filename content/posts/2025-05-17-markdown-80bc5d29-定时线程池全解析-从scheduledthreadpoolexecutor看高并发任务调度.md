{

  "title": "定时线程池全解析：从ScheduledThreadPoolExecutor看高并发任务调度",
  "has_date": true,
  "description": "前言 项目中经常会遇到一些非分布式的调度任务，需要在未来的某个时刻周期性执行。实现这样的功能，我们有多种方式可以选择： 类， jdk1.3引入，不推荐。 它所有任务都是串行执行的，同一时间只能有一个任务在执行，而且前一个任务的延迟或异常都将会影响到之后的任务。可能会出现任务执行时间过长而导致任务相互",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/04-threadpool2-scheduledthreadpoolexecutor - 定时线程池全解析：从ScheduledThreadPoolExecutor看高并发任务调度.md",
  "date": "2025-05-17"

}

## [前言](#前言)

项目中经常会遇到一些非分布式的调度任务，需要在未来的某个时刻周期性执行。实现这样的功能，我们有多种方式可以选择：

1. `Timer`类， jdk1.3引入，不推荐。

它所有任务都是串行执行的，同一时间只能有一个任务在执行，而且前一个任务的延迟或异常都将会影响到之后的任务。可能会出现任务执行时间过长而导致任务相互阻塞的情况

1. Spring的`@Scheduled`注解，不是很推荐

这种方式底层虽然是用线程池实现，但是有个最大的问题，所有的任务都使用的同一个线程池，可能会导致长周期的任务运行影响短周期任务运行，造成线程池"饥饿"，更加推荐的做法是同种类型的任务使用同一个线程池。

1. 自定义`ScheduledThreadPoolExecutor`实现调度任务

这也是本文重点讲解的方式，通过自定义`ScheduledThreadPoolExecutor`调度线程池，提交调度任务才是最优解。

### [基本介绍](#基本介绍)

ScheduledThreadPoolExecutor继承自 ThreadPoolExecutor，为任务提供延迟或周期执行，属于线程池的一种。和 ThreadPoolExecutor 相比，它还具有以下几种特性:

- 使用专门的任务类型—ScheduledFutureTask 来执行周期任务，也可以接收不需要时间调度的任务(这些任务通过 ExecutorService 来执行)。

- 使用专门的存储队列—DelayedWorkQueue 来存储任务，DelayedWorkQueue 是无界延迟队列DelayQueue 的一种。相比ThreadPoolExecutor也简化了执行机制(delayedExecute方法，后面单独分析)。

- 支持可选的run-after-shutdown参数，在池被关闭(shutdown)之后支持可选的逻辑来决定是否继续运行周期或延迟任务。并且当任务(重新)提交操作与 shutdown 操作重叠时，复查逻辑也不相同。

### [基本使用](#基本使用)

ScheduledThreadPoolExecutor 最常见的应用场景就是实现调度任务，

#### [创建方式](#创建方式)

创建`ScheduledThreadPoolExecutor`方式一共有两种，第一种是通过自定义参数，第二种通过`Executors`工厂方法创建。 根据阿里巴巴代码规范中的建议，更加推荐使用第一种方式创建。

1. **自定义参数创建**

- `corePoolSize`：核心工作的线程数量

- `threadFactory`：线程工厂，用来创建线程

- `handler`: 拒绝策略，饱和策略

1. `Executors`**工厂方法创建**

- `static ScheduledExecutorService newScheduledThreadPool(int corePoolSize)`：根据核心线程数创建调度线程池。

- `static ScheduledExecutorService newScheduledThreadPool(int corePoolSize, ThreadFactory threadFactory)`：根据核心线程数和线程工厂创建调度线程池。

#### [核心API](#核心api)

1. `schedule(Runnable command, long delay, TimeUnit unit)`：创建并执行在给定延迟后启用的一次性操作

- `command`: 执行的任务

- `delay`：延迟的时间

- `unit`: 单位

1. `scheduleWithFixedDelay(Runnable command, long initialDelay, long delay, TimeUnit unit)`：定时执行周期任务，任务执行完成后，延迟delay时间执行

- `command`: 执行的任务

- `initialDelay`: 初始延迟的时间

- `delay`: 上次执行结束，延迟多久执行

- `unit`：单位

1. `scheduleAtFixedRate(Runnable command, long initialDelay, long period, TimeUnit unit)`：按照固定的评率定时执行周期任务，不受任务运行时间影响。

- `command`: 执行的任务

- `initialDelay`: 初始延迟的时间

- `period`: 周期

- `unit`：单位

#### [综合案例](#综合案例)

通过`ScheduledThreadPoolExecutor`实现每周四 18:00:00 定时执行任务。

## [底层源码解析](#底层源码解析)

接下来一起看看 ScheduledThreadPool 的底层源码

### [数据结构](#数据结构)
![](/imported/markdown/2025-05-17-markdown-80bc5d29-定时线程池全解析-从scheduledthreadpoolexecutor看高并发任务调度/images/329634f0a6a9-202404251124087.jpg)
ScheduledThreadPoolExecutor继承自 ThreadPoolExecutor:

ScheduledThreadPoolExecutor 内部构造了两个内部类 ScheduledFutureTask 和 DelayedWorkQueue:

- ScheduledFutureTask: 继承了FutureTask，说明是一个异步运算任务；最上层分别实现了Runnable、Future、Delayed接口，说明它是一个可以延迟执行的异步运算任务。

- DelayedWorkQueue: 这是 ScheduledThreadPoolExecutor 为存储周期或延迟任务专门定义的一个延迟队列，继承了 AbstractQueue，为了契合 ThreadPoolExecutor 也实现了 BlockingQueue 接口。它内部只允许存储 RunnableScheduledFuture 类型的任务。与 DelayQueue 的不同之处就是它只允许存放 RunnableScheduledFuture 对象，并且自己实现了二叉堆(DelayQueue 是利用了 PriorityQueue 的二叉堆结构)。

### [内部类ScheduledFutureTask](#内部类scheduledfuturetask)

#### [属性](#属性)

- sequenceNumber: 当两个任务有相同的延迟时间时，按照 FIFO 的顺序入队。sequenceNumber 就是为相同延时任务提供的顺序编号。

- time: 任务可以执行时的时间，纳秒级，通过triggerTime方法计算得出。

- period: 任务的执行周期时间，纳秒级。正数表示固定速率执行(为scheduleAtFixedRate提供服务)，负数表示固定延迟执行(为scheduleWithFixedDelay提供服务)，0表示不重复任务。

- outerTask: 重新入队的任务，通过reExecutePeriodic方法入队重新排序。

#### [核心方法run()](#核心方法run)

说明: ScheduledFutureTask 的run方法重写了 FutureTask 的版本，以便执行周期任务时重置/重排序任务。任务的执行通过父类 FutureTask 的run实现。内部有两个针对周期任务的方法:

- setNextRunTime(): 用来设置下一次运行的时间，源码如下:

- reExecutePeriodic(): 周期任务重新入队等待下一次执行，源码如下:

reExecutePeriodic与delayedExecute的执行策略一致，只不过reExecutePeriodic不会执行拒绝策略而是直接丢掉任务。

#### [cancel方法](#cancel方法)

ScheduledFutureTask.cancel本质上由其父类 FutureTask.cancel 实现。取消任务成功后会根据removeOnCancel参数决定是否从队列中移除此任务。

### [核心属性](#核心属性)

- continueExistingPeriodicTasksAfterShutdown：和executeExistingDelayedTasksAfterShutdown是 ScheduledThreadPoolExecutor 定义的 run-after-shutdown 参数，用来控制池关闭之后的任务执行逻辑。

- removeOnCancel：用来控制任务取消后是否从队列中移除。当一个已经提交的周期或延迟任务在运行之前被取消，那么它之后将不会运行。默认配置下，这种已经取消的任务在届期之前不会被移除。 通过这种机制，可以方便检查和监控线程池状态，但也可能导致已经取消的任务无限滞留。为了避免这种情况的发生，我们可以通过setRemoveOnCancelPolicy方法设置移除策略，把参数removeOnCancel设为true可以在任务取消后立即从队列中移除。

- sequencer：是为相同延时的任务提供的顺序编号，保证任务之间的 FIFO 顺序。与 ScheduledFutureTask 内部的sequenceNumber参数作用一致。

### [构造函数](#构造函数)

首先看下构造函数，ScheduledThreadPoolExecutor 内部有四个构造函数，这里我们只看这个最大构造灵活度的:

构造函数都是通过super调用了ThreadPoolExecutor的构造，并且使用特定等待队列DelayedWorkQueue。

### [Schedule](#schedule)

说明: schedule主要用于执行一次性(延迟)任务。函数执行逻辑分两步:

- 封装 Callable/Runnable

- 执行任务

说明: delayedExecute是执行任务的主方法，方法执行逻辑如下:

- 如果池已关闭(ctl &gt;= SHUTDOWN)，执行任务拒绝策略；

- 池正在运行，首先把任务入队排序；然后重新检查池的关闭状态，执行如下逻辑:

A: 如果池正在运行，或者 run-after-shutdown 参数值为true，则调用父类方法ensurePrestart启动一个新的线程等待执行任务。ensurePrestart源码如下:

ensurePrestart是父类 ThreadPoolExecutor 的方法，用于启动一个新的工作线程等待执行任务，即使corePoolSize为0也会安排一个新线程。

B: 如果池已经关闭，并且 run-after-shutdown 参数值为false，则执行父类(ThreadPoolExecutor)方法remove移除队列中的指定任务，成功移除后调用ScheduledFutureTask.cancel取消任务

### [scheduleAtFixedRate 和 scheduleWithFixedDelay](#scheduleatfixedrate-和-schedulewithfixeddelay)

说明: scheduleAtFixedRate和scheduleWithFixedDelay方法的逻辑与schedule类似。

**注意scheduleAtFixedRate和scheduleWithFixedDelay的区别**: 乍一看两个方法一模一样，其实，在unit.toNanos这一行代码中还是有区别的。没错，scheduleAtFixedRate传的是正值，而scheduleWithFixedDelay传的则是负值，这个值就是 ScheduledFutureTask 的period属性。

### [shutdown()](#shutdown)

说明: 池关闭方法调用了父类ThreadPoolExecutor的shutdown，具体分析见 ThreadPoolExecutor 篇。这里主要介绍以下在shutdown方法中调用的关闭钩子onShutdown方法，它的主要作用是在关闭线程池后取消并清除由于关闭策略不应该运行的所有任务，这里主要是根据 run-after-shutdown 参数(continueExistingPeriodicTasksAfterShutdown和executeExistingDelayedTasksAfterShutdown)来决定线程池关闭后是否关闭已经存在的任务。

## [ScheduledThreadPoolExecutor吞掉异常](#scheduledthreadpoolexecutor吞掉异常)

如果`ScheduledThreadPoolExecutor`中执行的任务出错抛出异常后，不仅不会打印异常堆栈信息，同时还会取消后面的调度, 直接看例子。
![](/imported/markdown/2025-05-17-markdown-80bc5d29-定时线程池全解析-从scheduledthreadpoolexecutor看高并发任务调度/images/1114559ba95e-202410211203134.png)

- 只执行了5次后，就不打印，不执行了，因为报错了

- 任务报错，也没有打印一次堆栈，更导致调度任务取消，后果十分严重。

解决方法也非常简单，只要通过try catch捕获异常即可。

### [原理探究](#原理探究)

那大家有没有想过为什么任务出错会导致异常无法打印，甚至调度都取消了呢？从源码出发，一探究竟。

从上面`delayedExecute`方法可以看到，延迟或周期性任务的主要执行方法， 主要是将任务丢到队列中，后续再由工作线程获取执行。

1. 在任务入队列后，就是执行任务内容了，任务内容其实就是在继承了Runnable类的run方法中。

- 这里的关键就是看`ScheduledFutureTask.super.runAndReset()`方法是否返回true，如果是true的话继续调度。

1. runAndReset方法也很简单，关键就是看报异常如何处理。

- 关键点ran变量，最终返回是不是下次继续调度执行

- 如果抛出异常的话，可以看到不会修改ran为true。

### [小结](#小结)

Java的ScheduledThreadPoolExecutor定时任务线程池所调度的任务中如果抛出了异常，并且异常没有捕获直接抛到框架中，会导致ScheduledThreadPoolExecutor定时任务不调度了。

## [封装包装类，统一调度](#封装包装类-统一调度)

在实际项目使用中，可以在自己的项目中封装一个包装类，要求所有的调度都提交通过统一的包装类，从而规范代码，如下代码：

当然，也还可以在包装类里面封装各种监控行为，如本例打印日志执行时间等。

## [其它使用注意点](#其它使用注意点)

1. 为什么ThreadPoolExecutor 的调整策略却不适用于 ScheduledThreadPoolExecutor？

由于 ScheduledThreadPoolExecutor 是一个固定核心线程数大小的线程池，并且使用了一个无界队列，所以调整maximumPoolSize对其没有任何影响(所以 ScheduledThreadPoolExecutor 没有提供可以调整最大线程数的构造函数，默认最大线程数固定为Integer.MAX_VALUE)。此外，设置corePoolSize为0或者设置核心线程空闲后清除(allowCoreThreadTimeOut)同样也不是一个好的策略，因为一旦周期任务到达某一次运行周期时，可能导致线程池内没有线程去处理这些任务。

1. Executors 提供了哪几种方法来构造 ScheduledThreadPoolExecutor？

- newScheduledThreadPool: 可指定核心线程数的线程池。

- newSingleThreadScheduledExecutor: 只有一个工作线程的线程池。如果内部工作线程由于执行周期任务异常而被终止，则会新建一个线程替代它的位置。

注意: newScheduledThreadPool(1, threadFactory) 不等价于newSingleThreadScheduledExecutor。newSingleThreadScheduledExecutor创建的线程池保证内部只有一个线程执行任务，并且线程数不可扩展；而通过newScheduledThreadPool(1, threadFactory)创建的线程池可以通过setCorePoolSize方法来修改核心线程数。
