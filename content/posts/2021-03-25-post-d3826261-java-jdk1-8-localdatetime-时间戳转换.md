---
title: "Java jdk1.8 LocalDateTime 时间戳转换"
date: 2021-03-25
description: "LocalDateTime和时间戳互转 /** * 获取到毫秒级时间戳 * @param localDateTime 具体时间 * @return long 毫秒级时间戳 */ public static long toEpochMilli(LocalDateTime localDateTime){"
tags:
  - "JDK8~13"
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14569500.html"
---

<h1 style="text-align: center">LocalDateTime和时间戳互转</h1>
<div class="cnblogs_code">
<pre>  <span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 获取到毫秒级时间戳
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> localDateTime 具体时间
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span><span style="color: rgba(0, 128, 0, 1)"> long 毫秒级时间戳
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">long</span><span style="color: rgba(0, 0, 0, 1)"> toEpochMilli(LocalDateTime localDateTime){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> localDateTime.toInstant(ZoneOffset.of("+8"<span style="color: rgba(0, 0, 0, 1)">)).toEpochMilli();
    }

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 毫秒级时间戳转 LocalDateTime
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> epochMilli 毫秒级时间戳
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span><span style="color: rgba(0, 128, 0, 1)"> LocalDateTime
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> LocalDateTime ofEpochMilli(<span style="color: rgba(0, 0, 255, 1)">long</span><span style="color: rgba(0, 0, 0, 1)"> epochMilli){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> LocalDateTime.ofInstant(Instant.ofEpochMilli(epochMilli), ZoneOffset.of("+8"<span style="color: rgba(0, 0, 0, 1)">));
    }

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 获取到秒级时间戳
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> localDateTime 具体时间
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span><span style="color: rgba(0, 128, 0, 1)"> long 秒级时间戳
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">long</span><span style="color: rgba(0, 0, 0, 1)"> toEpochSecond(LocalDateTime localDateTime){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> localDateTime.toEpochSecond(ZoneOffset.of("+8"<span style="color: rgba(0, 0, 0, 1)">));
    }

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 秒级时间戳转 LocalDateTime
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> epochSecond 秒级时间戳
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span><span style="color: rgba(0, 128, 0, 1)"> LocalDateTime
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> LocalDateTime ofEpochSecond(<span style="color: rgba(0, 0, 255, 1)">long</span><span style="color: rgba(0, 0, 0, 1)"> epochSecond){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> LocalDateTime.ofEpochSecond(epochSecond, 0,ZoneOffset.of("+8"<span style="color: rgba(0, 0, 0, 1)">));
    }</span></pre>
