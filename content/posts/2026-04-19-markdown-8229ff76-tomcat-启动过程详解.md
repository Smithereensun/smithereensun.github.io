{

  "title": "Tomcat - 启动过程详解",
  "has_date": true,
  "description": "总体流程 我们看下整体的初始化和启动的流程，在**理解的时候可以直接和Tomcat架构设计中组件关联上**： 启动过程代码浅析 看了下网上关于Tomcat的文章，很多直接关注在纯代码的分析，这种是很难的；我建议你一定要把代码加载进来自己看一下，然后这里我把它转化为核心的几个问题来帮助你理解。 Boo",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-start - Tomcat - 启动过程详解.md",
  "date": "2026-04-19"

}

## [总体流程](#总体流程)

我们看下整体的初始化和启动的流程，在**理解的时候可以直接和Tomcat架构设计中组件关联上**：
![](/imported/markdown/2026-04-19-markdown-8229ff76-tomcat-启动过程详解/images/6bb4be041cd5-202603081035646.png)
## [启动过程代码浅析](#启动过程代码浅析)

看了下网上关于Tomcat的文章，很多直接关注在纯代码的分析，这种是很难的；我建议你一定要把代码加载进来自己看一下，然后这里我把它转化为核心的几个问题来帮助你理解。

### [Bootstrap主入口？](#bootstrap主入口)

Tomcat源码就从它的main方法开始。Tomcat的main方法在org.apache.catalina.startup.Bootstrap 里。让我们带着这个为看下Catalina的初始化的

通过上面几行关键代码的注释，我们就可以看出Catalina是如何初始化的。这里还留下一个问题，tomcat为什么要初始化不同的classloader呢？我们将在下文进行详解。

### [Bootstrap如何初始化Catalina的？](#bootstrap如何初始化catalina的)

我们用`Sequence Diagram`插件来看main方法的时序图，但是可以发现它并没有帮我们画出Bootstrap初始化Catalina的过程，这和上面的组件初始化不符合？
![](/imported/markdown/2026-04-19-markdown-8229ff76-tomcat-启动过程详解/images/0d2001c2ac05-202603081042949.png)
让我们带着这个为看下Catalina的初始化的

通过上面几行关键代码的注释，我们就可以看出Catalina是如何初始化的。这里还留下一个问题，tomcat为什么要初始化不同的classloader呢？我们将在下文进行详解。

## [启动过程：类加载机制详解](#启动过程-类加载机制详解)

### [Tomcat初始化了哪些classloader](#tomcat初始化了哪些classloader)

在Bootstrap中我们可以看到有如下三个classloader

#### [如何初始化的呢？](#如何初始化的呢)

可以看出，catalinaLoader 和 sharedLoader 的 parentClassLoader 是 commonLoader。

#### [如何创建classLoader的？](#如何创建classloader的)

不妨再看下如何创建的？

方法的逻辑也比较简单就是从 catalina.property文件里找 common.loader, shared.loader, server.loader 对应的值，然后构造成Repository 列表，再将Repository 列表传入ClassLoaderFactory.createClassLoader 方法，ClassLoaderFactory.createClassLoader 返回的是 URLClassLoader，而Repository 列表就是这个URLClassLoader 可以加在的类的路径。 在catalina.property文件里

其中 shared.loader, server.loader 是没有值的，createClassLoader 方法里如果没有值的话，就返回传入的 parent ClassLoader，也就是说，commonLoader,catalinaLoader,sharedLoader 其实是一个对象。在Tomcat之前的版本里，这三个是不同的URLClassLoader对象。

初始化完三个ClassLoader对象后，init() 方法就使用 catalinaClassLoader 加载了org.apache.catalina.startup.Catalina 类，并创建了一个对象，然后通过反射调用这个对象的 setParentClassLoader 方法，传入的参数是 sharedClassLoader。最后吧这个 Catania 对象复制给 catalinaDaemon 属性。

### [深入理解](#深入理解)

可以复习下类加载机制的基础：解密类加载机制：深入理解JVM如何加载你的代码

#### [什么是类加载机制](#什么是类加载机制)

Java是一门面向对象的语言，而对象又必然依托于类。类要运行，必须首先被加载到内存。我们可以简单地把类分为几类：

- Java自带的核心类

- Java支持的可扩展类

- 我们自己编写的类

- **为什么要设计多个类加载器**？

如果所有的类都使用一个类加载器来加载，会出现什么问题呢？

假如我们自己编写一个类`java.util.Object`，它的实现可能有一定的危险性或者隐藏的bug。而我们知道Java自带的核心类里面也有`java.util.Object`，如果JVM启动的时候先行加载的是我们自己编写的`java.util.Object`，那么就有可能出现安全问题！

所以，Sun（后被Oracle收购）采用了另外一种方式来保证最基本的、也是最核心的功能不会被破坏。你猜的没错，那就是双亲委派模式！

- **什么是双亲委派模型**？

双亲委派模型解决了类错乱加载的问题，也设计得非常精妙。

双亲委派模式对类加载器定义了层级，每个类加载器都有一个父类加载器。在一个类需要加载的时候，首先委派给父类加载器来加载，而父类加载器又委派给祖父类加载器来加载，以此类推。如果父类及上面的类加载器都加载不了，那么由当前类加载器来加载，并将被加载的类缓存起来。
![](/imported/markdown/2026-04-19-markdown-8229ff76-tomcat-启动过程详解/images/0b6c512490ee-202603081048197.png)
所以上述类是这么加载的

- Java自带的核心类 -- 由启动类加载器加载

- Java支持的可扩展类 -- 由扩展类加载器加载

- 我们自己编写的类 -- 默认由应用程序类加载器或其子类加载

但它也不是万能的，在有些场景也会遇到它解决不了的问题，比如如下场景。

#### [双亲委派模型问题是如何解决的？](#双亲委派模型问题是如何解决的)

在Java核心类里面有SPI（Service Provider Interface），它由Sun编写规范，第三方来负责实现。SPI需要用到第三方实现类。如果使用双亲委派模型，那么第三方实现类也需要放在Java核心类里面才可以，不然的话第三方实现类将不能被加载使用。但是这显然是不合理的！怎么办呢？

**ContextClassLoader**（上下文类加载器）就来解围了。

在java.lang.Thread里面有两个方法，get/set上下文类加载器

我们可以通过在SPI类里面调用getContextClassLoader来获取第三方实现类的类加载器。由第三方实现类通过调用setContextClassLoader来传入自己实现的类加载器, 这样就变相地解决了双亲委派模式遇到的问题。

#### [为什么Tomcat的类加载器也不是双亲委派模型](#为什么tomcat的类加载器也不是双亲委派模型)

我们知道，Java默认的类加载机制是通过双亲委派模型来实现的，而Tomcat实现的方式又和双亲委派模型有所区别。

**原因在于一个Tomcat容器允许同时运行多个Web程序，每个Web程序依赖的类又必须是相互隔离的**。因此，如果Tomcat使用双亲委派模式来加载类的话，将导致Web程序依赖的类变为共享的。

举个例子，假如我们有两个Web程序，一个依赖A库的1.0版本，另一个依赖A库的2.0版本，他们都使用了类xxx.xx.Clazz，其实现的逻辑因类库版本的不同而结构完全不同。那么这两个Web程序的其中一个必然因为加载的Clazz不是所使用的Clazz而出现问题！而这对于开发来说是非常致命的！

#### [Tomcat类加载机制是怎么样的呢](#tomcat类加载机制是怎么样的呢)

既然Tomcat的类加载机器不同于双亲委派模式，那么它又是一种怎样的模式呢？

我们在这里一定要看下官网提供的[类加载的文档](https://tomcat.apache.org/tomcat-9.0-doc/class-loader-howto.html)
![](/imported/markdown/2026-04-19-markdown-8229ff76-tomcat-启动过程详解/images/a28eccfb8b51-202603081048483.png)
结合经典的类加载机制，我们完整的看下Tomcat类加载图
![](/imported/markdown/2026-04-19-markdown-8229ff76-tomcat-启动过程详解/images/1d2e7410b7fc-202603081049372.png)
我们在这张图中看到很多类加载器，除了Jdk自带的类加载器，我们尤其关心Tomcat自身持有的类加载器。仔细一点我们很容易发现：Catalina类加载器和Shared类加载器，他们并不是父子关系，而是兄弟关系。为啥这样设计，我们得分析一下每个类加载器的用途，才能知晓。

- **Common类加载器**，负责加载Tomcat和Web应用都复用的类

  - **Catalina类加载器**，负责加载Tomcat专用的类，而这些被加载的类在Web应用中将不可见

  - **Shared类加载器**，负责加载Tomcat下所有的Web应用程序都复用的类，而这些被加载的类在Tomcat中将不可见

    - **WebApp类加载器**，负责加载具体的某个Web应用程序所使用到的类，而这些被加载的类在Tomcat和其他的Web应用程序都将不可见

    - **Jsp类加载器**，每个jsp页面一个类加载器，不同的jsp页面有不同的类加载器，方便实现jsp页面的热插拔

同样的，我们可以看到通过**ContextClassLoader**（上下文类加载器）的**setContextClassLoader**来传入自己实现的类加载器

#### [WebApp类加载器](#webapp类加载器)

到这儿，我们隐隐感觉到少分析了点什么！没错，就是WebApp类加载器。整个启动过程分析下来，我们仍然没有看到这个类加载器。它又是在哪儿出现的呢？

我们知道WebApp类加载器是Web应用私有的，而每个Web应用其实算是一个Context，那么我们通过Context的实现类应该可以发现。在Tomcat中，Context的默认实现为StandardContext，我们看看这个类的startInternal()方法，在这儿我们发现了我们感兴趣的WebApp类加载器。

入口代码非常简单，就是webappLoader不存在的时候创建一个，并调用setLoader方法。我们接着分析setLoader

这儿，我们感兴趣的就两行代码：

## [启动过程：Catalina的加载](#启动过程-catalina的加载)

### [Catalina的引入](#catalina的引入)

通过前面，我们知道了Tomcat的类加载机制和整体的组件加载流程；我们也知道通过Bootstrap初始化的catalinaClassLoader加载了Catalina，那么进而引入了一个问题就是Catalina是如何加载的呢？加载了什么呢？

- 先回顾下整个流程，和我们分析的阶段

![](/imported/markdown/2026-04-19-markdown-8229ff76-tomcat-启动过程详解/images/467a952dd9d0-202603081050972.png)

- 看下Bootstrap中Load的过程

### [Catalina的加载](#catalina的加载)

上一步，我们知道catalina load的触发，因为有参数所以是load(String[])方法。我们进而看下这个load方法做了什么？

- load(String[])本质上还是调用了load方法

- load加载过程本质上是初始化Server的实例

总体流程如下：
![](/imported/markdown/2026-04-19-markdown-8229ff76-tomcat-启动过程详解/images/639473177949-202603081051887.png)
#### [initDirs](#initdirs)

已经弃用了，Tomcat10会删除这个方法。

#### [initNaming](#initnaming)

设置额外的系统变量

#### [Server.xml的解析](#server-xml的解析)

分三大块，下面的代码还是很清晰的:

#### [initStreams](#initstreams)

替换掉System.out, System.err为自定义的PrintStream

### [Catalina 的启动](#catalina-的启动)

在 load 方法之后，Tomcat 就初始化了一系列的组件，接着就可以调用 start 方法进行启动了。

上面这段代码，逻辑非常简单，首先确定 getServer() 方法不为 null，也就是确定 server 属性不为null，而 server 属性是在 load 方法就初始化了。

整段代码的核心就是 try-catch 里的 getServer().start() 方法了，也就是调用 Server 对象的 start() 方法来启动 Tomcat。本篇文章就先不对 Server 的 start() 方法进行解析了，下篇文章会单独讲。

### [Catalina 的关闭](#catalina-的关闭)

调用完 Server#start 方法之后，注册了一个ShutDownHook，也就是 CatalinaShutdownHook 对象，

CatalinaShutdownHook 的逻辑也简单，就是调用 Catalina 对象的 stop 方法来停止 tomcat。

最后就进入 if 语句了，await 是在 Bootstrap 里调用的时候设置为 true 的，也就是本文开头的时候提到的三个方法中的一个。await 方法的作用是停住主线程，等待用户输入shutdown 命令之后，停止等待，之后 main 线程就调用 stop 方法来停止Tomcat。

Catalina 的 stop 方法主要逻辑是调用 Server 对象的 stop 方法。

### [聊聊关闭钩子](#聊聊关闭钩子)

上面我们看到CatalinaShutdownHook, 这里有必要谈谈JVM的关闭钩子。

关闭钩子是指通过**Runtime.addShutdownHook注册的但尚未开始的线程**。这些钩子可以用于**实现服务或者应用程序的清理工作**，例如删除临时文件，或者清除无法由操作系统自动清除的资源。

JVM既可以正常关闭，也可以强行关闭。正常关闭的触发方式有多种，包括：当最后一个“正常（非守护）”线程结束时，或者当调用了System.exit时，或者通过其他特定于平台的方法关闭时（例如发送了SIGINT信号或者键入Ctrl-C）。

在**正常关闭中，JVM首先调用所有已注册的关闭钩子**。JVM并不能保证关闭钩子的调用顺序。在关闭应用程序线程时，如果有（守护或者非守护）线程仍然在执行，那么这些线程接下来将与关闭进程并发执行。当所有的关闭钩子都执行结束时，如果runFinalizersOnExit为true【通过Runtime.runFinalizersOnExit(true)设置】，那么JVM将运行这些Finalizer（对象重写的finalize方法），然后再停止。JVM不会停止或中断任何在关闭时仍然运行的应用程序线程。当JVM最终结束时，这些线程将被强行结束。如果关闭钩子或者Finalizer没有执行完成，那么正常关闭进程“挂起”并且JVM必须被强行关闭。当**JVM被强行关闭时，只是关闭JVM，并不会运行关闭钩子**（举个例子，类似于电源都直接拔了，还怎么做其它动作呢？）。

下面是一个简单的示例：

和（可能的）执行结果（因为JVM不保证关闭钩子的调用顺序，因此结果中的第二、三行可能出现相反的顺序）：

可以看到，main函数执行完成，首先输出的是Main Thread Ends，接下来执行关闭钩子，输出Hook2 Ends和Hook1 Ends。这两行也可以证实：JVM确实不是以注册的顺序来调用关闭钩子的。而由于hook3在调用了addShutdownHook后，接着对其调用了removeShutdownHook将其移除，于是hook3在JVM退出时没有执行，因此没有输出Hook3 Ends。

另外，由于MyHook类实现了finalize方法，而main函数中第一行又通过Runtime.runFinalizersOnExit(true)打开了退出JVM时执行Finalizer的开关，于是3个hook对象的finalize方法被调用，输出了3行Finalize。

注意，多次调用addShutdownHook来注册同一个关闭钩子将会抛出IllegalArgumentException:

另外，从JavaDoc中得知：**一旦JVM关闭流程开始，就只能通过调用halt方法来停止该流程，也不可能再注册或移除关闭钩子了，这些操作将导致抛出IllegalStateException**。

如果在关闭钩子中关闭应用程序的公共的组件，如日志服务，或者数据库连接等，像下面这样：

由于**关闭钩子将并发执行，因此在关闭日志时可能导致其他需要日志服务的关闭钩子产生问题**。**为了避免这种情况，可以使关闭钩子不依赖那些可能被应用程序或其他关闭钩子关闭的服务**。实现这种功能的一种方式是对所有服务使用同一个关闭钩子（而不是每个服务使用一个不同的关闭钩子），并且在该关闭钩子中执行一系列的关闭操作。这确保了关闭操作在单个线程中串行执行，从而避免了在关闭操作之前出现竞态条件或死锁等问题。

#### [使用场景](#使用场景)

通过Hook实现临时文件清理

### [小结](#小结)

Catalina 类承接了 Bootstrap 类的 load 和 start 方法，然后根据配置初始化了 Tomcat 的组件，并调用了 Server 类的 init 和 start 方法来启动 Tomcat。
