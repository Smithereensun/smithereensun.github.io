---
title: "【全网首创】修改 Ext.ux.UploadDialog.Dialog 源码支持多选添加文件，批量上传文件"
date: 2023-05-31
description: "公司老框架的一个页面需要用到文件上传，本以为修改一个配置参数即可解决，百度一番发现都在说这个第三方插件不支持文件多选功能，还有各种各样缺点，暂且不讨论这些吧。先完成领导安排下来的任务。 任务一：支持多选添加文件 任务二：支持批量添加文件 我们先来说第二个任务吧，第二个任务相比较容易些，经过半天研究源"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11578372.html"
---

<p><span style="font-family: 宋体"><strong><span style="font-size: 16px">　　公司老框架的一个页面需要用到文件上传，本以为修改一个配置参数即可解决，百度一番发现都在说这个第三方插件不支持文件多选功能，还有各种各样缺点，暂且不讨论这些吧。先完成领导安排下来的任务。</span></strong></span></p>
<p><span style="font-size: 16px"><strong><span style="font-family: 宋体">　　任务一：支持多选添加文件</span></strong></span></p>
<p><span style="font-size: 16px"><strong><span style="font-family: 宋体">　　任务二：支持批量添加文件</span></strong></span></p>
<p><span style="font-size: 16px"><strong><span style="font-family: 宋体">　　我们先来说第二个任务吧，第二个任务相比较容易些，经过半天研究源码，发现他每次都将文件，添加到队列中“<strong>queue</strong>”然后不停的拿队列中的数据</span></strong></span></p>
<p><span style="font-size: 16px"><strong><span style="font-family: 宋体">　　添加队列源码(<span style="color: rgba(255, 0, 0, 1)">大约在源码的第35行左右</span>)</span></strong></span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span>   <span style="color: rgba(0, 0, 255, 1)">this</span>.postEvent = function(<span style="color: rgba(0, 0, 255, 1)">event</span><span style="color: rgba(0, 0, 0, 1)">, data)
</span><span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(0, 0, 0, 1)">  {
</span><span style="color: rgba(0, 128, 128, 1)">3</span>     data = data || <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">4</span>     <span style="color: rgba(0, 0, 255, 1)">this</span>.queue.push({<span style="color: rgba(0, 0, 255, 1)">event</span>: <span style="color: rgba(0, 0, 255, 1)">event</span><span style="color: rgba(0, 0, 0, 1)">, data: data});
</span><span style="color: rgba(0, 128, 128, 1)">5</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.is_processing) {
</span><span style="color: rgba(0, 128, 128, 1)">6</span>       <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.process();
</span><span style="color: rgba(0, 128, 128, 1)">7</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">8</span>   }</pre>
