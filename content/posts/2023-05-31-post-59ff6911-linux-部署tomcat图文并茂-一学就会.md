---
title: "Linux 部署Tomcat图文并茂 一学就会"
date: 2023-05-31
description: "导读 安装tomcat前首先要安装对应的jdk并配置Java环境。 安装jdk，请参考：点我直达 安装Tomcat 下载Tomcat包 官网地址：点我直达 Tomcat与jdk兼容关系 注：Tomcat与jdk兼容关系 将包放到linux 解压Tomcat tar -zxvf apache-tomc"
tags:
  - "Linux"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12548645.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　安装tomcat前首先要安装对应的jdk并配置Java环境。</p>
<p>安装jdk，请参考：<a href="https://blog.csdn.net/xlecho/article/details/97266591" target="_blank" rel="noopener nofollow">点我直达</a></p>
<h1 style="text-align: center">安装Tomcat</h1>
<h2>下载Tomcat包</h2>
<p>官网地址：<a href="https://tomcat.apache.org/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202003/1504448-20200322221630360-513032748.gif" alt="" /></p>
<h3>Tomcat与jdk兼容关系</h3>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200324222309402-251918272.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;　　<span style="color: rgba(255, 0, 0, 1); font-size: 18px"><strong>注：Tomcat与jdk兼容关系</strong></span></p>
<h2>将包放到linux</h2>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200322224735835-813442984.png" alt="" /></p>
<h2>解压Tomcat</h2>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200323232927964-1931868114.png" alt="" /></p>
<div class="cnblogs_code">
<pre>tar -zxvf apache-tomcat-10.0.0-M3.tar.gz -C /opt/apps/</pre>
