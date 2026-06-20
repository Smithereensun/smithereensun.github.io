{

  "title": "FutureTask深度解析：异步任务的实现原理",
  "has_date": true,
  "description": "前言 Callable、Future和FutureTask是jdk1.5，java.util.concurrent包提供的异步框架 这里先讲一下什么是异步？异步是指起多个线程，多个线程之间互不干扰，各自执行各自的任务，在代码中可能书写顺序有先有后，但有可能写在后面的线程会比写在前面的线程先执行任务，",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/04-threadpool3-futuretask - FutureTask深度解析：异步任务的实现原理.md",
  "date": "2025-05-17"

}

## [前言](#前言)

Callable、Future和FutureTask是jdk1.5，java.util.concurrent包提供的异步框架

这里先讲一下什么是异步？异步是指起多个线程，多个线程之间互不干扰，各自执行各自的任务，在代码中可能书写顺序有先有后，但有可能写在后面的线程会比写在前面的线程先执行任务，异步对应并行的概念，常见的异步操作有线程池、Callable、completeFuture等。

同步是多线程里针对竞争现象的一个处理，竞争是指同一时刻有多个线程访问临界资源，可能会引发程序执行错误的结果，同步就是保证某一时刻仅能有一个线程访问临界资源，同步对应串行的概念，常见的同步操作有synchronized关键字、Lock、线程变量、Atomic原子类等。

什么时候需要异步？比如要执行一个任务，该任务执行完后会返回一个结果供其他任务使用，但是该任务很耗时，如果我们把程序设计成串行执行，先执行这个耗时任务，等他结束后再把执行结果给下一个任务使用，这样会耗时，且在这个任务执行期间，其他任务都被阻塞了。那么就可以把程序设计成异步，起一个线程执行这个耗时任务，此外主线程做其他事情，等这个耗时任务执行完毕后，主线程再把结果拿到，使用这个结果继续做其他事情，这样在这个耗时任务执行的过程中，主线程可以去做其他事情而不是等他执行完，这样效率会很高，因此异步编程在提高并发量上使用广泛。

### [Callable接口](#callable接口)

先看Callable接口的源码：

首先是注解是函数式接口，意味着可以用lambda表达式更简洁地使用它。Callable是个泛型接口，只有一个方法call，该方法返回类型就是传递进来的V类型。call方法还支持抛出异常.

与Callable对应的是Runnable接口，实现了这两个接口的类都可以当做线程任务递交给线程池执行，Runnable接口的源码如下：

既然实现了这两个接口的类都可以当做线程任务，那么这两个接口有什么区别呢？

1. Runnable接口是java1.1就有的，Callable接口是java1.5才有的，可以认为Callable接口是升级版的Runnable接口；

1. Runnable接口里线程任务是在run方法里写的，Callable接口里线程任务是在call方法里写；

1. Callable接口的任务执行后会有返回值，Runnable接口的任务无返回值（void）；

1. Callable接口的call方法支持抛出异常，Runnable接口的run方法不可以；

1. 加入线程池运行，Runnable使用ExecutorService的execute方法，Callable使用ExecutorService的submit方法；

1. 运行Callable任务可以拿到一个Future对象，表示异步计算的结果。Future对象封装了检查计算是否完成、检索计算的结果的方法，而Runnable接口没有。

Callable使用ExecutorService的submit方法，这里看一下ExecutorService接口里的submit方法的重载情况：

常用的是第一个和第三个，这两个方法分别提交实现了Callable接口的类和实现了Runnable接口的类作为线程任务，返回异步计算结果Future，Future里面封装了一些实用方法可以对异步计算结果进行进一步处理。

### [Future接口](#future接口)

Future接口代表异步计算的结果，通过Future接口提供的方法可以查看异步计算是否执行完成，或者等待执行结果并获取执行结果，同时还可以取消执行。Future接口的定义如下:

下面对这五个方法介绍：

1. cancel():用来取消异步任务的执行。如果异步任务已经完成或者已经被取消，或者由于某些原因不能取消，则会返回false。如果任务还没有被执行，则会返回true并且异步任务不会被执行。如果任务已经开始执行了但是还没有执行完成，若mayInterruptIfRunning为true，则会立即中断执行任务的线程并返回true，若mayInterruptIfRunning为false，则会返回true且不会中断任务执行线程。

1. isCanceled():判断任务是否被取消，如果任务在结束(正常执行结束或者执行异常结束)前被取消则返回true，否则返回false。

1. isDone():判断任务是否已经完成，如果完成则返回true，否则返回false。需要注意的是：任务执行过程中发生异常、任务被取消也属于任务已完成，也会返回true。

1. get():获取任务执行结果，如果任务还没完成则会**阻塞等待**直到任务执行完成。如果任务被取消则会抛出CancellationException异常，如果任务执行过程发生异常则会抛出ExecutionException异常，如果阻塞等待过程中被中断则会抛出InterruptedException异常。

1. get(long timeout,Timeunit unit):带超时时间的get()版本，如果阻塞等待过程中超时则会抛出TimeoutException异常。

注意这里两个get方法都会抛出异常。

### [FutureTask](#futuretask)

Future是一个接口，而FutureTask 为 Future 提供了基础实现，如获取任务执行结果(get)和取消任务(cancel)等。如果任务尚未完成，获取任务执行结果时将会阻塞。一旦执行结束，任务就不能被重启或取消(除非使用runAndReset执行计算)。FutureTask 常用来封装 Callable 和 Runnable，也可以作为一个任务提交到线程池中执行。除了作为一个独立的类之外，此类也提供了一些功能性函数供我们创建自定义 task 类使用。FutureTask 的线程安全由CAS来保证。

源码如下：

FutureTask类实现的是`RunnableFuture &lt;V&gt;`接口，该接口的源码如下：

该接口继承了Runnable接口和Future接口，因此FutureTask类既可以当做线程任务递交给线程池执行，又能当Callable任务的计算结果。

### [Future VS FutureTask](#future-vs-futuretask)

Future与FutureTask的区别：

1. Future是一个接口，FutureTask是一个实现类；

1. 使用Future初始化一个异步任务结果一般需要搭配线程池的submit，且submit方法有返回值；而初始化一个FutureTask对象需要传入一个实现了Callable接口的类的对象，直接将FutureTask对象submit给线程池，无返回值；

1. Future + Callable获取结果需要Future对象的get，而FutureTask获取结果直接用FutureTask对象的get方法即可。

## [使用示例](#使用示例)

### [Callable + Future](#callable-future)

实现Callable接口创建一个异步任务的类，在主线程中起一个线程池执行异步任务，然后在主线程里拿到异步任务的返回结果。

执行结果如下：

### [Callable + FutureTask](#callable-futuretask)

要做的事情跟4.1一样。

执行结果与4.1一样。

## [底层源码解析](#底层源码解析)

### [FutureTask类关系](#futuretask类关系)
![](/imported/markdown/2025-05-17-markdown-676608d0-futuretask深度解析-异步任务的实现原理/images/128686b98877-202404251132262.jpg)
可以看到,FutureTask实现了RunnableFuture接口，则RunnableFuture接口继承了Runnable接口和Future接口，所以FutureTask既能当做一个Runnable直接被Thread执行，也能作为Future用来得到Callable的计算结果。

### [核心属性](#核心属性)

其中需要注意的是state是volatile类型的，也就是说只要有任何一个线程修改了这个变量，那么其他所有的线程都会知道最新的值。7种状态具体表示：

- NEW:表示是个新的任务或者还没被执行完的任务。这是初始状态。

- COMPLETING:任务已经执行完成或者执行任务的时候发生异常，但是任务执行结果或者异常原因还没有保存到outcome字段(outcome字段用来保存任务执行结果，如果发生异常，则用来保存异常原因)的时候，状态会从NEW变更到COMPLETING。但是这个状态会时间会比较短，属于中间状态。

- NORMAL:任务已经执行完成并且任务执行结果已经保存到outcome字段，状态会从COMPLETING转换到NORMAL。这是一个最终态。

- EXCEPTIONAL:任务执行发生异常并且异常原因已经保存到outcome字段中后，状态会从COMPLETING转换到EXCEPTIONAL。这是一个最终态。

- CANCELLED:任务还没开始执行或者已经开始执行但是还没有执行完成的时候，用户调用了cancel(false)方法取消任务且不中断任务执行线程，这个时候状态会从NEW转化为CANCELLED状态。这是一个最终态。

- INTERRUPTING: 任务还没开始执行或者已经执行但是还没有执行完成的时候，用户调用了cancel(true)方法取消任务并且要中断任务执行线程但是还没有中断任务执行线程之前，状态会从NEW转化为INTERRUPTING。这是一个中间状态。

- INTERRUPTED:调用interrupt()中断任务执行线程之后状态会从INTERRUPTING转换到INTERRUPTED。这是一个最终态。 有一点需要注意的是，所有值大于COMPLETING的状态都表示任务已经执行完成(任务正常执行完成，任务执行异常或者任务被取消)。

各个状态之间的可能转换关系如下图所示:
![](/imported/markdown/2025-05-17-markdown-676608d0-futuretask深度解析-异步任务的实现原理/images/407435cd563a-202404251132264.jpg)
### [构造函数](#构造函数)

- FutureTask(Callable&lt;V&gt; callable)

这个构造函数会把传入的Callable变量保存在this.callable字段中，该字段定义为private Callable&lt;V&gt; callable;用来保存底层的调用，在被执行完成以后会指向null,接着会初始化state字段为NEW。

- FutureTask(Runnable runnable, V result)

这个构造函数会把传入的Runnable封装成一个Callable对象保存在callable字段中，同时如果任务执行成功的话就会返回传入的result。这种情况下如果不需要返回值的话可以传入一个null。

顺带看下Executors.callable()这个方法，这个方法的功能是把Runnable转换成Callable，代码如下:

可以看到这里采用的是适配器模式，调用RunnableAdapter&lt;T&gt;(task, result)方法来适配，实现如下:

这个适配器很简单，就是简单的实现了Callable接口，在call()实现中调用Runnable.run()方法，然后把传入的result作为任务的结果返回。

在new了一个FutureTask对象之后，接下来就是在另一个线程中执行这个Task,无论是通过直接new一个Thread还是通过线程池，执行的都是run()方法，接下来就看看run()方法的实现。

### [核心方法 - run()](#核心方法-run)

**说明：**

- 运行任务，如果任务状态为NEW状态，则利用CAS修改为当前线程。执行完毕调用set(result)方法设置执行结果。set(result)源码如下：

- 首先利用cas修改state状态为COMPLETING，设置返回结果，然后使用 lazySet(UNSAFE.putOrderedInt)的方式设置state状态为NORMAL。结果设置完毕后，调用finishCompletion()方法唤醒等待线程，源码如下：

- 回到run方法，如果在 run 期间被中断，此时需要调用handlePossibleCancellationInterrupt方法来处理中断逻辑，确保任何中断(例如cancel(true))只停留在当前run或runAndReset的任务中，源码如下：

### [核心方法 - get()](#核心方法-get)

说明：FutureTask 通过get()方法获取任务执行结果。如果任务处于未完成的状态(state &lt;= COMPLETING)，就调用awaitDone方法(后面单独讲解)等待任务完成。任务完成后，通过report方法获取执行结果或抛出执行期间的异常。report源码如下：

### [核心方法 - awaitDone(boolean timed, long nanos)](#核心方法-awaitdone-boolean-timed-long-nanos)

说明：awaitDone用于等待任务完成，或任务因为中断或超时而终止。返回任务的完成状态。函数执行逻辑如下：

如果线程被中断，首先清除中断状态，调用removeWaiter移除等待节点，然后抛出InterruptedException。removeWaiter源码如下：

- 如果当前状态为结束状态(state&gt;COMPLETING),则根据需要置空等待节点的线程，并返回 Future 状态；

- 如果当前状态为正在完成(COMPLETING)，说明此时 Future 还不能做出超时动作，为任务让出CPU执行时间片；

- 如果state为NEW，先新建一个WaitNode，然后CAS修改当前waiters；

- 如果等待超时，则调用removeWaiter移除等待节点，返回任务状态；如果设置了超时时间但是尚未超时，则park阻塞当前线程；

- 其他情况直接阻塞当前线程。

### [核心方法 - cancel(boolean mayInterruptIfRunning)](#核心方法-cancel-boolean-mayinterruptifrunning)

说明：尝试取消任务。如果任务已经完成或已经被取消，此操作会失败。

- 如果当前Future状态为NEW，根据参数修改Future状态为INTERRUPTING或CANCELLED。

- 如果当前状态不为NEW，则根据参数mayInterruptIfRunning决定是否在任务运行中也可以中断。中断操作完成后，调用finishCompletion移除并唤醒所有等待线程
