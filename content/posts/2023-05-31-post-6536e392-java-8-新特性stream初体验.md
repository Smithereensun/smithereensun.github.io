---
title: "JAVA 8 新特性Stream初体验"
date: 2023-05-31
description: "什么是 Stream？ Stream（流）是一个来自数据源的元素队列并支持聚合操作 &lt;strong元素队列&lt; strong=&quot;&quot;&gt;元素是特定类型的对象，形成一个队列。 Java中的Stream并不会存储元素，而是按需计算。 数据源&#160;流的来源。 可以是集"
tags:
  - "JAVA"
  - "JDK8~13"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11624500.html"
---

<h1><a name="shwtop"></a>什么是 Stream？</h1>
<p>Stream（流）是一个来自数据源的元素队列并支持聚合操作</p>
<ul>
<li>&lt;strong元素队列&lt; strong=""&gt;元素是特定类型的对象，形成一个队列。 Java中的Stream并不会存储元素，而是按需计算。</li>
<li><strong>数据源</strong>&nbsp;流的来源。 可以是集合，数组，I/O channel， 产生器generator 等。</li>
<li><strong>聚合操作</strong>&nbsp;类似SQL语句一样的操作， 比如filter, map, reduce, find, match, sorted等。</li>
</ul>
<p>和以前的Collection操作不同， Stream操作还有两个基础的特征：</p>
<ul>
<li><strong>Pipelining</strong>: 中间操作都会返回流对象本身。 这样多个操作可以串联成一个管道， 如同流式风格（fluent style）。 这样做可以对操作进行优化， 比如延迟执行(laziness)和短路( short-circuiting)。</li>
<li><strong>内部迭代</strong>： 以前对集合遍历都是通过Iterator或者For-Each的方式, 显式的在集合外部进行迭代， 这叫做外部迭代。 Stream提供了内部迭代的方式， 通过访问者模式(Visitor)实现。</li>
</ul>
<h3>题目：</h3>
<p>　　有一个集合，里面存放字符串如："小王,98"、"小李,95"、"小陈,87"，要求打印输出所有成绩当中大于90分的数字。</p>
<h3>常规写法</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> main(String[] args) {
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span>         ArrayList&lt;String&gt; arrayList=<span style="color: rgba(0, 0, 255, 1)">new</span> ArrayList&lt;String&gt;<span style="color: rgba(0, 0, 0, 1)">();
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span>         arrayList.add(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">小王,98</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span>         arrayList.add(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">小李,95</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>         arrayList.add(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">小陈,87</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>         <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = <span style="color: rgba(128, 0, 128, 1)">0</span>; i &lt; arrayList.size(); i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>             String record=arrayList.<span style="color: rgba(0, 0, 255, 1)">get</span><span style="color: rgba(0, 0, 0, 1)">(i);
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>             String score=record.split(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">,</span><span style="color: rgba(128, 0, 0, 1)">"</span>)[<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>             <span style="color: rgba(0, 0, 255, 1)">int</span> num =<span style="color: rgba(0, 0, 0, 1)">Integer.parseInt(score);
</span><span style="color: rgba(0, 128, 128, 1)">10</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (num&gt;<span style="color: rgba(128, 0, 128, 1)">90</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">11</span>                 System.<span style="color: rgba(0, 0, 255, 1)">out</span><span style="color: rgba(0, 0, 0, 1)">.println(num);
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">14</span>     }</pre>
