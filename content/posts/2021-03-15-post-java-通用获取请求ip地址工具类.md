---
title: "Java 通用获取请求ip地址工具类"
date: 2021-03-15
description: "package com.ybchen.utils; import javax.servlet.http.HttpServletRequest; import java.net.InetAddress; import java.net.UnknownHostException; /** * @Desc"
tags:
  - "JavaSE"
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14537448.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.ybchen.utils;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletRequest;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.net.InetAddress;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.net.UnknownHostException;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @Description：ip地址工具类
 * @Author：chenyanbin
 * @Date：2021/3/13 下午4:14
 * @Versiion：1.0
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> IpUtils {
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 获取ip地址
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> request
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> String getIpAddr(HttpServletRequest request) {
        String ipAddress </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
        </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
            ipAddress </span>= request.getHeader("x-forwarded-for"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 0, 255, 1)">if</span> (ipAddress == <span style="color: rgba(0, 0, 255, 1)">null</span> || ipAddress.length() == 0 || "unknown"<span style="color: rgba(0, 0, 0, 1)">.equalsIgnoreCase(ipAddress)) {
                ipAddress </span>= request.getHeader("Proxy-Client-IP"<span style="color: rgba(0, 0, 0, 1)">);
            }
            </span><span style="color: rgba(0, 0, 255, 1)">if</span> (ipAddress == <span style="color: rgba(0, 0, 255, 1)">null</span> || ipAddress.length() == 0 || "unknown"<span style="color: rgba(0, 0, 0, 1)">.equalsIgnoreCase(ipAddress)) {
                ipAddress </span>= request.getHeader("WL-Proxy-Client-IP"<span style="color: rgba(0, 0, 0, 1)">);
            }
            </span><span style="color: rgba(0, 0, 255, 1)">if</span> (ipAddress == <span style="color: rgba(0, 0, 255, 1)">null</span> || ipAddress.length() == 0 || "unknown"<span style="color: rgba(0, 0, 0, 1)">.equalsIgnoreCase(ipAddress)) {
                ipAddress </span>=<span style="color: rgba(0, 0, 0, 1)"> request.getRemoteAddr();
                </span><span style="color: rgba(0, 0, 255, 1)">if</span> (ipAddress.equals("127.0.0.1"<span style="color: rgba(0, 0, 0, 1)">)) {
                    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 根据网卡取本机配置的IP</span>
                    InetAddress inet = <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
                    </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
                        inet </span>=<span style="color: rgba(0, 0, 0, 1)"> InetAddress.getLocalHost();
                    } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (UnknownHostException e) {
                        e.printStackTrace();
                    }
                    ipAddress </span>=<span style="color: rgba(0, 0, 0, 1)"> inet.getHostAddress();
                }
            }
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 对于通过多个代理的情况，第一个IP为客户端真实IP,多个IP按照','分割</span>
            <span style="color: rgba(0, 0, 255, 1)">if</span> (ipAddress != <span style="color: rgba(0, 0, 255, 1)">null</span> &amp;&amp; ipAddress.length() &gt; 15) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> "***.***.***.***".length()
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> = 15</span>
                <span style="color: rgba(0, 0, 255, 1)">if</span> (ipAddress.indexOf(",") &gt; 0<span style="color: rgba(0, 0, 0, 1)">) {
                    ipAddress </span>= ipAddress.substring(0, ipAddress.indexOf(","<span style="color: rgba(0, 0, 0, 1)">));
                }
            }
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception e) {
            ipAddress </span>= ""<span style="color: rgba(0, 0, 0, 1)">;
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> ipAddress;
    }
}</span></pre>
