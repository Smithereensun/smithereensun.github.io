---
title: "JVM 诊断神器-Arthas实战"
date: 2023-06-05
description: "什么是Arthas(阿尔萨斯） 阿里开源的Java诊断工具，它可以在运行时对Java应用程序进行动态诊断和调试 当你遇到以下类似问题而束手无策时，Arthas可以帮助你解决 这个类从哪个 jar 包加载的？为什么会报各种类相关的 Exception？ 我改的代码为什么没有执行到？难道是我没 comm"
tags:
  - "JVM"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/arthas.html"
---

<h1 style="text-align: center">什么是Arthas(阿尔萨斯）</h1>
<ul>
<li>
<p>阿里开源的Java诊断工具，它可以在运行时对Java应用程序进行动态诊断和调试</p>
</li>
<li>
<p>当你遇到以下类似问题而束手无策时，<code>Arthas</code>可以帮助你解决</p>
<ul>
<li>这个类从哪个 jar 包加载的？为什么会报各种类相关的 Exception？</li>
<li>我改的代码为什么没有执行到？难道是我没 commit？分支搞错了？</li>
<li>遇到问题无法在线上 debug，难道只能通过加日志再重新发布吗？</li>
<li>线上遇到某个用户的数据处理有问题，但线上同样无法 debug，线下无法重现！</li>
<li>是否有一个全局视角来查看系统的运行状况？</li>
<li>有什么办法可以监控到 JVM 的实时运行状态？</li>
<li>怎么快速定位应用的热点，生成火焰图？</li>
<li>怎样直接从 JVM 内查找某个类的实例？</li>
</ul>
</li>
<li>
<p>地址</p>
<ul>
<li>github：<a class="url" href="https://github.com/alibaba/arthas" target="_blank" rel="noopener nofollow">https://github.com/alibaba/arthas</a></li>
<li>官网：<a class="url" href="https://arthas.aliyun.com/" target="_blank" rel="noopener nofollow">https://arthas.aliyun.com/</a></li>
<li>版本：Arthas-3.6.9</li>
</ul>
</li>
</ul>
<h2>环境说明</h2>
<p><code>　　<strong><span style="color: rgba(255, 0, 0, 1)">Arthas</span></strong></code><strong><span style="color: rgba(255, 0, 0, 1)">&nbsp;支持 JDK 6+</span></strong>，支持 Linux/Mac/Windows，采用命令行交互模式，同时提供丰富的&nbsp;<code>Tab</code>&nbsp;自动补全功能，进一步方便进行问题的定位和诊断。</p>
<h1 style="text-align: center">安装&amp;下载</h1>
<h2>方式一</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">curl -O https://arthas.aliyun.com/math-game.jar
java -jar math-game.jar</span></pre>
