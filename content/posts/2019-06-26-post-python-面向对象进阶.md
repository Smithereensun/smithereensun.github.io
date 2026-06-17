---
title: "Python 面向对象进阶"
date: 2019-06-26
description: "sys模块 1 #!/usr/bin/env python 2 # -*- coding:utf-8 -*- 3 import sys 4 &#39;&#39;&#39; 5 sys.argv : 在命令行参数是一个空列表，在其他中第一个列表元素程序本身的路径 6 sys.exit(n) ：退出程序"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10403152.html"
---

<h2>&nbsp;sys模块</h2>
<div class="cnblogs_code"><img id="code_img_closed_02ab0f24-fc86-4213-a2a0-f2d799ae4ca1" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_02ab0f24-fc86-4213-a2a0-f2d799ae4ca1" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_02ab0f24-fc86-4213-a2a0-f2d799ae4ca1" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">!/usr/bin/env python</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> -*- coding:utf-8 -*-</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> sys
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(128, 0, 0, 1)">'''</span>
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(128, 0, 0, 1)">sys.argv : 在命令行参数是一个空列表，在其他中第一个列表元素程序本身的路径
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(128, 0, 0, 1)">sys.exit(n) ：退出程序，正常退出时exit(0)
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(128, 0, 0, 1)">sys.version ：获取python解释程序的版本信息
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(128, 0, 0, 1)">sys.path ：返回模块的搜索路径，初始化时使用 python PATH环境变量的值
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(128, 0, 0, 1)">sys.platform ：返回操作系统平台的名称
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(128, 0, 0, 1)">sys.stdin ：输入相关
</span><span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(128, 0, 0, 1)">sys.stdout ：输出相关
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(128, 0, 0, 1)">sys.stderror ：错误相关
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(128, 0, 0, 1)">'''</span>
<span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(sys.argv)  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> ['H:/pythons3_/2019-02-17-面向对象进阶/sys复习.py']</span>
<span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(sys.version)  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]</span>
<span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(sys.path)  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> ['H:\\pythons3_\\2019-02-17-面向对象进阶', 'H:\\pythons3_', 'D:\\Python\\insert3\\python37.zip', 'D:\\Python\\insert3\\DLLs', 'D:\\Python\\insert3\\lib', 'D:\\Python\\insert3', 'D:\\Python\\insert3\\lib\\site-packages', 'D:\\Python\\ide\\PyCharm 2018.2.4\\helpers\\pycharm_matplotlib_backend']</span>
<span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 255, 1)">print</span>(sys.platform)  <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)"> win32</span></pre>
