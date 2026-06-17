---
title: "SpringMvc 跨域处理"
date: 2023-05-31
description: "导读 由于浏览器对于JavaScript的同源策略的限制，导致A网站(Ajax请求)不能通过JS去访问B网站的数据，于是跨域问题就出现了。 跨域指的是域名、端口、协议的组合不同就是跨域。 http://www.chenyanbin.com/ https://www.chenyanbin.com/ h"
tags:
  - "MVC"
  - "JavaScript"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12045237.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　由于浏览器对于<span style="color: rgba(255, 0, 0, 1)"><strong>JavaScript</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>同源策略</strong></span>的限制，导致<span style="color: rgba(255, 0, 0, 1)"><strong>A网站</strong></span>(Ajax请求)<strong><span style="color: rgba(255, 0, 0, 1)">不能通过JS</span></strong>去<span style="color: rgba(255, 0, 0, 1)"><strong>访问B网站的数据</strong></span>，于是跨域问题就出现了。</p>
<p>跨域指的是域名、端口、协议的组合不同就是跨域。</p>
<ol>
<li>http://www.chenyanbin.com/</li>
<li>https://www.chenyanbin.com/</li>
<li>http://www.chenyanbin.cn</li>
<li>http://www.chenyanbin.com:8080/</li>
</ol>
<h1 style="text-align: center">为什么要有同源策略？</h1>
<p>　　举个例子：比如一个黑客程序，他利用IFrame把真正的银行登录页面嵌套到他的页面上，当你使用真实的用户名，密码登录时，他的页面就可以通过JavaScript读取到你的表单中input中的内容，这样用户名、密码就轻松到手啦。</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191215170911776-748742715.png" alt="" /></p>
<p>&nbsp;</p>
<h1 style="text-align: center">&nbsp;如何解决跨域?</h1>
<p>　　解决跨域的方式有多种，比如<span style="color: rgba(255, 0, 0, 1)"><strong>基于JavaScript</strong></span>的解决方式、<span style="color: rgba(255, 0, 0, 1)"><strong>基于Jquery的JSONP</strong></span>、以及<span style="color: rgba(255, 0, 0, 1)"><strong>基于CORS</strong></span>的方式。</p>
<p>　　JSONP和CORS的区别之一：<span style="color: rgba(255, 0, 0, 1)"><strong>JSONP只能解决get方式提交</strong></span>、<span style="color: rgba(255, 0, 0, 1)"><strong>CORS</strong></span>不仅<span style="color: rgba(255, 0, 0, 1)"><strong>支持GET</strong></span>方式，同时<span style="color: rgba(255, 0, 0, 1)"><strong>还</strong><strong>支持POST</strong></span>提交方式。</p>
<p>　　我们重点讲解<span style="color: rgba(255, 0, 0, 1)"><strong>CORS跨域</strong></span>方式。</p>
<h1 style="text-align: center">什么是CORS？</h1>
<p>　　CORS是一个<span style="color: rgba(255, 0, 0, 1)"><strong>W3C</strong></span>标准，全称是“<span style="color: rgba(255, 0, 0, 1)"><strong>跨域资源共享</strong></span>”(Cross-origin resource sharing)。</p>
<p>　　它允许浏览器向跨资源服务器，发出<span style="color: rgba(255, 0, 0, 1)"><strong>XMLHttpRequest</strong></span>请求，从而克服了AJAX只能同源使用的限制。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>CORS需要浏览器</strong></span>和<strong><span style="color: rgba(255, 0, 0, 1)">服务器同时支持</span></strong>。目前，所有浏览器都支持该功能，<span style="font-size: 16px"><strong><span style="color: rgba(255, 0, 0, 1)">浏览器</span><span style="color: rgba(255, 0, 0, 1)">不能低于IE10</span></strong></span>。</p>
<p>　　CORS原理：只需要向响应头header中注入：<span style="color: rgba(255, 0, 0, 1)"><strong>Access-Control-Allow-Origin</strong></span>，这样<span style="color: rgba(255, 0, 0, 1)"><strong>浏览器检测</strong></span>到<span style="color: rgba(255, 0, 0, 1)"><strong>header</strong></span>中的：<span style="color: rgba(255, 0, 0, 1)"><strong>Access-Control-Allow-Origin</strong></span>，则就可以<span style="color: rgba(255, 0, 0, 1)"><strong>跨域操作</strong></span>了。</p>
<h1 style="text-align: center">CORS请求分类标准</h1>
<p>　　浏览器将CORS请求分成两类：简单请求(<span style="color: rgba(255, 0, 0, 1)"><strong>simple request</strong></span>)和非简单请求(<span style="color: rgba(255, 0, 0, 1)"><strong>not-so-simple-request</strong></span>)。</p>
<h2>简单请求</h2>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191215172343114-14339813.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;　　凡是<span style="color: rgba(255, 0, 0, 1)"><strong>不同时满足</strong></span>上面<span style="color: rgba(255, 0, 0, 1)"><strong>两个条件</strong></span>，就<span style="color: rgba(255, 0, 0, 1)"><strong>属于非简单请求</strong></span>。</p>
<p>　　浏览器对这两种请求的处理，是不一样的。</p>
<p>　　对于一个简单请求，浏览器直接发出CORS请求，具体来说，就是在头信息之中，加上一个<span style="color: rgba(255, 0, 0, 1)"><strong>Origin</strong></span>字段。</p>
<h3>请求信息</h3>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191215172606867-1885552677.png" alt="" /></p>
<p>&nbsp;</p>
<h3>&nbsp;响应信息</h3>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191215172619138-1892560964.png" alt="" /></p>
<p>&nbsp;</p>
<h3>&nbsp;字段说明</h3>
<ol>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>Access-Control-Allow-Origin</strong></span>：该字段是必须的。它的值要么是请求时Origin字段的值，要么是一个*，表示接收任意域名的请求。</li>
<li>Access-Control-Allow-Credentials：该字段可选。它的值是一个布尔值，表示是否允许发送Cookie。默认情况下，Cookie不包括在CORS请求之中，设为True，即表示服务器明确许可，Cookie可以包含在请求中，一起发送给服务器。这个值也只能设为True，如果服务器不要浏览器发送Cookie，删除即可。</li>
</ol>
<h2>非简单请求</h2>
<p>　　非简单请求是那种对服务器有特殊要求的请求，比如请求方法是PUT或者DELETE，或者Content-Type字段的类型是：application/json。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>非简单请求</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>CORS请求</strong></span>，会<span style="color: rgba(255, 0, 0, 1)"><strong>在正式通信</strong></span>之<span style="color: rgba(255, 0, 0, 1)"><strong>前</strong></span>，增<span style="color: rgba(255, 0, 0, 1)"><strong>加一次HTTP查询请求</strong></span>，称为“<span style="color: rgba(255, 0, 0, 1)"><strong>预检</strong></span>”请求(preflight)。</p>
<p>　　浏览器先咨问服务器，当前网页所在的域名是否在服务器的许可名单之中，以及可以使用哪些HTTP动词和头信息字段。只有得到肯定答复，浏览器才会发出正式的XMLHttpRequest请求，否则就报错。</p>
<h3>请求信息</h3>
<p>　　Http请求的方式是put，并发送一个自定义头信息：X-Custom-Header。</p>
<p>　　浏览器发现，这是一个非简单请求，就自动发出一个“预检”请求，要求服务器确认可以这样请求。下面是这个“预检”请求的HTTP头信息。</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191215173804158-1957957070.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;“预检”请求用的请求方法是OPTIONS，表示这个请求是用来咨问的。头信息里面，关键字端是Origin，表示请求来自那个源。</p>
<p>除了Origin字段，“预检”请求的头信息包括两个特殊字段。</p>
<ol>
<li>Access-Control-Request-Method：该字段是必须的，用来列出浏览器的CORS请求会用到哪些HTTP方法，上例是PUT。</li>
<li>Access-Control-Request-Header：该字段是一个逗号分隔的字符串，指定浏览器CORS请求会额外发送的头信息字段，上例是X-Custom-Header。</li>
</ol>
<p>一旦服务器通过了“预检”请求，以后每次浏览器正常的CORS请求，就都跟简单请求一样了。会有一个Origin头信息字段。服务器的回应，也都会有一个Access-Control-Allow-Origin头信息字段。</p>
<h1 style="text-align: center">CORS实现</h1>
<h2>使用SpringMvc的拦截器实现</h2>
<p>具体的【<a class="postTitle2" href="https://www.cnblogs.com/chenyanbin/p/12041228.html">SpringMvc 拦截器</a>】参考</p>
<h2>跨域不提交Cookie</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb.ssm.controller;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletRequest;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletResponse;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.servlet.HandlerInterceptor;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> MyHandlerIntercepter <span style="color: rgba(0, 0, 255, 1)">implements</span><span style="color: rgba(0, 0, 0, 1)"> HandlerInterceptor {
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">boolean</span><span style="color: rgba(0, 0, 0, 1)"> preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) {
        System.out.println(</span>"Origin:"+request.getHeader("Origin"<span style="color: rgba(0, 0, 0, 1)">));
        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (request.getHeader("Origin") != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
            response.setContentType(</span>"text/html;charset=UTF-8"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 允许哪一个URL</span>
            response.setHeader("Access-Control-Allow-Origin", "*"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 允许那种请求方法</span>
            response.setHeader("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE"<span style="color: rgba(0, 0, 0, 1)">);
            response.setHeader(</span>"XDomainRequestAllowed", "1"<span style="color: rgba(0, 0, 0, 1)">);
            System.out.println(</span>"正在跨域"<span style="color: rgba(0, 0, 0, 1)">);
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">true</span>; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">True：允许访问；False：不允许访问</span>
<span style="color: rgba(0, 0, 0, 1)">    }
}</span></pre>
