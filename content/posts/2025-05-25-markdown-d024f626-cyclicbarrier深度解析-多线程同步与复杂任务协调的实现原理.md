{

  "title": "CyclicBarrier深度解析：多线程同步与复杂任务协调的实现原理",
  "has_date": true,
  "description": "介绍 循环屏障。 应用场景：CyclicBarrier可以用于多线程计算数据，最后合并计算结果的场景。例如，用一个Excel保存了用户所有银行流水，每个Sheet保存一个账户近一年的每笔银行流水，现在需要统计用户的日均银行流水，先用多线程处理每个sheet里的银行流水，都执行完之后，得到每个shee",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/05-concurrenttools2-cyclicbarrier - CyclicBarrier深度解析：多线程同步与复杂任务协调的实现原理.md",
  "date": "2025-05-25"

}

## [介绍](#介绍)

循环屏障。

应用场景：CyclicBarrier可以用于多线程计算数据，最后合并计算结果的场景。例如，用一个Excel保存了用户所有银行流水，每个Sheet保存一个账户近一年的每笔银行流水，现在需要统计用户的日均银行流水，先用多线程处理每个sheet里的银行流水，都执行完之后，得到每个sheet的日均银行流水，最后，再用barrierAction根据这些线程的计算结果，计算出整个Excel的日均银行流水。

用法：让一组线程到达一个屏障（也可以叫同步点）时被阻塞，直到最后一个线程到达屏障时，屏障才会开门，所有被屏障拦截的线程才会继续执行。**也就是说，一组线程互相等待到某个状态，然后这组线程再同时执行**。

这个屏障之所以用循环修饰，是因为在所有的线程释放彼此之后，这个屏障是可以重新使用的（reset()方法重置屏障点）。这一点与CountDownLatch不同。

### [基本概念](#基本概念)

- 屏障(Barrier)：一个线程在调用 await()方法时会被阻塞，直到所有参与的线程都到达屏障点。屏障点可以是一个特定的任务步骤。

- 线程数量: cyclicBarrier 需要的线程数量是预设的，当所有线程都到达屏障时，屏障被释放，所有线程可以继续执行。

- 重用性: cyclicBarrier 可以被重用，允许在多个阶段中同步线程。例如，在每个阶段的同步点上都可以使用 cyclicBarrier 。

构造函数
 cyclicBarrier(int parties)：初始化一个 cyclicBarrier 对象，设置需要等待的线程数量
 cyclicBarrier(int parties,Runnable barrierAction):除了设置线程数量外，还可以指定一个 Runnable 回调，在所有线程到达屏障后执行。

### [工作原理](#工作原理)
![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/5e8cfdc9ae7a-202505251601285.png)
它实际上是基于 ReentrantLock 和 Condition 的封装来实现这一功能的。

cyclicearier 内部维护了一个计数器，即达到屏障的线程数量，当线程调用 await 的时候计数器会减一，如果计数器减一不等于0的时候，线程会调用 condition.await 进行阻塞等待。

如果计数器减一的值等于0，说明最后一个线程也到达了屏違，于是如果有 barrierAction就执行 barrierAction，然后调用condition.signalAl唤醒之前等待的线程，并且重置计数器，然后开启下一代，所以它可以循环使用。

### [使用示例](#使用示例)

参数parties指让多少个线程或者任务等待至某个状态；参数barrierAction为当这些线程都达到某个状态时会执行的内容。

运行结果如下，可以看出CyclicBarrier是可以重用的：

当四个线程都到达barrier状态后，会从四个线程中选择一个线程去执行Runnable。

## [CyclicBarrier源码分析](#cyclicbarrier源码分析)

### [类的继承关系](#类的继承关系)

CyclicBarrier没有显示继承哪个父类或者实现哪个父接口, 所以他对AQS和重入锁不是通过继承实现的，而是通过组合实现的。

### [类的内部类](#类的内部类)

CyclicBarrier类存在一个内部类Generation，每一次使用的CycBarrier可以当成Generation的实例，其源代码如下

说明: Generation类有一个属性broken，用来表示当前屏障是否被损坏。

### [类的属性](#类的属性)

说明: 该属性有一个为ReentrantLock对象，有一个为Condition对象，而Condition对象又是基于AQS的，所以，归根到底，底层还是由AQS提供支持。

### [类的构造函数](#类的构造函数)

- CyclicBarrier(int, Runnable)型构造函数

说明: 该构造函数可以指定关联该CyclicBarrier的线程数量，并且可以指定在所有线程都进入屏障后的执行动作，该执行动作由最后一个进行屏障的线程执行。

- CyclicBarrier(int)型构造函数

说明: 该构造函数仅仅执行了关联该CyclicBarrier的线程数量，没有设置执行动作。

### [核心函数 - dowait函数](#核心函数-dowait函数)

此函数为CyclicBarrier类的核心函数，CyclicBarrier类对外提供的await函数在底层都是调用该了doawait函数，其源代码如下。

说明: dowait方法的逻辑会进行一系列的判断，大致流程如下:
![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/344a5d3e222a-202404251539583.jpg)
### [核心函数 - nextGeneration函数](#核心函数-nextgeneration函数)

此函数在所有线程进入屏障后会被调用，即生成下一个版本，所有线程又可以重新进入到屏障中，其源代码如下

在此函数中会调用AQS的signalAll方法，即唤醒所有等待线程。如果所有的线程都在等待此条件，则唤醒所有线程。其源代码如下

说明: 此函数判断头节点是否为空，即条件队列是否为空，然后会调用doSignalAll函数，doSignalAll函数源码如下

说明: 此函数会依次将条件队列中的节点转移到同步队列中，会调用到transferForSignal函数，其源码如下

说明: 此函数的作用就是将处于条件队列中的节点转移到同步队列中，并设置结点的状态信息，其中会调用到enq函数，其源代码如下。

说明: 此函数完成了结点插入同步队列的过程，也很好理解。

综合上面的分析可知，newGeneration函数的主要方法的调用如下:
![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/5a14853aaaf7-202404251539584.jpg)
### [breakBarrier函数](#breakbarrier函数)

此函数的作用是损坏当前屏障，会唤醒所有在屏障中的线程。源代码如下:

说明: 可以看到，此函数也调用了AQS的signalAll函数，由signal函数提供支持

## [CyclicBarrier原理示例](#cyclicbarrier原理示例)

下面通过一个例子来详解CyclicBarrier的使用和内部工作机制，源代码如下

说明: 根据结果可知，可能会存在如下的调用时序。
![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/fc76f4fe4873-202404251539586.jpg)
说明: 由上图可知，假设t1线程的cb.await是在main线程的cb.barrierAction动作是由最后一个进入屏障的线程执行的。根据时序图，进一步分析出其内部工作流程。

- main(主)线程执行cb.await操作，主要调用的函数如下。

![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/547c04aef5ac-202404251539589.jpg)
说明: 由于ReentrantLock的默认采用非公平策略，所以在dowait函数中调用的是ReentrantLock.NonfairSync的lock函数，由于此时AQS的状态是0，表示还没有被任何线程占用，故main线程可以占用，之后在dowait中会调用trip.await函数，最终的结果是条件队列中存放了一个包含main线程的结点，并且被禁止运行了，同时，main线程所拥有的资源也被释放了，可以供其他线程获取。

- t1线程执行cb.await操作，其中假设t1线程的lock.lock操作在main线程释放了资源之后，则其主要调用的函数如下。

![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/75fa2a1f24a6-202404251539592.jpg)
说明: 可以看到，之后condition queue(条件队列)里面有两个节点，包含t1线程的结点插入在队列的尾部，并且t1线程也被禁止了，因为执行了park操作，此时两个线程都被禁止了。

- t2线程执行cb.await操作，其中假设t2线程的lock.lock操作在t1线程释放了资源之后，则其主要调用的函数如下。

![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/048249ec63ec-202404251539390.jpg)
说明: 由上图可知，在t2线程执行await操作后，会直接执行command.run方法，不是重新开启一个线程，而是最后进入屏障的线程执行。同时，会将Condition queue中的所有节点都转移到Sync queue中，并且最后main线程会被unpark，可以继续运行。main线程获取cpu资源，继续运行。

- main线程获取cpu资源，继续运行，下图给出了主要的方法调用:

![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/fa863d62f1b3-202404251539412.jpg)
说明: 其中，由于main线程是在AQS.CO的wait中被park的，所以恢复时，会继续在该方法中运行。运行过后，t1线程被unpark，它获得cpu资源可以继续运行。

- t1线程获取cpu资源，继续运行，下图给出了主要的方法调用。

![](/imported/markdown/2025-05-25-markdown-d024f626-cyclicbarrier深度解析-多线程同步与复杂任务协调的实现原理/images/4e2745d62146-202404251539434.jpg)
说明: 其中，由于t1线程是在AQS.CO的wait方法中被park，所以恢复时，会继续在该方法中运行。运行过后，Sync queue中保持着一个空节点。头节点与尾节点均指向它。

注意: 在线程await过程中中断线程会抛出异常，所有进入屏障的线程都将被释放。至于CyclicBarrier的其他用法，读者可以自行查阅API，不再累赘。

## [和CountDownLatch的区别](#和countdownlatch的区别)

1.
CyclicBarrier 和 CountDownLatch 都能够实现线程之间的等待

- CountDownLatch简单的说就是一个线程等待，直到他所等待的其他线程都执行完成并且调用countDown()方法发出通知后，当前线程才可以继续执行。

- cyclicBarrier是所有线程都进行等待，直到所有线程都准备好进入await()方法之后，所有线程同时开始执行！

1.
CountDownLatch减计数，CyclicBarrier加计数。

1.
CountDownLatch是一次性的，CyclicBarrier可以重用。CyclicBarrier的计数器可以使用reset() 方法重置。所以CyclicBarrier能处理更为复杂的业务场景，比如如果计算发生错误，可以重置计数器，并让线程们重新执行一次。
