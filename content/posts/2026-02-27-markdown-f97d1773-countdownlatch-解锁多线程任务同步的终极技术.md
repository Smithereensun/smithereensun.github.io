{

  "title": "CountDownLatch：解锁多线程任务同步的终极技术",
  "has_date": true,
  "description": "介绍 CountDownLatch用于某个线程等待其他线程**执行完任务**再执行，与thread.join()功能类似。常见的应用场景是开启多个线程同时执行某个任务，等到所有任务执行完再执行特定操作，如汇总统计结果。 主要功能: 等待事件完成：通过 await()方法，线程可以等待其他线程完成某些",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/05-concurrenttools1-countdownlatch - CountDownLatch：解锁多线程任务同步的终极技术.md",
  "date": "2026-02-27"

}

## [介绍](#介绍)

CountDownLatch用于某个线程等待其他线程**执行完任务**再执行，与thread.join()功能类似。常见的应用场景是开启多个线程同时执行某个任务，等到所有任务执行完再执行特定操作，如汇总统计结果。

主要功能:

1. 等待事件完成：通过 await()方法，线程可以等待其他线程完成某些操作。

1. 递减计数器：其他线程在完成各自的任务后，通过调用 countDown()方法将计数器减 1。

1. 线程同步：当计数器变为 0 时，所有调用了await()的线程将被唤醒并继续执行。

### [面试题：如何能够保证T2在T1执行完后执行，T3在T2执行完后执行？](#面试题-如何能够保证t2在t1执行完后执行-t3在t2执行完后执行)

#### [join方法](#join方法)

可以使用join方法解决这个问题。比如在线程A中，调用线程B的join方法表示的意思就是： **A等待B线程执行完毕后（释放CPU执行权），再继续执行。**

#### [CountDownLatch](#countdownlatch)

倒计时计数器

CountDownLatch用于某个线程等待其他线程执行完任务再执行，可以被认为是加强版的join()。

调用了await后，主线程被挂起，它会等待直到count值为0才继续执行;因此只影响主线程的执行顺序一定要在T1 T2 T3之后，但T1 T2 T3之间的顺序互不影响

**应用场景:** 开启多个线程同时执行某个任务，等到所有任务执行完再执行特定操作，如汇总统计结果。

#### [两者区别](#两者区别)

相同点：都能等待一个或者多个线程执行完成操作,比如等待三个线程执行完毕后,第四个线程才能执行

不同点：join能让线程按我们预想的的顺序执行，比如线程1执行完了，线程2才能执行，线程2执行完,线程3才能执行，但是CountDownLatch就做不到.

当调用CountDownLatch的countDown方法时，N就会减1,CountDownLatch的await方法会阻塞当前线程，直到N变为零(也就是线程都执行完了)，由于countDown方法可以用在任何地方，**所以这里说的N个点，可以是N个线程，也可以是1个线程里的N个执行步骤**。用在多线程时,只需把这个CountDownLatch的引用传递到线程中即可

### [工作原理](#工作原理)

其底层是由AQS提供支持，所以其数据结构可以参考AQS的数据结构，而AQS的数据结构核心就是两个虚拟队列: 同步队列sync queue 和条件队列condition queue，不同的条件会有不同的条件队列。

CountDownLatch对AQS的共享方式实现为：CountDownLatch 将任务分为N个子线程去执行，将 state 初始化为 N, N与线程的个数一致，N个子线程是井行执行的，每个子线程都在执行完成后 countDown() 1次， state 执行 CAS 操作并减1。在所有子线程都执行完成(state=0)时会unpark()主线程，然后主线程会从 await()返回，继续执行后续的动作。
![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/e8e9001152c6-202404251531808.gif)
## [CountDownLatch源码分析](#countdownlatch源码分析)

### [类的继承关系](#类的继承关系)

CountDownLatch没有显示继承哪个父类或者实现哪个父接口, 它底层是AQS是通过内部类Sync来实现的。
![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/5cee4fdc954d-202404251531817.gif)
### [类的内部类](#类的内部类)

CountDownLatch类存在一个内部类Sync，继承自AbstractQueuedSynchronizer，其源代码如下。

说明: 对CountDownLatch方法的调用会转发到对Sync或AQS的方法的调用，所以，AQS对CountDownLatch提供支持。

### [类的属性](#类的属性)

可以看到CountDownLatch类的内部只有一个Sync类型的属性:

### [类的构造函数](#类的构造函数)

说明: 该构造函数可以构造一个用给定计数初始化的CountDownLatch，并且构造函数内完成了sync的初始化，并设置了状态数。

### [核心函数 - await函数](#核心函数-await函数)

此函数将会使当前线程在锁存器倒计数至零之前一直等待，除非线程被中断。其源码如下

说明: 由源码可知，对CountDownLatch对象的await的调用会转发为对Sync的acquireSharedInterruptibly(从AQS继承的方法)方法的调用。

- acquireSharedInterruptibly源码如下:

说明: 从源码中可知，acquireSharedInterruptibly又调用了CountDownLatch的内部类Sync的tryAcquireShared和AQS的doAcquireSharedInterruptibly函数。

- tryAcquireShared函数的源码如下:

说明: 该函数只是简单的判断AQS的state是否为0，为0则返回1，不为0则返回-1。

- doAcquireSharedInterruptibly函数的源码如下:

说明: 在AQS的doAcquireSharedInterruptibly中可能会再次调用CountDownLatch的内部类Sync的tryAcquireShared方法和AQS的setHeadAndPropagate方法。

- setHeadAndPropagate方法源码如下。

说明: 该方法设置头节点并且释放头节点后面的满足条件的结点，该方法中可能会调用到AQS的doReleaseShared方法，其源码如下。

说明: 该方法在共享模式下释放。

所以，对CountDownLatch的await调用大致会有如下的调用链。
![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/2fe06d1fd1a3-202404251531813.jpg)
说明: 上图给出了可能会调用到的主要方法，并非一定会调用到

### [核心函数 - countDown函数](#核心函数-countdown函数)

此函数将递减锁存器的计数，如果计数到达零，则释放所有等待的线程

说明: 对countDown的调用转换为对Sync对象的releaseShared(从AQS继承而来)方法的调用。

- releaseShared源码如下

说明: 此函数会以共享模式释放对象，并且在函数中会调用到CountDownLatch的tryReleaseShared函数，并且可能会调用AQS的doReleaseShared函数。

- tryReleaseShared源码如下

说明: 此函数会试图设置状态来反映共享模式下的一个释放。具体的流程在下面的示例中会进行分析。

- AQS的doReleaseShared的源码如下

说明: 此函数在共享模式下释放资源。

所以，对CountDownLatch的countDown调用大致会有如下的调用链
![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/eca7c27ecbda-202404251531812.jpg)
## [示例](#示例)

下面给出了一个使用CountDownLatch的示例。

运行结果(某一次):

说明: 本程序首先计数器初始化为2。根据结果，可能会存在如下的一种时序图。
![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/31e1b6276925-202404251531815.jpg)
说明: 首先main线程会调用await操作，此时main线程会被阻塞，等待被唤醒，之后t1线程执行了countDown操作，最后，t2线程执行了countDown操作，此时main线程就被唤醒了，可以继续运行。下面，进行详细分析。

- main线程执行countDownLatch.await操作，主要调用的函数如下。

![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/cb6f89edff5f-202404251531822.jpg)
说明: 在最后，main线程就被park了，即禁止运行了。此时Sync queue(同步队列)中有两个节点，AQS的state为2，包含main线程的结点的nextWaiter指向SHARED结点。

- t1线程执行countDownLatch.countDown操作，主要调用的函数如下。

![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/bcfd2fa4d7bf-202404251531424.jpg)
说明: 此时，Sync queue队列里的结点个数未发生变化，但是此时，AQS的state已经变为1了。

- t2线程执行countDownLatch.countDown操作，主要调用的函数如下。

![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/41860d6b9d9d-202404251531440.jpg)
说明: 经过调用后，AQS的state为0，并且此时，main线程会被unpark，可以继续运行。当main线程获取cpu资源后，继续运行。

- main线程获取cpu资源，继续运行，由于main线程是在parkAndCheckInterrupt函数中被禁止的，所以此时，继续在parkAndCheckInterrupt函数运行。

![](/imported/markdown/2026-02-27-markdown-f97d1773-countdownlatch-解锁多线程任务同步的终极技术/images/50fdaefa9587-202404251531538.jpg)
说明: main线程恢复，继续在parkAndCheckInterrupt函数中运行，之后又会回到最终达到的状态为AQS的state为0，并且head与tail指向同一个结点，该节点的额nextWaiter域还是指向SHARED结点
