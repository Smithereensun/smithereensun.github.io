{

  "title": "Tomcat - 事件的监听机制：观察者模式",
  "has_date": true,
  "description": "Lifecycle中出现的监听器 （老的版本中是LifecycleSupport接口） 多个组件中出现监听器** 对应到整体架构图中 对应到代码中 知识准备 理解上述监听器的需要你有些知识储备，一是设计模式中的观察者模式，另一个是事件监听机制。 观察者模式 观察者模式(observer patter",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-listener - Tomcat - 事件的监听机制：观察者模式.md",
  "date": "2026-04-19"

}

## [Lifecycle中出现的监听器](#lifecycle中出现的监听器)

（老的版本中是LifecycleSupport接口）

- **多个组件中出现监听器**

对应到整体架构图中
![](/imported/markdown/2026-04-19-markdown-c8ae95c5-tomcat-事件的监听机制-观察者模式/images/c1523f3e2b14-202603082018363.jpeg)
对应到代码中
![](/imported/markdown/2026-04-19-markdown-c8ae95c5-tomcat-事件的监听机制-观察者模式/images/fb58920c9600-202603082018279.jpeg)
## [知识准备](#知识准备)

理解上述监听器的需要你有些知识储备，一是设计模式中的观察者模式，另一个是事件监听机制。

### [观察者模式](#观察者模式)

观察者模式(observer pattern): 在对象之间定义一对多的依赖, 这样一来, 当一个对象改变状态, 依赖它的对象都会收到通知, 并自动更新

主题(Subject)具有注册和移除观察者、并通知所有观察者的功能，主题是通过维护一张观察者列表来实现这些操作的。

观察者(Observer)的注册功能需要调用主题的 registerObserver() 方法。
![](/imported/markdown/2026-04-19-markdown-c8ae95c5-tomcat-事件的监听机制-观察者模式/images/02ced1d60f35-202603082019726.png)
详情请参考 设计模式：行为型 - 观察者(Observer)

### [事件监听机制](#事件监听机制)

JDK 1.0及更早版本的事件模型基于职责链模式，但是这种模型不适用于复杂的系统，因此在JDK 1.1及以后的各个版本中，事件处理模型采用基于观察者模式的委派事件模型(DelegationEvent Model, DEM)，即一个Java组件所引发的事件并不由引发事件的对象自己来负责处理，而是委派给独立的事件处理对象负责。这并不是说事件模型是基于Observer和Observable的，事件模型与Observer和Observable没有任何关系，Observer和Observable只是观察者模式的一种实现而已。

java中的事件机制的参与者有**3种角色**

- `Event Eource`：事件源，发起事件的主体。

- `Event Object`：事件状态对象，传递的信息载体，就好比Watcher的update方法的参数，可以是事件源本身，一般作为参数存在于listerner 的方法之中。

- `Event Listener`：事件监听器，当它监听到event object产生的时候，它就调用相应的方法，进行处理。

其实还有个东西比较重要：事件环境，在这个环境中，可以添加事件监听器，可以产生事件，可以触发事件监听器。
![](/imported/markdown/2026-04-19-markdown-c8ae95c5-tomcat-事件的监听机制-观察者模式/images/3a71ea68122c-202603082020179.png)
这个和观察者模式大同小异，但要比观察者模式复杂一些。一些逻辑需要手动实现，比如注册监听器，删除监听器，获取监听器数量等等，这里的eventObject也是你自己实现的。

下面我们看下Java中事件机制的实现，理解下面的类结构将帮助你Tomcat中监听机制的实现。

- 监听器

- 监听事件

- 事件源：

- 测试

## [Tomcat中监听机制（Server部分）](#tomcat中监听机制-server部分)

基于上面的事件监听的代码结构，你就能知道Tomcat中事件监听的类结构了。

- 首先要定义一个监听器，它有一个监听方法，用来接受一个监听事件

- 监听事件, 由于它是lifecycle的监听器，所以它握有一个lifecycle实例

- 事件源的接口和实现

事件源的接口：在Lifecycle中

事件源的实现： 在 LifecycleBase 中

- 接下来是调用了

比如在LifecycleBase, 停止方法是基于LifecycleState状态改变来触发上面的fireLifecycleEvent方法：
