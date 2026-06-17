{

  "title": "springmvc: No converter found for return value of type",
  "date": "2019-12-01",
  "description": "刚开始学习springmvc的童鞋，相信很多都需要过这种情况，报错信息如下 毕竟项目是一点点搭建起来的，项目从无到有，很有可能是缺少依赖导致的，需要额外添加以下三个包",
  "tags": [
    "JAVA"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11968364.html"

}

刚开始学习springmvc的童鞋，相信很多都需要过这种情况，报错信息如下

```text
org.springframework.http.converter.HttpMessageNotWritableException: No converter found for return value of type: class com.cyb.ssm.po.Item
    org.springframework.web.servlet.mvc.method.annotation.AbstractMessageConverterMethodProcessor.writeWithMessageConverters(AbstractMessageConverterMethodProcessor.java:238)
    org.springframework.web.servlet.mvc.method.annotation.RequestResponseBodyMethodProcessor.handleReturnValue(RequestResponseBodyMethodProcessor.java:181)
    org.springframework.web.method.support.HandlerMethodReturnValueHandlerComposite.handleReturnValue(HandlerMethodReturnValueHandlerComposite.java:82)
    org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:124)
    org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:888)
    org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:793)
    org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:87)
    org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1040)
    org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:943)
    org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:1006)
    org.springframework.web.servlet.FrameworkServlet.doGet(FrameworkServlet.java:898)
    javax.servlet.http.HttpServlet.service(HttpServlet.java:621)
    org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:883)
    javax.servlet.http.HttpServlet.service(HttpServlet.java:728)
    org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:51)
```

　　毕竟项目是一点点搭建起来的，项目从无到有，很有可能是缺少依赖导致的，需要额外添加以下三个包

```text
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-annotations</artifactId>
            <version>2.10.1</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-core</artifactId>
            <version>2.10.1</version>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-databind</artifactId>
            <version>2.10.1</version>
        </dependency>
```
