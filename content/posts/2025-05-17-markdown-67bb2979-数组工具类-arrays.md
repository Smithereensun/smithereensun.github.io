{

  "title": "数组工具类 - Arrays",
  "has_date": true,
  "description": "数组专用工具类指的是 类，基本上常见的数组操作，这个类都提供了静态方法可供直接调用。毕竟数组本身想完成这些操作还是挺麻烦的，有了这层封装，就方便多了。 方法一览 方法名简要描述asList()返回由指定数组支持的固定大小的列表。sort()将数组排序（升序）parallelSort()将指定的数组按",
  "tags": [
    "工具库"
  ],
  "source": "local-markdown-library",
  "source_path": "tool-library/jdk-tools/arrays - 数组工具类 - Arrays.md",
  "date": "2025-05-17"

}

数组专用工具类指的是 `java.util.Arrays` 类，基本上常见的数组操作，这个类都提供了静态方法可供直接调用。毕竟数组本身想完成这些操作还是挺麻烦的，有了这层封装，就方便多了。

## [方法一览](#方法一览)
方法名简要描述asList()返回由指定数组支持的固定大小的列表。sort()将数组排序（升序）parallelSort()将指定的数组按升序排序binarySearch()使用二分搜索法快速查找指定的值（前提是数组必须是有序的）compare()按字典顺序比较两个数组compareUnsigned()按字典顺序比较两个数组，将数字元素处理为无符号copyOf()填充复制数组copyOfRange()将数组的指定范围复制到新数组fill()将指定元素填充给数组每一个元素equals()比较两个数组deepEquals()比较两个数组深度toString()将数组转换为字符串deepToString()将一个多维数组转换为字符串mismatch()查找并返回两个数组之间第一个不匹配的索引，如果未找到则返回-1parallelPrefix()使用提供的函数对数组元素进行操作parallelSetAll()使用提供的生成器函数并行设置指定数组的所有元素以计算每个元素setAll()使用提供的生成器函数设置指定数组的所有元素以计算每个元素
## [asList()](#aslist)

- **功能**：返回由指定数组支持的固定大小的列表

- **参数**：asList​(T… a)

- **返回值**：一个列表

需要注意的是，add方法和remove会报错。

这是因为asList() 返回的是Arrays类的内部类：
![](/imported/markdown/2025-05-17-markdown-67bb2979-数组工具类-arrays/images/70cea8c7e3ef-202408031904151.png)
这个内部类也继承了 java.util.AbstractList 类，重写了很多方法，比如contains方法、set方法，但是却没有重写add方法，最终是调用了父类的add(int, E)方法，所以在调用add方法时才会抛出java.lang.UnsupportedOperationException异常。

关于这一点，在《阿里巴巴Java开发手册》中，也有提及：使用工具类 Arrays.asList()把数组转换成集合时，不能使用其修改集合相关的方法，它的 add/remove/clear 方法会抛出 UnsupportedOperationException 异常。
![](/imported/markdown/2025-05-17-markdown-67bb2979-数组工具类-arrays/images/69d715af9e1a-202408031905600.gif)
所以大家在使用Arrays.asList时还是要注意下，避免踩坑。

## [toString() 和 deepToString()](#tostring-和-deeptostring)

- **功能**：将数组转换为字符串

- **参数**：待转化数组

- **返回值**：转化后的字符串

代码示例：

方法源码：

## [sort() 和 parallelSort()](#sort-和-parallelsort)

- 功能：都是将数组排序（默认升序，支持lambda，泛型），默认的排序算法是 Dual-Pivot Quicksort

- 参数：
`sort(Object[] a[, int fromIndex, int toIndex]) 或者 sort(T[] a[, int fromIndex, int toIndex,] Comparator&lt;? super T&gt; c)`
`parallelSort(Object[] a[, int fromIndex, int toIndex]) 或者 parallelSort(T[] a[, int fromIndex, int toIndex,] Comparator&lt;? super T&gt; c)`

代码示例：

### [sort源码](#sort源码)

从源码上看整体排序并不是调用的部分排序的方法，Arrays.sort(int[] a)和Arrays.sort(int[] a, int fromIndex, int toIndex)只是个入口，它们都会去调用DualPivotQuicksort.sort方法，都会传入排序部分的起终点，不过整体排序传入的起终点为0和length - 1。

从数组元素的类型来看，可以将Arrays.sort分为对基本数据类型的排序和对泛型及Object数组的排序。进入源码我们可以发现：对于基本数据类型数组的排序，Arrays.sort都将调用DualPivotQuicksort.sort方法，而泛型及Object数组的排序实现则与之不同。

#### [对基本数据类型数组的排序](#对基本数据类型数组的排序)

对于基本数据类型数组的排序，Arrays.sort都将调用`DualPivotQuicksort.sort`方法，来看看这个方法的部分源码（感兴趣可自行阅读，或可直接往后看结论）：
![若数组长度&lt;286，调用sort(a, left, right, true)](/imported/markdown/2025-05-17-markdown-67bb2979-数组工具类-arrays/images/a9947e51e97e-202408041128241.png)若数组长度&lt;286，调用sort(a, left, right, true)![若数组长度&lt;286，调用sort(a, left, right, true)](/imported/markdown/2025-05-17-markdown-67bb2979-数组工具类-arrays/images/565e3b4148d5-202408041129372.png)若数组长度&lt;286，调用sort(a, left, right, true)
也就是说，若数组长度小于286，则会再次判断：

- 若数组长度较小，，长度&lt;47，则使用插入排序

- 若数组长度&gt;=47，将使用快速排序

这是由排序算法的特性决定的，因为在数组长度很小时，在大量测试的平均结果下，插入排序将快于快排。

那么当数组长度&gt;=286时呢？重新回到DualPivotQuicksort.sort方法，发现会对数组的结构性进行判断：

- 若数组基本有序，则将使用归并排序

- 若数组的元素排列较为混乱，则调用sort(a, left, right, true)方法，由于数组长度&gt;=286，也&gt;=47，因此会进行快速排序。

为什么这样设计也是由排序算法的特性决定的，虽然快排和归并排序的（平均）时间复杂度是一样的，但对于基本有序的数组，归并排序的速度会比快速排序快，而对于近乎无序的数组，归并排序速度会比快速排序慢。

**总结一下**，对于基本数据类型数组的排序，排序算法的选择和数组长度的关系如下：
数组长度所使用的排序算法length &lt; 47插入排序47 &lt;= length &lt; 286快速排序length &gt;= 286 且数组基本有序归并排序length &gt;= 286 且数组基本无序快速排序
#### [对Object数组和泛型数组的排序](#对object数组和泛型数组的排序)

对于泛型数组的排序，可以传入实现了Comparator接口的类的对象，也可以不传，实际上传和不传都是调用的同一个方法，只不过不传入时，对应的参数为null。我们来看看Arrays.sort对Object数组和泛型数组的排序源码：

JDK8会默认选择TimSort作为排序算法。TimSort算法是一种起源于归并排序和插入排序的混合排序算法，原则上TimSort是归并排序，但小片段的合并中用了插入排序。对于泛型数组的排序，若不传入实现了Comparator接口的类的对象，将调用sort(Object[] a)方法

接下来看调用的ComparableTimSort.sort方法的部分源码：
![](/imported/markdown/2025-05-17-markdown-67bb2979-数组工具类-arrays/images/1ef8c33b6ef8-202408041143800.png)
ComparableTimSort.sort 会调用countRunAndMakeAscending方法和binarySort方法，而这两个方法都有将数组元素强转为Comparable接口类型的操作，因为它需要调用Comparable接口中的compareTo方法进行元素间的比较，Comparable接口中只定义了一个方法，那就是compareTo。

因此，若调用Arrays.sort(Object[] o)对Object数组进行排序，但数组元素类型表示的类并没有实现Comparable接口，那么Java将认为该类的对象是无法比较的，那么就会抛出ClassCastException异常.

#### [小结](#小结)

JDK中的Arrays.sort实际上采用的是设计模式中的模板模式，将排序算法的步骤封装了起来，而将如何比较两个数组元素交给了程序员来实现。
 当排序自定义类时，可以让这个类实现Comparable接口，并重写其compareTo方法。也可以创建一个实现了Comparator接口的类，重写其compare方法。具体如何比较两个数组元素的逻辑就写在了需要重写的这两个方法中。

比较两个数组元素o1与o2的大小无非三种结果：o1&gt;o2，o1=o2，o1&lt;o2。因此compareTo方法和compare方法的返回值有三种情况，这是针对默认升序设计的：

- 当o1 &gt; o2，返回一个正整数；

- 若o1 = o2，返回0；

- 若o1 &lt; o2，返回一个负整数。

对于实现了Comparable接口的类，o1 即为this，表示当前类对象。若在重写方法的逻辑中按上述对应关系去返回对应值(即return o1 -o2)，则调用Arrays.sort将会得到升序结果；若把对应关系写反((即return o2 -o1))，则会得到降序结果。

### [parallelSort()](#parallelsort)

parallelSort() 在功能上有所不同。与 sort() 使用单个线程对数据进行顺序排序不同，它使用 并行排序-合并排序 算法。它将数组分成子数组，这些子数组本身先进行排序然后合并。为了执行并行任务，它使用 ForkJoin 池。
![](/imported/markdown/2025-05-17-markdown-67bb2979-数组工具类-arrays/images/dd9d38717d21-202408041156839.jpeg)
parallelSort源码：如果数组大小小于或等于 8192，或者处理器只有一个核心，则它将使用顺序的 Dual-Pivot Quicksort 算法。否则，它使用并行排序。

### [小结](#小结-1)

当要排序的数据集很大时，parallelSort() 可能是更好的选择。但是，在数组较小的情况下，最好使用 sort()，因为它可以提供更好的性能。

## [binarySearch()](#binarysearch)

- **功能**：使用二分搜索法快速查找指定的值（前提是数组必须是有序的，支持lambda表达式，泛型）

- **参数**：binarySearch(Object[] a[, int fromIndex, int toIndex], Object key)

- **返回值**：有则返回对应下标，无则返回负值

代码示例：

源码：

## [创建数组](#创建数组)

使用 Arrays 类创建数组可以通过以下三个方法：

- copyOf，复制指定的数组，截取或用 null 填充

- copyOfRange，复制指定范围内的数组到一个新的数组

- fill，对数组进行填充

### [copyOf 和copyOfRange](#copyof-和copyofrange)

- **功能**：复制填充数组

- **参数**：
`copyOf(int[] original, int newLength)`
`copyOf(T[] original, int newLength)`
`copyOfRange(int[] original, int from, int to）`
`copyOfRange(T[] original, int from, int to)`
`copyOfRange(U[] original, int from, int to, class &lt;? extends T[]&gt; newType)`

- **返回值**：复制填充后的数组

- **区别**：
 copyOf()是从原数组0位置开始拷贝指定长度到新数组；
 copyOfRange()是从原数组中指定范围拷贝到新数组，如果指定长度或者范围超出原数组范围，则超出部分会补上此数据类型的默认值，如String类型会补null，int型会补0

代码示例

### [fill](#fill)

- **功能**：将指定元素填充给数组每一个元素

- **参数**：fill​(int[] a, 【int fromIndex, int toIndex】, int val)

- **返回值**：无

代码示例：

源码如下：

### [setAll 和 parallelSetAll()](#setall-和-parallelsetall)

Java 8 新增了 `setAll()` 方法，它提供了一个函数式编程的入口，可以对数组的元素进行填充：

可以用来为新数组填充基于原来数组的新元素。

parallelSetAll() 就是 setAll 的并行版本，都是通过索引值去改变元素，改编后的值与索引有关

## [equals() 和 deepEquals()](#equals-和-deepequals)

Arrays 类的 `equals()` 方法用来判断两个数组是否相等，来看下面这个例子：

区别在于：

- equals默认从头比较到尾，也可以指定范围，但是deepEquals不能指定范围

- deepEquals可以比较一维数组，也支持比较多维数组，而equals不能

- 当deepEquals比较一维数组时，不支持比较基本类型数组，如int[]，但支持int[][]

`equals()` 方法的源码：

这里数组是一个对象的问题 可以看这篇文章 数组是不是对象，int[]数组是Object，但不是Object[]，deepEquals支持的是Object[]，int[][]则属于Object[]

`deepEquals()` 方法的源码：

## [数组转流 stream()](#数组转流-stream)

Arrays 类的 `stream()` 方法可以将数组转换成流：

还可以为 `stream()` 方法指定起始下标和结束下标：

如果下标的范围有误的时候，比如说从 2 到 1 结束，则程序会抛出 ArrayIndexOutOfBoundsException 异常：

## [parallelPrefix](#parallelprefix)

parallelPrefix 通过遍历数组中的元素，将当前下标位置上的元素与它之前下标的元素进行操作，然后将操作后的结果覆盖当前下标位置上的元素。

上面代码中有一个 Lambda 表达式（`(left, right) -&gt; left + right`），是什么意思呢？上面这段代码等同于：

来看一下输出结果就明白了：

也就是说， Lambda 表达式执行了三次：

- 第一次是 1 和 2 相加，结果是 3，替换下标为 1 的位置

- 第二次是 3 和 3 相加，结果是 6，也就是第一次的结果和下标为 2 的元素相加的结果

- 第三次是 6 和 4 相加，结果是 10，也就是第二次的结果和下标为 3 的元素相加的结果
