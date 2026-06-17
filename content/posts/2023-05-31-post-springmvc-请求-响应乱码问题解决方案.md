---
title: "SpringMVC 请求/响应乱码问题解决方案"
date: 2023-05-31
description: "请求乱码解决之get乱码问题 GET请求乱码原因分析 GET请求参数是通过请求行中的URL发送给Web服务器(Tomcat)的。 Tomcat服务器会对URL进行编码操作(此时使用的是Tomcat设置的字符集，默认是iso8859-1) 到了我们的应用程序中的请求参数，已经是被Tomcat使用ISO"
tags:
  - "JAVA"
  - "Spring"
  - "Spring MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11986503.html"
---

<h1 style="text-align: center">请求乱码解决之get乱码问题</h1>
<h2>GET请求乱码原因分析</h2>
<p>　　GET<span style="color: rgba(255, 0, 0, 1)"><strong>请求参数</strong></span>是通过<span style="color: rgba(255, 0, 0, 1)"><strong>请求行中的URL</strong></span>发送给Web服务器(Tomcat)的。</p>
<p>　　Tomcat服务器会对URL进行编码操作(<span style="color: rgba(255, 0, 0, 1)"><strong>此时使用的是Tomcat设置的字符集，默认是iso8859-1</strong></span>)</p>
<p>　　到了我们的应用程序中的请求参数，已经是被Tomcat使用ISO8859-1字符集进行编码之后的了。</p>
<h2>解决方式</h2>
<h3>方式一</h3>
<p>修改tomcat配置文件，指定UTF-8编码，如下：</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">Connector </span><span style="color: rgba(255, 0, 0, 1)">URIEncoding</span><span style="color: rgba(0, 0, 255, 1)">="utf-8"</span><span style="color: rgba(255, 0, 0, 1)"> connectionTimeout</span><span style="color: rgba(0, 0, 255, 1)">="20000"</span><span style="color: rgba(255, 0, 0, 1)"> port</span><span style="color: rgba(0, 0, 255, 1)">="8080"</span><span style="color: rgba(255, 0, 0, 1)"> protocol</span><span style="color: rgba(0, 0, 255, 1)">="HTTP/1.1"</span><span style="color: rgba(255, 0, 0, 1)"> redirectPort</span><span style="color: rgba(0, 0, 255, 1)">="8443"</span><span style="color: rgba(0, 0, 255, 1)">/&gt;</span></pre>
