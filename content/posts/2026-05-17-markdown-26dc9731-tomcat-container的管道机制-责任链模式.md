{

  "title": "Tomcat - Container的管道机制：责任链模式",
  "has_date": true,
  "description": "内容引入 承接上文Engine的设计，从以下几个方面，我将向你解释为什么要理解Tomcat中管道机制，它要解决什么问题？ Tomcat总计架构图中Pipeline和Vavle 我们在上文Engine中有一块Pipline没有解释： 为什么Tomcat要引入Pipline呢？它要解决什么问题呢？ 下文",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-container-pipline - Tomcat - Container的管道机制：责任链模式.md",
  "date": "2026-05-17"

}

## [内容引入](#内容引入)

承接上文Engine的设计，从以下几个方面，我将向你解释为什么要理解Tomcat中管道机制，它要解决什么问题？

- Tomcat总计架构图中Pipeline和Vavle

![](/imported/markdown/2026-05-17-markdown-26dc9731-tomcat-container的管道机制-责任链模式/images/d5ab7bea7eee-202603082049541.jpeg)

- 我们在上文Engine中有一块Pipline没有解释：

![](/imported/markdown/2026-05-17-markdown-26dc9731-tomcat-container的管道机制-责任链模式/images/b00f4c347766-202603082049790.jpeg)

- 为什么Tomcat要引入Pipline呢？它要解决什么问题呢？

下文将向你详细阐述。

## [知识准备](#知识准备)

在弄清楚管道机制前，你需要一些基础知识和其它软件设计中的应用场景。

### [责任链模式](#责任链模式)

管道机制在设计模式上属于责任链模式，如果你不理解，请参看如下文章：

责任链模式(Chain of responsibility pattern): 通过责任链模式, 你可以为某个请求创建一个对象链. 每个对象依序检查此请求并对其进行处理或者将它传给链中的下一个对象。

### [FilterChain](#filterchain)

在软件开发的常接触的责任链模式是FilterChain，它体现在很多软件设计中：

- **比如Spring Security框架中**

![](/imported/markdown/2026-05-17-markdown-26dc9731-tomcat-container的管道机制-责任链模式/images/b4481f818f5b-202603082050804.jpeg)

- **比如HttpServletRequest处理的过滤器中**

当一个request过来的时候，需要对这个request做一系列的加工，使用责任链模式可以使每个加工组件化，减少耦合。也可以使用在当一个request过来的时候，需要找到合适的加工方式。当一个加工方式不适合这个request的时候，传递到下一个加工方法，该加工方式再尝试对request加工。

网上找了图，这里我们后文将通过Tomcat请求处理向你阐述。
![](/imported/markdown/2026-05-17-markdown-26dc9731-tomcat-container的管道机制-责任链模式/images/1e0d4065abe3-202603082050780.jpeg)
## [Pipline机制](#pipline机制)

为什么要有管道机制？

在一个比较复杂的大型系统中，如果一个对象或数据流需要进行繁杂的逻辑处理，我们可以选择在一个大的组件中直接处理这些繁杂的业务逻辑， 这个方式虽然达到目的，但扩展性和可重用性较差， 因为可能牵一发而动全身。更好的解决方案是采用管道机制，**用一条管道把多个对象(阀门部件)连接起来，整体看起来就像若干个阀门嵌套在管道中一样，而处理逻辑放在阀门上**。

### [Vavle接口设计](#vavle接口设计)

理解它的设计，第一步就是阀门设计

### [Pipline接口设计](#pipline接口设计)

由于Pipline是为容器设计的，所以它在设计时加入了一个Containerd接口, 就是为了制定当前Pipline所属的容器：

我们接着看下Pipline接口设计

### [BaseVavle设计](#basevavle设计)

由于Valve也是组件，需要生命周期管理，所以实现LifecycleMBeanBase，同时集成Contained和Valve

### [StandardPipline实现](#standardpipline实现)

里面方法很简单，就直接贴代码了。它必然是继承LifecycleBase同时实现Pipline.

贴个图方面你理解
![](/imported/markdown/2026-05-17-markdown-26dc9731-tomcat-container的管道机制-责任链模式/images/6d1cf3a61942-202603082050452.jpeg)
### [ContainerBase中运用Pipline](#containerbase中运用pipline)

那么容器中是如何运用Pipline的呢？

- 容器中是如何运用Pipline的？

由于Container中都有涉及，实现方法肯定是在抽象的实现类中，所以肯定是在ContainerBase中实现。

- 初始化

- Lifecycle模板方法

- 重点是**backgroundProcess方法**

看下相关链路
![](/imported/markdown/2026-05-17-markdown-26dc9731-tomcat-container的管道机制-责任链模式/images/3e5b8b8c70b8-202603082048605.jpeg)
## [对比下两种责任链模式](#对比下两种责任链模式)
管道/阀门过滤器链/过滤器管道（Pipeline）过滤器链（FilterChain）阀门（Valve）过滤器（Filter）底层实现为具有头（first）、尾（basic）指针的单向链表底层实现为数组Valve的核心方法invoke(request,response)Filter核心方法doFilter(request,response,chain)pipeline.getFirst().invoke(request,response)filterchain.doFilter(request,response)
