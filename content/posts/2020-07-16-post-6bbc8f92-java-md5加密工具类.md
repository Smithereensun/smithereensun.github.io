---
title: "java MD5加密工具类"
date: 2020-07-16
description: "/** * MD5加密工具类 * @param data * @return */ public static String MD5(String data) { try { java.security.MessageDigest md = java.security.MessageDigest.g"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13323672.html"
---

<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * MD5加密工具类
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> data
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> String MD5(String data) {
        </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
            java.security.MessageDigest md </span>= java.security.MessageDigest.getInstance("MD5"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 0, 255, 1)">byte</span>[] array = md.digest(data.getBytes("UTF-8"<span style="color: rgba(0, 0, 0, 1)">));
            StringBuilder sb </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> StringBuilder();
            </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">byte</span><span style="color: rgba(0, 0, 0, 1)"> bt : array) {
                sb.append(Integer.toHexString((bt </span>&amp; 0xFF) | 0x100).substring(1, 3<span style="color: rgba(0, 0, 0, 1)">));
            }
            </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> sb.toString().toUpperCase();
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex) {
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
    }</span></pre>
