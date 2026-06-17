---
title: "Java集合之Set"
date: 2023-05-31
description: "什么是Set数据结构 Set相对于List是简单的一种集合，具有和Collection完全一样的接口，只是实现接口不同，Set不保存重复的元素，存储一组唯一，无序的对象 Set中的元素是不重复的，实现细节可以看Map，因为这些Set的实现都是对应的Map的一种封装。比如HashSet是对HashMa"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13388704.html"
---

<h1 style="text-align: center">什么是Set数据结构</h1>
<ul>
<li>Set相对于List是简单的一种集合，具有和Collection完全一样的接口，只是实现接口不同，Set不保存重复的元素，存储一组唯一，无序的对象</li>
<li>Set中的元素是不重复的，实现细节可以看Map，因为这些Set的实现都是对应的Map的一种封装。比如HashSet是对HashMap的封装，TreeSet对应TreeMap</li>
<li>Set底层是一个HashMap，由于HashMap的put()方法是一个键值对，当新放入HashMap的Entry中key与集合原有Entry的key相同（hashCode()返回值相同，通过equals比较也返回true），新添加的Entry的value会将覆盖原来Entry的value，但key不会有任何改变</li>
<li>允许包含值为null的元素，但最多只能有一个null元素</li>
</ul>
<h2>常见的实现类</h2>
<ul>
<li>HashSet
<ul>
<li>HashSet类按照哈希算法来存取集合中的对象，存取速度比较快</li>
<li>对应的Map是hashMap，是基于Hash的快速元素插入，元素无顺序</li>
</ul>
</li>
<li>TreeSet
<ul>
<li>TreeSet类实现了SortedSet接口，能够对集合中的对象进行排序</li>
</ul>
</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建对象,HashSet和TreeSet api⼀样</span>
Set&lt;Integer&gt; set = <span style="color: rgba(0, 0, 255, 1)">new</span> HashSet&lt;&gt;<span style="color: rgba(0, 0, 0, 1)">();
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">往容器⾥⾯添加对象</span>
set.add("jack"<span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">清空元素</span>
<span style="color: rgba(0, 0, 0, 1)">set.clear();
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">返回⼤⼩</span>
<span style="color: rgba(0, 0, 0, 1)">set.size();
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">根据对象删除元素</span>
set.remove("jack"<span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">是否为空</span>
set.isEmpty();</pre>
