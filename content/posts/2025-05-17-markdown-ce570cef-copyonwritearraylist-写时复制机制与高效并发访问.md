{

  "title": "CopyOnWriteArrayList：写时复制机制与高效并发访问",
  "has_date": true,
  "description": "前言 Vector无论是add方法还是get方法都加上了**synchronized**修饰，当多线程读写List必须排队执行，很显然这样效率比较是低下的，CopyOnWriteArrayList是读写分离的，好处是提高线程访问效率。 CopyOnWrite容器即**写时复制**的容器。通俗的理解是",
  "tags": [
    "Java",
    "集合"
  ],
  "source": "local-markdown-library",
  "source_path": "java/collection/04-juc1-copyonwritearrayList - CopyOnWriteArrayList：写时复制机制与高效并发访问.md",
  "date": "2025-05-17"

}

## [前言](#前言)

Vector无论是add方法还是get方法都加上了**synchronized**修饰，当多线程读写List必须排队执行，很显然这样效率比较是低下的，CopyOnWriteArrayList是读写分离的，好处是提高线程访问效率。

CopyOnWrite容器即**写时复制**的容器。通俗的理解是当往一个容器添加元素的时候，不直接往当前容器添加，而是先将当前容器里的值Copy到新的容器，然后再往新的容器里添加元素，添加完元素之后，再将原容器的引用指向新的容器。这样做的好处是我们可以对CopyOnWrite容器进行并发的读 要加锁，因为当前容器不会添加任何元素。所以CopyOnWrite容器也是一种读写分离的思想，读和写不同的容器。

## [底层原理](#底层原理)

1. CopyOnWriteArrayList的动态数组机制 -- 它内部有个volatile数组(array)来保持数据。在“添加/删除”数据时，都会新建一个数组，并将更新后的数据拷贝到新建的数组中，最后再将该数组赋值给volatile数组。这就是它叫做CopyOnWriteArrayList的原因！

1. 每一个CopyOnWriteArrayList都和一个监视器锁lock绑定，通过lock，实现了对CopyOnWriteArrayList的互斥添加/删除。

### [类的继承关系](#类的继承关系)

CopyOnWriteArrayList实现了List接口，List接口定义了对列表的基本操作；同时实现了RandomAccess接口，表示可以随机访问(数组具有随机访问的特性)；同时实现了Cloneable接口，表示可克隆；同时也实现了Serializable接口，表示可被序列化。

### [类的内部类](#类的内部类)

- COWIterator类

COWIterator表示迭代器，其也有一个Object类型的数组作为CopyOnWriteArrayList数组的快照，这种快照风格的迭代器方法在创建迭代器时使用了对当时数组状态的引用。此数组在迭代器的生存期内不会更改，因此不可能发生冲突，并且迭代器保证不会抛出 ConcurrentModificationException。创建迭代器以后，迭代器就不会反映列表的添加、移除或者更改。在迭代器上进行的元素更改操作(remove、set 和 add)不受支持。这些方法将抛出 UnsupportedOperationException。

### [类的属性](#类的属性)

属性中有一个可重入锁，用来保证线程安全访问，还有一个Object类型的数组，用来存放具体的元素。当然，也使用到了反射机制和CAS来保证原子性的修改lock域。

### [类的构造函数](#类的构造函数)

- 默认构造函数

- CopyOnWriteArrayList(Collection&lt;? extends E&gt;)

该构造函数的处理流程如下

1.
判断传入的集合c的类型是否为CopyOnWriteArrayList类型，若是，则获取该集合类型的底层数组(Object[])，并且设置当前CopyOnWriteArrayList的数组(Object[]数组)，进入步骤③；否则，进入步骤②

1.
将传入的集合转化为数组elements，判断elements的类型是否为Object[]类型(toArray方法可能不会返回Object类型的数组)，若不是，则将elements转化为Object类型的数组。进入步骤③

1.
设置当前CopyOnWriteArrayList的Object[]为elements。

- CopyOnWriteArrayList(E[])：该构造函数用于创建一个保存给定数组的副本的列表。

### [核心函数分析](#核心函数分析)

对于CopyOnWriteArrayList的函数分析，主要明白Arrays.copyOf方法即可理解CopyOnWriteArrayList其他函数的意义。

#### [copyOf函数](#copyof函数)

该函数用于复制指定的数组，截取或用 null 填充(如有必要)，以使副本具有指定的长度。

#### [add函数](#add函数)

此函数用于将指定元素添加到此列表的尾部，处理流程如下

1. 获取锁(保证多线程的安全访问)，获取当前的Object数组，获取Object数组的长度为length，进入步骤②。

1. 根据Object数组复制一个长度为length+1的Object数组为newElements(此时，newElements[length]为null)，进入下一步骤。

1. 将下标为length的数组元素newElements[length]设置为元素e，再设置当前Object[]为newElements，释放锁，返回。这样就完成了元素的添加。

#### [addIfAbsent方法](#addifabsent方法)

该函数用于添加元素(如果数组中不存在，则添加；否则，不添加，直接返回)，可以保证多线程环境下不会重复添加元素。

该函数的流程如下:

1.
获取锁，获取当前数组为current，current长度为len，判断数组之前的快照snapshot是否等于当前数组current，若不相等，则进入步骤2；否则，进入步骤4

1.
不相等，表示在snapshot与current之间，对数组进行了修改(如进行了add、set、remove等操作)，获取长度(snapshot与current之间的较小者)，对current进行遍历操作，若遍历过程发现snapshot与current的元素不相等并且current的元素与指定元素相等(可能进行了set操作)，进入步骤5，否则，进入步骤3

1.
在当前数组中索引指定元素，若能够找到，进入步骤5，否则，进入步骤4

1.
复制当前数组current为newElements，长度为len+1，此时newElements[len]为null。再设置newElements[len]为指定元素e，再设置数组，进入步骤5

1.
释放锁，返回。

#### [set函数](#set函数)

此函数用于用指定的元素替代此列表指定位置上的元素，也是基于数组的复制来实现的。

#### [remove函数](#remove函数)

此函数用于移除此列表指定位置上的元素。

处理流程如下

1. 获取锁，获取数组elements，数组长度为length，获取索引的值elements[index]，计算需要移动的元素个数(length - index - 1),若个数为0，则表示移除的是数组的最后一个元素，复制elements数组，复制长度为length-1，然后设置数组，进入步骤③；否则，进入步骤②

1. 先复制index索引前的元素，再复制index索引后的元素，然后设置数组。

1. 释放锁，返回旧值

1.

## [CopyOnWriteArrayList是Fail Safe的](#copyonwritearraylist是fail-safe的)

采用安全失败机制的集合容器，在遍历时不是直接在集合内容上访问的，而是先复制原有集合内容，在拷贝的集合上进行遍历。java.util.concurrent包下的容器都是安全失败，可以在多线程下并发使用，并发修改。

原理：由于迭代时是对原集合的拷贝进行遍历，所以在遍历过程中对原集合所作的修改并不能被迭代器检测到，所以不会触发Concurrent Modification Exception。

缺点：基于拷贝内容的优点是避免了Concurrent Modification Exception，但同样地，迭代器并不能访问到修改后的内容，即：迭代器遍历的是开始遍历那一刻拿到的集合拷贝，在遍历期间原集合发生的修改迭代器是不知道的。

Vector无论是add方法还是get方法都加上了**synchronized**修饰，当多线程读写List必须排队执行，很显然这样效率比较是低下的，CopyOnWriteArrayList是读写分离的，好处是提高线程访问效率。

## [缺陷和使用场景](#缺陷和使用场景)

- CopyOnWriteArrayList的写效率比Vector慢。当CopyOnWriteArrayList写元素时是通过备份数组的方式实现的，当多线程同步激烈，数据量较大时会不停的**复制数组，内存浪费严重**。如果原数组的内容比较多的情况下，可能导致young gc或者full gc

- 弱一致性：不能用于实时读的场景，像拷贝数组、新增元素都需要时间，所以调用一个set操作后，读取到数据可能还是旧的，虽然CopyOnWriteArrayList 能做到最终一致性，但是还是没法满足实时性要求；

**小结：** CopyOnWriteArrayList合适读多写少的场景，例如黑名单白名单等
