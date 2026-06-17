---
title: "Oracle Job定时任务详解、跨数据库数据同步"
date: 2023-05-31
description: "业务需求，需要与A公司做数据对接，我们公司用的Oracle，A公司用的SQL Server数据库，如何跨数据库建立连接呢？这里使用的是DBLink，不会配置的请看我的另外一篇博客:https://www.cnblogs.com/chenyanbin/p/11291752.html 如果做数据同步呢？"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11356933.html"
---

<p><span style="font-family: &quot;Microsoft YaHei&quot;">　　业务需求，需要与A公司做数据对接，我们公司用的Oracle，A公司用的SQL Server数据库，如何跨数据库建立连接呢？这里使用的是DBLink，不会配置的请看我的另外一篇博客:<span style="color: rgba(255, 0, 0, 1)"><strong>https://www.cnblogs.com/chenyanbin/p/11291752.html</strong></span></span></p>
<p><span style="font-family: &quot;Microsoft YaHei&quot;"><span style="color: rgba(255, 0, 0, 1)"><span style="color: rgba(0, 0, 0, 1)">　　如果做数据同步呢？上面我们已经通过DBLink与SQL Server建立连接了，那么我们就可以获取A公司表中的数据。在通过Oracle Job定时任务，具体JOB还有那些功能，这里不做详细介绍了，百度上一大堆，这里我们只讲解Oracle Job创建步骤。</span></span></span></p>
<p><span style="font-family: &quot;Microsoft YaHei&quot;"><span style="color: rgba(255, 0, 0, 1)"><span style="color: rgba(0, 0, 0, 1)">　　我们已经知道job是一个定时任务，也就是说可以在一个规定的时间内，执行某一项任务，这个任务就是“存储过程”。</span></span></span></p>
<h2>第一步：先创建存储过程(做一个简单DEMO往一张表插入当前时间)</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> create or replace procedure proc_add_test <span style="color: rgba(0, 0, 255, 1)">as</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">begin
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span>   insert into test values (to_char(sysdate, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">yyyy-mm-dd hh:mi</span><span style="color: rgba(128, 0, 0, 1)">'</span>));<span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">向测试表插入数据</span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 4</span>   commit; <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">提交</span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 0, 1)">end;
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> 
<span style="color: rgba(0, 128, 128, 1)"> 7</span> 
<span style="color: rgba(0, 128, 128, 1)"> 8</span> create or replace procedure 存储过程名称 <span style="color: rgba(0, 0, 255, 1)">as</span>
<span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">begin
</span><span style="color: rgba(0, 128, 128, 1)">10</span>   <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">业务逻辑片段</span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">11</span> end;</pre>
