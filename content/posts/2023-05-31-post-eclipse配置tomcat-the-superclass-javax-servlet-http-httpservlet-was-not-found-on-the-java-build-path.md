---
title: "eclipse配置Tomcat The superclass \"javax.servlet.http.HttpServlet\" was not found on the Java Build Path"
date: 2023-05-31
description: "介绍 问题描述 我们在使用Ecplise开发java web时，可能会报错误：The superclass &quot;javax.servlet.http.HttpServlet&quot; was not found on the Java Build Path 问题原因 项目中找不到Tomca"
tags:
  - "IDE"
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11936111.html"
---

<h1 style="text-align: center">介绍</h1>
<h2>问题描述</h2>
<p>　　我们在使用Ecplise开发java web时，可能会报错误：<span style="color: rgba(255, 0, 0, 1)"><strong><em>The superclass "javax.servlet.http.HttpServlet" was not found on the Java Build&nbsp;</em></strong></span></p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong><em id="__mceDel"> Path</em></strong></span></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201911/1504448-20191126151627338-457468233.png" alt="" /></p>
<p>&nbsp;</p>
<h2>问题原因</h2>
<p>　　项目中找不到<span style="color: rgba(255, 0, 0, 1)"><em><strong>Tomcat运行时相关类</strong></em></span></p>
<h1 style="text-align: center">解决方法</h1>
<h2>下载Tomcat</h2>
<h3>方法一</h3>
<p>　　指定Tomcat版本后，让Ecplise自动下载(Download and Install)，具体请看动态图,自动会下载到指定的路径下，下载过程根据个人网速可能会有点差异，耐心等待就好啦</p>
<p><img src="https://img2018.cnblogs.com/common/1504448/201911/1504448-20191126153343824-750955314.gif" alt="" /></p>
<h2>方式二</h2>
<p>　　官网下载：https://tomcat.apache.org/</p>
<p>　　进入官网找到想下载的Tomcat的版本，并适合当前操作系统的文件，下载到指定位置即可，操作步骤请看动态图</p>
<p><img src="https://img2018.cnblogs.com/common/1504448/201911/1504448-20191126154336635-897692217.gif" alt="" /></p>
<h2>为项目指定Tomcat</h2>
<p>　　找到我们刚才下载后的Tomcat文件，配置请看动态图</p>
<p><img src="https://img2018.cnblogs.com/common/1504448/201911/1504448-20191126155326209-1153141716.gif" alt="" /></p>
<p>搞定！！！</p>
