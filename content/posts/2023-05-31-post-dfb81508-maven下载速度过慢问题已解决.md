---
title: "Maven下载速度过慢问题已解决"
date: 2023-05-31
description: "因为Maven 默认仓库的服务器在国外所以我们国内的使用效果极差，我们可以修改成为国内镜像地址加速下载。 两种方法 修改全局文件 C:\\Users\\您电脑帐号\\ .m2\\settings.xml没有文件的下载附件里面 修改局部,需要使用的时候指定配置文件 修改Maven安装目录下/conf/sett"
tags:
  - "IDE"
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11706339.html"
---

<p>因为Maven 默认仓库的服务器在国外所以我们国内的使用效果极差，我们可以修改成为国内镜像地址加速下载。</p>
<h1>两种方法</h1>
<h2>修改全局文件</h2>
<p>C:\Users\您电脑帐号\ .m2\settings.xml<br>没有文件的下载附件里面</p>
<h2>修改局部,需要使用的时候指定配置文件</h2>
<p>修改Maven安装目录下<code>/conf/settings.xml</code>文件</p>
<p>找到<code>&lt;mirrors&gt;&lt;/mirrors&gt;</code>在这里面 加入国内镜像源·华为云和阿里云提供的镜像</p>
<p><span style="font-size: 15px"><strong><span style="color: rgba(255, 0, 0, 1)">注：您要是觉得手动配置节点麻烦的，请直接下载，覆盖相应路径文件即可：</span></strong></span><a href="https://files-cdn.cnblogs.com/files/chenyanbin/settings.xml" target="_blank">直接下载</a></p>
<div class="cnblogs_code">
<pre>&lt;mirror&gt;
    &lt;id&gt;HuaweiCloud&lt;/id&gt;
    &lt;mirrorOf&gt;*,!HuaweiCloudSDK&lt;/mirrorOf&gt;
     &lt;url&gt;https:<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">mirrors.huaweicloud.com/repository/maven/&lt;/url&gt;</span>
&lt;/mirror&gt;
&lt;mirror&gt;
&lt;id&gt;AliYUN&lt;/id&gt;
    &lt;name&gt;AliYUN Maven&lt;/name&gt;
    &lt;mirrorOf&gt;*,!HuaweiCloudSDK&lt;/mirrorOf&gt;
    &lt;url&gt;http:<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">maven.aliyun.com/nexus/content/groups/public/&lt;/url&gt;</span>
&lt;/mirror&gt;</pre>
