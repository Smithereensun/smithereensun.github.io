{

  "title": "Tomcat - Server的设计和实现：StandardServer",
  "has_date": true,
  "description": "理解思路 第一：抓住StandardServer整体类依赖结构来理解** 第二：结合server.xml来理解** 见下文具体阐述。 第三：结合Server Config官方配置文档** http://tomcat.apache.org/tomcat-9.0-doc/config/server.ht",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-server - Tomcat - Server的设计和实现：StandardServer.md",
  "date": "2026-04-19"

}

## [理解思路](#理解思路)

- **第一：抓住StandardServer整体类依赖结构来理解**

![](/imported/markdown/2026-04-19-markdown-513f610f-tomcat-server的设计和实现-standardserver/images/a02a3cd51282-202603082024048.jpeg)

- **第二：结合server.xml来理解**

见下文具体阐述。

- **第三：结合Server Config官方配置文档**

[http://tomcat.apache.org/tomcat-9.0-doc/config/server.html](http://tomcat.apache.org/tomcat-9.0-doc/config/server.html)

## [Server结构设计](#server结构设计)

我们需要从高一点的维度去理解Server的结构设计，而不是多少方法多少代码；这里的理解一定是要结合Server.xml对应理解。

### [server.xml](#server-xml)

- 首先要看下server.xml，这样你便知道了需要了解的四个部分

### [Server中的接口设计](#server中的接口设计)

- **公共属性**, 包括上面的port，shutdown, address等

属性描述className使用的Java类名称。此类必须实现org.apache.catalina.Server接口。如果未指定类名，则将使用标准实现。address该服务器等待关闭命令的TCP / IP地址。如果未指定地址，localhost则使用。port该服务器等待关闭命令的TCP / IP端口号。设置为-1禁用关闭端口。注意：当使用Apache Commons Daemon启动Tomcat （在Windows上作为服务运行，或者在un * xes上使用jsvc运行）时，禁用关闭端口非常有效。但是，当使用标准shell脚本运行Tomcat时，不能使用它，因为它将阻止shutdown.batportOffset应用于port和嵌套到任何嵌套连接器的端口的偏移量。它必须是一个非负整数。如果未指定，0则使用默认值。shutdown为了关闭Tomcat，必须通过与指定端口号的TCP / IP连接接收的命令字符串。utilityThreads此service中用于各种实用程序任务（包括重复执行的线程）的线程数。特殊值0将导致使用该值 Runtime.getRuntime().availableProcessors()。Runtime.getRuntime().availableProcessors() + value除非小于1，否则将使用负值， 在这种情况下将使用1个线程。预设值是1。

- NamingResources

- Service相关， 包括添加Service， 查找Service，删除service等

## [StandardServer的实现](#standardserver的实现)

### [线程池](#线程池)

### [Service相关方法实现](#service相关方法实现)

里面的方法都很简单。

### [Lifecycle相关模板方法](#lifecycle相关模板方法)

这里只展示startInternal方法

方法的第一行代码先触发 CONFIGURE_START_EVENT 事件，以便执行 StandardServer 的 LifecycleListener 监听器，然后调用 setState 方法设置成 LifecycleBase 的 state 属性为 LifecycleState.STARTING。 接着就 globalNamingResources.start()，跟 initInternal 方法其实是类似的。

再接着就调用 Service 的 start 方法来启动 Service 组件。可以看出，StandardServe 的 startInternal 跟 initInternal 方法类似，都是调用内部的 service 组件的相关方法。

调用完 service.init 方法后，就使用 getUtilityExecutor() 返回的线程池延迟执行startPeriodicLifecycleEvent 方法，而在 startPeriodicLifecycleEvent 方法里，也是使用 getUtilityExecutor() 方法，定期执行 fireLifecycleEvent 方法，处理 Lifecycle.PERIODIC_EVENT 事件，如果有需要定期处理的，可以再 Server 的 LifecycleListener 里处理 Lifecycle.PERIODIC_EVENT 事件。
