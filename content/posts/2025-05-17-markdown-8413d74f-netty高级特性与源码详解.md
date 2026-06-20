{

  "title": "Netty高级特性与源码详解",
  "has_date": true,
  "description": "粘包与半包 粘包现象 粘包的问题出现是因为不知道一个用户消息的边界在哪，如果知道了边界在哪，接收方就可以通过边界来划分出有效的用户消息。 服务端代码 客户端代码希望发送 10 个消息，每个消息是 16 字节 服务器端的某次输出，可以看到一次就接收了 160 个字节，而期望的是一次16字节，分 10 ",
  "tags": [
    "框架"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/networkio/netty-advancedusage - Netty高级特性与源码详解.md",
  "date": "2025-05-17"

}

## [粘包与半包](#粘包与半包)

### [粘包现象](#粘包现象)

粘包的问题出现是因为不知道一个用户消息的边界在哪，如果知道了边界在哪，接收方就可以通过边界来划分出有效的用户消息。

服务端代码

客户端代码希望发送 10 个消息，每个消息是 16 字节

服务器端的某次输出，可以看到一次就接收了 160 个字节，而期望的是一次16字节，分 10 次接收。这就出现了粘包现象

### [半包现象](#半包现象)

半包是指 接收端只收到了部分数据，而非完整的数据的情况

客户端代码希望发送 1 个消息，这个消息是 160 字节，代码改为

为现象明显，服务端修改一下接收缓冲区，其它代码不变

服务器端的某次输出，可以看到接收的消息被分为两节，如 第一次 20 字节，第二次 140 字节

**注意**：serverBootstrap.option(ChannelOption.SO_RCVBUF, 10) 影响的底层接收缓冲区（即滑动窗口）大小，仅决定了 netty 读取的最小单位，netty 实际每次读取的一般是它的整数倍

### [现象分析](#现象分析)

这里出现的粘包半包问题，并非是JavaNIO或Netty的问题，本质是TCP是流失协议，消息无边界。

粘包：

- 现象，发送 abc def，接收 abcdef

- 原因

  - 应用层：接收方 ByteBuf 设置太大（Netty 默认 1024）

  - 滑动窗口：假设发送方 256 bytes 表示一个完整报文，但由于接收方处理不及时且窗口大小足够大，这 256 bytes 字节就会缓冲在接收方的滑动窗口中，当滑动窗口中缓冲了多个报文就会粘包

  - Nagle 算法：会造成粘包

半包

- 现象，发送 abcdef，接收 abc def

- 原因

  - 应用层：接收方 ByteBuf 小于实际发送数据量

  - 滑动窗口：假设接收方的窗口只剩了 128 bytes，发送方的报文大小是 256 bytes，这时放不下了，只能先发送前 128 bytes，等待 ack 后才能发送剩余部分，这就造成了半包

  - MSS 限制：当发送的数据超过 MSS 限制后，会将数据切分发送，就会造成半包

### [解决方案](#解决方案)

接下来看下Netty如何解决以上问题的：

1. 短链接，发一个包建立一次连接，这样连接建立到连接断开之间就是消息的边界，缺点效率太低

1. 每一条消息采用固定长度，缺点浪费空间

1. 每一条消息采用分隔符，例如 \n，缺点需要转义

1. 每一条消息分为 head 和 body，head 中包含 body 的长度

#### [方法1：短链接（极不推荐）](#方法1-短链接-极不推荐)

以解决粘包为例

输出，略

半包用这种办法还是不好解决，因为接收方的缓冲区大小是有限的

#### [方法2：固定长度](#方法2-固定长度)

让所有数据包长度固定（假设长度为 8 字节），服务器端加入

客户端测试代码，注意, 采用这种方法后，客户端什么时候 flush 都可以

客户端输出

服务端输出

缺点是，数据包的大小不好把握

- 长度定的太大，浪费

- 长度定的太小，对某些数据包又显得不够

#### [方法3：固定分隔符](#方法3-固定分隔符)

服务端加入，默认以 \n 或 \r\n 作为分隔符，如果超出指定长度仍未出现分隔符，则抛出异常

客户端在每条消息之后，加入 \n 分隔符

客户端输出

服务端输出

缺点，处理字符数据比较合适，但如果**内容本身包含了分隔符**（字节数据常常会有此情况），那么就会解析错误

#### [方法4：预设长度](#方法4-预设长度)

在发送消息前，先约定用定长字节表示接下来数据的长度

客户端代码

客户端输出

服务端输出

## [协议设计与解析](#协议设计与解析)

### [为什么需要协议？](#为什么需要协议)

TCP/IP 中消息传输基于流的方式，没有边界。

协议的目的就是划定消息的边界，制定通信双方要共同遵守的通信规则

例如：在网络上传输

是中文一句著名的无标点符号句子，在没有标点符号情况下，这句话有数种拆解方式，而意思却是完全不同，所以常被用作讲述标点符号的重要性

一种解读

另一种解读

如何设计协议呢？其实就是给网络传输的信息加上“标点符号”。但通过分隔符来断句不是很好，因为分隔符本身如果用于传输，那么必须加以区分。因此，下面一种协议较为常用

例如，假设一个中文字符长度为 3，按照上述协议的规则，发送信息方式如下，就不会被接收方弄错意思了

### [redis 协议举例](#redis-协议举例)

模拟 redis 客户端发送命令。

当然 netty提供了现成的这些协议，不需要我们自己来开发，这里是为了知其所以然

### [http 协议举例](#http-协议举例)

模拟http服务端

### [自定义协议要素](#自定义协议要素)

- 魔数：约定好的，用来在第一时间判定是否是无效数据包。

- 版本号：可以支持协议的升级

- 序列化算法：消息正文到底采用哪种序列化反序列化方式，可以由此扩展，例如：json、protobuf、hessian、jdk

- 指令类型：是登录、注册、单聊、群聊... 跟业务相关

- 请求序号：为了双工通信，提供异步能力

- 正文长度

- 消息正文

#### [编解码器](#编解码器)

根据上面的要素，设计一个登录请求消息和登录响应消息，并使用 Netty 完成收发

测试

#### [@Sharable](#sharable)

- 当 handler 不保存状态时，就可以安全地在多线程下被共享

- 但要注意对于编解码器类，不能继承 ByteToMessageCodec 或 CombinedChannelDuplexHandler 父类，他们的构造方法对 @Sharable 有限制

- 如果能确保编解码器不会保存状态，可以继承 MessageToMessageCodec 父类

## [扩展序列化算法](#扩展序列化算法)

序列化，反序列化主要用在消息正文的转换上

- 序列化时，需要将 Java 对象变为要传输的数据（可以是 byte[]，或 json 等，最终都需要变成 byte[]）

- 反序列化时，需要将传入的正文数据还原成 Java 对象，便于处理

目前的代码仅支持 Java 自带的序列化，反序列化机制，核心代码如下

为了支持更多序列化算法，抽象一个 Serializer 接口

提供两个实现，这里直接将具体实现加入了枚举类 Serializer.Algorithm 中

增加配置类和配置文件

配置文件

修改编解码器

其中确定具体消息类型，可以根据 `消息类型字节` 获取到对应的 `消息 class`

## [参数调优](#参数调优)

相关源码待更新

### [客户端参数 CONNECT_TIMEOUT_MILLIS](#客户端参数-connect-timeout-millis)

- 属于 SocketChannal 参数

- 用在客户端建立连接时，如果在指定毫秒内无法连接，会抛出 timeout 异常

- SO_TIMEOUT 主要用在阻塞 IO，阻塞 IO 中 accept，read 等都是无限等待的，如果不希望永远阻塞，使用它调整超时时间

另外源码部分 `io.netty.channel.nio.AbstractNioChannel.AbstractNioUnsafe#connect`

### [服务端参数 SO_BACKLOG](#服务端参数-so-backlog)

这是属于 ServerSocketChannal 的参数

三次握手时有半连接队列和全连接队列，详情看这篇文章：TCP - 半连接队列和全连接队列

- sync queue - 半连接队列

  - 大小通过 /proc/sys/net/ipv4/tcp_max_syn_backlog 指定，在 `syncookies` 启用的情况下，逻辑上没有最大值限制，这个设置便被忽略

- accept queue - 全连接队列

  - 其大小通过 /proc/sys/net/core/somaxconn 指定，在使用 listen 函数时，内核会根据传入的 backlog 参数与系统参数，取二者的较小值

  - 如果 accpet queue 队列满了，server 将发送一个拒绝连接的错误信息到 client

netty 中 可以通过 option(ChannelOption.SO_BACKLOG, 值) 来设置backlog 的大小

可以通过下面源码查看默认大小

### [TCP_NODELAY](#tcp-nodelay)

- 属于 SocketChannal 参数

立即发送，建议设置成true。false就是开启了nagle算法

### [SO_SNDBUF & SO_RCVBUF](#so-sndbuf-so-rcvbuf)

设置滑动窗口的参数，在早些可能需要设置这些参数，但现在tcp会根据拥塞等对窗口进行自动调整，因此不建议手动设置这两个值。

- SO_SNDBUF 属于 SocketChannal 参数

- SO_RCVBUF 既可用于 SocketChannal 参数，也可以用于 ServerSocketChannal 参数（建议设置到 ServerSocketChannal 上）

### [ALLOCATOR](#allocator)

- 属于 SocketChannal 参数

- 用来分配 ByteBuf， ctx.alloc()

### [RCVBUF_ALLOCATOR](#rcvbuf-allocator)

- 属于 SocketChannal 参数

- 控制 netty 接收缓冲区大小

- 负责入站数据的分配，决定入站缓冲区的大小（并可动态调整），统一采用 direct 直接内存，具体池化还是非池化由 allocator 决定

## [源码详解](#源码详解)

### [启动剖析](#启动剖析)

我们就来看看 netty 中对下面的代码是怎样进行处理的

入口 `io.netty.bootstrap.ServerBootstrap#bind`

关键代码 `io.netty.bootstrap.AbstractBootstrap#doBind`

这个函数是由哪些线程处理的呢？可以先有个概念，再往下看：

1. init & register regFuture 处理

  1. init：由main处理

    1. 创建NioServerSocketChannel：由main处理

    1. 添加 NioServerSocketChannel 初始化 handler ：由main处理

      1. 初始化 handler 等待调用

1. register

  1. 启动 nio boss 线程 ：由main处理

  1. 原生 ssc 注册至 selector 未关注事件：由nio-thread处理

  1. 执行 NioServerSocketChannel 初始化 handler：由nio-thread处理

1. regFuture 等待回调 doBind0：由nio-thread处理

  1. 原生 ServerSocketChannel 绑定：由nio-thread处理

  1. 触发NioServerSocketChannel active 事件：由nio-thread处理

关键代码 `io.netty.bootstrap.AbstractBootstrap#initAndRegister`

关键代码 `io.netty.bootstrap.ServerBootstrap#init`

关键代码 `io.netty.channel.AbstractChannel.AbstractUnsafe#register`

`io.netty.channel.AbstractChannel.AbstractUnsafe#register0`

关键代码 `io.netty.channel.ChannelInitializer#initChannel`

关键代码 `io.netty.bootstrap.AbstractBootstrap#doBind0`

关键代码 `io.netty.channel.AbstractChannel.AbstractUnsafe#bind`

关键代码 `io.netty.channel.socket.nio.NioServerSocketChannel#doBind`

关键代码 `io.netty.channel.DefaultChannelPipeline.HeadContext#channelActive`

关键代码 `io.netty.channel.nio.AbstractNioChannel#doBeginRead`

### [NioEventLoop 剖析](#nioeventloop-剖析)

NioEventLoop 线程不仅要处理 IO 事件，还要处理 Task（包括普通任务和定时任务），

提交任务代码 `io.netty.util.concurrent.SingleThreadEventExecutor#execute`

唤醒 select 阻塞线程`io.netty.channel.nio.NioEventLoop#wakeup`

启动 EventLoop 主循环 `io.netty.util.concurrent.SingleThreadEventExecutor#doStartThread`

`io.netty.channel.nio.NioEventLoop#run` 主要任务是执行死循环，不断看有没有新任务，有没有 IO 事件

#### [注意](#注意)

这里有个费解的地方就是 wakeup，它既可以由提交任务的线程来调用（比较好理解），也可以由 EventLoop 线程来调用（比较费解），这里要知道 wakeup 方法的效果：

- 由非 EventLoop 线程调用，会唤醒当前在执行 select 阻塞的 EventLoop 线程

- 由 EventLoop 自己调用，会本次的 wakeup 会取消下一次的 select 操作

`io.netty.channel.nio.NioEventLoop#select`

处理 keys `io.netty.channel.nio.NioEventLoop#processSelectedKeys`

`io.netty.channel.nio.NioEventLoop#processSelectedKey`

### [accept 剖析](#accept-剖析)

nio 中如下代码，在 netty 中的流程

先来看可接入事件处理（accept）

`io.netty.channel.nio.AbstractNioMessageChannel.NioMessageUnsafe#read`

关键代码 `io.netty.bootstrap.ServerBootstrap.ServerBootstrapAcceptor#channelRead`

又回到了熟悉的 `io.netty.channel.AbstractChannel.AbstractUnsafe#register` 方法

`io.netty.channel.AbstractChannel.AbstractUnsafe#register0`

回到了熟悉的代码 `io.netty.channel.DefaultChannelPipeline.HeadContext#channelActive`

`io.netty.channel.nio.AbstractNioChannel#doBeginRead`

### [read 剖析](#read-剖析)

再来看可读事件 `io.netty.channel.nio.AbstractNioByteChannel.NioByteUnsafe#read`，注意发送的数据未必能够一次读完，因此会触发多次 nio read 事件，一次事件内会触发多次 pipeline read，一次事件会触发一次 pipeline read complete

`io.netty.channel.DefaultMaxMessagesRecvByteBufAllocator.MaxMessageHandle#continueReading(io.netty.util.UncheckedBooleanSupplier)`
