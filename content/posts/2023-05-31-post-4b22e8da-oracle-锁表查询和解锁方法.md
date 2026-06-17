---
title: "Oracle 锁表查询和解锁方法"
date: 2023-05-31
description: "system登录 查询被锁表信息 select sess.sid, sess.serial#, lo.oracle_username, lo.os_user_name, ao.object_name, lo.locked_mode from v$locked_object lo, dba_objec"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12800777.html"
---

<h1>system登录</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202004/1504448-20200429105203241-1746093088.png" alt="" /></p>
<h1>查询被锁表信息</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202004/1504448-20200429105750421-1778889030.png" alt="" /></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">select</span><span style="color: rgba(0, 0, 0, 1)"> sess.sid,
       sess.serial#,
       lo.oracle_username,
       lo.os_user_name,
       ao.</span><span style="color: rgba(255, 0, 255, 1)">object_name</span><span style="color: rgba(0, 0, 0, 1)">,
       lo.locked_mode     </span><span style="color: rgba(0, 0, 255, 1)">from</span><span style="color: rgba(0, 0, 0, 1)"> v$locked_object lo,
       dba_objects        ao,
       v$session          sess </span><span style="color: rgba(0, 0, 255, 1)">where</span> ao.<span style="color: rgba(255, 0, 255, 1)">object_id</span> <span style="color: rgba(128, 128, 128, 1)">=</span> lo.<span style="color: rgba(255, 0, 255, 1)">object_id</span> <span style="color: rgba(128, 128, 128, 1)">and</span> lo.session_id <span style="color: rgba(128, 128, 128, 1)">=</span> sess.sid;</pre>
