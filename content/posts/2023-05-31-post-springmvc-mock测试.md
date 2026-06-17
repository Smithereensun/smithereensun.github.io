---
title: "SpringMVC Mock测试"
date: 2023-05-31
description: "什么是mock测试？ 在测试过程中，对于某些不容易构成或者不容易获取的对象，用一个虚拟的对象来创建以便测试的测试方法，就是Mock测试。 Servlet、Request、Response等Servlet API相关对象本来就是由Servlet容器(Tomcat)创建的。 这个虚拟的对象就是Mock对"
tags:
  - "JAVA"
  - "Spring"
  - "MVC"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12031170.html"
---

<h1 style="text-align: center">什么是mock测试？</h1>
<p>　　在测试过程中，对于某些不容易构成或者不容易获取的对象，用一个<span style="color: rgba(255, 0, 0, 1)"><strong>虚拟的对象</strong></span>来创建以便测试的测试方法，就是<span style="color: rgba(255, 0, 0, 1)"><strong>Mock测试</strong></span>。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>Servlet、Request、Response等Servlet API相关对象本来就是由Servlet容器(Tomcat)创建的。</strong></span></p>
<p>　　这个<span style="color: rgba(255, 0, 0, 1)"><strong>虚拟的对象</strong></span>就是<span style="color: rgba(255, 0, 0, 1)"><strong>Mock对象</strong></span>。</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>Mock对象</strong></span>是真实对象在调试期间的<span style="color: rgba(255, 0, 0, 1)"><strong>代替品</strong></span>。</p>
<h1 style="text-align: center">为什么使用Mock测试?</h1>
<ol>
<li>避免开发模块之间的耦合</li>
<li>轻量、简单、灵活</li>
</ol>
<h1 style="text-align: center">MockMVC介绍</h1>
<h2>MockMvcBuilder</h2>
<p>　　他是用来构造MockMVC的构造器</p>
<p>　　主要有两个实现：<span style="color: rgba(255, 0, 0, 1)"><strong>StandaloneMockMvcBuilder</strong></span>和<span style="color: rgba(255, 0, 0, 1)"><strong>DefaultMockMvcBuilder</strong></span>，分别对应之前的两种测试方式。</p>
<p>　　我们直接使用<span style="color: rgba(255, 0, 0, 1)"><strong>静态工厂MockMvcBuilders</strong></span>创建即可。</p>
<h2>MockMvcBuilders</h2>
<p>　　负责创建MockMvcBuilder对象</p>
<p>　　有两种创建方式</p>
<p>　　　　1、standaloneSetup(Object... controllers)</p>
<p>　　　　2、<span style="color: rgba(255, 0, 0, 1)"><strong>webAppContextSetup(WebApplicationContext wac)</strong></span>：指定WebApplicationContext，将会从该上下文获取相应的控制器并得到相应的MockMvc</p>
<h2><span style="color: rgba(255, 0, 0, 1)">MockMvc</span></h2>
<p>　　对于服务器端的Spring MVC测试支持<span style="color: rgba(255, 0, 0, 1)"><strong>主入口点</strong></span>。</p>
<p>　　通过MockMvcBuilder构造</p>
<p>　　MockMvcBuilder由MockMvcBuilders的静态方法去构造。</p>
<p>　　核心方法：<span style="color: rgba(255, 0, 0, 1)"><strong><span style="font-size: 18px">perform(RequestBuilder requestBuilder)</span>----&gt;执行一个RequestBuilder请求，会自动执行SpringMvc的流程并映射到相应的控制器执行处理，该方法的返回值是一个ResultActions；</strong></span></p>
<h2>ResultActions</h2>
<h3>andExpect</h3>
<p>　　添加ResultMatcher验证规则，验证控制器执行完成后结果是否正确。</p>
<h3>andDo</h3>
<p>　　添加ResultHandler结果处理器，比如调试时打印结果到控制台；</p>
<h3>andReturn</h3>
<p>　　最后返回相应的<span style="color: rgba(255, 0, 0, 1)"><strong>MvcResult</strong></span>；然后进行自定义验证/进行下一步的异步处理。</p>
<h2>MockMvcRequestBuilders</h2>
<ol>
<li>用来构造请求</li>
<li>主要由两个子类<span style="color: rgba(255, 0, 0, 1)"><strong>MockHttpServletRequestBuilder</strong></span>和<span style="color: rgba(255, 0, 0, 1)"><strong>MockMultipartHttpServletRequestBuilder</strong></span>(如文件上传)，即用来Mock客户端请求需要的所有数据。</li>
</ol>
<h2>MockMvcResultMatchers</h2>
<ol>
<li>用来<span style="color: rgba(255, 0, 0, 1)"><strong>匹配</strong></span>执行完<span style="color: rgba(255, 0, 0, 1)"><strong>请求</strong></span>后的<span style="color: rgba(255, 0, 0, 1)"><strong>结果验证</strong></span></li>
<li>如果匹配失败将抛出相应的异常</li>
<li>包含了很多验证API方法</li>
</ol>
<h2>MockMvcResultHandlers</h2>
<ol>
<li>结果处理器，表示要对结果做点什么事情</li>
<li>比如此处使用MockMvcResultHandlers.print()输出整个相应结果信息。</li>
</ol>
<h2>MvcResult</h2>
<p>　　单元测试执行结果，可以针对执行结果进行<span style="color: rgba(255, 0, 0, 1)"><strong>自定义验证逻辑</strong></span>。</p>
<h1 style="text-align: center">MocMvc的使用</h1>
<h2>添加依赖</h2>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> spring 单元测试组件包 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.springframework<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>spring-test<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>5.0.7.RELEASE<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
 
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 单元测试Junit </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>junit<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>junit<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>4.12<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
