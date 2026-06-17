---
title: "Jquery补充及插件"
date: 2020-03-08
description: "此篇为jQuery补充的一些知识点，详细资料请看另一篇博客，地址：https://www.cnblogs.com/chenyanbin/p/10454503.html 一、jQuery中提供的两个函数 1 $.map(array,callback(element,index)); 2 1.对于数组a"
tags:
  - "JavaScript"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10747656.html"
---

<p>此篇为jQuery补充的一些知识点，详细资料请看另一篇博客，地址：https://www.cnblogs.com/chenyanbin/p/10454503.html</p>
<h1>一、jQuery中提供的两个函数</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 0, 0, 1)">$.map(array,callback(element,index));
</span><span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(0, 0, 0, 1)">    1.对于数组array中的每个元素，调用callback()函数，最终返回一个新的数组。原数组不变
</span><span style="color: rgba(0, 128, 128, 1)">3</span> 
<span style="color: rgba(0, 128, 128, 1)">4</span> <span style="color: rgba(0, 0, 0, 1)">$.each(array,fn);遍历数组，return false来退出循环。
</span><span style="color: rgba(0, 128, 128, 1)">5</span> <span style="color: rgba(0, 0, 0, 1)">    1.主要用来遍历数组，不修改数组，对于普通数组或者“键值对”数组都没有问题
</span><span style="color: rgba(0, 128, 128, 1)">6</span>     2.在each函数中可以直接使用this，表示当前元素的值</pre>
