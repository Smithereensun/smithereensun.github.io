{

  "title": "ReentrantReadWriteLock：解锁高性能读写并发编程的关键技术",
  "has_date": true,
  "description": "ReentrantReadWriteLock使用场景 ReentrantReadWriteLock 是 Java 的一种读写锁，它允许多个读线程同时访问，但只允许一个写线程访问（会阻塞所有的读写线程）。这种锁的设计可以提高性能，特别是在读操作的数量远远超过写操作的情况下。 在并发场景中，为了解决线程",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/03-juclock3-reentrantreadwritelock - ReentrantReadWriteLock：解锁高性能读写并发编程的关键技术.md",
  "date": "2025-05-17"

}

## [ReentrantReadWriteLock使用场景](#reentrantreadwritelock使用场景)

ReentrantReadWriteLock 是 Java 的一种读写锁，它允许多个读线程同时访问，但只允许一个写线程访问（会阻塞所有的读写线程）。这种锁的设计可以提高性能，特别是在读操作的数量远远超过写操作的情况下。

在并发场景中，为了解决线程安全问题，我们通常会使用关键字 synchronized 或者 JUC 包中实现了 Lock 接口的 ReentrantLock。但它们都是独占式获取锁，也就是在同一时刻只有一个线程能够获取锁。

而在一些业务场景中，大部分只是读数据，写数据很少，如果仅仅是读数据的话并不会影响数据正确性，而如果在这种业务场景下，依然使用独占锁的话，很显然会出现性能瓶颈。针对这种读多写少的情况，Java 提供了另外一个实现 Lock 接口的 ReentrantReadWriteLock——读写锁。

`ReentrantReadWriteLock`其实就是 **读读并发、读写互斥、写写互斥**。如果一个对象并发读的场景大于并发写的场景，那就可以使用 `ReentrantReadWriteLock`来达到保证线程安全的前提下提高并发效率。首先，我们先了解一下Doug Lea为我们准备的两个demo。

### [CachedData](#cacheddata)

一个缓存对象的使用案例，缓存对象在使用时，一般并发读的场景远远大于并发写的场景，所以缓存对象是非常适合使用`ReentrantReadWriteLock`来做控制的

### [RWDictionary](#rwdictionary)

Doug Lea给出的第二个demo，一个并发容器的demo。并发容器我们一般都是直接使用ConcurrentHashMap的，但是我们可以使用非并发安全的容器+ReentrantReadWriteLock来组合出一个并发容器。如果这个并发容器的读的频率&gt;写的频率，那这个效率还是不错的

## [ReentrantReadWriteLock的特性](#reentrantreadwritelock的特性)

**读写锁允许同一时刻被多个读线程访问，但是在写线程访问时，所有的读线程和其他的写线程都会被阻塞**。

在分析 WirteLock 和 ReadLock 的互斥性时，我们可以按照 WriteLock 与 WriteLock，WriteLock 与 ReadLock 以及 ReadLock 与 ReadLock 进行对比分析。

这里总结一下读写锁的特性：

1. **公平性选择**：支持非公平性（默认）和公平的锁获取方式，非公平的吞吐量优于公平；

1. **重入性**：支持重入，读锁获取后能再次获取，写锁获取之后能够再次获取写锁，同时也能够获取读锁；

1. **锁降级**：写锁降级是一种允许写锁转换为读锁的过程。通常的顺序是：

  - 获取写锁：线程首先获取写锁，确保在修改数据时排它访问。

  - 获取读锁：在写锁保持的同时，线程可以再次获取读锁。

  - 释放写锁：线程保持读锁的同时释放写锁。

  - 释放读锁：最后线程释放读锁。

这样，写锁就降级为读锁，允许其他线程进行并发读取，但仍然排除其他线程的写操作。

接下来额外说一下锁降级

- 锁降级

锁降级指的是写锁降级成为读锁。如果当前线程拥有写锁，然后将其释放，最后再获取读锁，这种分段完成的过程不能称之为锁降级。锁降级是指把持住(当前拥有的)写锁，再获取到读锁，随后释放(先前拥有的)写锁的过程。

接下来看一个锁降级的示例。因为数据不常变化，所以多个线程可以并发地进行数据处理，当数据变更后，如果当前线程感知到数据变化，则进行数据的准备工作，同时其他处理线程被阻塞，直到当前线程完成数据的准备工作，如代码如下所示：

上述示例中，当数据发生变更后，update变量(布尔类型且volatile修饰)被设置为false，此时所有访问processData()方法的线程都能够感知到变化，但只有一个线程能够获取到写锁，其他线程会被阻塞在读锁和写锁的lock()方法上。当前线程获取写锁完成数据准备之后，再获取读锁，随后释放写锁，完成锁降级。

锁降级中读锁的获取是否必要呢? 答案是必要的。主要是为了保证数据的可见性，如果当前线程不获取读锁而是直接释放写锁，假设此刻另一个线程(记作线程T)获取了写锁并修改了数据，那么当前线程无法感知线程T的数据更新。如果当前线程获取读锁，即遵循锁降级的步骤，则线程T将会被阻塞，直到当前线程使用数据并释放读锁之后，线程T才能获取写锁进行数据更新。

RentrantReadWriteLock不支持锁升级(把持读锁、获取写锁，最后释放读锁的过程)。目的也是保证数据可见性，如果读锁已被多个线程获取，其中任意线程成功获取了写锁并更新了数据，则其更新对其他获取到读锁的线程是不可见的。

## [ReentrantReadWriteLock源码分析](#reentrantreadwritelock源码分析)

### [类的继承关系](#类的继承关系)

说明: 可以看到，ReentrantReadWriteLock实现了ReadWriteLock接口，ReadWriteLock接口定义了获取读锁和写锁的规范，具体需要实现类去实现；同时其还实现了Serializable接口，表示可以进行序列化，在源代码中可以看到ReentrantReadWriteLock实现了自己的序列化逻辑。

### [类的内部类](#类的内部类)

ReentrantReadWriteLock有五个内部类，五个内部类之间也是相互关联的。内部类的关系如下图所示。
![](/imported/markdown/2025-05-17-markdown-5769a4ac-reentrantreadwritelock-解锁高性能读写并发编程的关键技术/images/543761ca5160-202404251057400.jpg)
说明: 如上图所示，Sync继承自AQS、NonfairSync继承自Sync类、FairSync继承自Sync类；ReadLock实现了Lock接口、WriteLock也实现了Lock接口。

### [内部类 -类Sync](#内部类-类sync)

- Sync类的继承关系

说明: Sync抽象类继承自AQS抽象类，Sync类提供了对ReentrantReadWriteLock的支持。

- Sync类的内部类

Sync类内部存在两个内部类，分别为HoldCounter和ThreadLocalHoldCounter，其中HoldCounter主要与读锁配套使用，其中，HoldCounter源码如下。

说明: HoldCounter主要有两个属性，count和tid，其中count表示某个读线程重入的次数，tid表示该线程的tid字段的值，该字段可以用来唯一标识一个线程。ThreadLocalHoldCounter的源码如下

说明: ThreadLocalHoldCounter重写了ThreadLocal的initialValue方法，ThreadLocal类可以将线程与对象相关联。在没有进行set的情况下，get到的均是initialValue方法里面生成的那个HolderCounter对象。

- Sync类的属性

说明: 该属性中包括了读锁、写锁线程的最大量。本地线程计数器等。

- Sync类的构造函数

说明：在Sync的构造函数中设置了本地线程计数器和AQS的状态state。

### [类的属性](#类的属性)

说明: 可以看到ReentrantReadWriteLock属性包括了一个ReentrantReadWriteLock.ReadLock对象，表示读锁；一个ReentrantReadWriteLock.WriteLock对象，表示写锁；一个Sync对象，表示同步队列。

### [类的构造函数](#类的构造函数)

- ReentrantReadWriteLock()型构造函数

说明: 此构造函数会调用另外一个有参构造函数。

- ReentrantReadWriteLock(boolean)型构造函数

说明: 可以指定设置公平策略或者非公平策略，并且该构造函数中生成了读锁与写锁两个对象。

### [内部类 - Sync核心函数分析](#内部类-sync核心函数分析)

对ReentrantReadWriteLock对象的操作绝大多数都转发至Sync对象进行处理。下面对Sync类中的重点函数进行分析

- sharedCount函数

表示占有读锁的线程数量，源码如下

说明:：直接将state右移16位，就可以得到读锁的线程数量，因为state的高16位表示读锁，对应的低十六位表示写锁数量。

- exclusiveCount函数

表示占有写锁的线程数量，源码如下

说明：

**EXCLUSIVE_MASK**为:

EXCLUSIVE_MASK 为 1 左移 16 位然后减 1，即为 0x0000FFFF。而 exclusiveCount 方法是将同步状态（state 为 int 类型）与 0x0000FFFF 相与，即取同步状态的低 16 位。

那么低 16 位代表什么呢？根据 exclusiveCount 方法的注释为独占式获取的次数即写锁被获取的次数，现在就可以得出来一个结论**同步状态的低 16 位用来表示写锁的获取次数**。

#### [写锁的获取](#写锁的获取)

同一时刻，ReentrantReadWriteLock 的写锁是不能被多个线程获取的，很显然 ReentrantReadWriteLock 的写锁是独占式锁，而实现写锁的同步语义是通过重写 AQS 中的 tryAcquire 方法实现的。

- tryAcquire函数

说明: 此函数用于获取写锁：首先会获取state，判断是否为0；
 1. 若为0，表示此时没有读锁线程，再判断写线程是否应该被阻塞，而在非公平策略下总是不会被阻塞，在公平策略下会进行判断(判断同步队列中是否有等待时间更长的线程；若存在，则需要被阻塞，否则，无需阻塞)，之后在设置状态state，然后返回true。
 2. 若state不为0，则表示此时存在读锁或写锁线程，若写锁线程数量为0或者当前线程为独占锁线程，则返回false，表示不成功，否则，判断写锁线程的重入次数是否大于了最大值，若是，则抛出异常，否则，设置状态state，返回true，表示成功。其函数流程图如下
![](/imported/markdown/2025-05-17-markdown-5769a4ac-reentrantreadwritelock-解锁高性能读写并发编程的关键技术/images/8e195294d34d-202404251057430.jpg)
其主要逻辑为：**当读锁已经被读线程获取或者写锁已经被其他写线程获取，则写锁获取失败；否则，获取成功并支持重入，增加写状态。**

#### [写锁的释放](#写锁的释放)

写锁释放通过重写 AQS 的 tryRelease 方法，源码为：

- tryRelease函数

说明: 此函数用于释放写锁资源，首先会判断该线程是否为独占线程，若不为独占线程，则抛出异常，否则，计算释放资源后的写锁的数量，若为0，表示成功释放，资源不将被占用，否则，表示资源还被占用。其函数流程图如下。
![](/imported/markdown/2025-05-17-markdown-5769a4ac-reentrantreadwritelock-解锁高性能读写并发编程的关键技术/images/a40874172444-202404251057433.jpg)
#### [读锁的获取](#读锁的获取)

看完了写锁，再来看看读锁，读锁不是独占式锁，即同一时刻该锁可以被多个读线程获取，也就是一种共享式锁。按照之前对 AQS 的介绍，实现共享式同步组件的同步语义需要通过重写 AQS 的 tryAcquireShared 方法和 tryReleaseShared 方法。读锁的获取实现方法为：

- tryAcquireShared函数

说明: 此函数表示读锁线程获取读锁。首先判断写锁是否为0并且当前线程不占有独占锁，直接返回；否则，判断读线程是否需要被阻塞并且读锁数量是否小于最大值并且比较设置状态成功，若当前没有读锁，则设置第一个读线程firstReader和firstReaderHoldCount；若当前线程线程为第一个读线程，则增加firstReaderHoldCount；否则，将设置当前线程对应的HoldCounter对象的值。流程图如下。
![](/imported/markdown/2025-05-17-markdown-5769a4ac-reentrantreadwritelock-解锁高性能读写并发编程的关键技术/images/efdab12c8e29-202404251057428.jpg)
**当写锁被其他线程获取后，读锁获取失败**，否则获取成功，会利用 CAS 更新同步状态。

另外，当前同步状态需要加上 SHARED_UNIT（`(1 &lt;&lt; SHARED_SHIFT)`，即 0x00010000）的原因，我们在上面也说过了，同步状态的高 16 位用来表示读锁被获取的次数。

如果 CAS 失败或者已经获取读锁的线程再次获取读锁时，是靠 fullTryAcquireShared 方法实现的。

- fullTryAcquireShared函数

说明: 在tryAcquireShared函数中，如果下列三个条件不满足(读线程是否应该被阻塞、小于最大值、比较设置成功)则会进行fullTryAcquireShared函数中，它用来保证相关操作可以成功。其逻辑与tryAcquireShared逻辑类似，可以继续再往后看。

#### [读锁的释放](#读锁的释放)

读锁释放的实现主要通过方法 tryReleaseShared，源码如下，主要逻辑请看注释：

- tryReleaseShared函数

说明: 此函数表示读锁线程释放锁。首先判断当前线程是否为第一个读线程firstReader，若是，则判断第一个读线程占有的资源数firstReaderHoldCount是否为1，若是，则设置第一个读线程firstReader为空，否则，将第一个读线程占有的资源数firstReaderHoldCount减1；若当前线程不是第一个读线程，那么首先会获取缓存计数器(上一个读锁线程对应的计数器 )，若计数器为空或者tid不等于当前线程的tid值，则获取当前线程的计数器，如果计数器的计数count小于等于1，则移除当前线程对应的计数器，如果计数器的计数count小于等于0，则抛出异常，之后再减少计数即可。无论何种情况，都会进入无限循环，该循环可以确保成功设置状态state。其流程图如下
![](/imported/markdown/2025-05-17-markdown-5769a4ac-reentrantreadwritelock-解锁高性能读写并发编程的关键技术/images/373a7089cde3-202404251057425.jpg)
#### [锁降级](#锁降级)

读写锁支持锁降级，**遵循按照获取写锁，获取读锁再释放写锁的次序，写锁能够降级成为读锁**，不支持锁升级，关于锁降级，下面的示例代码摘自 ReentrantWriteReadLock 源码：

这里的流程可以解释如下：

- 获取读锁：首先尝试获取读锁来检查某个缓存是否有效。

- 检查缓存：如果缓存无效，则需要释放读锁，因为在获取写锁之前必须释放读锁。

- 获取写锁：获取写锁以便更新缓存。此时，可能还需要重新检查缓存状态，因为在释放读锁和获取写锁之间可能有其他线程修改了状态。

- 更新缓存：如果确认缓存无效，更新缓存并将其标记为有效。

- 写锁降级为读锁：在释放写锁之前，获取读锁，从而实现写锁到读锁的降级。这样，在释放写锁后，其他线程可以并发读取，但不能写入。

- 使用数据：现在可以安全地使用缓存数据了。

- 释放读锁：完成操作后释放读锁。

这个流程结合了读锁和写锁的优点，确保了数据的一致性和可用性，同时允许在可能的情况下进行并发读取。使用读写锁的代码可能看起来比使用简单的互斥锁更复杂，但它提供了更精细的并发控制，可能会提高多线程应用程序的性能

## [ReadWriteLock和StampedLock](#readwritelock和stampedlock)

### [ReadWriteLock](#readwritelock)

ReadWriteLock 是Java**提供的一个接口**，全类名：java.util.concurrent.locks.ReadWriteLock，上面的ReentrantReadWriteLock就是继承自这个接口。它允许多个线程同时读取共享资源，但只允许一个线程写入共享资源。这种机制可以提高读取操作的并发性，但写入操作需要独占资源。

#### [特性](#特性)

- 多个线程可以同时获取读锁，但只有一个线程可以获取写锁。

- 当一个线程持有写锁时，其他线程无法获取读锁和写锁，读写互斥。

- 当一个线程持有读锁时，其他线程可以同时获取读锁，读读共享。但无法获取写锁，读写互斥

#### [使用场景](#使用场景)

ReadWriteLock 适用于读多写少的场景，例如缓存系统、数据库连接池等。在这些场景中，读取操作占据大部分时间，而写入操作较少。

#### [使用示例](#使用示例)

使用 ReadWriteLock 的示例，实现了一个简单的缓存系统：

在上述示例中，Cache 类使用 ReadWriteLock 来实现对 data 的并发访问控制。get 方法获取读锁并读取数据，put 方法获取写锁并写入数据。

### [StampedLock](#stampedlock)

StampedLock 是Java 8 中引入的一种新的锁机制，全类名：java.util.concurrent.locks.StampedLock，它提供了一种乐观读的机制，可以进一步提升读取操作的并发性能。

#### [特性](#特性-1)

- 与 ReadWriteLock 类似，StampedLock 也支持多个线程同时获取读锁，但只允许一个线程获取写锁。

- 与 ReadWriteLock 不同的是，StampedLock 还提供了一个乐观读锁（Optimistic Read Lock），即不阻塞其他线程的写操作，但在读取完成后需要验证数据的一致性。

#### [使用场景](#使用场景-1)

StampedLock 适用于读远远大于写的场景，并且对数据的一致性要求不高，例如统计数据、监控系统等。

#### [使用示例](#使用示例-1)

使用 StampedLock 的示例，实现了一个计数器：

在上述示例中，Counter 类使用 StampedLock 来实现对计数器的并发访问控制。getCount 方法首先尝试获取乐观读锁，并读取计数器的值，然后通过 validate 方法验证数据的一致性。如果验证失败，则获取悲观读锁，并重新读取计数器的值。increment 方法获取写锁，并对计数器进行递增操作。

### [小结](#小结)

ReadWriteLock 和 StampedLock 都是Java中用于并发控制的重要机制。

- ReadWriteLock 适用于读多写少的场景;

- StampedLock 则适用于读远远大于写的场景，并且对数据的一致性要求不高;

在实际应用中，我们需要根据具体场景来选择合适的锁机制。通过合理使用这些锁机制，我们可以提高并发程序的性能和可靠性。
