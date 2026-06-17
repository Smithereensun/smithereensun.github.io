---
title: "python 迭代器协议和生成器"
date: 2019-06-26
description: "一、什么是迭代器协议 1.迭代器协议是指：对象必须提供一个next方法，执行该方法要么返回迭代中的下一项，要么就引起一个stoplteration异常，以终止迭代（只能往后走，不能往前退） 2.可迭代对象：实现了迭代器协议的对象（如何实现：对象内部定义一个__iter__()方法） 3.协议是一种约"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10294814.html"
---

<p>一、什么是迭代器协议</p>
<p>　　1.迭代器协议是指：对象必须提供一个next方法，执行该方法要么返回迭代中的下一项，要么就引起一个stoplteration异常，以终止迭代（只能往后走，不能往前退）</p>
<p>　　2.可迭代对象：实现了迭代器协议的对象（如何实现：对象内部定义一个__iter__()方法）</p>
<p>　　3.协议是一种约定，可迭代对象实现了迭代器协议，python的内部工具（如for循环，sum，min，max函数等）使用迭代器协议访问对象</p>
<p>二、python中强大的for循环机制</p>
<p>for循环的本质：循环所有对象，全都是使用迭代器协议。</p>
<p><span style="color: rgba(255, 0, 0, 1)">正文清源：</span></p>
<p><span style="color: rgba(255, 0, 0, 1)">很多人会想，for循环的本质就是遵循迭代器协议去访问对象，那么for循环的对象肯定都是迭代器了啊。没错，那既然这样，for循环可以遍历（字符串，列表，元祖，字典，集合，文件对象），那这些类型的数据肯定是可迭代对象啊？但是，我tmd为什么定义一个列表=[1, 2, 3, 4]没有next方法，打脸麽？</span></p>
<p><span style="color: rgba(0, 0, 0, 1)">（字符串，列表，元祖，字典，集合，文件对象）这些都不是可迭代对象，只不过在for循环式，调用了他们内部的__iter__方法,把他们变成了可迭代对象。</span></p>
<p><span style="color: rgba(0, 0, 0, 1)">然后for循环调用可迭代对象的__next__方法取值，而且for循环会捕捉stoplteration异常，以终止迭代。</span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> ls = [<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">a</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">b</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">c</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">]
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 一、下标访问方式,默认从0开始计数</span>
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 255, 1)">print</span><span style="color: rgba(0, 0, 0, 1)">(ls[0])
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(ls[1<span style="color: rgba(0, 0, 0, 1)">])
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(ls[2<span style="color: rgba(0, 0, 0, 1)">])
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> print(ls[3]) # 报错，超出索引下标</span>
<span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> # 二、遵循迭代器协议访问方式</span>
<span style="color: rgba(0, 128, 128, 1)">10</span> diedai_ls = ls.<span style="color: rgba(128, 0, 128, 1)">__iter__</span><span style="color: rgba(0, 0, 0, 1)">()
</span><span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(diedai_ls.<span style="color: rgba(128, 0, 128, 1)">__next__</span><span style="color: rgba(0, 0, 0, 1)">())
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(diedai_ls.<span style="color: rgba(128, 0, 128, 1)">__next__</span><span style="color: rgba(0, 0, 0, 1)">())
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(diedai_ls.<span style="color: rgba(128, 0, 128, 1)">__next__</span><span style="color: rgba(0, 0, 0, 1)">())
</span><span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 三for循环访问方式</span>
<span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 255, 1)">for</span> item <span style="color: rgba(0, 0, 255, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> ls:
</span><span style="color: rgba(0, 128, 128, 1)">16</span>     <span style="color: rgba(0, 0, 255, 1)">print</span><span style="color: rgba(0, 0, 0, 1)">(item)
</span><span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 使用while循环方式</span>
<span style="color: rgba(0, 128, 128, 1)">18</span> diedai_ls = ls.<span style="color: rgba(128, 0, 128, 1)">__iter__</span><span style="color: rgba(0, 0, 0, 1)">()
</span><span style="color: rgba(0, 128, 128, 1)">19</span> <span style="color: rgba(0, 0, 255, 1)">while</span><span style="color: rgba(0, 0, 0, 1)"> True:
</span><span style="color: rgba(0, 128, 128, 1)">20</span>     <span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)">:
</span><span style="color: rgba(0, 128, 128, 1)">21</span>         <span style="color: rgba(0, 0, 255, 1)">print</span>(diedai_ls.<span style="color: rgba(128, 0, 128, 1)">__next__</span><span style="color: rgba(0, 0, 0, 1)">())
</span><span style="color: rgba(0, 128, 128, 1)">22</span>     <span style="color: rgba(0, 0, 255, 1)">except</span><span style="color: rgba(0, 0, 0, 1)"> StopIteration:
</span><span style="color: rgba(0, 128, 128, 1)">23</span>         <span style="color: rgba(0, 0, 255, 1)">print</span>(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">迭代完啦！</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 128, 1)">24</span>         <span style="color: rgba(0, 0, 255, 1)">break</span></pre>
