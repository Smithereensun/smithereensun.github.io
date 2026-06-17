---
title: "SpringMvc 异常处理器"
date: 2023-05-31
description: "简介 SpringMvc 在处理请求过程中出现异常信息由异常处理器进行处理，自定义异常处理器可以实现一个系统的异常处理逻辑。 异常理解 异常包含编译时异常和运行时异常，其中编译时异常也叫预期异常。运行时异常只有在项目运行的情况下才会发现，编译的时候不需要关心。 运行时异常，比如：空指针异常、数组越界"
tags:
  - "JAVA"
  - "Spring"
  - "MVC"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12022180.html"
---

<h1 style="text-align: center">简介</h1>
<p>　　SpringMvc 在处理请求过程中出现异常信息由异常处理器进行处理，自定义异常处理器可以实现一个系统的异常处理逻辑。</p>
<h1 style="text-align: center">异常理解</h1>
<p>　　异常包含<span style="color: rgba(255, 0, 0, 1)"><strong>编译时异常</strong></span>和<span style="color: rgba(255, 0, 0, 1)"><strong>运行时异常</strong></span>，其中编译时异常也叫<span style="color: rgba(255, 0, 0, 1)"><strong>预期异常</strong></span>。运行时异常只有在项目运行的情况下才会发现，编译的时候不需要关心。</p>
<p>　　运行时异常，比如：<span style="color: rgba(255, 0, 0, 1)"><strong>空指针异常、数组越界异常</strong></span>，对于这样的异常，只能通过程序员丰富的经验来解决和测试人员不断的严格测试来解决。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>编译时异常</strong></span>，比如：<span style="color: rgba(255, 0, 0, 1)"><strong>数据库异常、文件读取异常、自定义异常</strong></span>等。对于这样的异常，必须使用 <span style="color: rgba(255, 0, 0, 1)"><strong>try catch</strong></span>代码块或者<span style="color: rgba(255, 0, 0, 1)"><strong>throws</strong></span>关键字来处理异常。</p>
<h1 style="text-align: center">异常处理思路</h1>
<p>　　系统中异常包括两类：<span style="color: rgba(255, 0, 0, 1)"><strong>预期异常(编译时异常)和运行时异常RuntimeException</strong></span>，前者通过捕获异常从而获取异常信息，后者主要通过规范代码开发、测试等手段减少运行时异常的发生。</p>
<p>　　系统的dao、service、controller出现都通过throws Exception向上抛出，最后由SpringMvc前端控制器交给异常处理器进行异常处理，如下图：</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191211093548923-1491720000.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;<span style="color: rgba(255, 0, 0, 1)"><strong>全局范围只有一个异常处理器。</strong></span></p>
<h1 style="text-align: center">自定义异常类</h1>
<h2>第一步：CustomException.java</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb.ssm.exception;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * 自定义编译时异常
 * 
 * </span><span style="color: rgba(128, 128, 128, 1)">@author</span><span style="color: rgba(0, 128, 0, 1)"> apple
 *
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> CustomException <span style="color: rgba(0, 0, 255, 1)">extends</span><span style="color: rgba(0, 0, 0, 1)"> Exception {
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String msg;

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getMsg() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> msg;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setMsg(String msg) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.msg =<span style="color: rgba(0, 0, 0, 1)"> msg;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> CustomException(String msg) {
        </span><span style="color: rgba(0, 0, 255, 1)">super</span><span style="color: rgba(0, 0, 0, 1)">();
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.msg =<span style="color: rgba(0, 0, 0, 1)"> msg;
    }
}</span></pre>
