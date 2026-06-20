{

  "title": "集合工具类 - Collections",
  "has_date": true,
  "description": "Collections 是 JDK 提供的一个工具类，位于 java.util 包下，提供了一系列的静态方法，方便我们对集合进行各种操作，算是集合框架的一个大管家。 大致看一下方法名和参数就能知道这个方法是干嘛的: 排序操作 ：反转顺序 ：洗牌，将顺序打乱 ：自然升序 ：按照自定义的比较器排序 ：将",
  "tags": [
    "工具库"
  ],
  "source": "local-markdown-library",
  "source_path": "tool-library/jdk-tools/collections - 集合工具类 - Collections.md",
  "date": "2025-05-17"

}

Collections 是 JDK 提供的一个工具类，位于 java.util 包下，提供了一系列的静态方法，方便我们对集合进行各种操作，算是集合框架的一个大管家。

大致看一下方法名和参数就能知道这个方法是干嘛的:
![](/imported/markdown/2025-05-17-markdown-bbe1a7a6-集合工具类-collections/images/3b91417bd73c-202407282314408.png)
## [排序操作](#排序操作)

- `reverse(List list)`：反转顺序

- `shuffle(List list)`：洗牌，将顺序打乱

- `sort(List list)`：自然升序

- `sort(List list, Comparator c)`：按照自定义的比较器排序

- `swap(List list, int i, int j)`：将 i 和 j 位置的元素交换位置

来看例子：

输出后：

## [查找操作](#查找操作)

- `binarySearch(List list, Object key)`：二分查找法，前提是 List 已经排序过了

- `max(Collection coll)`：返回最大元素

- `max(Collection coll, Comparator comp)`：根据自定义比较器，返回最大元素

- `min(Collection coll)`：返回最小元素

- `min(Collection coll, Comparator comp)`：根据自定义比较器，返回最小元素

- `frequency(Collection c, Object o)`：返回指定对象出现的次数

来看例子：

输出后：

## [填充集合](#填充集合)

- `fill(List list, Object obj)`：使用指定对象填充

- `addAll(Collection&lt;? super T&gt; c, T... elements)`，往集合中添加元素

## [同步控制(不常用)](#同步控制-不常用)

ArrayList 是线程不安全的，没法在多线程环境下使用，那 Collections 工具类中提供了多个 synchronizedXxx 方法，这些方法会返回一个同步的对象，从而解决多线程中访问集合时的安全问题。
![](/imported/markdown/2025-05-17-markdown-bbe1a7a6-集合工具类-collections/images/84077c8158d5-collections-02.png)
使用起来也非常的简单：

看一眼 SynchronizedList 的源码就明白了，不过是在方法里面使用了 synchronized 关键字，加了一层锁而已。

那这样的话，其实效率和那些直接在方法上加 synchronized 关键字的 Vector、Hashtable 差不多（JDK 1.0 时期就有了），而这些集合类基本上已经废弃了，几乎不怎么用。正确的做法是使用并发包下的 CopyOnWriteArrayList、ConcurrentHashMap。

## [不可变集合(不常用)](#不可变集合-不常用)

- `emptyXxx()`：制造一个空的不可变集合

- `singletonXxx()`：制造一个只有一个元素的不可变集合

- `unmodifiableXxx()`：为指定集合制作一个不可变集合

举个例子：

这段代码在执行的时候就抛出错误了。

这是因为 `Collections.emptyList()` 会返回一个 Collections 的内部类 EmptyList，而 EmptyList 并没有重写父类 AbstractList 的 `add(int index, E element)` 方法，所以执行的时候就抛出了不支持该操作的 UnsupportedOperationException 了。

这是从分析 add 方法源码得出的原因。除此之外，emptyList 方法是 final 的，返回的 EMPTY_LIST 也是 final 的，种种迹象表明 emptyList 返回的就是不可变对象，没法进行增删改查。

Collections的不可变集合并不是真的不可变的，建议使用Guava的不可变集合Immutable
