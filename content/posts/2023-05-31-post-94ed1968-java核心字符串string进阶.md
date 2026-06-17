---
title: "Java核心字符串String进阶"
date: 2023-05-31
description: "字符串对象 字符串是对象，不是简单数据类型 封装在java.lang包，自动导入 创建字符串对象 常见创建一个字符串对象有下面2个方法 String str=new String(&quot;chenyanbin&quot;); String str=&quot;chenyanbin&quot;;"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13417375.html"
---

<h1 style="text-align: center">字符串对象</h1>
<ul>
<li>字符串是对象，不是简单数据类型</li>
<li>封装在java.lang包，自动导入</li>
</ul>
<h1 style="text-align: center">创建字符串对象</h1>
<ul>
<li>常见创建一个字符串对象有下面2个方法
<ul>
<li>String str=new String("chenyanbin");</li>
<li>String str="chenyanbin";</li>
</ul>
</li>
</ul>
<h1 style="text-align: center">字符串比较内容是否相等</h1>
<ul>
<li>==：比较地址</li>
<li>内容是否相等需要用equals()方法比较</li>
</ul>
<p>常见API</p>
<div class="cnblogs_code">
<pre> String str = "https://www.cnblogs.com/chenyanbin/"
 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">获取字符串⻓度:</span>
<span style="color: rgba(0, 0, 0, 1)"> str.length();
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">通过下标获取字符：</span>
 <span style="color: rgba(0, 0, 255, 1)">char</span> <span style="color: rgba(0, 0, 255, 1)">ch</span> = str.charAt(5<span style="color: rgba(0, 0, 0, 1)">);
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">字符串⽐较：</span>
 <span style="color: rgba(0, 0, 255, 1)">boolean</span> result =<span style="color: rgba(0, 0, 0, 1)"> str1.equals(str2);
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">字符串⽐较忽略⼤⼩写</span>
 <span style="color: rgba(0, 0, 255, 1)">boolean</span> result =<span style="color: rgba(0, 0, 0, 1)"> str1.equalsIgnoreCase(str2);
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">查找字符串出现的位置</span>
 <span style="color: rgba(0, 0, 255, 1)">int</span> index = str.indexOf("."<span style="color: rgba(0, 0, 0, 1)">);
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">字符串截取</span>
String result1 =<span style="color: rgba(0, 0, 0, 1)"> str.substring(index)；
String result2 </span>=<span style="color: rgba(0, 0, 0, 1)"> str.substring(index1, index2)；
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">字符串拆分 ,注意正则，可以先简单知道</span>
 String [] arr = str.split("\\."<span style="color: rgba(0, 0, 0, 1)">);
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">字符串替换</span>
 str.replace("x","a"<span style="color: rgba(0, 0, 0, 1)">);
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">字符串⼤⼩写转换</span>
<span style="color: rgba(0, 0, 0, 1)">str.toUpperCase();
str.toLowerCase();
 </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">字符串去除空格</span>
 str1.trim();</pre>
