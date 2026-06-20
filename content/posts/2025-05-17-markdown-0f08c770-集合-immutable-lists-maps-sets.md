{

  "title": "集合 - Immutable&Lists&Maps&Sets",
  "has_date": true,
  "description": "Immutable 如《Effective Java》Item1)所述，在设计类的时候，倾向优先使用静态工厂方法(static factory method)而非构造函数(constructor)创建对象，优点在于: 静态工厂方法多了一层名称信息，比构造函数更富表达性。 可以更灵活地创建对象，比如缓",
  "tags": [
    "工具库"
  ],
  "source": "local-markdown-library",
  "source_path": "tool-library/guava/guava-collections - 集合 - Immutable&Lists&Maps&Sets.md",
  "date": "2025-05-17"

}

## [Immutable](#immutable)

如《Effective Java》Item1)所述，在设计类的时候，倾向优先使用静态工厂方法(static factory method)而非构造函数(constructor)创建对象，优点在于:

1. 静态工厂方法多了一层名称信息，比构造函数更富表达性。

1. 可以更灵活地创建对象，比如缓式初始化，缓存已创建对象。

1. 静态方法内部返回的对象类型，可以是其声明类型的子类。

同样，如《Effective Java》Item17所述，需要最小化可变性，`ImmutableList`遵循了最佳实践。首先，`ImmutableList`不可以通过构造函数实例化，更准确地说，不可以在`package`外部通过构造函数实例化。

而在程序设计中使用不可变对象，也可以提高代码的可靠性和可维护性，其优势包括：

1. **线程安全性（Thread Safety）**：不可变对象是线程安全的，无需同步操作，避免了竞态条件

1. **安全性**：可以防止在程序运行时被意外修改，提高了程序的安全性

1. **易于理解和测试**：不可变对象在创建后不会发生变化，更容易理解和测试

1. **克隆和拷贝**：不可变对象不需要实现可变对象的复制（Clone）和拷贝（Copy）逻辑，因为它们的状态不可变，克隆即是自己

创建对象的不可变拷贝是一项很好的防御性编程技巧。Guava为所有JDK标准集合类型和Guava新集合类型都提供了简单易用的不可变版本。JDK也提供了Collections.unmodifiableXXX方法把集合包装为不可变形式.

### [JDK不可变集合存在的问题](#jdk不可变集合存在的问题)

JDK 的 Collections 提供了 Unmodified Collections 不可变集合，但仅仅是通过装饰器模式提供了一个只读的视图，unmodifiableList本身是无法进行add等修改操作，但并没有阻止对原始集合的修改操作，所以说Collections.unmodifiableList实现的不是真正的不可变集合。

- 笨重而且累赘：不能舒适地用在所有想做防御性拷贝的场景；

- 不安全：要保证没人通过原集合的引用进行修改，返回的集合才是事实上不可变的；

- 低效：包装过的集合仍然保有可变集合的开销，比如并发修改的检查、散列表的额外空间，等等。

### [Guava不可变集合案例](#guava不可变集合案例)

而 Guava 提供的不可变集合不是原容器的视图，而是原容器的一份拷贝，因此更加简单高效，确保了真正的不可变性。

但是还要注意，由于immutable只是copy了元容器本身，并不是deep copy，因此对原容器的引用的内容进行修改，也会影响immutableXXX

**注意**：每个Guava immutable集合类的实现都拒绝null值。如果确实需要能接受null值的集合类，可以考虑用Collections.unmodifiableXXX。

immutable集合可以有以下几种方式来创建：

1. 用copyOf方法，比如，ImmutableSet.copyOf(set)

1. 使用of方法，比如，ImmutableSet.of("a", "b", "c") 或者 ImmutableMap.of("a", 1, "b", 2)

1. 使用Builder类：减少中间对象的创建，提高内存使用效率。

### [更智能的copyOf](#更智能的copyof)

ImmutableXXX.copyOf会在合适的情况下避免拷贝元素的操作。

在这段代码中，ImmutableList.copyOf(imSet)会智能地直接返回 imSet.asList()，它是一个ImmutableSet的常量时间复杂度的List视图。

实际上，要实现`copyOf`方法，最简单的就是直接将底层的每个元素做深拷贝然后生成`ImmutableList`。但是对于所有情况都深拷贝的话，性能和存储开销必然比较大，那么源码里面是如何优化的呢？

所有不可变集合都有一个asList() 方法提供ImmutableList视图，让我们可以用列表形式方便地读取集合元素。例如，我们可以使用sortedSet.asList().get(k) 从 ImmutableSortedSet 中读取第k个最小元素。
 asList()返回的ImmutableList 通常是（但并不总是）开销稳定的视图实现，而不是简单地把元素拷贝进List，也就是说，asList返回的列表视图通常比一般的列表平均性能更好，比如，在底层集合支持的情况下，它总是使用高效的contains方法。

源码如下：

实际上，ImmutableXXX.copyOf(ImmutableCollection)会试图对如下情况避免线性时间拷贝：

- **在常量时间内使用底层数据结构是可能的**：因为会获取视图后返回

- **不会造成内存泄露**：例如，有个很大的不可变集合`ImmutableList&lt;String&gt; hugeList`， `ImmutableList.copyOf(hugeList.subList(0, 10))`就会显式地拷贝（如上源码，会判断是否是局部视图），以免不必要地持有hugeList的引用。

- **不改变语义**：所以ImmutableSet.copyOf(myImmutableSortedSet)都会显式地拷贝，因为和基于比较器的ImmutableSortedSet相比，ImmutableSet对hashCode()和equals有不同语义。

在可能的情况下避免线性拷贝，可以最大限度地减少防御性编程风格所带来的性能开销。

### [Guava集合和不可变对应关系](#guava集合和不可变对应关系)
**可变集合类型****可变集合源：JDK or Guava?****Guava不可变集合**CollectionJDKImmutableCollectionListJDKImmutableListSetJDKImmutableSetSortedSet/NavigableSetJDKImmutableSortedSetMapJDKImmutableMapSortedMapJDKImmutableSortedMapMultisetGuavaImmutableMultisetSortedMultisetGuavaImmutableSortedMultisetMultimapGuavaImmutableMultimapListMultimapGuavaImmutableListMultimapSetMultimapGuavaImmutableSetMultimapBiMapGuavaImmutableBiMapClassToInstanceMapGuavaImmutableClassToInstanceMapTableGuavaImmutableTable
## [Lists](#lists)

私有的构造方法，可以看到这是一个真正的功能函数，下面对其函数进行分析

### [功能函数](#功能函数)

首先根据每一个函数的更能进行了分类：
功能方法创建ArrayList方法1、newArrayList()
2、newArrayList(E... elements)
3、newArrayList(Iterable&lt;? extends E&gt; elements)
4、newArrayList(Iterator&lt;? extends E&gt; elements)
5、newArrayListWithCapacity(int initialArraySize)
6、newArrayListWithExpectedSize(int estimatedSize)创建LinkedList方法1、newLinkedList()
2、newLinkedList(Iterable&lt;? extends E&gt; elements)创建CopyOnWriteArrayList方法1、newCopyOnWriteArrayList()
2、newCopyOnWriteArrayList(Iterable&lt;? extends E&gt; elements)创建自制List规则1、asList(@Nullable E first, E[] rest)
2、asList(@Nullable E first, @Nullable E second, E[] rest)List笛卡尔乘积1、cartesianProduct(List&lt;? extends List&lt;? extends B&gt;&gt; lists)
2、cartesianProduct(List&lt;? extends B&gt;... lists)List变形transform(List&lt;F&gt; fromList, Function&lt;? super F, ? extends T&gt; function)分割list（作用之一：分页）partition(List&lt;T&gt; list, int size)将字符串作为字符数组进行操作1、charactersOf(String string)
2、charactersOf(CharSequence sequence)将list逆序reverse(List&lt;T&gt; list)
### [创建ArrayList方法](#创建arraylist方法)

1.
没有参数的创建ArrayList

1.
传入一个数组，返回一个ArrayList

1.
传入一个集合顶级接口，然后返回一个ArrayList

1.
传入一个迭代器，返回一个ArrayList

1.
传入想要的list长度，返回一个与传入值等长的ArrayList

1.
传入一个想要的list长度，返回一个程序调优后的长度的ArrayList

### [创建LinkedList方法](#创建linkedlist方法)

1.
不传入参数，直接返回一个LinkedList

1.
传入一个容器，返回一个LinkedList

### [创建CopyOnWriteArrayList方法](#创建copyonwritearraylist方法)

1.
不传入参数，直接返回一个新的CopyOnWriteArrayList

1.
传入一个容器，返回一个CopyOnWriteArrayList，带有传入容器的值

### [创建自制List规则](#创建自制list规则)

使用案例：

这样做的一个好处是可以提高代码的可读性，因为它明确地区分了 "leader" 和 "members"，而不是将它们混在一起。而且，如果 "members" 是动态确定的（例如，它们来自另一个方法或计算结果），那么这个 `asList` 方法将比手动创建 `List` 并添加元素更为方便。

**注意**：asList返回的是视图，也就是说，原容器的变更会影响这些方法返回的容器内容

1.
根据参数生成一个多一个参数的List

1.
根据参数生成一个多两个个参数的List

### [List笛卡尔乘积](#list笛卡尔乘积)

### [List变形](#list变形)

使用案例：

源码：

### [分割list（作用之一：分页）](#分割list-作用之一-分页)

这里的RandomAccessPartition是Partition的子类，且RandomAccessPartition对其的处理是直接调用了父类的方法，所以我们只需要解析Partition类就可以了

### [将字符串作为字符数组进行操作](#将字符串作为字符数组进行操作)

主要用于将一个字符串转换为一个不可变的 `List&lt;Character&gt;`，使得字符串的字符可以像列表元素一样进行操作。

### [list逆序](#list逆序)

实际上调用了ImmutableList类的reverse方法进行处理的逆序

## [Maps](#maps)

私有的构造方法，可以看到这是一个真正的功能函数，下面对其函数进行分析

### [功能函数](#功能函数-1)
功能方法创建EnumMap1、EnumMap&lt;K, V&gt; newEnumMap(Class&lt;K&gt; type)
2、EnumMap&lt;K, V&gt; newEnumMap(Map&lt;K, ? extends V&gt; map)返回不可变EnumMapImmutableMap&lt;K, V&gt; immutableEnumMap(Map&lt;K, ? extends V&gt; map)创建HashMap1、HashMap&lt;K, V&gt; newHashMap()
2、HashMap&lt;K, V&gt; newHashMapWithExpectedSize(int expectedSize)
3、HashMap&lt;K, V&gt; newHashMap(Map&lt;? extends K, ? extends V&gt; map)创建LinkedHashMap1、LinkedHashMap&lt;K, V&gt; newLinkedHashMap()
2、LinkedHashMap&lt;K, V&gt; newLinkedHashMap(Map&lt;? extends K, ? extends V&gt; map)创建ConcurrentMapConcurrentMap&lt;K, V&gt; newConcurrentMap()创建TreeMap1、TreeMap&lt;K, V&gt; newTreeMap()
2、TreeMap&lt;K, V&gt; newTreeMap(SortedMap&lt;K, ? extends V&gt; map)
3、TreeMap&lt;K, V&gt; newTreeMap(@Nullable Comparator&lt;C&gt; comparator)创建IdentityHashMapIdentityHashMap&lt;K, V&gt; newIdentityHashMap()获取两个Map中不同元素的值1、MapDifference&lt;K, V&gt; difference(Map&lt;? extends K, ? extends V&gt; left, Map&lt;? extends K, ? extends V&gt; right)
2、MapDifference&lt;K, V&gt; difference(Map&lt;? extends K, ? extends V&gt; left, Map&lt;? extends K, ? extends V&gt; right, Equivalence&lt;? super V&gt; valueEquivalence)
3、SortedMapDifference&lt;K, V&gt; difference(SortedMap&lt;K, ? extends V&gt; left, Map&lt;? extends K, ? extends V&gt; right)根据函数和set，构造Map1、Map&lt;K, V&gt; asMap(Set&lt;K&gt; set, Function&lt;? super K, V&gt; function)
2、SortedMap&lt;K, V&gt; asMap(SortedSet&lt;K&gt; set, Function&lt;? super K, V&gt; function)
3、NavigableMap&lt;K, V&gt; asMap(NavigableSet&lt;K&gt; set, Function&lt;? super K, V&gt; function)根据函数和迭代器，构造不可变的Map1、ImmutableMap&lt;K, V&gt; toMap(Iterator&lt;K&gt; keys, Function&lt;? super K, V&gt; valueFunction)
2、ImmutableMap&lt;K, V&gt; toMap(Iterator&lt;K&gt; keys, Function&lt;? super K, V&gt; valueFunction)
3、ImmutableMap&lt;K, V&gt; uniqueIndex(Iterable&lt;V&gt; values, Function&lt;? super V, K&gt; keyFunction)
4、ImmutableMap&lt;K, V&gt; uniqueIndex(Iterator&lt;V&gt; values, Function&lt;? super V, K&gt; keyFunction)从配置文件中读取数据，创建不可变的MapImmutableMap&lt;String, String&gt; fromProperties(Properties properties)返回Entry或Entry集合1、Entry&lt;K, V&gt; immutableEntry(@Nullable K key, @Nullable V value)
2、Set&lt;Entry&lt;K, V&gt;&gt; unmodifiableEntrySet(Set&lt;Entry&lt;K, V&gt;&gt; entrySet)
3、Entry&lt;K, V&gt; unmodifiableEntry(final Entry&lt;? extends K, ? extends V&gt; entry)返回特殊的BiMap类1、BiMap&lt;K, V&gt; synchronizedBiMap(BiMap&lt;K, V&gt; bimap)
2、BiMap&lt;K, V&gt; unmodifiableBiMap(BiMap&lt;? extends K, ? extends V&gt; bimap)根据Map和函数对Map进行转型1、Map&lt;K, V2&gt; transformValues(Map&lt;K, V1&gt; fromMap, Function&lt;? super V1, V2&gt; function)
2、SortedMap&lt;K, V2&gt; transformValues(SortedMap&lt;K, V1&gt; fromMap, Function&lt;? super V1, V2&gt; function)
3、NavigableMap&lt;K, V2&gt; transformValues(NavigableMap&lt;K, V1&gt; fromMap, Function&lt;? super V1, V2&gt; function)
4、Map&lt;K, V2&gt; transformEntries(Map&lt;K, V1&gt; fromMap, Maps.EntryTransformer&lt;? super K, ? super V1, V2&gt; transformer)
5、SortedMap&lt;K, V2&gt; transformEntries(SortedMap&lt;K, V1&gt; fromMap, Maps.EntryTransformer&lt;? super K, ? super V1, V2&gt; transformer)
6、NavigableMap&lt;K, V2&gt; transformEntries(NavigableMap&lt;K, V1&gt; fromMap, Maps.EntryTransformer&lt;? super K, ? super V1, V2&gt; transformer)使用函数进行过滤Map，然后返回同类型的Map分为4种过滤
一、针对Key进行过滤
1.Map&lt;K, V&gt; filterKeys(Map&lt;K, V&gt; unfiltered, Predicate&lt;? super K&gt; keyPredicate)
2.SortedMap&lt;K, V&gt; filterKeys(SortedMap&lt;K, V&gt; unfiltered, Predicate&lt;? super K&gt; keyPredicate)
3.NavigableMap&lt;K, V&gt; filterKeys(NavigableMap&lt;K, V&gt; unfiltered, Predicate&lt;? super K&gt; keyPredicate)
4.BiMap&lt;K, V&gt; filterKeys(BiMap&lt;K, V&gt; unfiltered, Predicate&lt;? super K&gt; keyPredicate)
二、针对Value进行过滤
1.Map&lt;K, V&gt; filterValues(Map&lt;K, V&gt; unfiltered, Predicate&lt;? super V&gt; valuePredicate)
2.SortedMap&lt;K, V&gt; filterValues(SortedMap&lt;K, V&gt; unfiltered, Predicate&lt;? super V&gt; valuePredicate)
3.NavigableMap&lt;K, V&gt; filterValues(NavigableMap&lt;K, V&gt; unfiltered, Predicate&lt;? super V&gt; valuePredicate)
4.BiMap&lt;K, V&gt; filterValues(BiMap&lt;K, V&gt; unfiltered, Predicate&lt;? super V&gt; valuePredicate)
三、针对Entry进行过滤
1.Map&lt;K, V&gt; filterEntries(Map&lt;K, V&gt; unfiltered, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
2.SortedMap&lt;K, V&gt; filterEntries(SortedMap&lt;K, V&gt; unfiltered, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
3.SortedMap&lt;K, V&gt; filterSortedIgnoreNavigable(SortedMap&lt;K, V&gt; unfiltered, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
4.NavigableMap&lt;K, V&gt; filterEntries(NavigableMap&lt;K, V&gt; unfiltered, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
5.BiMap&lt;K, V&gt; filterEntries(BiMap&lt;K, V&gt; unfiltered, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
四、为含有过滤规则的Map进行过滤
1.Map&lt;K, V&gt; filterFiltered(Maps.AbstractFilteredMap&lt;K, V&gt; map, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
2.SortedMap&lt;K, V&gt; filterFiltered(Maps.FilteredEntrySortedMap&lt;K, V&gt; map, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
3.NavigableMap&lt;K, V&gt; filterFiltered(Maps.FilteredEntryNavigableMap&lt;K, V&gt; map, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
4.BiMap&lt;K, V&gt; filterFiltered(Maps.FilteredEntryBiMap&lt;K, V&gt; map, Predicate&lt;? super Entry&lt;K, V&gt;&gt; entryPredicate)
### [创建EnumMap](#创建enummap)

1.
传入一个Class变量，返回一个EnumMap

1.
传入一个Map变量，返回一个EnumMap

### [返回不可变EnumMap](#返回不可变enummap)

传入一个Map，返回一个不可变的Map容器

### [创建HashMap](#创建hashmap)

1.
直接返回一个新的HashMap

1.
返回一个有初始长度的HashMap

这里为什么是 0.75这个系数呢？

1.
传入一个Map型变量，返回一个HashMap

### [创建LinkedHashMap](#创建linkedhashmap)

1.
直接返回一个新的LinkedHashMap

1.
传入一个Map变量，返回一个LinkedHashMap

### [创建ConcurrentMap](#创建concurrentmap)

直接返回一个新的ConcurrentMap

### [创建TreeMap](#创建treemap)

1.
直接返回一个新的TreeMap

1.
传入一个Map变量，返回一个TreeMap，并将Map的值赋值给TreeMap

1.
传入一个比较接口，返回一个根据传入的比较规则形成的TreeMap

### [创建IdentityHashMap](#创建identityhashmap)

直接返回一个identityHashMap

IdentityHashMap与HashMap不同之处在于可以存入相同类的相同值，实际上他在put里的添加操作是不是使用equals而是用的==进行判断的

### [获取两个Map中不同元素的值](#获取两个map中不同元素的值)

在说明Maps中这三个方法之前，先了解一下MapDifference接口和的实现类MapDifferenceImpl可以表现什么吧：

可以看到 MapDifferenceImpl 实现类中有4个变量

- onlyOnLeft只存变量名为left的Map中独有的；

- onlyOnRight只存变量名为right的Map中独有的；

- onBoth存储两个map中共有的key并且value也相等的元素；

- differences因为value存储的类型为ValueDifference，differences中存储的是共有的key并且value不同的元素

1.
传入两个Map变量，根据left变量名的Map的类型进行判断交给哪个difference方法去处理

1.
传入两个Map，使用doDifference方法将两个Map中的元素进行分类

1.
传入一个SortedMap和一个Map变量，返回一个分类后的类

### [根据函数和set，构造Map](#根据函数和set-构造map)

这个方法展示了如何将一个`Set`和一个`Function` 结合起来，创建一个视图（view），这个视图在每次查询时通过应用函数来动态生成键值对。

1. **视图特性**：`AsMapView`创建的是一个视图，而不是一个独立的新集合。这意味着原始集合（`Set`）的任何修改都会反映在`AsMapView`中，反之亦然。这种行为类似于如何通过`Collections.unmodifiableList()`方法得到的不可修改的视图，但`AsMapView`是可修改的，其修改会影响到原始的集合。

1. **延迟加载**：`AsMapView`在实际调用其`get()`方法之前不会计算键对应的值。这意味着如果你有一个非常昂贵的转换逻辑，它只有在实际需要该值时才会执行，这有助于提高效率。

1. **用途**：这个类非常适合创建动态计算的映射，其中映射的值是依赖于键的，并且可能不希望提前计算所有可能的值。例如，可以用它来根据需要生成配置设置、进行数据转换等。

1. **实现**：在内部，`AsMapView`使用了提供的`Set`和`Function`来实现`Map`接口。当调用`get(Object key)`时，如果`key`存在于集合中，则使用`Function`来计算值。

使用案例：

方法介绍：

1.
传入一个set和一个规则，返回一个Map

1.
传入一个SortedSet和一个规则，返回一个SortMap

1.
传入一个NavigableSet和一个规则，返回一个NavigableMap

### [根据函数和迭代器，构造不可变的Map](#根据函数和迭代器-构造不可变的map)

此类方法传入的是一个容器的迭代器和一个规则，然后返回一个不可变的Map容器

1.
传入一个key值容器和一个规则，直接交给重载函数去处理，返回一个不可变的Map容器

1.
传入一个key值迭代器和一个规则返回一个不可变的map容器

1.
根据value值容器和一个规则，直接交给重载函数去处理，返回一个不可变的Map容器

1.
传入一个value值迭代器和一个规则返回一个不可变的map容器

### [从properties文件中读取数据，创建不可变的Map](#从properties文件中读取数据-创建不可变的map)

从Properties获取的key和value，返回一个不可变的Map

### [返回Entry或Entry集合](#返回entry或entry集合)

传入一个key和一个value，返回一个不可变的Entry

### [返回特殊的BiMap类](#返回特殊的bimap类)

Guava 提供了 BiMap 支持支持双向的映射关系，关于BiMap详情可以看后文

1.
传入一个BiMap返回一个线程安全的BiMap

1.
传入一个BiMap返回一个unmodifiableBiMap

### [根据Map和函数对Map进行转型](#根据map和函数对map进行转型)

此类方法使用使用到了函数式编程，将一个Map的value作为新的Map的key，根据函数的规则计算出新的Map的Value，而这个转换只有在查看的时候才会做计算，而真正存储的是传入的map

1.
传入一个Map和一个规则，返回一个有规则计算出来的Map

1.
传入一个SortedMap和一个规则，返回一个由规则计算出来的新的Map

1.
传入一个NavigableMap和一个规则，返回一个由规则计算出来的NavigableMap

1.
传入一个Map和一个Maps规定的规则格式，根据规则返回一个新的Map

1.
传入一个NavigableMap和一个Maps规定的规则格式，根据规则返回一个新的NavigableMap

### [使用函数进行过滤Map，然后返回同类型的Map](#使用函数进行过滤map-然后返回同类型的map)

这里我们主要针对Key进行过滤的源码进行分析。当然Maps还提供了一些对Value、Entry、含有过滤器的Map进行过滤的方法。与上面过滤key的方法大体一样，都是继承了AbstractFilteredMap抽象类，实现了各自的过滤功能

使用keyPredicate函数接口制定过滤规则，对Map进行过滤，对于Map中Key进行过滤的类FilteredKeyMap源码如下：

1.
传入一个Map和过滤他的规则，返回一个新的Map

1.
传入一个SortedMap，然后交给filterEntries方法进行处理

1.
传入一个NavigableMap，然后交给filterEntries方法进行处理

1.
传入一个BiMap，然后交给filterEntries方法进行处理

## [Sets](#sets)

### [功能函数](#功能函数-2)
功能方法创建不可变的set1、ImmutableSet&lt;E&gt; immutableEnumSet(E anElement, E... otherElements)
2、ImmutableSet&lt;E&gt; immutableEnumSet(Iterable&lt;E&gt; elements)创建HashSet1、HashSet&lt;E&gt; newHashSet()
2、HashSet&lt;E&gt; newHashSet(E... elements)
3、HashSet&lt;E&gt; newHashSetWithExpectedSize(int expectedSize)
4、HashSet&lt;E&gt; newHashSet(Iterable&lt;? extends E&gt; elements)
5、HashSet&lt;E&gt; newHashSet(Iterator&lt;? extends E&gt; elements)创建线程安全的Set1、Set&lt;E&gt; newConcurrentHashSet()
2、Set&lt;E&gt; newConcurrentHashSet(Iterable&lt;? extends E&gt; elements)创建LinkedHashMap1、LinkedHashSet&lt;E&gt; newLinkedHashSet()
2、LinkedHashSet&lt;E&gt; newLinkedHashSetWithExpectedSize(int expectedSize)
3、LinkedHashSet&lt;E&gt; newLinkedHashSet(Iterable&lt;? extends E&gt; elements)创建TreeSet1、TreeSet&lt;E&gt; newTreeSet()
2、TreeSet&lt;E&gt; newTreeSet(Iterable&lt;? extends E&gt; elements)
3、TreeSet&lt;E&gt; newTreeSet(Comparator&lt;? super E&gt; comparator)创建IdentityHashSetSet&lt;E&gt; newIdentityHashSet()创建CopyOnWriteArraySet1、CopyOnWriteArraySet&lt;E&gt; newCopyOnWriteArraySet()
2、CopyOnWriteArraySet&lt;E&gt; newCopyOnWriteArraySet(Iterable&lt;? extends E&gt; elements)创建EnumSet1、EnumSet&lt;E&gt; newEnumSet(Iterable&lt;E&gt; iterable, Class&lt;E&gt; elementType)
2、EnumSet&lt;E&gt; complementOf(Collection&lt;E&gt; collection)
3、EnumSet&lt;E&gt; complementOf(Collection&lt;E&gt; collection, Class&lt;E&gt; type)
4、EnumSet&lt;E&gt; makeComplementByHand(Collection&lt;E&gt; collection, Class&lt;E&gt; type)根据Map创建一个SetSet&lt;E&gt; newSetFromMap(Map&lt;E, Boolean&gt; map)以两个Set的并集作为视图Sets.SetView&lt;E&gt; union(final Set&lt;? extends E&gt; set1, final Set&lt;? extends E&gt; set2)以两个Set的交集作为视图Sets.SetView&lt;E&gt; intersection(final Set&lt;E&gt; set1, final Set&lt;?&gt; set2)以两个Set的互不重叠的部分作为视图Sets.SetView&lt;E&gt; difference(final Set&lt;E&gt; set1, final Set&lt;?&gt; set2)以两个Set的对称部分作为视图Sets.SetView&lt;E&gt; symmetricDifference(Set&lt;? extends E&gt; set1, Set&lt;? extends E&gt; set2)过滤Set1、filter(Set&lt;E&gt; unfiltered, Predicate&lt;? super E&gt; predicate)
2、SortedSet&lt;E&gt; filter(SortedSet&lt;E&gt; unfiltered, Predicate&lt;? super E&gt; predicate)
3、SortedSet&lt;E&gt; filterSortedIgnoreNavigable(SortedSet&lt;E&gt; unfiltered, Predicate&lt;? super E&gt; predicate)
4、NavigableSet&lt;E&gt; filter(NavigableSet&lt;E&gt; unfiltered, Predicate&lt;? super E&gt; predicate)获取两个Set集合的笛卡尔积1、Set&lt;List&lt;B&gt;&gt; cartesianProduct(List&lt;? extends Set&lt;? extends B&gt;&gt; sets)
2、Set&lt;List&lt;B&gt;&gt; cartesianProduct(Set&lt;? extends B&gt;... sets)
### [创建不可变的Set](#创建不可变的set)

1.
根据传入的参数，创建一个不可变的Set

1.
根据一个集合创建一个不可变的Set

### [创建HashSet](#创建hashset)

1.
直接new一个HashSet

1.
传入一个数组，返回一个HashSet

1.
创建一个期望大小的HashSet

1.
根据传入的集合创建一个HashSet

1.
根据传入的迭代器创建一个HashSet

### [创建线程安全的Set](#创建线程安全的set)

1.
使用ConcurrentHashMap创建一个Set

1.
使用传入的集合创建一个线程安全的Set

### [创建LinkedHashSet](#创建linkedhashset)

1.
直接创建一个LinkedHashSet

1.
创建一个期望大小的LinkedHashSet

1.
根据传入的集合，返回一个LinkedHashSet

### [创建TreeSet](#创建treeset)

1.
直接创建一个TreeSet

1.
传入一个集合，返回一个TreeSet，并将集合中的元素赋值给TreeSet

1.
传入一个Comparator，根据Comparator的规则创建一个TreeSet

### [创建IdentityHashSet](#创建identityhashset)

根据Maps.newIdentityHashMap()和Sets.newSetFromMap两个方法创建一个IdentityHashSet

### [创建CopyOnWriteArraySet](#创建copyonwritearrayset)

1.
直接创建一个CopyOnWriteArraySet

1.
根据传入的集合创建一个CopyOnWriteArraySet，并将集合中的数据赋值给CopyOnWriteArraySet

### [创建EnumSet](#创建enumset)

1.
根据传入的集合和一个类型，返回一个EnumSet

1.
传入一个集合，返回一个EnumSet

### [根据一个Map创建一个Set](#根据一个map创建一个set)

根据Map创建一个Set

### [以两个Set的互不重叠的部分作为视图](#以两个set的互不重叠的部分作为视图)

传入两个Set，返回一个两个set1中不包含set2中的元素

### [以两个Set的并集作为视图](#以两个set的并集作为视图)

### [以两个Set的交集作为视图](#以两个set的交集作为视图)

### [以两个Set的对称部分作为视图](#以两个set的对称部分作为视图)

### [过滤Set](#过滤set)

Set的过滤和Maps中实现的各种过滤都是大同小异。

传入一个Set和一个过滤规则，返回一个过滤后的Set：
