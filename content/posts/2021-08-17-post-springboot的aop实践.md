---
title: "SpringBoot的AOP实践"
date: 2021-08-17
description: "导读 之前写过一篇，利用AOP记录用户操作日志：点我直达。 核心概念 横切关注点 对那些方法进行拦截，拦截后怎么处理，这些就叫横切关注点 比如：权限认证、日志、事务 通知 Advice 在特定的切入点上执行的增强处理，有5种通知 用途：记录日志、控制事务、提前编写好通用的模块，需要的地方直接调用 连"
tags:
  - "Spring Boot"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15151587.html"
---

<p>&nbsp;</p>
<h1 style="text-align: center">导读</h1>
<p>　　之前写过一篇，利用AOP记录用户操作日志：<a href="https://www.cnblogs.com/chenyanbin/p/14811979.html" target="_blank">点我直达</a>。</p>
<h1 style="text-align: center">核心概念</h1>
<h1 id="横切关注点">横切关注点<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/13304842.html#横切关注点"><br></a></h1>
<ul>
<li>对那些方法进行拦截，拦截后怎么处理，这些就叫横切关注点</li>
<li>比如：权限认证、日志、事务</li>
</ul>
<h1 id="通知-advice">通知 Advice<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/13304842.html#通知-advice"><br></a></h1>
<ul>
<li>在特定的切入点上执行的增强处理，有5种通知</li>
<li>用途：记录日志、控制事务、提前编写好通用的模块，需要的地方直接调用</li>
</ul>
<h1 id="连接点-jointpoint">连接点 JointPoint<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/13304842.html#连接点-jointpoint"><br></a></h1>
<ul>
<li>要用通知的地方，业务流程在运行过程中需要插入切面的具体位置</li>
<li>一般是方法的调用前后，全部方法都可以是连接点</li>
<li>只是概念，没啥特殊</li>
</ul>
<h1 id="切入点-pointcut">切入点 Pointcut<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/13304842.html#切入点-pointcut"><br></a></h1>
<ul>
<li>不能全部方法都是连接点，通过特定的规则来筛选连接点，就是Pointcut，选中那几个你想要的方法</li>
<li>在程序中主要体现为书写切入点表达式(通过通配、正则表达式)过滤出特定的一组JointPoint连接点</li>
<li>过滤出相应的Advicce将要发生的joinPoint地方</li>
</ul>
<h1 id="切面-aspect">切面 Aspect<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/13304842.html#切面-aspect"><br></a></h1>
<ul>
<li>通常是一个类，里面定义 切入点+通知，定义在什么地方；什么时间点，做什么事情</li>
<li>通知 advice致命类时间和做的事情（前置、后置等）</li>
<li>切入点pointcut指定在什么地方干这个事情</li>
<li>web接口设计中，web层-》网关层-》服务层-》数据层，每一层之间也是一个切面，对象和对象，方法和方法之间都是一个个切面</li>
</ul>
<h1 id="目标-target">目标 target<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/13304842.html#目标-target"><br></a></h1>
<ul>
<li>目标类，真正的业务逻辑，可以在目标类不知情的条件下，增加新的功能到目标类的链路上</li>
</ul>
<h1 id="织入-weaving">织入 Weaving<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/13304842.html#织入-weaving"><br></a></h1>
<ul>
<li>把切面（某个类）应用到目标函数的过程成为织入</li>
</ul>
<h1 id="aop-代理">AOP 代理<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/13304842.html#aop-代理"><br></a></h1>
<ul>
<li>AOP框架创建的对象，代理就是目标对象的加强</li>
<li>Spring中的AOP代理可以使用JDK动态代理，也可以是CGLIB代理</li>
</ul>
<h1 style="text-align: center">添加依赖</h1>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> AOP依赖 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.springframework.boot<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>spring-boot-starter-aop<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">exclusions</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">exclusion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.springframework.boot<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>spring-boot-starter-logging<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">exclusion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">exclusions</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.aspectj<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>aspectjweaver<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
