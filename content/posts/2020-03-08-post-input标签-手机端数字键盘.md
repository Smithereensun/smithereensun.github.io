---
title: "input标签 手机端数字键盘"
date: 2020-03-08
description: "要一点击提起数字键盘,安卓只要设置input的类型是number或tel, ios 需要 pattern=&quot;number&quot;可以直接打开搜狗输入法的数字键盘,可以输入.和数字如果只能输入数字,比如输入手机号或银行卡号,则是pattern=&quot;[0-9]*&quot; 可以调"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11040042.html"
---

<p>要一点击提起数字键盘,安卓只要设置input的类型是number或tel,</p>
<p>ios 需要&nbsp;</p>
<pre>pattern="number"<br>可以直接打开搜狗输入法的数字键盘,可以输入.和数字<br>如果只能输入数字,比如输入手机号或银行卡号,则是<br>pattern="[0-9]*"   可以调九宫格</pre>
<pre>提起数字和小数点键盘:<br>&lt;input type="number" name="cashWthdrawal" pattern="number"&gt;</pre>
<pre>提起数字键盘:<em><br></em>&lt;input type="number" name="cashWthdrawal" pattern="[0-9]*"&gt;<br><br>保证数字键盘及只有数字和小数点可以输入:<br>&lt;input type="number" pattern="number" onkeyup="value=value.replace(/[^\d\.]/g,'')"/&gt;</pre>
