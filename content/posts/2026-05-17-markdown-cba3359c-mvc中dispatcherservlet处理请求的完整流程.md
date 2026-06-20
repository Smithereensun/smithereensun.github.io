{

  "title": "MVC中DispatcherServlet处理请求的完整流程",
  "has_date": true,
  "description": "整体流程 用户发送请求——&gt;DispatcherServlet：接收用户的请求：前端控制器收到请求后自己不进行处理，而是委托给其他的解析器进行 处理，作为统一访问点，进行全局的流程控制； DispatcherServlet——&gt;HandlerMapping：HandlerMapping ",
  "tags": [
    "框架",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/spring/mvc4-processofdispatcherservletprocessingrequests - MVC中DispatcherServlet处理请求的完整流程.md",
  "date": "2026-05-17"

}

## [整体流程](#整体流程)
![](/imported/markdown/2026-05-17-markdown-cba3359c-mvc中dispatcherservlet处理请求的完整流程/images/f593ee1d840d-202404281540071.png)

1. 用户发送请求——&gt;DispatcherServlet：接收用户的请求：前端控制器收到请求后自己不进行处理，而是委托给其他的解析器进行 处理，作为统一访问点，进行全局的流程控制；

1. DispatcherServlet——&gt;HandlerMapping：HandlerMapping 将会把请求映射为 HandlerExecutionChain 对象（包含一 个Handler 处理器（页面控制器）对象、多个HandlerInterceptor 拦截器）对象，通过这种策略模式，很容易添加新的映射策略；

1. DispatcherServlet——&gt;HandlerAdapter：HandlerAdapter 将会把处理器包装为适配器，从而支持多种类型的处理器， 即适配器设计模式的应用，从而很容易支持很多类型的处理器；

1. HandlerAdapter——&gt;处理器功能处理方法的调用：HandlerAdapter 将会根据适配的结果调用真正的处理器的功能处理方法（也就是执行所有注册拦截器的preHandler方法），完成功能处理；并返回一个ModelAndView 对象（包含模型数据、逻辑视图名）；

1. 倒序执行所有注册拦截器的postHandler方法

1. ModelAndView 的逻辑视图名——&gt; ViewResolver：ViewResolver 将把逻辑视图名解析为具体的View，通过这种策略模式，很容易更换其他视图技术；

1. View——&gt;渲染：View 会根据传进来的Model 模型数据进行渲染，此处的Model 实际是一个Map 数据结构，因此 很容易支持其他视图技术；

1. 返回控制权给DispatcherServlet：由DispatcherServlet 返回响应给用户，到此一个流程结束

## [源码解析](#源码解析)

### [doGet入口](#doget入口)

HttpServlet处理get请求是doGet方法，所以要去找DispatcherServlet类结构中的doGet方法。

processRequest处理请求的方法如下：

本质上就是调用doService方法，由DispatchServlet类实现

### [请求分发](#请求分发)

doDispatch方法是真正处理请求的核心方法

### [①映射和适配器处理](#_1映射和适配器处理)

对于真正的handle方法，我们看下其处理流程

交给handleInternal方法处理，以RequestMappingHandlerAdapter这个HandlerAdapter中的处理方法为例

然后执行invokeHandlerMethod这个方法，用来对RequestMapping（usercontroller中的list方法）进行处理

### [②视图渲染](#_2视图渲染)

接下来继续执行processDispatchResult方法，对视图和model（如果有异常则对异常处理）进行处理（显然就是渲染页面了）

接下来显然就是渲染视图了, spring在initStrategies方法中初始化的组件（LocaleResovler等）就派上用场了。

后续就是通过viewResolver进行解析了，这里就不再继续看代码了，上述流程基本上够帮助你构建相关的认知了。

最后无非是返回控制权给DispatcherServlet，由DispatcherServlet 返回响应给用户。

最后的最后我们看下请求的日志：

## [总结](#总结)
