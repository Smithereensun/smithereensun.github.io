{

  "title": "Tomcat - Request请求处理过程：Connector",
  "has_date": true,
  "description": "引入 线程池Executor是在哪里启动的？ Request是如何处理并交个Container处理的？ Tomcat支持哪些协议？这些协议是处理的？协议层次结构如何设计的？ Connector Connector构造 本质是初始化了ProtocolHandler，默认是HTTP/1.1 NIO实现。",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-connector - Tomcat - Request请求处理过程：Connector.md",
  "date": "2026-04-19"

}

## [引入](#引入)

- 线程池Executor是在哪里启动的？

- Request是如何处理并交个Container处理的？

- Tomcat支持哪些协议？这些协议是处理的？协议层次结构如何设计的？

## [Connector](#connector)

### [Connector构造](#connector构造)

本质是初始化了ProtocolHandler，默认是HTTP/1.1 NIO实现。

ProtocolHandler是怎么通过protocol初始化实现的呢？我们看下`ProtocolHandler.create(protocol, apr)`

我们看到上述方法实际通过Protocol初始化了ProtocolHandler, 我们看下它所支持的HTTP1.1，Ajp协议的处理，我们通过它的类层次结构来看协议支持处理类
![](/imported/markdown/2026-04-19-markdown-d826663b-tomcat-request请求处理过程-connector/images/5fad2f1f3e66-202603082052065.jpeg)
### [Connector初始化](#connector初始化)

在JMX的初始化模板方法`initInternal`中，进行了Connector的初始化，它做了哪些事呢？

- 给protocolHandler初始化了adapter //这adapter是真正衔接Container处理的适配器，后文我们会有详解。

- 设置parseBody的方法，默认为POST方法

- 一些校验

- 调用protocolHandler的init

protocolHandler的init做了什么？本质上调用了AbstractEndpoint的init方法

`endpoint.init()`做了什么呢？之前的版本中是直接调用bind方法，这里改成了bindWithCleanup, 变化点在于失败后的清理操作。

`bindWithCleanup()`做了bind方法，如果绑定失败就回调unbind方法。

`bind()`方法做了初始化ServerSocket和初始化ssl

### [Connector的启动](#connector的启动)

这里依然是调用JMX的模板方法startInternal方法, start方法本质就是委托给`protocolHandler`处理，调用它的start方法

`protocolHandler.start()`方法如下，它又交给endpoint进行start处理

`endpoint.start()`就是调用startInternal方法。当然它会先检查是否绑定端口，没有绑定便执行bindWithCleanup方法

我们看下NIOEndPoint的`startInternal`方法做了啥

`createExecutor()`方法如下，本质是创建一个ThreadPoolExecutor
