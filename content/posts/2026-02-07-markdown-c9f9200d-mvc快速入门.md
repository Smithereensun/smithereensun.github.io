{

  "title": "MVC快速入门",
  "has_date": true,
  "description": "前言 什么是MVC MVC英文是Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计规范，本质上也是一种解耦。 Model**（模型）是应用程序中用于处理应用程序数据逻辑的部分。通常模型对象负责在数据库中存取数据。 V",
  "tags": [
    "框架",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/spring/mvc1-summary - MVC快速入门.md",
  "date": "2026-02-07"

}

## [前言](#前言)

### [什么是MVC](#什么是mvc)

MVC英文是Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，一种软件设计规范，本质上也是一种解耦。
![](/imported/markdown/2026-02-07-markdown-c9f9200d-mvc快速入门/images/cda5cc521245-202407212156709.png)

- **Model**（模型）是应用程序中用于处理应用程序数据逻辑的部分。通常模型对象负责在数据库中存取数据。

- **View**（视图）是应用程序中处理数据显示的部分。通常视图是依据模型数据创建的。

- **Controller**（控制器）是应用程序中处理用户交互的部分。通常控制器负责从视图读取数据，控制用户输入，并向模型发送数据。

### [什么是SpringMVC](#什么是springmvc)

而Spring Web MVC 则是一种基于Java 的实现了Web MVC 设计模式的请求驱动类型的轻量级Web 框架，即使用了MVC 架构模式的思想，将 web 层进行职责解耦，基于请求驱动指的就是使用请求-响应模型，框架的目的就是为了简化开 发，Spring Web MVC 也是要简化我们日常Web 开发的。

说白了，Spring MVC 就是 【接收请求】【响应数据】

Spring MVC 下一般把后端项目分为 Service 层（处理业务）、Dao 层（数据库操作）、Entity 层（实体类）、Controller 层(控制层，返回数据给前台页面)。

常用组件：

- 前端控制器（DispatcherServlet）：接收用户请求，给用户返回结果。

- 处理器映射器（HandlerMapping）：根据请求的url路径，通过注解或者xml配置，寻找匹配的Handler。

- 处理器适配器（HandlerAdapter）：Handler 的适配器，调用 handler 的方法处理请求。

- 处理器（Handler）：执行相关的请求处理逻辑，并返回相应的数据和视图信息，将其封装到ModelAndView对象中。

- 视图解析器（ViewResolver）：将逻辑视图名解析成真正的视图View。

- 视图（View）：接口类，实现类可支持不同的View类型（JSP、FreeMarker、Excel等）

## [MVC案例](#mvc案例)

### [基于webxml](#基于webxml)
![](/imported/markdown/2026-02-07-markdown-c9f9200d-mvc快速入门/images/fb1355e5dd69-202602011306237.png)
[示例源码点击这里](https://github.com//Spring-Demo/tree/master/07-spring-mvc-helloworld)

#### [maven引入](#maven引入)

#### [业务代码编写](#业务代码编写)

- entity的User类

- dao层

- service层

- controller层

#### [webapp下的web.xml](#webapp下的web-xml)

#### [springmvc.xml](#springmvc-xml)

web.xml中配置初始化参数contextConfigLocation，路径是classpath:springmvc.xml，因此文件直接创建在resources目录下

#### [JSP视图](#jsp视图)

创建userList.jsp

之后就是使用tomcat部署测试了，这块就不说了

### [纯注解版](#纯注解版)

无需配置xml文件，依靠注解和配置类完成配置，注意需要注意满足sevlet3.0规范

具体源码[点击这里](https://github.com//Spring-Demo/tree/master/08-spring-mvc-helloworld-anno)

这个不做过多讲解，真实项目的用得较少。因为若是老项目，就是基于webxml的，若是新项目，则直接上springboot了。

## [Spring MVC响应请求](#spring-mvc响应请求)

### [直接返回ModelAndView对象](#直接返回modelandview对象)

ModelAndView对象将数据模型和视图信息封装在一起。

### [返回视图名称（页面跳转）](#返回视图名称-页面跳转)

该方法返回 `"userDetail.jsp"`，并可以在页面上通过 `${user}`获取数据

### [使用Map传递数据](#使用map传递数据)

该方法返回 `"userDetail.jsp"`，并可以在页面上通过 `${user}`获取数据

### [返回void](#返回void)

这种方式绕过了SpringMVC的视图解析，提供了最大灵活性，但需要自行处理响应细节，与Servlet API耦合度高，一般不推荐作为主要方式

### [重定向跳转](#重定向跳转)

redirect:会让浏览器地址栏变为新的URL。注意，重定向是两次请求，原始请求域（request scope）中的数据会丢失。若要传递参数，可使用 RedirectAttributes

### [使用HttpServletResponse](#使用httpservletresponse)

此方式适用于文件下载、输出特定二进制内容等需要精细控制输出流的场景。它完全绕过了SpringMVC的视图解析机制

### [直接返回数据（如JSON）](#直接返回数据-如json)

@ResponseBody注解是核心，它告诉Spring将方法返回值直接写入响应流。若项目中配置了消息转换器（如Jackson），可直接返回对象，Spring会自动将其转为JSON

## [SringMVC接收数据](#sringmvc接收数据)

### [基本数据类型接收](#基本数据类型接收)

### [接收路径参数](#接收路径参数)

### [对象接收（自动绑定）](#对象接收-自动绑定)

#### [接收简单对象参数](#接收简单对象参数)

#### [接收嵌套对象参数](#接收嵌套对象参数)

### [数组接收](#数组接收)

数组在表单中的应用

### [集合接收（通过包装对象）](#集合接收-通过包装对象)

SpringMVC 不能直接在方法参数中接收集合，但可以通过对象包装的方式来接收。

### [自定义转换器](#自定义转换器)

- 日期格式转换器

- 枚举类型转换器

- 注册自定义转换器

- 在控制器中使用自定义转换

## [SpringMVC其它使用](#springmvc其它使用)

### [视图解析器添加前后缀](#视图解析器添加前后缀)

配置视图解析器可以免去重复书写视图文件路径的前后缀。

- xml 或者Java Config

- 控制器代码

此配置后，控制器返回的 `"index"`会被自动补全为 `/views/index.jsp`，极大简化了视图管理

### [中文乱码问题处理](#中文乱码问题处理)

### [静态资源处理](#静态资源处理)

默认情况下，DispatcherServlet 会拦截所有请求，包括静态资源请求，这会导致静态资源无法正常访问。因此，我们需要配置 Spring MVC 以允许容器直接提供静态资源。

有两种主要方式来处理静态资源：

1. 使用 `&lt;mvc:resources /&gt;`标签（XML 配置）

1. 使用 `WebMvcConfigurer`的 `addResourceHandlers`方法（Java 配置）

另外，还可以使用 `&lt;mvc:default-servlet-handler /&gt;`来允许容器默认的 Servlet 处理静态资源。

- XML 配置方式-使用默认Servlet处理（简单方式）

- XML 配置方式-使用资源映射（推荐方式）

- JavaConfig 配置方式
