---
title: "Spring 获取Bean ApplicationContextAware的使用"
date: 2020-08-20
description: "创建类继承ApplicationContextAware package net.ybclass.online_ybclass.utils; import org.springframework.beans.BeansException; import org.springframework.con"
tags:
  - "Spring Boot"
  - "JAVA"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13534217.html"
---

<h2><span style="color: rgba(255, 0, 0, 1)"><strong>创建类继承ApplicationContextAware</strong></span></h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.ybclass.online_ybclass.utils;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.beans.BeansException;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.ApplicationContext;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.ApplicationContextAware;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.stereotype.Component;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @ClassName：AppUtil
 * @Description：获取bean工具类
 * @Author：chenyb
 * @Date：2020/8/20 11:39 上午
 * @Versiion：1.0
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
@Component
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> AppUtil <span style="color: rgba(0, 0, 255, 1)">implements</span><span style="color: rgba(0, 0, 0, 1)"> ApplicationContextAware {
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> ApplicationContext applicationContext;
    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> setApplicationContext(ApplicationContext args) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> BeansException {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.applicationContext=<span style="color: rgba(0, 0, 0, 1)">args;
    }
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> Object getObject(String id){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> applicationContext.getBean(id);
    }
}</span></pre>
