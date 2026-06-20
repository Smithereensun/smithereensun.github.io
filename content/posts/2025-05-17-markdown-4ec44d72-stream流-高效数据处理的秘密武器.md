{

  "title": "Stream流：高效数据处理的秘密武器",
  "has_date": true,
  "description": "Java 8的新特性之一就是流stream，配合同版本出现的 ，使得操作集合（Collection）提供了极大的便利。 案例引入 在JAVA中，涉及到对数组、Collection等集合类中的元素进行操作的时候，通常会通过循环的方式进行逐个处理，或者使用Stream的方式进行处理。 假设遇到了这么一个",
  "tags": [
    "Java"
  ],
  "source": "local-markdown-library",
  "source_path": "java/basis/stream - Stream流：高效数据处理的秘密武器.md",
  "date": "2025-05-17"

}

Java 8的新特性之一就是流stream，配合同版本出现的 `Lambda`，使得操作集合（Collection）提供了极大的便利。

## [案例引入](#案例引入)

在JAVA中，涉及到对数组、Collection等集合类中的元素进行操作的时候，通常会通过循环的方式进行逐个处理，或者使用Stream的方式进行处理。

假设遇到了这么一个需求：从给定句子中返回单词长度大于5的单词列表，按长度倒序输出，最多返回3个。

在未接触Stream流的时候，可能会这样写函数：

然而，如果用上了Stream流：

就是两个字：优雅

### [流的三大特点](#流的三大特点)

流) (Stream) 到底是什么呢？是数据渠道，用于操作数据源（集合、数组等）所生成的元素序列。“ 集合讲的是数据， 流讲的是 计 算 ！ ”

1. 流并**不存储元素**。这些元素**存储在底层的集合中**，或者是按需生成。

1. 流的操作不会修改源数据元素，而是生成一个新的流。

1. 流的操作是尽可能**惰性执行**的。这意味着直至需要其结果时，操作才会执行。

### [操作分类](#操作分类)

官方将 Stream 中的操作分为两大类：

- `中间操作（Intermediate operations）`，只对操作进行了记录，即只会返回一个流，不会进行计算操作。

- `终结操作（Terminal operations）`，实现了计算操作。

中间操作又可以分为：

- `无状态（Stateless）操作`，元素的处理不受之前元素的影响。

- `有状态（Stateful）操作`，指该操作只有拿到所有元素之后才能继续下去。

终结操作又可以分为：

- `短路（Short-circuiting）`操作，指遇到某些符合条件的元素就可以得到最终结果

- `非短路（Unshort-circuiting）`操作，指必须处理完所有元素才能得到最终结果。

![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/8fd0fa80f4dc-202408011606864.jpeg)
## [如何使用](#如何使用)

概括讲，可以将Stream流操作分为3种类型：

- 创建Stream

- Stream中间处理

- 终止Steam

![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/ea3512efa1b3-202408172140064.webp)
每个Stream管道操作都包含若干方法，先列举一下各个API的方法：

### [开始管道](#开始管道)

主要负责新建一个Stream流，或者基于现有的数组、List、Set、Map等集合类型对象创建出新的Stream流。
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/fe4faf5ce594-202408172141732.webp)
#### [由数组创建流](#由数组创建流)

Java8 中的 Arrays 的静态方法 stream() 可以获取数组流：

- static &lt;T&gt; Stream&lt;T&gt; stream(T[] array): 返回一个流

重载形式， 能够处理对应基本类型的数组 ：

- public static IntStream stream(int[] array)

- public static LongStream stream(long[] array)

- public static DoubleStream stream(double[] array)

#### [由值创建流](#由值创建流)

可以使用静态方法 Stream.of()，通过显示的值创建一个流。它可以接收任意数量的参数。

- public static&lt;T&gt; Stream&lt;T&gt; of(T... values) : 返回一个流

#### [由函数创建流 ： 创建无限流](#由函数创建流-创建无限流)

可以使用静态方法 Stream.iterate() 和Stream.generate()，创建无限流。

- 迭代：public static&lt;T&gt; Stream&lt;T&gt; iterate(final T seed, final UnaryOperator&lt;T&gt; f)

- 生成：public static&lt;T&gt; Stream&lt;T&gt; generate(Supplier&lt;T&gt; s) :

### [中间管道](#中间管道)

负责对Stream进行处理操作，并返回一个新的Stream对象，中间管道操作可以进行叠加。
API功能说明filter()按照条件过滤符合要求的元素， 返回新的stream流。map()将已有元素转换为另一个对象类型，一对一逻辑，返回新的stream流。flatMap()将已有元素转换为另一个对象类型，一对多逻辑，即原来一个元素对象可能会转换为1个或者多个新类型的元素，返回新的stream流。limit()仅保留集合前面指定个数的元素，返回新的stream流。skip()跳过集合前面指定个数的元素，返回新的stream流。concat()将两个流的数据合并起来为1个新的流，返回新的stream流。distinct()对Stream中所有元素进行去重，返回新的stream流。sorted()对stream中所有的元素按照指定规则进行排序，返回新的stream流。peek()对stream流中的每个元素进行逐个遍历处理，返回处理后的stream流。
#### [map与flatMap](#map与flatmap)

在项目中，经常看到也经常使用到map与flatMap，比如代码：
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/54c64dc724a0-202408172146514.webp)
map与flatMap都是用于转换已有的元素为其它元素，区别点在于：

- map 必须是一对一的，即每个元素都只能转换为1个新的元素；

- flatMap 可以是一对多的，即每个元素都可以转换为1个或者多个新的元素；

下面两张图形象地说明了两者之间的区别：

map图：
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/688f04526582-202408172146520.webp)

flatMap图：
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/a90ce18cc4cf-202408172146496.webp)
##### [map用例](#map用例)

有一个字符串ID列表，现在需要将其转为别的对象列表。

##### [flatMap用例](#flatmap用例)

现有一个句子列表，需要将句子中每个单词都提取出来得到一个所有单词列表：

这里需要补充一句，flatMap操作的时候其实是先每个元素处理并返回一个新的Stream，然后将多个Stream展开合并为了一个完整的新的Stream，如下：
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/80c557685e64-202408172147908.webp)
#### [peek方法](#peek方法)

peek可以用于对元素进行遍历然后逐个处理。

peek属于中间方法，这也就意味着peek只能作为管道中途的一个处理步骤，而没法直接执行得到结果，其后面必须还要有其它终止操作的时候才会被执行

#### [filter、sorted、distinct、limit](#filter、sorted、distinct、limit)

这几个都是常用的Stream的中间操作方法，具体的方法的含义在上面的表格里面有说明。具体使用的时候，可以根据需要选择一个或者多个进行组合使用，或者同时使用多个相同方法的组合：

### [终止管道](#终止管道)

顾名思义，通过终止管道操作之后，Stream流将会结束，最后可能会执行某些逻辑处理，或者是按照要求返回某些执行后的结果数据。
API功能说明count()返回stream处理后最终的元素个数。max()返回stream处理后的元素最大值。min()返回stream处理后的元素最小值。findFirst()找到第一个符合条件的元素时则终止流处理。findAny()找到任何一个符合条件的元素时则退出流处理，这个对于串行流时与findFirst相同，对于并行流时比较高效，任何分片中找到都会终止后续计算逻辑。anyMatch()返回一个boolean值，类似于isContains(),用于判断是否有符合条件的元素。allMatch()返回一个boolean值，用于判断是否所有元素都符合条件。noneMatch()返回一个boolean值， 用于判断是否所有元素都不符合条件。collect()将流转换为指定的类型，通过Collectors进行指定。toArray()将流转换为数组。iterator()将流转换为Iterator对象。foreach()无返回值，对元素进行逐个遍历，然后执行给定的处理逻辑。
#### [foreach](#foreach)

foreach和peek一样，都可以用于对元素进行遍历然后逐个处理。但foreach属于终止方法，也就是说foreach可以直接执行相关操作。

#### [collect](#collect)

可以支持生成如下类型的结果数据：

1.
一个集合类，比如List、Set或者HashMap等；

1.
StringBuilder对象，支持将多个字符串进行拼接处理并输出拼接后结果；

1.
一个可以记录个数或者计算总和的对象（数据批量运算统计）；

#### [对 Stream 流操作认知不完善导致的空指针异常](#对-stream-流操作认知不完善导致的空指针异常)

findFirst()方法需要可能会存在的空指针问题！

例如，如果第一个元素恰好为 `null`，`findFirst()` 将抛出 `NullPointerException`。这是因为 `findFirst()` 返回一个 `Optional`，而 `Optional` 不能包含空值。

`max()`、`min()` 和 `reduce()`，也表现出类似的行为。如果 `null` 是最终结果，则会抛出异常。

再例如：我们在使用 `Stream` 流式编程时，如果流包含 `null`，可以转换为 `toList()` 或 `toSet()`；

然而，`toMap()` 要注意， 不允许空值（允许空Key）：

以及：`groupingBy()` 不允许空 Key：

可见在流中使用了空对象存在许多陷阱；所以，要重点关注 Stream 流的数据来源，避免在流中存在 `null`，不确定的话建议用 `filter(Objects::nonNull)` 将它们过滤掉。

## [并行Stream](#并行stream)

### [parallelStream的机制说明](#parallelstream的机制说明)

使用并行流，可以有效利用计算机的多CPU硬件，提升逻辑的执行速度。并行流通过将一整个stream划分为多个片段，然后对各个分片流并行执行处理逻辑，最后将各个分片流的执行结果汇总为一个整体流。
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/60543db67295-202408172159067.gif)
可以通过parallelStream的源码发现parallel Stream底层是将任务进行了切分，最终将任务传递给了jdk8自带的“全局”ForkJoinPool线程池。 在Fork-Join中，比如一个拥有4个线程的ForkJoinPool线程池，有一个任务队列，一个大的任务切分出的子任务会提交到线程池的任务队列中，4个线程从任务队列中获取任务执行，哪个线程执行的任务快，哪个线程执行的任务就多，只有队列中没有任务线程才是空闲的，这就是工作窃取。

可以通过下图更好的理解这种“分而治之”的思想：
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/3b351bfb0333-202408172156003.webp)
### [约束与限制](#约束与限制)

1.
parallelStream()中foreach()操作必须保证是线程安全的；
 很多人在用惯了流式处理之后，很多for循环都会直接使用流式foreach()，实际上这样不一定是合理的，如果只是简单的for循环，确实没有必要使用流式处理，因为流式底层封装了很多流式处理的复杂逻辑，从性能上来讲不占优。

1.
parallelStream()中foreach()不要直接使用默认的线程池；

1.
parallelStream()使用的时候尽量避免耗时操作；

### [注意](#注意)

**parallelStream和整个java进程共用ForkJoinPool**：如果直接使用parallelStream().foreach会默认使用全局的ForkJoinPool，而这样就会导致当前程序很多地方共用同一个线程池，包括gc相关操作在内，所以一旦任务队列中满了之后，就会出现阻塞的情况，导致整个程序的只要当前使用ForkJoinPool的地方都会出现问题。

**parallelStream使用后ThreadLocal数据为空**：parallelStream创建的并行流在真正执行时是由ForkJoin框架创建多个线程并行执行，由于ThreadLocal本身不具有可继承性，新生成的线程自然无法获取父线程中的ThreadLocal数据。

## [流的运行流程](#流的运行流程)

下面是一段比较简单常见的stream操作代码，经过映射与过滤操作后，最后得到的endList=["vb"]，下文讲解都会以此代码为例。

一段Stream代码的运行包括以下三部分：

1. 搭建流水线，定义各阶段功能。即创建stream

1. 从终结点反向索引，生成操作实例Sink。

1. 数据源送入流水线，经过各阶段处理后，生成结果。

### [类图介绍](#类图介绍)
![Stream类图](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/f90a21c32fe3-202408011614687.jpeg)Stream类图
Stream是一个接口，它**定义了对Stream的操作**，它继承自BaseStream，BaseStream是最顶端的接口类，定义了流的基本接口方法，最主要的方法为 spliterator、isParallel。

Stream主要可分为中间操作与终结操作，中间操作对流进行转化，定义了 `映射(map)`、`过滤(filter)`、`排序(sorted)`等行为。终结操作启动流水线，获取结果数据(collect)。

AbstractPipline是一个抽象类，定义了**流水线节点的常用属性**：

- sourceStage：指向流水线首节点

- previousStage ：指向本节点上层节点

- nextStage ：指向本节点下层节点

- depth：代表本节点处于流水线第几层（从0开始计数）

- sourceSpliterator：指向数据源

ReferencePipline 实现Stream接口，继承AbstractPipline类，它**主要对Stream中的各个操作进行实现**。此外，它还定义了`Head`、`StatelessOp`、`StatefulOp`三个内部类。

- Head为流水线首节点，在集合转为流后，生成Head节点。

- StatelessOp为无状态操作：无状态操作只对当前元素进行作用，比如filter操作只需判断“v”元素符不符合“startWith("v")”这个要求，无需在对“v”进行判断时关注数据源其他元素（“s”，“e”，“n”）的状态

- StatefulOp为有状态操作：有状态操作需要关注数据源中其他元素的状态，比如sorted操作要保留数据源其他元素，然后进行排序，生成新流。

Sink 接口定义了 Stream 之间的操作行为，包含 `begin()`、`end()`、`cancellationRequested()`、`accpt()`四个方法。ReferencePipeline最终会将整个 Stream 流操作组装成一个调用链，而这条调用链上的各个 Stream 操作的上下关系就是通过 Sink 接口协议来定义实现的。

### [搭建流水线](#搭建流水线)

首先需要区分一个概念，Stream(流)并不是一个容器，不存储数据，它更像是一个个具有不同功能的流水线节点，可相互串联，容许数据源挨个通过，最后随着终结操作生成结果。Stream流水线搭建包括三个阶段：

1. 创建一个流，如通过stream()产生Head，Head就是初始流，数据存储在Spliterator。

1. 将初始流转换成其他流的中间操作，可能包含多个步骤，比如上面map与filter操作。

1. 终止操作，用于产生结果，终结操作后，流也就走到了终点。

#### [定义输入源HEAD](#定义输入源head)

只有实现了Collection接口的类才能创建流，所以Map并不能创建流，List与Set这种单列集合才可创建流。上述代码使用stream()方法创建流，也可使用Stream.of()创建任何数量引元的流，或是 Array.stream(array,from,to) 从数组中from到to的位置创建输入源。

#### [stream()运行结果](#stream-运行结果)

示例代码中使用stream()方法生成流，看看生成的流中有哪些内容：
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/dcd81292eba2-202407302230750.png)
从运行结果来看，stream(）方法生成了ReferencPipeline$Head类，ReferencPipeline是Stream的实现类，Head是ReferencePipline的内部类。其中:

- sourceStage指向实例本身

- depth=0代表Head是流水线首层

- sourceSpliterator 指向底层存储数据的集合，其中list即初始数据源。

#### [stream()源码分析](#stream-源码分析)

spliterator()将 “调用stream()方法的对象本身startlist” 传入构造函数，生成Spliterator类，传入StreamSupport.stream()方法。

StreamSupport.stream()返回了ReferencPipeline$Head类。

点击构造函数，一路追溯至 AbstractPipline 中，可看到使用sourceSpliterator指向数据源，sourceStage为Head实例本身，深度depth=0。

### [定义流水线中间节点](#定义流水线中间节点)

#### [Map](#map)

##### [map()运行结果](#map-运行结果)

对数据进行映射，对每个元素后接"b"。
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/11ce94ff993f-202407302240793.png)
此时：（由于是多次dubug，因此对象的地址值与上面不一致，但不影响案例分析，下同）

- sourceStage与previousStage 皆指向Head节点

- depth变为1，表示为流水线第二节点

- 由于代码后续没接其他操作，所以nextStage为null

- mapper代表函数式接口，指向lambda代码块，即 “r-&gt;r+"b"” 这个操作。

##### [map()源码分析](#map-源码分析)

可以看到，map()方法是在ReferencePipline中被实现的，返回了一个无状态操作StatelessOp，定义opWrapSink方法，运行时会将lambda代码块的内容替换apply方法，对数据元素u进行操作。opWrapSink方法将返回Sink对象，其用处将在下文讲解。downstream为opWrapSink的入参sink。

#### [Filter](#filter)

##### [filter()运行结果](#filter-运行结果)

filter对元素进行过滤，只留存以“v”开头的数据元素。
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/ef268344e0b7-202407302248619.png)
Filter阶段：

- depth再次+1，变为2

- sourceStage指向Head

- predict指向lamda表达式的代码块：“r-&gt;r.startsWith("a")”

- previousStage指向前序Map节点

- Map节点中的nextStage 开始指向Filter，形成了双向链表。

##### [filter()源码分析](#filter-源码分析)

filter()也是在ReferencePipline中被实现，返回一个无状态操作StatelessOp，实现opWrapSink方法，也是返回一个Sink，其中accept方法中的`predicate.test="r-&gt;r.startsWith("v")"`，用以过滤符合要求的元素。downstream等于opWrapSink入参Sink。

new StatelessOp 最终会调用父类 AbstractPipeline 的构造函数，这个构造函数将前后的 Stage 联系起来，生成一个 Stage 双向链表：

### [定义终结操作](#定义终结操作)

#### [collect()运行结果](#collect-运行结果)
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/668f4bf28b26-202407302257007.png)
经过终结操作后，生成最终结果[“vb”]。

#### [collect()源码分析](#collect-源码分析)

同样的，collect终结操作也在ReferencePipline中被实现。由于不是并行操作，只要关注evaluate()方法即可，而evaluate()方法中有一个makeRef()方法

makeRef()方法中也有个类似opWrapSink一样返回Sink的方法，不过没有以其他Sink为输入，而是直接new一个ReducingSInk对象。

至此，可以根据源码绘出下图，使用双向链表连接各个流水线节点，并将每个阶段的lambda代码块存入Sink类中。数据源使用sourceSpliterator引用。
![流水线搭建](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/a5eb45895176-202407302303235.webp)流水线搭建
### [反向回溯生成操作实例](#反向回溯生成操作实例)

Stream是“惰性执行”的，在一层一层搭建中间节点时，并未有任何结果产生，而在终结操作collect之后，才会生成最终结果endList，接下来具体探究一下collect()方法中的evaluate方法。

这里调用了Collect中定义的makeSink()方法，输入终结节点生成的sink与数据源spliterator。

先来看wrapSink方法，在这个方法里，中间节点的opWrapSink方法利用previousStage反向索引，后一个节点的sink送入前序节点的opWrapSink方法中做入参，也就是downstream，生成当前sink，再索引向前，生成套娃Sink。

最后索引到 depth=1 的Map节点，生成的结果Sink包含了depth2节点Filter与终结节点Collect的Sink。
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/096605e6745c-202407312105124.png)
红色框图表示Map节点的Sink，包含当前Stream与downstream（Filter节点Sink），黄色代表Filter节点Sink，downstream指向Collect节点。

Sink被反向套娃实例化，一步步索引到Map节点。
![反向索引生成Sink](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/f699c0273a91-202407302309214.webp)反向索引生成Sink
#### [启动流水线](#启动流水线)

一切准备就绪后，就是把数据源冲入流水线，在wrapSink方法套娃生成Sink之后，copyInto方法将数据源送入了流水线。

先是调用Sink中已定义好的begin方法，做些前序处理，Sink中的begin方法会不断调用下一个Sink的begin方法。

随后对数据源中各个元素进行遍历，调用Sink中定义好的accept方法处理数据元素。accept执行的就是咱在每一节点定义的lambda代码块。
![](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/08fb960f5c87-202407302310286.webp)
随后调用end方法做后序扫尾工作。
![数据源冲入操作实例，生成最终结果](/imported/markdown/2025-05-17-markdown-4ec44d72-stream流-高效数据处理的秘密武器/images/ca1a5a8ade0e-202407302310306.webp)数据源冲入操作实例，生成最终结果
一个简单Stream整体关联图如上所示，最后调用get()方法生成结果。
