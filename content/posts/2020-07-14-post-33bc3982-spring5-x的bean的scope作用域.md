---
title: "Spring5.X的bean的scope作用域"
date: 2020-07-14
description: "scope属性 singleton：单例，默认值，调用getBean方法返回是同一个对象，实例会被缓存起来，效率比较高，当一个bean被标识为singleton时候，spring的IOC容器中只会存在一个该bean prototype：多例，调用getBean方法创建不同的对象，会频繁的创建和销毁对"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13302902.html"
---

<h1>scope属性</h1>
<ul>
<li><strong><span style="color: rgba(255, 0, 0, 1)">singleton</span></strong>：单例，默认值，调用getBean方法返回是同一个对象，实例会被缓存起来，效率比较高，当一个bean被标识为singleton时候，spring的IOC容器中只会存在一个该bean</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>prototype</strong></span>：多例，调用getBean方法创建不同的对象，会频繁的创建和销毁对象造成很大的开销</li>
其他少用(作用于只在WebApplicationContext)
<ul>
<li>request：每个Http请求都会创建一个新的bean</li>
<li>session：每个Http Session请求都会创建一个新的bean</li>
<li>global session(基本不用)</li>
</ul>
</ul>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200714224909416-1310899886.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
