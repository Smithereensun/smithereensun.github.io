{

  "title": "基础工具类 - Strings&Ints",
  "has_date": true,
  "description": "String相关工具 Strings Guava 提供了一系列用于字符串处理的工具： 对字符串为null或空的处理 nullToEmpty(@Nullable String string)：如果非空，则返回给定的字符串；否则返回空字符串 isNullOrEmpty(@Nullable String ",
  "tags": [
    "工具库"
  ],
  "source": "local-markdown-library",
  "source_path": "tool-library/guava/guava-string-ints - 基础工具类 - Strings&Ints.md",
  "date": "2025-05-17"

}

## [String相关工具](#string相关工具)

### [Strings](#strings)

Guava 提供了一系列用于字符串处理的工具：

#### [对字符串为null或空的处理](#对字符串为null或空的处理)

1.
nullToEmpty(@Nullable String string)：如果非空，则返回给定的字符串；否则返回空字符串

1.
.isNullOrEmpty(@Nullable String string)：如果字符串为空或长度为0返回true，否则返回false

1.
emptyToNull(@Nullable String string)：如果非空，则返回给定的字符串；否则返回null

#### [生成指定字符串的字符串副本](#生成指定字符串的字符串副本)

1.
padStart(String string, int minLength, char padChar)：根据传入的minLength进行补充，如果minLength小于原来字符串的长度，则直接返回原来字符串，否则在字符串开头添加`string.length() - minLength`个padChar字符

1.
padEnd(String string, int minLength, char padChar)：根据传入的minLength进行补充，如果minLength小于原来字符串的长度，则直接返回原来字符串，否则在字符串结尾添加 `string.length() - minLength` 个padChar字符

1.
repeat(String string, int count)：返回count个 string字符串拼接成的字符串

#### [查找两个字符串的公共前缀或后缀](#查找两个字符串的公共前缀或后缀)

在看commonPrefix和commonSuffix 这两个方法之前需要先看下validSurrogatePairAt方法

这个方法的作用是 判断最后两个字符是不是合法的“Java 平台增补字符

- Character.isHighSurrogate：确定给定char值是否为Unicode高位代理。这个值并不代表字符本身，而是在UTF-16编码的补充的字符的表示被使用。

- Character.isLowSurrogate：确定给定char值是否为一个Unicode低代理项代码单元（也称为尾部代理项代码单元）。这些值并不代表本身的字符，但用于表示增补字符的UTF-16编码。

简单的说就是Java 语言内部的字符信息是使用 UTF-16 编码。因为char 这个类型是 16 bit 的。它可以有65536种取值，即65536个编号，每个编号可以代表1种字符。而在Unicode字符集中，有一些字符的编码超出了16 bit的范围，也就是超过了`char`类型能够直接表示的范围，65536 就不够用。

为了能够在Java中表示这些字符，Unicode引入了一种叫做“代理对”（Surrogate Pair）的机制。从这65536个编号里，拿出2048个，规定它们是「Surrogates」，让它们两个为一组，来代表编号大于65536的那些字符。 更具体地，编号为 D800 至 DBFF 的规定为「High Surrogates」，共1024个。编号为 DC00至 DFFF 的规定为「Low Surrogates」，也是1024个。它们两两组合出现，就又可以多表示1048576种字符。

如果丢失一个高位代理Surrogates或者低位代理Surrogates，就会出现乱码。这就是为什么emoji会出现乱码了。例如输入了一个emoji:😆，假如可以写成这样：\uD83D\uDC34

String s = '\uD83D' + '\uDC34' + "";

那么在按字节截取s的时候，就要考虑这个字符是不是高位代理Surrogates或者低位代理Surrogates，避免出现半个字符。

1.
commonPrefix(CharSequence a, CharSequece b)：返回a和b两个字符串的公共前缀

1.
commonSuffix(CharSequence a, CharSequence b)：返回字符串a和字符串b的公共后缀

### [Joiner](#joiner)

将字符串数组按指定分隔符连接起来，或字符串串按指定索引开始使用指定分隔符连接起来，创建的**都是不可变实例，所以是线程安全的**。

底层实际是在用StringBuilder进行拼接操作。

#### [使用案例](#使用案例)

#### [静态创建Joiner](#静态创建joiner)

这两个方法一个传入字符串，一个传入字符，然后直接分别使用两个构造器构造

#### [join()方法](#join-方法)

对于4个join方法实际可以分为两类，一类是join实现类，另一类是join解析参数类

1. 解析参数类：

第3个实现方法需要 iterable方法对数组进行融合，所以看一下 iterable的实现方式：

1. join实现类

#### [useForNull方法](#usefornull方法)

将传入的字符串代替集合中的null输出

使用 useForNull方法后由于重写了useForNull和skipNulls方法，并且在两个方法中都抛出了异常。所以不能再次调用这两个方法。

**注意**：空字符串"" 无法命中这个方法，从源码中也可以看出来

#### [skipNulls方法](#skipnulls方法)

自动跳过null元素进行拼接

**注意**：空字符串"" 无法命中这个方法，从源码中也可以看出来

#### [对Map解析的函数和类](#对map解析的函数和类)

可以看到这个函数返回的是Joiner中的一个内部类，这个类里的大多方法都是在处理Map连接的函数

MapJoiner中的join方法实际上是对Map的entrySet即可以的集合进行拼接。整体思路与上面一致

### [CharMatchers](#charmatchers)

字符序列匹配和处理的工具，内置了大量常用的匹配器。使用上通常分两步：

- 确定匹配的字符和模式

- 用匹配的字符做处理

#### [实现类](#实现类)
实现类类作用ANY匹配任何字符ASCII匹配是否是ASCII字符BREAKING_WHITESPACE匹配所有可换行的空白字符(不包括非换行空白字符,例如"\u00a0")JAVA_ISO_CONTROL匹配ISO控制字符, 使用 Charater.isISOControl() 实现NONE不匹配所有字符WHITESPACE匹配所有空白字符
常用方法可分为4类：

#### [得到匹配指定规则的Matcher](#得到匹配指定规则的matcher)

#### [判断字符串是否匹配](#判断字符串是否匹配)

#### [获取字符串与Matcher匹配的位置信息](#获取字符串与matcher匹配的位置信息)

#### [对字符串进行怎样匹配处理](#对字符串进行怎样匹配处理)

### [Splitter](#splitter)

字符串分割工具，**创建的也是不可变实例，所以是线程安全的**。

底层用的是 String的subString方法

#### [使用案例](#使用案例-1)

#### [两个内部类](#两个内部类)

在通读整片源码前先来了解其中的两个内部类，这两个内部类是真正去分解字符串的：

其中一个是 处理字符、字符串、正则的接口，此接口的定义实质为 策略模式

这个接口中只有一个方法，返回的是一个Iterator迭代器，这里可以先联想到最终返回的集合的迭代器会与它有关系

这里实现了一个惰性迭代器：惰性迭代器就是指 直到不得不计算的时候才会去将字符串分割，即在迭代的时候才去分割字符串，无论将分隔符还是被分割的字符串加载到Splitter类中，都不会去分割，只有在迭代的时候才会**真正的去分割**。

这是一个实现AbstractIterator的一个抽象类，实现了 computeNext方法（此方法可以在看集合源码的时候也多注意一下），这个方法实际上是规定了此迭代器的一个迭代规则。所以Splitter类为他分割完的结果集也写了一个迭代器并规定了自己的迭代规则。从这个迭代器的实现上，在结合Strategy 类便可以将整个字符串分割的过程给串起来了。

除了这两个，还有一个内部类是 MapSplitter，是用于处理Map，对Map进行分割的

#### [变量](#变量)

#### [静态创建Splitter](#静态创建splitter)

两个构造函数都是私有构造器，所以不能直接使用这两个构造器去创建Splitter，想要创建Splitter只能使用静态方法。

静态创建Splitter函数有四种：

1.
接收**字符**的构造器

1.
接收**字符串**的构造器

1.
接收**正则表达式**的构造器

@GwtIncompatible用于指示某个类、方法或字段不兼容或不应被用于Google Web Toolkit (GWT)。GWT是一个开发工具，允许开发者编写Java代码，然后将这些代码编译成高效的JavaScript代码，以便在浏览器中运行。这个工具使得Java开发者可以编写前端代码，而不需要直接使用JavaScript。

1.
按指定长度分割的构造器

#### [进行分割的函数 （split、splittingIterator）](#进行分割的函数-split、splittingiterator)

1.
返回值是 Iterable 的函数：

这里调用了Strategy的iterator方法，这个方法在 静态创建Splitter中 里面有多种的实现方法，再结合内部类中的 SplittingIterator类重写的迭代方法，这里就形成了一个特殊的容器返回。也就是说，真正的拆分字符串动作是在迭代的时候进行的，即在这个函数中进行的。

1.
返回值是List对象的函数

与上面一样是先调用了Strategy的iterator方法。再遍历将结果集放在了ArrayList容器中，再返回不可变的List。

#### [其它功能性方法](#其它功能性方法)

1.
omitEmptyStrings方法：移去结果中的空字符串

这里就是将omitEmptyStrings标记位改为true，在computeNext方法中进行输出操作时将空结果略过

1.
trimResults方法

调用此方法可以将结果集中的每个字符串前缀和后缀都去除trimmer，他的实现也是在computeNext方法中进行的

1.
limit方法：达到指定数目后停止字符串划分

将传入的limit值赋值给变量

#### [MapSpliter](#mapspliter)

Spliter和MapSpliter跟Joiner以及MapJoiner功能正好相反。

## [通用/其它工具](#通用-其它工具)

### [Preconditions](#preconditions)

提供静态方法来检查方法或构造函数。如果方法失败则抛出 NullPointerException。

JDK 7 开始提供的 Objects 类也提供了一些类似的功能，具体可以参考 [JDK Doc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Objects.html)。

#### [对null的处理](#对null的处理)

根据三个方法的描述，reference是要进行判断的引用，接下来的信息是自定义异常打印信息

#### [对真假的处理](#对真假的处理)

对真假的判断实现有两种实现函数checkArgument()和checkState()

两个函数的实现大体一致，都是对传入的boolean类型参数进行判断

如果为false

- checkArgument方法会抛出IllegalArgumentException()

- checkState方法会抛出IllegalStateException()

#### [对数组下标是否符合的处理](#对数组下标是否符合的处理)

对数组下标合格的判断有三种方法checkElementIndex()、checkPositionIndex()、checkPositionIndexs()

### [Ints](#ints)

1.
compare(int a, int b)：比较两个指定的int值

1.
asList(int... backingArray)：返回由指定数组支持的固定大小的列表，类似Arrays.asList(Object[]).

由源码可以看到，如果传入的参数长度为0，那么就会创建一个Collections.emptyList()，如果参数长度不为0，那么就会创建一个Ints的内部类IntArrayAsList。

**特殊说明**：Ints的asList与JDK的Arrays.asLis的不同点：

- Arrays.asList(Object[])返回的是一个List&lt;数组&gt;，而Ints的asList返回的是List&lt;Integer&gt;。

- Ints的asList返回的是内部的一个不可变的List，没有重写add方法，因此执行add操作会抛异常。

![](/imported/markdown/2025-05-17-markdown-af240620-基础工具类-strings-ints/images/1579d52c8ae7-202407131416842.png)

1.
contains(int[] array, int target)：如果array中存在target返回true，反之返回false

### [字符常量/大小写转换](#字符常量-大小写转换)

1.
**Charsets**: 提供了6种标准的字符集常量引用，例如`Charsets.UTF_8`。JDK 7 以后建议使用内置的 `StandardCharsets`

1.
**CaseFormat**: 大小写转换的工具

**Format****Example**[LOWER_CAMEL](http://google.github.io/guava/releases/snapshot/api/docs/com/google/common/base/CaseFormat.html#LOWER_CAMEL)lowerCamel[LOWER_HYPHEN](http://google.github.io/guava/releases/snapshot/api/docs/com/google/common/base/CaseFormat.html#LOWER_HYPHEN)lower-hyphen[LOWER_UNDERSCORE](http://google.github.io/guava/releases/snapshot/api/docs/com/google/common/base/CaseFormat.html#LOWER_UNDERSCORE)lower_underscore[UPPER_CAMEL](http://google.github.io/guava/releases/snapshot/api/docs/com/google/common/base/CaseFormat.html#UPPER_CAMEL)UpperCamel[UPPER_UNDERSCORE](http://google.github.io/guava/releases/snapshot/api/docs/com/google/common/base/CaseFormat.html#UPPER_UNDERSCORE)UPPER_UNDERSCORE
