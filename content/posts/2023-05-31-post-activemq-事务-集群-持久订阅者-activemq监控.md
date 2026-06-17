---
title: "ActiveMQ 事务、集群、持久订阅者、ActiveMQ监控"
date: 2023-05-31
description: "JMS介绍 JMS是什么? JMS的全称Java Message Service，既Java消息服务。 JMS是SUN提供的旨在统一各种MOM(Message-Oriented Middleware)系统接口的规范，它包含点对点(Point to Point,PTP)和发布/订阅(Publish/S"
tags:
  - "Linux"
  - "MQ"
  - "负载均衡"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12841966.html"
---

<h1 style="text-align: center">JMS介绍</h1>
<h2>JMS是什么?</h2>
<p>　　JMS的全称<strong>Java Message Service</strong>，既Java消息服务。</p>
<p>　　JMS是SUN提供的旨在统一各种MOM(Message-Oriented Middleware)系统接口的规范，它包含<strong>点对点(Point to Point,PTP)</strong>和<strong>发布/订阅(Publish/Subscribe，pub/sub)</strong>两种消息模型，提供可靠<strong>消息传输、事务和消息过滤</strong>等机制。</p>
<p>　　ActiveMQ是Apache出品的开源项目，他是JMS规范的一个实现。</p>
<h2>MOM是什么？</h2>
<p>　　<strong>MOM(Message-Oriented Middleware)</strong>：<strong>面向消息的中间件</strong>，使用<strong>消息中间件</strong>来协调消息传输操作。</p>
<p>MOM需要提供API和管理工具</p>
<ul>
<li><strong>客户端</strong>调用API，把消息发送到<strong>消息中间件</strong>指定的目的地。在消息发送之后，客户端会继续执行其他的工作。</li>
<li><strong>接收方</strong>收到这个消息确认之前，<strong>消息中间件</strong>一直保留该消息。</li>
</ul>
<h2>JMS的作用是什么？</h2>
<p>　　在不同应用之间进行通信或者从一个系统传输数据到另外一个系统。两个应用程序之间，或分布式系统中发送消息，进行<strong>异步通信，程序或应用之间解耦</strong>。</p>
<p>　　它主要用于在生产者和消费者之间进行消息传递，生产者负责产生消息，而消费者负责接收消息。把它应用到实际的业务需求中的话我们可以在特定的时候利用生产者生成-消息，并进行发送，对应的消费者在接收到对应的消息后去完成对应的业务逻辑。</p>
<h2>JMS的应用场景</h2>
<p>主要可以应用于规模和复杂度较高的分布式系统：</p>
<ul>
<li><strong>异步通信</strong>：客户发出调用后，不用等待服务对象完成处理并返回结果后就能继续执行；</li>
<li><strong>客户和服务对象的生命周期解耦合</strong>：客户进行和服务对象进行不需要都正常运行；如果由于服务对象崩溃或网络故障导致客户的请求不可达，不会影响客户端正常响应；</li>
<li><strong>一对一或一对多通信</strong>：客户的一次调用可以发送给一个或多个目标对象；</li>
</ul>
<h2>JMS中的角色</h2>
<p>三种角色：<strong>生产者(<span style="color: rgba(255, 0, 0, 1)">Java应用程序</span>)、消费者(<span style="color: rgba(255, 0, 0, 1)">Java应用程序</span>)、消息中间件(<span style="color: rgba(255, 0, 0, 1)">MQ</span>)</strong></p>
<h2>JMS消息模型</h2>
<h3>点对点模型(基于队列)</h3>
<ul>
<li>消息的生产者和消费者之间没有时间上的相关性。</li>
<li>生产者把消息发送到队列中(<strong><span style="color: rgba(255, 0, 0, 1)">Queue</span></strong>)，可以有多个发送者，但只能被一个消费者消费。一个消息只能被一个消费者消费一次。</li>
<li>消费者无需订阅，当消费者未消费到消息时就会处于阻塞状态</li>
</ul>
<h3>发布者/订阅者模型(基于主题的)</h3>
<ul>
<li>生产者和消费者之间有时间上的相关性，订阅一个主题的消费者只能消费自它订阅之后发布的消息</li>
<li>生产者将消息发送到主题上(<strong><span style="color: rgba(255, 0, 0, 1)">Topic</span></strong>)</li>
<li>消费者必须先订阅，JMS规范允许提供客户端创建持久订阅</li>
</ul>
<h2>JMS消息组成</h2>
<h3>消息头</h3>
<h3>消息正文</h3>
<p>　　JMS定义了五种不同的消息正文格式，以及调用的消息类型，允许你发送并接收一些不同形式的数据，提供现有消息格式的一些级别的兼容性。</p>
<ul>
<li>StreamMessage --Java原始值得数据流</li>
<li>MapMessage --一套名称-值对</li>
<li>TextMessage --一个字符串对象</li>
<li>ObjectMessage --一个序列化的Java对象</li>
<li>BytesMessage --一个字节的数据流</li>
</ul>
<h3>消息属性</h3>
<h2>总结</h2>
<p>1、JMS是什么？是指定消息发送和接收的一套标准</p>
<p>2、JMS的角色：生产者、消费者、MOM消息中间件</p>
<p>3、JMS消息模型：点对点、发布订阅模型</p>
<p>4、JMS消息正文：Stream、Map、Text、Byte、Object</p>
<h1 style="text-align: center">ActiveMQ介绍</h1>
<h2>什么是ActiveMQ</h2>
<p>　　MQ，既Message Queue，就是消息队列的意思。</p>
<p>　　ActiveMQ是Apache出品，最流行，能力强劲的开源消息总线。ActiveMQ是一个完全支持JMS1.1和J2EE 1.4规范的JMS Provider实现，尽管JMS规范出台已经是很久的事情了，但是JMS在当今的J2EE应用中间仍然扮演着特殊地位。</p>
<h2>ActiveMQ主要特点</h2>
<ol>
<li>多种语言和协议编写客户端，语言：<a href="https://baike.baidu.com/item/C" target="_blank" rel="noopener nofollow">C</a>、<a href="https://baike.baidu.com/item/C%2B%2B" target="_blank" rel="noopener nofollow">C++</a>、<a href="https://baike.baidu.com/item/C%23" target="_blank" rel="noopener nofollow">C#</a>、<a href="https://baike.baidu.com/item/Delphi" target="_blank" rel="noopener nofollow">Delphi</a>、<a href="https://baike.baidu.com/item/Erlang" target="_blank" rel="noopener nofollow">Erlang</a>、<a href="https://baike.baidu.com/item/Adobe%20Flash" target="_blank" rel="noopener nofollow">Adobe Flash</a>、<a href="https://baike.baidu.com/item/Haskell" target="_blank" rel="noopener nofollow">Haskell</a>、<a href="https://baike.baidu.com/item/Java" target="_blank" rel="noopener nofollow">Java</a>、<a href="https://baike.baidu.com/item/JavaScript" target="_blank" rel="noopener nofollow">JavaScript</a>、<a href="https://baike.baidu.com/item/Perl" target="_blank" rel="noopener nofollow">Perl</a>、<a href="https://baike.baidu.com/item/PHP" target="_blank" rel="noopener nofollow">PHP</a>、<a href="https://baike.baidu.com/item/Pike" target="_blank" rel="noopener nofollow">Pike</a>、<a href="https://baike.baidu.com/item/Python" target="_blank" rel="noopener nofollow">Python</a>和<a href="https://baike.baidu.com/item/Ruby" target="_blank" rel="noopener nofollow">Ruby</a></li>
<li>支持<a href="https://baike.baidu.com/item/Java%E6%B6%88%E6%81%AF%E6%9C%8D%E5%8A%A1" target="_blank" rel="noopener nofollow">Java消息服务</a>(JMS) 1.1 版本</li>
<li>对Srping的支持，ActiveMQ可以很容易内嵌到使用Spring的系统里面去，而且也支持Spring2.0的特性</li>
<li>协议支持包括：OpenWire、<a href="https://baike.baidu.com/item/REST" target="_blank" rel="noopener nofollow">REST</a>、STOMP、WS-Notification、MQTT、<a href="https://baike.baidu.com/item/XMPP" target="_blank" rel="noopener nofollow">XMPP</a>以及AMQP</li>
<li>集群</li>
</ol>
<h2>ActiveMQ下载安装</h2>
<h3>下载</h3>
<div class="cnblogs_code">
<pre>http://activemq.apache.org/components/classic/download/</pre>
