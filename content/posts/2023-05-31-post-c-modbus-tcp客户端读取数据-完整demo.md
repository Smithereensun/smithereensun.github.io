---
title: "C# ModBus Tcp客户端读取数据 完整Demo"
date: 2023-05-31
description: "简单介绍： 项目上需要与多家公司做接口对接。我们提供接口的有，其他公司提供的接口也有。所有的接口全部对接完了，遇到一个非常棘手的问题，需要获取甲方船厂设备上的状态，就给了一个文档，文档上写了IP、端口、协议、一些地址，没有API文档，拿到手上一面懵逼，这怎么玩儿。。。。 文档如下： 百度百科： Mo"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11394599.html"
---

<h2><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 18px">简单介绍：</span></h2>
<p><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 16px">　　项目上需要与多家公司做接口对接。我们提供接口的有，其他公司提供的接口也有。所有的接口全部对接完了，遇到一个非常棘手的问题，需要获取甲方船厂设备上的状态，就给了一个文档，文档上写了IP、端口、协议、一些地址，没有API文档，拿到手上一面懵逼，这怎么玩儿。。。。</span></p>
<h2><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 18px">文档如下：</span></h2>
<p><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 16px"><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190822152342416-930262951.png" alt="" /></span></p>
<p>&nbsp;</p>
<h2><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 18px">百度百科：</span></h2>
<p><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 16px">　　Modbus是一种串行<a href="https://baike.baidu.com/item/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE" target="_blank" rel="noopener nofollow">通信协议</a>，是Modicon公司（现在的<a href="https://baike.baidu.com/item/%E6%96%BD%E8%80%90%E5%BE%B7%E7%94%B5%E6%B0%94" target="_blank" rel="noopener nofollow">施耐德电气</a>&nbsp;Schneider Electric）于1979年为使用<a href="https://baike.baidu.com/item/%E5%8F%AF%E7%BC%96%E7%A8%8B%E9%80%BB%E8%BE%91%E6%8E%A7%E5%88%B6%E5%99%A8" target="_blank" rel="noopener nofollow">可编程逻辑控制器</a>（PLC）通信而发表。Modbus已经成为工业领域通信协议的业界标准（De facto），并且现在是工业电子设备之间常用的连接方式。</span></p>
<p><span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 16px">　　看上去好像跟Socket差不多，本身又不是工业领域出身的，大概知道是一种工业领域通用的一套通信标准，下面直接上DEMO示例</span></p>
<h1>第一步：下载类库</h1>
<p>使用的类库已上传百度云盘：</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190822144353001-512491606.png" alt="" /></p>
<p>链接：https://pan.baidu.com/s/1JtaGC0r17jjnQPMhkMKRJg <br>提取码：wagl </p>
<h1>第二步：引入类库</h1>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190822144508448-895330501.png" alt="" /></p>
<h1>第三步：引入命名空间</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> HslCommunication.ModBus;
</span><span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(0, 0, 255, 1)">using</span> HslCommunication;</pre>
