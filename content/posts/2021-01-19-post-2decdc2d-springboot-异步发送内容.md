---
title: "SpringBoot 异步发送内容"
date: 2021-01-19
description: "启动类上加注解 @EnableAsync 控制层 @RestController @RequestMapping(&quot;asyn&quot;) public class AsyncController { @Autowired AsynComponent asynComponent; @Get"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14296439.html"
---

<h1 style="text-align: center">启动类上加注解</h1>
<p>@EnableAsync</p>
<h1 style="text-align: center">控制层</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">@RestController
@RequestMapping(</span>"asyn"<span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> AsyncController {
    @Autowired
    AsynComponent asynComponent;
    @GetMapping(</span>"test"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String test(){
        asynComponent.run(</span>"ssss"<span style="color: rgba(0, 0, 0, 1)">);
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> "ok"<span style="color: rgba(0, 0, 0, 1)">;
    }
}</span></pre>
