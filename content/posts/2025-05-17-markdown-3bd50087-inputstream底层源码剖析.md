{

  "title": "InputStream底层源码剖析",
  "has_date": true,
  "description": "InputStream 类实现关系 InputStream 抽象类 InputStream 类重要方法设计如下： 底层源码实现 梳理部分InputStream及其实现类的源码分析。 InputStream InputStream抽象类源码如下： 总结下JDK9的更新点: 类 java.io.Inpu",
  "tags": [
    "Java"
  ],
  "source": "local-markdown-library",
  "source_path": "java/io/01-io-inputstream-sourcecode - InputStream底层源码剖析.md",
  "date": "2025-05-17"

}

## [InputStream 类实现关系](#inputstream-类实现关系)
![](/imported/markdown/2025-05-17-markdown-3bd50087-inputstream底层源码剖析/images/a4bf1a6c4751-202404250745983.jpg)
## [InputStream 抽象类](#inputstream-抽象类)

InputStream 类重要方法设计如下：

## [底层源码实现](#底层源码实现)

梳理部分InputStream及其实现类的源码分析。

### [InputStream](#inputstream)

InputStream抽象类源码如下：

总结下JDK9的更新点:

类 java.io.InputStream 中增加了新的方法来读取和复制 InputStream 中包含的数据。

- readAllBytes

- readNBytes

- transferTo

read(byte[], int, int) **和 readNBytes(byte[], int, int)看似是实现的相同功能，为何会设计readNBytes方法呢**

1. read(byte[], int, int)是尝试读到最多len个bytes，但是**读取到的内容长度可能是小于len**

1. readNBytes(byte[], int, int) 会一直（while循环）查找直到stream尾为止

举个例子：如果文本内容是12345&lt;end&gt;, read(s,0,10)是允许返回123的, 而readNbytes(s,0,10)会一直（while循环）查找直到stream尾为止，并返回12345

#### [read方法详解](#read方法详解)

在Java8中，InputStream被定义为一个抽象类，相应的，该类下的read()方法也是一个抽象方法，这也就意味着必须有一个类继承InputStream并且实现这个read方法。
![](/imported/markdown/2025-05-17-markdown-3bd50087-inputstream底层源码剖析/images/23dedee06ee7-202406171812353.png)
但是在这三个方法中，只有参数列表为空的read方法定义为抽象方法，这也就意味着在直接继承自InputStream的所有子类中，必须重写这个方法.

1. read()
 首先我们来看这个没有参数的read方法，从（来源）输入流中（读取的内容）读取数据的下一个字节到（去处）java程序内部中，返回值为0到255的int类型的值，返回值为字符的ASCII值（如a就返回97，n就返回110）。如果没有可用的字节，因为已经到达流的末尾，返回值 -1，运行一次只读一个字节，所以经常与while((len = inputstream.read()) != -1)一起使用

1. read(byte [] b )
 从（来源）输入流中（读取的内容）读取的一定数量字节数，并将它们存储到（去处）缓冲区数组b中，返回值为实际读取的字节数，运行一次读取一定的数量的字节数。java会尽可能的读取b个字节，但也有可能读取少于b的字节数。至少读取一个字节，第一个字节存储读入元素b[0]，下一个b[1]，等等。读取的字节数是最多等于b的长度。如果没有可用的字节，因为已经到达流的末尾，返回值-1，如果b.length==0，则返回0

1. read( byte [] b , int off , int len)
 读取 len字节的数据从输入流到一个字节数组。试图读取多达 len字节，但可能读取到少于len字节。返回实际读取的字节数为整数。 第一个字节存储读入元素b[off]，下一个b[off+1]，等等。读取的字节数是最多等于len。k被读取的字节数,这些字节将存储在元素通过b[off+k-1]b[off]，离开元素通过b[off+len-1] b[off+k]未受影响。read(byte[]b)就是相当于read(byte [] b , 0 , b.length)，所以两者差不多，性质一样。

这里有个问题，read()无参方法读取一个字节，为什么返回的是一个int类型，而不是一个byte类型?
 因为字节输入流可以操作任意类型的文件，比如图片音频等，这些文件底层都是以二进制形式的存储的，一个字节是8个二进制，也就是说我们实际read完后得到的是这样的东西(11111110,00001010)，如果每次读取都返回byte，有可能在读到中间的时候遇到111111111(文件的底层按补码来存储的)，那么这11111111是byte类型的-1，我们的程序是遇到-1就会停止不读了，后面的数据就读不到了，所以在读取的时候用int类型接收，如果11111111会在其前面补上24个0凑足4个字节，那么byte类型的-1就变成int类型的255了，这样可以保证整个数据读完，而结束标记的-1就是int类型

#### [JDK11的空对象模式](#jdk11的空对象模式)

JDK11为什么会增加nullInputStream方法的设计？即空对象模式

举个例子：

然后便**可以始终可以这么调用，而不用再判断空了**

### [FilterInputStream](#filterinputstream)

FilterInputStream 源码如下

### [ByteArrayInputStream](#bytearrayinputstream)

ByteArrayInputStream属于内存IO的范畴，就是把内存中的数据又读取到内存中。

ByteArrayInputStream源码如下

### [BufferedInputStream](#bufferedinputstream)

BufferedInputStream缓冲流，其实就是多给InputStream了一层包装，InputStream在读取数据时可以设置缓冲区大小，而BufferedInputStream就是将缓冲区大小默认设置为8192，即8MB

BufferedInputStream源码如下
