---
title: "bean的二次加工-Spring5.X后置处理器BeanPostProcessor"
date: 2020-07-15
description: "什么是BeanPostProcessor 是Spring IOC容器给我们提供的一个扩展接口 在调用初始化方法前后对Bean进行额外加工，ApplicationContext会自动扫描实现了BeanPostProcessor得bean，并注册这些bean为后置处理器 是Bean的统一前置后置处理而不"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13304153.html"
---

<h1 style="text-align: center">什么是BeanPostProcessor</h1>
<ul>
<li>是Spring IOC容器给我们提供的一个扩展接口</li>
<li>在调用初始化方法前后对Bean进行额外加工，ApplicationContext会自动扫描实现了BeanPostProcessor得bean，并注册这些bean为后置处理器</li>
<li>是Bean的统一前置后置处理而不是基于某一个bean</li>
</ul>
<h2>执行顺序</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">Spring IOC容器实例化
调用BeanPostProcessor的postProcessBeforeInitialization方法
调用bean实例的初始化方法
调用BeanPostProcessor的postProcessAfterInitialization方法</span></pre>
