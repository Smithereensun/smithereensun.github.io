{

  "title": "ArrayList深度剖析：源码解读与性能优化",
  "has_date": true,
  "description": "ArrayList介绍 ArrayList**实现了**List**接口，是顺序容器，即元素存放的数据与放进去的顺序相同，允许放入null元素，底层通过**数组实现**。除该类未实现同步外，其余跟**Vector**大致相同。每个**ArrayList**都有一个容量(capacity)，表示底层数",
  "tags": [
    "Java",
    "集合"
  ],
  "source": "local-markdown-library",
  "source_path": "java/collection/02-collection1-arraylist - ArrayList深度剖析：源码解读与性能优化.md",
  "date": "2025-12-21"

}

## [ArrayList介绍](#arraylist介绍)

**ArrayList**实现了**List**接口，是顺序容器，即元素存放的数据与放进去的顺序相同，允许放入null元素，底层通过**数组实现**。除该类未实现同步外，其余跟**Vector**大致相同。每个**ArrayList**都有一个容量(capacity)，表示底层数组的实际大小，容器内存储元素的个数不能多于当前容量。当向容器中添加元素时，如果容量不足，容器会自动增大底层数组的大小。
![](/imported/markdown/2025-12-21-markdown-b5bfb6e9-arraylist深度剖析-源码解读与性能优化/images/9fbb9dd17b05-202404250836769.jpg)
ArrayList 在JDK1.8 前后的实现区别：

- JDK1.7：像饿汉式，直接创建一个初始容量为10的数组

- JDK1.8：像懒汉式，一开始创建一个长度为0的数组，当添加add第一个元素时再创建一个初始容量为10的数组

size(), isEmpty(), get(), set()方法均能在常数时间内完成，add()方法的时间开销跟插入位置有关，addAll()方法的时间开销跟添加元素的个数成正比。其余方法大都是线性时间。

为追求效率，ArrayList没有实现同步(synchronized)，如果需要多个线程并发访问，用户可以手动同步，也可使用Vector替代

## [底层原理介绍](#底层原理介绍)

### [底层数据结构](#底层数据结构)

### [构造方法](#构造方法)

### [自动扩容](#自动扩容)

每当向数组中添加元素时，都要去检查添加后元素的个数是否会超出当前数组的长度，如果超出，数组将会进行扩容，以满足添加数据的需求。

扩容方法流程：

1.
首先获取数组长度

1.
将数组新容量扩容为原数组容量的1.5倍取整

1.
将新容量和当前所需最小容量做对比，(最小容量是在add方法中得到的，minCapacity=size+1，即原数组中元素数量加1)，而newCapacity=elementData.length*1.5，一般来说肯定是1.5倍比+1的大。但是这里要考虑当数组为空时的情况。数组为空又分为两种情况：①指定了数组容量为0 ②没有显式指定数组大小。

- 当数组为空时进行插入操作，因为元素个数size为0，数组容量也为0，那么就会进行扩容操作，对于空数组，扩容1.5倍后你的容量还是为0，那么此时就会小于我所需的最小容量（也就是1）,此时会令 newCapacity = minCapacity;

- 而对于①，传入到grow方法的minCapacity = 1，因此它扩容后的容量就是1

- 对于②，在ensureCapacityInternal方法中，使minCapacity = DEFAULT_CAPACITY（10），因此扩容后的数组长度就是DEFAULT_CAPACITY，也就是10。

    - 原因在于在有参构造方法中使this.elementData = EMPTY_ELEMENTDATA;（无参构造方法中this.elementData = DEFAULTCAPACITY_EMPTY_ELEMENTDATA;），此时在ensureCapacityInternal方法中会对this.elementData进行判断，因此对于①，传入到grow方法的minCapacity = 1；而对于②，minCapacity = Math.max(DEFAULT_CAPACITY, minCapacity)，即minCapacity = 10

1. 最后判断新容量大小是否大于默认数组的最大值（Integer.MAX_VALUE-8），则赋予它整型的最大值

1. 扩容之后，会调用Arrays.copyOf()方法对数组进行拷贝。

实际上，对数组的copy需要创建一个新数组，并对原数组进行复制的操作，这会造成资源消耗。因此在添加大量元素前，建议使用ensureCapacity操作先增加 ArrayList 实例的容量，先进行稍少量数组数据的copy，再添加元素
![](/imported/markdown/2025-12-21-markdown-b5bfb6e9-arraylist深度剖析-源码解读与性能优化/images/f10997db0614-202404250836779.jpg)
### [add(), addAll()](#add-addall)

add 操作可能会导致capacity不足，因此在添加元素之前，都需要进行剩余空间检查，如果需要则自动扩容。扩容操作最终是通过grow()方法完成的。

假设使用的是空参构造，第一次添加元素 add(1)

addAll()方法能够一次添加多个元素，根据位置不同也有两个版本，

- 在末尾添加的`addAll(Collection&lt;? extends E&gt; c)`方法，

- 从指定位置开始插入的`addAll(int index, Collection&lt;? extends E&gt; c)`方法

跟add()方法类似，在插入之前也需要进行空间检查，如果需要则自动扩容；如果从指定位置插入，也会存在移动元素的情况。 addAll()的时间复杂度不仅跟插入元素的多少有关，也跟插入的位置相关。

### [set()](#set)

由于底层是数组，因此set()方法就是直接对数组的指定位置赋值。

### [get()](#get)

由于底层是数组，get()方法也是直接从数组索引处获取值，唯一要注意的是由于底层数组是Object[]，得到元素后需要进行类型转换。

### [remove方法](#remove方法)

remove()方法也有两个

- remove(int index)删除指定位置的元素，

- remove(Object o)删除第一个满足o.equals(elementData[index])的元素。

删除操作是add()操作的逆过程，会需要将删除点之后的元素向前移动一个位置

### [trimToSize()](#trimtosize)

将底层数组的容量调整为当前列表保存的实际元素的大小的功能

### [indexOf(), lastIndexOf()](#indexof-lastindexof)

获取元素的第一次出现的index:

获取元素的最后一次出现的index:

## [遍历时删除（添加）常见陷阱](#遍历时删除-添加-常见陷阱)

### [for循环遍历list](#for循环遍历list)

删除某个元素后，list的大小发生了变化，而索引也在变化，所以会导致遍历的时候漏掉某些元素。比如当删除第1个元素后，继续根据索引访问第2个元素时，因为删除的关系后面的元素都往前移动了一位，所以实际访问的是第3个元素。因此，这种方式可以用在删除特定的一个元素时使用，但不适合循环删除多个元素时使用。

解决办法：从list最后一个元素开始遍历

### [增强for循环](#增强for循环)

删除元素后继续循环会抛异常java.util.ConcurrentModificationException，因为元素在使用的时候发生了并发的修改

解决方法：但只能删除一个"del"元素

### [iterator遍历](#iterator遍历)

这种方式可以正常的循环及删除。但要注意的是，使用iterator的remove方法，如果用list的remove方法同样会报上面提到的ConcurrentModificationException错误。

## [FailFast机制](#failfast机制)

上面提到的ConcurrentModificationException异常，都是有这个机制的存在，通过记录modCount参数来实现。在面对并发的修改时，迭代器很快就会完全失败，而不是冒着在将来某个不确定时间发生任意不确定行为的风险。

fail-fast 机制是java集合(Collection)中的一种错误机制。当多个线程对同一个集合的内容进行操作时，就可能会产生fail-fast事件。例如：当某一个线程A通过iterator去遍历某集合的过程中，若该集合的内容被其他线程所改变了；那么线程A遍历集合时，即出现expectedModCount != modCount 时，就会抛出ConcurrentModificationException异常，产生fail-fast事件。
![](/imported/markdown/2025-12-21-markdown-b5bfb6e9-arraylist深度剖析-源码解读与性能优化/images/da15cc8f1b6a-202404250836775.gif)
fail-fast 机制并不保证在不同步的修改下抛出异常，他只是尽最大努力去抛出，所以这种机制一般仅用于检测 bug

### [解决 fail-fast的解决方案：](#解决-fail-fast的解决方案)

1. 在遍历过程中所有涉及到改变modCount值得地方全部加上synchronized或者直接使用Collections.synchronizedList，这样就可以解决(实际上Vector结构就是这样实现的)。但是不推荐，因为增删造成的同步锁可能会阻塞遍历操作。

1. 使用CopyOnWriteArrayList来替换ArrayList。推荐使用该方案。CopyOnWriteArrayList是兼顾了并发的线程安全

## [ArrayList和Vector和CopyOnWriteArrayList和LinkedList](#arraylist和vector和copyonwritearraylist和linkedlist)

继承关系结构图：
![](/imported/markdown/2025-12-21-markdown-b5bfb6e9-arraylist深度剖析-源码解读与性能优化/images/5bc2b32e4af7-202404250836772.gif)
ArrayList和Vector和CopyOnWriteArrayList的区别：

- ArrayList非线程安全的，如果需要考虑到线程安全问题，那么可以使用Vector和CopyOnWriteArrayList；

- Vector和CopyOnWriteArrayList的区别是：Vector增删改查方法都加了synchronized，保证同步，但是每个方法执行的时候都要去获得锁，性能就会大大下降，而CopyOnWriteArrayList 只是在增删改上加锁，但是读不加锁，在读方面的性能就好于Vector，CopyOnWriteArrayList支持读多写少的并发情况。

ArrayList和LinkedList的区别：

- ArrayList基于动态数组实现；

- LinkedList基于链表实现。对于随机index访问的get和set方法，ArrayList的速度要优于LinkedList。因为ArrayList直接通过数组下标直接找到元素；LinkedList要移动指针遍历每个元素直到找到为止。

- 对于 add(int index, E element)，remove(int index)的操作：LinkedList 和 ArrayList的时间复杂度一样，都是O(n)；虽然时间复杂度一样，但实际执行时间是不一样的，如下代码所示：

虽然ArrayList在索引位置新增或删除数据时需要移动数据（往前移、往后移），但是在连续内存中的块的数据，是可以操作整片内存的。而LinkedList需要一个一个的先查找到具体索引位置的元素，所以在寻址方面数组的效率高于链表。

- 对于add新增元素：理论上来说LinkedList的速度（O(1)）要优于ArrayList（O(n)），因为ArrayList在新增和删除元素时，可能会扩容和复制数组；LinkedList只需要修改指针即可。但在实际测试中，在数据量小的情况下，两者执行时间几乎一致；增大数据量后，就能看出区别了，如下代码所示：

这是因为LinkedList 存在一定的性能问题
