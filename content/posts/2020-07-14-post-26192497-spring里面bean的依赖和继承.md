---
title: "Spring里面bean的依赖和继承"
date: 2020-07-14
description: "继承 bean继承：两个类之间大多数的属性都相同，避免重复配置，通过bean标签的parent属性重用已有的Bean元素的配置信息 继承指的是配置信息的复用，和java类的继承没有关系 video.java（父类） package net.cybclass.sp.domain; public cla"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13303172.html"
---

<h1 style="text-align: center">继承</h1>
<ul>
<li>bean继承：两个类之间大多数的属性都相同，避免重复配置，通过bean标签的parent属性重用已有的Bean元素的配置信息</li>
<li>继承指的是配置信息的复用，和java类的继承没有关系</li>
</ul>
<p>video.java（<strong><span style="color: rgba(255, 0, 0, 1)">父类</span></strong>）</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.domain;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Video {
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> id;
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String title;
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> getId() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> id;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> setId(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> id) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.id =<span style="color: rgba(0, 0, 0, 1)"> id;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getTitle() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> title;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setTitle(String title) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.title =<span style="color: rgba(0, 0, 0, 1)"> title;
    }
}</span></pre>
