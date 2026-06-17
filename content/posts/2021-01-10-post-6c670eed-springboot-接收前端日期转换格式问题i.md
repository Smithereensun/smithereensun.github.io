---
title: "SpringBoot 接收前端日期转换格式问题i"
date: 2021-01-10
description: "使用FastJson替换jackson import com.alibaba.fastjson.serializer.SerializerFeature; import com.alibaba.fastjson.support.config.FastJsonConfig; import com.al"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14258951.html"
---

<p>使用FastJson替换jackson</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.alibaba.fastjson.serializer.SerializerFeature;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.alibaba.fastjson.support.config.FastJsonConfig;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.alibaba.fastjson.support.spring.FastJsonHttpMessageConverter;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.boot.autoconfigure.http.HttpMessageConverters;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.annotation.Bean;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.annotation.Configuration;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.http.converter.HttpMessageConverter;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.servlet.config.annotation.WebMvcConfigurer;


@Configuration
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> WebMvcConfigurerImpl <span style="color: rgba(0, 0, 255, 1)">implements</span><span style="color: rgba(0, 0, 0, 1)"> WebMvcConfigurer {


    @Bean
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> HttpMessageConverters fastjsonHttpMessageConverter() {
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">定义一个转换消息的对象</span>
        FastJsonHttpMessageConverter fastConverter = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> FastJsonHttpMessageConverter();

        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">添加fastjson的配置信息 比如 ：是否要格式化返回的json数据</span>
        FastJsonConfig fastJsonConfig = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> FastJsonConfig();

        fastJsonConfig.setSerializerFeatures(SerializerFeature.PrettyFormat);

        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">在转换器中添加配置信息</span>
<span style="color: rgba(0, 0, 0, 1)">        fastConverter.setFastJsonConfig(fastJsonConfig);

        HttpMessageConverter converter </span>=<span style="color: rgba(0, 0, 0, 1)"> fastConverter;

        </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> HttpMessageConverters(converter);

    }
}</span></pre>
