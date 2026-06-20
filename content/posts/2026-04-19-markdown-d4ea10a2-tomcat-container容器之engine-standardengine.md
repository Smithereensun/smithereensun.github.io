{

  "title": "Tomcat - Container容器之Engine：StandardEngine",
  "has_date": true,
  "description": "理解思路 第一：抓住StandardEngine整体类依赖结构来理解** 第二：结合server.xml中Engine配置来理解** 见下文具体阐述。 第三：结合Engine Config官方配置文档** http://tomcat.apache.org/tomcat-9.0-doc/config/",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-container-engine - Tomcat - Container容器之Engine：StandardEngine.md",
  "date": "2026-04-19"

}

## [理解思路](#理解思路)

- **第一：抓住StandardEngine整体类依赖结构来理解**

![](/imported/markdown/2026-04-19-markdown-d4ea10a2-tomcat-container容器之engine-standardengine/images/bc7633e2345e-202603082045545.jpeg)

- **第二：结合server.xml中Engine配置来理解**

见下文具体阐述。

- **第三：结合Engine Config官方配置文档**

[http://tomcat.apache.org/tomcat-9.0-doc/config/engine.html](http://tomcat.apache.org/tomcat-9.0-doc/config/engine.html)

## [Engine接口设计](#engine接口设计)

这看Engine.java接口前，先要看下相关属性

- 支持设置的属性列表

属性描述backgroundProcessorDelay此值表示在此引擎及其子容器（包括所有Host和Context）上调用backgroundProcess方法之间的延迟（以秒为单位）。如果子容器的延迟值不为负（则表示它们正在使用自己的处理线程），则不会调用它们。将此值设置为正值将导致产生线程。等待指定的时间后，线程将在此引擎及其所有子容器上调用backgroundProcess方法。如果未指定，则此属性的默认值为10，表示10秒的延迟。className使用的Java类名称。此类必须实现org.apache.catalina.Engine接口。如果未指定，将使用标准值（定义如下）。**defaultHost**默认的主机名，它标识Host将处理针对主机名此服务器上的请求，但在此配置文件中没有配置。此名称必须与嵌套在name 其中的Host元素之一的属性匹配。**jvmRoute**必须在负载平衡方案中使用的标识符才能启用会话亲缘关系。标识符（在参与集群的所有Tomcat服务器之间必须是唯一的）将附加到生成的会话标识符上，因此允许前端代理始终将特定会话转发到同一Tomcat实例。注意，jvmRoute也可以使用jvmRoutesystem属性设置 。属性中的`jvmRoute set&lt;Engine&gt;`将覆盖任何jvmRoute系统属性。name此引擎的逻辑名称，用于日志和错误消息。在同一台Server中使用多个Service元素时，必须为每个引擎分配一个唯一的名称。startStopThreads该引擎将用来并行启动子Host元素的线程数。特殊值0将导致使用该值 Runtime.getRuntime().availableProcessors()。Runtime.getRuntime().availableProcessors() + value除非小于1，否则将使用负值， 在这种情况下将使用1个线程。如果未指定，将使用默认值1。如果使用了1个线程，那么ExecutorService将使用当前线程，而不是使用。

- Engine的接口设计

这里你会发现，如下接口中包含上述defaultHost和jvmRoute属性设置；同时还有Service，因为Engine的上层是service。

- 其它属性支持都包含在我们上文分析的ContainerBase中

## [Engine接口实现：StandardEngine](#engine接口实现-standardengine)

### [接口中简单方法实现](#接口中简单方法实现)

上述接口里面的defaultHost, JvmRoute, service 很简单

### [child, parent](#child-parent)

`addChild`重载方法，限制只能添加Host作为子容器；

`setParent`直接抛出异常，因为Engine接口中已经包含了setService方法作为它的上层，而Engine的上层没有容器的概念。

### [Lifecycle的模板方法](#lifecycle的模板方法)

无非就是调用上文中我们介绍ContainerBase中的方法

### [LogAccess](#logaccess)

这里需要补充下之前没有介绍的**日志访问**，这里介绍下。

运行Web服务器时，**正常生成的输出文件之一是访问日志**，该访问日志以标准格式为服务器处理的每个请求生成一行信息。Catalina包括一个可选的Valve实现，该实现可以创建与Web服务器创建的标准格式相同的访问日志，也可以创建任意数量的自定义格式。

需要先看下xml配置; 您可以通过嵌套如下所示的Valve元素，要求Catalina为Engine， Host或Context处理的所有请求创建访问日志：

好了看下具体的实现，使用适配器模式获取AccessLog类型的Valve：

适配器模式看这里：结构型 - 适配器(Adapter)

AccessLog(日志记录器)主要的作用就是记录日志，这个记录的方法就是`logAccess()`方法

其中涉及的相关内部类如下：

### [JMX相关](#jmx相关)

之前已经有过相关介绍，这里不再介绍相关方法，只列出相关方法：
