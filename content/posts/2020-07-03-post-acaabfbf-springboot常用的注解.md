---
title: "SpringBoot常用的注解"
date: 2020-07-03
description: "@Controller 作用：用于标记这个类是一个控制器，返回页面的时候使用；如果要返回JSON，则需要在接口上使用@ResponseBody才可以 @RestController 作用：用于标记这个类是一个控制器，返回JSON数据的时候使用，如果使用这个注解，则接口返回数据会被序列化为JSON 所"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13232547.html"
---

<h1>@Controller</h1>
<p>　　作用：用于标记这个类是一个控制器，返回页面的时候使用；如果要返回JSON，则需要在接口上使用@ResponseBody才可以</p>
<h1>@RestController</h1>
<p>　　作用：用于标记这个类是一个控制器，返回JSON数据的时候使用，如果使用这个注解，则接口返回数据会被序列化为JSON</p>
<p>　　所以：@RestControlle = @Controller + @ResponseBody</p>
<h1>@RequestMapping</h1>
<p>　　作用：路由映射，用于类上做1级路径；用于某个方法上做自路径</p>
<h1>@SpringBootApplication</h1>
<p>　　作用：用于标记是StringBoot应用，里面包含多个子注解</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">@SpringBootAppliccation = @Configuration + @EnableAutoConfiguration + @ComponentScan

@Configuration:主要标记在某个类上，用于Spring扫描注入，一般结合@Bean
@EnableAutoConfiguration:启用Spring的自动加载配置，自动载入应用程序所需的所有Bean
@ComponentScan:告诉spring扫描包的范围，默认是Application类所在的全部子包，可以指定其他包
@ComponentScan({"net.cyb.package1","net.cyb.package2"})</span></pre>
