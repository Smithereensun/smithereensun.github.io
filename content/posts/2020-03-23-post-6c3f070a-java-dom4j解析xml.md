---
title: "java dom4j解析xml"
date: 2020-03-23
description: "jar包下载 官网地址：点我直达 将jar包导入工程 package com.cyb; import java.io.InputStream; import java.security.MessageDigest; import java.security.NoSuchAlgorithmExcept"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12555050.html"
---

<h1 style="text-align: center">jar包下载</h1>
<p>官网地址：<a href="https://dom4j.github.io/#" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202003/1504448-20200323204818950-1812780110.gif" alt="" /></p>
<h2>将jar包导入工程</h2>
<p><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200323205001744-1383141432.png" alt="" /></p>
<p>&nbsp;</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.InputStream;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.security.MessageDigest;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.security.NoSuchAlgorithmException;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.Arrays;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.HashMap;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.List;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.Map;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.dom4j.Document;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.dom4j.DocumentException;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.dom4j.Element;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.dom4j.io.SAXReader;


</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> WxService {

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 解析XML数据包
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> is InputStream输入流
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> Map&lt;String, String&gt;<span style="color: rgba(0, 0, 0, 1)"> parseRequest(InputStream is){
        Map</span>&lt;String, String&gt; map=<span style="color: rgba(0, 0, 255, 1)">new</span> HashMap&lt;String, String&gt;<span style="color: rgba(0, 0, 0, 1)">();
        SAXReader reader</span>=<span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> SAXReader();
        
        </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">读取输入流，获取文档对象</span>
            Document document=<span style="color: rgba(0, 0, 0, 1)">reader.read(is);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">根据文档对象获取根节点</span>
            Element root=<span style="color: rgba(0, 0, 0, 1)">document.getRootElement();
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">获取根节点的所有子节点</span>
            List&lt;Element&gt; elements=<span style="color: rgba(0, 0, 0, 1)">root.elements();
            </span><span style="color: rgba(0, 0, 255, 1)">for</span><span style="color: rgba(0, 0, 0, 1)"> (Element e:elements) {
                map.put(e.getName(), e.getStringValue());
            }
            
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (DocumentException e) {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> TODO Auto-generated catch block</span>
<span style="color: rgba(0, 0, 0, 1)">            e.printStackTrace();
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> map;
    }
}</span></pre>
