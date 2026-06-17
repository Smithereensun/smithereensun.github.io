---
title: "Spring DI(依赖注入)自动装配 @Autowired、@Resource注解"
date: 2020-05-21
description: "@Autowired：一部分功能是查找实例，从Spring容器中根据类型（Java类）获取对应的实例；另一部分功能就是赋值，将找到的实例，装配给另一个实例的属性值。（注：一个Java类型在同一个Spring容器中，只能有一个实例。） @Resource：一部分功能是查找实例，从Spring容器中根据"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12929760.html"
---

<ol>
<li>@Autowired：一部分功能是<span style="color: rgba(255, 0, 0, 1)"><strong>查找实例</strong></span>，从Spring容器中<span style="color: rgba(255, 0, 0, 1)"><strong>根据类型</strong></span>（Java类）<span style="color: rgba(255, 0, 0, 1)"><strong>获取对应的实例</strong></span>；另一部分功能就是<span style="color: rgba(255, 0, 0, 1)"><strong>赋值</strong></span>，将找到的实例，装配给另一个实例的属性值。（<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>注：一个Java类型在同一个Spring容器中，只能有一个实例。</strong></span>）</li>
<li>@Resource：一部分功能是<span style="color: rgba(255, 0, 0, 1)"><strong>查找实例</strong></span>，从Spring容器中<span style="color: rgba(255, 0, 0, 1)"><strong>根据Bean的名称</strong></span>（bean标签的名称）<span style="color: rgba(255, 0, 0, 1)"><strong>获取对应的实例</strong></span>；另一部分功能就是<span style="color: rgba(255, 0, 0, 1)"><strong>赋值</strong></span>，将找到的实例，装配给另一个实例的属性值。</li>
</ol>
