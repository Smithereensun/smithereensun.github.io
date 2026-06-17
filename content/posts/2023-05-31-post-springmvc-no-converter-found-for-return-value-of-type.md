---
title: "springmvc: No converter found for return value of type"
date: 2023-05-31
description: "刚开始学习springmvc的童鞋，相信很多都需要过这种情况，报错信息如下 org.springframework.http.converter.HttpMessageNotWritableException: No converter found for return value of type:"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11968364.html"
---

<p>　　刚开始学习springmvc的童鞋，相信很多都需要过这种情况，报错信息如下</p>
<div class="cnblogs_code">
<pre>org.springframework.http.converter.HttpMessageNotWritableException: No converter found <span style="color: rgba(0, 0, 255, 1)">for</span> <span style="color: rgba(0, 0, 255, 1)">return</span> value of type: <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb.ssm.po.Item
    org.springframework.web.servlet.mvc.method.annotation.AbstractMessageConverterMethodProcessor.writeWithMessageConverters(AbstractMessageConverterMethodProcessor.java:</span>238<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.mvc.method.annotation.RequestResponseBodyMethodProcessor.handleReturnValue(RequestResponseBodyMethodProcessor.java:</span>181<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.method.support.HandlerMethodReturnValueHandlerComposite.handleReturnValue(HandlerMethodReturnValueHandlerComposite.java:</span>82<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:</span>124<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:</span>888<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:</span>793<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:</span>87<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:</span>1040<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:</span>943<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:</span>1006<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.FrameworkServlet.doGet(FrameworkServlet.java:</span>898<span style="color: rgba(0, 0, 0, 1)">)
    javax.servlet.http.HttpServlet.service(HttpServlet.java:</span>621<span style="color: rgba(0, 0, 0, 1)">)
    org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:</span>883<span style="color: rgba(0, 0, 0, 1)">)
    javax.servlet.http.HttpServlet.service(HttpServlet.java:</span>728<span style="color: rgba(0, 0, 0, 1)">)
    org.apache.tomcat.websocket.server.WsFilter.doFilter(WsFilter.java:</span>51)</pre>
