---
title: "Spring Boot拦截器中获取request post请求中的参数"
date: 2021-03-25
description: "最近有一个需要从拦截器中获取post请求的参数的需求，这里记录一下处理过程中出现的问题。首先想到的就是request.getParameter(String )方法，但是这个方法只能在get请求中取到参数，post是不行的，后来想到了使用流的方式，调用request.getInputStream()"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14559094.html"
---

<p>最近有一个需要从拦截器中获取post请求的参数的需求，这里记录一下处理过程中出现的问题。<br>首先想到的就是request.getParameter(String )方法，但是这个方法只能在get请求中取到参数，post是不行的，后来想到了使用流的方式，调用request.getInputStream()获取流，然后从流中读取参数，如下代码所示：</p>
<div class="cnblogs_code">
<pre>            BufferedReader br =<span style="color: rgba(0, 0, 0, 1)"> request.getReader();
            String str, wholeStr </span>= ""<span style="color: rgba(0, 0, 0, 1)">;
            </span><span style="color: rgba(0, 0, 255, 1)">while</span> ((str = br.readLine()) != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
                wholeStr </span>+=<span style="color: rgba(0, 0, 0, 1)"> str;
            }
            System.out.println(</span>"post:" + wholeStr);</pre>
