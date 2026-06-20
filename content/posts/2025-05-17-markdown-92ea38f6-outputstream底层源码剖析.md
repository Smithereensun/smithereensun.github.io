{

  "title": "OutputStream底层源码剖析",
  "has_date": true,
  "description": "OutputStream 类实现关系 OutputStream是输出字节流，具体的实现类层次结构如下： OutputStream 抽象类 OutputStream 类重要方法设计如下： 底层源码 梳理部分OutputStream及其实现类的源码分析。 OutputStream OutputStrea",
  "tags": [
    "Java"
  ],
  "source": "local-markdown-library",
  "source_path": "java/io/02-io-outputstream-sourcecode - OutputStream底层源码剖析.md",
  "date": "2025-05-17"

}

## [OutputStream 类实现关系](#outputstream-类实现关系)

OutputStream是输出字节流，具体的实现类层次结构如下：
![](/imported/markdown/2025-05-17-markdown-92ea38f6-outputstream底层源码剖析/images/81178787c6e2-202404250752991.jpg)
## [OutputStream 抽象类](#outputstream-抽象类)

OutputStream 类重要方法设计如下：

## [底层源码](#底层源码)

梳理部分OutputStream及其实现类的源码分析。

### [OutputStream](#outputstream)

OutputStream抽象类源码如下：

#### [JDK11的空对象模式](#jdk11的空对象模式)

举个例子：

然后便**可以始终可以这么调用，而不用再判断空了**

### [FilterOutputStream](#filteroutputstream)

FilterOutputStream 源码如下

对比下JDK8中，close方法是没有加锁处理的。这种情况下你可以看JDK8源码中，直接利用java7的try with resources方式，优雅的调用flush方法后对out进行关闭。

### [ByteArrayOutputStream](#bytearrayoutputstream)

ByteArrayOutputStream 源码如下

### [BufferedOutputStream](#bufferedoutputstream)

BufferedOutputStream 源码如下

BufferedOutputStream的flush和close方法的区别：

- flush()方法：用来刷新缓冲区，刷新后可以再次写出

- close()方法

  - 用来关闭流释放资源

  - 如果是带缓冲区的流对象的close()方法，不但会关闭流，close()方法还调用了flush()方法，也就是说，在关闭流之前会执行最后一次flush()
