---
title: "Spring常见面试题总结"
date: 2020-06-28
description: "Spring是什么? Spring是一个轻量级的IoC和AOP容器框架。是为Java应用程序提供基础性服务的一套框架，目的是用于简化企业应用程序的开发，它使得开发者只需要关心业务需求。常见的配置方式有三种：基于XML的配置、基于注解的配置、基于Java的配置。 主要由以下几个模块组成： Spring"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13203974.html"
---

<h1>Spring是什么?</h1>
<p>　　Spring是一个轻量级的IoC和AOP容器框架。是为Java应用程序提供基础性服务的一套框架，目的是用于简化企业应用程序的开发，它使得开发者只需要关心业务需求。常见的配置方式有三种：基于XML的配置、基于注解的配置、基于Java的配置。</p>
<p>主要由以下几个模块组成：</p>
<p>　　Spring Core：核心类库，提供IOC服务；</p>
<p>　　Spring Context：提供框架式的Bean访问方式，以及企业级功能（JNDI、定时任务等）；</p>
<p>　　Spring AOP：AOP服务；</p>
<p>　　Spring DAO：对JDBC的抽象，简化了数据访问异常的处理；</p>
<p>　　Spring ORM：对现有的ORM框架的支持；</p>
<p>　　Spring Web：提供了基本的面向Web的综合特性，例如多方文件上传；</p>
<p>　　Spring MVC：提供面向Web应用的Model-View-Controller实现。</p>
<h1>Spring 的优点？</h1>
<p>（1）spring属于低侵入式设计，代码的污染极低；</p>
<p>（2）spring的DI机制将对象之间的依赖关系交由框架处理，减低组件的耦合性；</p>
<p>（3）Spring提供了AOP技术，支持将一些通用任务，如安全、事务、日志、权限等进行集中式管理，从而提供更好的复用。</p>
<p>（4）spring对于主流的应用框架提供了集成支持。</p>
<h1>Spring的AOP理解</h1>
<p>　　OOP面向对象，允许开发者定义纵向的关系，但并适用于定义横向的关系，导致了大量代码的重复，而不利于各个模块的重用。</p>
<p>　　AOP，一般称为面向切面，作为面向对象的一种补充，用于将那些与业务无关，但却对多个对象产生影响的公共行为和逻辑，抽取并封装为一个可重用的模块，这个模块被命名为“切面”（Aspect），减少系统中的重复代码，降低了模块间的耦合度，同时提高了系统的可维护性。可用于权限认证、日志、事务处理。</p>
<p>　　AOP实现的关键在于 代理模式，AOP代理主要分为静态代理和动态代理。静态代理的代表为AspectJ；动态代理则以Spring AOP为代表。</p>
<p>（1）AspectJ是静态代理的增强，所谓静态代理，就是AOP框架会在编译阶段生成AOP代理类，因此也称为编译时增强，他会在编译阶段将AspectJ(切面)织入到Java字节码中，运行的时候就是增强之后的AOP对象。</p>
<p>（2）Spring AOP使用的动态代理，所谓的动态代理就是说AOP框架不会去修改字节码，而是每次运行时在内存中临时为方法生成一个AOP对象，这个AOP对象包含了目标对象的全部方法，并且在特定的切点做了增强处理，并回调原对象的方法。</p>
<p>Spring AOP中的动态代理主要有两种方式，JDK动态代理和CGLIB动态代理：</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;①JDK动态代理只提供接口的代理，不支持类的代理。核心InvocationHandler接口和Proxy类，InvocationHandler&nbsp;通过invoke()方法反射来调用目标类中的代码，动态地将横切逻辑和业务编织在一起；接着，Proxy利用 InvocationHandler动态创建一个符合某一接口的的实例,&nbsp; 生成目标类的代理对象。</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;②如果代理类没有实现 InvocationHandler 接口，那么Spring AOP会选择使用CGLIB来动态代理目标类。CGLIB（Code Generation Library），是一个代码生成的类库，可以在运行时动态的生成指定类的一个子类对象，并覆盖其中特定方法并添加增强代码，从而实现AOP。CGLIB是通过继承的方式做的动态代理，因此如果某个类被标记为final，那么它是无法使用CGLIB做动态代理的。</p>
<p>（3）静态代理与动态代理区别在于生成AOP代理对象的时机不同，相对来说AspectJ的静态代理方式具有更好的性能，但是AspectJ需要特定的编译器进行处理，而Spring AOP则无需特定的编译器处理。</p>
<div class="cnblogs_code">
<pre>&nbsp;InvocationHandler 的 invoke(Object&nbsp;&nbsp;proxy,Method&nbsp;&nbsp;method,Object[] args)：proxy是最终生成的代理实例;&nbsp;&nbsp;method 是被代理目标实例的某个具体方法;&nbsp;&nbsp;args 是被代理目标实例某个方法的具体入参, 在方法反射调用时使用。</pre>
