---
title: "MyBatis详解 一篇就够啦"
date: 2023-05-31
description: "第1章MyBatis框架配置文件详解 1.1 typeHandlers类型转换器 每当MyBatis 设置参数到PreparedStatement 或者从ResultSet 结果集中取得值时，就会使用TypeHandler 来处理数据库类型与java 类型之间转换。下表描述了默认 TypeHandl"
tags:
  - "JAVA"
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11656461.html"
---

<h1>第1章MyBatis框架配置文件详解</h1>
<h2>1.1 typeHandlers类型转换器</h2>
<p>　　每当MyBatis 设置参数到PreparedStatement 或者从ResultSet 结果集中取得值时，就会使用TypeHandler 来处理数据库类型与java 类型之间转换。下表描述了默认</p>
<p>TypeHandlers</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191011194636429-1672088814.png" alt="" /></p>
<h3>&nbsp;1.1.1 自定义类型转换器</h3>
<p>假设表中字段是int类型,而实体类与之对应的属性是boolean类型,此时可以采用自定义类型转换器进行对应</p>
<p>(1)实体类</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)">package com.chenyanbin.beans;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> 
<span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Dept {
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span>     <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> Integer deptNo;
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>     <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String dname;
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>     <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String loc;
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>     <span style="color: rgba(255, 0, 0, 1)"><strong>private boolean flag;
</strong></span><span style="color: rgba(0, 128, 128, 1)"> 8</span>     <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Integer getDeptNo() {
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> deptNo;
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">11</span>     <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> boolean isFlag() {
</span><span style="color: rgba(0, 128, 128, 1)">12</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> flag;
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">14</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setFlag(boolean flag) {
</span><span style="color: rgba(0, 128, 128, 1)">15</span>         <span style="color: rgba(0, 0, 255, 1)">this</span>.flag =<span style="color: rgba(0, 0, 0, 1)"> flag;
</span><span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">17</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setDeptNo(Integer deptNo) {
</span><span style="color: rgba(0, 128, 128, 1)">18</span>         <span style="color: rgba(0, 0, 255, 1)">this</span>.deptNo =<span style="color: rgba(0, 0, 0, 1)"> deptNo;
</span><span style="color: rgba(0, 128, 128, 1)">19</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">20</span>     <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getDname() {
</span><span style="color: rgba(0, 128, 128, 1)">21</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> dname;
</span><span style="color: rgba(0, 128, 128, 1)">22</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">23</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setDname(String dname) {
</span><span style="color: rgba(0, 128, 128, 1)">24</span>         <span style="color: rgba(0, 0, 255, 1)">this</span>.dname =<span style="color: rgba(0, 0, 0, 1)"> dname;
</span><span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">26</span>     <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getLoc() {
</span><span style="color: rgba(0, 128, 128, 1)">27</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> loc;
</span><span style="color: rgba(0, 128, 128, 1)">28</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">29</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setLoc(String loc) {
</span><span style="color: rgba(0, 128, 128, 1)">30</span>         <span style="color: rgba(0, 0, 255, 1)">this</span>.loc =<span style="color: rgba(0, 0, 0, 1)"> loc;
</span><span style="color: rgba(0, 128, 128, 1)">31</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">32</span> }</pre>
