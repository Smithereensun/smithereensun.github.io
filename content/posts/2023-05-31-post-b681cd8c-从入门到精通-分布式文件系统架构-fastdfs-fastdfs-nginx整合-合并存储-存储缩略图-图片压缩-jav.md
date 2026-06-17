---
title: "从入门到精通(分布式文件系统架构)-FastDFS，FastDFS-Nginx整合，合并存储，存储缩略图，图片压缩，Java客户端"
date: 2023-05-31
description: "导读 篇幅较长，干货满满，需花费较长时间，转载请注明出处！ 互联网环境中的文件如何存储？ 不能存本地应用服务器 NFS(采用mount挂载) HDFS(适合大文件) FastDFS(强力推荐&#128077;) 云存储(有免费和收费的，不推荐，使用前可以看该公司实力怎么样，别文件都存上去了，过2年公"
tags:
  - "FastDFS"
  - "分布式架构"
  - "负载均衡"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12782615.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　篇幅较长，干货满满，需花费较长时间，转载请注明出处！</p>
<h2>互联网环境中的文件如何存储？</h2>
<ol>
<li>不能存本地应用服务器</li>
<li>NFS(采用mount挂载)</li>
<li>HDFS(适合大文件)</li>
<li>FastDFS(<span style="color: rgba(255, 0, 0, 1)"><strong>强力推荐</strong></span><strong>👍</strong>)</li>
<li>云存储(<span style="color: rgba(255, 0, 0, 1)"><strong>有免费和收费的，不推荐，使用前可以看该公司实力怎么样，别文件都存上去了，过2年公司破产了，损失惨重呀，呜呜呜~~~</strong></span>)</li>
</ol>
<h2>互联网环境中的文件如何进行HTTP访问？</h2>
<p>Web服务器：Nginx(<span style="color: rgba(255, 255, 255, 1); background-color: rgba(255, 0, 0, 1); font-size: 16px"><strong>本案例使用Nginx，还不会用Nginx的小伙伴，请看我另一篇博客：</strong></span><a href="https://www.cnblogs.com/chenyanbin/p/12521296.html" target="_blank">点我直达</a>)、Apache等等。</p>
<h1 style="text-align: center">FastDFS介绍</h1>
<h2>FastDFS是什么？</h2>
<ol>
<li>FastDFS是一个C编写的开源的<span style="color: rgba(255, 0, 0, 1)"><strong>高性能分布式文件系统</strong></span>(Distributed File System，简称DFS)</li>
<li>它由淘宝开发平台部资深架构师余庆开发,论坛：http://bbs.chinaunix.net/forum-240-1.html</li>
<li>它对<span style="color: rgba(255, 0, 0, 1)"><strong>文件进行管理</strong></span>，功能包括：<span style="color: rgba(255, 0, 0, 1)"><strong>文件存储、文件同步、文件访问(文件上传、文件下载)</strong></span>等，解决了大容量存储和负载均衡的问题</li>
<li>特别适合以文件为载体的在线服务，如<span style="color: rgba(255, 0, 0, 1)"><strong>相册网站、视频网站、电商</strong></span>等等。特别适合以<span style="color: rgba(255, 0, 0, 1)"><strong>中小文件</strong></span>(建议范围：4KB&lt;file_size&lt;500mb)为载体的在线服务</li>
<li>FastDFS为互联网量身定制，充分考虑了<span style="color: rgba(255, 0, 0, 1)"><strong>冗余备份、负载均衡、线性扩容</strong></span>等机制，并注重<span style="color: rgba(255, 0, 0, 1)"><strong>高可用、高性能</strong></span>等指标，使用<span style="color: rgba(255, 0, 0, 1)"><strong>FastDFS很容易搭建一套高性能的文件服务器集群提供文件上传、下载</strong></span>等服务</li>
<li>github：https://github.com/happyfish100/fastdfs</li>
</ol>
<p>技术文档</p>
<div class="cnblogs_code">
<pre>链接: https://pan.baidu.com/s/1BpPwJBg2mR8CvqOiKj2rDQ  密码: ocj5</pre>
