---
title: "Spring中@Resource注解报错"
date: 2023-05-31
description: "描述:Spring框架中,@Resource注解报错,在书写时没有自动提示 解决方法:因为maven配置文件的pom.xml文件中缺少javax.annotation的依赖,在pom.项目路中加入依赖即可 &lt;!-- Javax Annotation --&gt; &lt;dependency&"
tags:
  - "JAVA"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11789483.html"
---

<p>描述:Spring框架中,@Resource注解报错,在书写时没有自动提示</p>
<p>解决方法:因为maven配置文件的pom.xml文件中缺少javax.annotation的依赖,在pom.项目路中加入依赖即可</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201911/1504448-20191103220452742-1037305141.png" alt="" /></p>
<div class="cnblogs_code">
<pre>&lt;!-- Javax Annotation --&gt;  
        &lt;dependency&gt;  
            &lt;groupId&gt;javax.annotation&lt;/groupId&gt;  
            &lt;artifactId&gt;jsr250-api&lt;/artifactId&gt;  
            &lt;version&gt;1.0&lt;/version&gt;  
        &lt;/dependency&gt;  </pre>
