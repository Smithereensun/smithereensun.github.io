---
title: "WebService 接收JSON字符串"
date: 2023-05-31
description: "晚上学习时公司的同事，暂且叫A吧，A：“我们公司XXX纺织的AM接口不通，让我看下”，我：“接口写的不是有AJAX异步请求的示例嘛，参考下，我都测试过接口，都是通的。”，A：“我走的不是AJAX，走的CS端”，我：“哦，明白了，CS端的HttpWebRequest模拟前端的AJAX请求，我之前写过一"
tags:
  - "WebService"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11312704.html"
---

<p><span style="font-family: &quot;Microsoft YaHei&quot;">　　晚上学习时公司的同事，暂且叫A吧，A：“我们公司XXX纺织的AM接口不通，让我看下”，我：“接口写的不是有AJAX异步请求的示例嘛，参考下，我都测试过接口，都是通的。”，A：“我走的不是AJAX，走的CS端”，我：“哦，明白了，CS端的HttpWebRequest模拟前端的AJAX请求，我之前写过一次，我写个DEMO调试看看”</span></p>
<h1><span style="font-family: &quot;Microsoft YaHei&quot;">排查结果如下</span></h1>
<h2><strong><span style="color: rgba(255, 0, 255, 1)">错误示例，因为CS没法前面加前缀：jsonData</span></strong></h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190807000950900-344425566.png" alt="" /></p>
<h2><span style="color: rgba(255, 0, 255, 1)"><strong>正确的AJAX示例，前面有jsonData(因为后台获取的是jsonData中的数据，CS端这个没法传)</strong></span></h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190807000913015-346379947.png" alt="" /></p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190807001413329-1347695382.png" alt="" /></p>
<h2><strong><span style="font-family: &quot;Microsoft YaHei&quot;">网上找了半天解决方法，我们可以使用上下文，获取JSON数据流，然后在将流还原回JSON字符串即可</span></strong></h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span>             Stream s = HttpContext.Current.Request.InputStream;<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">获得json 字符流
</span><span style="color: rgba(0, 128, 128, 1)">2</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">还原数据流</span>
<span style="color: rgba(0, 128, 128, 1)">3</span>             <span style="color: rgba(0, 0, 255, 1)">byte</span>[] b = <span style="color: rgba(0, 0, 255, 1)">new</span> <span style="color: rgba(0, 0, 255, 1)">byte</span><span style="color: rgba(0, 0, 0, 1)">[s.Length];
</span><span style="color: rgba(0, 128, 128, 1)">4</span>             s.Read(b, <span style="color: rgba(128, 0, 128, 1)">0</span>, (<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)">)s.Length);
</span><span style="color: rgba(0, 128, 128, 1)">5</span>             <span style="color: rgba(0, 0, 255, 1)">string</span> jsontext = Encoding.UTF8.GetString(b); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">JSON字符串</span></pre>
