{

  "title": "CAS与原子类详解：无锁并发编程的实现原理",
  "has_date": true,
  "description": "CAS 介绍 CAS 可以保证对共享变量操作的原子性 CAS全称Compare And Swap，比较与交换，是乐观锁的主要实现方式。CAS在不使用锁的情况下实现多线程之间的变量同步。ReentrantLock内部的AQS和原子类内部都使用了CAS。 CAS算法涉及到三个操作数：需要读写的内存值V。",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/03-juclock1-cas-atomic - CAS与原子类详解：无锁并发编程的实现原理.md",
  "date": "2025-05-17"

}

## [CAS](#cas)

### [介绍](#介绍)

CAS 可以保证对共享变量操作的原子性

CAS全称Compare And Swap，比较与交换，是乐观锁的主要实现方式。CAS在不使用锁的情况下实现多线程之间的变量同步。ReentrantLock内部的AQS和原子类内部都使用了CAS。

CAS算法涉及到三个操作数：需要读写的内存值V。进行比较的值A。要写入的新值B。只有当V的值等于A时，才会使用原子方式用新值B来更新V的值，否则会继续重试直到成功更新值。

以AtomicInteger为例，AtomicInteger的getAndIncrement()方法底层就是CAS实现，关键代码是 compareAndSwapInt(obj, offset, expect, update)，其含义就是，如果obj内的value和expect相等，就证明没有其他线程改变过这个变量，那么就更新它为update，如果不相等，那就会继续重试直到成功更新值。

### [CAS存在的问题](#cas存在的问题)

CAS不加锁，保证一致性，但是需要多次比较

#### [循环时间长，开销大](#循环时间长-开销大)

例如AtomicInteger因为执行的是do while，如果比较不成功一直在循环，最差的情况，就是某个线程一直取到的值和预期值都不一样，这样就会无限循环）

解决方案：可以使用java8中的LongAdder，分段CAS和自动分段迁移。

#### [只能保证一个共享变量的原子操作](#只能保证一个共享变量的原子操作)

当对一个共享变量执行操作时，我们可以通过循环CAS的方式来保证原子操作

但是对于多个共享变量操作时，循环CAS就无法保证操作的原子性，这个时候只能用锁来保证原子性

解决方案：可以用AtomicReference，这个是封装自定义对象的，多个变量可以放一个自定义对象里，然后他会检查这个对象的引用是不是同一个。如果多个线程同时对一个对象变量的引用进行赋值，用AtomicReference的CAS操作可以解决并发冲突问题。

#### [ABA问题](#aba问题)

假设两个线程T1和T2访问同一个变量V，当T1访问变量V时，读取到V的值为A；此时线程T1被抢占了，T2开始执行，T2先将变量V的值从A变成B，然后又将变量V的值从B变成A；此时T1又抢占了主动权，继续执行，它发现V的值还是A，以为没有变化，所以就继续执行了。这个过程中，变量V从A变为B，再由B变为A就形象的称为ABA问题。

解决方案：可以引入版本号改变这个问题，每次改变版本号都+1

从Java 1.5开始，JDK的Atomic包里提供了一个类AtomicStampedReference来解决ABA问题。这个类的compareAndSet方法的作用是首先检查当前引用是否等于预期引用，并且检查当前标志是否等于预期标志，如果全部相等，则以原子方式将该引用和该标志的值设置为给定的更新值。

### [无锁并发](#无锁并发)

CAS 可以保证对共享变量操作的原子性，而volatile可以实现可见性和有序性，结合CAS和volatile可以实现无锁并发，适用于竞争不激烈，多核CPU的场景下。

CAS之所以效率高是因为在其内部没有使用synchronized关键字，CAS不会让线程进入阻塞状态，那么也就避免了synchronized当中用户态和内核态的切换所带来的的性能消耗问题，也避免了线程挂起等问题。如果竞争非常激烈，那么CAS就会出现线程大量重试，因为多线程来进行竞争，那么也就导致有可能很多的线程设置取值失败，那么又要进行while循环重试，即大量的线程进行重试操作，成功存的线程反而不多，那么这样的话反而会使性能大大降低。所以如果竞争太激烈还使用的是CAS机制，会导致其性能比synchronized还要低。

### [小结](#小结)

CAS可以将比较和交换转换为原子操作，这个原子操作直接由处理器保证（由CPU支持），会拿旧的预估值与内存当中的最新值进行比较；如果相同就进行交换并且把最新的值赋值到内存当中的这个变量；

CAS 必须借助 volatile 才能读取到共享变量的最新值来实现【比较并交换】的效果。

使用CAS时，线程数不要超过CPU的核心数，每个CPU核心都能同时并行某个线程，超过的话想运行也运行不了，得发生上下文切换。线程的上下文切换的成本很高，要保存线程的信息，当从阻塞恢复成可运行，还要恢复线程的信息。

## [原子类Atomic](#原子类atomic)

### [AtomicInteger](#atomicinteger)

#### [问题](#问题)

改为原子类

#### [底层源码](#底层源码)

AtomicInteger类当中其内部会包含一个叫做UnSafe的类，该类可以保证变量在赋值时的原子操作；

- 变量valueOffset：表示该变量值在内存中的偏移地址，因为Unsafe就是根据内存偏移地址获取数据的

- 变量value用volatile修饰：保证了多线程之间的内存可见性

变量解释：

- var5：就是从主内存中拷贝到工作内存中的值

- val1：AtomicInteger对象本身

- var2：该对象值的valueOffset

- var4：需要变动的数量

- var5：用var1和var2找到的内存中的真实值

compareAndSwapInt(var1, var2, var5, var5 + var4) 表示用该对象当前的值与var5比较

- 如果相同，更新成var5 + var4 并返回true

- 如果不同，继续取值然后再比较，直到更新完成

需要比较工作内存中的值，和主内存中的值进行比较

假设执行 compareAndSwapInt返回false，那么就一直执行 while方法，直到期望的值和真实值一样
![](/imported/markdown/2025-05-17-markdown-e47c6e3e-cas与原子类详解-无锁并发编程的实现原理/images/31315733c2d0-202404251040434.gif)
假设线程A和线程B同时执行getAndInt操作（分别跑在不同的CPU上）

1. AtomicInteger里面的value原始值为3，即主内存中AtomicInteger的 value 为3，根据JMM模型，线程A和线程B各自持有一份价值为3的副本，分别存储在各自的工作内存

1. 线程A通过getIntVolatile(var1 , var2) 拿到value值3，这时线程A被挂起（该线程失去CPU执行权）

1. 线程B也通过getIntVolatile(var1, var2)方法获取到value值也是3，此时刚好线程B没有被挂起，并执行了compareAndSwapInt方法，比较内存的值也是3，成功修改内存值为4，线程B打完收工，一切OK

1. 这时线程A恢复，执行CAS方法，比较发现自己手里的数字3和主内存中的数字4不一致，说明该值已经被其它线程抢先一步修改过了，那么A线程本次修改失败，只能够重新读取后在来一遍了，也就是继续执行do while

1. 线程A重新获取value值，因为变量value被volatile修饰，所以其它线程对它的修改，线程A总能够看到，线程A继续执行compareAndSwapInt进行比较替换，直到成功。

但是AtomicInteger会存在CAS循环开销大的问题，因此JDK8引入LongAdder来解决这个问题

### [LongAdder](#longadder)

LongAdder主要使用分段CAS以及自动分段迁移的方式来大幅度提升多线程高并发执行CAS操作的性能
![](/imported/markdown/2025-05-17-markdown-e47c6e3e-cas与原子类详解-无锁并发编程的实现原理/images/eb596ae97b82-202404251040438.gif)
实现过程：

1. 在LongAdder的底层实现中，首先有一个base值，刚开始多线程来不停的累加数值，都是对base进行累加的，比如刚开始累加成了base = 5。

1. 接着如果发现并发更新的线程数量过多，就会开始施行分段CAS的机制，也就是内部会搞一个Cell数组，每个数组是一个数值分段。

1. 这时，让大量的线程分别去对不同Cell内部的value值进行CAS累加操作，这样就把CAS计算压力分散到了不同的Cell分段数值中了！

1. 这样就可以大幅度的降低多线程并发更新同一个数值时出现的无限循环的问题，大幅度提升了多线程并发更新数值的性能和效率！

1. 内部实现了自动分段迁移的机制，也就是如果某个Cell的value执行CAS失败了，那么就会自动去找另外一个Cell分段内的value值进行CAS操作。这样也解决了线程空旋转、自旋不停等待执行CAS操作的问题，让一个线程过来执行CAS时可以尽快的完成这个操作。

最后，如果要从LongAdder中获取当前累加的总值，就会把base值和所有Cell分段数值加起来返回。

总的来说LongAdder减少了乐观锁的重试次数

#### [add源码](#add源码)

longAccumulate方法

### [AtomicStampedReference](#atomicstampedreference)

AtomicStampedReference主要维护包含一个对象引用以及一个可以自动更新的整数"stamp"的pair对象来解决ABA问题。

- 如果元素值和版本号都没有变化，并且和新的也相同，返回true；

- 如果元素值和版本号都没有变化，并且和新的不完全相同，就构造一个新的Pair对象并执行CAS更新pair。

可以看到，java中的实现跟我们上面讲的ABA的解决方法是一致的。

- 首先，使用版本号控制；

- 其次，不重复使用节点(Pair)的引用，每次都新建一个新的Pair来作为CAS比较的对象，而不是复用旧的；

- 最后，外部传入元素值及版本号，而不是节点(Pair)的引用。
