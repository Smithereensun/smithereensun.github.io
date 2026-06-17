---
title: "Spring PropertySource，获取指定application.properties文件"
date: 2020-12-10
description: "@PropertySource注解的使用 @PropeertySource，指定加载配置文件 配置文件映射到实体类 使用@Value映射到具体的java属性 CustomConfig.java package net.cybclass.sp.aop; import org.springframewo"
tags:
  - "Spring"
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13307369.html"
---

<h1 style="text-align: center">@PropertySource注解的使用</h1>
<ul>
<li>@PropeertySource，指定加载配置文件
<ul>
<li>配置文件映射到实体类</li>
</ul>
</li>
<li>使用@Value映射到具体的java属性</li>
</ul>
<h2>CustomConfig.java</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.aop;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.beans.factory.annotation.Value;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.annotation.Configuration;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource(value </span>= "classpath:config.properties"<span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> CustomConfig {
    @Value(</span>"${server.host}"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String host;
    @Value(</span>"${server.port}"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> port;

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getHost() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> host;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setHost(String host) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.host =<span style="color: rgba(0, 0, 0, 1)"> host;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> getPort() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> port;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> setPort(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> port) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.port =<span style="color: rgba(0, 0, 0, 1)"> port;
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String toString() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> "CustomConfig{" +
                "host='" + host + '\'' +
                ", port=" + port +
                '}'<span style="color: rgba(0, 0, 0, 1)">;
    }
}</span></pre>
