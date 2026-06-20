{

  "title": "LinkedHashSet & LinkedHashMap：链表与哈希表的协同工作原理",
  "has_date": true,
  "description": "写在前面 从一道Leetcode题目说起 首先，来看一下Leetcode里面的一道经典题目：146.LRU缓存机制，题目描述如下： 请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。 实现 类： 以 **正整数** 作为容量 初始化 LRU 缓存 如果关键字 存在于缓存中，则返",
  "tags": [
    "Java",
    "集合"
  ],
  "source": "local-markdown-library",
  "source_path": "java/collection/03-map3-linkedhashset-map - LinkedHashSet & LinkedHashMap：链表与哈希表的协同工作原理.md",
  "date": "2025-05-17"

}

## [写在前面](#写在前面)

从一道Leetcode题目说起

首先，来看一下Leetcode里面的一道经典题目：[146.LRU缓存机制](https://leetcode.cn/problems/lru-cache/description/)，题目描述如下：

请你设计并实现一个满足 [LRU (最近最少使用) 缓存](https://baike.baidu.com/item/LRU) 约束的数据结构。

实现 `LRUCache` 类：

- `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存

- `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。

- `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity`，则应该 **逐出** 最久未使用的关键字。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

LRU 的全称是 Least Recently Used，也就是说我们认为最近使用过的数据应该是是「有用的」，很久都没用过的数据应该是无用的，内存满了就优先删那些很久没用过的数据。

### [分析](#分析)

要让 LRU 的 `put` 和 `get` 方法的时间复杂度为 O(1)，可以总结出 LRU 这个数据结构必要的条件：

1. 显然 LRU 中的元素必须有时序，以区分最近使用的和久未使用的数据，当容量满了之后要删除最久未使用的那个元素腾位置。

1. 要在 LRU 中快速找某个 `key` 是否已存在并得到对应的 `val`；

1. 每次访问 LRU 中的某个 `key`，需要将这个元素变为最近使用的，也就是说 LRU 要支持在任意位置快速插入和删除元素。

那么，什么数据结构同时符合上述条件呢？哈希表查找快，但是数据无固定顺序；链表有顺序之分，插入删除快，但是查找慢。所以结合一下，形成一种新的数据结构：哈希链表 `LinkedHashMap`。

LRU 缓存算法的核心数据结构就是哈希链表，双向链表和哈希表的结合体。这个数据结构长这样：
![](/imported/markdown/2025-05-17-markdown-c860b1a6-linkedhashset-linkedhashmap-链表与哈希表的协同工作原理/images/8badeda7681a-202409122042336.png)
借助这个结构，逐一分析上面的 3 个条件：

1. 如果我们每次默认从链表尾部添加元素，那么显然越靠尾部的元素就是最近使用的，越靠头部的元素就是最久未使用的。

1. 对于某一个 `key`，我们可以通过哈希表快速定位到链表中的节点，从而取得对应 `val`。

1. 链表显然是支持在任意位置快速插入和删除的，改改指针就行。只不过传统的链表无法按照索引快速访问某一个位置的元素，而这里借助哈希表，可以通过 `key` 快速映射到任意一个链表节点，然后进行插入和删除。

put方法流程图：
![](/imported/markdown/2025-05-17-markdown-c860b1a6-linkedhashset-linkedhashmap-链表与哈希表的协同工作原理/images/eae8a2f9f260-202409122042820.png)
### [代码实现](#代码实现)

## [LinkedHashMap介绍](#linkedhashmap介绍)

**LinkedHashSet**和**LinkedHashMap**其实也是一回事。**LinkedHashSet**和**LinkedHashMap**在Java里也有着相同的实现，前者仅仅是对后者做了一层包装，也就是说**LinkedHashSet里面有一个LinkedHashMap(适配器模式)**。

**LinkedHashMap**实现了**Map**接口，即允许放入key为null的元素，也允许插入value为null的元素。从名字上可以看出该容器是**linked list**和**HashMap**的混合体，也就是说它同时满足**HashMap**和**linked list**的某些特性。**可将LinkedHashMap看作采用linked list增强的HashMap。**
![](/imported/markdown/2025-05-17-markdown-c860b1a6-linkedhashset-linkedhashmap-链表与哈希表的协同工作原理/images/f386393b86e6-202404250918723.jpg)
事实上**LinkedHashMap**是**HashMap**的直接子类，**二者唯一的区别是LinkedHashMap在HashMap的基础上，采用双向链表(doubly-linked list)的形式将所有entry连接起来，这样的好处：**

-
**可以保证元素的迭代顺序跟插入顺序相同**。跟**HashMap**相比，多了header指向双向链表的头部(是一个哑元)，**该双向链表的迭代顺序就是entry的插入顺序**。

-
**迭代LinkedHashMap时不需要像HashMap那样遍历整个table，而只需要直接遍历header指向的双向链表即可**，也就是说**LinkedHashMap**的迭代时间就只跟entry的个数相关，而跟table的大小无关。

有两个参数可以影响**LinkedHashMap**的性能: 初始容量(inital capacity)和负载系数(load factor)。初始容量指定了初始table的大小，负载系数用来指定自动扩容的临界值。当entry的数量超过capacity*load_factor时，容器将自动扩容并重新哈希。对于插入元素较多的场景，将初始容量设大可以减少重新哈希的次数。这点与HashMap是一样的

## [方法剖析](#方法剖析)

### [get()](#get)

get(Object key)方法根据指定的key值返回对应的value。该方法跟HashMap.get()方法的流程几乎完全一样

### [put()](#put)

put(K key, V value)方法是将指定的key, value对添加到map里。该方法首先会对map做一次查找，看是否包含该元组，如果已经包含则直接返回，查找过程类似于get()方法；如果没有找到，则会通过addEntry(int hash, K key, V value, int bucketIndex)方法插入新的entry。

注意，这里的**插入有两重含义**:

- 从table的角度看，新的entry需要插入到对应的bucket里，当有哈希冲突时，采用头插法将新的entry插入到冲突链表的头部。

- 从header的角度看，新的entry需要插入到双向链表的尾部。

![](/imported/markdown/2025-05-17-markdown-c860b1a6-linkedhashset-linkedhashmap-链表与哈希表的协同工作原理/images/3c9bfc52a989-202404250918720.jpg)
addEntry()代码如下:

上述代码中用到了addBefore()方法将新entry e插入到双向链表头引用header的前面，这样e就成为双向链表中的最后一个元素。addBefore()的代码如下:

### [remove()](#remove)

remove(Object key)的作用是删除key值对应的entry，该方法的具体逻辑是在removeEntryForKey(Object key)里实现的。removeEntryForKey()方法会首先找到key值对应的entry，然后删除该entry(修改链表的相应引用)。查找过程跟get()方法类似。

注意，这里的**删除也有两重含义**:

- 从table的角度看，需要将该entry从对应的bucket里删除，如果对应的冲突链表不空，需要修改冲突链表的相应引用。

- 从header的角度来看，需要将该entry从双向链表中删除，同时修改链表中前面以及后面元素的相应引用。

![](/imported/markdown/2025-05-17-markdown-c860b1a6-linkedhashset-linkedhashmap-链表与哈希表的协同工作原理/images/181fdabbfc5b-202404250918717.jpg)
removeEntryForKey()对应的代码如下:

## [LinkedHashSet](#linkedhashset)

LinkedHashSet是对LinkedHashMap的简单包装，对LinkedHashSet的函数调用都会转换成合适的LinkedHashMap方法，因此LinkedHashSet的实现非常简单
