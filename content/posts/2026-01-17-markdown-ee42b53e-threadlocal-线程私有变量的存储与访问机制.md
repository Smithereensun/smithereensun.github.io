{

  "title": "ThreadLocal：线程私有变量的存储与访问机制",
  "has_date": true,
  "description": "概述 线程本地变量。当使用 ThreadLocal 维护变量时， ThreadLocal 为每个使用该变量的线程提供独立的变量副本，所以每一个线程都可以独立地改变自己的副本，而不会影响其它线程。 每个线程都有一个 ThreadLocalMap （ ThreadLocal 内部类），Map中元素的**",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/06-threadlocal - ThreadLocal：线程私有变量的存储与访问机制.md",
  "date": "2026-01-17"

}

## [概述](#概述)

线程本地变量。当使用 ThreadLocal 维护变量时， ThreadLocal 为每个使用该变量的线程提供独立的变量副本，所以每一个线程都可以独立地改变自己的副本，而不会影响其它线程。

每个线程都有一个 ThreadLocalMap （ ThreadLocal 内部类），Map中元素的**键为 ThreadLocal**，而值对应线程的变量副本。
![](/imported/markdown/2026-01-17-markdown-ee42b53e-threadlocal-线程私有变量的存储与访问机制/images/4a0ddd1f3374-202404251607824.gif)
## [ThreadLocal原理](#threadlocal原理)

### [如何实现线程隔离](#如何实现线程隔离)

具体关于为线程分配变量副本的代码如下:

- 首先获取当前线程对象t, 然后从线程t中获取到ThreadLocalMap的成员属性threadLocals

- 如果当前线程的threadLocals已经初始化(即不为null) 并且存在以当前ThreadLocal对象为Key的值, 则直接返回当前线程要获取的对象(本例中为Connection);

- 如果当前线程的threadLocals已经初始化(即不为null)但是不存在以当前ThreadLocal对象为Key的的对象, 那么重新创建一个Connection对象, 并且添加到当前线程的threadLocals Map中,并返回

- 如果当前线程的threadLocals属性还没有被初始化, 则重新创建一个ThreadLocalMap对象, 并且创建一个Connection对象并添加到ThreadLocalMap对象中并返回。

如果存在则直接返回很好理解, 那么对于如何初始化的代码又是怎样的呢?

- 首先调用上面写的重载过后的initialValue方法

- 继续查看当前线程的threadLocals是不是空的, 如果ThreadLocalMap已被初始化, 那么直接将产生的对象添加到ThreadLocalMap中, 如果没有初始化, 则创建并添加对象到其中;

同时, ThreadLocal还提供了直接操作Thread对象中的threadLocals的方法

这样也可以不实现initialValue:

看过代码之后就很清晰的知道了为什么ThreadLocal能够实现变量的多线程隔离了; 其实就是用了Map的数据结构给当前线程缓存了, 要使用的时候就从本线程的threadLocals对象中获取就可以了, key就是当前线程;

当然了在当前线程下获取当前线程里面的Map里面的对象并操作肯定没有线程并发问题了, 当然能做到变量的线程间隔离了;

### [ThreadLocalMap对象是什么](#threadlocalmap对象是什么)

本质上来讲, 它就是一个Map, 但是这个ThreadLocalMap与平时见到的Map有点不一样

- 它没有实现Map接口;

- 它没有public的方法, 最多有一个default的构造方法, 因为这个ThreadLocalMap的方法仅仅在ThreadLocal类中调用, 属于静态内部类

- ThreadLocalMap的Entry实现继承了WeakReference&lt;ThreadLocal&lt;?&gt;&gt;

- 该方法仅仅用了一个Entry数组来存储Key, Value; Entry并不是链表形式, 而是每个bucket里面仅仅放一个Entry;

要了解ThreadLocalMap的实现, 我们先从入口开始, 就是往该Map中添加一个值:

先进行简单的分析, 对该代码表层意思进行解读:

- 看下当前threadLocal的在数组中的索引位置 比如: i = 2，看i = 2位置上面的元素(Entry)的Key是否等于threadLocal 这个 Key, 如果等于就很好说了, 直接将该位置上面的Entry的Value替换成最新的就可以了;

- 如果当前位置上面的 Entry 的 Key为空, 说明ThreadLocal对象已经被回收了, 那么就调用replaceStaleEntry

- 如果清理完无用条目(ThreadLocal被回收的条目)、并且数组中的数据大小 &gt; 阈值的时候对当前的Table进行重新哈希 所以, 该HashMap是处理冲突检测的机制是向后移位, 清除过期条目 最终找到合适的位置;

了解完Set方法, 后面就是Get方法了:

先找到ThreadLocal的索引位置, 如果索引位置处的entry不为空并且键与threadLocal是同一个对象, 则直接返回; 否则去后面的索引位置继续查找

### [Entry对象](#entry对象)

这里的key指向的ThreadLocal是弱引用，是为了防止ThreadLocal对象永远不会被回收。因为，若key为强引用，当ThreadLocal不想用了，那么就令 tl = null，但是此时key中还有一个强引用指向ThreadLocal，因此也就永远无法进行回收(除非ThreadLocalMap不用了)，所以会有内存泄露；但如果key使用的是弱引用，只要GC，就会回收
![](/imported/markdown/2026-01-17-markdown-ee42b53e-threadlocal-线程私有变量的存储与访问机制/images/c9d280fc7188-202404251607832.gif)
但是还会有内存泄漏存在，ThreadLocal被回收，就导致key=null,此时map中也就无法访问到value，无法访问到的value也就无用了，也就是说，这个k-v对无用了，那么value也应该被回收，但实际上value可能没有被回收，因此依然存在内存泄露

内存泄漏（Memory Leak）是指程序中已动态分配的堆内存由于某种原因程序未释放或无法释放，造成系统内存的浪费，导致程序运行速度减慢甚至系统崩溃等严重后果。

弱引用：GC时，若没有强引用指向这个对象了，只剩下弱引用，就会直接进行回收。原因就在于GC时无关内存是否足够，弱引用会被直接回收。所以，只要tl=null了，那么GC时，key指向的ThreadLocal对象就会被回收

### [ThreadLocal内存泄漏的原因？](#threadlocal内存泄漏的原因)

每个线程都有⼀个 ThreadLocalMap 的内部属性，map的key是 ThreaLocal，定义为弱引用，value是强引用类型。垃圾回收的时候会⾃动回收key，而value的回收取决于Thread对象的生命周期。

一般会通过线程池的方式复用线程节省资源，而如果用线程池来操作ThreadLocal 对象确实会造成内存泄露, 因为对于线程池里面不会销毁的线程, 里面总会存在着&lt;ThreadLocal, LocalVariable&gt;的强引用, 因为final static 修饰的 ThreadLocal 并不会释放, 而ThreadLocalMap 对于 Key 虽然是弱引用, 但是强引用不会释放, 弱引用当然也会一直有值, 同时创建的LocalVariable对象也不会释放, 就造成了内存泄露; 如果LocalVariable对象不是一个大对象的话, 其实泄露的并不严重, 泄露的内存 = 核心线程数 * LocalVariable对象的大小;

所以, 为了避免出现内存泄露的情况, ThreadLocal提供了一个清除线程中对象的方法, 即 remove, 其实内部实现就是调用 ThreadLocalMap 的remove方法:

## [应用场景](#应用场景)

### [每个线程维护了一个“序列号”](#每个线程维护了一个-序列号)

### [Session的管理](#session的管理)

Web 应用中的请求处理：在 Web 应用中，一个请求通常会被多个线程处理，每个线程需要访问自己的数据，使用 ThreadLocal 可以确保数据在每个线程中的独立性。

经典的另外一个例子：

### [在线程内部创建ThreadLocal](#在线程内部创建threadlocal)

线程池中的线程对象共享数据：线程池中的线程对象是可以被多个任务共享的，如果线程对象中需要保存任务相关的数据，使用 ThreadLocal 可以保证线程安全。

当然，在使用线程池时，ThreadLocal 可能会导致线程重用时的数据残留，从而影响程序的正确性。因此，在使用线程池时，要确保在任务执行前后清理 ThreadLocal 的值，以避免线程重用时的数据残留。

线程类内部创建ThreadLocal，基本步骤如下：

- 在多线程的类(如ThreadDemo类)中，创建一个ThreadLocal对象threadXxx，用来保存线程间需要隔离处理的对象xxx。

- 在ThreadDemo类中，创建一个获取要隔离访问的数据的方法getXxx()，在方法中判断，若ThreadLocal对象为null时候，应该new()一个隔离访问类型的对象，并强制转换为要应用的类型。

- 在ThreadDemo类的run()方法中，通过调用getXxx()方法获取要操作的数据，这样可以保证每个线程对应一个数据对象，在任何时刻都操作的是这个对象。

### [java 开发手册中推荐的 ThreadLocal](#java-开发手册中推荐的-threadlocal)

看看阿里巴巴 java 开发手册中推荐的 ThreadLocal 的用法:

然后再要用到 DateFormat 对象的地方，这样调用：

## [InheritableThreadLocal](#inheritablethreadlocal)

InheritableThreadLocal相比ThreadLocal多一个能力：在创建子线程Thread时，子线程Thread会自动继承父线程的InheritableThreadLocal信息到子线程中，进而实现在在子线程获取父线程的InheritableThreadLocal值的目的。

### [和 ThreadLocal 的区别](#和-threadlocal-的区别)

举个简单的栗子对比下InheritableThreadLocal和ThreadLocal：

执行结果：

可以看到子线程中可以获取到父线程设置的inheritableThreadLocal值，但不能获取到父线程设置的threadLocal值

### [实现原理](#实现原理)

InheritableThreadLocal 的实现原理相当精妙，它通过在创建子线程的瞬间，“复制”父线程的线程局部变量，从而实现了数据从父线程到子线程的**一次性、创建时**的传递 。

其核心工作原理可以清晰地通过以下序列图展示，它描绘了当父线程创建一个子线程时，数据是如何被传递的：

下面我们来详细拆解图中的关键环节。

#### [核心实现机制](#核心实现机制)

1. **数据结构基础：`Thread`类内部维护了两个 `ThreadLocalMap`类型的变量 ：

  - `threadLocals`：用于存储普通 `ThreadLocal`设置的变量副本。

  - `inheritableThreadLocals`：专门用于存储 `InheritableThreadLocal`设置的变量副本 。`InheritableThreadLocal`通过重写 `getMap`和 `createMap`方法，使其所有操作都针对 `inheritableThreadLocals`字段，从而与普通 `ThreadLocal`分离开 。

1. **继承触发时刻：子线程的创建**。继承行为发生在子线程被创建（即执行 `new Thread()`）时。在 `Thread`类的 `init`方法中，如果判断需要继承（`inheritThreadLocals`参数为 `true`）**且**父线程（当前线程）的 `inheritableThreadLocals`不为 `null`，则会执行复制逻辑 。

1. **复制过程的核心：`createInheritedMap`**。这是实现复制的核心方法 。它会创建一个新的 `ThreadLocalMap`，并将父线程 `inheritableThreadLocals`中的所有条目遍历拷贝到新 Map 中。

  - **Key的复制**：Key（即 `InheritableThreadLocal`对象本身）是直接复制的引用。

  - **Value的生成**：Value 并非直接复制引用，而是通过调用 `InheritableThreadLocal`的 `childValue(T parentValue)`方法来生成子线程中的初始值。**默认实现是直接返回父值**（`return parentValue;`），这意味着对于对象类型，父子线程将共享同一个对象引用 。

#### [关键特性与注意事项](#关键特性与注意事项)

1. **创建时复制，后续独立**：继承只发生一次，即在子线程对象创建的瞬间。此后，父线程和子线程对各自 `InheritableThreadLocal`变量的修改互不影响 。

1. **在线程池中的局限性**：这是 `InheritableThreadLocal`最需要警惕的问题。线程池中的线程是复用的，这些线程在首次创建时可能已经从某个父线程继承了值。但当它们被用于执行新的任务时，新的任务提交线程（逻辑上的“父线程”）与工作线程已无直接的创建关系，因此之前继承的值不会更新，这会导致**数据错乱**（如用户A的任务拿到了用户B的信息）或**内存泄漏**​ 。对于线程池场景，应考虑使用阿里开源的 **TransmittableThreadLocal (TTL)**​ 。

1. **浅拷贝与对象共享**：由于 `childValue`方法默认是浅拷贝，如果存入的是可变对象（如 `Map`、`List`），父子线程实际持有的是同一个对象的引用。在一个线程中修改该对象的内部状态，会直接影响另一个线程 。若需隔离，可以重写 `childValue`方法实现深拷贝 。

1. **内存泄漏风险**：与 `ThreadLocal`类似，如果线程长时间运行（如线程池中的核心线程），并且未及时调用 `remove`方法清理，那么该线程的 `inheritableThreadLocals`会一直持有值的强引用，导致无法被GC回收。良好的实践是在任务执行完毕后主动调用 `remove()`

#### [线程池中局限性](#线程池中局限性)

一般来说，在真实的业务场景下，没人会直接 new Thread，而都是使用线程池的，因此`InheritableThreadLocal`在线程池中的使用局限性要额外注意

首先，我们先理解 `InheritableThreadLocal`的继承前提

- `InheritableThreadLocal`的继承只发生在 **新线程被创建时**（即 `new Thread()`并启动时）。在创建过程中，子线程会复制父线程的 `InheritableThreadLocal`值。

- 在线程池中，线程是预先创建或按需创建的，并且会被复用。因此，继承只会在线程池**创建新线程**时发生，而不会在复用现有线程时发生。

再看线程池创建新线程的条件，对于标准的 `ThreadPoolExecutor`，新线程的创建遵循以下规则：

1. **当前线程数 &lt; 核心线程数**：当提交新任务时，如果当前运行的线程数小于核心线程数，即使有空闲线程，线程池也会创建新线程来处理任务。此时，新线程会继承父线程（提交任务的线程）的 `InheritableThreadLocal`。

1. **当前线程数 &gt;= 核心线程数 && 队列已满 && 线程数 &lt; 最大线程数**：当任务队列已满，且当前线程数小于最大线程数时，线程池会创建新线程来处理任务。同样，新线程会继承父线程的 `InheritableThreadLocal`。

不会继承的场景

- **线程复用**：当线程池中有空闲线程时（例如，当前线程数 &gt;= 核心线程数，但队列未满），任务会被分配给现有线程执行。此时，没有新线程创建，因此不会发生继承。现有线程的 `InheritableThreadLocal`值保持不变（可能是之前任务设置的值），这可能导致数据错乱（如用户A的任务看到用户B的数据）。

- **线程数已达最大值**：如果线程数已达最大线程数，且队列已满，新任务会被拒绝（根据拒绝策略），也不会创建新线程，因此不会继承。

不只是线程池污染，线程池使用 `InheritableThreadLocal` 还可能存在获取不到值的情况。例如，在执行异步任务的时候，复用了某个已有的线程A，并且当时创建该线程A的时候，没有继承InheritableThreadLocal，进而导致后面复用该线程的时候，从InheritableThreadLocal获取到的值为null：

执行结果：

当然了，解决这个问题可以考虑使用阿里开源的 **TransmittableThreadLocal (TTL)**，​或者在提交异步任务前，先获取线程数据，再传入。例如：

### [与 ThreadLocal 的对比](#与-threadlocal-的对比)
特性ThreadLocalInheritableThreadLocal**数据隔离**​线程绝对隔离线程绝对隔离**子线程继承**​**不支持**​**支持**（创建时）**底层存储字段**​`Thread.threadLocals``Thread.inheritableThreadLocals`**适用场景**​线程内全局变量，避免传参**父子线程间**需要传递上下文数据
