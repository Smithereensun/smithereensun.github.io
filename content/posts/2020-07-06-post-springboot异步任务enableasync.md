---
title: "SpringBoot异步任务EnableAsync"
date: 2020-07-06
description: "什么是一部任务和使用场景：适用于处理log、发送邮件、短信...等 下单接口-&gt;查库存 1000 余额校验 1500 风控用户 1000 启动类里面使用@EnableAsync注解开启功能，自动扫描 定义异步任务类并使用@Component标记组件被容器扫描，异步方法加上@Async Test"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13257749.html"
---

<p>什么是一部任务和使用场景：适用于处理log、发送邮件、短信...等</p>
<ul>
<li>下单接口-&gt;查库存 1000</li>
<li>余额校验 1500</li>
<li>风控用户 1000</li>
</ul>
<p>启动类里面使用@EnableAsync注解开启功能，自动扫描</p>
<p>定义异步任务类并使用@Component标记组件被容器扫描，异步方法加上@Async</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706213318991-1433179778.png" alt="" loading="lazy" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706214315622-608902887.png" alt="" loading="lazy" /></p>
<p>TestController.java</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706214015728-308458212.png" alt="" loading="lazy" /></p>
<p>测试</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706214621473-1755260483.gif" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
