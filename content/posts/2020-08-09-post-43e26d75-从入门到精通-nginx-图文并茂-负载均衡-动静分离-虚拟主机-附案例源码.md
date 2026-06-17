---
title: "从入门到精通-Nginx，图文并茂、负载均衡、动静分离、虚拟主机 附案例源码"
date: 2020-08-09
description: "导读 篇幅较长，干货满满，需花费较长时间，转载请注明出处！ Nginx概述 简介 Nginx&#160;(engine x) 是一个高性能的HTTP和反向代理web服务器，同时也提供了IMAP/POP3/SMTP服务。Nginx是由伊戈尔&#183;赛索耶夫为俄罗斯访问量第二的Rambler.ru站"
tags:
  - "Nginx"
  - "负载均衡"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12521296.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　<span style="font-family: 隶书">篇幅较长，干货满满，需花费较长时间，转载请注明出处！<br></span></p>
<h1 style="text-align: center">Nginx概述</h1>
<h2 style="text-align: left">简介</h2>
<p><em>　　Nginx</em>&nbsp;(engine x) 是一个<span style="color: rgba(255, 0, 0, 1)"><strong>高性能</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>HTTP</strong></span>和<span style="color: rgba(255, 0, 0, 1)"><strong>反向代理web服务器</strong></span>，同时也提供了IMAP/POP3/SMTP服务。Nginx是由伊戈尔·赛索耶夫为俄罗斯访问量第二的Rambler.ru站点（俄文：Рамблер）开发的，第一个公开版本0.1.0发布于2004年10月4日。</p>
<p>　　Nginx是<span style="color: rgba(255, 0, 0, 1)"><strong>一款轻量级</strong></span>的Web&nbsp;服务器/反向代理服务器及电子邮件（IMAP/POP3）<span style="color: rgba(255, 0, 0, 1)"><strong>代理服务器</strong></span>，在BSD-like 协议下发行。其特点是<span style="color: rgba(255, 0, 0, 1)"><strong>占有内存少</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>并发</strong></span>能力<span style="color: rgba(255, 0, 0, 1)"><strong>强</strong></span>，事实上nginx的并发能力在同类型的网页服务器中表现较好，中国大陆使用nginx网站用户有：百度、京东、新浪、网易、腾讯、淘宝等。</p>
<h2>代理服务器</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>代理服务器根据</strong></span>其<span style="color: rgba(255, 0, 0, 1)"><strong>代理对象</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>不同</strong></span>，可以<span style="color: rgba(255, 0, 0, 1)"><strong>分为正向代理服务器与反向代理服务器</strong></span>。这里的“正”与“反”均是站在客户端角度来说的。</p>
<h2>正向代理</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>正向代理是对客户端</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>代理</strong></span>。<span style="color: rgba(255, 0, 0, 1)"><strong>客户端C</strong></span>想<span style="color: rgba(255, 0, 0, 1)"><strong>要</strong></span>从<span style="color: rgba(255, 0, 0, 1)"><strong>服务端S获取资源</strong></span>，但<span style="color: rgba(255, 0, 0, 1)"><strong>由</strong><strong>于某些原因</strong></span><span style="color: rgba(255, 0, 0, 1)"><strong>不能</strong><strong>直接访问服务端</strong></span>，而是<span style="color: rgba(255, 0, 0, 1)"><strong>通过</strong><strong>另外</strong></span>一台<span style="color: rgba(255, 0, 0, 1)"><strong>主机P向服务端发送请求</strong></span>。当<span style="color: rgba(255, 0, 0, 1)"><strong>服务端处理完毕</strong></span>请求<span style="color: rgba(255, 0, 0, 1)"><strong>后</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>将响应发</strong></span>送<span style="color: rgba(255, 0, 0, 1)"><strong>给</strong><strong>主机P</strong></span>，主机<span style="color: rgba(255, 0, 0, 1)"><strong>P</strong></span>在<span style="color: rgba(255, 0, 0, 1)"><strong>接收</strong></span>到来自<span style="color: rgba(255, 0, 0, 1)"><strong>服务端的响应后</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>将响应又转给</strong></span>了<span style="color: rgba(255, 0, 0, 1)"><strong>客户端C</strong></span>。此时的<span style="color: rgba(255, 0, 0, 1)"><strong>主机P</strong></span>，就<span style="color: rgba(255, 0, 0, 1)"><strong>称为客户端C</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>正向代理服务器</strong></span>。</p>
<p>　　客户端在使用正向代理服务器时是知道其要访问的目标服务器的地址等信息的。</p>
<p>　　正向代理服务器是服务器的用户(客户端)架设的主机，与服务器无关，正向代理服务器的出现，使服务端根本就不知道真正客户端的存在。</p>
<h2>反向代理</h2>
<p>　　反向代理，其实客户端对代理是无感知的，因为<span style="color: rgba(255, 0, 0, 1)"><strong>客户端不</strong></span>需要任何<span style="color: rgba(255, 0, 0, 1)"><strong>配置</strong></span>就可以访问，我们<span style="color: rgba(255, 0, 0, 1)"><strong>只</strong></span>需要<span style="color: rgba(255, 0, 0, 1)"><strong>将请求</strong><strong>发</strong></span>送到<span style="color: rgba(255, 0, 0, 1)"><strong>反向代理服务器</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>由反向代理服务器</strong></span>去<span style="color: rgba(255, 0, 0, 1)"><strong>选择目标服务器</strong></span>获取数据后，在<span style="color: rgba(255, 0, 0, 1)"><strong>将响应</strong></span>返回<span style="color: rgba(255, 0, 0, 1)"><strong>给客户端</strong></span>，此时反向代理服务器和目标服务器对外就是一个服务器，<span style="color: rgba(255, 0, 0, 1)"><strong>暴露的是代理服务器地址，隐藏了真实服务器IP地址</strong></span>。</p>
<h2>两者区别</h2>
<p>　　在知乎上找了2张图，可以帮助我们更好的理解。</p>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200319000108778-1079230454.png" alt="" />&nbsp;</p>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200319000121704-9929620.png" alt="" /></p>
<h2>Nginx的特点</h2>
<ul>
<li>高并发</li>
<li>低消耗</li>
<li>热部署</li>
<li>高扩展</li>
<li>高可用</li>






</ul>
<h2>Nginx的web请求处理机制</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>Nginx</strong></span>结合<span style="color: rgba(255, 0, 0, 1)"><strong>多进程</strong></span>机制和<span style="color: rgba(255, 0, 0, 1)"><strong>异步</strong></span>机制<span style="color: rgba(255, 0, 0, 1)"><strong>对外提供服务</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>异步</strong></span>机制使用的<span style="color: rgba(255, 0, 0, 1)"><strong>是异步非阻塞</strong></span>方式。Nginx的master进程会生成多个worker进程，<span style="color: rgba(255, 0, 0, 1)"><strong>master</strong></span>进程<span style="color: rgba(255, 0, 0, 1)"><strong>负责管理</strong></span>这些<span style="color: rgba(255, 0, 0, 1)"><strong>worker进程</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>生命周期</strong></span>、<span style="color: rgba(255, 0, 0, 1)"><strong>接受外部命令</strong></span>、<span style="color: rgba(255, 0, 0, 1)"><strong>解析perl脚本等</strong></span>。而<span style="color: rgba(255, 0, 0, 1)"><strong>worker</strong></span>进程则<span style="color: rgba(255, 0, 0, 1)"><strong>用于接受和处理客户端请求</strong></span>。</p>
<p>　　每个worker进程能够使用异步非阻塞方式处理多个客户端请求。当某个worker进程接收到客户端的请求后，会调用IO进程处理，如果不能立即得到结果，worker进程就去处理其他的请求。当IO返回结果后，就会通知worker进程，而worker进程得到通知后，就会挂起当前正在处理的事务，拿IO返回结果去响应客户端请求，<span style="color: rgba(255, 0, 0, 1)"><strong>worker</strong></span>进程<span style="color: rgba(255, 0, 0, 1)"><strong>采用</strong></span>的是<span style="color: rgba(255, 0, 0, 1)"><strong>epoll事件驱动模型</strong></span>与<span style="color: rgba(255, 0, 0, 1)"><strong>IO进行通信</strong></span>的。epoll模型底层采用的是“回调callback”代替里轮询，使效率高于select模型。</p>
<h1 style="text-align: center">Nginx的下载与安装</h1>
<h2>Nginx的下载</h2>
<p>nginx的官网：http://nginx.org/</p>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200319205945376-971529772.png" alt="" /></p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>注：主线版，是最新的版本；稳定版，推荐生产环境下使用；旧版，以前的版本。</strong></span></p>
<h3>百度云盘地址</h3>
<div class="cnblogs_code">
<pre>链接:https://pan.baidu.com/s/1kjQST_x1Sf_thg3XDmqx6w  密码:18sc</pre>
