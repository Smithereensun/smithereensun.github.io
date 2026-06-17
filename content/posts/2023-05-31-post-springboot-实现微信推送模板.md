---
title: "SpringBoot 实现微信推送模板"
date: 2023-05-31
description: "导读 由于最近手头上需要做个Message Gateway，涉及到：邮件(点我直达)、短信、公众号等推送功能，网上学习下，整理下来以备以后使用。 添加依赖 在SpringBoot项目中添加依赖 &lt;!--微信模版消息推送三方sdk--&gt; &lt;dependency&gt; &lt;gro"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14047389.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　由于最近手头上需要做个Message Gateway，涉及到：邮件(<a href="https://www.cnblogs.com/chenyanbin/p/14042642.html" target="_blank">点我直达</a>)、短信、公众号等推送功能，网上学习下，整理下来以备以后使用。</p>
<h1 style="text-align: center">添加依赖</h1>
<p>　　在SpringBoot项目中添加依赖</p>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">微信模版消息推送三方sdk</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.github.binarywang<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>weixin-java-mp<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>3.3.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
