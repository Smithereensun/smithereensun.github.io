{

  "title": "HashSet & HashMap：Java开发者的高效数据结构选择",
  "has_date": true,
  "description": "HashSet**和**HashMap**者在Java里有着相同的实现，前者仅仅是对后者做了一层包装，也就是说**HashSet**里面有一个**HashMap**(适配器模式)。因此了解**HashMap源码也就了解HashSet了** 介绍 Key的存储方式是基于哈希表的 HashMap是 Ma",
  "tags": [
    "Java",
    "集合"
  ],
  "source": "local-markdown-library",
  "source_path": "java/collection/03-map1-hashset-hashmap - HashSet & HashMap：Java开发者的高效数据结构选择.md",
  "date": "2025-09-20"

}

**HashSet**和**HashMap**者在Java里有着相同的实现，前者仅仅是对后者做了一层包装，也就是说**HashSet**里面有一个**HashMap**(适配器模式)。因此了解**HashMap源码也就了解HashSet了**

## [介绍](#介绍)

- Key的存储方式是基于哈希表的

- HashMap是 Map 接口 使用频率最高的实现类。

- 允许使用null键和null值，与HashSet一样，不保证映射的顺序。

- 所有的key构成的集合是无序的、唯一不可重复的。所以，key所在的类要重写：equals()和hashCode()

- 所有的value构成的集合是Collection:无序的、可以重复的。所以，value所在的类要重写：equals()

- 一个key-value构成一个entry

- 所有的entry构成的集合是Set:无序的、不可重复的

- HashMap 判断两个 key 相等的标准是：两个 key 通过 equals() 方法返回 true，hashCode 值也相等。

- HashMap 判断两个 value 相等的标准是：两个 value 通过 equals() 方法返回 true

## [底层原理介绍](#底层原理介绍)

### [底层数据结构和初始属性](#底层数据结构和初始属性)

为什么默认负载因子是 0.75？官方答案如下：

As a general rule, the default load factor (.75) offers a good tradeoff between time and space costs. Higher values decrease the space overhead but increase the lookup cost (reflected in most of the operations of the HashMap class, including get and put). The expected number of entries in the map and its load factor should be taken into account when setting its initial capacity, so as to minimize the number of rehash operations. If the initial capacity is greater than the maximum number of entries divided by the load factor, no rehash operations will ever occur.

上面的意思，简单来说是默认负载因子为 0.75，是因为它提供了空间和时间复杂度之间的良好平衡。 负载因子太低会导致大量的空桶浪费空间，负载因子太高会导致大量的碰撞，降低性能。0.75 的负载因子在这两个因素之间取得了良好的平衡。也就是说官方并未对负载因子为 0.75 做过的的解释，只是大概的说了一下，0.75 是空间和时间复杂度的平衡，但更多的细节是未做说明的，Stack Overflow 进行了[负载因子的科学推测](https://stackoverflow.com/questions/10901752/what-is-the-significance-of-load-factor-in-hashmap)，感兴趣的可以学习学习

### [构造方法](#构造方法)

### [put方法](#put方法)

先计算key的hash值，再对其put

这里分为了三步：

1. h=key.hashCode() //第一步 取hashCode值

1. h^(h&gt;&gt;&gt;16) //第二步 高位参与运算，减少冲突，hash计算到这里

1. return h&(length-1); //第三步 取模运算，计算数据在桶中的位置，这里看后面的源码

第3步(n-1)&hash原理：

- 实际上(n-1) & hash等于 hash%n都可以得到元素在桶中的位置，但是(n-1)&hash操作更快。

- 取余操作如果除数是 2 的整数次幂可以优化为移位操作。这也是为什么扩容时必须是必须是2的n次方

位运算(&)效率要比代替取模运算(%)高很多，主要原因是位运算（如与、或、移位等）是 CPU 的基本指令，几乎所有现代 CPU 都能在**单个时钟周期**内完成这些操作。而取模运算通常需要先执行除法，再计算余数，除法操作在 CPU 上比位运算复杂得多，需要**多个时钟周期**才能完成。

而计算hash是通过同时使用hashCode()的高16位异和低16位实现的(h &gt;&gt;&gt; 16)：这么做可以在数组比较小的时候，也能保证考虑到高低位都参与到Hash的计算中，可以减少冲突，同时不会有太大的开销。

hash值其实是一个int类型，二进制位为32位，而HashMap的table数组初始化size为16，取余操作为hashCode & 15 ==&gt; hashCode & 1111 。这将会存在一个巨大的问题，1111只会与hashCode的低四位进行与操作，也就是hashCode的高位其实并没有参与运算，会导很多hash值不同而高位有区别的数，最后算出来的索引都是一样的。 举个例子，假设hashCode为1111110001，那么1111110001 & 1111 = 0001，如果有些key的hash值低位与前者相同，但高位发生了变化，如1011110001 & 1111 = 0001，1001110001 & 1111 = 0001，显然在高位发生变化后，最后算出来的索引还是一样，这样就会导致很多数据都被放到一个数组里面了，造成性能退化。 为了避免这种情况，HashMap将高16位与低16位进行异或，这样可以保证高位的数据也参与到与运算中来，以增大索引的散列程度，让数据分布得更为均匀（个人认为是为了分布均匀）

put流程如下：
![](/imported/markdown/2025-09-20-markdown-cca3dbbb-hashset-hashmap-java开发者的高效数据结构选择/images/84bed0ae636f-202404250901133.jpg)
总结put方法流程：

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

### [数组扩容](#数组扩容)

显然，HashMap的扩容机制，就是当达到扩容条件时会进行扩容。扩容条件就是当HashMap中的元素个数超过临界值时就会自动扩容（threshold = loadFactor * capacity）。如果是初始化扩容，只执行resize的前半部分代码，但如果是随着元素的增加而扩容，HashMap需要重新计算oldTab中每个值的位置，即重建hash表，随着元素的不断增加，HashMap会发生多次扩容，这样就会非常影响性能。所以一般建议创建HashMap的时候指定初始化容量

但是当使用HashMap(int initialCapacity)来初始化容量的时候，HashMap并不会使用传进来的initialCapacity直接作为初始容量。JDK会默认计算一个相对合理的值当做初始容量。所谓合理值，其实是找到第一个比用户传入的值大的**2的幂**。也就是说，当new HashMap(7)创建HashMap的时候，JDK会通过计算，创建一个容量为8的Map；当new HashMap(9)创建HashMap的时候，JDK会通过计算，创建一个容量为16的Map。当然了，当创建一个`HashMap`时，表的大小并不会立即分配，而是在第一次put元素时进行分配，并且分配的大小会是大于或等于初始容量的最小的2的幂。

一般来说，initialCapacity = (需要存储的元素个数 / 负载因子) + 1。注意负载因子（即 loaderfactor）默认为 0.75，如果暂时无法确定初始值大小，请设置为 16（即默认值）。HashMap 需要放置 1024 个元素，由于没有设置容量初始大小，随着元素增加而被迫不断扩容，resize() 方法总共会调用 8 次，反复重建哈希表和数据迁移。当放置的集合元素个数达千万级时会影响程序性能。

总结HashMap的实现：

1. HashMap的内部存储结构其实是 数组+ 链表+ 红黑树 的结合。当实例化一个HashMap时，会初始化initialCapacity和loadFactor，此时还不会创建数组

1. 在put第一对映射关系时，系统会创建一个长度为initialCapacity（默认为16）的Node数组，这个长度在哈希表中被称为容量(Capacity)，在这个数组中可以存放元素的位置我们称之为“桶”(bucket)，每个bucket都有自己的索引，系统可以根据索引快速的查找bucket中的元素。

1. 每个bucket中存储一个元素，即一个Node对象，但每一个Node对象可以带一个引用变量next，用于指向下一个元素，因此，在一个桶中，就有可能生成一个Node链。也可能是一个一个TreeNode对象，每一个TreeNode对象可以有两个叶子结点left和right，因此，在一个桶中，就有可能生成一个TreeNode树。而新添加的元素作为链表的last，或树的叶子结点

总结HashMap的扩容和树形化：

1. 当HashMap中的元素个数超过数组大小(数组总大小length,不是数组中个数size)*loadFactor 时，就会进行数 组扩容，loadFactor的默认值(DEFAULT_LOAD_FACTOR)为0.75，这是一个折中的取值。也就是说，默认情况下，数组大小(DEFAULT_INITIAL_CAPACITY)为16，那么当HashMap中元素个数超过16*0.75=12（这个值就是代码中的threshold值，也叫做临界值）的时候，就把数组的大小扩展为 2*16=32，即扩大一倍，然后重新计算每个元素在数组中的位置，而这是一个非常消耗性能的操作，所以如果我们已经预知HashMap中元素的个数，那么预设元素的个数能够有效的提高HashMap的性能

1. 当HashMap中的其中一个链的对象个数如果达到了8个，此时如果capacity没有达到64，那么HashMap会先扩容解决，如果已经达到了64，那么这个链会变成树，结点类型由Node变成TreeNode类型。当然，如果当映射关系被移除后，下次resize方法时判断树的结点个数低于6个，也会把树再转为链表。

即当数组的某一个索引位置上的元素以链表形式存在的数据个数&gt;8且当前数组的长度&gt;64时，此时此索引位置上的所有数据改为使用红黑树存储

### [get方法](#get方法)

总结get方法：

1. 首先通过hash()函数得到对应数组下标，然后依次判断。

1. 判断第一个元素与key是否匹配，如果匹配就返回参数值；

1. 判断链表是否红黑树，如果是红黑树，就进入红黑树方法获取参数值；

1. 如果不是红黑树结构，直接循环遍历链表判断，直到获取参数为止；

### [remove方法](#remove方法)

jdk1.8的删除逻辑实现比较复杂，删除时有红黑树节点删除和调整：

1. 默认判断链表第一个元素是否是要删除的元素；

1. 如果第一个不是，就继续判断当前冲突链表是否是红黑树，如果是，就进入红黑树里面去找；

1. 如果当前冲突链表不是红黑树，就直接在链表中循环判断，直到找到为止；

1. 将找到的节点，删除掉，如果是红黑树结构，会进行颜色转换、左旋、右旋调整，直到满足红黑树特性为止；

## [HashMap的遍历](#hashmap的遍历)

HashMap **遍历从大的方向来说，可分为以下 4 类**：

1. 迭代器（Iterator）方式遍历；

1. For Each 方式遍历；

1. Lambda 表达式遍历（JDK 1.8+）;

1. Streams API 遍历（JDK 1.8+）。

但每种类型下又有不同的实现方式，因此具体的遍历方式又可以分为以下 7 种：

1. 使用迭代器（Iterator）EntrySet 的方式进行遍历；

1. 使用迭代器（Iterator）KeySet 的方式进行遍历；

1. 使用 For Each EntrySet 的方式进行遍历；

1. 使用 For Each KeySet 的方式进行遍历；

1. 使用 Lambda 表达式的方式进行遍历；

1. 使用 Streams API 单线程的方式进行遍历；

1. 使用 Streams API 多线程的方式进行遍历。

接下来我们来看每种遍历方式的具体实现代码。

### [遍历方式的具体实现](#遍历方式的具体实现)

#### [迭代器 EntrySet](#迭代器-entryset)

#### [迭代器 KeySet](#迭代器-keyset)

#### [ForEach EntrySet](#foreach-entryset)

#### [ForEach KeySet](#foreach-keyset)

#### [Lambda](#lambda)

#### [Streams API 单线程](#streams-api-单线程)

#### [Streams API 多线程](#streams-api-多线程)

### [性能测试](#性能测试)

接下来我们使用 Oracle 官方提供的性能测试工具 JMH（Java Microbenchmark Harness，JAVA 微基准测试套件）来测试一下这 7 种循环的性能。

首先，我们先要引入 JMH 框架，在 `pom.xml` 文件中添加如下配置：

然后编写测试代码，如下所示：

所有被添加了 `@Benchmark` 注解的方法都会被测试，因为 parallelStream 为多线程版本性能一定是最好的，所以就不参与测试了，其他 6 个方法的测试结果如下：
![](/imported/markdown/2025-09-20-markdown-cca3dbbb-hashset-hashmap-java开发者的高效数据结构选择/images/2fb6c43abaa7-202409211728570.webp)
其中 Units 为 ns/op 意思是执行完成时间（单位为纳秒），而 Score 列为平均执行时间， `±` 符号表示误差。从以上结果可以看出，两个 `entrySet` 的性能相近，并且执行速度最快，接下来是 `stream`，然后是两个 `keySet`，性能最差的是 `KeySet` 。

**从以上结果可以看出 `entrySet` 的性能比 `keySet` 的性能高出了一倍之多，因此我们应该尽量使用 `entrySet` 来实现 Map 集合的遍历**。

#### [字节码分析](#字节码分析)

要理解以上的测试结果，我们需要把所有遍历代码通过 `javac` 编译成字节码来看具体的原因。

编译后，我们使用 Idea 打开字节码，内容如下：

从结果可以看出，除了 Lambda 和 Streams API 之外，通过迭代器循环和 `for` 循环的遍历的 `EntrySet` 最终生成的代码是一样的，他们都是在循环中创建了一个遍历对象 `Entry`，代码如下：

而 `KeySet` 的代码也是类似的，如下所示：

所以我们在使用迭代器或是 `for` 循环 `EntrySet` 时，他们的性能都是相同的，因为他们最终生成的字节码基本都是一样的；同理 `KeySet` 的两种遍历方式也是类似的。

#### [性能分析](#性能分析)

`EntrySet` 之所以比 `KeySet` 的性能高是因为，`KeySet` 在循环时使用了 `map.get(key)`，而 `map.get(key)` 相当于又遍历了一遍 Map 集合去查询 `key` 所对应的值。为什么要用“又”这个词？那是因为**在使用迭代器或者 for 循环时，其实已经遍历了一遍 Map 集合了，因此再使用 `map.get(key)` 查询时，相当于遍历了两遍**（尽管不是遍历整个map，那也多了一次hash计算，以及遍历了对应bucket中的元素）。

而 `EntrySet` 只遍历了一遍 Map 集合，之后通过代码“Entry&lt;Integer, String&gt; entry = iterator.next()”把对象的 `key` 和 `value` 值都放入到了 `Entry` 对象中，因此再获取 `key` 和 `value` 值时就无需再遍历 Map 集合，只需要从 `Entry` 对象中取值就可以了。

所以，**`EntrySet` 的性能比 `KeySet` 的性能高出了一倍，因为 `KeySet` 相当于循环了两遍 Map 集合，而 `EntrySet` 只循环了一遍**。

## [HashSet](#hashset)

- Set 不能存放重复元素，无序的，允许一个null(基于HashMap 实现，HashMap的key可以为null)；

- Set 基于 Map 实现，Set 里的元素值就是 Map的键值。

HashSet 基于 HashMap 实现。放入HashSet中的元素实际上由HashMap的key来保存，而HashMap的value则存储了一个静态的Object对象。

底层源码
