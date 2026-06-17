---
title: "Spring Boot面试题"
date: 2020-07-01
description: "什么是 Spring Boot？ Spring Boot 是 Spring 开源组织下的子项目，是 Spring 组件一站式解决方案，主要是简化了使用 Spring 的难度，简省了繁重的配置，提供了各种启动器，开发者能快速上手。 更多 Spring Boot 详细介绍请看这篇文章《什么是Spring"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13220008.html"
---

<h1>什么是 Spring Boot？</h1>
<p>Spring Boot 是 Spring 开源组织下的子项目，是 Spring 组件一站式解决方案，主要是简化了使用 Spring 的难度，简省了繁重的配置，提供了各种启动器，开发者能快速上手。</p>
<p>更多 Spring Boot 详细介绍请看这篇文章《<a href="https://mp.weixin.qq.com/s?__biz=MzI3ODcxMzQzMw==&amp;mid=2247484224&amp;idx=1&amp;sn=94a5a2865da38f93941b05f2de006966&amp;scene=21#wechat_redirect" rel="noopener nofollow">什么是Spring Boot?</a>》。</p>
<h1>为什么要用 Spring Boot？</h1>
<p>Spring Boot 优点非常多，如：</p>
<p><span>&nbsp;● &nbsp;</span><span>独立运行</span><br><span>&nbsp;● &nbsp;</span><span>简化配置</span><br><span>&nbsp;● &nbsp;</span><span>自动配置</span><br><span>&nbsp;● &nbsp;</span><span>无代码生成和XML配置</span><br><span>&nbsp;● &nbsp;</span><span>应用监控</span><br><span>&nbsp;● &nbsp;</span><span>上手容易</span><br><span>&nbsp;● &nbsp;</span><span>…</span></p>
<p>Spring Boot 集这么多优点于一身，还有理由不使用它呢？</p>
<h1>Spring Boot 的核心配置文件有哪几个？它们的区别是什么？</h1>
<p>Spring Boot 的核心配置文件是 application 和 bootstrap 配置文件。</p>
<p>application 配置文件这个容易理解，主要用于 Spring Boot 项目的自动化配置。</p>
<p>bootstrap 配置文件有以下几个应用场景。</p>
<p><span>&nbsp;● &nbsp;</span><span>使用 Spring Cloud Config 配置中心时，这时需要在 bootstrap 配置文件中添加连接到配置中心的配置属性来加载外部配置中心的配置信息；</span><br><span>&nbsp;● &nbsp;</span><span>一些固定的不能被覆盖的属性；</span><br><span>&nbsp;● &nbsp;</span><span>一些加密/解密的场景；</span></p>
<p>具体请看这篇文章《<a href="https://mp.weixin.qq.com/s?__biz=MzI3ODcxMzQzMw==&amp;mid=2247486541&amp;idx=2&amp;sn=436ab454a6367fdc33912162855c02c7&amp;scene=21#wechat_redirect" rel="noopener nofollow">Spring Boot 核心配置文件详解</a>》。</p>
<h1>Spring Boot 的配置文件有哪几种格式？它们有什么区别？</h1>
<p>.properties 和 .yml，它们的区别主要是书写格式不同。</p>
<p>1).properties</p>
<div class="cnblogs_code">
<pre>app.user.name&nbsp;=&nbsp;javastack</pre>
