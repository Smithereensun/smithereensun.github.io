---
title: "Java int/int 保留2位小数"
date: 2020-08-24
description: "@Test public void txfloat() { // TODO 自动生成的方法存根 int a=9; int b=7; DecimalFormat df=new DecimalFormat(&quot;0.00&quot;); System.out.println(df.format(("
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13555015.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">@Test
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> txfloat() {
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> TODO 自动生成的方法存根</span>
    <span style="color: rgba(0, 0, 255, 1)">int</span> a=9<span style="color: rgba(0, 0, 0, 1)">;
    </span><span style="color: rgba(0, 0, 255, 1)">int</span> b=7<span style="color: rgba(0, 0, 0, 1)">;
    DecimalFormat df</span>=<span style="color: rgba(0, 0, 255, 1)">new</span> DecimalFormat("0.00"<span style="color: rgba(0, 0, 0, 1)">);

    System.out.println(df.format((</span><span style="color: rgba(0, 0, 255, 1)">float</span>)a/<span style="color: rgba(0, 0, 0, 1)">b));
    System.out.println(df.format(a</span>/(<span style="color: rgba(0, 0, 255, 1)">float</span><span style="color: rgba(0, 0, 0, 1)">)b));
    System.out.println(df.format((</span><span style="color: rgba(0, 0, 255, 1)">float</span>)a/(<span style="color: rgba(0, 0, 255, 1)">float</span><span style="color: rgba(0, 0, 0, 1)">)b));
    System.out.println(df.format((</span><span style="color: rgba(0, 0, 255, 1)">float</span>)(a/<span style="color: rgba(0, 0, 0, 1)">b)));
}</span></pre>
