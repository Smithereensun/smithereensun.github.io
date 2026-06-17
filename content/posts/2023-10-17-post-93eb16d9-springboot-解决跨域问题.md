---
title: "SpringBoot 解决跨域问题"
date: 2023-10-17
description: "今天遇到一个很神奇的问题，之前写的项目，后端跨域都处理好的，按部就班使用原来的方式，前后端都开发完之后，部署本地后，跨域没起效，一脸懵逼，然后使用公司另外一个同事的跨域解决方案，具体我也没深入研究到底咋回事，先记录下来。 方式一 我之前的做法 CorsInterceptor.java package"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13953473.html"
---

<p>　　今天遇到一个很神奇的问题，之前写的项目，后端跨域都处理好的，按部就班使用原来的方式，前后端都开发完之后，部署本地后，跨域没起效，一脸懵逼，然后使用公司另外一个同事的跨域解决方案，具体我也没深入研究到底咋回事，先记录下来。</p>
<h1 style="text-align: center">方式一</h1>
<p>　　我之前的做法</p>
<h2>CorsInterceptor.java</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.ybclass.online_ybclass.interceptor;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.http.HttpMethod;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.servlet.HandlerInterceptor;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.servlet.ModelAndView;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletRequest;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletResponse;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> CorsInterceptor <span style="color: rgba(0, 0, 255, 1)">implements</span><span style="color: rgba(0, 0, 0, 1)"> HandlerInterceptor {
    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">boolean</span> preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">表示接受任意域名的请求,也可以指定域名</span>
        response.setHeader("Access-Control-Allow-Origin", request.getHeader("origin"<span style="color: rgba(0, 0, 0, 1)">));

        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">该字段可选，是个布尔值，表示是否可以携带cookie</span>
        response.setHeader("Access-Control-Allow-Credentials", "true"<span style="color: rgba(0, 0, 0, 1)">);

        response.setHeader(</span>"Access-Control-Allow-Methods", "GET, HEAD, POST, PUT, PATCH, DELETE, OPTIONS"<span style="color: rgba(0, 0, 0, 1)">);

        response.setHeader(</span>"Access-Control-Allow-Headers", "*"<span style="color: rgba(0, 0, 0, 1)">);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">这里可以不加，但是其他语言开发的话记得处理options请求</span>
        <span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
         * 非简单请求是对那种对服务器有特殊要求的请求，
         * 比如请求方式是PUT或者DELETE，或者Content-Type字段类型是application/json。
         * 都会在正式通信之前，增加一次HTTP请求，称之为预检。浏览器会先询问服务器，当前网页所在域名是否在服务器的许可名单之中，
         * 服务器允许之后，浏览器会发出正式的XMLHttpRequest请求
         </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
        <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (HttpMethod.OPTIONS.toString().equals(request.getMethod())) {
            </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, ModelAndView modelAndView) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {

    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {

    }
}</span></pre>
