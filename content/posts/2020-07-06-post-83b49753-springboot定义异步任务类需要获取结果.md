---
title: "SpringBoot定义异步任务类需要获取结果"
date: 2020-07-06
description: "注意点： 要把异步任务封装到类里面，不能直接写到Controller 增加Future&lt;String&gt;返回结果AsyncResult&lt;String&gt;(&quot;task执行完成&quot;) 如果需要拿到结果，需要判断全部的task.isDone()"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13257853.html"
---

<p>注意点：</p>
<ol>
<li>要把异步任务封装到类里面，不能直接写到Controller</li>
<li>增加Future&lt;String&gt;返回结果AsyncResult&lt;String&gt;("task执行完成")</li>
<li>如果需要拿到结果，需要判断全部的task.isDone()</li>
</ol>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706220002101-1428087729.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706220057613-1024433281.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706220126116-614168533.png" alt="" loading="lazy" /></p>
