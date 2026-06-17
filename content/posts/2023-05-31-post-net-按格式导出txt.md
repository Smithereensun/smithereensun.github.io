---
title: ".NET 按格式导出txt"
date: 2023-05-31
description: "效果图 后台代码 private void DownTxt() { try { StringBuilder sb = new StringBuilder(); for (int i = 0; i &lt; 50000; i++) { sb.Append(&quot;测试i=&quot; + i+&q"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12581490.html"
---

<h1>效果图</h1>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200327145453549-1279580623.png" alt="" /></p>
<p>&nbsp;</p>
<h1>后台代码</h1>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> DownTxt()
        {
            </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)">
            {
                StringBuilder sb </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> StringBuilder();
                </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = <span style="color: rgba(128, 0, 128, 1)">0</span>; i &lt; <span style="color: rgba(128, 0, 128, 1)">50000</span>; i++<span style="color: rgba(0, 0, 0, 1)">)
                {
                    sb.Append(</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">测试i=</span><span style="color: rgba(128, 0, 0, 1)">"</span> + i+<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">\r\n</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
                }
                Response.Clear();
                Response.Headers[</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Content-Disposition</span><span style="color: rgba(128, 0, 0, 1)">"</span>] = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">attachment;filename=aaa.txt</span><span style="color: rgba(128, 0, 0, 1)">"</span>;<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">输出文件格式</span>
                Response.ContentEncoding = System.Text.Encoding.GetEncoding(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">UTF-8</span><span style="color: rgba(128, 0, 0, 1)">"</span>); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">解决乱码问题</span>
<span style="color: rgba(0, 0, 0, 1)">                Response.Write(sb.ToString());
            }
            </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception EX)
            {
                </span><span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> EX;
            }
        }</span></pre>
