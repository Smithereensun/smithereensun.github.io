{

  "title": "IO工具 - GuavaIO",
  "has_date": true,
  "description": "引言 Guava 使用术语 **流**来表示可关闭的，并且在底层资源中有位置状态的 I/O 数据流。字节流对应的工具类为 ByteSterams，字符流对应的工具类为 CharStreams。 Guava 中为了避免和流直接打交道，抽象出可读的 **源 source** 和可写的 **汇 sink*",
  "tags": [
    "工具库"
  ],
  "source": "local-markdown-library",
  "source_path": "tool-library/guava/guava-io - IO工具 - GuavaIO.md",
  "date": "2025-05-17"

}

## [引言](#引言)

Guava 使用术语 **流**来表示可关闭的，并且在底层资源中有位置状态的 I/O 数据流。字节流对应的工具类为 ByteSterams，字符流对应的工具类为 CharStreams。
 Guava 中为了避免和流直接打交道，抽象出可读的 **源 source** 和可写的 **汇 sink** 两个概念，指可以从中打开流的资源，比如 File、URL，同样也分别有字节和字符对应的源和汇，定义了一系列读写的方法。

Guava IO 极大简化了文件和流的操作。比如说，读写文件这种看似简单的操作，在Java原生代码中可能要写好几行，还不包括错误处理。Guava则可以用一两行搞定，简洁到让人惊叹。其次，它还提供了更丰富的功能，比如对不同字符集的处理，还有资源的高效管理。这些都是在开发过程中经常遇到的问题，Guava给了我们优雅的解决方案。

来看个简单的例子，比如说读取一个文本文件的内容。在Java原生代码中，可能得这么写：

但是用Guava，就可以变得超级简单：

看到区别了吧？Guava的代码不仅更短，而且可读性也强很多。而且，Guava还考虑了很多细节，比如字符集处理，在这里用的是`Charsets.UTF_8`，这在处理有不同编码的文件时特别有用。

## [文件操作简化](#文件操作简化)

在Java的世界里，文件操作是个老生常谈的话题。传统的Java I/O操作，虽然功能强大，但代码写起来往往既长又复杂，但是，有了Guava，这一切都变得轻松多了。

### [读取文件](#读取文件)

读取文件场景中，在Java原生方法里，可能需要创建`FileReader`，然后再包装成`BufferedReader`，最后一行一行地读。但在Guava中，只需要几行代码，就能搞定。

看这个例子：
![](/imported/markdown/2025-05-17-markdown-7ded55ab-io工具-guavaio/images/a8be5de53020-202407171502823.png)
在这段代码里，`Files.asCharSource`方法创建了一个字符源（CharSource），这样就可以直接读取文件中的内容了。再也不用担心`FileNotFoundException`和`IOException`这些让人头疼的异常了，Guava都处理好了一切。

### [写入文件](#写入文件)

在传统的Java I/O中，写文件也是一大堆代码，需要处理流的打开和关闭，还得小心处理异常。但在Guava中，这也变得超级简单：
![img](/imported/markdown/2025-05-17-markdown-7ded55ab-io工具-guavaio/images/2314e58c6a4c-202407171502063.png)img
在这里，`Files.asCharSink`创建了一个字符汇（CharSink），它能轻松写入数据到文件中。这些代码不仅简洁，而且易于理解和维护。

### [复制和移动文件](#复制和移动文件)

但Guava的魔法不止于此。想要复制或者移动文件？也是分分钟的事情。看看这个：

## [流处理与转换](#流处理与转换)

在Java中，流（Streams）是处理数据的核心，不论是文件I/O还是网络通信，流都扮演着至关重要的角色。但有时候，处理Java原生的InputStream和OutputStream会让人觉得有点小复杂。幸好，Guava在这方面提供了非常便捷的工具，让流处理变得既简单又高效。

### [简化的流读取](#简化的流读取)

在传统的Java I/O中，从InputStream读取数据通常需要创建一个buffer，然后一点点读取。但用Guava，整个过程就变得异常简单：

在这里，`CharStreams.toString`方法直接将整个InputStream转换为字符串。再也不需要手动创建buffer和循环读取了，一行代码就搞定。

### [流的转换和处理](#流的转换和处理)

有时候，需要对流中的数据进行某种形式的处理或转换。Guava在这方面也提供了很大的帮助。看看这个例子：

在这个例子中，`CharStreams.readLines`方法读取了所有行，并且通过`transform`方法对每一行进行了转换，这里是将其转换为大写。Guava的流式处理风格让这种转换变得非常优雅。

### [高效的流拷贝](#高效的流拷贝)

在Java中，从一个流拷贝数据到另一个流通常需要手动创建buffer，并循环进行读写。但在Guava中，这也变得简单多了：

在这个例子中，`ByteStreams.copy`方法就直接完成了从一个流到另一个流的数据拷贝。Guava把复杂的操作隐藏在了简洁的API背后，大大降低了编码的复杂性。

## [字符集与编码处理](#字符集与编码处理)

在Java世界里，字符集和编码经常会让人头疼，特别是当处理不同来源的数据时，比如从不同的文件或网络。字符编码问题能让一个简单的任务变得异常复杂。但别担心，Guava来帮忙了！

### [字符编码的挑战](#字符编码的挑战)

在Java中，处理不同编码的文本，尤其是在I/O操作中，经常会遇到`UnsupportedEncodingException`。这是因为不同的系统和文本文件可能使用不同的字符编码。比如，Windows可能默认使用CP1252，而Linux可能使用UTF-8。如果不正确处理这些编码，就会导致乱码或者错误。

### [Guava的Charsets](#guava的charsets)

Guava提供了一套字符集（Charsets）工具，让处理这些问题变得简单。Guava定义了所有标准的Java字符集，这样咱们就不必手动处理那些繁琐的字符串了。比如，当需要转换字节数据到字符串，或者相反的操作时，Guava的Charsets就派上用场了。

看看下面这个例子：

在这段代码里，使用`Charsets.UTF_8`来确保字符串正确地被编码和解码。Guava的Charsets处理起来既简单又不易出错。

### [更多字符处理工具](#更多字符处理工具)

除了Charsets，Guava还提供了更多字符处理工具。比如，有时咱们需要对字符串中的特定字符进行操作，Guava的`CharMatcher`类就是专门为此设计的。

来看个例子，假设咱们要从字符串中移除所有数字：

在这个例子中，`CharMatcher.inRange('0', '9')`创建了一个匹配所有数字的匹配器，然后`removeFrom`方法就将这些数字从字符串中移除了。这样的处理不仅代码量少，而且逻辑清晰易懂。

详情可以看这篇文章 String&Ints

## [源（Source）和汇（Sink）模式](#源-source-和汇-sink-模式)

在处理文件和流的时候，常常需要读数据（Source）和写数据（Sink）。Guava在这方面提供了一套非常优雅的解决方案，让这些操作变得既简单又直观。

在Guava中，Source代表一个数据的来源，可以是文件、URL或者任何其他数据源。而Sink则是数据的目的地，比如文件或者某个输出流。这种抽象的好处是，无论数据来源或去向如何变化，操作逻辑都保持一致。

### [文件的Source和Sink](#文件的source和sink)

先来看看文件操作。在传统的Java I/O中，需要创建FileInputStream或FileOutputStream，然后进行读写操作。但用Guava的Source和Sink，整个过程变得更加清晰。

看这个读文件的例子：

在这段代码中，`Files.asCharSource`创建了一个`CharSource`实例，它代表了文件中的字符数据。`charSource.read()`方法就能读取整个文件的内容。这样的代码不仅简洁，而且非常容易理解。

再来看看写文件的操作：

这里`Files.asCharSink`创建了一个`CharSink`实例，它代表文件的写入点。`charSink.writeLines`方法可以轻松地将一个字符串列表写入文件。

### [URL的Source](#url的source)

除了文件，Source和Sink还可以用于其他类型的数据源。比如，可以从一个URL读取数据：

在这个例子中，`Resources.asByteSource`创建了一个表示URL数据的`ByteSource`。然后就可以使用`byteSource.read()`来读取数据，非常方便。

## [异常处理与资源管理](#异常处理与资源管理)

在Java编程中，正确处理异常和资源是非常重要的，尤其是在进行I/O操作或者处理外部资源时。如果处理不当，很容易造成资源泄露或程序崩溃。Guava在这方面提供了一些非常棒的工具，帮助咱们写出更安全、更可靠的代码。

### [快速失败：Preconditions](#快速失败-preconditions)

在开始处理数据之前，检查输入是非常重要的。Guava提供了`Preconditions`类，帮助咱们快速校验条件，并在条件不满足时立即失败。这种“快速失败”机制有助于尽早发现问题，避免更深层次的错误。

看看这个例子：

这段代码中，`Preconditions.checkNotNull`方法确保传入的`data`不是`null`。如果是`null`，它会抛出一个`NullPointerException`，并附带自定义的错误消息。这样的校验既直观又有效，有助于提高代码的健壮性。

详情可以看这篇文章 String&Ints

### [资源管理：Closeables和FluentIterable](#资源管理-closeables和fluentiterable)

在Java中，正确管理资源，特别是那些需要关闭的资源，如流或连接，是非常重要的。Guava的`Closeables`类提供了便捷的方法来关闭这些资源，而不必担心`IOException`。

在这个例子中，无论在使用流的过程中是否发生异常，`Closeables.closeQuietly`都会在`finally`块中安全地关闭流。这样的处理方式不仅简洁，而且可以避免因忘记关闭资源而导致的问题。

Guava的`FluentIterable`也是资源管理的好帮手。它提供了一种链式的方法来处理集合，使得操作集合变得既简洁又优雅。

在这段代码中，`FluentIterable.from`创建了一个可迭代的集合视图，`filter`方法用于过滤，最后`toList`将结果转换为List。这样的链式调用，不仅代码可读性高，而且易于维护。

## [Guava与Java NIO的结合](#guava与java-nio的结合)

本章我们要聊聊Guava和Java NIO（非阻塞I/O）的结合。对于那些需要处理大量数据，或者对性能要求较高的应用来说，Java的NIO库是个非常强大的工具。但是，NIO的API有时候会显得有点复杂。这时候，Guava又一次展示了它的魔力，帮助我们更简单、更优雅地使用NIO。

### [Guava对NIO的增强](#guava对nio的增强)

Guava对Java NIO做了一些增强，让它的使用变得更加友好。Guava提供了类似于`ByteSource`和`ByteSink`这样的抽象，使得使用NIO进行文件操作或网络操作更加直观。

来看看这个读取文件内容的例子：

在这个例子中，`Files.asByteSource`方法创建了一个`ByteSource`实例，它代表文件中的字节数据。然后，可以使用`byteSource.read()`方法读取这些数据。这种方式比直接使用Java NIO的Channel和Buffer要简单得多。

### [NIO与流的转换](#nio与流的转换)

另一个强大的功能是Guava提供的NIO和流之间的转换。在某些情况下，可能需要在NIO的Channel和Java的InputStream/OutputStream之间进行转换。Guava在这方面提供了便利的工具。

在这个例子中，`Channels.newChannel`方法将一个InputStream转换为一个ReadableByteChannel。这样的转换让我们能够在需要使用NIO时，更加灵活地处理流。
