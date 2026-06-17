---
title: "SpringMVC面试题及答案"
date: 2020-06-25
description: "SpringMvc 的控制器是不是单例模式，如果是，有什么问题，怎么解决？ 问题：单例模式，在多线程访问时有线程安全问题 解决方法：不要用同步，在控制器里面不能写字段 SpringMvc 中控制器的注解？ @Controller：该注解表明该类扮演控制器的角色 @RequestMapping 注解用"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13193393.html"
---

<h1>SpringMvc 的控制器是不是单例模式，如果是，有什么问题，怎么解决？</h1>
<p>问题：单例模式，在多线程访问时有线程安全问题</p>
<p>解决方法：不要用同步，在控制器里面不能写字段</p>
<h1>SpringMvc 中控制器的注解？</h1>
<p>@Controller：该注解表明该类扮演控制器的角色</p>
<h1>@RequestMapping 注解用在类上的作用？</h1>
<p>作用：用来映射一个URL到一个类或者一个特定的处理方法上</p>
<h1>前台多个参数，这些参数都是一个对象，快速得到对象？</h1>
<p>方法：直接在方法中声明这个对象，SpringMvc就自动把属性赋值到这个对象里面</p>
<h1>SpringMvc中函数的返回值？</h1>
<p>String，ModelAndView，List，Set 等</p>
<p>一般String，Ajax请求，返回一个List集合</p>
<h1>SpringMvc中的转发和重定向?</h1>
<div>
<div>
<p>转发： return：“hello”</p>
<p>重定向 ：return：“redirect:hello.jsp”</p>
<p>通过JackSon框架把java里面对象直接转换成js可识别的json对象，具体步骤如下：</p>
<p>加入JackSon.jar</p>
<p>在配置文件中配置json的映射</p>
<p>在接受Ajax方法里面直接返回Object，list等，方法前面需要加上注解@ResponseBody</p>
