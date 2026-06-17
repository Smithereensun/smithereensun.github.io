---
title: "Spring Boot整合ElasticSearch和Mysql 附案例源码"
date: 2023-05-31
description: "导读 前二天，写了一篇ElasticSearch7.8.1从入门到精通的（点我直达），但是还没有整合到SpringBoot中，下面演示将ElasticSearch和mysql整合到Spring Boot中，附演示源码。 项目介绍 模仿NBA网站 网址地址：点我直达 接口开发 将数据库数据导入到Ela"
tags:
  - "ElasticSearch7.8.1"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13473132.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　前二天，写了一篇ElasticSearch7.8.1从入门到精通的（<a href="https://www.cnblogs.com/chenyanbin/p/13419497.html" target="_blank">点我直达</a>），但是还没有整合到SpringBoot中，下面演示将ElasticSearch和mysql整合到Spring Boot中，附演示源码。</p>
<h1 style="text-align: center">项目介绍</h1>
<h2>模仿NBA网站</h2>
<p>网址地址：<a href="https://china.nba.com/playerindex/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200810225033587-1561809235.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h2>接口开发</h2>
<ol>
<li>将数据库数据导入到ElasticSearch</li>
<li>通过姓名查找球员</li>
<li>通过国家或者球队查询球员</li>
<li>通过姓名字母查找球员</li>
</ol>
<h1 style="text-align: center">项目搭建</h1>
<h2>SpringBoot整合ElasticSearch和Mysql</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200810225349206-759706903.png" alt="" loading="lazy" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200810225505658-297819577.png" alt="" loading="lazy" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200810225604830-1516252005.png" alt="" loading="lazy" /></p>
<h2>数据库数据</h2>
<p>　　将百度云盘里的sql，在mysql上运行即可</p>
<div class="cnblogs_code">
<pre>链接: https://pan.baidu.com/s/1MJaJy8isfVnPha00tlS8_w  密码: u3dg</pre>
