---
title: "Mybatis 二级缓存的使用"
date: 2020-07-13
description: "Mybatis二级缓存 简介：二级缓存是namesace级别的，多个SqlSession去操作同个namespace下的Mapper的sql语句，多个SqlSession可以共用二级缓存，如果两个mapper的namespace相同，(既使是两个mapper，那么这两个mapper中执行sql查询的"
tags:
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13296267.html"
---

<h1 style="text-align: center">Mybatis二级缓存</h1>
<ul>
<li>简介：<span style="color: rgba(255, 0, 0, 1)"><strong>二级缓存是namesace级别的</strong></span>，多个SqlSession去操作同个namespace下的Mapper的sql语句，多个SqlSession可以共用二级缓存，如果两个mapper的namespace相同，(既使是两个mapper，那么这两个mapper中执行sql查询的数据也将存在相同的二级缓存区域中，但是最后是每个Mapper单独的命名空间)</li>
<li>基于PerpetualCache的HashMap本地缓存，可自定义存储源，如Ehcacche/Redis等</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>默认</strong></span>是<span style="color: rgba(255, 0, 0, 1)"><strong>没有开启二级缓存</strong></span></li>
<li>操作流程：第一次调用某个namespacce下的SQL去查询信息，查询到的信息会存放该mapper对应的二级缓存区域。第二次调用同个namespace下的mapper映射文件中，相同的sql去查询信息，会去对应的二级缓存内取结果</li>
</ul>
<h1 style="text-align: center"><strong><span style="color: rgba(255, 0, 0, 1)">失效策略</span></strong></h1>
<p>　　执行同个namespace下的mapper映射文件中增删改sql，并执行了commit操作，会清空该二级缓存</p>
<p>注意：实现二级缓存的时候，Mybatis建议返回的POJO是可序列化的，也就是建议实现Serializable接口</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>缓存淘汰策略</strong></span>：会使用默认的<span style="color: rgba(255, 0, 0, 1)"><strong>LRU</strong></span>算法来收回(最近最少使用的)</p>
<h1 style="text-align: center">开启缓存</h1>
<p>如何开启某个二级缓存mapper.xml里面配置</p>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">开启Mapper的namespace下的二级缓存</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">
        eviction：代表的是缓存回收策略，常见下面两种
        1）、LRU，最近最少使用的，移除最长时间不用的对象
        2）、FIFO，先进先出，按对象进入缓存的顺序来移除他们
        flushInterval：刷新间隔时间，单位为毫秒，这里配置的是10秒，如果不配置他，当SQL被执行的时候才会去刷新缓存
        size：引入数目，代表缓存最多可以存储多少个对象，设置过大会导致内存溢出
        readOnly：只读，缓存数据只能读取不能修改，默认值为false
    </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">cache </span><span style="color: rgba(255, 0, 0, 1)">eviction</span><span style="color: rgba(0, 0, 255, 1)">="LRU"</span><span style="color: rgba(255, 0, 0, 1)"> flushInterval</span><span style="color: rgba(0, 0, 255, 1)">="100000"</span><span style="color: rgba(255, 0, 0, 1)"> readOnly</span><span style="color: rgba(0, 0, 255, 1)">="true"</span><span style="color: rgba(255, 0, 0, 1)"> size</span><span style="color: rgba(0, 0, 255, 1)">="1024"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">cache</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
