{

  "title": "MVC中的拦截器实现案例",
  "has_date": true,
  "description": "MVC 拦截器 Spring MVC 拦截器对应HandlerInterctor接口，该接口位于org.springframework.web.servlet的包中，定义了三个方法，若要实现该接口，就要实现其三个方法： 前置处理（preHandle()方法）：该方法在执行控制器方法之前执行。返回值为",
  "tags": [
    "框架",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/spring/mvc2-Interceptor - MVC中的拦截器实现案例.md",
  "date": "2026-04-19"

}

## [MVC 拦截器](#mvc-拦截器)

Spring MVC 拦截器对应HandlerInterctor接口，该接口位于org.springframework.web.servlet的包中，定义了三个方法，若要实现该接口，就要实现其三个方法：

1. 前置处理（preHandle()方法）：该方法在执行控制器方法之前执行。返回值为Boolean类型，如果返回false，表示拦截请求，不再向下执行，如果返回true，表示放行，程序继续向下执行（如果后面没有其他Interceptor，就会执行controller方法）。所以此方法可对请求进行判断，决定程序是否继续执行，或者进行一些初始化操作及对请求进行预处理。

1. 后置处理（postHandle()方法）：该方法在执行控制器方法调用之后，且在返回ModelAndView之前执行。由于该方法会在DispatcherServlet进行返回视图渲染之前被调用，所以此方法多被用于处理返回的视图，可通过此方法对请求域中的模型和视图做进一步的修改。

1. 已完成处理（afterCompletion()方法）：该方法在执行完控制器之后执行，由于是在Controller方法执行完毕后执行该方法，所以该方法适合进行一些资源清理，记录日志信息等处理操作。

可以通过拦截器进行权限检验，参数校验，记录日志等操作

## [拦截器 (Interceptor) 实现案例](#拦截器-interceptor-实现案例)

拦截器（Interceptor）依赖于web框架，在SpringMVC中就是依赖于SpringMVC框架。在实现上,基于Java的反射机制，属于面向切面编程（AOP）的一种运用。

就是在service或者一个方法前，调用一个方法，或者在方法后，调用一个方法，比如**动态代理就是拦截器的简单实现**，在调用方法前打印出字符串（或者做其它业务逻辑的操作）。

也可以在调用方法后打印出字符串，甚至在抛出异常的时候做业务逻辑的操作。由于拦截器是基于web框架的调用，因此可以使用Spring的依赖注入（DI）进行一些业务操作，同时一个拦截器实例在一个controller生命周期之内可以多次调用。

但是缺点是只能对controller请求进行拦截，对其他的一些比如直接访问静态资源的请求则没办法进行拦截处理。

### [自定义拦截器实现](#自定义拦截器实现)

### [拦截器配置](#拦截器配置)

## [过滤器 (Filter) 实现案例](#过滤器-filter-实现案例)

过滤器 (Filter) 依赖于servlet容器。在实现上，基于函数回调，它可以对几乎所有请求进行过滤，但是缺点是一个过滤器实例只能在容器初始化时调用一次。

使用过滤器的目的，是用来做一些过滤操作，获取我们想要获取的数据。

比如：在Javaweb中，对传入的request、response提前过滤掉一些信息，或者提前设置一些参数，然后再传入servlet或者Controller进行业务逻辑操作。

通常用的场景是：在过滤器中修改字符编码（CharacterEncodingFilter）、在过滤器中修改HttpServletRequest的一些参数（XSSFilter(自定义过滤器)）。

如：过滤低俗文字、危险字符等。

### [自定义过滤器实现](#自定义过滤器实现)

### [过滤器配置（多种方式）](#过滤器配置-多种方式)

- 使用 @Component + @Order（推荐）： 上面的示例已经使用这种方式

- 使用 FilterRegistrationBean（更灵活）

- 使用 @WebFilter 注解

需要在启动类添加 `@ServletComponentScan`：

## [MVC 的Interctor和 Filter 过滤器的区别](#mvc-的interctor和-filter-过滤器的区别)

- 功能相同：Interctor和 Filter 都能实现相应的功能

- 容器不同：Interctor构建在 Spring MVC 体系中；Filter 构建在 Servlet 容器之上

- 拦截内容不同：Filter对所有访问进行增强，Interctor仅对MVC访问进行增强

- 使用便利性不同：Interctor提供了三个方法，分别在不同的时机执行；过滤器仅提供一个方法

### [使用场景区别](#使用场景区别)

- 使用拦截器的场景：

  - **业务逻辑处理**：权限验证、日志记录、参数预处理

  - **需要访问Spring上下文**：需要注入Spring Bean的业务

  - **控制器相关处理**：只需要对Spring MVC管理的请求进行处理

  - **需要修改ModelAndView**：在视图渲染前修改模型数据

- 使用过滤器的场景：

  - **通用请求处理**：字符编码、CORS支持、压缩处理

  - **静态资源处理**：需要对所有请求（包括静态资源）进行处理

  - **底层请求处理**：需要在DispatcherServlet之前执行的逻辑

  - **请求/响应包装**：需要修改请求参数或响应内容

### [组合使用示例](#组合使用示例)

### [过滤器和拦截器执行顺序](#过滤器和拦截器执行顺序)

请求进入 → 过滤器预处理 → Spring MVC 核心处理 → 拦截器预处理 → 控制器执行 → 拦截器后处理 → 拦截器完成处理 → 过滤器后处理 → 响应返回
![](/imported/markdown/2026-04-19-markdown-c49d1af3-mvc中的拦截器实现案例/images/cfba57dbbcc2-202602042323295.png)
详细执行步骤分解：

第一阶段：过滤器预处理（Filter Pre-processing）

1. **进入过滤器**：客户端请求首先到达 Servlet 容器

1. **执行 `chain.doFilter(request, response)`之前的逻辑**：

  - 对请求进行通用预处理

  - 常见操作：设置字符编码、添加 CORS 头部、安全检查、请求日志记录

  - **此时尚未进入 Spring MVC 框架**

第二阶段：Spring MVC 核心分发

1. **Servlet 的 `service()`方法**：请求进入 Servlet 容器处理流程

1. **Spring MVC 的 `doService()`方法**：Spring MVC 框架开始接管请求

1. **Spring MVC 请求分发方法**：`DispatcherServlet`根据 URL 映射确定对应的处理器（Handler）

第三阶段：拦截器预处理

1. **进入拦截器**：请求正式进入 Spring MVC 的拦截器链

1. **执行 `Controller`之前调用 `preHandle()`**：

  - 进行**业务相关**的预处理

  - 常见操作：用户认证、权限检查、参数验证、业务日志

  - 返回值控制：

    - `true`：继续执行后续拦截器和控制器

    - `false`：中断请求，直接返回

第四阶段：控制器执行

- 执行具体的业务逻辑

- 准备模型数据（Model）

- 确定视图信息（View）

第五阶段：拦截器后处理

1. **`postHandle()`方法执行**：

  - **时机**：控制器逻辑执行完毕，但在返回 `ModelAndView`之前

  - **能力**：可以查看和修改控制器返回的 `ModelAndView`对象

  - 常见操作：添加全局模型数据、记录处理结果、统一响应格式

第六阶段：拦截器完成处理，**`afterCompletion()`方法执行**：

- **时机**：控制器已经返回 `ModelAndView`，但在过滤器将响应返回给客户端之前

- **特点**：无论请求成功还是异常，都会执行（类似 `finally`块）

- 常见操作：清理 ThreadLocal 资源、记录最终处理状态、性能监控

第七阶段：过滤器后处理，**`FilterAfter`逻辑执行**：

- **时机**：服务器端所有逻辑执行完成，准备将响应返回给客户端之前

- 常见操作：响应压缩、添加安全头部、响应日志记录、编码最后确认

### [多拦截器执行顺序](#多拦截器执行顺序)

- 当配置多个拦截器时，会形成拦截器链

- 拦截器的运行顺序参照拦截器添加顺序为准，即addInterctor的顺序（过滤器同理）

- 当拦截器中出现对原始处理器的拦截，后面的拦截器均终止运行

- 当拦截器运行中断，仅运行配置在前面的拦截器afterCompletion

流程解析看下图：
