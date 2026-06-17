---
title: "SpringBoot+Websocket 打造实时聊天、实时监听JVM负载"
date: 2022-07-03
description: "WebSocket 介绍 WebSocket协议是基于TCP的一种新的网络协议。它实现了浏览器与服务器全双工(full-duplex)通信——允许服务器主动发送信息给客户端 使用场景 弹幕 网页聊天系统 实时监控 股票行情推送​ 单播 点对点，私信私聊方式 广播 游戏公告，发布订阅 多播(也叫组播)"
tags:
  - "Spring Boot"
  - "websocket"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/16438809.html"
---

<h1 style="text-align: center">WebSocket</h1>
<h2 style="text-align: left">介绍</h2>
<p>　　WebSocket协议是基于TCP的一种新的网络协议。它实现了浏览器与服务器全双工(full-duplex)通信——允许服务器主动发送信息给客户端</p>
<h2>使用场景</h2>
<ul>
<li>弹幕</li>
<li>网页聊天系统</li>
<li>实时监控</li>
<li>股票行情推送​</li>
</ul>
<h3>单播</h3>
<p>　　点对点，私信私聊方式</p>
<h3>广播</h3>
<p>　　游戏公告，发布订阅</p>
<h3>多播(也叫组播)</h3>
<p>　　多人聊天，发布订阅</p>
<h1 class=" CodeMirror-line " style="text-align: center"><span class="cm-tab-wrap-hack">socketjs</span></h1>
<h2>介绍</h2>
<ol>
<li>是一个浏览器JavaScript库，提供了一个类似WebSocket的对象。</li>
<li>提供了一个连贯的跨浏览器的JavaScriptAPI，在浏览器和Web服务器之间创建了一个低延迟，全双工，跨域的通信通道</li>
<li>在底层SockJS首先尝试使用本地WebSocket。如果失败了，它可以使用各种浏览器特定的传输协议，并通过类似WebSocket的抽象方式呈现它们</li>
<li>SockJS旨在适用于所有现代浏览器和不支持WebSocket协议的环境。</li>
</ol>
<h2 class=" CodeMirror-line "><span>git地址</span></h2>
<p class=" CodeMirror-line "><a href="https://github.com/sockjs/sockjs-client" target="_blank" rel="noopener nofollow"><span>https://github.com/sockjs/sockjs-client</span></a></p>
<h1 class=" CodeMirror-line " style="text-align: center"><span>stompjs</span></h1>
<h2>介绍</h2>
<p class=" CodeMirror-line "><span>　　STOMP Simple (or Streaming) Text Orientated Messaging Protocol </span>它定义了可互操作的连线格式，以便任何可用的STOMP客户端都可以与任何STOMP消息代理进行通信，以在语言和平台之间提供简单而广泛的消息互操作性（归纳一句话：是一个简单的面向文本的消息传递协议。）</p>
<h2>官网</h2>
<p><a href="http://jmesnil.net/stomp-websocket/doc/" target="_blank" rel="noopener nofollow">http://jmesnil.net/stomp-websocket/doc/</a></p>
<p><a href="https://stomp-js.github.io/stomp-websocket/codo/class/Client.html" target="_blank" rel="noopener nofollow">https://stomp-js.github.io/stomp-websocket/codo/class/Client.html</a></p>
<p>&nbsp;</p>
<h1 style="text-align: center">SpringBoot第一个案例(游戏公告通知)</h1>
<h2>项目结构</h2>
<p><img src="https://img2022.cnblogs.com/blog/1504448/202207/1504448-20220703163649502-380948935.png" alt="" loading="lazy" /></p>
<h2>添加依赖</h2>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.springframework.boot<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>spring-boot-starter-websocket<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>

        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.projectlombok<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>lombok<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.18.24<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
