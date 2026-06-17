---
title: "Eclipse Java SE升级Java EE"
date: 2023-05-31
description: "网上教程大多是提供了“http://download.eclipse.org/releases/ganymede/”地址，但是实际更新过程中会报错。 参考来自：eclipse 安装java ee插件（java se升级到java ee） 本来安装的java se，后需要开发java ee程序，走了些"
tags:
  - "IDE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11781189.html"
---

<p>网上教程大多是提供了“http://download.eclipse.org/releases/ganymede/”地址，但是实际更新过程中会报错。</p>
<p>参考来自：<a href="https://blog.csdn.net/weixin_39525565/article/details/82886059" target="_blank" rel="noopener nofollow">eclipse 安装java ee插件（java se升级到java ee）</a></p>
<p>本来安装的java se，后需要开发java ee程序，走了些弯路才安装成功。如下是步骤</p>
<p>1.打开eclipse，help-&gt;About Eclipse IDE，看好我下图红线圈出的地方，也就是版本号</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201911/1504448-20191102113011276-987142264.png" alt="" /></p>
<p>2.help-&gt;install New Software,在Work with的框里填&nbsp;http://download.eclipse.org/releases/+<span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>步骤一中的版本号</strong></span>，回车，等待加载出内容，选择Web，XML,Java EE and OSGi。。。这一项，然后就是一直next即可。</p>
<p><span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>注意：因为我上面的版本是2019-06，后面跟自己的本版号</strong></span></p>
<div class="cnblogs_code">
<pre>http:<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">download.eclipse.org/releases/2019-06</span></pre>
