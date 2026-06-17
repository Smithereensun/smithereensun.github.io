---
title: "C#WinForm解决跨线程访问控件属性报错"
date: 2019-06-26
description: "方式一（在程序初始化构造函数中加一行代码）： 方式二（推荐）："
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11028115.html"
---

<p>方式一（在程序初始化构造函数中加一行代码）：</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span>         <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Form1()
</span><span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">3</span> <span style="color: rgba(0, 0, 0, 1)">            InitializeComponent();
</span><span style="color: rgba(0, 128, 128, 1)">4</span>             <span style="color: rgba(255, 0, 0, 1)"><strong>Control.CheckForIllegalCrossThreadCalls = false;</strong> </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">设置不捕获线程异常</span>
<span style="color: rgba(0, 128, 128, 1)">5</span>         }</pre>
