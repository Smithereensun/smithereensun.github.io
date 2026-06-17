---
title: "java soarqube扫描new Random()报bug，修改为securerandom.getinstancestrong()造成线程阻塞，使用apache工具类生成随机数"
date: 2021-07-23
description: "描述 项目中生成随机数的，new Random()写法sonarqube会提示是个bug，推荐写成Random rand = SecureRandom.getInstanceStrong();这种方式本地没啥问题，发到线上会造成线程阻塞；可以使用如下方式，org.apache.commons.lan"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15049859.html"
---

<h1 style="text-align: center">描述</h1>
<p>　　项目中生成随机数的，new Random()写法sonarqube会提示是个bug，推荐写成Random rand = SecureRandom.getInstanceStrong();这种方式本地没啥问题，发到线上会造成线程阻塞；可以使用如下方式，org.<span class="keyword">apache.commons.lang.RandomStringUtils包下的<br></span></p>
<div class="cnblogs_code">
<pre>  <span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
         * count 创建一个随机字符串，其长度是指定的字符数,字符将从参数的字母数字字符集中选择，如参数所示。
         * letters true,生成的字符串可以包括字母字符
         * numbers true,生成的字符串可以包含数字字符
         </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
        String random </span>= RandomStringUtils.random(15, <span style="color: rgba(0, 0, 255, 1)">true</span>, <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">);
        System.out.println(random);</span></pre>
