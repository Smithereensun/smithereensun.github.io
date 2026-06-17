---
title: "解决Maven无法下载fastdfs-client-java依赖，Dependency 'org.csource:fastdfs-client-java:1.27-SNAPSHOT' not found."
date: 2023-05-31
description: "因为fastdfs-client-java-1.27-SNAPSHOT.jar这个依赖包在maven中央仓库是没有的， 需要自己编译源码成jar本地安装到maven 的本地仓库，安装完以后就能正常引用了（注意：本地必须安装了Maven，并配置好Maven环境变量） &lt;dependency&gt"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12831553.html"
---

<p>因为fastdfs-client-java-1.27-SNAPSHOT.jar这个依赖包在maven中央仓库是没有的，</p>
<p>需要自己编译源码成jar本地安装到maven 的本地仓库，安装完以后就能正常引用了（注意：本地必须安装了Maven，并配置好Maven环境变量）</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
      <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.csource<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
      <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>fastdfs-client-java<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
      <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.27-SNAPSHOT<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
