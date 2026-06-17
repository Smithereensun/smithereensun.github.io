---
title: "Mybatis 找不到src下的*.xml"
date: 2021-05-09
description: "&lt;!-- 你的mapper.xml文件是放在src/main/java目录下还是src/main/sources下，如果放在src/main/java下默认打包时xml文件是不加进去的，通过以下配置可解决 --&gt; &lt;build&gt; &lt;resources&gt; &lt;r"
tags:
  - "MyBatis"
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14251756.html"
---

<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 你的mapper.xml文件是放在src/main/java目录下还是src/main/sources下，如果放在src/main/java下默认打包时xml文件是不加进去的，通过以下配置可解决 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">build</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">resources</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">resource</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">directory</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>src/main/java<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">directory</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">includes</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">include</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>**/*.xml<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">include</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">includes</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">resource</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">resource</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">directory</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>src/main/resources<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">directory</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">resource</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">resources</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">build</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
