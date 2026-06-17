---
title: "SpringBoot2.X新版本配置拦截器在项目中的使用"
date: 2020-07-05
description: "拦截器：和过滤器用途基本类似 SpringBoot2.X新版本配置拦截器 implements WebMvcConfigure 自定义拦截器 HandlerInterceptor preHandle：调用Controller某个方法之前 postHandle：Controller之后调用，视图渲染之"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13246572.html"
---

<p>拦截器：和过滤器用途基本类似</p>
<p>SpringBoot2.X新版本配置拦截器 implements WebMvcConfigure</p>
<ul>
<li>自定义拦截器 HandlerInterceptor
<ul>
<li>preHandle：调用Controller某个方法之前</li>
<li>postHandle：Controller之后调用，视图渲染之前，如果控制器Controller出现了异常，则不会执行此方法</li>
<li>afterCompletion：不管有没有异常，这个afterCompletion都会被调用，用于资源清理</li>
</ul>
</li>
<li>按照注册顺序进行拦截，先注册，先被拦截</li>
</ul>
<p>拦截不生效常见问题</p>
<ol>
<li>是否有加@Configuration</li>
<li>拦截路径是否有问题 **和*</li>
<li>拦截器最后路径一定要 /** 如果是目录的话则是 /*/</li>
</ol>
<p>场景：权限控制、用户登陆状态控制等</p>
<p>和Filter过滤器的区别</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">Filter和Interceptor二者都是AOP编程思想的体现，功能基本都可以实现
拦截器功能更强大些，Filter能做的事情它都能做
Filter在只在Servlet前后起作用，而Interceptor能够深入到方法前后、异常抛出前后等
依赖于Servlet容器既web应用中，而Interceptor不依赖于Servlet容器所以可以运行在多种环境<br>在接口调用的生命周期，Interceptor可以被多次调用，而Filter只能在容器初始化时调用一次。<br>Filter和Interceptor的执行顺序<br>过滤前-&gt;拦截前-&gt;action执行-&gt;拦截后-&gt;过滤后</span></pre>
