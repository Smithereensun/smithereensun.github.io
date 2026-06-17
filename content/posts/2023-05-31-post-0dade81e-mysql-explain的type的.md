---
title: "mysql explain的type的"
date: 2023-05-31
description: "导语 很多情况下，有很多人用各种select语句查询到了他们想要的数据后，往往便以为工作圆满结束了。这些事情往往发生在一些学生亦或刚入职场但之前又没有很好数据库基础的小白身上，但所谓闻道有先后，只要我们小白好好学习，天天向上，还是很靠谱的。 当一个sql查询语句被写出来之后，其实你的工作只完成了一小"
tags:
  - "SQL"
  - "SQL优化"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13096937.html"
---

<h1 id="导语" style="text-align: center">导语</h1>
<p>　　很多情况下，有很多人用各种select语句查询到了他们想要的数据后，往往便以为工作圆满结束了。<br>这些事情往往发生在一些学生亦或刚入职场但之前又没有很好数据库基础的小白身上，但所谓闻道有先后，只要我们小白好好学习，天天向上，还是很靠谱的。</p>
<p>　　当一个sql查询语句被写出来之后，其实你的工作只完成了一小半，接下来更重要的工作是评估你自己写的sql的质量与效率。mysql为我们提供了很有用的辅助武器explain，它向我们展示了mysql接收到一条sql语句的执行计划。根据explain返回的结果我们便可以知道我们的sql写的怎么样，是否会造成查询瓶颈，同时根据结果不断的修改调整查询语句，从而完成sql优化的过程。</p>
<p><img src="https://images2015.cnblogs.com/blog/461250/201511/461250-20151107183901336-1206203739.png" alt="" /></p>
<p>　　虽然 explain返回的结果项很多，这里我们只关注三种，分别是type，key，rows。其中key表明的是这次查找中所用到的索引，rows是指这次查找数据所扫描的行数（这里可以先这样理解，但实际上是内循环的次数）。而type则是本文要详细记录的连接类型，前两项重要而且简单，无需多说。</p>
<h2 id="type----连接类型">type -- 连接类型</h2>
<p>　　type意味着类型，这里的type官方全称是“join type”，意思是“连接类型”,这样很容易给人一种错觉觉得必须需要俩个表以上才有连接类型。事实上这里的连接类型并非字面那样的狭隘，它更确切的说是一种数据库引擎查找表的一种方式，在《高性能mysql》一书中作者更是觉得称呼它为访问类型更贴切一些。</p>
<p>　　mysql5.7中type的类型达到了14种之多，这里只记录和理解最重要且经常遇见的六种类型，它们分别是all,index,range,ref,eq_ref，const。从左到右，它们的效率依次是增强的。撇开sql的具体应用环境以及其他因素，你应当尽量优化你的sql语句，使它的type尽量靠右，但实际运用中还是要综合考虑各个方面的。</p>
<p>接下来，为了演示和重现这几种连接类型，我新建了一个数据测试表，以方面更好的理解这五种类型。</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(128, 128, 128, 1)">|</span> employee <span style="color: rgba(128, 128, 128, 1)">|</span> <span style="color: rgba(0, 0, 255, 1)">CREATE</span> <span style="color: rgba(0, 0, 255, 1)">TABLE</span><span style="color: rgba(0, 0, 0, 1)"> `employee` (
  `rec_id` </span><span style="color: rgba(0, 0, 255, 1)">int</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">11</span>) <span style="color: rgba(128, 128, 128, 1)">NOT</span> <span style="color: rgba(0, 0, 255, 1)">NULL</span><span style="color: rgba(0, 0, 0, 1)"> AUTO_INCREMENT,
  `no` </span><span style="color: rgba(0, 0, 255, 1)">varchar</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">10</span>) <span style="color: rgba(128, 128, 128, 1)">NOT</span> <span style="color: rgba(0, 0, 255, 1)">NULL</span><span style="color: rgba(0, 0, 0, 1)">,
  `name` </span><span style="color: rgba(0, 0, 255, 1)">varchar</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">20</span>) <span style="color: rgba(128, 128, 128, 1)">NOT</span> <span style="color: rgba(0, 0, 255, 1)">NULL</span><span style="color: rgba(0, 0, 0, 1)">,
  `position` </span><span style="color: rgba(0, 0, 255, 1)">varchar</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">20</span>) <span style="color: rgba(128, 128, 128, 1)">NOT</span> <span style="color: rgba(0, 0, 255, 1)">NULL</span><span style="color: rgba(0, 0, 0, 1)">,
  `age` </span><span style="color: rgba(0, 0, 255, 1)">varchar</span>(<span style="color: rgba(128, 0, 0, 1); font-weight: bold">2</span>) <span style="color: rgba(128, 128, 128, 1)">NOT</span> <span style="color: rgba(0, 0, 255, 1)">NULL</span><span style="color: rgba(0, 0, 0, 1)">,
  </span><span style="color: rgba(0, 0, 255, 1)">PRIMARY</span> <span style="color: rgba(0, 0, 255, 1)">KEY</span><span style="color: rgba(0, 0, 0, 1)"> (`rec_id`)
) ENGINE</span><span style="color: rgba(128, 128, 128, 1)">=</span>InnoDB AUTO_INCREMENT<span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(128, 0, 0, 1); font-weight: bold">6</span> <span style="color: rgba(0, 0, 255, 1)">DEFAULT</span> CHARSET<span style="color: rgba(128, 128, 128, 1)">=</span>utf8 <span style="color: rgba(128, 128, 128, 1)">|</span></pre>
