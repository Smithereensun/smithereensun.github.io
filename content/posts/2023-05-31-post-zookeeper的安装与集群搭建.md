---
title: "Zookeeper的安装与集群搭建"
date: 2023-05-31
description: "简介 Zookeeper下载 官网地址：点我直达 百度云盘：点我直达 踩坑录 官网下载一定要下载带bin的 要不然zookeeper起不起来，找不到加载类，原来从版本3.5.5开始，带有bin名称的包才是我们想要的下载可以直接使用的里面有编译后的二进制的包，而之前的普通的tar.gz的包里面是只是源"
tags:
  - "分布式架构"
  - "Linux"
  - "Zookeeper"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12202048.html"
---

<h1 style="text-align: center">简介</h1>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200117114123920-476372720.png" alt="" /></p>
<h1 style="text-align: center">Zookeeper下载</h1>
<p>官网地址：<a href="https://www.apache.org/dyn/closer.cgi/zookeeper/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p>百度云盘：<a href="https://pan.baidu.com/s/1uZnWUsePTJSJ-Xkm33xdHQ" target="_blank" rel="noopener nofollow">点我直达</a></p>
<h1 style="text-align: center">踩坑录</h1>
<p>官网下载一定要下载带bin的</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200117094249822-138407522.png" alt="" />&nbsp;</p>
<p>要不然zookeeper起不起来，找不到加载类，原来从版本3.5.5开始，带有bin名称的包才是我们想要的下载可以直接使用的里面有编译后的二进制的包，而之前的普通的tar.gz的包里面是只是源码的包无法直接使用。</p>
<p>好想吐槽下啊，Zookeeper的包的变动，源码的包就不能向其他的安装包一样加个src的标识吗？见名知意多好，以避免误下载。</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200117094332023-1361172885.png" alt="" /></p>
<h1 style="text-align: center">单机Zookeeper</h1>
<h2>创建目录及解压</h2>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200116170435776-2104717756.png" alt="" /></p>
<h2>进入解压目录&nbsp;<img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200116213610369-431442890.png" alt="" /></h2>
<h2>进入conf&nbsp;</h2>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200116213700070-1120299089.png" alt="" /></p>
<h2>拷贝zoo_sample.cfg(<span style="color: rgba(255, 0, 0, 1)"><strong>目标文件，必须zoo.cfg</strong></span>)<img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200116213853164-1523459185.png" alt="" /></h2>
<h2>编译拷贝后的文件:zoo.cfg</h2>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200116220651886-746579010.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200116220629445-1515132838.png" alt="" /></p>
<p>注：修改完快照存储目录后，用:<strong><span style="color: rgba(255, 0, 0, 1)">x</span></strong></p>
<h2>建立软连接</h2>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200116230705903-1445644511.png" alt="" /></p>
<h2>环境变量配置</h2>
<div class="cnblogs_code">
<pre>vim /etc/profile</pre>
