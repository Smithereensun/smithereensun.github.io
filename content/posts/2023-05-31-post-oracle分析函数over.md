---
title: "Oracle分析函数Over()"
date: 2023-05-31
description: "Over()分析函数 说明：聚合函数（如sum()、max()等）可以计算基于组的某种聚合值，但是聚合函数对于某个组只能返回一行记录。若想对于某组返回多行记录，则需要使用分析函数。 rank()/dense_rank over(partition by ... order by ...) 说明：ov"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12447963.html"
---

<h1 style="text-align: center">Over()分析函数</h1>
<p>　　说明：聚合函数（如sum()、max()等）可以计算基于组的某种聚合值，但是聚合函数对于某个组只能返回一行记录。若想对于某组返回多行记录，则需要使用分析函数。</p>
<h2>rank()/dense_rank over(partition by ... order by ...)</h2>
<p>说明：over()在什么条件之上;&nbsp;</p>
<p>　　partition by 按哪个字段划分组；</p>
<p>　　order by 按哪个字段排序；</p>
<p>注意：</p>
<p>　　（1）使用rank()/dense_rank() 时，必须要带order by否则非法</p>
<p>　　（2）rank()/dense_rank()分级的区别：</p>
<p>　　　　rank(): 跳跃排序，如果有两个第一级时，接下来就是第三级。<br>　　　　dense_rank(): 连续排序，如果有两个第一级时，接下来仍然是第二级。</p>
<p>示例：查询每个部门工资最高的员工信息</p>
<h3>一般的写法</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">SELECT</span><span style="color: rgba(0, 0, 0, 1)"> E.ENAME, E.JOB, E.SAL, E.DEPTNO
  </span><span style="color: rgba(0, 0, 255, 1)">FROM</span><span style="color: rgba(0, 0, 0, 1)"> SCOTT.EMP E,
       (</span><span style="color: rgba(0, 0, 255, 1)">SELECT</span> E.DEPTNO, <span style="color: rgba(255, 0, 255, 1)">MAX</span>(E.SAL) SAL <span style="color: rgba(0, 0, 255, 1)">FROM</span> SCOTT.EMP E <span style="color: rgba(0, 0, 255, 1)">GROUP</span> <span style="color: rgba(0, 0, 255, 1)">BY</span><span style="color: rgba(0, 0, 0, 1)"> E.DEPTNO) ME
 </span><span style="color: rgba(0, 0, 255, 1)">WHERE</span> E.DEPTNO <span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(0, 0, 0, 1)"> ME.DEPTNO
   </span><span style="color: rgba(128, 128, 128, 1)">AND</span> E.SAL <span style="color: rgba(128, 128, 128, 1)">=</span> ME.SAL;</pre>
