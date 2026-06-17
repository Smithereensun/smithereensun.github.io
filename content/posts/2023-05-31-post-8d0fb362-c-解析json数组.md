---
title: "C#解析JSON数组"
date: 2023-05-31
description: "方式一 第一步:使用前，需下载:Newtonsoft.Json.dll 没有的，请到我百度云盘下载 链接：https://pan.baidu.com/s/1JBkee4qhtW7XOyYFiGOL2Q&#160;提取码：b5uq 第二步：引入命名空间：using Newtonsoft.Json; 第"
tags:
  - "JSON"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11200415.html"
---

<h1><span style="font-family: 幼圆; color: rgba(255, 0, 0, 1)">方式一</span></h1>
<h2><span style="font-family: 幼圆">第一步:使用前，需下载:Newtonsoft.Json.dll</span></h2>
<p>没有的，请到我百度云盘下载</p>
<p>链接：https://pan.baidu.com/s/1JBkee4qhtW7XOyYFiGOL2Q&nbsp;<br>提取码：b5uq</p>
<h2>第二步：引入命名空间：using Newtonsoft.Json;</h2>
<h2>第三步：封装一个函数，方便以后使用</h2>
<p>待解析JSON数组</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190717131529930-1212210582.png" alt="" /></p>
<p>函数：</p>
<div class="cnblogs_code">
<pre> <span style="color: rgba(0, 0, 0, 1)">        public static Newtonsoft.Json.Linq.JArray GetToJsonList(string json)
</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span> <span style="color: rgba(0, 0, 0, 1)">            Newtonsoft.Json.Linq.JArray jsonArr = (Newtonsoft.Json.Linq.JArray)JsonConvert.DeserializeObject(json);
</span> <span style="color: rgba(0, 0, 0, 1)">            return jsonArr;
</span>         }</pre>
