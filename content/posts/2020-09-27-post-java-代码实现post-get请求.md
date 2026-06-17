---
title: "Java 代码实现POST/GET请求"
date: 2020-09-27
description: "方式一 package com.cyb.util; import java.io.BufferedReader; import java.io.DataOutputStream; import java.io.IOException; import java.io.InputStream; impo"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12582294.html"
---

<h1 style="text-align: center">方式一</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.cyb.util;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.BufferedReader;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.DataOutputStream;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.IOException;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.InputStream;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.InputStreamReader;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.UnsupportedEncodingException;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.net.HttpURLConnection;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.net.URL;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.net.URLEncoder;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.HashMap;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.Map;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Util {
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">final</span> String DEF_CHATSET = "UTF-8"<span style="color: rgba(0, 0, 0, 1)">;
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">final</span> <span style="color: rgba(0, 0, 255, 1)">int</span> DEF_CONN_TIMEOUT = 30000<span style="color: rgba(0, 0, 0, 1)">;
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">final</span> <span style="color: rgba(0, 0, 255, 1)">int</span> DEF_READ_TIMEOUT = 30000<span style="color: rgba(0, 0, 0, 1)">;
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> String userAgent =  "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36"<span style="color: rgba(0, 0, 0, 1)">;
 
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">配置您申请的KEY</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">final</span> String APPKEY ="*************************"<span style="color: rgba(0, 0, 0, 1)">;
    
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
    *
    * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> strUrl 请求地址
    * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> params 请求参数
    * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> method 请求方法
    * </span><span style="color: rgba(128, 128, 128, 1)">@return</span><span style="color: rgba(0, 128, 0, 1)">  网络请求字符串
    * </span><span style="color: rgba(128, 128, 128, 1)">@throws</span><span style="color: rgba(0, 128, 0, 1)"> Exception
    </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
   <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> String net(String strUrl, Map params,String method) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {
       HttpURLConnection conn </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
       BufferedReader reader </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
       String rs </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
       </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
           StringBuffer sb </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> StringBuffer();
           </span><span style="color: rgba(0, 0, 255, 1)">if</span>(method==<span style="color: rgba(0, 0, 255, 1)">null</span> || method.equals("GET"<span style="color: rgba(0, 0, 0, 1)">)){
               strUrl </span>= strUrl+"?"+<span style="color: rgba(0, 0, 0, 1)">urlencode(params);
           }
           URL url </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> URL(strUrl);
           conn </span>=<span style="color: rgba(0, 0, 0, 1)"> (HttpURLConnection) url.openConnection();
           </span><span style="color: rgba(0, 0, 255, 1)">if</span>(method==<span style="color: rgba(0, 0, 255, 1)">null</span> || method.equals("GET"<span style="color: rgba(0, 0, 0, 1)">)){
               conn.setRequestMethod(</span>"GET"<span style="color: rgba(0, 0, 0, 1)">);
           }</span><span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)">{
               conn.setRequestMethod(</span>"POST"<span style="color: rgba(0, 0, 0, 1)">);
               conn.setDoOutput(</span><span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">);
           }
           conn.setRequestProperty(</span>"User-agent"<span style="color: rgba(0, 0, 0, 1)">, userAgent);
           conn.setUseCaches(</span><span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">);
           conn.setConnectTimeout(DEF_CONN_TIMEOUT);
           conn.setReadTimeout(DEF_READ_TIMEOUT);
           conn.setInstanceFollowRedirects(</span><span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">);
           conn.connect();
           </span><span style="color: rgba(0, 0, 255, 1)">if</span> (params!= <span style="color: rgba(0, 0, 255, 1)">null</span> &amp;&amp; method.equals("POST"<span style="color: rgba(0, 0, 0, 1)">)) {
               </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
                   DataOutputStream out </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> DataOutputStream(conn.getOutputStream());
                       out.writeBytes(urlencode(params));
               } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception e) {
                   </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> TODO: handle exception</span>
<span style="color: rgba(0, 0, 0, 1)">               }
           }
           InputStream is </span>=<span style="color: rgba(0, 0, 0, 1)"> conn.getInputStream();
           reader </span>= <span style="color: rgba(0, 0, 255, 1)">new</span> BufferedReader(<span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> InputStreamReader(is, DEF_CHATSET));
           String strRead </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
           </span><span style="color: rgba(0, 0, 255, 1)">while</span> ((strRead = reader.readLine()) != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
               sb.append(strRead);
           }
           rs </span>=<span style="color: rgba(0, 0, 0, 1)"> sb.toString();
       } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (IOException e) {
           e.printStackTrace();
       } </span><span style="color: rgba(0, 0, 255, 1)">finally</span><span style="color: rgba(0, 0, 0, 1)"> {
           </span><span style="color: rgba(0, 0, 255, 1)">if</span> (reader != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
               reader.close();
           }
           </span><span style="color: rgba(0, 0, 255, 1)">if</span> (conn != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
               conn.disconnect();
           }
       }
       </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> rs;
   }

   </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">将map型转为请求参数型</span>
   <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> String urlencode(Map&lt;String,Object&gt;<span style="color: rgba(0, 0, 0, 1)">data) {
       StringBuilder sb </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> StringBuilder();
       </span><span style="color: rgba(0, 0, 255, 1)">for</span><span style="color: rgba(0, 0, 0, 1)"> (Map.Entry i : data.entrySet()) {
           </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
               sb.append(i.getKey()).append(</span>"=").append(URLEncoder.encode(i.getValue()+"","UTF-8")).append("&amp;"<span style="color: rgba(0, 0, 0, 1)">);
           } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (UnsupportedEncodingException e) {
               e.printStackTrace();
           }
       }
       </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> sb.toString();
   }
}</span></pre>
