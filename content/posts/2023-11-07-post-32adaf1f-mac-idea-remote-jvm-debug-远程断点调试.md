---
title: "Mac Idea Remote JVM Debug 远程断点调试"
date: 2023-11-07
description: "部署jar项目时，添加启动参数 jdk8：java -jar&#160;-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=9999 xxx.jar jdk8以上版本：java -jar&#160;-agentlib:jdwp="
tags:
  - "JAVA"
  - "Spring Boot"
  - "Mac系统"
  - "IDE"
  - "JVM"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/remoteJvm.html"
---

<h1 style="text-align: center">部署jar项目时，添加启动参数</h1>
<ul>
<li>jdk8：<span style="color: rgba(255, 0, 0, 1)"><strong>java -jar&nbsp;<span style="background-color: rgba(0, 0, 0, 1); color: rgba(255, 255, 0, 1)">-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=9999</span> xxx.jar</strong></span></li>
<li>jdk8以上版本：<span style="color: rgba(255, 0, 0, 1)"><strong>java -jar&nbsp;<span style="color: rgba(255, 255, 0, 1); background-color: rgba(0, 0, 0, 1)">-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:9999</span> xxx.jar</strong></span></li>
</ul>
<h1 style="text-align: center">准备SpringBoot项目</h1>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202311/1504448-20231107232458979-806782504.png" alt="" loading="lazy" /></p>
<h2>准备一个接口</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.example.demo.controller;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.GetMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RequestMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RestController;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @description:
 * </span><span style="color: rgba(128, 128, 128, 1)">@author</span><span style="color: rgba(0, 128, 0, 1)">: Alex
 * @create: 2023-11-07 23:08
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
@RestController
@RequestMapping(</span>"/api/v1"<span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> DemoController {
    @GetMapping(</span>"hi"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String hi() {
        </span><span style="color: rgba(0, 0, 255, 1)">int</span> a = 1<span style="color: rgba(0, 0, 0, 1)">;
        System.out.println(</span>"a&gt;&gt;&gt;" +<span style="color: rgba(0, 0, 0, 1)"> a);
        </span><span style="color: rgba(0, 0, 255, 1)">int</span> b = 2<span style="color: rgba(0, 0, 0, 1)">;
        System.out.println(</span>"b&gt;&gt;&gt;" +<span style="color: rgba(0, 0, 0, 1)"> b);
        </span><span style="color: rgba(0, 0, 255, 1)">int</span> num = a +<span style="color: rgba(0, 0, 0, 1)"> b;
        System.out.println(</span>"nun&gt;&gt;&gt;&gt;" +<span style="color: rgba(0, 0, 0, 1)"> num);
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> "hello world"<span style="color: rgba(0, 0, 0, 1)">;
    }
}</span></pre>
