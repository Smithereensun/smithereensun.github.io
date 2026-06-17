---
title: "SpringBoot中使用Servlet3.0注解开发自定义的拦截器"
date: 2020-07-05
description: "使用Servlet3.0的注解进行配置步骤 启动类里面加@ServletComponentScan，进行扫描 新建一个Filter类，implements Filter，并实现对应的接口 @WebFilter标记一个类为filter，被spring扫描 urlPatterns：拦截规则，支持正则 控"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13238256.html"
---

<h1 style="text-align: center">使用Servlet3.0的注解进行配置步骤</h1>
<ul>
<li>启动类里面加@ServletComponentScan，进行扫描</li>
<li>新建一个Filter类，implements Filter，并实现对应的接口</li>
<li>@WebFilter标记一个类为filter，被spring扫描</li>
<li>urlPatterns：拦截规则，支持正则</li>
<li>控制chain.doFilter的方法调用，来实现是否通过放行</li>
<li>不放行，web应用resp.sendRedirect("/index.html")或者返回json字符串</li>
</ul>
<h2>场景</h2>
<p>　　权限控制、用户登陆状态控制，也可以交给拦截器处理等</p>
<h2>实现</h2>
<h3>项目结构</h3>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200705132629324-841368221.png" alt="" loading="lazy" /></p>
<h3>VideoOrderController.java</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cyb.demo.controller;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> net.cyb.demo.utils.JsonData;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RequestMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(</span>"/api/v1/pri/order"<span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> VideoOrderController {
    @RequestMapping(</span>"save"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> JsonData saveOrder(){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> JsonData.buildSuccess("下单成功"<span style="color: rgba(0, 0, 0, 1)">);
    }
}</span></pre>
