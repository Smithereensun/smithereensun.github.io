{

  "title": "Exchanger：多线程数据交换与任务协调的实现原理",
  "has_date": true,
  "description": "Exchanger简介 Exchanger用于进行两个线程之间的数据交换。它提供一个同步点，在这个同步点，两个线程可以交换彼此的数据。这两个线程通过exchange()方法交换数据，当一个线程先执行exchange()方法后，它会一直等待第二个线程也执行exchange()方法，当这两个线程到达同步",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/05-concurrenttools4-exchanger - Exchanger：多线程数据交换与任务协调的实现原理.md",
  "date": "2025-05-17"

}

## [Exchanger简介](#exchanger简介)

Exchanger用于进行两个线程之间的数据交换。它提供一个同步点，在这个同步点，两个线程可以交换彼此的数据。这两个线程通过exchange()方法交换数据，当一个线程先执行exchange()方法后，它会一直等待第二个线程也执行exchange()方法，当这两个线程到达同步点时，这两个线程就可以交换数据了。

## [Exchanger示例](#exchanger示例)

来一个非常经典的并发问题：有相同的数据buffer，一个或多个数据生产者，和一个或多个数据消费者。只是Exchange类只能同步2个线程，所以你只能在你的生产者和消费者问题中只有一个生产者和一个消费者时使用这个类。

可以看到，其结果可能如下：

## [Exchanger实现机制](#exchanger实现机制)

比如有2条线程A和B，A线程交换数据时，发现slot为空，则将需要交换的数据放在slot中等待其它线程进来交换数据，等线程B进来，读取A设置的数据，然后设置线程B需要交换的数据，然后唤醒A线程，原理就是这么简单。但是当多个线程之间进行交换数据时就会出现问题，所以Exchanger加入了slot数组。

## [Exchanger源码解析](#exchanger源码解析)

### [内部类 - Participant](#内部类-participant)

Participant的作用是为每个线程保留唯一的一个Node节点, 它继承ThreadLocal，说明每个线程具有不同的状态。

### [内部类 - Node](#内部类-node)

在Node定义中有两个变量值得思考：bound以及collides。前面提到了数组area是为了避免竞争而产生的，如果系统不存在竞争问题，那么完全没有必要开辟一个高效的arena来徒增系统的复杂性。首先通过单个slot的exchanger来交换数据，当探测到竞争时将安排不同的位置的slot来保存线程Node，并且可以确保没有slot会在同一个缓存行上。如何来判断会有竞争呢? CAS替换slot失败，如果失败，则通过记录冲突次数来扩展arena的尺寸，我们在记录冲突的过程中会跟踪“bound”的值，以及会重新计算冲突次数在bound的值被改变时。

### [核心属性](#核心属性)

- 为什么会有 **arena数组槽?**

slot为单个槽，arena为数组槽, 他们都是Node类型。在这里可能会感觉到疑惑，slot作为Exchanger交换数据的场景，应该只需要一个就可以了啊? 为何还多了一个Participant 和数组类型的arena呢? 一个slot交换场所原则上来说应该是可以的，但实际情况却不是如此，多个参与者使用同一个交换场所时，会存在严重伸缩性问题。既然单个交换场所存在问题，那么我们就安排多个，也就是数组arena。通过数组arena来安排不同的线程使用不同的slot来降低竞争问题，并且可以保证最终一定会成对交换数据。但是**Exchanger不是一来就会生成arena数组来降低竞争，只有当产生竞争是才会生成arena数组**。

- 那么怎么将Node与当前线程绑定呢？

Participant，Participant 的作用就是为每个线程保留唯一的一个Node节点，它继承ThreadLocal，同时在Node节点中记录在arena中的下标index。

### [构造函数](#构造函数)

初始化participant对象。

### [核心方法 - exchange(V x)](#核心方法-exchange-v-x)

等待另一个线程到达此交换点(除非当前线程被中断)，然后将给定的对象传送给该线程，并接收该线程的对象。

这个方法比较好理解：arena为数组槽，如果为null，则执行slotExchange()方法，否则判断线程是否中断，如果中断值抛出InterruptedException异常，没有中断则执行arenaExchange()方法。整套逻辑就是：如果slotExchange(Object item, boolean timed, long ns)方法执行失败了就执行arenaExchange(Object item, boolean timed, long ns)方法，最后返回结果V。

NULL_ITEM 为一个空节点，其实就是一个Object对象而已，slotExchange()为单个slot交换。

### [slotExchange(Object item, boolean timed, long ns)](#slotexchange-object-item-boolean-timed-long-ns)

程序首先通过participant获取当前线程节点Node。检测是否中断，如果中断return null，等待后续抛出InterruptedException异常。

- 如果slot不为null，则进行slot消除，成功直接返回数据V，否则失败，则创建arena消除数组。

- 如果slot为null，但arena不为null，则返回null，进入arenaExchange逻辑。

- 如果slot为null，且arena也为null，则尝试占领该slot，失败重试，成功则跳出循环进入spin+block(自旋+阻塞)模式。

在自旋+阻塞模式中，首先取得结束时间和自旋次数。如果match(做releasing操作的线程传递的项)为null，其首先尝试spins+随机次自旋(改自旋使用当前节点中的hash，并改变之)和退让。当自旋数为0后，假如slot发生了改变(slot != p)则重置自旋数并重试。否则假如：当前未中断&arena为null&(当前不是限时版本或者限时版本+当前时间未结束)：阻塞或者限时阻塞。假如：当前中断或者arena不为null或者当前为限时版本+时间已经结束：不限时版本：置v为null；限时版本：如果时间结束以及未中断则TIMED_OUT；否则给出null(原因是探测到arena非空或者当前线程中断)。

match不为空时跳出循环。

### [arenaExchange(Object item, boolean timed, long ns)](#arenaexchange-object-item-boolean-timed-long-ns)

此方法被执行时表示多个线程进入交换区交换数据，arena数组已被初始化，此方法中的一些处理方式和slotExchange比较类似，它是通过遍历arena数组找到需要交换的数据。

首先通过participant取得当前节点Node，然后根据当前节点Node的index去取arena中相对应的节点node。

- 前面提到过arena可以确保不同的slot在arena中是不会相冲突的，那么是怎么保证的呢？

- 用@sun.misc.Contended来规避伪共享？

**伪共享说明**：假设一个类的两个相互独立的属性a和b在内存地址上是连续的(比如FIFO队列的头尾指针)，那么它们通常会被加载到相同的cpu cache line里面。并发情况下，如果一个线程修改了a，会导致整个cache line失效(包括b)，这时另一个线程来读b，就需要从内存里再次加载了，这种多线程频繁修改ab的情况下，虽然a和b看似独立，但它们会互相干扰，非常影响性能。

我们再看Node节点的定义, 在Java 8 中我们是可以利用sun.misc.Contended来规避伪共享的。所以说通过 &lt;&lt; ASHIFT方式加上sun.misc.Contended，所以使得任意两个可用Node不会再同一个缓存行中。

再次回到arenaExchange()。取得arena中的node节点后，如果定位的节点q 不为空，且CAS操作成功，则交换数据，返回交换的数据，唤醒等待的线程。

- 如果q等于null且下标在bound & MMASK范围之内，则尝试占领该位置，如果成功，则采用自旋 + 阻塞的方式进行等待交换数据。

- 如果下标不在bound & MMASK范围之内获取由于q不为null但是竞争失败的时候：消除p。加入bound 不等于当前节点的bond(b != p.bound)，则更新p.bound = b，collides = 0，i = m或者m - 1。如果冲突的次数不到m 获取m 已经为最大值或者修改当前bound的值失败，则通过增加一次collides以及循环递减下标i的值；否则更新当前bound的值成功：我们令i为m+1即为此时最大的下标。最后更新当前index的值。

## [和SynchronousQueue的对比](#和synchronousqueue的对比)

Exchanger是一种线程间安全交换数据的机制。可以和之前分析过的SynchronousQueue对比一下：线程A通过SynchronousQueue将数据a交给线程B；线程A通过Exchanger和线程B交换数据，线程A把数据a交给线程B，同时线程B把数据b交给线程A。可见，SynchronousQueue是交给一个数据，Exchanger是交换两个数据。

- 不同JDK实现有何差别？

- 在JDK5中Exchanger被设计成一个容量为1的容器，存放一个等待线程，直到有另外线程到来就会发生数据交换，然后清空容器，等到下一个到来的线程。

- 从JDK6开始，Exchanger用了类似ConcurrentMap的分段思想，提供了多个slot，增加了并发执行时的吞吐量。
