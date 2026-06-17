---
title: "java 内存模型"
date: 2023-05-31
description: "为什么现在开发中强调JVM 1、当前的互联网开发环境有直接的关系：已经不再单独的面对传统的一台主机运行一些程序，而后在进行简单的维护，现在讲究的是：高并发、分布式、高可用，对于程序的调优里面就需要去考虑JVM参数设计、JUC的使用。 【面试必问内容】Java架构师(基础能力)：框架设计+通讯+多线程"
tags:
  - "JVM"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12728212.html"
---

<h1 style="text-align: center">为什么现在开发中强调JVM</h1>
<p>1、当前的互联网开发环境有直接的关系：已经不再单独的面对传统的一台主机运行一些程序，而后在进行简单的维护，现在讲究的是：<strong><span style="color: rgba(255, 0, 0, 1)">高并发、分布式、高可用</span></strong>，对于程序的调优里面就需要去考虑JVM参数设计、JUC的使用。</p>
<p>　　【面试必问内容】Java架构师(基础能力)：框架设计+通讯+多线程(JUC)+JVM+数据结构+良好的结构设计(需要大量的代码基础)</p>
<p>2、需要清楚内存模型、虚拟机分类、运行模式</p>
<p>3、不适当的<strong><span style="color: rgba(255, 0, 0, 1)">JVM运行状态</span></strong>，有可能会浪费你的<span style="color: rgba(255, 255, 0, 1)"><strong><span style="background-color: rgba(255, 0, 0, 1)">电脑性能、良好的JVM调优</span></strong></span>，可以<span style="color: rgba(255, 255, 0, 1)"><strong><span style="background-color: rgba(255, 0, 0, 1)">增加你电脑处理的负载</span></strong></span>；</p>
<p>4、GC处理流程以及常见的算法(JDK1.8、JDK1.9-JDK1.11)</p>
<h1 style="text-align: center">Java程序执行流程</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202004/1504448-20200418222126501-1769037348.png" alt="" /></p>
<p>双亲加载机制：系统类由系统类加载负责，而自定义类由其他的类加载器负责。</p>
<h2>Java运行时数据区(内存问题)</h2>
<p>1、方法区：最重要的内存区域，多线程内存共享，保存了类的信息(名称、成员、接口、父类)，反射机制是重要组成部分，动态进行类操作的实现。</p>
<p>2、<strong><span style="background-color: rgba(51, 204, 204, 1); color: rgba(255, 204, 153, 1)">堆内存(Heap)</span></strong>：保存对象的真实信息，该内存牵扯到释放问题(GC)；</p>
<p>3、<strong><span style="background-color: rgba(51, 204, 204, 1); color: rgba(255, 204, 153, 1)">栈内存(Stack)</span></strong>：线程的私有空间，在每一次进行方法调用的时候都会存在有栈帧，采用先进后出的设计原则；</p>
<p>　　3.1、本地变量表：局部参数或形参，允许保存有32位的插槽(Solt)，如果超过了32位的长度，需要开辟两个连续性的插槽(long、double)--volatile关键字问题</p>
<p>　　3.2、操作数栈：执行所有的方法计算操作</p>
<p>　　3.3、常量池引用：String类、Integer类实例</p>
<p>　　3.4、返回地址：方法执行完毕后的恢复执行点</p>
<p>4、程序计数器：执行指令的一个顺序编码，该区域的所占比率几乎可以忽略；</p>
<p>5、本地方法栈：与栈内存功能类似，区别在于是为本地方法服务的</p>
<h1 style="text-align: center">JVM分类</h1>
<p>　　Java是直接通过指针进行的程序访问，所以它没有采用句柄的形式操作，这样使得程序的性能更高。</p>
<p>　　传统意义上来讲，JVM一共分为三种(虚拟机是一个公共标准)</p>
<p>　　　　【SUN】从JDK1.2开始使用了HotSpot虚拟机标准(2006年开源，利用C++实现、一些JNI部分使用的是系统提供C程序实现的、JIT即时编译器)；</p>
<p>　　　　【BEA】使用了JRockit虚拟机标准，例如WebLogic；</p>
<p>　　　　【IBM】开发了JVM’s(J9)虚拟机；</p>
<p>　　Oracle后来通过收购得到了：SUN与BEA，那么Oracle有了两个虚拟机标准(不可能浪费两个研发团队去干相同的事情)；</p>
<h1 style="text-align: center">HotSpot</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">java version "13.0.1" 2019-10-15
Java(TM) SE Runtime Environment (build 13.0.1+9)
Java HotSpot(TM) 64-Bit Server VM (build 13.0.1+9, mixed mode, sharing)</span></pre>
