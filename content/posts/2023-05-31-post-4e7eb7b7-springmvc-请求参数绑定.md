---
title: "SpringMVC 请求参数绑定"
date: 2023-05-31
description: "什么是请求参数绑定 请求参数格式 默认是key/value格式，比如：http:xxxx?id=1&amp;type=2 请求参数值的数据类型 都是字符串类型的各种值 请求参数值要绑定的目标类型 Controller类中的方法参数，比如简单类型、POJO类型、集合类型等。 SpringMVC内置的参"
tags:
  - "JAVA"
  - "Spring"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11980465.html"
---

<h1 style="text-align: center">什么是请求参数绑定</h1>
<h2>请求参数格式</h2>
<p>　　默认是<span style="color: rgba(255, 0, 0, 1)"><strong>key/value</strong></span>格式，比如：http:xxxx?id=1&amp;type=2</p>
<h2>请求参数值的数据类型</h2>
<p>　　都是<span style="color: rgba(255, 0, 0, 1)"><strong>字符串类型</strong></span>的各种值</p>
<h2>请求参数值要绑定的目标类型</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>Controller类中的方法参数</strong></span>，比如简单类型、POJO类型、集合类型等。</p>
<h2>SpringMVC内置的<span style="color: rgba(255, 0, 0, 1)"><strong>参数解析组件</strong></span></h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>默认内置了24种参数解析组件(ArgumentResolver)</strong></span></p>
<h2>什么是参数绑定？</h2>
<p>　　就是将请求参数串中的<span style="color: rgba(255, 0, 0, 1)"><strong>value值</strong></span>获取到之后，<span style="color: rgba(255, 0, 0, 1)"><strong>在</strong></span>进行<span style="color: rgba(255, 0, 0, 1)"><strong>类型转换</strong></span>，然后将转换后的值赋值给Controller类中<span style="color: rgba(255, 0, 0, 1)"><strong>方法的形参</strong></span>，这个过程就是<span style="color: rgba(255, 0, 0, 1)"><strong>参数绑定</strong></span></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191203225957091-1690733793.png" alt="" /></p>
<p>&nbsp;</p>
<h1 style="text-align: center">&nbsp;默认支持的参数类型(Servlet API支持)</h1>
<p>Controller方法形参中可以随时添加如下类型的参数，处理适配器会自动识别并进行赋值。</p>
<ul>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>HttpServletRequest</strong></span>
<ul>
<li>通过request对象获取请求信息</li>
</ul>
</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>HttpServletResponse</strong></span>
<ul>
<li>通过response处理响应信息</li>
</ul>
</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>HttpSession</strong></span>
<ul>
<li>通过session对象获取session中存放的对象</li>
</ul>
</li>
<li>InputStream、OutputStream</li>
<li>Reader、Writer</li>
<li><strong><span style="color: rgba(255, 0, 0, 1)">Model/ModelMap</span></strong>
<ul>
<li>ModelMap继承自LinkedHashMap，Model是一个接口，它们的底层实现都是同一个类(<span style="color: rgba(255, 0, 0, 1)"><strong>BindingAwareModelMap</strong></span>)，作用就是向页面传递数据，相当于Request的作用，如下</li>
</ul>
</li>
</ul>
<h1 style="text-align: center">绑定简单数据类型</h1>
<h2>简单类型参数绑定方式</h2>
<p>　　简单类型指的就是8种基本类型数据以及它们的包装类，还有String类型。</p>
<p>　　在SpringMVC中，对于java简单类型的参数，推荐的参数绑定方式有两种：</p>
<ol>
<li><strong><span style="color: rgba(255, 0, 0, 1)">直接绑定</span></strong></li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>注解绑定</strong></span></li>
</ol>
<h2>直接绑定</h2>
<h3>要求</h3>
<p>　　http请求参数的<span style="color: rgba(255, 0, 0, 1)"><strong>key</strong></span>和controller方法的<span style="color: rgba(255, 0, 0, 1)"><strong>形参名称一致</strong></span></p>
<h3>请求URL</h3>
<p>　　http://localhose:8080/xxx/findItem?id=1</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>请求参数的key为id</strong></span></p>
<h3>Controller方法</h3>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>Controller的形参为Interger id，它和请求参数的key一致，所以直接绑定成功</strong></span></p>
<div class="cnblogs_code">
<pre>@RequestMapping(value = "/findItem"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String findItem(Integer id) {
         System.out.println(</span>"接收到的请求参数是："+<span style="color: rgba(0, 0, 0, 1)"> id);
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> "success"<span style="color: rgba(0, 0, 0, 1)">;
    }</span></pre>
