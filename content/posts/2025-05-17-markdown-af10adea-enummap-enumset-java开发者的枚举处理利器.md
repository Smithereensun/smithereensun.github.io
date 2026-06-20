{

  "title": "EnumMap & EnumSet：Java开发者的枚举处理利器",
  "has_date": true,
  "description": "在EffectiveJava中的第 36条中建议 用 EnumSet 替代位字段，在第37条中建议 用EnumMap替换序数索引，为什么？ EnumSet 在EffectiveJava中的第 36条中建议 用 EnumSet 替代位字段 、用 EnumSet替代位字段 如果枚举类型的元素主要在 Se",
  "tags": [
    "Java",
    "集合"
  ],
  "source": "local-markdown-library",
  "source_path": "java/collection/03-map4-enumset-map - EnumMap & EnumSet：Java开发者的枚举处理利器.md",
  "date": "2025-05-17"

}

在EffectiveJava中的第 36条中建议 用 EnumSet 替代位字段，在第37条中建议 用EnumMap替换序数索引，为什么？

## [EnumSet](#enumset)

在EffectiveJava中的第 36条中建议 用 EnumSet 替代位字段

### [36、用 EnumSet替代位字段](#_36、用-enumset替代位字段)

如果枚举类型的元素主要在 Set 中使用，传统上使用 int 枚举模式，通过不同的 2 的平方数为每个常量赋值：

这种表示方式称为位字段，允许你使用位运算的或操作将几个常量组合成一个 Set：

位字段具有 int 枚举常量所有缺点，例如：

1. 被打印成数字时难以理解

1. 没有简单的方法遍历位字段所有元素

1. 一旦确定了int或long作为位字段的存储类型，就不能超过它的范围（32位或64位）

EnumSet类是一种更好的选择，它避免了以上缺点。而且由于它在底层实现上与位操作类似，因此与位字段性能相当。

将之前的示例修改为使用EnumSet的方法，更加简单清晰：

下面是将 EnumSet 实例传递给 applyStyles 方法的用户代码。EnumSet 类提供了一组丰富的静态工厂，可以方便地创建 Set：

EnumSet是与枚举类型一起使用的专用 Set 集合，EnumSet 中所有元素都必须是枚举类型。

与其他Set接口的实现类HashSet/TreeSet(内部都是用对应的HashMap/TreeMap实现的)不同的是，EnumSet在内部实现是位向量，它是一种极为高效的位运算操作，由于直接存储和操作都是bit，因此EnumSet空间和时间性能都十分可观，足以媲美传统上基于 int 的“位标志”的运算。并且重要的是我们可像操作set集合一般来操作位运算，这样使用代码更简单易懂同时又具备类型安全的优势。

**注意**：EnumSet不允许使用 null 元素。试图插入 null 元素将抛出 NullPointerException，但试图测试判断是否存在null 元素或移除 null 元素则不会抛出异常，与大多数collection 实现一样，EnumSet不是线程安全的，因此在多线程环境下应该注意数据同步问题。

那么EnumSet是如何使用的，底层实现是怎么样的呢？

### [基本用法](#基本用法)

创建EnumSet并不能使用new关键字，因为它是个抽象类，而应该使用其提供的静态工厂方法，EnumSet的静态工厂方法比较多，如下：

代码演示如下：

### [源码分析](#源码分析)

#### [初始化方法](#初始化方法)

以 `noneOf` 方法为例，来看下 `EnumSet` 是如何初始化的

在 noneOf 方法中首先根据枚举类型获取所有的枚举值，接着判断然后根据枚举类型的元素个数初始化对应的 EnumSet 对象。

RegularEnumSet 使用一个long对象来存储EnumSet的元素。 long元素的每一个比特都代表一个Enum值。 由于long的大小是64位，它可以存储多达64个不同的元素。 JumboEnumSet 使用一个long元素的数组来存储EnumSet的元素。 与RegularEnumSet的唯一区别是**JumboEnumSet使用一个长数组来存储位向量，从而允许超过64个值**。

- getUniverse 方法如下：

关于 SharedSecrets，Java 官方文档是这么描述的：A repository of “shared secrets”, which are a mechanism for calling implementation-private methods in another package without using reflection.
 意思是在不使用反射的情况下在另外的包中调用实现私有方法的机制。而 SharedSecrets.getJavaLangAccess().getEnumConstantsShared 方法用于获取指定类型的枚举元素数组。

#### [add 方法](#add-方法)

下面以 RegularEnumSet 为例来看下具体源码的实现细节。

首先进行枚举类型检查，接着用一个 long 类型的整数值接收 elements，下面是 elements 在 RegularEnumSet 中的定义：

在 RegularEnumSet 中使用的是一个 long 整数（二进制）来表示是否添加或者删除了某个枚举值。添加枚举元素的关键代码是这句：`elements |= (1L &lt;&lt; ((Enum&lt;?&gt;)e).ordinal());`，下面我们以一个例子来说明是如何把枚举元素添加到集合的。

以 Season 枚举为例，假设此时没有添加任何元素则 elements 的值为 0，现在往集合里添加元素 FAIL，假设 FAIL的顺序为2，则e.ordinal() 的值为 2，1 右移 2 位值为 4，换成二进制表示为 0000 0100。如果 elements 用二进制表示且某下标（index）的值为 1，则表示该位上有枚举元素，则枚举元素就是 e.ordinal() = index 位置上的。

再举个例子验证一下，假设集合中已经有了 FAIL 元素则 elements 的值为 4（0000 0100），现在添加元素 WINTER，假设 WINTER的顺序为3，e.ordinal() 的值为 3，1 右移 3 位值为 8，换成二进制表示为 0000 1000，与 elements 进行或运算后是（0000 1100）。此时就表示有FAIL 和 WINTER两个值了

#### [remove 方法](#remove-方法)

移除元素无非就是把对应位置上的 1 替换为 0，`elements &= ~(1L &lt;&lt; ((Enum&lt;?&gt;)e).ordinal());` 这行代码执行的就是这个逻辑。

假设现在集合中有 FAIL 与 WINTER，则 elements 的值为 12（0000 1100），现在我们要移除 FAIL，`(1L &lt;&lt; ((Enum&lt;?&gt;)e).ordinal())` 运算过后值为 4（0000 0100），取反过后为 1111 1011，与 0000 1100 进行与运算之后为 0000 1000，最后的结果可以看出，FAIL 对应位置上的 1 经过运算之后变成了 0。

## [EnumMap](#enummap)

在第37条中建议 用EnumMap替换序数索引

### [37、使用 EnumMap替换序数索引](#_37、使用-enummap替换序数索引)

**用序数索引数组不如使用 EnumMap，应尽量少使用 `ordinal()` 。**

例如这个类表示一种植物：

假设有一个代表花园全部植物的 Plant 数组 plantsByLifeCycle，用于列出按生命周期（一年生、多年生或两年生）排列的植物：

有些程序员会将这些集合放到一个按照类型序号进行索引的数组实现这一点。

这种技术有如下问题：

1.
数组与泛型不兼容，需要 unchecked 转换。

  1.
**类型擦除**：Java 的泛型是在编译时实现的，也就是说，在运行时，泛型类型信息会被擦除。而在Java中，数组是一个协变的、具有运行时类型信息的数据结构。由于泛型信息在运行时被擦除，因此在运行时无法知道具体的泛型参数类型，这和数组的运行时类型信息是相冲突的。

  1.
**类型安全性**：Java为了保证类型安全，禁止了泛型数组的创建。假设Java允许我们创建泛型数组，则有可能发生下面的情况：

这里，将一个`ArrayList&lt;Integer&gt;`赋给了一个`Object[]`引用，并没有引发任何警告或错误。但是，现在`stringLists[0]`实际上就是一个Integer列表，如果我们试图在其中放入一个字符串，就会在运行时抛出`ClassCastException`。

1.
数组不知道索引表示什么，必须手动标记输出。

1.
int 不提供枚举的类型安全性，无法检验int值的正确性。

解决方案：

1.
使用 `java.util.EnumMap`：

这个程序比原来的版本更短，更清晰，更安全，速度也差不多。速度相当的原因是，EnumMap 在内部使用这样的数组，但是它向程序员隐藏了实现细节。

1.
使用流可以进一步缩短程序：

这段代码的性能较差，因为底层不是基于 EnumMap，而是自己实现Map。

1.
要改进性能，可以使用 mapFactory 参数指定 Map 实现：

下面例子用二维数组描述了气液固三台之间的装换，并使用序数索引读取二维数组的值：

这个程序的问题与前面 garden 示例一样，编译器无法知道序数和数组索引之间的关系。如果你在转换表中出错，或者在修改 Phase 或 `Phase.Transition` 枚举类型时忘记更新，程序将在运行时失败。

使用 EnumMap 可以做得更好：

如果你想向系统中加入一种新阶段：等离子体。这个阶段只有两个变化：电离、去离子作用。修改基于EnumMap的版本要比基于数组的版本容易得多，而且更加清晰安全：

那么EnumMap是如何使用的，底层实现是怎么样的呢？

### [基本用法](#基本用法-1)

先思考这样一个问题，现在有一堆size大小相同而颜色不同的数据，需要统计出每种颜色的数量是多少以便将数据录入仓库，定义如下枚举用于表示颜色Color:

代码比较简单，我们使用两种解决方案，一种是HashMap，一种EnumMap，虽然都统计出了正确的结果，但是EnumMap作为枚举的专属的集合，我们没有理由再去使用HashMap，毕竟**EnumMap要求其Key必须为Enum类型**，因而使用Color枚举实例作为key是最恰当不过了，也避免了获取name的步骤，

更重要的是EnumMap效率更高，因为其内部是通过数组实现的（稍后分析），注意EnumMap的key值不能为null，虽说是枚举专属集合，但其操作与一般的Map差不多，概括性来说EnumMap是专门为枚举类型量身定做的Map实现，虽然使用其它的Map（如HashMap）也能完成相同的功能，但是使用EnumMap会更加高效，它只能接收同一枚举类型的实例作为键值且不能为null，由于枚举类型实例的数量相对固定并且有限，所以EnumMap使用数组来存放与枚举类型对应的值，毕竟数组是一段连续的内存空间，根据程序局部性原理，效率会相当高。

下面我们来进一步了解EnumMap的用法，先看构造函数：

与HashMap不同，它需要传递一个类型信息，即Class对象，通过这个参数EnumMap就可以根据类型信息初始化其内部数据结构，另外两个构造函数初始化时传入一个Map集合，代码演示如下：

至于EnumMap的方法，跟普通的map几乎没有区别，注意与HashMap的主要不同在于构造方法需要传递类型参数和EnumMap保证Key顺序与枚举中的顺序一致，但请记住Key不能为null。

### [源码分析](#源码分析-1)

EnumMap的源码部分我们主要分析其内部存储结构，添加查找的实现，了解这几点，对应EnumMap内部实现原理也就比较清晰了

#### [数据结构和构造函数](#数据结构和构造函数)

EnumMap继承了AbstractMap类，因此EnumMap具备一般map的使用方法。

在构造函数中通过`keyUniverse = getKeyUniverse(keyType);` 初始化了keyUniverse数组的值，内部存储的是所有可能的枚举值，接着初始化了存在Value值得数组vals，其大小与枚举实例的个数相同，getKeyUniverse方法实现如下

从方法的返回值来看，返回类型是枚举数组；显然，最终返回值正是枚举类型的values方法的返回值，在枚举章节我们分析过values方法返回所有可能的枚举值，因此keyUniverse数组存储就是枚举类型的所有可能的枚举值。

#### [put方法](#put方法)

这里通过typeCheck方法进行了key类型检测，判断是否为枚举类型，如果类型不对，会抛出异常

接着通过`int index = key.ordinal()`的方式获取到该枚举实例的顺序值，利用此值作为下标，把值存储在vals数组对应下标的元素中即`vals[index]`，这也是为什么EnumMap能维持与枚举实例相同存储顺序的原因。

在对vals[]中元素进行赋值和返回旧值时分别调用了maskNull方法和unmaskNull方法

由此看来EnumMap还是允许存放null值的，但key绝对不能为null，对于null值，EnumMap进行了特殊处理，将其包装为NULL对象，毕竟vals[]存的是Object，maskNull方法和unmaskNull方法正是用于null的包装和解包装的。

#### [get方法](#get方法)

相对应put方法，get方法显得相当简洁，key有效的话，直接通过ordinal方法取索引，然后在值数组vals里通过索引获取值返回。

#### [remove方法](#remove方法)

非常简单，key值有效，通过key获取下标索引值，把vals[]对应下标值设置为null，size减一。

#### [contains方法](#contains方法)

#### [小结](#小结)

这就是EnumMap的主要实现原理，即内部有两个数组，长度相同，一个表示所有可能的键(枚举值)，一个表示对应的值，不允许keynull，但允许value为null，键都有一个对应的索引，根据索引直接访问和操作其键数组和值数组，由于操作都是数组，因此效率很高。
