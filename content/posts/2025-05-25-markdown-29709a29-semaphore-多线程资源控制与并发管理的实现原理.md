{

  "title": "Semaphore：多线程资源控制与并发管理的实现原理",
  "has_date": true,
  "description": "介绍 信号量 Semaphore类似于锁，它用于控制同时访问特定资源的线程数量，控制并发线程数。 运行结果如下，可以看出并非按照线程访问顺序获取资源的锁，即 应用场景**：Semaphore可以用于做流量控制，特别是公共资源有限的应用场景，比如数据库连接。假如有一个需求要读取几万个文件的数据，因为都",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/05-concurrenttools3-semaphore - Semaphore：多线程资源控制与并发管理的实现原理.md",
  "date": "2025-05-25"

}

## [介绍](#介绍)

信号量

Semaphore类似于锁，它用于控制同时访问特定资源的线程数量，控制并发线程数。
![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/7657f708ac1c-202404251545639.gif)
运行结果如下，可以看出并非按照线程访问顺序获取资源的锁，即

**应用场景**：Semaphore可以用于做流量控制，特别是公共资源有限的应用场景，比如数据库连接。假如有一个需求要读取几万个文件的数据，因为都是IO密集型任务，可以启动几十个线程并发地读取，读到内存中后，还需要存储到数据库中，而数据库的连接数只有10个，那么就可以控制这几十个线程只有10个线程同时获取数据库连接来保存数据。这个时候，就可以使用Semaphore来做流量控制。

### [基本概念](#基本概念)

- 许可(Permits)：表示可以访问资源的线程数量。semaphore 对象内部维护了一个许可计数器，线程在访问资源时需要获取许可，访问完成后需要释放许可。

- 获取许可(Acquire)：线程通过acquire()方法尝试获取许可。如果没有足够的许可，线程将被阻塞直到有许可可用。

- 释放许可(Release)：线程在完成对共享资源的访问后，通过 release()方法释放许可，使其他等待的线程可以获取许可。

它支持公平与非公平策略:

- 公平(Fair)：在公平模式下，线程按照请求许可的顺序获取许可，防止线程饥饿。但公平模式可能会导致性能下降。

- 非公平(Unfair)：非公平模式下，线程不保证按照请求许可的顺序获取许可，可以提高性能，但可能会导致某些线程长时间无法获取许可,

### [常见用法](#常见用法)

限制访问数量：例如，限制数据库连接池中最大连接数。

控制并发执行：例如，限制同时执行的任务数量

## [Semaphore源码分析](#semaphore源码分析)

### [类的继承关系](#类的继承关系)

说明: Semaphore实现了Serializable接口，即可以进行序列化。
![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/a3dbd8086a6c-202404251545649.gif)
### [类的内部类](#类的内部类)

Semaphore总共有三个内部类，并且三个内部类是紧密相关的，下面先看三个类的关系。
![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/a910d670be6b-202404251545644.jpg)
说明: Semaphore与ReentrantLock的内部类的结构相同，类内部总共存在Sync、NonfairSync、FairSync三个类，NonfairSync与FairSync类继承自Sync类，Sync类继承自AbstractQueuedSynchronizer抽象类。下面逐个进行分析。

### [类的内部类 - Sync类](#类的内部类-sync类)

Sync类的源码如下

说明: Sync类的属性相对简单，只有一个版本号，Sync类存在如下方法和作用如下。
![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/b5e9bce7067a-202404251545646.jpg)
### [类的内部类 - NonfairSync类](#类的内部类-nonfairsync类)

NonfairSync类继承了Sync类，表示采用非公平策略获取资源，其只有一个tryAcquireShared方法，重写了AQS的该方法，其源码如下:

说明: 从tryAcquireShared方法的源码可知，其会调用父类Sync的nonfairTryAcquireShared方法，表示按照非公平策略进行资源的获取。

### [类的内部类 - FairSync类](#类的内部类-fairsync类)

FairSync类继承了Sync类，表示采用公平策略获取资源，其只有一个tryAcquireShared方法，重写了AQS的该方法，其源码如下。

说明: 从tryAcquireShared方法的源码可知，它使用公平策略来获取资源，它会判断同步队列中是否存在其他的等待节点。

### [类的属性](#类的属性)

说明: Semaphore自身只有两个属性，最重要的是sync属性，基于Semaphore对象的操作绝大多数都转移到了对sync的操作。

### [类的构造函数](#类的构造函数)

- Semaphore(int)型构造函数

说明: 该构造函数会创建具有给定的许可数和非公平的公平设置的Semaphore。

- Semaphore(int, boolean)型构造函数

说明: 该构造函数会创建具有给定的许可数和给定的公平设置的Semaphore。

### [核心函数分析 - acquire函数](#核心函数分析-acquire函数)

此方法从信号量获取一个(多个)许可，在提供一个许可前一直将线程阻塞，或者线程被中断，其源码如下

说明: 该方法中将会调用Sync对象的acquireSharedInterruptibly(从AQS继承而来的方法)方法，而acquireSharedInterruptibly方法在CountDownLatch中已经进行了分析，在此不再累赘。

最终可以获取大致的方法调用序列(假设使用非公平策略)。如下图所示。
![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/79922021c5f9-202404251545659.jpg)
说明: 上图只是给出了大体会调用到的方法，和具体的示例可能会有些差别，之后会根据具体的示例进行分析。

### [核心函数分析 - release函数](#核心函数分析-release函数)

此方法释放一个(多个)许可，将其返回给信号量，源码如下。

说明: 该方法中将会调用Sync对象的releaseShared(从AQS继承而来的方法)方法，而releaseShared方法在上一篇CountDownLatch中已经进行了分析，在此不再累赘。

最终可以获取大致的方法调用序列(假设使用非公平策略)。如下图所示:
![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/e599508c8b16-202404251545657.jpg)
说明: 上图只是给出了大体会调用到的方法，和具体的示例可能会有些差别。

## [Semaphore示例](#semaphore示例)

下面给出了一个使用Semaphore的示例。

说明: 首先，生成一个信号量，信号量有10个许可，然后，main，t1，t2三个线程获取许可运行，根据结果，可能存在如下的一种时序。
![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/44920f88e99b-202404251545378.jpg)
说明: 如上图所示，首先，main线程执行acquire操作，并且成功获得许可，之后t1线程执行acquire操作，成功获得许可，之后t2执行acquire操作，由于此时许可数量不够，t2线程将会阻塞，直到许可可用。之后t1线程释放许可，main线程释放许可，此时的许可数量可以满足t2线程的要求，所以，此时t2线程会成功获得许可运行，t2运行完成后释放许可。下面进行详细分析。

- main线程执行semaphore.acquire操作。主要的函数调用如下图所示。

![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/bfe9f3333956-202404251545399.jpg)
说明: 此时，可以看到只是AQS的state变为了5，main线程并没有被阻塞，可以继续运行。

- t1线程执行semaphore.acquire操作。主要的函数调用如下图所示。

![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/20d9f4875e3b-202404251545418.jpg)
说明: 此时，可以看到只是AQS的state变为了2，t1线程并没有被阻塞，可以继续运行。

- t2线程执行semaphore.acquire操作。主要的函数调用如下图所示。

![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/c9380cda81be-202404251545445.jpg)
说明: 此时，t2线程获取许可不会成功，之后会导致其被禁止运行，值得注意的是，AQS的state还是为2。

- t1执行semaphore.release操作。主要的函数调用如下图所示。

![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/1a5339da8f26-202404251545468.jpg)
说明: 此时，t2线程将会被unpark，并且AQS的state为5，t2获取cpu资源后可以继续运行。

- main线程执行semaphore.release操作。主要的函数调用如下图所示。

![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/4eee8d8f5259-202404251545490.jpg)
说明: 此时，t2线程还会被unpark，但是不会产生影响，此时，只要t2线程获得CPU资源就可以运行了。此时，AQS的state为10。

- t2获取CPU资源，继续运行，此时t2需要恢复现场，回到parkAndCheckInterrupt函数中，也是在should继续运行。主要的函数调用如下图所示。

![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/6af3110032cb-202404251545290.jpg)
说明: 此时，可以看到，Sync queue中只有一个结点，头节点与尾节点都指向该结点，在setHeadAndPropagate的函数中会设置头节点并且会unpark队列中的其他结点。

- t2线程执行semaphore.release操作。主要的函数调用如下图所示。

![](/imported/markdown/2025-05-25-markdown-29709a29-semaphore-多线程资源控制与并发管理的实现原理/images/ee169c2aebfc-202404251545309.jpg)
说明: t2线程经过release后，此时信号量的许可又变为10个了，此时Sync queue中的结点还是没有变化。

## [注意](#注意)

不同于CyclicBarrier和ReentrantLock，单独使用Semaphore是不会使用到AQS的条件队列的，其实，只有进行await操作才会进入条件队列，其他的都是在同步队列中，只是当前线程会被park。

## [场景问题](#场景问题)

1.
semaphore初始化有10个令牌，11个线程同时各调用1次acquire方法，会发生什么?

  - 答案：拿不到令牌的线程阻塞，不会继续往下运行。

1.
semaphore初始化有10个令牌，一个线程重复调用11次acquire方法，会发生什么?

  - 答案：线程阻塞，不会继续往下运行。可能你会考虑类似于锁的重入的问题，很好，但是，令牌没有重入的概念。你只要调用一次acquire方法，就需要有一个令牌才能继续运行。

1.
semaphore初始化有1个令牌，1个线程调用一次acquire方法，然后调用两次release方法，之后另外一个线程调用acquire(2)方法，此线程能够获取到足够的令牌并继续运行吗?

  - 答案：能，原因是release方法会添加令牌，并不会以初始化的大小为准。

1.
semaphore初始化有2个令牌，一个线程调用1次release方法，然后一次性获取3个令牌，会获取到吗?

  - 答案：能，原因是release会添加令牌，并不会以初始化的大小为准。Semaphore中release方法的调用并没有限制要在acquire后调用。

具体示例如下，如果不相信的话，可以运行一下下面的demo。
