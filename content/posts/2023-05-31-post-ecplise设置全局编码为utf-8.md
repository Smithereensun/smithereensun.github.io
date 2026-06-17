---
title: "Ecplise设置全局编码为UTF-8"
date: 2023-05-31
description: "简介 Eclipse工作空间(workspace)的缺省字符编码是操作系统缺省的编码，简体中文操作系统 (Windows XP、Windows 2000简体中文)的缺省编码是GB18030，Windows7/8/10的缺省编码是GBK，在此工作空间中建立的工程编码是GB18030或者GBK，工程中建"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11935710.html"
---

<h1 style="text-align: center">简介</h1>
<p>　　Eclipse工作空间(workspace)的缺省字符编码是操作系统缺省的编码，简体中文操作系统 (Windows XP、Windows 2000简体中文)的缺省编码是GB18030，Windows7/8/10的缺省编码是GBK，在此工作空间中建立的工程编码是GB18030或者GBK，工程中建立的java文件也是GB18030或者GBK。</p>
<h1 style="text-align: center">设置编码格式</h1>
<h2>设置一</h2>
<p>　　路径：Window-&gt;Preferences-&gt;General-&gt;Workspace</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201911/1504448-20191126150415678-867913597.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;设置二</h2>
<p>　　路径：Window-&gt;Preferences-&gt;General-&gt;Content Types，导航树中的Text所有子项全部设置为UTF-8，并Update</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201911/1504448-20191126150836073-341186950.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201911/1504448-20191126150741951-298694128.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;配置三</h2>
<p>　　路径：Window-&gt;Web下的所有子项，编码格式设置为：<span style="color: rgba(255, 0, 0, 1)"><strong>ISO 10646/Unicode(UTF-8)</strong></span></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201911/1504448-20191126151123021-748475751.png" alt="" /></p>
