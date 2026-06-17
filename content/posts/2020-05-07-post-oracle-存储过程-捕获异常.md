---
title: "Oracle 存储过程 捕获异常"
date: 2020-05-07
description: "1、带参数插入并带返回值，异常信息 CREATE OR REPLACE PROCEDURE test_pro (v_id in int,v_name in varchar2,app_code out int,error_Msg out varchar) -- in 是输入参数；out 输出参数 IS"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12749912.html"
---

<p>1、带参数插入并带返回值，异常信息</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">CREATE</span> <span style="color: rgba(128, 128, 128, 1)">OR</span> <span style="color: rgba(255, 0, 255, 1)">REPLACE</span> <span style="color: rgba(0, 0, 255, 1)">PROCEDURE</span> test_pro (v_id <span style="color: rgba(128, 128, 128, 1)">in</span> <span style="color: rgba(0, 0, 255, 1)">int</span>,v_name <span style="color: rgba(128, 128, 128, 1)">in</span> <span style="color: rgba(0, 0, 255, 1)">varchar2</span>,app_code out <span style="color: rgba(0, 0, 255, 1)">int</span>,error_Msg out <span style="color: rgba(0, 0, 255, 1)">varchar</span>) <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)"> in 是输入参数；out 输出参数</span>
<span style="color: rgba(0, 0, 255, 1)">IS</span>
<span style="color: rgba(0, 0, 255, 1)">BEGIN</span>
        <span style="color: rgba(0, 0, 255, 1)">INSERT</span> <span style="color: rgba(0, 0, 255, 1)">INTO</span> proc_test (id,name) <span style="color: rgba(0, 0, 255, 1)">VALUES</span> (v_id,v_name); <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">往表中插入一条数据</span>
        app_code:<span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(128, 0, 0, 1); font-weight: bold">8</span>;          <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">执行状态码，8 成功；9失败</span>
        error_Msg:<span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">执行成功</span><span style="color: rgba(255, 0, 0, 1)">'</span>; <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">执行执行结果</span>
        <span style="color: rgba(0, 0, 255, 1)">commit</span>; <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">提交事务</span>
<span style="color: rgba(0, 0, 0, 1)">EXCEPTION
        </span><span style="color: rgba(0, 0, 255, 1)">rollback</span>; <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">回滚提交的事务</span>
        <span style="color: rgba(0, 0, 255, 1)">when</span> others <span style="color: rgba(0, 0, 255, 1)">then</span><span style="color: rgba(0, 0, 0, 1)"> 
          app_code:</span><span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(128, 0, 0, 1); font-weight: bold">9</span>; <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">执行状态码，8 成功；9失败</span>
          error_Msg:<span style="color: rgba(128, 128, 128, 1)">=</span>SUBSTR(SQLERRM, <span style="color: rgba(128, 0, 0, 1); font-weight: bold">1</span>, <span style="color: rgba(128, 0, 0, 1); font-weight: bold">200</span>); <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">返回报错信息</span>
          <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">存储过程调用失败，往存储过程日志表追加一条记录，方便以后查询；第一个参数：调用存储过程名，第二个参数：错误信息</span>
          <span style="color: rgba(0, 0, 255, 1)">INSERT</span> <span style="color: rgba(0, 0, 255, 1)">INTO</span> proc_error (proc_name,msg_error) <span style="color: rgba(0, 0, 255, 1)">VALUES</span> (<span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(255, 0, 0, 1)">test_pro</span><span style="color: rgba(255, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,error_Msg);
          </span><span style="color: rgba(0, 0, 255, 1)">commit</span>; <span style="color: rgba(0, 128, 128, 1)">--</span><span style="color: rgba(0, 128, 128, 1)">重新提交事务，记录日志</span>
<span style="color: rgba(0, 0, 255, 1)">END</span>;</pre>
