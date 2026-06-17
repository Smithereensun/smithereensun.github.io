---
title: "SpringBoot注解配置文件映射属性和实体类"
date: 2020-07-04
description: "配置文件加载 方式一 Controller上面配置@PropertySource({&quot;classpath:pay.properties&quot;}) 添加属性@Value(&quot;wxpay.appid&quot;)&#160;private String payAppid; pay"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13236903.html"
---

<h1 style="text-align: center">配置文件加载</h1>
<h2>方式一</h2>
<ul>
<li>Controller上面配置@PropertySource({"classpath:pay.properties"})</li>
<li>添加属性@Value("wxpay.appid")&nbsp;private String payAppid;</li>
</ul>
<p>pay.properties</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)"># 微信支付的appid
wxpay.appid=w23232323
# 支付密钥
wxpay.sercret=abd
# 微信支付商户号
wx.mechid=1234</span></pre>
