---
title: "SpringBoot目录文件结构和官方推荐的目录规范、静态资源访问"
date: 2020-07-03
description: "目录讲解 src/main/java：存放代码 src/main/resourcces static：存放静态文件，比如css、js、image，（访问方式：http://localhost:8080/js/main.js） templates：存放静态页面jsp、html、tpl config：存"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13232630.html"
---

<h1>目录讲解</h1>
<ul>
<li>src/main/java：存放代码</li>
<li>src/main/resourcces</li>
<li>static：存放静态文件，比如css、js、image，（访问方式：http://localhost:8080/js/main.js）</li>
<li>templates：存放静态页面jsp、html、tpl</li>
<li>config：存放配置文件，application.properties</li>
<li>resources</li>
</ul>
<h1>同个文件的加载顺序，静态资源文件Spring Boot默认会挨个从</h1>
<ul>
<li>META/resources&gt;</li>
<li>resources&gt;</li>
<li>static&gt;</li>
<li>public</li>
</ul>
<p>里面找到是否存在相应的资源，如果有则直接返回，不在默认加载的目录，则找不到</p>
<h1>默认配置</h1>
<ul>
<li>spring.resources.static-locations = classpath:/META-INF/resources/,classpath:/resources/,classpath:/static/,classpath:/public/</li>
</ul>
<p>基本互联网企业静态资源文件存储在CDN，HTML，CSS，图片等</p>
