---
title: "SpringBoot全局异常，返回JSON数据"
date: 2020-07-05
description: "全局异常处理 为什么要配全局异常？ 不配全局服务端报错场景，1/0、空指针等 配置好处 统一的错误页面或错误码 对用户更友好 配置全局异常 第一步类添加注解 @ControllerAdvicce，如果需要返回JSON数据，则方法需要加@ReponseBody @RestControllerAdvic"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13237872.html"
---

<h1 style="text-align: center">全局异常处理</h1>
<h2 style="text-align: left">为什么要配全局异常？</h2>
<ul>
<li>不配全局服务端报错场景，1/0、空指针等</li>
</ul>
<h3>配置好处</h3>
<ul>
<li>统一的错误页面或错误码</li>
<li>对用户更友好</li>
</ul>
<h1 style="text-align: center">配置全局异常</h1>
<h2>第一步类添加注解</h2>
<ul>
<li>@ControllerAdvicce，如果需要返回JSON数据，则方法需要加@ReponseBody</li>
<li>@RestControllerAdvice，默认返回JSON数据，方法不需要加@ResponseBody</li>
</ul>
<h2>第二步方法添加处理器</h2>
<ul>
<li>捕获全局异常，处理所有不可知的异常</li>
<li>@ExceptionHandler(value=Exception.class)</li>
</ul>
<p>CustomExtHandler.java</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cyb.demo.handler;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> net.cyb.demo.utils.JsonData;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.ExceptionHandler;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RestControllerAdvice;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletRequest;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * 标记这是一个异常处理类
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
@RestControllerAdvice
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> CustomExtHandler {
    @ExceptionHandler(value </span>= Exception.<span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)">)
    JsonData HandlerException(Exception e, HttpServletRequest request){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> JsonData.buildError(-2,"服务端出问题了"<span style="color: rgba(0, 0, 0, 1)">);
    }
}</span></pre>
