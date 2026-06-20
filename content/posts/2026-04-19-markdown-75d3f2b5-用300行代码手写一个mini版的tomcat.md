{

  "title": "用300行代码手写一个mini版的Tomcat",
  "has_date": true,
  "description": "Tomcat 是 Java Web 开发的基石。我们天天使用它，但你是否思考过它内部是如何工作的？为了打破这个“黑盒”，最好的方式就是动手实现一个极度精简的核心。本项目 “TinyTomcat” 的目标，就是**用大约 300 行纯 Java 代码，实现一个能够解析 HTTP 请求、路由到对应处理逻",
  "tags": [
    "框架",
    "Web"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/web/tomcat-source300 - 用300行代码手写一个mini版的Tomcat.md",
  "date": "2026-04-19"

}

Tomcat 是 Java Web 开发的基石。我们天天使用它，但你是否思考过它内部是如何工作的？为了打破这个“黑盒”，最好的方式就是动手实现一个极度精简的核心。本项目 “TinyTomcat” 的目标，就是**用大约 300 行纯 Java 代码，实现一个能够解析 HTTP 请求、路由到对应处理逻辑并返回响应的微型服务器**。通过这个过程，你将透彻理解 Tomcat 处理请求的**本质**：监听端口、解析协议、调度响应。

所以，我们的目标是：

1. 监听一个端口（比如8080），接受HTTP请求。

1. 解析HTTP请求，至少能解析请求的URL和方法（GET、POST等）。

1. 根据请求的URL，找到对应的处理逻辑（类似于Servlet），并返回响应。

1. 响应基本的HTTP格式，包括状态行、头部和响应体。

## [核心设计思路](#核心设计思路)

一个基础的 HTTP 服务器，无论规模大小，其核心流程都可以抽象为下图所示的步骤：

基于这个流程，我们设计出五个核心类，共同完成了上图的闭环：

1. **SimpleTomcat (服务器引擎)**：这是大脑，负责启动、监听端口，并协调所有工作。

1. **SimpleRequest (请求解析器)**：这是翻译官，将原始的、文本格式的 HTTP 请求解析成程序容易理解的 Java 对象。

1. **SimpleResponse (响应构建器)**：这是包装工，负责将我们的处理结果，包装成符合 HTTP 协议格式的字节流。

1. **SimpleServlet (处理接口)**：这是业务合同，定义了所有动态处理器（Servlet）必须遵守的规范。

1. **HelloServlet (业务实现)**：这是我们的一个具体业务逻辑例子。

## [构建服务器引擎 (SimpleTomcat.java)](#构建服务器引擎-simpletomcat-java)

这个类是程序的起点，也是调度中心。其核心逻辑在 `start()`和 `handleClient`方法中。

- **多线程处理**。我们使用 `ExecutorService`线程池来处理每一个客户端连接 (`Socket`)，这是服务器能同时服务多个请求的基础，避免了单线程阻塞。

- **路由分发**。在 `handleClient`方法中，我们读取请求的第一行（如 `GET /hello HTTP/1.1`），解析出请求路径，然后根据一个预设的“路由表” (`servletMapping`) 来决定将这个请求派发给谁处理。这模仿了 Tomcat 中 `web.xml`或注解配置的 Servlet 映射机制。

- **区分动态与静态**。我们的路由逻辑区分了三种情况：访问根路径返回欢迎页、访问注册的 Servlet 路径则动态处理、其他路径则尝试查找静态文件
 ​

## [解析 HTTP 请求 (SimpleRequest.java)](#解析-http-请求-simplerequest-java)

HTTP 请求本质上是按特定格式组织的文本。`SimpleRequest`类的任务就是解析它。

- **解析请求行**。构造函数中，通过 `requestLine.split(" ")`可以得到方法、路径和协议版本

- **解析查询参数**。在 `parseQueryString`方法中，我们处理 URL 中 `?`后面的部分（如 `name=Bob&age=25`），将其拆解成键值对，存入 `params`映射，这样 Servlet 中就能通过 `getParameter("name")`获取值。

- **解析请求头**。通过循环读取输入流直到空行，将 `HeaderName: HeaderValue`这样的行解析后存入 `headers`映射。虽然我们的迷你版没有用到所有头部信息，但这种设计为后续扩展（如处理 Cookie、Session）留出了空间。

## [构建 HTTP 响应 (SimpleResponse.java)](#构建-http-响应-simpleresponse-java)

与解析请求相对，我们需要构建一个格式正确的 HTTP 响应。HTTP 响应由状态行、响应头和响应体三部分组成。

-
**延迟发送头**。我们设置了 `headersSent`标志位。这是因为在业务代码（Servlet）中，可能会先设置状态、内容类型等头部信息，再输出响应体。`getWriter()`或 `getOutputStream()`方法会**在第一次被调用时**，自动将所有已设置的头部信息发送出去（`sendHeaders`方法），这是一个巧妙的设计，确保了头部先于身体发送。

-
**头部格式**。在 `sendHeaders`方法中，我们严格按照 `HTTP/1.1 200 OK\r\nHeader: Value\r\n\r\n`的格式拼接字符串。注意最后的空行 `\r\n\r\n`，它是分隔头部和身体的关键标记。

## [定义处理契约 (SimpleServlet.java)](#定义处理契约-simpleservlet-java)

为了支持灵活的动态处理，我们定义了极简的 `SimpleServlet`接口。它只有一个 `service`方法，接受请求和响应对象。这模仿了标准 Servlet 的 `service`方法，是设计模式中**策略模式**​ 的体现。我们可以为不同路径（如 `/hello`, `/time`）注册不同的实现类，服务器引擎无需关心具体逻辑，只需调用其 `service`方法即可

## [实现业务逻辑 (HelloServlet.java)](#实现业务逻辑-helloservlet-java)

HelloServlet是我们契约的一个具体实现。实现的步骤是：

1. 从 SimpleRequest对象中获取用户参数（req.getParameter("name")）。

1. 通过 SimpleResponse对象设置内容类型。

1. 通过 res.getWriter()获得输出流，生成动态的 HTML 内容。

这个 Servlet 就像一个简单的控制器（Controller），它处理业务（组合问候语和当前时间），并渲染视图（生成 HTML 页面）。

## [总结](#总结)

我们这个 TinyTomcat 虽然简单，但基本已经有了Tomcat的的核心骨架。真正的 Tomcat 正是在此基础上，在各个维度进行了史诗级的增强：

- **性能与并发**：使用 NIO/AIO 连接器、更精细的线程池、缓存机制。

- **配置与可扩展性**：通过 `server.xml`, `web.xml`, 注解等方式进行复杂配置，支持 Valve、Filter 等扩展链。

- **安全**：实现安全管理器、 Realm 域认证。

- **生命周期与容器**：实现完整的 `Lifecycle`接口，管理 Server、Service、Engine、Host、Context、Wrapper 等层次化容器。

- **协议支持**：支持 HTTP/1.1、HTTP/2，甚至 AJP 协议。

- **会话管理**：实现复杂而强大的 Session 创建、跟踪、持久化机制。

- **异步处理**：支持 Servlet 3.0+ 的异步 I/O 处理。

接下来，我将会继续从源码角度介绍 Tomcat 的核心设计，可以持续关注
