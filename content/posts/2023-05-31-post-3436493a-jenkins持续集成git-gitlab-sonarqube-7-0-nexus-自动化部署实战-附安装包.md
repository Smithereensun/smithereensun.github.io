---
title: "Jenkins持续集成git、gitlab、sonarqube(7.0)、nexus，自动化部署实战，附安装包"
date: 2023-05-31
description: "导读 之前用的都是SVN，由于工作需要用到Git，求人不如求己，技多不压身，多学一项技能，未来就少求别人一次，系统的学一遍，自己搭建一整套环境，自动化部署(自动发版)，代码质量检测等等(为啥不用docker搭建环境呢，个人平时比较忙，暂未学习docker，过段时间会学docker相关，也会写相应博文"
tags:
  - "Git"
  - "技术干货"
  - "自动化部署"
  - "Linux"
  - "Nexus"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/qq543210188.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　之前用的都是SVN，由于工作需要用到Git，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>求人不如求己</strong></span>，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>技多不压身</strong></span>，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>多学一项技能</strong></span>，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>未来就少求别人一次</strong></span>，系统的学一遍，自己搭建一整套环境，自动化部署(自动发版)，代码质量检测等等(<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>为啥不用docker搭建环境呢，个人平时比较忙，暂未学习docker，过段时间会学docker相关，也会写相应博文</strong></span>)。为啥要打水印，Wechat上有人告诉我，之前很多博文，被某些网站白嫖，然后挂到自己网站(<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>未来博客上都会打水印</strong></span>)，~@￥#%￥@%#@%￥再次声明，<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>创作不易，严禁转载！！！</strong></span></p>
<h2>踩坑</h2>
<p>　　从10月12、13(周末)天天搞到夜里2、3点，周一至周五，由于个人原因，刚换份工作，平时也忙，个人精力有限，只能晚上花2、3小时，学习-搭建-踩坑-度娘-搭建-成功，一直到今天，才完整的搭建出来，博客才发出来。安装过程中，并不是一帆风顺的，在此为了避免学习的小朋友踩相同的坑，最好版本和我一致，下面都会有提供我使用的安装包。<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>那些坑，我已经巧妙的绕开啦，按照我的步骤来，干就完事儿啦，欧力给~</strong></span></p>
<h2 style="text-align: left">演示环境</h2>
<ol>
<li style="text-align: left">mac系统</li>
<li style="text-align: left">虚拟机：Centos 6.5(<span style="color: rgba(255, 0, 0, 1)"><strong>我分配了4G，2核，配置低了会卡！里面用到ES服务器配置低，服务起不来，ES脑补链接：<a href="https://www.cnblogs.com/chenyanbin/category/1811337.html" target="_blank">点我直达</a>，磁盘至少分50G，当初我给了20G，最后服务配置太多以后，导致服务跑不起来了</strong></span>)</li>
</ol>
<h1 style="text-align: center">Git</h1>
<h2>Git是什么</h2>
<p>　　Git 是一个<span style="color: rgba(255, 0, 0, 1)"><strong>开源</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>分布式版本控制</strong></span>系统，用于<span style="color: rgba(255, 0, 0, 1)"><strong>敏捷高效</strong></span>地处理任何或小或大的<span style="color: rgba(255, 0, 0, 1)"><strong>项目</strong></span>。</p>
<p>　　Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。</p>
<p>　　Git 与常用的版本控制工具 CVS, Subversion 等不同，它采用了分布式版本库的方式，不必服务器端软件支持。</p>
<h2>Git的安装</h2>
<p>　　官网地址：<a href="https://git-scm.com/downloads" target="_blank" rel="noopener nofollow">https://git-scm.com/downloads</a><a href="https://git-scm.com/" target="_blank" rel="noopener nofollow"><br></a></p>
<p>　　不要慌，最下面我会提供我使用的所有安装包</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">linux：yum install -y git
mac：自带的有git
windows：需要自动手动下载,一直下一步即可</span></pre>
