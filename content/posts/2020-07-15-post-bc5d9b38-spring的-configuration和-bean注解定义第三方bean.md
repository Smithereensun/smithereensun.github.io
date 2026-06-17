---
title: "Spring的@Configuration和@Bean注解定义第三方bean"
date: 2020-07-15
description: "@Configuration和@Bean注解的使用 @Configuration标注在类上，相当于把该类作为spring的xml配置文件中&lt;beans&gt;，作用为：配置spring容器(应用上下文) @bean注解：用于告诉方法产生一个Bean对象，然后这个Bean对象交给Spring管理"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13307323.html"
---

<h1 style="text-align: center">@Configuration和@Bean注解的使用</h1>
<ul>
<li>@Configuration标注在类上，相当于把该类作为spring的xml配置文件中&lt;beans&gt;，作用为：配置spring容器(应用上下文)</li>
<li>@bean注解：用于告诉方法产生一个Bean对象，然后这个Bean对象交给Spring管理，Spring将会将这个Bean对象放在自己的IOC容器中</li>
<li>注意：Spring IOC容器管理一个或多个bean，这些bean都需要在@Configuration注解下进行创建</li>
</ul>
<h2>AppConfig.java</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.config;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.domain.VideoOrder;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.annotation.Bean;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.annotation.Configuration;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.annotation.Scope;

@Configuration
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> AppConfig {
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">使用@Bean注解，表明这个bean交给spring进行管理，如果没有指定名称，默认采用方法名首字母小写
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">@Bean</span>
    @Bean(value = "videoOrder",initMethod = "init",destroyMethod = "destroy"<span style="color: rgba(0, 0, 0, 1)">)
    @Scope
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> VideoOrder videoOrder(){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> VideoOrder();
    }
}</span></pre>
