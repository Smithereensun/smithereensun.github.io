---
title: "Maven设置华为代理"
date: 2021-01-22
description: "只需要将maven的配置文件settings.xml修改如下即可 &lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt; &lt;settings xmlns=&quot;http://maven.apache.org/SET"
tags:
  - "Maven"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14315616.html"
---

<p>　　只需要将maven的配置文件settings.xml修改如下即可</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;?</span><span style="color: rgba(255, 0, 255, 1)">xml version="1.0" encoding="UTF-8"</span><span style="color: rgba(0, 0, 255, 1)">?&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">settings
    </span><span style="color: rgba(255, 0, 0, 1)">xmlns</span><span style="color: rgba(0, 0, 255, 1)">="http://maven.apache.org/SETTINGS/1.0.0"</span><span style="color: rgba(255, 0, 0, 1)">
    xmlns:xsi</span><span style="color: rgba(0, 0, 255, 1)">="http://www.w3.org/2001/XMLSchema-instance"</span><span style="color: rgba(255, 0, 0, 1)">
          xsi:schemaLocation</span><span style="color: rgba(0, 0, 255, 1)">="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">pluginGroups</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">pluginGroups</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">proxies</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">proxies</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">servers</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">servers</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">mirrors</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">maven代理开始</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">mirror</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>huaweicloud<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">mirrorOf</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>*<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">mirrorOf</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">url</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>https://repo.huaweicloud.com/repository/maven/<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">url</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">mirror</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">maven代理结束</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">mirrors</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">profiles</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">profiles</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">settings</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
