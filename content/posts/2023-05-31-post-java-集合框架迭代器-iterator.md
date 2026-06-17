---
title: "Java 集合框架迭代器(Iterator)"
date: 2023-05-31
description: "什么是迭代器 使用循环遍历集合 普通for循环 for(int i=0;i&lt;10;i++){} 增强for循环 for(String str:list){} 什么是迭代器Iterator Iterator是Java中的一个接口，核心作用就是用来遍历容器的元素，当容器实现了Iterator接口后"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13401059.html"
---

<h1 style="text-align: center">什么是迭代器</h1>
<h2>使用循环遍历集合</h2>
<ul>
<li>普通for循环
<ul>
<li>for(int i=0;i&lt;10;i++){}</li>
</ul>
</li>
<li>增强for循环
<ul>
<li>for(String str:list){}</li>
</ul>
</li>
</ul>
<h2>什么是迭代器Iterator</h2>
<ul>
<li>Iterator是Java中的一个接口，核心作用就是用来遍历容器的元素，当容器实现了Iterator接口后，可以通过调用Iterator()方法获取一个Iterator对象</li>
<li>为啥是调用容器里面的Iterator方法呢？
<ul>
<li>因为容器的实现有多种，不同的容器遍历规则不一样，比如：ArrayList、LinkedList、HashSet、TreeSet等，所以设计了Iterator接口，让容器本身去实现这个接口，实现里面的方法，从而让开发人员不用关心容器的遍历机制，直接使用对应的方法即可</li>
</ul>
</li>
</ul>
<h2>三个核心方法</h2>
<ul>
<li>boolean hashNext()：用于判断Iterator内是否有下个元素，如果有则返回true，没有则false</li>
<li>Object next()：返回Iterator的下一个元素，同时指针也会向后移动一位</li>
<li>void remove()：删除指针的上一个元素(<strong><span style="color: rgba(255, 0, 0, 1)">建议使用自己容器里的方法</span></strong>)</li>
</ul>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> testSet() {
        Set</span>&lt;String&gt; set = <span style="color: rgba(0, 0, 255, 1)">new</span> HashSet&lt;&gt;<span style="color: rgba(0, 0, 0, 1)">();
        set.add(</span>"jack"<span style="color: rgba(0, 0, 0, 1)">);
        set.add(</span>"tom"<span style="color: rgba(0, 0, 0, 1)">);
        set.add(</span>"marry"<span style="color: rgba(0, 0, 0, 1)">);
        set.add(</span>"tony"<span style="color: rgba(0, 0, 0, 1)">);
        set.add(</span>"jack"<span style="color: rgba(0, 0, 0, 1)">);
        Iterator</span>&lt;String&gt; iterator =<span style="color: rgba(0, 0, 0, 1)"> set.iterator();
        </span><span style="color: rgba(0, 0, 255, 1)">while</span><span style="color: rgba(0, 0, 0, 1)"> (iterator.hasNext()) {
            String str </span>=<span style="color: rgba(0, 0, 0, 1)"> iterator.next();
            System.out.println(str);
        }
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> testList() {
        List</span>&lt;String&gt; list = <span style="color: rgba(0, 0, 255, 1)">new</span> ArrayList&lt;&gt;<span style="color: rgba(0, 0, 0, 1)">();
        list.add(</span>"jack"<span style="color: rgba(0, 0, 0, 1)">);
        list.add(</span>"tom"<span style="color: rgba(0, 0, 0, 1)">);
        list.add(</span>"mary"<span style="color: rgba(0, 0, 0, 1)">);
        list.add(</span>"tim"<span style="color: rgba(0, 0, 0, 1)">);
        list.add(</span>"tony"<span style="color: rgba(0, 0, 0, 1)">);
        list.add(</span>"eric"<span style="color: rgba(0, 0, 0, 1)">);
        list.add(</span>"jack"<span style="color: rgba(0, 0, 0, 1)">);
        Iterator</span>&lt;String&gt; iterator =<span style="color: rgba(0, 0, 0, 1)"> list.iterator();
        </span><span style="color: rgba(0, 0, 255, 1)">while</span><span style="color: rgba(0, 0, 0, 1)"> (iterator.hasNext()) {
            String str </span>=<span style="color: rgba(0, 0, 0, 1)"> iterator.next();
            System.out.println(str);
        }
    }</span></pre>
