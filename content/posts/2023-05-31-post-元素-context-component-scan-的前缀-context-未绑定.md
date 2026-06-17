---
title: "元素“context:component-scan”的前缀“context”未绑定"
date: 2023-05-31
description: "首先报这个错误，你得明白，是什么原因导致的？ 答：未引入命名空间，和约束文件 解决方法： &lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt; &lt;beans xmlns=&quot;http://www.springf"
tags:
  - "JAVA"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11784503.html"
---

<p>　　首先报这个错误，你得明白，是什么原因导致的？</p>
<p>　　答：未引入命名空间，和约束文件</p>
<p>解决方法：</p>
<div class="cnblogs_code">
<pre>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;beans xmlns="http://www.springframework.org/schema/beans"<span style="color: rgba(0, 0, 0, 1)">
    xmlns:xsi</span>="http://www.w3.org/2001/XMLSchema-instance"<span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>
    xmlns:context="http://www.springframework.org/schema/context"</strong></span><span style="color: rgba(0, 0, 0, 1)">
    xsi:schemaLocation</span>="http://www.springframework.org/schema/beans
        http:<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">www.springframework.org/schema/beans/spring-beans.xsd</span>
        <span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>http://www.springframework.org/schema/context
        http://</strong></span><span style="color: rgba(0, 128, 0, 1)"><span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>www.springframework.org/schema/context/spring-context.xsd</strong></span>"&gt;</span>
        &lt;!-- 组件扫描器，主要是spring使用，用来扫描带有指定注解的类，将这些加载成BeanDefinition --&gt;
    &lt;context:component-scan base-<span style="color: rgba(0, 0, 255, 1)">package</span>="com.cyb.spring.service" /&gt;
&lt;/beans&gt;</pre>
