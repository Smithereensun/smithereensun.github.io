{

  "title": "Tomcat - Request请求处理：Container设计",
  "has_date": true,
  "description": "理解思路 为什么我们说上面的是Container呢？我们看下几个Container之间的关系**： 从上图上，我们也可以看出Container顶层也是基于Lifecycle的组件设计的。 在设计Container组件层次组件时，上述4个组件分别做什么的呢？为什么要四种组件呢？** 如下是Contai",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-container - Tomcat - Request请求处理：Container设计.md",
  "date": "2026-04-19"

}

![](/imported/markdown/2026-04-19-markdown-2ebbdaa7-tomcat-request请求处理-container设计/images/9144d256a0d5-202603082041943.png)
## [理解思路](#理解思路)

- **为什么我们说上面的是Container呢？我们看下几个Container之间的关系**：

![](/imported/markdown/2026-04-19-markdown-2ebbdaa7-tomcat-request请求处理-container设计/images/70228a99e241-202603082042639.jpeg)
从上图上，我们也可以看出Container顶层也是基于Lifecycle的组件设计的。

- **在设计Container组件层次组件时，上述4个组件分别做什么的呢？为什么要四种组件呢？**

如下是Container接口类的相关注释

**Engine** - 表示整个catalina的servlet引擎，多数情况下包含**一个或多个**子容器，这些子容器要么是Host，要么是Context实现，或者是其他自定义组。

**Host** - 表示包含多个Context的虚拟主机的。

**Context** — 表示一个ServletContext，表示一个webapp，它通常包含一个或多个wrapper。

**Wrapper** - 表示一个servlet定义的（如果servlet本身实现了SingleThreadModel，则可能支持多个servlet实例）。

- **结合整体的框架图中上述组件部分，我们看下包含了什么**？

![](/imported/markdown/2026-04-19-markdown-2ebbdaa7-tomcat-request请求处理-container设计/images/ec169f238c5d-202603082042501.png)
很明显，除了四个组件的嵌套关系，Container中还包含了Realm，Cluster，Listeners, Pipleline等支持组件。

这一点，还可以通过相关注释可以看出：

## [Container的设计](#container的设计)

这container应该包含哪些接口呢？如果你看源代码它包含二十多个接口，这里理解的时候一定要分组去理解。

### [Container的层次结构方法](#container的层次结构方法)

查找父容器的方法：

由于Engine显然上层是Service，所以里面加了一个getService的方法

类比树接口，有Parent方法，那肯定也child方法：

### [Container事件监听相关方法](#container事件监听相关方法)

前文我们也分析过Tomcat的事件监听机制，Container也是一样， 比如如下的ContainerListener

除了Container级别的，和前文我们理解的一样，还有属性相关的Listener, 显然就增删属性的监听方法

最后显然还有事件的触发方法

### [Container功能支撑方法](#container功能支撑方法)

前面我们知道，Loader, Logger, Manager, Realm, Resources等支撑功能。这里简单看下接口定义，相关基本实现看下节ContainerBase的实现。

- Loader

- Logger

- Manager

体现在我们之前分析的JMX管理

- Realm

- Cluster

- 其它

## [Container基本实现：ContainerBase](#container基本实现-containerbase)

就讲讲几个比较核心的

### [Logger](#logger)

日志记录器，比较简单，直接看代码

### [Cluster](#cluster)

- `getCluster`：读锁，获取子类的cluster，如果没有则返回父类的cluster；

- `getClusterInternal`: 读锁，获取子类的cluster

- `setCluster`: 写锁，设置container的cluster；由于cluster具备生命周期，所以需要对停止旧的cluster，启动新的cluster；设置成功后，再触发cluster变更事件。

### [Realm](#realm)

Realm和上面的Cluster方法基本一致。

### [name等属性](#name等属性)

此类属性改变时触发属性变更事件，比如name是容器的名字，name变更会触发name变更事件。

### [child相关](#child相关)

添加子容器

查找子容器

- 删除子容器

子容器有生命周期，所以应该是先停止，然后销毁（distroy), 再触发删除事件，最后将children中子容器删除。

### [Lifecycle的模板方法](#lifecycle的模板方法)

- **initInternal**

startStopThreads 默认为 1，所以 reconfigureStartStopExecutor 方法会走 if 语句，而 startStopExecutor 最开始是没有赋值的，startStopExecutor instanceof InlineExecutorService 会返回 false，因此最终会执行 startStopExecutor = new InlineExecutorService()，InlineExecutorService 只是简单地实现了 java.util.concurrent.AbstractExecutorService 类。 最终 reconfigureStartStopExecutor 给 startStopExecutor 这个成员变量设置了，startStopExecutor。

- **startInternal**

试想，container中有很多组件，而且属于Lifecycle生命周期管理；那么启动容器的时候，必然是逐个将这些子组件（包括子容器）启动起来。

- **stopInternal**

和initInternal初始化子组件方式倒过来，逐一停止子组件，并触发相关事件。

- **destroyInternal**

对比下initInternal，它初始化了什么就destory什么
