---
title: "dubbo面试题及答案"
date: 2020-06-25
description: "Dubbo是什么？ Dubbo是阿里巴巴开源的基于 Java 的高性能 RPC 分布式服务框架，现已成为 Apache 基金会孵化项目。 面试官问你如果这个都不清楚，那下面的就没必要问了。 官网：http://dubbo.apache.org 为什么要用Dubbo？ 因为是阿里开源项目，国内很多互联"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13193539.html"
---

<h1>Dubbo是什么？</h1>
<p>Dubbo是阿里巴巴开源的基于 Java 的高性能 RPC 分布式服务框架，现已成为 Apache 基金会孵化项目。</p>
<p>面试官问你如果这个都不清楚，那下面的就没必要问了。</p>
<p>官网：http://dubbo.apache.org</p>
<h1>为什么要用Dubbo？</h1>
<p>因为是阿里开源项目，国内很多互联网公司都在用，已经经过很多线上考验。内部使用了 Netty、Zookeeper，保证了高性能高可用性。</p>
<p>使用 Dubbo 可以将核心业务抽取出来，作为独立的服务，逐渐形成稳定的服务中心，可用于提高业务复用灵活扩展，使前端应用能更快速的响应多变的市场需求。</p>
<p>下面这张图可以很清楚的诠释，最重要的一点是，分布式架构可以承受更大规模的并发流量。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625234551024-1679374511.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>下面是 Dubbo 的服务治理图。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625234615259-1564776234.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1>Dubbo 和 Spring Cloud 有什么区别？</h1>
<p>两个没关联，如果硬要说区别，有以下几点。</p>
<p>1）通信方式不同</p>
<p>Dubbo 使用的是 RPC 通信，而 Spring Cloud 使用的是 HTTP RESTFul 方式。</p>
<p>2）组成部分不同</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625234821272-1083979362.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1>dubbo都支持什么协议，推荐用哪种？</h1>
<ul>
<li>
<p>dubbo://（推荐）</p>
</li>
<li>
<p>rmi://</p>
</li>
<li>
<p>hessian://</p>
</li>
<li>
<p>http://</p>
</li>
<li>
<p>webservice://</p>
</li>
<li>
<p>thrift://</p>
</li>
<li>
<p>memcached://</p>
</li>
<li>
<p>redis://</p>
</li>
<li>
<p>rest://</p>
</li>
</ul>
<h1>Dubbo需要 Web 容器吗？</h1>
<p>不需要，如果硬要用 Web 容器，只会增加复杂性，也浪费资源。</p>
<h1>Dubbo内置了哪几种服务容器？</h1>
<ul>
<li>
<p>Spring Container</p>
</li>
<li>
<p>Jetty Container</p>
</li>
<li>
<p>Log4j Container</p>
</li>
</ul>
<p>Dubbo 的服务容器只是一个简单的 Main 方法，并加载一个简单的 Spring 容器，用于暴露服务。</p>
<h1>Dubbo里面有哪几种节点角色？</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625234953401-1008826764.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1>画一画服务注册与发现的流程图</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625235012227-1392177845.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>该图来自 Dubbo 官网，供你参考，如果你说你熟悉 Dubbo, 面试官经常会让你画这个图，记好了。</p>
<h1>Dubbo默认使用什么注册中心，还有别的选择吗？</h1>
<p>推荐使用 Zookeeper 作为注册中心，还有 Redis、Multicast、Simple 注册中心，但不推荐。</p>
<h1>Dubbo有哪几种配置方式？</h1>
<p>1）Spring 配置方式<br>2）Java API 配置方式</p>
<h1>Dubbo 核心的配置有哪些？</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625235149722-719441297.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>配置之间的关系见下图。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625235206870-1498404313.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1>在 Provider 上可以配置的 Consumer 端的属性有哪些？</h1>
<p>1）timeout：方法调用超时<br>2）retries：失败重试次数，默认重试 2 次<br>3）loadbalance：负载均衡算法，默认随机<br>4）actives 消费者端，最大并发调用限制</p>
<h1>Dubbo启动时如果依赖的服务不可用会怎样？</h1>
<p>Dubbo 缺省会在启动时检查依赖的服务是否可用，不可用时会抛出异常，阻止 Spring 初始化完成，默认 check="true"，可以通过 check="false" 关闭检查。</p>
<h1>Dubbo推荐使用什么序列化框架，你知道的还有哪些？</h1>
<p>推荐使用Hessian序列化，还有Duddo、FastJson、Java自带序列化。</p>
<h1>Dubbo默认使用的是什么通信框架，还有别的选择吗？</h1>
<p>Dubbo 默认使用 Netty 框架，也是推荐的选择，另外内容还集成有Mina、Grizzly。</p>
<h1>Dubbo有哪几种集群容错方案，默认是哪种？</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625235353431-799889747.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1>Dubbo有哪几种负载均衡策略，默认是哪种？</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625235411536-1418657324.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1>注册了多个同一样的服务，如果测试指定的某一个服务呢？</h1>
<p>可以配置环境点对点直连，绕过注册中心，将以服务接口为单位，忽略注册中心的提供者列表。</p>
<h1>Dubbo支持服务多协议吗？</h1>
<p>Dubbo 允许配置多协议，在不同服务上支持不同协议或者同一服务上同时支持多种协议。</p>
<h1>当一个服务接口有多种实现时怎么做？</h1>
<p>当一个接口有多种实现时，可以用 group 属性来分组，服务提供方和消费方都指定同一个 group 即可。</p>
<h1>服务上线怎么兼容旧版本？</h1>
<p>可以用版本号（version）过渡，多个不同版本的服务注册到注册中心，版本号不同的服务相互间不引用。这个和服务分组的概念有一点类似。</p>
<h1>Dubbo可以对结果进行缓存吗？</h1>
<p>可以，Dubbo 提供了声明式缓存，用于加速热门数据的访问速度，以减少用户加缓存的工作量。</p>
<h1>Dubbo服务之间的调用是阻塞的吗？</h1>
<p>默认是同步等待结果阻塞的，支持异步调用。</p>
<p>Dubbo 是基于 NIO 的非阻塞实现并行调用，客户端不需要启动多线程即可完成并行调用多个远程服务，相对多线程开销较小，异步调用会返回一个 Future 对象。</p>
<p>异步调用流程图如下。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625235619420-1458155956.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h2>Dubbo支持分布式事务吗？</h2>
<p>目前暂时不支持，后续可能采用基于 JTA/XA 规范实现，如以图所示。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202006/1504448-20200625235647122-501646360.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1>Dubbo支持服务降级吗？</h1>
<p>Dubbo 2.2.0 以上版本支持。</p>
<h1>Dubbo如何优雅停机？</h1>
<p>Dubbo 是通过 JDK 的 ShutdownHook 来完成优雅停机的，所以如果使用 kill -9 PID 等强制关闭指令，是不会执行优雅停机的，只有通过 kill PID 时，才会执行。</p>
<h1>服务提供者能实现失效踢出是什么原理？</h1>
<p>服务失效踢出基于 Zookeeper 的临时节点原理。</p>
<h1>如何解决服务调用链过长的问题？</h1>
<p>Dubbo 可以使用 Pinpoint 和 Apache Skywalking(Incubator) 实现分布式服务追踪，当然还有其他很多方案。</p>
<h1>服务读写推荐的容错策略是怎样的？</h1>
<p>读操作建议使用 Failover 失败自动切换，默认重试两次其他服务器。</p>
<p>写操作建议使用 Failfast 快速失败，发一次调用失败就立即报错。</p>
<h1>Dubbo必须依赖的包有哪些？</h1>
<p>Dubbo 必须依赖 JDK，其他为可选。</p>
