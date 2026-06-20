{

  "title": "Tomcat - Service的设计和实现：StandardService",
  "has_date": true,
  "description": "理解思路 第一：类比StandardServer, 抓住StandardService整体类依赖结构来理解** 第二：结合server.xml中service配置来理解** 见下文具体阐述。 第三：结合Service Config官方配置文档** http://tomcat.apache.org/t",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-service - Tomcat - Service的设计和实现：StandardService.md",
  "date": "2026-04-19"

}

## [理解思路](#理解思路)

- **第一：类比StandardServer, 抓住StandardService整体类依赖结构来理解**

![](/imported/markdown/2026-04-19-markdown-5048433a-tomcat-service的设计和实现-standardservice/images/78db47dfd787-202603082029193.jpeg)

- **第二：结合server.xml中service配置来理解**

见下文具体阐述。

- **第三：结合Service Config官方配置文档**

[http://tomcat.apache.org/tomcat-9.0-doc/config/service.html](http://tomcat.apache.org/tomcat-9.0-doc/config/service.html)

## [Service结构设计](#service结构设计)

我们需要从高一点的维度去理解service的结构设计，而不是多少方法多少代码；这里的理解一定是要结合Server.xml中service配置部分对应理解。

### [server.xml](#server-xml)

- 首先要看下server.xml中Service的配置，这样你便知道了需要了解的4个部分

### [Service中的接口设计](#service中的接口设计)

- **公共属性**, name等

- 父Server相关

- Connector相关

- Engine

- Excutor相关

## [StandardService的实现](#standardservice的实现)

属性和父Server相关比较简单，这里主要看下其它的方法：

### [Engine相关](#engine相关)

### [Connectors相关](#connectors相关)

### [Executor相关](#executor相关)

CRUD方法，代码比较简单

### [Lifecycle相关模板方法](#lifecycle相关模板方法)

首先看 **initInternal** 方法

initInternal 代码很短，思路也很清晰，就是依次调用了这个成员变量的 init 方法

**startInternal 方法**

startInternal 跟 initInternal 方法一样，也是依次调用

### [补充下MapperListener](#补充下mapperlistener)

mapperListener 的作用是在 start 的时候将容器类对象注册到 Mapper 对象中。

Mapper是 Tomcat 处理 Http 请求时非常重要的组件。Tomcat 使用 Mapper 来处理一个 Request 到 Host、Context 的映射关系，从而决定使用哪个 Service 来处理请求。

MapperListener 也是继承自 LifecycleMBeanBase，不过没有重载 initInternal 方法。

- startInternal 方法

- findDefaultHost() 方法

首先看 findDefaultHost() 方法

findDefaultHost() 是主要是找出 defaultHost，并调用 `mapper.setDefaultHostName(defaultHost);` 这个 defaultHost 是 server.xml 的 `&lt;Engine&gt;` 标签的属性，一般都是 "localHost"。

从上面代码 for 代码块里可以看出，Host 是 Engine 的子 Container。for 语句就是找出一个名字跟 defaultHost 指定的名字相同的 Host 对象。

- addListeners(engine) 方法

这个方法的作用是，将 MapperListener 这个监听器添加到 Engine 及其子容器中

- registerHost 调用 registerHost方法来注册 Engine 的字容器 Host。

registerHost 方法先调用 mapper.addHost，然后调用 registerContext 方法注册 Host 的子容器 Context。 mapper.addHost 方法是将 Host 加入的 Mapper 类的的成员变量MappedHost[] hosts 中。

接着看 registerContext 方法

registerContext 里先获取一些对象，比如 WebResourceRoot 对象、WrapperMappingInfo 对象，然后调用 mapper.addContextVersion。

Mapper#addContextVersion 方法比较琐细，就不细讲了。

其主要逻辑是将 Context 对象，以及 Context 的子容器 Wrapper 对象，每一个都分别构建一个对应的 MappedContext 和 MappedWrapper 对象，

然后把 MappedContext 和 MappedWrapper 塞进 ContextVersion 对象中，

最后把 Context 和 ContextVersion 的对应关系放在 Mapper 对象的一个 Map 里。

这里的 MappedContext 和 MappedWrapper 在 Tomcat 处理 Http 请求的时候是比较关键的。

registerHost 最后再更新了一下可能发生改变里的的 defaultHost。
