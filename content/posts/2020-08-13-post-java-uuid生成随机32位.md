---
title: "Java uuid生成随机32位"
date: 2020-08-13
description: "import java.util.UUID; /** * @ClassName：UuidUtils * @Description：uuid工具类 * @Author：chenyb * @Date：2020/8/13 12:52 下午 * @Versiion：1.0 */ public class U"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13498504.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.UUID;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @ClassName：UuidUtils
 * @Description：uuid工具类
 * @Author：chenyb
 * @Date：2020/8/13 12:52 下午
 * @Versiion：1.0
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> UuidUtils {
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 生成uuid32位
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> String getUUID32(){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> UUID.randomUUID().toString().replace("-", ""<span style="color: rgba(0, 0, 0, 1)">).toLowerCase();
    }
}</span></pre>
