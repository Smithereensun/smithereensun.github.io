---
title: "SpringMvc 拦截器"
date: 2023-05-31
description: "SpringMvc 拦截器介绍 SpringMVC拦截器（Interceptor）实现对每一个请求处理前后进行相关的业务处理，类似与servlet中的Filter。 SpringMVC 中的Interceptor 拦截请求是通过HandlerInterceptor来实现的。 在SpringMVC中定"
tags:
  - "MVC"
  - "JAVA"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12041228.html"
---

<h1 style="text-align: center">SpringMvc 拦截器介绍</h1>
<ul>
<li class="15">SpringMVC拦截器（<span style="color: rgba(255, 0, 0, 1)"><strong>Interceptor</strong></span><span style="font-family: &quot;YaHei Consolas Hybrid&quot;">）实现对每一个请求处理前后进行相关的业务处理，类似与</span>servlet中的<span style="color: rgba(255, 0, 0, 1)"><strong>Filter</strong></span>。</li>
</ul>
<ul>
<li class="15">SpringMVC 中的Interceptor 拦截请求是通过<span style="color: rgba(255, 0, 0, 1)"><strong>HandlerInterceptor</strong></span>来实现的。</li>
</ul>
<ul>
<li class="15"><span style="font-family: &quot;YaHei Consolas Hybrid&quot;">在</span>SpringMVC中定义一个Interceptor非常简单，主要有4种方式：</li>
</ul>
<p class="15">　　　　1）实现Spring的<span style="color: rgba(255, 0, 0, 1)"><strong>HandlerInterceptor</strong></span>接口；</p>
<p class="15">　　　　2）继承实现了HandlerInterceptor接口的类，比如Spring 已经提供的实现了HandlerInterceptor 接口的抽象类HandlerInterceptorAdapter；</p>
<p class="15">　　　　3）实现Spring的WebRequestInterceptor接口；</p>
<p class="15">　　　　4）继承实现了WebRequestInterceptor的类；</p>
<h1 style="text-align: center">定义拦截器</h1>
<h2>实现HandlerIntercepter接口：</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> MyHandlerIntercepter1 <span style="color: rgba(0, 0, 255, 1)">implements</span><span style="color: rgba(0, 0, 0, 1)"> HandlerInterceptor{

    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">Handler执行前调用
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">应用场景：登录认证、身份授权
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">返回值为true则是放行，为false是不放行</span>
<span style="color: rgba(0, 0, 0, 1)">    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">boolean</span><span style="color: rgba(0, 0, 0, 1)"> preHandle(HttpServletRequest request,
            HttpServletResponse response, Object handler) </span><span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {
        
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
    }

    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">进入Handler开始执行，并且在返回ModelAndView之前调用
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">应用场景：对ModelAndView对象操作，可以把公共模型数据传到前台，可以统一指定视图</span>
<span style="color: rgba(0, 0, 0, 1)">    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> postHandle(HttpServletRequest request,
            HttpServletResponse response, Object handler,
            ModelAndView modelAndView) </span><span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {
        
    }
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">执行完Handler之后调用
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">应用场景：统一异常处理、统一日志处理</span>
<span style="color: rgba(0, 0, 0, 1)">    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> afterCompletion(HttpServletRequest request,
            HttpServletResponse response, Object handler, Exception ex)
            </span><span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {
        
    }

}</span></pre>
