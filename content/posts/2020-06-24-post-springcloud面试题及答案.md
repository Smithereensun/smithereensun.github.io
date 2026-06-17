---
title: "SpringCloud面试题及答案"
date: 2020-06-24
description: "什么是 spring cloud？ spring cloud 是一系列框架的有序集合。它利用 spring boot 的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中心、消息总线、负载均衡、断路器、数据监控等，都可以用 spring boot 的开发风格做到一键启动和部署。"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13186510.html"
---

<h2><strong>什么是 spring cloud？</strong></h2>
<p><strong>　　spring cloud 是一系列框架的有序集合。它利用 spring boot 的开发便利性巧妙地简化了分布式系统基础设施的开发，如服务发现注册、配置中心、消息总线、负载均衡、断路器、数据监控等，都可以用 spring boot 的开发风格做到一键启动和部署。</strong></p>
<h2><strong>spring cloud 断路器的作用是什么？</strong></h2>
<p><strong>　　在分布式架构中，断路器模式的作用也是类似的，当某个服务单元发生故障（类似用电器发生短路）之后，通过断路器的故障监控（类似熔断保险丝），向调用方返回一个错误响应，而不是长时间的等待。这样就不会使得线程因调用故障服务被长时间占用不释放，避免了故障在分布式系统中的蔓延。</strong></p>
<h2><strong>spring cloud 的核心组件有哪些？</strong></h2>
<ul class="list-paddingleft-2">
<li>
<p>Eureka：服务注册于发现。</p>
</li>
<li>
<p>Feign：基于动态代理机制，根据注解和选择的机器，拼接请求 url 地址，发起请求。</p>
</li>
<li>
<p>Ribbon：实现负载均衡，从一个服务的多台机器中选择一台。</p>
</li>
<li>
<p>Hystrix：提供线程池，不同的服务走不同的线程池，实现了不同服务调用的隔离，避免了服务雪崩的问题。</p>
</li>
<li>
<p>Zuul：网关管理，由 Zuul 网关转发请求给对应的服务。</p>
</li>
</ul>
<h2>SpringCloud和Dubbo</h2>
<p>SpringCloud和Dubbo都是现在主流的微服务架构<br>SpringCloud是Apache旗下的Spring体系下的微服务解决方案<br>Dubbo是阿里系的分布式服务治理框架<br>从技术维度上,其实SpringCloud远远的超过Dubbo,Dubbo本身只是实现了服务治理,而SpringCloud现在以及有21个子项目以后还会更多<br>所以其实很多人都会说Dubbo和SpringCloud是不公平的<br>但是由于RPC以及注册中心元数据等原因,在技术选型的时候我们只能二者选其一,所以我们常常为用他俩来对比<br>服务的调用方式Dubbo使用的是RPC远程调用,而SpringCloud使用的是 Rest API,其实更符合微服务官方的定义<br>服务的注册中心来看,Dubbo使用了第三方的ZooKeeper作为其底层的注册中心,实现服务的注册和发现,SpringCloud使用Spring Cloud Netflix Eureka实现注册中心,当然SpringCloud也可以使用ZooKeeper实现,但一般我们不会这样做<br>服务网关,Dubbo并没有本身的实现,只能通过其他第三方技术的整合,而SpringCloud有Zuul路由网关,作为路由服务器,进行消费者的请求分发,SpringCloud还支持断路器,与git完美集成分布式配置文件支持版本控制,事务总线实现配置文件的更新与服务自动装配等等一系列的微服务架构要素</p>
<h3><strong>从技术选型上讲~</strong></h3>
<p>目前国内的分布式系统选型主要还是Dubbo毕竟国产,而且国内工程师的技术熟练程度高,并且Dubbo在其他维度上的缺陷可以由其他第三方框架进行集成进行弥补<br>而SpringCloud目前是国外比较流行,当然我觉得国内的市场也会慢慢的偏向SpringCloud,就连刘军作为Dubbo重启的负责人也发表过观点,Dubbo的发展方向是积极适应SpringCloud生态,并不是起冲突</p>
<h3><strong>Rest和RPC对比</strong></h3>
<p>其实如果仔细阅读过微服务提出者马丁福勒的论文的话可以发现其定义的服务间通信机制就是Http Rest<br>RPC最主要的缺陷就是服务提供方和调用方式之间依赖太强,我们需要为每一个微服务进行接口的定义,并通过持续继承发布,需要严格的版本控制才不会出现服务提供和调用之间因为版本不同而产生的冲突<br>而REST是轻量级的接口,服务的提供和调用不存在代码之间的耦合,只是通过一个约定进行规范,但也有可能出现文档和接口不一致而导致的服务集成问题,但可以通过swagger工具整合,是代码和文档一体化解决,所以REST在分布式环境下比RPC更加灵活<br>这也是为什么当当网的DubboX在对Dubbo的增强中增加了对REST的支持的原因</p>
<h3><strong>文档质量和社区活跃度</strong></h3>
<p>SpringCloud社区活跃度远高于Dubbo,毕竟由于梁飞团队的原因导致Dubbo停止更新迭代五年,而中小型公司无法承担技术开发的成本导致Dubbo社区严重低落,而SpringCloud异军突起,迅速占领了微服务的市场,背靠Spring混的风生水起<br>Dubbo经过多年的积累文档相当成熟,对于微服务的架构体系各个公司也有稳定的现状</p>
<h2>SpringBoot和SpringCloud</h2>
<p>SpringBoot是Spring推出用于解决传统框架配置文件冗余,装配组件繁杂的基于Maven的解决方案,旨在快速搭建单个微服务<br>而SpringCloud专注于解决各个微服务之间的协调与配置,服务之间的通信,熔断,负载均衡等<br>技术维度并相同,并且SpringCloud是依赖于SpringBoot的,而SpringBoot并不是依赖与SpringCloud,甚至还可以和Dubbo进行优秀的整合开发</p>
<p>总结:</p>
<ul class="list-paddingleft-2">
<ul class="list-paddingleft-2">
<li>
<p>SpringBoot专注于快速方便的开发单个个体的微服务</p>

</li>
<li>
<p>SpringCloud是关注全局的微服务协调整理治理框架,整合并管理各个微服务,为各个微服务之间提供,配置管理,服务发现,断路器,路由,事件总线等集成服务</p>

</li>
<li>
<p>SpringBoot不依赖于SpringCloud,SpringCloud依赖于SpringBoot,属于依赖关系</p>

</li>
<li>
<p>SpringBoot专注于快速,方便的开发单个的微服务个体,SpringCloud关注全局的服务治理框架</p>

</li>

</ul>
</ul>
<h2>微服务之间是如何独立通讯的</h2>
<p>1.远程过程调用（Remote Procedure Invocation）：</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;也就是我们常说的服务的注册与发现</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;直接通过远程过程调用来访问别的service。</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;优点：</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;简单，常见,因为没有中间件代理，系统更简单</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;缺点：</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;只支持请求/响应的模式，不支持别的，比如通知、请求/异步响应、发布/订阅、发布/异步响应</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;降低了可用性，因为客户端和服务端在请求过程中必须都是可用的</p>
<p>2.消息：</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;使用异步消息来做服务间通信。服务间通过消息管道来交换消息，从而通信。</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;优点:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;把客户端和服务端解耦，更松耦合</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;提高可用性，因为消息中间件缓存了消息，直到消费者可以消费</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;支持很多通信机制比如通知、请求/异步响应、发布/订阅、发布/异步响应</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;缺点:</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp;消息中间件有额外的复杂</p>
<h2>负载均衡的意义是什么?</h2>
<p>在计算中，负载均衡可以改善跨计算机，计算机集群，网络链接，中央处理单元或磁盘驱动器等多种计算资源的工作负载分布。负载均衡旨在优化资源使用，最大吞吐量，最小响应时间并避免任何单一资源的过载。使用多个组件进行负载均衡而不是单个组件可能会通过冗余来提高可靠性和可用性。负载平衡通常涉及专用软件或硬件，例如多层交换机或域名系统服务进程。</p>
<h2>springcloud如何实现服务的注册?</h2>
<p>1.服务发布时，指定对应的服务名,将服务注册到 注册中心(eureka zookeeper)<br>2.注册中心加@EnableEurekaServer,服务用@EnableDiscoveryClient，然后用ribbon或feign进行服务直接的调用发现。</p>
<h2>什么是服务熔断?什么是服务降级</h2>
<p>在复杂的分布式系统中,微服务之间的相互调用,有可能出现各种各样的原因导致服务的阻塞,在高并发场景下,服务的阻塞意味着线程的阻塞,导致当前线程不可用,服务器的线程全部阻塞,导致服务器崩溃,由于服务之间的调用关系是同步的,会对整个微服务系统造成服务雪崩</p>
<p>为了解决某个微服务的调用响应时间过长或者不可用进而占用越来越多的系统资源引起雪崩效应就需要进行服务熔断和服务降级处理。</p>
<p>所谓的服务熔断指的是某个服务故障或异常一起类似显示世界中的“保险丝"当某个异常条件被触发就直接熔断整个服务，而不是一直等到此服务超时。</p>
<p>服务熔断就是相当于我们电闸的保险丝,一旦发生服务雪崩的,就会熔断整个服务,通过维护一个自己的线程池,当线程达到阈值的时候就启动服务降级,如果其他请求继续访问就直接返回fallback的默认值</p>
<h2><strong>微服务的优缺点分别是什么?说下你在项目开发中碰到的坑</strong></h2>
<p><strong>优点</strong></p>
<ul class="list-paddingleft-2">
<li>
<p>每一个服务足够内聚,代码容易理解</p>
</li>
<li>
<p>开发效率提高,一个服务只做一件事</p>
</li>
<li>
<p>微服务能够被小团队单独开发</p>
</li>
<li>
<p>微服务是松耦合的,是有功能意义的服务</p>
</li>
<li>
<p>可以用不同的语言开发,面向接口编程</p>
</li>
<li>
<p>易于与第三方集成</p>
</li>
<li>
<p>微服务只是业务逻辑的代码,不会和HTML,CSS或者其他界面组合</p>
</li>
</ul>
<p>&nbsp; &nbsp; &nbsp; &nbsp; 开发中,两种开发模式<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;前后端分离<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;全栈工程师</p>
<ul class="list-paddingleft-2">
<li>
<p>可以灵活搭配,连接公共库/连接独立库</p>

</li>

</ul>
<p><strong>缺点</strong></p>
<ul class="list-paddingleft-2">
<ul class="list-paddingleft-2">
<li>
<p>分布式系统的负责性</p>

</li>
<li>
<p>多服务运维难度,随着服务的增加,运维的压力也在增大</p>

</li>
<li>
<p>系统部署依赖</p>

</li>
<li>
<p>服务间通信成本</p>

</li>
<li>
<p>数据一致性</p>

</li>
<li>
<p>系统集成测试</p>

</li>
<li>
<p>性能监控</p>

</li>

</ul>
</ul>
<h2>你所知道的微服务技术栈？</h2>
<ul>
<li>维度(springcloud)</li>
<li>服务开发：springboot spring springmvc</li>
<li>服务配置与管理:Netfix公司的Archaiusm ,阿里的Diamond</li>
<li>服务注册与发现:Eureka,Zookeeper</li>
<li>服务调用:Rest RPC gRpc</li>
<li>服务熔断器:Hystrix</li>
<li>服务负载均衡:Ribbon Nginx</li>
<li>服务接口调用:Fegin</li>
<li>消息队列:Kafka Rabbitmq activemq</li>
<li>服务配置中心管理:SpringCloudConfig</li>
<li>服务路由（API网关）Zuul</li>
<li>事件消息总线:SpringCloud Bus</li>
</ul>
<h2>Eureka和ZooKeeper都可以提供服务注册与发现的功能,请说说两个的区别</h2>
<p>1.ZooKeeper保证的是CP,Eureka保证的是AP</p>
<p>ZooKeeper在选举期间注册服务瘫痪,虽然服务最终会恢复,但是选举期间不可用的</p>
<p>Eureka各个节点是平等关系,只要有一台Eureka就可以保证服务可用,而查询到的数据并不是最新的</p>
<p>自我保护机制会导致</p>
<p>Eureka不再从注册列表移除因长时间没收到心跳而应该过期的服务</p>
<p>Eureka仍然能够接受新服务的注册和查询请求,但是不会被同步到其他节点(高可用)</p>
<p>当网络稳定时,当前实例新的注册信息会被同步到其他节点中(最终一致性)</p>
<p>Eureka可以很好的应对因网络故障导致部分节点失去联系的情况,而不会像ZooKeeper一样使得整个注册系统瘫痪</p>
<p>2.ZooKeeper有Leader和Follower角色,Eureka各个节点平等</p>
<p>3.ZooKeeper采用过半数存活原则,Eureka采用自我保护机制解决分区问题</p>
<p>4.Eureka本质上是一个工程,而ZooKeeper只是一个进程</p>
<h2>eureka自我保护机制是什么?</h2>
<p>当Eureka Server 节点在短时间内丢失了过多实例的连接时（比如网络故障或频繁启动关闭客户端）节点会进入自我保护模式，保护注册信息，不再删除注册数据，故障恢复时，自动退出自我保护模式。</p>
<h2>什么是Ribbon？</h2>
<p>ribbon是一个负载均衡客户端，可以很好的控制htt和tcp的一些行为。feign默认集成了ribbon。</p>
<h2>什么是feigin？它的优点是什么？</h2>
<p>1.feign采用的是基于接口的注解<br>2.feign整合了ribbon，具有负载均衡的能力<br>3.整合了Hystrix，具有熔断的能力</p>
<p>使用:<br>1.添加pom依赖。<br>2.启动类添加@EnableFeignClients<br>3.定义一个接口@FeignClient(name=“xxx”)指定调用哪个服务</p>
<h2>Ribbon和Feign的区别？</h2>
<p>1.Ribbon都是调用其他服务的，但方式不同。<br>2.启动类注解不同，Ribbon是@RibbonClient feign的是@EnableFeignClients<br>3.服务指定的位置不同，Ribbon是在@RibbonClient注解上声明，Feign则是在定义抽象方法的接口中使用@FeignClient声明。<br>4.调用方式不同，Ribbon需要自己构建http请求，模拟http请求然后使用RestTemplate发送给其他服务，步骤相当繁琐。Feign需要将调用的方法定义成抽象方法即可。</p>
<h2>什么是Hystrix?</h2>
<p>防雪崩利器，具备服务降级，服务熔断，依赖隔离，监控（Hystrix Dashboard）<br>服务降级:<br>双十一 提示 哎哟喂，被挤爆了。 app秒杀 网络开小差了，请稍后再试。<br>优先核心服务，非核心服务不可用或弱可用。通过HystrixCommand注解指定。<br>fallbackMethod(回退函数)中具体实现降级逻辑。</p>
