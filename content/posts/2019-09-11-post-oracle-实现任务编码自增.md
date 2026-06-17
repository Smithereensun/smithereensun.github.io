---
title: "oracle 实现任务编码自增"
date: 2019-09-11
description: "业务需求：任务编号前面4位数(通过查询其他表，值不确定)，后面5位数实现自增 实现方法如下 1、创建序列 2、创建触发器"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11506595.html"
---

<p>业务需求：任务编号前面4位数(通过查询其他表，值不确定)，后面5位数实现自增</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201909/1504448-20190911153118312-1279655147.png" alt="" /></p>
<p>&nbsp;</p>
<p>实现方法如下</p>
<p>1、创建序列</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)"> create sequence GENERAL_DES_TASK_SEQ_1
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span>  increment by <span style="color: rgba(128, 0, 128, 1)">1</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span>  start with <span style="color: rgba(128, 0, 128, 1)">1</span>
<span style="color: rgba(0, 128, 128, 1)"> 4</span>  maxvalue <span style="color: rgba(128, 0, 128, 1)">999999</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> 
<span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">格式：
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 0, 1)"> create sequence 序列名
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>  increment by <span style="color: rgba(128, 0, 128, 1)">1</span>
<span style="color: rgba(0, 128, 128, 1)"> 9</span>  start with <span style="color: rgba(128, 0, 128, 1)">1</span>
<span style="color: rgba(0, 128, 128, 1)">10</span>  maxvalue <span style="color: rgba(128, 0, 128, 1)">999999999</span>;</pre>
