---
title: "Oracle DBLink跨数据库访问SQL server数据同步"
date: 2023-05-31
description: "第一步：需要去下载一个透明网管，相当于一个中间件(我们用的Oracle 11g，可能不同的数据库版本要安装不同的透明网管) 需要的朋友请到我的百度云盘上下载 链接：https://pan.baidu.com/s/1W6rEww1_NxxsMXYi0BOKPQ 提取码：sac2 第二步：安装透明网关"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11291752.html"
---

<h1><span style="font-family: &quot;Microsoft YaHei&quot;">　　第一步：需要去下载一个透明网管，相当于一个中间件(我们用的Oracle 11g，可能不同的数据库版本要安装不同的透明网管)</span></h1>
<p><span style="font-family: &quot;Microsoft YaHei&quot;"><strong><span style="font-size: 16px">需要的朋友请到我的百度云盘上下载</span></strong></span></p>
<p><strong><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 16px">链接：https://pan.baidu.com/s/1W6rEww1_NxxsMXYi0BOKPQ </span></strong><br><strong><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 16px">提取码：sac2 </span></strong></p>
<h1><span style="font-family: &quot;Microsoft YaHei&quot;">　　第二步：安装透明网关</span></h1>
<h3><span style="font-family: &quot;Microsoft YaHei&quot;">1、解压安装包后，点击setup.exe安装</span></h3>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190802223253863-438638962.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190802223320050-1315980309.png" alt="" /></p>
<h3><span style="font-family: &quot;Microsoft YaHei&quot;">2、下一步(<span style="color: rgba(255, 0, 0, 1)">注：貌似一定要和Oracle数据库安装目录一致，第一次安装的时候，就和Oracle安装在不同地方了，最终百度很久发现，要和Oracle安装同一个位置</span>)</span></h3>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201909/1504448-20190926113201371-110289564.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h3><span style="font-family: &quot;Microsoft YaHei&quot;">3、选择组建，选择SQL Server</span></h3>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190802223637082-726224621.png" alt="" /></p>
<h3><span style="font-family: &quot;Microsoft YaHei&quot;">4、填写SQL SERVER的主机名和数据库名称</span></h3>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190802223827851-1387743110.png" alt="" /></p>
<h3><span style="font-family: &quot;Microsoft YaHei&quot;">5、开始安装</span></h3>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190802223850258-1827749045.png" alt="" /></p>
<h3><span style="font-family: &quot;Microsoft YaHei&quot;">6、安装完成后就退出，然后开始配置监听，下面是重点！！！！</span></h3>
<h1><span style="font-family: &quot;Microsoft YaHei&quot;">&nbsp;　　第三步：透明网关配置</span></h1>
<h2><span style="font-family: &quot;Microsoft YaHei&quot;"><strong><span style="color: rgba(255, 0, 255, 1)">&nbsp;配置说明：</span></strong></span></h2>
<h2><span style="font-family: &quot;Microsoft YaHei&quot;"><strong><span style="color: rgba(255, 0, 0, 1)">本地Oracle安装目录：D:\Oracle\product\11.2.0\dbhome_1</span></strong></span></h2>
<h2><span style="font-family: &quot;Microsoft YaHei&quot;"><strong><span style="color: rgba(255, 0, 0, 1)">本地DBLink安装目录:D:\Oracle\product\11.2.0\dbhome_1</span></strong></span></h2>
<h2><span style="font-family: &quot;Microsoft YaHei&quot;"><strong><span style="color: rgba(255, 0, 0, 1)">SQL Server：账号：sa;密码:password；IP地址:127.0.0.1</span></strong></span></h2>
<h2><span style="font-family: &quot;Microsoft YaHei&quot;">1、来到:D:\Oracle\product\11.2.0\dbhome_1\dg4msql\admin;打开initdg4msql.ora</span></h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190802224310636-637782306.png" alt="" /></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> 这个目录下可以看到以下initdg4msql.ora文件，上面在安装透明网关的时候有配置的要链接SQL SERVER数据的地址和数据库名称，在这里都可以体现：</pre>
