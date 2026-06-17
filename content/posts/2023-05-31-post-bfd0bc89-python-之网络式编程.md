---
title: "Python 之网络式编程"
date: 2023-05-31
description: "一&#160;客户端/服务器架构 即C/S架构，包括 1、硬件C/S架构（打印机） 2、软件B/S架构（web服务） C/S架构与Socket的关系： 我们学习Socket就是为了完成C/S的开发 二 OSI七层 引子： 计算机组成原理：硬件、操作系统、应用软件三者组成。 具备以上条件后，计算机就可"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10406263.html"
---

<h1>一&nbsp;客户端/服务器架构</h1>
<p>即C/S架构，包括</p>
<p>1、硬件C/S架构（打印机）</p>
<p>2、软件B/S架构（web服务）</p>
<p>C/S架构与Socket的关系：</p>
<p>我们学习Socket就是为了完成C/S的开发</p>
<h1>二 OSI七层</h1>
<p>引子：　　</p>
<p>　　计算机组成原理：硬件、操作系统、应用软件三者组成。</p>
<p>　　具备以上条件后，计算机就可以工作，如果你要和别人一起玩，那你就需要上网了。互联网的核心就是由一堆协议组成，协议就是标准。</p>
<p>&nbsp;</p>
<p>为什么学习Socket之前要先了解互联网协议？</p>
<p>　　1、C/S架构的软件（应用软件属于应用层）是基于网络进行通信的</p>
<p>　　2、网络的核心即一堆协议，协议即标准，想开发一款基于网络通信的软件，就必须遵循这些标准</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201902/1504448-20190220140518890-564668344.jpg" alt="" /></p>
<h2>OSI七层：</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201902/1504448-20190220140746962-1232225480.jpg" alt="" /></p>
<h1>三 Socket层</h1>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201902/1504448-20190220140830113-193820327.jpg" alt="" /></p>
<h1>四 Socket是什么&nbsp;</h1>
<p>　　Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口，在设计模式中，Socket其实就是一个门面模式，它把负责的TCP/IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部，让Socket去组织数据，以符合指定的协议。</p>
<p>　　所以，我们无需深入学习理解TCP/UDP协议，Socket已经为我们封装好了，我们只需要遵循Socket的规定去编程，写出的程序自然就是遵循TCP/UDP标准的。</p>
<h1>五&nbsp;套接字发展史及分类</h1>
<p>　　套接字起源于20世纪70年代加利福尼亚大学伯克利分校版本的Unix，即人们所说的BSD Unix。因此，有时人们也把套接字成为“伯克利套接字”或“BSD套接字”。一开始，套接字被设计用在一台主机上多个应用程序之间的通信，这也被称作进程间通许或IPC。套接字有两种（或者称为两个种族），分别是基于文件型和就网络型。</p>
<p><strong><span style="color: rgba(51, 102, 255, 1); font-size: 16px">基于文件类型的套接字家族</span></strong></p>
<p>套接字家族的名字：AF_UNIX</p>
<p>　　UNIX一切皆文件，基于文件的套接字调用的就是底层的文件系统来取数据，两个套接字进程运行在同一机器上，可以通过访问同一文件系统间接完成通信。</p>
<p><strong><span style="font-size: 16px; color: rgba(51, 102, 255, 1)">基于网络类型的套接字家族</span></strong></p>
<p>套接字家族的名字：AF_INET</p>
<p>　　还有AF_INET6被用于ipv6，还有一些其他的地址家族，不过，他们要么是只用于某个平台，要么就是已经被废弃，或者是很少被使用，或者是根本没有实现，所有地址家族中，AF_INET是使用最广泛的一个，Python支持很多地址家族，但是由于我们只关心网络编程，所以大部分时候我们只使用AF_INET(AF:Address Family;INET:Internet)</p>
<h1>六&nbsp;套接字工作流程</h1>
<p>　　生活中，你要打电话给一个朋友，先拨号，朋友听到电话铃声响后接打电话，这时你和你的朋友就建立起了连接，就可以讲话了，等交流结束，挂断电话结束此次通话。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201902/1504448-20190220152916548-2021261384.jpg" alt="" /></p>
<h2>&nbsp;利用Socket模拟生活中打电话：</h2>
<div class="cnblogs_code"><img id="code_img_closed_9f9211f4-20e8-4dbb-8c10-b2ba643b2fe9" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_9f9211f4-20e8-4dbb-8c10-b2ba643b2fe9" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_9f9211f4-20e8-4dbb-8c10-b2ba643b2fe9" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> socket
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 买手机;socket.AF_INET:基于网络协议;socket.SOCK_STREAM:基于流的TCP协议</span>
<span style="color: rgba(0, 128, 128, 1)"> 6</span> phone.bind((<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">127.0.0.1</span><span style="color: rgba(128, 0, 0, 1)">'</span>, 8080))  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 绑定手机卡;元祖形式，ip地址+端口</span>
<span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 注：服务器的ip地址写本机的ip地址</span>
<span style="color: rgba(0, 128, 128, 1)"> 8</span> phone.listen(5)  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 开机</span>
<span style="color: rgba(0, 128, 128, 1)"> 9</span> conn, addr = phone.accept()  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 等电话</span>
<span style="color: rgba(0, 128, 128, 1)">10</span> msg = conn.recv(1024)  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 收消息</span>
<span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">客户端发来的消息是:</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, msg)
</span><span style="color: rgba(0, 128, 128, 1)">12</span> conn.send(msg.upper())  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 发消息</span>
<span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">conn.close()
</span><span style="color: rgba(0, 128, 128, 1)">14</span> phone.close()</pre>
