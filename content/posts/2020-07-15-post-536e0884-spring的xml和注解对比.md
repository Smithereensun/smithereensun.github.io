---
title: "Spring的xml和注解对比"
date: 2020-07-15
description: "常用注解 bean定义 XML方式：&lt;bean&gt;&lt;/bean&gt; 注解方式：@Component 通用组件 @Controller（web层） @Service（service层） @Repository（dao层） bean取名 XML方式：通过id或者name 注解方式：@"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13307014.html"
---

<h1 style="text-align: center">常用注解</h1>
<h2>bean定义</h2>
<ul>
<li>XML方式：&lt;bean&gt;&lt;/bean&gt;</li>
<li>注解方式：@Component 通用组件
<ul>
<li>@Controller（web层）</li>
<li>@Service（service层）</li>
<li>@Repository（dao层）</li>
</ul>
</li>
</ul>
<h2>bean取名</h2>
<ul>
<li>XML方式：通过id或者name</li>
<li>注解方式：@Component("xxx")</li>
</ul>
<h2>bean注入</h2>
<ul>
<li>xml方式：通过&lt;property&gt;</li>
<li>注解方式：类型注入@Autowired名称注入@Qualifier</li>
</ul>
<h2>bean生命周期</h2>
<ul>
<li>XML方式：init-method、destroy-method</li>
<li>注解方式：@PostConstruct初始化、@PreDestroy销毁</li>
</ul>
<h2>bean的作用范围</h2>
<ul>
<li>XML方式：scope属性</li>
<li>注解方式：@scope注解</li>
</ul>
<p>&nbsp;</p>
