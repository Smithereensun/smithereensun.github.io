{

  "title": "MVC中DispatcherServlet初始化的深度探索",
  "has_date": true,
  "description": "概述 DispatcherServlet首先是Sevlet，Servlet有自己的生命周期的方法（init,destory等），那么在看DispatcherServlet初始化时首先需要看源码中DispatcherServlet的类结构设计。 首先我们看DispatcherServlet的类结构关系",
  "tags": [
    "框架",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/spring/mvc3-initializationprocessofdispatcherservlet - MVC中DispatcherServlet初始化的深度探索.md",
  "date": "2026-05-17"

}

## [概述](#概述)

DispatcherServlet首先是Sevlet，Servlet有自己的生命周期的方法（init,destory等），那么在看DispatcherServlet初始化时首先需要看源码中DispatcherServlet的类结构设计。

首先我们看DispatcherServlet的类结构关系，在这个类依赖结构中找到init的方法
![](/imported/markdown/2026-05-17-markdown-48371109-mvc中dispatcherservlet初始化的深度探索/images/cec8bd16993c-202404281539257.png)
## [核心方法](#核心方法)

### [init](#init)

init()方法如下, 主要读取web.xml中servlet参数配置，并将交给子类方法initServletBean()继续初始化

读取配置可以从下图看出，正是初始化了我们web.xml中配置
![](/imported/markdown/2026-05-17-markdown-48371109-mvc中dispatcherservlet初始化的深度探索/images/188f730b877c-202404281539895.png)
再看下initServletBean()方法，位于FrameworkServlet类中

### [initWebApplicationContext](#initwebapplicationcontext)

initWebApplicationContext用来初始化和刷新WebApplicationContext。

这个方法主要做了以下几步：

1. 从ServletContext中获取第一步中创建的SpringMVC根上下文，为下面做准备

1. 根据init-param中的contextAttribute属性值从ServletContext查找是否存在上下文对象

1. 以XmlWebApplicationContext作为Class类型创建上下文对象，设置父类上下文，并完成刷新

1. 执行子类扩展方法onRefresh，在DispatcherServlet内初始化所有web相关组件

1. 将servlet子上下文对象发布到ServletContext

org.springframework.web.servlet.FrameworkServlet#initWebApplicationContext() 方法如下

webApplicationContext只会初始化一次，依次尝试构造函数初始化，没有则通过contextAttribute初始化，仍没有则创建新的

createWebApplicationContext方法创建SpringMVC的应用上下文，并调用configureAndRefreshWebApplicationContext方法进行上下文的刷新。创建的createWebApplicationContext方法如下

configureAndRefreshWebApplicationContext会先将新创建的这个上下文与servletcontext绑定，然后进行刷新操作，这个刷新操作就IOC的执行过程一样，configureAndRefreshWebApplicationContext方法初始化设置Spring环境

到这一步为止，就创建了3个context，分别为：

1. ServletContext：全局唯一，tomcat启动该web项目了创建

1. Spring的context：由servletcontext的监听器contextloaderlistener创建，默认读取servletcontext.xml配置，具体内容参考我们之前介绍的IOC的源码实现。同时该cntext与servletcontext互相关联，该context被注册到servletcontext中以webapplicationcontext属性存在。

1. SpringMVC的context：SpringMVC初始化DispacherServlet时创建的上下文，该context为Spring的context的子容器，可以访问Spring容器中的内容（子容器可以访问父容器中的内容，但是反过来不行）。

经过上面两个步骤，DispatcherServlet父类中的流程已经全部走完，这几个步骤主要的功能就是生成了SpringMVC容器，并将其与ServletContext、Spring容器相关联。

### [refresh](#refresh)

有了webApplicationContext后，就开始刷新了（onRefresh()方法），这个方法是FrameworkServlet提供的模板方法，由子类DispatcherServlet来实现的。

刷新主要是调用initStrategies(context)方法对DispatcherServlet中的组件进行初始化，这些组件就是在SpringMVC请求流程中包的主要组件。

### [initHanlderxxx](#inithanlderxxx)

主要看initHandlerXXX相关的方法，它们之间的关系可以看SpringMVC的请求流程：
![](/imported/markdown/2026-05-17-markdown-48371109-mvc中dispatcherservlet初始化的深度探索/images/0d30fb08b998-202404281540287.png)

1. HandlerMapping 是映射处理器

1. HandlerAdpter是**处理适配器**，它用来找到你的Controller中的处理方法

1. HandlerExceptionResolver是当遇到处理异常时的异常解析器

#### [initMultipartResolver](#initmultipartresolver)

文件的上传请求，则需要使用MultipartResolver
![](/imported/markdown/2026-05-17-markdown-48371109-mvc中dispatcherservlet初始化的深度探索/images/fc4152e55e5f-202602011305916.png)
#### [initHandlerMapping](#inithandlermapping)

该方法负责进行HandlerMapping接口实现类的加载。HandlerMapping接口主要用来提供request 请求对象和Handler对象 映射关系的接口。所谓request对象比如web应用中的http 请求，Handler对象则指的是对应rquest请求的相关处理逻辑。

首先判断是否查找所有HandlerMapping(默认为true)。如果为是，则从上下文(包括所有父上下文)中查询类型为HandlerMapping的Bean,并进行排序。如果为否，则从上下文中按指定名称去寻找。如果都没有找到，提供一个默认的实现。这个默认实现从DispatcherServlet同级目录的DispatcherServlet.properties中加载的。

initHandlerMapping方法如下，无非就是获取按照优先级排序后的HanlderMappings, 将来匹配时按照优先级最高的HanderMapping进行处理
![](/imported/markdown/2026-05-17-markdown-48371109-mvc中dispatcherservlet初始化的深度探索/images/405915f59912-202602011033351.png)
initHandlerMapping 没有找到自定义配置的，则构建默认的。默认值在
 DispatcherServlet.properties 文件中，九大组件均有默认值
![](/imported/markdown/2026-05-17-markdown-48371109-mvc中dispatcherservlet初始化的深度探索/images/3a15b2be0495-202602011034305.png)
#### [initHandlerAdapters](#inithandleradapters)

通过initHandlerMappings已经将request通过HandlerMapping(处理器映射器)将请求映射到了对应的Handler上，这一步就需要考虑如何解析并执行该handler对象。

initHandlerAdapters方法和initHandlerExceptionResolvers方法也是类似的，如果没有找到，那就构建默认的。

这里Spring使用了适配器模式，主要是因为handler对象有两种不同的类型。

最后看下初始化的日志：

## [总结](#总结)

整体流程如下图：
![](/imported/markdown/2026-05-17-markdown-48371109-mvc中dispatcherservlet初始化的深度探索/images/04905b8cfe85-202404281540503.png)
初始化整体流程如下：

1. 加载配置文件：Spring MVC的配置文件一般为 XML 格式，通过 ApplicationContext 来加载配置文件，获取相关的bean。

1. 初始化 DispatcherServlet：DispatcherServlet 是整个 Spring MVC 的核心，它继承了 HttpServlet，实现了对 HTTP 请求的处理和响应。在初始化 DispatcherServlet 时，会调用其 init() 方法，并且为其设置一些参数，例如 SpringMVC 配置文件的位置等。

1. 初始化 HandlerMapping：HandlerMapping负责将请求映射到相应的Controller上，DispatcherServlet在初始化时会初始化HandlerMapping，并将其注册到自己的属性中。

1. 初始化 HandlerAdapter：HandlerAdapter 用于将请求对象转换成 ModelAndView 对象。在初始化时，DispatcherServlet 会根据 HandlerMapping 获取相应的 Controller，并生成相应的 HandlerAdapter。

1. 初始化 ViewResolver：ViewResolver 用于将 ModelAndView 对象渲染成具体的视图（如JSP、HTML等）。在初始化时，DispatcherServlet 会根据 ViewResolver 的配置，生成相应的ViewResolver 对象。

1. 启动 Spring MVC：DispatcherServlet 在初始化完成后，就可以监听HTTP请求，并将请求分发到相应的 Controller上 进行处理。处理完成后，将 ModelAndView 对象交给 ViewResolver 进行渲染。
