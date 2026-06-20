{

  "title": "新集合 - BiMap&Multimap&Multiset",
  "has_date": true,
  "description": "BiMap Map 可以实现 key -&gt; value 的映射，如果想要 value -&gt; key 的映射，就需要定义两个 Map，并且同步更新，很不优雅。Guava 提供了 BiMap 支持支持双向的映射关系，常用实现有 。 而它对key和value严格的保证唯一性。如果使用put方法",
  "tags": [
    "工具库"
  ],
  "source": "local-markdown-library",
  "source_path": "tool-library/guava/guava-newcollections - 新集合 - BiMap&Multimap&Multiset.md",
  "date": "2025-05-17"

}

## [BiMap](#bimap)

Map 可以实现 key -&gt; value 的映射，如果想要 value -&gt; key 的映射，就需要定义两个 Map，并且同步更新，很不优雅。Guava 提供了 BiMap 支持支持双向的映射关系，常用实现有`HashMap, EnumBiMap, EnumHashBiMap...`。

而它对key和value严格的保证唯一性。如果使用put方法添加相同的value值或key值则会抛出异常：java.lang.IllegalArgumentException，如果使用forcePut方法添加则会覆盖掉原来的value值。

这里主要使用HashBiMap 进行分析

### [成员变量](#成员变量)

HashMap做的是唯一key值对应的value可以不唯一，而Bimap做的是唯一key值，value值也要唯一，方便从key找到value，从value找到key

对比一下HashMap的Node源码：

### [构造方法](#构造方法)

可以看到构造方法是私有的，所以在类中一定会有静态方法构造器会用到这个私有的构造方法。

这个构造方法调用了init方法，可以看一下init方法的源码：

### [静态方法构造器](#静态方法构造器)

### [添加功能](#添加功能)

添加功能有两种，一个是put方法，一个是forcePut方法：

可以看到，这两个方法同时调用了本类的put方法，只不过是这两个方法的第三个参数不同，一个为ture，一个为false，看一下put的源码，看看第三个参数有什么用

## [Multimap](#multimap)

支持将 key 映射到多个 value 的方式，而不用定义`Map&lt;K, List&lt;V&gt;&gt; 或 Map&lt;K, Set&lt;V&gt;&gt;`这样的形式。实现类包括`ArrayListMultimap, HashMultimap, LinkedListMultimap, TreeMultimap...`

### [HashMultimap构造器](#hashmultimap构造器)

因为他的构造方法是私有的，所有他会拥有静态方法构造器：

三个构造方法都调用了私有的构造器，私有构造器的源码如下：

三个私有构造方法都调用了父类的构造方法，接下来看看父类的构造器源码，发现最后的Multimap的数据结构也体现在AbstractMapBasedMultimap这个类中，所以看一下这个类的构造器个变量：

### [put方法的实现](#put方法的实现)

### [get方法的实现](#get方法的实现)

## [Multiset](#multiset)

Multiset 是一个新的集合类型，可以多次添加相等的元素，既可以看成是无序的列表，也可以看成存储元素和对应数量的键值对映射`[E1: cnt1; E2:cnt2]`。常用实现包括 `HashMultiset, TreeMultiset, LinkedHashMultiset...`

### [接口源码](#接口源码)

Multiset的接口中方法的实现在AbstractMapBasedMultiset抽象类中，下面针对AbstractMapBasedMultiset类的存储数据结构。add、remove、count和迭代器的实现进行分析

### [存储数据结构](#存储数据结构)

### [构造方法](#构造方法-1)

### [add方法](#add方法)

### [remove方法](#remove方法)

### [Count方法](#count方法)

### [迭代器](#迭代器)

Multiset中有一个实现了Iterator接口的类：

这个迭代器的好处是，存储多个相同的值，不会占用多个地方，只会占用1个位置。
