---
title: "springmvc Controller详解"
date: 2023-05-31
description: "简介 在SpringMVC&#160;中，控制器Controller&#160;负责处理由DispatcherServlet&#160;分发的请求，它把用户请求的数据经过业务处理层处理之后封装成一个Model&#160;，然后再把该Model&#160;返回给对应的View&#160;进行展示。 示"
tags:
  - "Spring"
  - "JAVA"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11961019.html"
---

<h1 style="text-align: center">简介</h1>
<p>　　在SpringMVC&nbsp;中，控制器Controller&nbsp;负责处理由DispatcherServlet&nbsp;分发的请求，它把用户请求的数据经过业务处理层处理之后封装成一个Model&nbsp;，然后再把该Model&nbsp;返回给对应的View&nbsp;进行展示。</p>
<h1 style="text-align: center">示例</h1>
<h2>不适用注解修饰</h2>
<h3>返回ModelAndView</h3>
<p>controller方法中定义ModelAndView对象并返回，对象中可添加model数据、指定view。</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb.ssm.controller;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.ArrayList;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.List;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.beans.factory.annotation.Autowired;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.stereotype.Controller;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.stereotype.Service;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RequestMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.servlet.ModelAndView;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb.ssm.po.Item;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb.ssm.service.ItemService;

@Controller
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> ItemController {
    @Autowired
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> ItemService Service;
    
    @RequestMapping(</span>"queryItem"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> ModelAndView queryItem() {
        List</span>&lt;Item&gt; itemList =<span style="color: rgba(0, 0, 0, 1)"> Service.queryItemList();
        ModelAndView mvAndView </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> ModelAndView();
        mvAndView.addObject(</span>"itemList"<span style="color: rgba(0, 0, 0, 1)">, itemList);
        mvAndView.setViewName(</span>"item/item-list"<span style="color: rgba(0, 0, 0, 1)">);
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> mvAndView;
    }
}</span></pre>
