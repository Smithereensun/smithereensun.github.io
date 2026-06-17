---
title: "Spring AOP里的静态代理和动态代理，你真的了解嘛？"
date: 2023-05-31
description: "什么是代理？ 为某一个对象创建一个代理对象，程序不直接用原本的对象，而是由创建的代理对象来控制原对象，通过代理类这中间一层，能有效控制对委托类对象的直接访问，也可以很好地隐藏和保护委托类对象，同时也为实施不同控制策略预留了空间 什么是静态代理？ 由程序创建或特定工具自动生成源代码，在程序运行前，代理"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13306055.html"
---

<h1 style="text-align: center">什么是代理？</h1>
<p>　　为某一个对象创建一个代理对象，程序不直接用原本的对象，而是由创建的代理对象来控制原对象，通过代理类这中间一层，能有效控制对委托类对象的直接访问，也可以很好地隐藏和保护委托类对象，同时也为实施不同控制策略预留了空间</p>
<h1 style="text-align: center">什么是静态代理？</h1>
<p>　　由程序创建或特定工具自动生成源代码，在程序运行前，代理类的.class文件就已经存在</p>
<p>　　通过将目标类与代理类实现同一个接口，让代理类持有真实类对象，然后在代理类方法中调用真实类方法，在调用真实类方法的前后添加我们所需要的功能扩展代码来达到增强的目的。</p>
<h2>优点</h2>
<p>　　代理使客户端不需要知道实现类是什么，怎么做，而客户端只需知道代理即可</p>
<p>　　方便增加功能，扩展业务逻辑</p>
<h2>缺点</h2>
<p>　　代理类中常出现大量冗余的代码，非常不利于扩展和维护</p>
<p>　　如果接口增加一个方法，除了所有实现类需要实现这个方法外，所有代理类也需要实现此方法。增加了代码维护的复杂度</p>
<h2>案例演示</h2>
<h3>PayService.java（<span style="color: rgba(255, 0, 0, 1)">接口</span>）</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.proxy;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">interface</span><span style="color: rgba(0, 0, 0, 1)"> PayService {
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 支付回调
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> outTradeNo 订单号
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    String callback(String outTradeNo);

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 下单
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> userId 用户id
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> productId 产品id
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">int</span> save(<span style="color: rgba(0, 0, 255, 1)">int</span> userId,<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> productId);
}</span></pre>
