---
title: "Spring AOP注解"
date: 2020-07-15
description: "声明切面类 @Aspect(切面)：通常是一个类，里面可以定义切入点和通知 配置切入点和通知 LogAdvice.java package net.cybclass.sp.aop; import org.aspectj.lang.JoinPoint; import org.aspectj.lang."
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13308228.html"
---

<h1 style="text-align: center">声明切面类</h1>
<p>　　@Aspect(切面)：通常是一个类，里面可以定义切入点和通知</p>
<h2>配置切入点和通知</h2>
<p>LogAdvice.java</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.aop;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.JoinPoint;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.annotation.Aspect;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.annotation.Before;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.annotation.Pointcut;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.stereotype.Component;

</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">能被扫描</span>
<span style="color: rgba(0, 0, 0, 1)">@Component
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">告诉Spring，这是一个切面类，里面可以定义切入点和通知</span>
<span style="color: rgba(0, 0, 0, 1)">@Aspect
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> LogAdvice {
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">切入点表达式</span>
    @Pointcut("execution(* net.cybclass.sp.servicce.VideoServiceImpl.*(..))"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> aspect(){

    }
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">前置通知</span>
    @Before("aspect()"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> beforeLog(JoinPoint joinPoint) {
        System.out.println(</span>"LogAdvice beforeLog 被调用了"<span style="color: rgba(0, 0, 0, 1)">);
    }
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">后置通知</span>
    @Before("aspect()"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> afterLog(JoinPoint joinPoint) {
        System.out.println(</span>"LogAdvice afterLog 被调用了"<span style="color: rgba(0, 0, 0, 1)">);
    }
}</span></pre>
