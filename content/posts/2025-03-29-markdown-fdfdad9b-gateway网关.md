{

  "title": "Gateway网关",
  "has_date": true,
  "description": "Spring Cloud Gateway 项目是基于 Spring 5.0，Spring Boot 2.0 和 Project Reactor 等响应式编程和事件流技术开发的网关，它旨在为微服务架构提供一种简单有效的统一的 API 路由管理方式。 为什么需要网关 Gateway网关是我们服务的守门神",
  "tags": [
    "微服务"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/springcloud/gateway - Gateway网关.md",
  "date": "2025-03-29"

}

Spring Cloud Gateway 项目是基于 Spring 5.0，Spring Boot 2.0 和 Project Reactor 等响应式编程和事件流技术开发的网关，它旨在为微服务架构提供一种简单有效的统一的 API 路由管理方式。

## [为什么需要网关](#为什么需要网关)

Gateway网关是我们服务的守门神，所有微服务的统一入口。

网关的**核心功能特性**：

- 请求路由

- 权限控制

- 限流

架构图：
![](/imported/markdown/2025-03-29-markdown-fdfdad9b-gateway网关/images/0e53de26acff-202501011229678.png)

- **权限控制**：网关作为微服务入口，需要校验用户是是否有请求资格，如果没有则进行拦截。

- **路由和负载均衡**：一切请求都必须先经过gateway，但网关不处理业务，而是根据某种规则，把请求转发到某个微服务，这个过程叫做路由。当然路由的目标服务有多个时，还需要做负载均衡。

- **限流**：当请求流量过高时，在网关中按照下流的微服务能够接受的速度来放行请求，避免服务压力过大。

在SpringCloud中网关的实现包括两种：

- gateway

- zuul

Zuul是基于Servlet的实现，属于阻塞式编程。而SpringCloudGateway则是基于Spring5中提供的WebFlux，属于响应式编程的实现，具备更好的性能。

## [gateway快速入门](#gateway快速入门)

下面，我们就演示下网关的基本路由功能。基本步骤如下：

1. 创建SpringBoot工程gateway，引入网关依赖

1. 编写启动类

1. 编写基础配置和路由规则

1. 启动网关服务进行测试

### [引入依赖](#引入依赖)

### [编写启动类](#编写启动类)

### [编写基础配置和路由规则](#编写基础配置和路由规则)

创建application.yml文件，内容如下：

我们将符合`Path` 规则的一切请求，都代理到 `uri`参数指定的地址。

本例中，我们将 `/user/**`开头的请求，代理到`lb://userservice`，lb是负载均衡，根据服务名拉取服务列表，实现负载均衡。

### [重启测试](#重启测试)

重启网关，访问[http://localhost:10010/user/1时，符合`/user/**`规则，请求转发到uri：http://userservice/user/1，得到了结果：](http://localhost:10010/user/1%E6%97%B6%EF%BC%8C%E7%AC%A6%E5%90%88%60/user/**%60%E8%A7%84%E5%88%99%EF%BC%8C%E8%AF%B7%E6%B1%82%E8%BD%AC%E5%8F%91%E5%88%B0uri%EF%BC%9Ahttp://userservice/user/1%EF%BC%8C%E5%BE%97%E5%88%B0%E4%BA%86%E7%BB%93%E6%9E%9C%EF%BC%9A)
![](/imported/markdown/2025-03-29-markdown-fdfdad9b-gateway网关/images/a8b393f08699-202501011231024.png)
### [网关路由的流程图](#网关路由的流程图)

整个访问的流程如下：
![](/imported/markdown/2025-03-29-markdown-fdfdad9b-gateway网关/images/a26dec394589-202501011231026.png)
总结：

网关搭建步骤：

1.
创建项目，引入nacos服务发现和gateway依赖

1.
配置application.yml，包括服务基本信息、nacos地址、路由

路由配置包括：

1.
路由id：路由的唯一标示

1.
路由目标（uri）：路由的目标地址，http代表固定地址，lb代表根据服务名负载均衡

1.
路由断言（predicates）：判断路由的规则，

1.
路由过滤器（filters）：对请求或响应做处理

接下来，就重点来学习路由断言和路由过滤器的详细知识

## [断言工厂](#断言工厂)

我们在配置文件中写的断言规则只是字符串，这些字符串会被Predicate Factory读取并处理，转变为路由判断的条件

例如Path=/user/**是按照路径匹配，这个规则是由`org.springframework.cloud.gateway.handler.predicate.PathRoutePredicateFactory`类来处理的，像这样的断言工厂在SpringCloudGateway还有十几个:
**名称****说明****示例**After是某个时间点后的请求- After=2037-01-20T17:42:47.789-07:00[America/Denver]Before是某个时间点之前的请求- Before=2031-04-13T15:14:47.433+08:00[Asia/Shanghai]Between是某两个时间点之前的请求- Between=2037-01-20T17:42:47.789-07:00[America/Denver], 2037-01-21T17:42:47.789-07:00[America/Denver]Cookie请求必须包含某些cookie- Cookie=chocolate, ch.pHeader请求必须包含某些header- Header=X-Request-Id, \d+Host请求必须是访问某个host（域名）- Host=**.somehost.org,**.anotherhost.orgMethod请求方式必须是指定方式- Method=GET,POSTPath请求路径必须符合指定规则- Path=/red/{segment},/blue/**Query请求参数必须包含指定参数- Query=name, Jack或者- Query=nameRemoteAddr请求者的ip必须是指定范围- RemoteAddr=192.168.1.1/24Weight权重处理
我们只需要掌握Path这种路由工程就可以了。

## [过滤器工厂](#过滤器工厂)

GatewayFilter是网关中提供的一种过滤器，可以对进入网关的请求和微服务返回的响应做处理：
![](/imported/markdown/2025-03-29-markdown-fdfdad9b-gateway网关/images/ff07ce97357f-202501011231031.png)
### [路由过滤器的种类](#路由过滤器的种类)

Spring提供了31种不同的路由过滤器工厂。例如：
**名称****说明**AddRequestHeader给当前请求添加一个请求头RemoveRequestHeader移除请求中的一个请求头AddResponseHeader给响应结果中添加一个响应头RemoveResponseHeader从响应结果中移除有一个响应头RequestRateLimiter限制请求的流量
### [请求头过滤器](#请求头过滤器)

下面我们以AddRequestHeader 为例来讲解。

**需求**：给所有进入userservice的请求添加一个请求头：Truth= is freaking awesome!

只需要修改gateway服务的application.yml文件，添加路由过滤即可：

当前过滤器写在userservice路由下，因此仅仅对访问userservice的请求有效。

### [默认过滤器](#默认过滤器)

如果要对所有的路由都生效，则可以将过滤器工厂写到default下。格式如下：

### [总结](#总结)

过滤器的作用是什么？

1. 对路由的请求或响应做加工处理，比如添加请求头

1. 配置在路由下的过滤器只对当前路由的请求生效

defaultFilters的作用是什么？对所有路由都生效的过滤器

## [全局过滤器](#全局过滤器)

过滤器，网关提供了31种，但每一种过滤器的作用都是固定的。如果我们希望拦截请求，做自己的业务逻辑则没办法实现。

### [全局过滤器作用](#全局过滤器作用)

全局过滤器的作用也是处理一切进入网关的请求和微服务响应，与GatewayFilter的作用一样。区别在于GatewayFilter通过配置定义，处理逻辑是固定的；而GlobalFilter的逻辑需要自己写代码实现。

定义方式是实现GlobalFilter接口。

在filter中编写自定义逻辑，可以实现下列功能：

- 登录状态判断

- 权限校验

- 请求限流等

### [自定义全局过滤器](#自定义全局过滤器)

需求：定义全局过滤器，拦截请求，判断请求的参数是否满足下面条件：

- 参数中是否有authorization，

- authorization参数值是否为admin

如果同时满足则放行，否则拦截

实现：在gateway中定义一个过滤器：

### [过滤器执行顺序](#过滤器执行顺序)

请求进入网关会碰到三类过滤器：当前路由的过滤器、DefaultFilter、GlobalFilter

请求路由后，会将当前路由过滤器和DefaultFilter、GlobalFilter，合并到一个过滤器链（集合）中，排序后依次执行每个过滤器：
![](/imported/markdown/2025-03-29-markdown-fdfdad9b-gateway网关/images/ea1626375fbe-202501011231035.png)
排序的规则是什么呢？

- 每一个过滤器都必须指定一个int类型的order值，**order值越小，优先级越高，执行顺序越靠前**。

- GlobalFilter通过实现Ordered接口，或者添加@Order注解来指定order值，由我们自己指定

- 路由过滤器和defaultFilter的order由Spring指定，默认是按照声明顺序从1递增。

- 当过滤器的order值一样时，会按照 defaultFilter &gt; 路由过滤器 &gt; GlobalFilter的顺序执行。

详细内容，可以查看源码：

`org.springframework.cloud.gateway.route.RouteDefinitionRouteLocator#getFilters()`方法是先加载defaultFilters，然后再加载某个route的filters，然后合并。

`org.springframework.cloud.gateway.handler.FilteringWebHandler#handle()`方法会加载全局过滤器，与前面的过滤器合并后根据order排序，组织过滤器链

## [跨域问题](#跨域问题)

### [什么是跨域问题](#什么是跨域问题)

跨域：域名不一致就是跨域，主要包括：

- 域名不同： [www.taobao.com](http://www.taobao.com) 和 [www.taobao.org](http://www.taobao.org) 和 [www.jd.com](http://www.jd.com) 和 [miaosha.jd.com](http://miaosha.jd.com)

- 域名相同，端口不同：localhost:8080和localhost:8081

跨域问题：浏览器禁止请求的发起者与服务端发生跨域ajax请求，请求被浏览器拦截的问题

解决方案：CORS，这里不再赘述了，不知道的小伙伴可以查看[https://www.ruanyifeng.com/blog/2016/04/cors.html](https://www.ruanyifeng.com/blog/2016/04/cors.html)

### [模拟跨域问题](#模拟跨域问题)

可以在浏览器控制台看到下面的错误：
![](/imported/markdown/2025-03-29-markdown-fdfdad9b-gateway网关/images/9535c7ef74ea-202501011231045.png)
从localhost:8090访问localhost:10010，端口不同，显然是跨域的请求。

### [解决跨域问题](#解决跨域问题)

在gateway服务的application.yml文件中，添加下面的配置：
