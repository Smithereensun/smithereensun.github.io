{

  "title": "Java集合 常见面试题",
  "has_date": false,
  "description": "集合概述 数组到底是不是对象？ 先说说对象的概念。对象是根据某个类创建出来的一个实例，表示某类事物中一个具体的个体。 对象具有各种属性，并且具有一些特定的行为。站在计算机的角度，对象就是内存中的一个内存块，在这个内存块封装了一些数据，也就是类中定义的各个属性。 所以，对象是用来封装数据的。 java",
  "tags": [
    "面试",
    "Java"
  ],
  "source": "local-markdown-library",
  "source_path": "interview/java/collection - Java集合 常见面试题.md"

}

---

## [集合概述](#集合概述)

### [数组到底是不是对象？](#数组到底是不是对象)

先说说对象的概念。对象是根据某个类创建出来的一个实例，表示某类事物中一个具体的个体。

对象具有各种属性，并且具有一些特定的行为。站在计算机的角度，对象就是内存中的一个内存块，在这个内存块封装了一些数据，也就是类中定义的各个属性。

所以，对象是用来封装数据的。

java中的数组具有java中其他对象的一些基本特点。比如封装了一些数据，可以访问属性，也可以调用方法。

因此，可以说，数组是对象。

也可以通过代码验证数组是对象的事实。比如以下的代码，输出结果为java.lang.Object。

由此，可以看出，数组类的父类就是Object类，那么可以推断出数组就是对象。

### [为什么使用基本类型数组进行Arrays.sort时不能自定义比较器](#为什么使用基本类型数组进行arrays-sort时不能自定义比较器)

Arrays.sort()默认是升序排序，如果要降序排序，需要自定义比较器

报错显示：需要的是int类型，但提供的是T类型的
![](/imported/markdown/undated-markdown-9ce7e709-java集合-常见面试题/images/2ed69d24be1c-202408031537390.png)

这是因为`Arrays.sort`方法有多个重载版本，其中针对基本类型数组（如`int[]`）的版本不接受自定义比较器。

具体来说，`Arrays.sort`有以下几种主要的重载方法：

1. `Arrays.sort(int[] arr)`：用于排序`int`数组，按自然顺序排序，不接受比较器。

1. `Arrays.sort(T[] arr, Comparator&lt;? super T&gt; c)`：用于排序泛型对象数组，按自定义比较器排序。

因此如果试图将一个自定义比较器传入`int`数组的`Arrays.sort`方法，这是不被允许的，因为基本类型数组的排序方法不接受比较器。

一维数组自定义排序可以用如下方法：

### [Comparator与Comparable有什么区别？](#comparator与comparable有什么区别)

Comparator和Comparable都是Java中用于对象排序的接口，它们之间有一些关键的区别。

Comparable接口是在对象自身的类中实现的，它定义了对象的自然排序方式。一个类实现了Comparable接口后，可以使用compareTo方法来比较当前对象和其他对象的大小关系。这个接口只能在对象自身的类中实现，不需要额外的比较器。

Comparator接口是一个独立的比较器，它可以用于对不同类的对象进行排序。Comparator接口允许在对象类之外创建一个单独的比较器类或匿名类，并使用它来定义对象的排序规则。比较器通过实现compare方法来比较两个对象的大小关系。

因此，主要区别如下：

- Comparable接口是在对象自身的类中实现，定义了对象的自然排序方式。

- Comparator接口是一个单独的比较器，定义了用于排序的规则，可以用于不同类的对象排序。

- Comparable是内部排序，对象的类必须实现Comparable接口才能进行排序。

- Comparator是外部排序，可以独立定义排序规则，并与任何类的对象一起使用。

在使用时，如果需要对对象的默认排序进行操作，可以实现Comparable接口。如果需要对不同类的对象进行排序，或者需要定义多种不同的排序规则，可以使用Comparator接口。

### [Java中的集合框架有哪些核心接口？有什么区别？](#java中的集合框架有哪些核心接口-有什么区别)

Java中的集合框架提供了一组接口和类，用于存储和操作数据集合。其中一些核心接口包括：

- Collection接口：是集合框架中最通用的接口，用于表示一组对象。它是List、Set和Queue接口的父接口，定义了对集合进行基本操作的方法。

- List接口：表示一个有序的、可重复的集合。List接口的实现类可以根据元素的插入顺序访问和操作集合中的元素。常见的List接口的实现类有ArrayList、LinkedList和Vector。

- Set接口：表示一个无序的、不可重复的集合。Set接口的实现类不能包含重复的元素。常见的Set接口的实现类有HashSet、TreeSet和LinkedHashSet。

- Queue接口：表示一个先进先出的集合。Queue接口的实现类通常用于实现队列数据结构。常见的Queue接口的实现类有LinkedList和PriorityQueue。

- Map接口：表示一个键值对的映射集合。Map接口中的每个元素由一个键和一个值组成，并且每个键只能在Map中出现一次。常见的Map接口的实现类有HashMap、TreeMap和LinkedHashMap。

### [常见的集合有哪些？](#常见的集合有哪些)

Java集合类主要由两个接口**Collection**和**Map**派生出来的，Collection有三个子接口：List、Set、Queue。

Java集合框架图如下：
![](/imported/markdown/undated-markdown-9ce7e709-java集合-常见面试题/images/6157001eb58c-202409211736331.png)![](/imported/markdown/undated-markdown-9ce7e709-java集合-常见面试题/images/571ba860702e-202409211736556.png)
List代表了有序可重复集合，可直接根据元素的索引来访问；Set代表无序不可重复集合，只能根据元素本身来访问；Queue是队列集合。Map代表的是存储key-value对的集合，可根据元素的key来访问value。

集合体系中常用的实现类有`ArrayList、LinkedList、HashSet、TreeSet、HashMap、TreeMap`等实现类。

### [集合框架底层数据结构总结](#集合框架底层数据结构总结)

**对于本面经中所有不够理解的点，可以查看详细内容进一步深入学习**，都有更详细的解释和原理介绍。

#### [List](#list)

- `ArrayList`：`Object[]` 数组。详细可以查看：ArrayList 源码详解。

- `Vector`：`Object[]` 数组。

- `LinkedList`：双向链表。详细可以查看：LinkedList 源码详解。

#### [Queue](#queue)

- `PriorityQueue`: `Object[]` 数组来实现小顶堆。详细可以查看：PriorityQueue 源码分析。

- `ArrayDeque`: 可扩容动态双向数组。详细可以查看：ArrayQueue 源码分析。

#### [Set](#set)

- `HashSet`(无序，唯一): 基于 `HashMap` 实现的，底层采用 `HashMap` 来保存元素。

- `LinkedHashSet`: `LinkedHashSet` 是 `HashSet` 的子类，并且其内部是通过 `LinkedHashMap` 来实现的。

- `TreeSet`(有序，唯一): 红黑树(自平衡的排序二叉树)。

#### [Map](#map)

- `HashMap`：JDK1.8 之前 `HashMap` 由数组+链表组成的，数组是 `HashMap` 的主体，链表则是主要为了解决哈希冲突而存在的（“拉链法”解决冲突）。JDK1.8 以后在解决哈希冲突时有了较大的变化，当链表长度大于阈值（默认为 8）（将链表转换成红黑树前会判断，如果当前数组的长度小于 64，那么会选择先进行数组扩容，而不是转换为红黑树）时，将链表转化为红黑树，以减少搜索时间。详细可以查看：HashMap 源码分析。

- `LinkedHashMap`：`LinkedHashMap` 继承自 `HashMap`，所以它的底层仍然是基于拉链式散列结构即由数组和链表或红黑树组成。另外，`LinkedHashMap` 在上面结构的基础上，增加了一条双向链表，使得上面的结构可以保持键值对的插入顺序。同时通过对链表进行相应的操作，实现了访问顺序相关逻辑。详细可以查看：LinkedHashMap 源码分析

- `Hashtable`：数组+链表组成的，数组是 `Hashtable` 的主体，链表则是主要为了解决哈希冲突而存在的。

- `TreeMap`：红黑树（自平衡的排序二叉树）。详细可以查看：TreeMap源码分析

#### [并发容器](#并发容器)

- `CopyOnWriteArrayList`：线程安全的`ArrayList`，`CopyOnWriteArrayList`是读写分离的，好处是提高线程访问效率。详细可以查看：CopyOnWriteArrayList详解

- `ConcurrentHashMap`：HashMap是线程不安全的，`ConcurrentHashMap`是一个支持高并发更新与查询的哈希表(基于`HashMap`)。详细可以查看：ConcurrentHashMap详解

- `ConcurrentLinkedQueue`：`ConcurrentLinkedQueue`是基于链接节点的无界线程安全队列。此队列按照FIFO（先进先出）原则对元素进行排序。详细可以查看：ConcurrentLinkedQueue详解

- `BlockingQueue`:BlockingQueue 通常用于一个线程生产对象，而另外一个线程消费这些对象的场景。详细可以查看：BlockingQueue详解

### [如何选用集合?](#如何选用集合)

主要根据集合的特点来选择合适的集合。比如：

- 需要根据键值获取到元素值时就选用 `Map` 接口下的集合，需要排序时选择 `TreeMap`，不需要排序时就选择 `HashMap`，需要保证线程安全就选用 `ConcurrentHashMap`。

- 只需要存放元素值时，就选择实现`Collection` 接口的集合，需要保证元素唯一时选择实现 `Set` 接口的集合比如 `TreeSet` 或 `HashSet`，不需要就选择实现 `List` 接口的比如 `ArrayList` 或 `LinkedList`，然后再根据实现这些接口的集合的特点来选用。

### [Comparable 和 Comparator 的区别](#comparable-和-comparator-的区别)

`Comparable` 接口和 `Comparator` 接口都是 Java 中用于排序的接口，它们在实现类对象之间比较大小、排序等方面发挥了重要作用：

- `Comparable` 接口实际上是出自`java.lang`包 它有一个 `compareTo(Object obj)`方法用来排序

- `Comparator`接口实际上是出自 `java.util` 包它有一个`compare(Object obj1, Object obj2)`方法用来排序

一般我们需要对一个集合使用自定义排序时，我们就要重写`compareTo()`方法或`compare()`方法，当我们需要对某一个集合实现两种排序方式，比如一个 `song` 对象中的歌名和歌手名分别采用一种排序方法的话，我们可以重写`compareTo()`方法和使用自制的`Comparator`方法或者以两个 `Comparator` 来实现歌名排序和歌星名排序，第二种代表我们只能使用两个参数版的 `Collections.sort()`.

## [List](#list-1)

### [ArrayList 了解吗？](#arraylist-了解吗)

`ArrayList` 的底层是动态数组，它的容量能动态增长。在添加大量元素前，应用可以使用`ensureCapacity`操作增加 `ArrayList` 实例的容量。ArrayList 继承了 AbstractList，并实现了 List 接口。

### [ArrayList 和 Array（数组）的区别？](#arraylist-和-array-数组-的区别)

`ArrayList` 内部基于动态数组实现，比 `Array`（静态数组） 使用起来更加灵活：

- `ArrayList`会根据实际存储的元素动态地扩容或缩容，而 `Array` 被创建之后就不能改变它的长度了。

- `ArrayList` 允许使用泛型来确保类型安全，`Array` 则不可以。

- `ArrayList` 中只能存储对象。对于基本类型数据，需要使用其对应的包装类（如 Integer、Double 等）。`Array` 可以直接存储基本类型数据，也可以存储对象。

- `ArrayList` 支持插入、删除、遍历等常见操作，并且提供了丰富的 API 操作方法，比如 `add()`、`remove()`等。`Array` 只是一个固定长度的数组，只能按照下标访问其中的元素，不具备动态添加、删除元素的能力。

- `ArrayList`创建时不需要指定大小，而`Array`创建时必须指定大小。

### [ArrayList 的扩容机制？](#arraylist-的扩容机制)

ArrayList扩容的本质就是计算出新的扩容数组的size后实例化，并将原有数组内容复制到新数组中去。**默认情况下，新的容量会是原容量的1.5倍**。以JDK1.8为例说明:

简要回答：

1. 当 ArrayList 中的元素数量超过其当前容量时，会触发扩容机制。默认情况下，ArrayList 的初始容量为 10。

1. 当发生扩容时，ArrayList 会创建一个新的数组，其容量为原数组的 1.5倍(即 oldcapacity+(oldcapacity &gt;&gt; 1))，然后将原数组中的元素复制到新数组中

1. 复制过程是通过Arrays.copyof()方法实现的。

扩容方法流程：

1. 首先获取数组长度

1. 将数组新容量扩容为原数组容量的1.5倍取整

1. 将新容量和当前所需最小容量做对比，(最小容量是在add方法中得到的，minCapacity=size+1，即原数组中元素数量加1)，而newCapacity=elementData.length*1.5，一般来说肯定是1.5倍比+1的大。但是这里要考虑当数组为空时的情况。数组为空又分为两种情况：①指定了数组容量为0 ②没有显式指定数组大小。

  - 当数组为空时进行插入操作，因为元素个数size为0，数组容量也为0，那么就会进行扩容操作，对于空数组，扩容1.5倍后你的容量还是为0，那么此时就会小于我所需的最小容量（也就是1）,此时会令 newCapacity = minCapacity;

  - 而对于①，传入到grow方法的minCapacity = 1，因此它扩容后的容量就是1

  - 对于②，在ensureCapacityInternal方法中，使minCapacity = DEFAULT_CAPACITY（10），因此扩容后的数组长度就是DEFAULT_CAPACITY，也就是10。

    - 原因在于在有参构造方法中使this.elementData = EMPTY_ELEMENTDATA;（无参构造方法中this.elementData = DEFAULTCAPACITY_EMPTY_ELEMENTDATA;），此时在ensureCapacityInternal方法中会对this.elementData进行判断，因此对于①，传入到grow方法的minCapacity = 1；而对于②，minCapacity = Math.max(DEFAULT_CAPACITY, minCapacity)，即minCapacity = 10

1. 最后判断新容量大小是否大于默认数组的最大值（Integer.MAX_VALUE-8），则赋予它整型的最大值

1. 扩容之后，会调用Arrays.copyOf()方法对数组进行拷贝。

实际上，对数组的copy需要创建一个新数组，并对原数组进行复制的操作，这会造成资源消耗。因此在添加大量元素前，建议使用ensureCapacity操作先增加 ArrayList 实例的容量，先进行稍少量数组数据的copy，再添加元素

### [怎么在遍历 ArrayList 时移除一个元素？](#怎么在遍历-arraylist-时移除一个元素)

foreach删除会导致快速失败问题，可以使用迭代器的 remove() 方法。

### [Arraylist 和 Vector 的区别](#arraylist-和-vector-的区别)

1. ArrayList在内存不够时扩容为原来的1.5倍，Vector是扩容为原来的2倍。

1. Vector属于线程安全级别的，但是大多数情况下不使用Vector，因为操作Vector效率比较低。

### [Vector 和 Stack 的区别？](#vector-和-stack-的区别)

- `Vector` 和 `Stack` 两者都是线程安全的，都是使用 `synchronized` 关键字进行同步处理。

- `Stack` 继承自 `Vector`，是一个后进先出的栈，而 `Vector` 是一个列表。

随着 Java 并发编程的发展，`Vector` 和 `Stack` 已经被淘汰，推荐使用并发集合类（例如 `ConcurrentHashMap`、`CopyOnWriteArrayList` 等）或者手动实现线程安全的方法来提供安全的多线程操作支持。

### [ArrayList 可以添加 null 值吗？](#arraylist-可以添加-null-值吗)

`ArrayList` 中可以存储任何类型的对象，包括 `null` 值。不过，不建议向`ArrayList` 中添加 `null` 值， `null` 值无意义，会让代码难以维护比如忘记做判空处理就会导致空指针异常。

### [ArrayList 插入和删除元素的时间复杂度？](#arraylist-插入和删除元素的时间复杂度)

对于插入：

- 头部插入：由于需要将所有元素都依次向后移动一个位置，因此时间复杂度是 O(n)。

- 尾部插入：当 `ArrayList` 的容量未达到极限时，往列表末尾插入元素的时间复杂度是 O(1)，因为它只需要在数组末尾添加一个元素即可；当容量已达到极限并且需要扩容时，则需要执行一次 O(n) 的操作将原数组复制到新的更大的数组中，然后再执行 O(1) 的操作添加元素。

- 指定位置插入：需要将目标位置之后的所有元素都向后移动一个位置，然后再把新元素放入指定位置。这个过程需要移动平均 n/2 个元素，因此时间复杂度为 O(n)。

对于删除：

- 头部删除：由于需要将所有元素依次向前移动一个位置，因此时间复杂度是 O(n)。

- 尾部删除：当删除的元素位于列表末尾时，时间复杂度为 O(1)。

- 指定位置删除：需要将目标元素之后的所有元素向前移动一个位置以填补被删除的空白位置，因此需要移动平均 n/2 个元素，时间复杂度为 O(n)。

### [LinkedList 插入和删除元素的时间复杂度？](#linkedlist-插入和删除元素的时间复杂度)

- 头部插入/删除：只需要修改头结点的指针即可完成插入/删除操作，因此时间复杂度为 O(1)。

- 尾部插入/删除：只需要修改尾结点的指针即可完成插入/删除操作，因此时间复杂度为 O(1)。

- 指定位置插入/删除：需要先移动到指定位置，再修改指定节点的指针完成插入/删除，因此需要遍历平均 n/2 个元素，时间复杂度为 O(n)。

### [LinkedList 为什么不能实现 RandomAccess 接口？](#linkedlist-为什么不能实现-randomaccess-接口)

`RandomAccess` 是一个标记接口，用来表明实现该接口的类支持随机访问（即可以通过索引快速访问元素）。由于 `LinkedList` 底层数据结构是链表，内存地址不连续，只能通过指针来定位，不支持随机快速访问，所以不能实现 `RandomAccess` 接口。

`ArrayList` 实现了 `RandomAccess` 接口， 而 `LinkedList` 没有实现。为什么呢？`ArrayList` 底层是数组，而 `LinkedList` 底层是链表。数组天然支持随机访问，时间复杂度为 O(1)，所以称为快速随机访问。链表需要遍历到特定位置才能访问特定位置的元素，时间复杂度为 O(n)，所以不支持快速随机访问。`ArrayList` 实现了 `RandomAccess` 接口，就表明了他具有快速随机访问功能。 `RandomAccess` 接口只是标识，并不是说 `ArrayList` 实现 `RandomAccess` 接口才具有快速随机访问功能的！

### [ArrayList 与 LinkedList 区别?](#arraylist-与-linkedlist-区别)

- **是否保证线程安全：**`ArrayList` 和 `LinkedList` 都是不同步的，也就是不保证线程安全；

- **底层数据结构：**`ArrayList` 底层使用的是 **`Object` 数组**；`LinkedList` 底层使用的是 **双向链表** 数据结构（JDK1.6 之前为循环链表，JDK1.7 取消了循环。注意双向链表和双向循环链表的区别！）

- **插入和删除性能受元素位置的影响：**

  - `ArrayList` 采用数组存储，所以插入和删除元素的时间复杂度受元素位置的影响。 比如：执行`add(E e)`方法的时候， `ArrayList` 会默认在将指定的元素追加到此列表的末尾，这种情况时间复杂度就是 O(1)。但是如果要在指定位置 i 插入和删除元素的话（`add(int index, E element)`），时间复杂度就为 O(n)。因为在进行上述操作的时候集合中第 i 和第 i 个元素之后的(n-i) 个元素都要执行向后位/向前移一位的操作。

  - `LinkedList` 采用链表存储，所以在头尾插入或者删除元素不受元素位置的影响（`add(E e)`、`addFirst(E e)`、`addLast(E e)`、`removeFirst()`、 `removeLast()`），时间复杂度为 O(1)，如果是要在指定位置 `i` 插入和删除元素的话（`add(int index, E element)`，`remove(Object o)`,`remove(int index)`）， 时间复杂度为 O(n)，因为需要先移动到指定位置再插入和删除。

- **随机访问性能：**`LinkedList` 不支持高效的随机元素访问，而 `ArrayList`（实现了 `RandomAccess` 接口） 支持。快速随机访问就是通过元素的序号快速获取元素对象(对应于`get(int index)`方法)。

- **内存空间占用：**`ArrayList` 的空间浪费主要体现在在 list 列表的结尾会预留一定的容量空间，而 LinkedList 的空间花费则体现在它的每一个元素都需要消耗比 ArrayList 更多的空间（因为要存放直接后继和直接前驱以及数据）。

### [ArrayList 与 LinkedList 如何选用？](#arraylist-与-linkedlist-如何选用)

一般是不会使用到 `LinkedList` 的，需要用到 `LinkedList` 的场景几乎都可以使用 `ArrayList` 来代替，并且，性能通常会更好！就连 `LinkedList` 的作者约书亚 · 布洛克（Josh Bloch）自己都说从来不会使用 `LinkedList` 。

LinkedList详解这篇文章中有更详细的解释

选择 ArrayList 还是 LinkedList 主要取决于对集合的操作模式：

- 选择 ArrayList 的场景：读多写少，特别是需要频繁地通过索引进行随机访问（get(index)）。

- 选择 LinkedList 的场景：写多读少，特别是需要频繁地在列表的中间、开头或结尾进行插入和删除操作。

也就是说，如果操作模式未知，通常会从 ArrayList 开始，因为其随机访问性能优异，且在大多数常见场景下表现良好。只有当性能分析显示中间增删是瓶颈时，才考虑 LinkedList。

### [LinkedList 一定最适合元素增删场景吗？](#linkedlist-一定最适合元素增删场景吗)

`LinkedList` 仅仅在头尾插入或者删除元素的时候时间复杂度近似 O(1)，其他情况增删元素的平均时间复杂度都是 O(n) 。

且在生产环境中，还是ArrayList的使用远大于 LinkedList 的使用

## [Queue](#queue-1)

### [Queue 与 Deque 的区别](#queue-与-deque-的区别)

`Queue` 是单端队列，只能从一端插入元素，另一端删除元素，实现上一般遵循 **先进先出（FIFO）** 规则。

`Queue` 扩展了 `Collection` 的接口，根据 **因为容量问题而导致操作失败后处理方式的不同** 可以分为两类方法: 一种在操作失败后会抛出异常，另一种则会返回特殊值。

### [讲一下ArrayDeque？](#讲一下arraydeque)

ArrayDeque实现了双端队列，内部使用循环数组实现，默认大小为16。它的特点有：

1. 在两端添加、删除元素的效率较高

1. 根据元素内容查找和删除的效率比较低。

1. 没有索引位置的概念，不能根据索引位置进行操作。

### [ArrayDeque 与 LinkedList 的区别](#arraydeque-与-linkedlist-的区别)

`ArrayDeque` 和 `LinkedList` 都实现了 `Deque` 接口，两者都具有队列的功能，但两者有什么区别呢？

- `ArrayDeque` 是基于可变长的数组和双指针来实现，而 `LinkedList` 则通过链表来实现。

- `ArrayDeque` 不支持存储 `NULL` 数据，但 `LinkedList` 支持。

- `ArrayDeque` 是在 JDK1.6 才被引入的，而`LinkedList` 早在 JDK1.2 时就已经存在。

- `ArrayDeque` 插入时可能存在扩容过程, 不过均摊后的插入操作依然为 O(1)。虽然 `LinkedList` 不需要扩容，但是每次插入数据时均需要申请新的堆空间，均摊性能相比更慢。

从性能的角度上，选用 `ArrayDeque` 来实现队列要比 `LinkedList` 更好。此外，`ArrayDeque` 也可以用于实现栈。

ArrayDeque和LinkedList都是线程不安全的，可以使用Collections工具类中synchronizedXxx()转换成线程同步。

### [说一说 PriorityQueue](#说一说-priorityqueue)

`PriorityQueue` 是在 JDK1.5 中被引入的, 其与 `Queue` 的区别在于元素出队顺序是与优先级相关的，即总是优先级最高的元素先出队。

这里列举其相关的一些要点：

- `PriorityQueue` 利用了二叉堆的数据结构来实现的，底层使用可变长的数组来存储数据

- `PriorityQueue` 通过堆元素的上浮和下沉，实现了在 O(logn) 的时间复杂度内插入元素和删除堆顶元素。

- `PriorityQueue` 是非线程安全的，且不支持存储 `NULL` 和 `non-comparable` 的对象。

- `PriorityQueue` 默认是小顶堆，但可以接收一个 `Comparator` 作为构造参数，从而来自定义元素优先级的先后。

`PriorityQueue` 在面试中可能更多的会出现在手撕算法的时候，典型例题包括堆排序、求第 K 大的数、带权图的遍历等，所以需要会熟练使用才行。

## [Set](#set-1)

### [HashSet底层原理？](#hashset底层原理)

HashSet 基于 HashMap 实现。放入HashSet中的元素实际上由HashMap的key来保存，而HashMap的value则存储了一个静态的Object对象。

### [HashSet、LinkedHashSet 和 TreeSet 的区别？](#hashset、linkedhashset-和-treeset-的区别)

- `HashSet`、`LinkedHashSet` 和 `TreeSet` 都是 `Set` 接口的实现类，都能保证元素唯一，并且都不是线程安全的。

- `HashSet`、`LinkedHashSet` 和 `TreeSet` 的主要区别在于底层数据结构不同。`HashSet` 的底层数据结构是哈希表（基于 `HashMap` 实现）。`LinkedHashSet` 的底层数据结构是链表和哈希表，元素的插入和取出顺序满足 FIFO。`TreeSet` 底层数据结构是红黑树，元素是有序的，排序的方式有自然排序和定制排序。

- 底层数据结构不同又导致这三者的应用场景不同。`HashSet` 用于不需要保证元素插入和取出顺序的场景，`LinkedHashSet` 用于保证元素的插入和取出顺序满足 FIFO 的场景，`TreeSet` 用于支持对元素自定义排序规则的场景。

- `HashSet` 是 `Set` 接口的主要实现类，`HashSet` 的底层是 `HashMap`，线程不安全的，可以存储 null 值；

- `LinkedHashSet` 是 `HashSet` 的子类，能够按照添加的顺序遍历；

- `TreeSet` 底层使用红黑树，能够按照添加元素的顺序进行遍历，排序的方式可以自定义。

### [无序性和不可重复性的含义是什么](#无序性和不可重复性的含义是什么)

- 无序性不等于随机性，无序性是指存储的数据在底层数组中并非按照数组索引的顺序添加，而是根据数据的哈希值决定的。

- 不可重复性是指添加的元素按照 `equals()` 判断时，返回 false，需要同时重写 `equals()` 方法和 `hashCode()` 方法。

## [Map](#map-1)

Map中最常用的集合就是HashMap

HashMap 使用数组+链表+红黑树（JDK1.8增加了红黑树部分）实现的， 链表长度大于8（`TREEIFY_THRESHOLD`）时，会把链表转换为红黑树，红黑树节点个数小于6（`UNTREEIFY_THRESHOLD`）时才转化为链表，防止频繁的转化。

### [解决hash冲突的办法有哪些？HashMap用的哪种？](#解决hash冲突的办法有哪些-hashmap用的哪种)

解决Hash冲突方法有：拉链法、开放地址法、再散列法。HashMap中采用的是 拉链法 。

- 开放定址法基本思想就是，如果`p=H(key)`出现冲突时，则以`p`为基础，再次hash，`p1=H(p)`,如果p1再次出现冲突，则以p1为基础，以此类推，直到找到一个不冲突的哈希地址`pi`。 因此开放定址法所需要的hash表的长度要大于等于所需要存放的元素，而且因为存在再次hash，所以`只能在删除的节点上做标记，而不能真正删除节点。`

- 再哈希法提供多个不同的hash函数，当`R1=H1(key1)`发生冲突时，再计算`R2=H2(key1)`，直到没有冲突为止。 这样做虽然不易产生堆集，但增加了计算的时间。

- 拉链法将哈希值相同的元素构成一个同义词的单链表，并将单链表的头指针存放在哈希表的第i个单元中，查找、插入和删除主要在同义词链表中进行。链表法适用于经常进行插入和删除的情况。

详细可以看这里的介绍解决哈希冲突的三种方法

### [HashMap使用的hash算法？](#hashmap使用的hash算法)

Hash算法：取key的hashCode值、高位运算、取模运算。

在JDK1.8的实现中，优化了高位运算的算法，通过`hashCode()`的高16位异或低16位实现的：这么做可以在数组比较小的时候，也能保证考虑到高低位都参与到Hash的计算中，可以减少冲突，同时不会有太大的开销。

### [为什么建议设置HashMap的容量？](#为什么建议设置hashmap的容量)

HashMap有扩容机制，就是当达到扩容条件时会进行扩容。扩容条件就是当HashMap中的元素个数超过临界值时就会自动扩容（threshold = loadFactor * capacity）。

如果没有设置初始容量大小，随着元素的不断增加，HashMap会发生多次扩容。而HashMap每次扩容都需要重建hash表，非常影响性能。所以建议开发者在创建HashMap的时候指定初始化容量。

### [hashCode()和equals()的重要性:](#hashcode-和equals-的重要性)

hashMap的键必须实现 hashCode() 和equals()方法。hashCode()用于计算哈希值，以决定键的存绪位置，而 equals() 用于比较两个键是否相同，在put 操作时，如果两个键的 hashCode() 相同，但 equals() 返回 false,则这两个键会被视为不同的键，存储在同一个桶的不同位置。

误用 hashcode()和 equals()会导致 Hashmap 中的元素无法正常查找或插入。

### [HashMap扩容过程是怎样的？](#hashmap扩容过程是怎样的)

1.8扩容机制：当元素个数大于`threshold`时，会进行扩容，使用2倍容量的数组代替原有数组。采用尾插入的方式将原数组元素拷贝到新数组。1.8扩容之后链表元素相对位置没有变化，而1.7扩容之后链表元素会倒置。

1.7链表新节点采用的是**头插法**，这样在线程一扩容迁移元素时，会将元素顺序改变，导致两个线程中出现元素的相互指向而形成循环链表，1.8采用了尾插法，避免了这种情况的发生。

原数组的元素在重新计算hash之后，因为数组容量n变为2倍，那么n-1的mask范围在高位多1bit。在元素拷贝过程不需要重新计算元素在数组中的位置，只需要看看原来的hash值新增的那个bit是1还是0，是0的话索引没变，是1的话索引变成“原索引+oldCap”（根据`e.hash & oldCap == 0`判断） 。这样可以省去重新计算hash值的时间，而且由于新增的1bit是0还是1可以认为是随机的，因此resize的过程会均匀的把之前的冲突的节点分散到新的bucket。

### [HashMap 扩容机制的性能影响](#hashmap-扩容机制的性能影响)

扩容触发条件：当 HashMap 中的元素数量超过 `容量x负载因子` 时，会触发扩容。扩容会将容量扩展为当前容量的两倍，并将所有键值对重新分配到新的桶(bucket)中。

性能影响：扩容是一个耗时的操作，因为它需要重新计算每个键的哈希值，并将键值对重新分配到新的桶中。因此，频繁的扩容会显著影响性能，特别是在存储大量数据时。

### [为什么 HashMap 在扩容时采用2的n次方倍?](#为什么-hashmap-在扩容时采用2的n次方倍)

原因是：为了能让 HashMap 存取高效，尽量较少碰撞，也就是要尽量把数据分配均匀。

HasMap通过(n - 1)&hash来计算元素存储的索引位置，这种位运算只有在数组容量是2的n次方时才能确保索引均匀分布，位运算的效率高于取模运算(hash%n)，提高了哈希计算的读度

且当 hashMap扩容时，通过容量为2的n次方，扩容时只需通过简单的位运算判断是否需要迁移，这减少了重新计算哈希值的开销，提升了 rehash 的效率。

### [说说HashMap的put方法流程？](#说说hashmap的put方法流程)

put方法流程：

1.
如果table没有初始化就先进行初始化过程

1.
使用hash算法计算key的索引判断索引处有没有存在元素，没有就直接插入

1.
如果索引处存在元素，则遍历插入，有两种情况，

- 一种是链表形式就直接遍历到尾端插入，

- 一种是红黑树就按照红黑树结构

1.
插入链表的数量大于阈值8，且数组大小已经大等于64，就要转换成红黑树的结构

1.
添加成功后会检查是否需要扩容

![](/imported/markdown/undated-markdown-9ce7e709-java集合-常见面试题/images/3a922cb956df-202409211736564.png)
### [红黑树的特点？](#红黑树的特点)

- 每个节点或者是黑色，或者是红色。

- 根节点和叶子节点（`NIL`）是黑色的。

- 如果一个节点是红色的，则它的子节点必须是黑色的。

- 从一个节点到该节点的子孙节点的所有路径上包含相同数目的黑节点。

### [在解决 hash 冲突的时候，为什么选择先用链表，再转红黑树?](#在解决-hash-冲突的时候-为什么选择先用链表-再转红黑树)

因为红黑树需要进行左旋，右旋，变色这些操作来保持平衡，而单链表不需要。所以，当元素个数小于8个的时候，采用链表结构可以保证查询性能。而当元素个数大于8个的时候并且数组容量大于等于64，会采用红黑树结构。因为红黑树搜索时间复杂度是 `O(logn)`，而链表是 `O(n)`，在n比较大的时候，使用红黑树可以加快查询速度。

### [HashMap默认加载因子是多少？为什么是 0.75？](#hashmap默认加载因子是多少-为什么是-0-75)

先看下HashMap的默认构造函数：

Node[] table的初始化长度length为16，默认的loadFactor是0.75

为什么默认负载因子是 0.75？官方答案如下：

As a general rule, the default load factor (.75) offers a good tradeoff between time and space costs. Higher values decrease the space overhead but increase the lookup cost (reflected in most of the operations of the HashMap class, including get and put). The expected number of entries in the map and its load factor should be taken into account when setting its initial capacity, so as to minimize the number of rehash operations. If the initial capacity is greater than the maximum number of entries divided by the load factor, no rehash operations will ever occur.

上面的意思，简单来说是默认负载因子为 0.75，是因为它提供了空间和时间复杂度之间的良好平衡。 负载因子太低会导致大量的空桶浪费空间，负载因子太高会导致大量的碰撞，降低性能。0.75 的负载因子在这两个因素之间取得了良好的平衡。也就是说官方并未对负载因子为 0.75 做过多的解释，只是大概的说了一下，0.75 是空间和时间复杂度的平衡，但更多的细节是未做说明的，Stack Overflow 进行了[负载因子的科学推测](https://stackoverflow.com/questions/10901752/what-is-the-significance-of-load-factor-in-hashmap)，感兴趣的可以学习学习

也就是说所，0.75是对空间和时间效率的一个平衡选择，根据泊松分布，loadFactor 取0.75碰撞最小。一般不会修改，除非在时间和空间比较特殊的情况下 ：

- 如果内存空间很多而又对时间效率要求很高，可以降低负载因子Load factor的值 。

- 如果内存空间紧张而对时间效率要求不高，可以增加负载因子loadFactor的值，这个值可以大于1。

### [一般用什么作为HashMap的key?](#一般用什么作为hashmap的key)

一般用`Integer`、`String`这种不可变类当 HashMap 当 key。String类比较常用。

- 因为 String 是不可变的，所以在它创建的时候`hashcode`就被缓存了，不需要重新计算。这就是 HashMap 中的key经常使用字符串的原因。

- 获取对象的时候要用到 `equals()` 和 `hashCode()` 方法，而Integer、String这些类都已经重写了 `hashCode()` 以及 `equals()` 方法，不需要自己去重写这两个方法。

### [使用 HashMap 时，有哪些提升性能的技巧?](#使用-hashmap-时-有哪些提升性能的技巧)

- 合理设置初始容量:如果在使用时可以预估 HashMap 存储的数据量大小，那么需要在创建时设置一个合适的初始容量，以避免频繁的扩容操作。Java 中 HashMap 默认初始容量是 16。

- 调整负载因子:官方提供的默认负载因子是 0.75。可以根据具体应用场景调整这个值，较低的负载因子会减少冲突，提高查找效率，但会占用更多内存，较高的负载因子则会减少内存消耗，但可能增加)冲突的概率，降低查找效率。

- 确保 hashCode 均匀分布：对应 key 的 hashCode() 方法生成的哈希值需均匀分布，减少哈希冲突。避免使用质量不高的哈希函数，防止大量键映射到相同的槽位上，造成性能瓶颈。

### [HashMap为什么线程不安全？](#hashmap为什么线程不安全)

- 多线程下扩容死循环。JDK1.7中的 HashMap 使用头插法插入元素，在多线程的环境下，扩容的时候有可能导致**环形链表**的出现，形成死循环。

- 在JDK1.8中，在多线程环境下，put不安全，会发生**数据覆盖**的情况。

JDK1.8中，put的不安全

由于多线程对HashMap进行put操作，调用了HashMap的putVal()，具体原因：

1.
假设两个线程A、B都在进行put操作，并且hash函数计算出的插入下标是相同的；
 2. 当线程A执行完第6行由于时间片耗尽导致被挂起，而线程B得到时间片后在该下标处插入了元素，完成了正常的插入；
 3. 接着线程A获得时间片，由于之前已经进行了hash碰撞的判断，所以此时不会再进行判断，而是直接进行插入；
 4. 最终就导致了线程B插入的数据被线程A覆盖了，从而线程不安全。

1.
代码的第38行处有个++size，线程A、B，这两个线程同时进行put操作时，假设当前HashMap的zise大小为10；
 6. 当线程A执行到第40行代码时，从主内存中获得size的值为10后准备进行+1操作，但是由于时间片耗尽只好让出CPU；
 7. 接着线程B拿到CPU后从主内存中拿到size的值10进行+1操作，完成了put操作并将size=11写回主内存；
 8. 接着线程A再次拿到CPU并继续执行(此时size的值仍为10)，当执行完put操作后，还是将size=11写回内存；
 9. 此时，线程A、B都执行了一次put操作，但是size的值只增加了1，所有说还是由于数据覆盖又导致了线程不安全。

### [HashMap和HashTable的区别？](#hashmap和hashtable的区别)

HashMap和Hashtable都实现了Map接口。

1. null值：HashMap可以接受为null的key和value，key为null的键值对放在下标为0的头结点的链表中，而Hashtable则不行。

1. 线程安全性：HashMap是非线程安全的，HashTable是线程安全的。Jdk1.5提供了ConcurrentHashMap，它是HashTable的替代。 因为线程安全的问题，`HashMap` 要比 `Hashtable` 效率高一点。另外，`Hashtable` 基本被淘汰，不要在代码中使用它；

1. 继承和接口实现：Hashtable继承自Dictionary类，而HashMap则继承自AbstractMap类并实现了Map接口。

1. 使用性能：Hashtable很多方法是同步方法，在单线程环境下它比HashMap要慢。

1. 哈希值的使用不同：HashTable直接使用对象的hashCode。而HashMap重新计算hash值。

1. 初始容量和扩容机制：Hashtable在创建时必须指定容量大小，且默认大小为11。而HashMap可以在创建时不指定容量大小，系统会自动分配初始容量，并采用2倍扩容机制。

1. 迭代器：迭代器 Iterator 对 Hashtable 是安全的，而 Iterator 对 HashMap 不是安全的，因为迭代器被设计为工作于一个快照上，如果在迭代过程中其他线程修改了 HashMap，则会抛出并发修改异常。

### [HashMap 和 HashSet 区别?](#hashmap-和-hashset-区别)

如果看过 `HashSet` 源码的话就应该知道：`HashSet` 底层就是基于 `HashMap` 实现的。（`HashSet` 的源码非常非常少，因为除了 `clone()`、`writeObject()`、`readObject()`是 `HashSet` 自己不得不实现之外，其他方法都是直接调用 `HashMap` 中的方法。

### [讲一下TreeMap？](#讲一下treemap)

TreeMap是一个能比较元素大小的Map集合，会对传入的key进行了大小排序。可以使用元素的自然顺序，也可以使用集合中自定义的比较器来进行排序。

TreeMap 的继承结构：
![](/imported/markdown/undated-markdown-9ce7e709-java集合-常见面试题/images/21826f2eb9e7-202409211736525.png)
**TreeMap的特点：**

1. TreeMap是有序的key-value集合，通过红黑树实现。根据键的自然顺序进行排序或根据提供的Comparator进行排序。

1. TreeMap继承了AbstractMap，实现了NavigableMap接口，支持一系列的导航方法，给定具体搜索目标，可以返回最接近的匹配项。如floorEntry()、ceilingEntry()分别返回小于等于、大于等于给定键关联的Map.Entry()对象，不存在则返回null。lowerKey()、floorKey、ceilingKey、higherKey()只返回关联的key。

### [HashMap 和 TreeMap 区别?](#hashmap-和-treemap-区别)

`TreeMap` 和`HashMap` 都继承自`AbstractMap`，但是需要注意的是`TreeMap`它还实现了`NavigableMap`接口和`SortedMap` 接口。

实现 `NavigableMap` 接口让 `TreeMap` 有了对集合内元素的搜索的能力。

`NavigableMap` 接口提供了丰富的方法来探索和操作键值对:

1. **定向搜索**: `ceilingEntry()`, `floorEntry()`, `higherEntry()`和 `lowerEntry()` 等方法可以用于定位大于、小于、大于等于、小于等于给定键的最接近的键值对。

1. **子集操作**: `subMap()`, `headMap()`和 `tailMap()` 方法可以高效地创建原集合的子集视图，而无需复制整个集合。

1. **逆序视图**:`descendingMap()` 方法返回一个逆序的 `NavigableMap` 视图，使得可以反向迭代整个 `TreeMap`。

1. **边界操作**: `firstEntry()`, `lastEntry()`, `pollFirstEntry()`和 `pollLastEntry()` 等方法可以方便地访问和移除元素。

这些方法都是基于红黑树数据结构的属性实现的，红黑树保持平衡状态，从而保证了搜索操作的时间复杂度为 O(log n)，这让 `TreeMap` 成为了处理有序集合搜索问题的强大工具。

实现`SortedMap`接口让 `TreeMap` 有了对集合中的元素根据键排序的能力。默认是按 key 的升序排序，也可以指定排序的比较器。

### [LinkedHashMap底层原理？](#linkedhashmap底层原理)

HashMap是无序的，迭代HashMap所得到元素的顺序并不是它们最初放到HashMap的顺序，即不能保持它们的插入顺序。

LinkedHashMap继承于HashMap，是HashMap和LinkedList的融合体，具备两者的特性。每次put操作都会将entry插入到双向链表的尾部。

使用场景：

- 缓存实现：可以根据访问顺序移除最久未使用的元素，常用于LRU(Least Recently Used)缓存

- 数据存储：需要保持元素插入顺序的场景。

### [IdentityHashMap 是什么?](#identityhashmap-是什么)

IcentibHishnep是 一个 Map 实现，和普通的 HashMap 不同，它使用**引用相等性 (reference equality)作为健的比较方式**。换句话说，它使用 == 来比较键，而不是 equals 方法，因此，只有当两个键的引用相同时，才被认为是相同的键。

使用场景:

- 对象身份区分：适用于需要基于对象身份(引用)进行区分的场景，比如需要跟踪对象实例，而不是逻辑上的值相等性。

- 特殊缓存：有时用于构建缓存或映射结构，确保即使两个对象内容相同，但只要它们是不同的实例，就会被当作不同的键

主要特性：

- 引用相等：IdentityHashmap 使用 == 比较键的相等性，而不是通过 equals()，这使得它适合那些需要基于对象身份(引用)的场景。

- 哈希实现：虽然名字中有"Hash"，但 IdentityHashmap并不使用对象的 hashcode()方法，而是依赖 system.identityHashcode()，这是基于对象引用的哈希值。

- 允许 null 键和 null 值：类似 HashMap， IdentityHashmap也允许 null 键和 null 值，但它使用的是对 null 的引用比较。

- 非线程安全：与 HashMap类似，IdentityHashmap 不是线程安全的，在多线程环境下需要手动同步。

### [WeakHashMap 是什么?](#weakhashmap-是什么)

WeakHashMap 是 一个特殊的的 Map 实现，它使用弱引用(Weak Reference)作为键，弱引用允许垃圾回收器在没有其他强引用指向该对象时回收它的内存。因此，当一个键不再被其他对象引用时，会自动删除与该键相关联的条目。

常用于缓存(内存敏感场景)的实现。当缓存中的键不再被其他地方引用时，可以自动移除相应的缓存条目，节省内存，防止内存泄漏。

## [并发容器](#并发容器-1)

JDK 提供的这些容器大部分在 `java.util.concurrent` 包中。

- **ConcurrentHashMap:** 线程安全的 HashMap

- **CopyOnWriteArrayList:** 线程安全的 List，在读多写少的场合性能非常好，远远好于 Vector.

- **ConcurrentLinkedQueue:** 高效的并发队列，使用链表实现。可以看做一个线程安全的 LinkedList，这是一个非阻塞队列。

- **BlockingQueue:** 阻塞队列接口，JDK 内部通过链表、数组等方式实现了这个接口。非常适合用于作为数据共享的通道。

- **ConcurrentSkipListMap:** 跳表的实现。使用跳表的数据结构进行快速查找。

### [什么是fail fast？](#什么是fail-fast)

**边遍历边修改集合**就会产生fast-fail事件，抛出 ConcurrentModificationException 异常

fast-fail是Java集合的一种错误机制。当多个线程对同一个集合进行操作时，就有可能会产生fast-fail事件。例如：当线程a正通过iterator遍历集合时，另一个线程b修改了集合的内容，此时modCount（记录集合操作过程的修改次数）会加1，不等于expectedModCount，那么线程a访问集合的时候，就会抛出ConcurrentModificationException，产生fast-fail事件。

解决方法：

- 使用Colletions.synchronizedList方法或在修改集合内容的地方加上synchronized。这样的话，增删集合内容的同步锁会阻塞遍历操作，影响性能。

- 使用CopyOnWriteArrayList来替换ArrayList。在对CopyOnWriteArrayList进行修改操作的时候，会拷贝一个新的数组，对新的数组进行操作，操作完成后再把引用移到新的数组。

### [什么是fail safe？](#什么是fail-safe)

采用安全失败机制的集合容器，在遍历时不是直接在集合内容上访问的，而是先复制原有集合内容，在拷贝的集合上进行遍历。java.util.concurrent包下的容器都是fail safe，可以在多线程下并发使用，并发修改。

**原理**：由于迭代时是对原集合的拷贝进行遍历，所以在遍历过程中对原集合所作的修改并不能被迭代器检测到，所以不会触发Concurrent Modification Exception。

**缺点**：基于拷贝内容的优点是避免了Concurrent Modification Exception，但同样地，迭代器并不能访问到修改后的内容，即：迭代器遍历的是开始遍历那一刻拿到的集合拷贝，在遍历期间原集合发生的修改迭代器是不知道的。

### [哪些集合类是线程安全的？哪些不安全？](#哪些集合类是线程安全的-哪些不安全)

线性安全的集合类：

- Vector：比ArrayList多了同步机制。

- Hashtable。

- ConcurrentHashMap：是一种高效并且线程安全的集合。

- Stack：栈，也是线程安全的，继承于Vector。

线性不安全的集合类：

- Hashmap

- Arraylist

- LinkedList

- HashSet

- TreeSet

- TreeMap

### [迭代器 Iterator 是什么？](#迭代器-iterator-是什么)

Iterator模式用同一种逻辑来遍历集合。它可以把访问逻辑从不同类型的集合类中抽象出来，不需要了解集合内部实现便可以遍历集合元素，统一使用 Iterator 提供的接口去遍历。它的特点是更加安全，因为它可以保证，在当前遍历的集合元素被更改的时候，就会抛出 ConcurrentModificationException 异常。

主要有三个方法：hasNext()、next()和remove()。

### [Iterator 和 ListIterator 有什么区别？](#iterator-和-listiterator-有什么区别)

ListIterator 是 Iterator的增强版。

- ListIterator遍历可以是逆向的，因为有previous()和hasPrevious()方法，而Iterator不可以。

- ListIterator有add()方法，可以向List添加对象，而Iterator却不能。

- ListIterator可以定位当前的索引位置，因为有nextIndex()和previousIndex()方法，而Iterator不可以。

- ListIterator可以实现对象的修改，set()方法可以实现。Iierator仅能遍历，不能修改。

- ListIterator只能用于遍历List及其子类，Iterator可用来遍历所有集合。

### [lterator 与 for-each 循环的关系](#lterator-与-for-each-循环的关系)

for-each 循环实际上是对 Iterator 的一种简化形式，背后是通过 Iterator 实现的。

不过 for-each 适合只遍历集合而不进行删除等操作。如果需要在遍历过程中修改集合内容，则需要使用 Iterator。

因为 itenator在遍历集合的过程中，如果检测到集合的结构发生了非送代器自身的修改 (比如使用 List#add()、List#remove()直接修改集合，会抛出 concurentModificationException。这种机制称为“fail-fast”。

为了避免这种情况发生，修改集合时应使用 Iterator的remove()方法，而非直接操作集合。

### [如何让一个集合不能被修改？](#如何让一个集合不能被修改)

可以采用Collections包下的unmodifiableMap/unmodifiableList/unmodifiableSet方法，通过这个方法返回的集合，是不可以修改的。如果修改的话，会抛出 java.lang.UnsupportedOperationException异常。

对于List/Set/Map集合，Collections包都有相应的支持。

当然，用Guava工具的 Immutable 类更好，比Collections包更有优势，详情请看集合 - Immutable&Lists&Maps&Sets

**那使用final关键字进行修饰可以实现吗？**

答案是不可以。

final关键字修饰的成员变量如果是是引用类型的话，则表示这个引用的地址值是不能改变的，但是这个引用所指向的对象里面的内容还是可以改变的。

而集合类都是引用类型，用final修饰的话，集合里面的内容还是可以修改的。

### [CopyOnWrite](#copyonwrite)

Copy-On-Write，写时复制。当我们往容器添加元素时，不直接往容器添加，而是先将当前容器进行复制，复制出一个新的容器，然后往新的容器添加元素，添加完元素之后，再将原容器的引用指向新容器。这样做的好处就是可以对`CopyOnWrite`容器进行并发的读而不需要加锁，因为当前容器不会被修改。

从JDK1.5开始Java并发包里提供了两个使用CopyOnWrite机制实现的并发容器，它们是`CopyOnWriteArrayList`和`CopyOnWriteArraySet`。

**缺点：**

- 内存占用问题。由于CopyOnWrite的写时复制机制，在进行写操作的时候，内存里会同时驻扎两个对象的内存。

- CopyOnWrite容器不能保证数据的实时一致性，可能读取到旧数据。

### [CopyOnWriteArrayList](#copyonwritearraylist)

**CopyOnWriteArrayList**是Java并发包中提供的一个并发容器。CopyOnWriteArrayList相当于线程安全的ArrayList，CopyOnWriteArrayList使用了一种叫写时复制的方法，当有新元素add到CopyOnWriteArrayList时，先从原有的数组中拷贝一份出来，然后在新的数组做写操作，写完之后，再将原来的数组引用指向到新数组。

`CopyOnWriteArrayList`中add方法添加的时候是需要加锁的，保证同步，避免了多线程写的时候复制出多个副本。读的时候不需要加锁，如果读的时候有其他线程正在向`CopyOnWriteArrayList`添加数据，还是可以读到旧的数据。

#### [CopyOnWriteArrayList 和Vector的区别](#copyonwritearraylist-和vector的区别)

- CopyOnWriteArrayList的写效率比Vector慢。当CopyOnWriteArrayList写元素时是通过备份数组的方式实现的，当多线程同步激烈，数据量较大时会不停的**复制数组，内存浪费严重**。如果原数组的内容比较多的情况下，可能导致young gc或者full gc

- 弱一致性：不能用于实时读的场景，像拷贝数组、新增元素都需要时间，所以读取数据可能是旧的，虽然CopyOnWriteArrayList 能做到最终一致性，但是还是没法满足实时性要求；

CopyOnWriteArrayList合适读多写少的场景，例如黑名单白名单等

### [CopyOnWriteArrayList 和 Collections.synchronizedList 有什么区别?分别有什么优缺点?](#copyonwritearraylist-和-collections-synchronizedlist-有什么区别-分别有什么优缺点)

CopyOnWriteArrayList：是一个线程安全的 List 实现，特性就是写时复制。

每次对 List 的修改操作(如 add,set,remove)都会复制创建一个新的底层数组。读操作不需要加锁，写操作需要加锁。

优点：
 读操作无锁：每次写操作都会创建并复制新数组，所以读写之间不冲突，因此读操作不需要加锁，能够提供非常高效的并发读性能。

缺点：

- 写操作开销大：每次写操作都会创建并复制新数组，且要将数据复制到新的数组中，在写操作频繁的场景下性能会较低。

- 内存消耗大：每次写操作都会创建并复制新数组，在数据量大的情况下，同一时刻会存在两倍 List 大小的内存占用，开销较大。

CopyOnwriteArrayList 适合读多写少的场景。

Collections.synchronizedList：是一个包装方法，可以将任何 list 转换为线程安全的版本，它会对每个访问方法(如 get, set add,remove)进行同步(加 synchronized 锁)，从而保证线程安全。

优点：方便，简单一个方法就可以将 List 变为线程安全版本，非常方便。

缺点：并发低，读写操作都需要加锁，高并发场景下性能不高。

Collections.synchronizedList 适用于简单将 List 转为线程安全版本临时使用的场景。特定的场景还需使用并发度高的JUC 类，可以说，在显示生产环境中没见过用这个类的

### [ConcurrentHashMap](#concurrenthashmap)

多线程环境下，使用Hashmap进行put操作会造成数据覆盖，应该使用支持多线程的 ConcurrentHashMap。

JDK1.8 ConcurrentHashMap取消了segment分段锁，而采用CAS和synchronized来保证并发安全。数据结构采用数组+链表/红黑二叉树。synchronized只锁定当前链表或红黑二叉树的首节点，相比1.7锁定HashEntry数组，锁粒度更小，支持更高的并发量。当链表长度过长时，Node会转换成TreeNode，提高查找速度。

#### [ConcurrentHashMap原理？put执行流程？](#concurrenthashmap原理-put执行流程)

回顾hashMap的put方法过程

1. 计算出key的槽位

1. 根据槽位类型进行操作(链表，红黑树)

1. 根据槽位中成员数量进行数据转换，扩容等操作

![](/imported/markdown/undated-markdown-9ce7e709-java集合-常见面试题/images/88cf94c5a4e7-202409211744062.gif)
如何高效的执行并发操作：根据上面hashMap的数据结构可以直观的看到，如果以整个容器为一个资源进行锁定，那么就变为了串行操作。而根据hash表的特性，具有冲突的操作只会出现在同一槽位，而与其它槽位的操作互不影响。基于此种判断，那么就可以将资源锁粒度缩小到槽位上，这样热点一分散，冲突的概率就大大降低，并发性能就能得到很好的增强。
![](/imported/markdown/undated-markdown-9ce7e709-java集合-常见面试题/images/4543616647e3-202409211744019.gif)
总体上来说，就是采用 `Node + CAS + synchronized` 来保证并发安全。数据结构跟 `HashMap` 1.8 的结构类似，数组+链表/红黑二叉树。Java 8 在链表长度超过一定阈值（8）时将链表（时间复杂度为 O(N)）转换为红黑树（时间复杂度为 O(log(N))）。

Java 8 中，锁粒度更细，`synchronized` 只锁定当前链表或红黑二叉树的首节点，这样只要 hash 不冲突，就不会产生并发，就不会影响其他 Node 的读写，效率大幅提升。

#### [ConcurrentHashMap 的get 方法是否需要加锁?](#concurrenthashmap-的get-方法是否需要加锁)

不需要加锁。

通过 volatile 关键字，concurentHashmap能够确保 get 方法的线程安全，即使在写入发生时，读取线程仍然能够获得最新的数据，不会引发并发问题

具体是通过 unsafe#getxxxvolatile 和用 volatile 来修饰节点的 val 和 next 指针来实现的。

#### [ConcurrentHashMap 和 Hashtable 的区别？](#concurrenthashmap-和-hashtable-的区别)

相同点：ConcurrentHashMap 和 Hashtable 都是线程安全的，可以在多个线程同时访问它们而不需要额外的同步措施。

不同点：

1. Hashtable通过使用synchronized修饰方法的方式来实现多线程同步，因此，Hashtable的同步会锁住整个数组。在高并发的情况下，性能会非常差。ConcurrentHashMap采用了使用数组+链表+红黑树数据结构和CAS原子操作实现；synchronized锁住桶，以及大量的CAS操作来保证线程安全。

1. Hashtable 读写操作都加锁，ConcurrentHashMap的读操作不加锁，写操作加锁

1. Hashtable默认的大小为11，当达到阈值后，每次按照下面的公式对容量进行扩充：newCapacity = oldCapacity * 2 + 1。ConcurrentHashMap默认大小是16，扩容时容量扩大为原来的2倍。

1. Null 键和值： ConcurrentHashMap 不允许存储 null 键或 null 值，如果尝试存储 null 键或值，会抛出 NullPointerException。 Hashtable 也不允许存储 null 键和值。

#### [为什么JDK8不用ReentrantLock而用synchronized](#为什么jdk8不用reentrantlock而用synchronized)

- 减少内存开销：如果使用ReentrantLock则需要节点继承AQS来获得同步支持，增加内存开销，而1.8中只有头节点需要进行同步。

- 内部优化：synchronized则是JVM直接支持的，JVM能够在运行时作出相应的优化措施：锁粗化、锁消除、锁自旋等等。

#### [为什么key 和 value 不允许为 null](#为什么key-和-value-不允许为-null)

HashMap中，null可以作为键或者值都可以。而在ConcurrentHashMap中，key和value都不允许为null。

ConcurrentHashMap的作者——Doug Lea的解释如下：
![](/imported/markdown/undated-markdown-9ce7e709-java集合-常见面试题/images/525924656567-202409211745524.gif)
主要意思就是说：

ConcurrentMap（如ConcurrentHashMap、ConcurrentSkipListMap）不允许使用null值的主要原因是，在非并发的Map中（如HashMap)，是可以容忍模糊性（二义性）的，而在并发Map中是无法容忍的。

假如说，所有的Map都支持null的话，那么map.get(key)就可以返回null，但是，这时候就会存在一个不确定性，当你拿到null的时候，你是不知道他是因为本来就存了一个null进去还是说就是因为没找到而返回了null。

在HashMap中，因为它的设计就是给单线程用的，所以当我们map.get(key)返回null的时候，我们是可以通过map.contains(key)检查来进行检测的，如果它返回true，则认为是存了一个null，否则就是因为没找到而返回了null。

但是，像ConcurrentHashMap，它是为并发而生的，它是要用在并发场景中的，当我们map.get(key)返回null的时候，是没办法通过map.contains(key)(ConcurrentHashMap有这个方法，但不可靠)检查来准确的检测，因为在检测过程中可能会被其他线程锁修改，而导致检测结果并不可靠。

所以，为了让ConcurrentHashMap的语义更加准确，不存在二义性的问题，他就不支持null。

#### [集合线程安全不等于业务安全](#集合线程安全不等于业务安全)

需要知道的是，集合线程安全并不等于业务线程安全，并不是说使用了线程安全的集合 如ConcurrentHashMap 就能保证业务的线程安全。这是因为，ConcurrentHashMap只能保证put时是安全的，但是在put操作前如果还有其他的操作，那业务并不一定是线程安全的。

例如存在复合操作，也就是存在多个基本操作(如`put`、`get`、`remove`、`containsKey`等)组成的操作，例如先判断某个键是否存在`containsKey(key)`，然后根据结果进行插入或更新`put(key, value)`。这种操作在执行过程中可能会被其他线程打断，导致结果不符合预期。

例如，有两个线程 A 和 B 同时对 `ConcurrentHashMap` 进行复合操作，如下：

如果线程 A 和 B 的执行顺序是这样：

1. 线程 A 判断 map 中不存在 key

1. 线程 B 判断 map 中不存在 key

1. 线程 B 将 (key, anotherValue) 插入 map

1. 线程 A 将 (key, value) 插入 map

那么最终的结果是 (key, value)，而不是预期的 (key, anotherValue)。这就是复合操作的非原子性导致的问题。

#### [那如何保证 `ConcurrentHashMap` 复合操作的原子性呢？](#那如何保证-concurrenthashmap-复合操作的原子性呢)

`ConcurrentHashMap` 提供了一些原子性的复合操作，如 `putIfAbsent`、`compute`、`computeIfAbsent` 、`computeIfPresent`、`merge`等。这些方法都可以接受一个函数作为参数，根据给定的 key 和 value 来计算一个新的 value，并且将其更新到 map 中。

上面的代码可以改写为：

或者：

很多同学可能会说了，这种情况也能加锁同步呀！确实可以，但不建议使用加锁的同步机制，违背了使用 `ConcurrentHashMap` 的初衷。在使用 `ConcurrentHashMap` 的时候，尽量使用这些原子性的复合操作方法来保证原子性。

#### [SynchronizedMap和ConcurrentHashMap有什么区别？](#synchronizedmap和concurrenthashmap有什么区别)

SynchronizedMap一次锁住整张表来保证线程安全，所以每次只能有一个线程来访问map。

JDK1.8 ConcurrentHashMap采用CAS和synchronized来保证并发安全。数据结构采用数组+链表/红黑二叉树。synchronized只锁定当前链表或红黑二叉树的首节点，支持并发访问、修改。
 另外ConcurrentHashMap使用了一种不同的迭代方式。当iterator被创建后集合再发生改变就不再是抛出ConcurrentModificationException，取而代之的是在改变时new新的数据从而不影响原有的数据，iterator完成后再将头指针替换为新的数据，这样iterator线程可以使用原来老的数据，而写线程也可以并发的完成改变。

### [ConcurrentLinkedQueue](#concurrentlinkedqueue)

非阻塞队列。高效的并发队列，使用链表实现。可以看做一个线程安全的 `LinkedList`，通过 CAS 操作实现。

如果对队列加锁的成本较高则适合使用无锁的 `ConcurrentLinkedQueue` 来替代。适合在对性能要求相对较高，同时有多个线程对队列进行读写的场景。

**非阻塞队列中的几种主要方法：**

- `add(E e)`：将元素e插入到队列末尾，如果插入成功，则返回true；如果插入失败（即队列已满），则会抛出异常； 内部调用的就是offer()方法。

- `remove()`：移除队首元素，若移除成功，则返回true；如果移除失败（队列为空），则会抛出异常；

- `offer(E e)`：将元素e插入到队列末尾，如果插入成功，则返回true；如果插入失败（即队列已满），则返回false；

- `poll()`：移除并获取队首元素，若成功，则返回队首元素；否则返回null；

- `peek()`：获取队首元素，若成功，则返回队首元素；否则返回null

对于非阻塞队列，一般情况下建议使用offer、poll和peek三个方法，不建议使用add和remove方法。核心原因在于**它们处理“失败”的方式更加友好，避免了异常机制带来的开销和代码复杂度**。
核心方法操作成功时的行为操作失败时（如空队列取元素/满队列加元素）的行为`offer(E e)`, `poll()`, `peek()`返回 `true`或具体对象**返回特殊值**（`false`或 `null`）`add(E e)`, `remove()`, `element()`返回 `true`或具体对象**抛出运行时异常**（如 队列满add时抛出`IllegalStateException`, 空队列remove时抛出`NoSuchElementException`）
### [BlockingQueue](#blockingqueue)

### [什么是阻塞队列以及应用场景](#什么是阻塞队列以及应用场景)

阻塞队列是`java.util.concurrent`包下重要的数据结构，`BlockingQueue`提供了线程安全的队列访问方式：当阻塞队列进行插入数据时，如果队列已满，线程将会阻塞等待直到队列非满；从阻塞队列取数据时，如果队列已空，线程将会阻塞等待直到队列非空。并发包下很多高级同步类的实现都是基于`BlockingQueue`实现的。`BlockingQueue` 适合用于作为数据共享的通道。

使用阻塞算法的队列可以用一个锁（入队和出队用同一把锁）或两个锁（入队和出队用不同的锁）等方式来实现。

阻塞队列和一般的队列的区别就在于：

1. 多线程支持，多个线程可以安全的访问队列

1. 阻塞操作，当队列为空的时候，消费线程会阻塞等待队列不为空；当队列满了的时候，生产线程就会阻塞直到队列不满

**方法**
方法\处理方式抛出异常返回特殊值一直阻塞超时退出插入方法add(e)offer(e)put(e)offer(e,time,unit)移除方法remove()poll()take()poll(time,unit)检查方法element()peek()不可用不可用
应用场景：

- 生产者-消费者模型：在生产者-消费者模型中，生产者线程生成数据并放入队列，消费者线程从队列中取出数据进行处理。阻塞队列的自动阻塞机制使得它能够简单高效地实现生产者-消费者模型。

- 线程池工作队列：在Java的线程池实现中，阻塞队列常用来保存任务。例如，ThreadPoolExecutor使用阻塞队列来管理提交但未被执行的任务。

- 实时数据处理系统：在需要处理实时流数据的系统中，阻塞队列可以用于在数据生成模块和数据处理模块之间传递数据，确保数据以正确的顺序被处理，并且不会因过快的生产速度导致数据丢失。

#### [JDK提供的阻塞队列](#jdk提供的阻塞队列)

JDK 7 提供了7个阻塞队列，如下

1、**ArrayBlockingQueue**

有界阻塞队列，底层采用数组实现。`ArrayBlockingQueue` 一旦创建，容量不能改变。其并发控制采用可重入锁来控制，不管是插入操作还是读取操作，都需要获取到锁才能进行操作。此队列按照先进先出（FIFO）的原则对元素进行排序。默认情况下不能保证线程访问队列的公平性，参数`fair`可用于设置线程是否公平访问队列。为了保证公平性，通常会降低吞吐量。

2、**LinkedBlockingQueue**

`LinkedBlockingQueue`是一个用单向链表实现的有界阻塞队列，可以当做无界队列也可以当做有界队列来使用。通常在创建 `LinkedBlockingQueue` 对象时，会指定队列最大的容量。此队列的默认和最大长度为`Integer.MAX_VALUE`。此队列按照先进先出的原则对元素进行排序。与 `ArrayBlockingQueue` 相比起来具有更高的吞吐量。

3、**PriorityBlockingQueue**

支持优先级的**无界**阻塞队列。默认情况下元素采取自然顺序升序排列。也可以自定义类实现`compareTo()`方法来指定元素排序规则，或者初始化`PriorityBlockingQueue`时，指定构造参数`Comparator`来进行排序。

`PriorityBlockingQueue` 只能指定初始的队列大小，后面插入元素的时候，如果空间不够的话会**自动扩容**。

`PriorityQueue` 的线程安全版本。不可以插入 null 值，同时，插入队列的对象必须是可比较大小的（comparable），否则报 ClassCastException 异常。它的插入操作 put 方法不会 block，因为它是无界队列（take 方法在队列为空的时候会阻塞）。

4、**DelayQueue**

支持延时获取元素的无界阻塞队列。队列使用`PriorityBlockingQueue`来实现。队列中的元素必须实现Delayed接口，在创建元素时可以指定多久才能从队列中获取当前元素。只有在延迟期满时才能从队列中提取元素。

5、**SynchronousQueue**

不存储元素的阻塞队列，每一个put必须等待一个take操作，否则不能继续添加元素。支持公平访问队列。

`SynchronousQueue`可以看成是一个传球手，负责把生产者线程处理的数据直接传递给消费者线程。队列本身不存储任何元素，非常适合传递性场景。`SynchronousQueue`的吞吐量高于`LinkedBlockingQueue`和`ArrayBlockingQueue`。

6、**LinkedTransferQueue**

由链表结构组成的无界阻塞TransferQueue队列。相对于其他阻塞队列，多了`tryTransfer`和`transfer`方法。

transfer方法：如果当前有消费者正在等待接收元素（take或者待时间限制的poll方法），transfer可以把生产者传入的元素立刻传给消费者。如果没有消费者等待接收元素，则将元素放在队列的tail节点，并等到该元素被消费者消费了才返回。

tryTransfer方法：用来试探生产者传入的元素能否直接传给消费者。如果没有消费者在等待，则返回false。和上述方法的区别是该方法无论消费者是否接收，方法立即返回。而transfer方法是必须等到消费者消费了才返回。

#### [原理](#原理)

JDK使用通知模式实现阻塞队列。所谓通知模式，就是当生产者往满的队列里添加元素时会阻塞生产者，当消费者消费了一个队列中的元素后，会通知生产者当前队列可用。

ArrayBlockingQueue使用Condition来实现：

#### [ArrayBlockingQueue 和 LinkedBlockingQueue 有什么区别？](#arrayblockingqueue-和-linkedblockingqueue-有什么区别)

`ArrayBlockingQueue` 和 `LinkedBlockingQueue` 是 Java 并发包中常用的两种阻塞队列实现，它们都是线程安全的。不过，不过它们之间也存在下面这些区别：
特性维度ArrayBlockingQueueLinkedBlockingQueue**底层数据结构**​基于**数组**实现基于**单向链表**实现**队列边界**​**有界队列**，创建时必须指定固定容量**默认无界**（容量为`Integer.MAX_VALUE`），也可创建为有界队列**锁机制**​使用**单一锁**（生产者和消费者共用同一把锁）采用**锁分离**技术（生产用`putLock`，消费用`takeLock`）**内存占用与GC**​内存预分配，插入/删除不产生额外对象，GC压力小动态创建Node节点，长时间运行下对GC影响较大**并发吞吐量**​一般。由于使用一把锁，生产与消费无法完全并行**较高**。生产与消费操作通常可并行**性能稳定性**​较高。基于数组，性能表现稳定相对较低。在大多数并发应用中性能可预测性较差
**选择 `ArrayBlockingQueue`时**：

- 适用于**队列大小固定**、**性能要求稳定**、且**生产者和消费者速率相对均衡**的场景 。

- 例如，线程池（如`ThreadPoolExecutor`）的任务队列常使用它，以防止资源过度消耗。

**选择 `LinkedBlockingQueue`时**：

- 适用于**任务量不确定**、**生产者与消费者速率差异较大**，且需要**高吞吐量**的场景 。

- 例如，作为消息中间件的临时传输队列。但需警惕其无界特性可能导致的内存溢出风险，**强烈建议创建时指定合适的容量**​

但从本人实践的情况来看，大部分时候还是用的`LinkedBlockingQueue`
