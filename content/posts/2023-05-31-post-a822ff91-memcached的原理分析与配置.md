---
title: "Memcached的原理分析与配置"
date: 2023-05-31
description: "一、Why Memcached? • 高并发访问数据库的痛楚：死锁！ • 硬盘IO之痛：本机：AspNet：HttpRuntime.Cache • 多客户端共享缓存 • Net+Memory&gt;&gt;IO • 读写性能完美 Redies:Mm,1S：读取可以1W次。写：10W • 超简单集群搭"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11415368.html"
---

<h1>一、Why Memcached?</h1>
<p>　　• 高并发访问数据库的痛楚：死锁！</p>
<p>　　• 硬盘IO之痛：本机：AspNet：HttpRuntime.Cache</p>
<p>　　• 多客户端共享缓存</p>
<p>　　• Net+Memory&gt;&gt;IO</p>
<p>　　• 读写性能完美 Redies:Mm,1S：读取可以1W次。写：10W</p>
<p>　　• 超简单集群搭建Cluster</p>
<p>　　• 开源Open Source</p>
<p>　　• 没有提供主从赋值功能，也没提供容灾等功能，所以所有的代码基本都只是考虑性能最佳</p>
<p>　　• 学习成本非常低，入门非常容易</p>
<p>　　• 丰富的成功的案例</p>
<h1>二、软件从单机到分布式</h1>
<p>1、 走向分布式第一步就是解决：多台机器共享登陆信息的问题。</p>
<p>　　例如：现在有3台机器组成了一个Web应用集群，其中一台机器登陆，然后其他另外两台机器共享登陆状态？</p>
<p>　　• 方案一：AspNet 进程外的Session</p>
<p>　　• 方案二：用数据库存储当前登录状态</p>
<p>　　• 方案三：Memcache【性能最好，类似的：Redis，NoSql】</p>
<h1>三、Memcache基础原理</h1>
<p>　　• Socket 服务器端</p>
<p>　　• 数据：键值对存储</p>
<p>　　• 内存处理的算法：</p>
<p>　　　　• 本质就是一个大的哈希表。key最大长度255长度</p>
<p>　　　　• 内存模型：Memcache预先将可支配的内存空间进行分区(Slab)，每个分区里再分成多个块(Chunk)最大1MB，但同一个分区里：块的长度(bytes)是固定的。</p>
<p>　　　　• 插入数据，查找适合自己长度的块，然后插入，会有内存浪费。</p>
<p>　　　　• LRU闲置&gt;过期&gt;最小访问</p>
<p>　　　　• 惰性删除：它并没有提供监控数据过期的限制，而是惰性的，当查到某个key数据时，如果过期那么直接抛弃。</p>
<p>　　• 集群搭建原理</p>
<p>　　　　• Memcache服务器端并没有提供集群功能，但是通过客户端的驱动程序实现了集群配置。</p>
<p>　　　　• 客户端实现集群的原理：首先客户端配置多台集群机器的ip和端口的列表。然后客户端驱动程序在写入之前，首先对key做哈希处理得到哈希值后对总的机器个数进行取余然后就选择余数对应的机器。</p>
<p>Memcache原理图：</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190826225358582-1931020048.png" alt="" /></p>
<h1>四、Windows下使用Memcache</h1>
<p>　　• 下载Memcache：https://www.runoob.com/memcached/window-install-memcached.html</p>
<p>&nbsp;　　• 将服务程序拷贝到一个磁盘上的目录</p>
<p>　　• 安装服务：cmd-&gt;Memcached.exe -d install 打开服务监控窗口可以查看服务是否启动(<span style="color: rgba(255, 0, 0, 1)"><strong>注：Win10安装过程中64位1.4.5报错，换成64位1.4.4没报错，具体什么原因网上也没有详细介绍</strong></span>)</p>
<p>　　• 启动服务：cmd-&gt;Memcached.exe -d start (restart重启、stop关闭、start启动)</p>
<p>　　•&nbsp;检查服务是否启动：连接到Memcache控制台：telnet ServerIp 11211 输入命令：stats检查当前服务状态</p>
<p>　　• 卸载服务：Memcached.exe -d uninstall</p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>安装:</strong></span></p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190827001531398-219000124.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>服务安装完成：</strong></span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190827001129021-112491294.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>启动服务：</strong></span>在memcached上右键-&gt;启动</p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>连接Memcache：</strong></span></p>
<p>注：安装前确保本机电脑上已安装telnet服务</p>
<p>控制面板-&gt;程序-&gt;启动或关闭Windows功能</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190827001956190-97105770.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190827002458889-804333470.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>连接成功(黑丫丫的一片)：</strong></span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190827002545469-1356402311.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>输入第一个命令：stats</strong></span></p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190827002732129-49547861.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>参数值</strong></span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190827002827080-296526981.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>SET(既可以修改，也可以添加，不存在则添加，反之也成立)</strong></span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> 格式：<span style="color: rgba(0, 0, 255, 1)">set</span><span style="color: rgba(0, 0, 0, 1)"> key flags exptime bytes [noreply] value
</span><span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(0, 0, 0, 1)">其中的含义如下：
</span><span style="color: rgba(0, 128, 128, 1)">3</span> 　　key：键值 key-<span style="color: rgba(0, 0, 0, 1)">value 结构中的 key，用于查找缓存值。
</span><span style="color: rgba(0, 128, 128, 1)">4</span> <span style="color: rgba(0, 0, 0, 1)">　　flags：可以包括键值对的整型参数，客户机使用它存储关于键值对的额外信息 。
</span><span style="color: rgba(0, 128, 128, 1)">5</span> 　　exptime：在缓存中保存键值对的时间长度（以秒为单位，<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)"> 表示永远）
</span><span style="color: rgba(0, 128, 128, 1)">6</span> <span style="color: rgba(0, 0, 0, 1)">　　bytes：在缓存中存储的字节数
</span><span style="color: rgba(0, 128, 128, 1)">7</span> <span style="color: rgba(0, 0, 0, 1)">　　noreply（可选）： 该参数告知服务器不需要返回数据
</span><span style="color: rgba(0, 128, 128, 1)">8</span> 　　value：存储的值（始终位于第二行）（可直接理解为key-value结构中的value）</pre>
