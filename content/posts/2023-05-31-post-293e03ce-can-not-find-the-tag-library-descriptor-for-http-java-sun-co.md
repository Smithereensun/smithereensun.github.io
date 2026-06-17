---
title: "Can not find the tag library descriptor for “http://java.sun.com/jstl/core\""
date: 2023-05-31
description: "此文原博文地址：https://blog.csdn.net/kolamemo/article/details/51407467 按照查到的资料，JSTL taglib需要jstl.jar来支持。在1.0和1.1版本的时候，还需要standard.jar来配合。但从1.2版本开始，jar文件名字变成了"
tags:
  - "JAVA"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11937668.html"
---

<p>此文原博文地址：https://blog.csdn.net/kolamemo/article/details/51407467</p>
<p>　　按照查到的资料，JSTL taglib需要jstl.jar来支持。在1.0和1.1版本的时候，还需要standard.jar来配合。但从1.2版本开始，jar文件名字变成了jstl-1.2.jar，也不再需要standard.jar了。另外，servlet 版本需要2.4以上。所以正确的做法是把jstl-1.2.jar放到WEB-INF/lib里面就可以了。或者通过maven来配置，如下：</p>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>javax.servlet<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>jstl<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.2<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
