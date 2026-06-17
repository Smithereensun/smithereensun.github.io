---
title: "Java集合之Map"
date: 2023-05-31
description: "Map基础介绍 什么是map数据结构 底层就是一个数组结构，数组中的每一项又是一个链表，即数组和链表的结合体 Table是数组，数组的元素时Entry Entry元素时一个key-value键值对，它持有一个指向下一个Entry元素的引用，table数组的每个entry元素同时也作为当前Entry链"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13383035.html"
---

<h1 style="text-align: center">Map基础介绍</h1>
<h2>什么是map数据结构</h2>
<ul>
<li>底层就是一个数组结构，数组中的每一项又是一个链表，即数组和链表的结合体</li>
<li>Table是数组，数组的元素时Entry</li>
<li>Entry元素时一个key-value键值对，它持有一个指向下一个Entry元素的引用，table数组的每个entry元素同时也作为当前Entry链表的首节点，也指向了该链表的下一个Entry元素</li>
</ul>
<h2>常见的实现类</h2>
<h3>HashMap</h3>
<ul>
<li>一个散列桶(数组和链表)，它存储的内容是键值对(key-value)映射</li>
<li>是基于hashing的原理，使用put(key,value)存储对象到HashMap中，使用get(key)从HashMap中获取对象。当put()方法传递键和值时，会先对键调用hashCode()方法，计算并返回的hashCode是用于找到Map数组的bucket位置来存储Entry对象的，是非线程安全的，所以HashMap从操作速度很快</li>
</ul>
<p>区别：乱序</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200727235544706-1138436682.png" alt="" loading="lazy" /></p>
<h3>TreeMap</h3>
<ul>
<li>在数据的存储过程中，能够自动对数据进行排序，实现了StoredMap接口，它是有序集合</li>
<li>TreeMap使用的存储结构是平衡二叉树，也成为红黑树</li>
<li>默认排序规则：按照key的字典顺序来排序(升序)，也可以自定义排序规则，要实现Comparator接口</li>
</ul>
<p>区别：按一定规则排序</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200727235632771-1640686564.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h3>LinkedHashMap</h3>
<p>区别：放入怎样顺序，打印怎样顺序</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200727235743876-1876913042.png" alt="" loading="lazy" /></p>
<h2>Map常用API</h2>
<div class="cnblogs_code">
<pre>        HashMap&lt;String, String&gt; map=<span style="color: rgba(0, 0, 255, 1)">new</span> HashMap&lt;String, String&gt;<span style="color: rgba(0, 0, 0, 1)">();
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">往map里面放key-value</span>
        map.put("小陈", "上海"<span style="color: rgba(0, 0, 0, 1)">);
        map.put(</span>"小红", "深圳"<span style="color: rgba(0, 0, 0, 1)">);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">根据key获取value</span>
        String str=map.get("小陈"<span style="color: rgba(0, 0, 0, 1)">);
        System.out.println(str);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">判断是否包含某个key</span>
        Boolean flag=map.containsKey("小陈"<span style="color: rgba(0, 0, 0, 1)">);
        System.out.println(flag);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">返回map的元素数量</span>
        <span style="color: rgba(0, 0, 255, 1)">int</span> size=<span style="color: rgba(0, 0, 0, 1)">map.size();
        System.out.println(size);
        map.put(</span>"小陈", "上海"<span style="color: rgba(0, 0, 0, 1)">);
        System.out.println(map.size());
        Collection</span>&lt;String&gt; values =<span style="color: rgba(0, 0, 0, 1)"> map.values();
        </span><span style="color: rgba(0, 0, 255, 1)">for</span><span style="color: rgba(0, 0, 0, 1)">(String s:values) {
            System.out.println(s);
        }
        Set</span>&lt;Entry&lt;String, String&gt;&gt; entrySet =<span style="color: rgba(0, 0, 0, 1)"> map.entrySet();
        </span><span style="color: rgba(0, 0, 255, 1)">for</span><span style="color: rgba(0, 0, 0, 1)">(Map.Entry entry:entrySet) {
            System.out.println(</span>"key="+entry.getKey()+",value="+<span style="color: rgba(0, 0, 0, 1)">entry.getValue());
        }</span></pre>
