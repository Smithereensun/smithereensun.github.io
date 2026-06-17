---
title: "Log4Net配置"
date: 2023-05-31
description: "简介： Log4Net是用来记录日志，可以将程序运行过程中的信息输出到一些地方(文件、数据库、EventLog等)，日志就是程序的黑匣子，可以通过日志查看系统的运行过程，从而发现系统的问题。 日志的作用：将运行过程的步骤、成功失败记录下来，将关键性的数据记录下来分析系统问题所在。 演示： 第一步：官"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11386036.html"
---

<h1>简介：</h1>
<p>　　Log4Net是用来记录日志，可以将程序运行过程中的信息输出到一些地方(文件、数据库、EventLog等)，日志就是程序的黑匣子，可以通过日志查看系统的运行过程，从而发现系统的问题。</p>
<p>　　日志的作用：将运行过程的步骤、成功失败记录下来，将关键性的数据记录下来分析系统问题所在。</p>
<h1>演示：</h1>
<h2>第一步：官网下载类库</h2>
<p>地址:http://logging.apache.org/log4net/download_log4net.cgi</p>
<p>也可以到我百度云盘下载：</p>
<p>链接：https://pan.baidu.com/s/1OOjRwz6K2_ImeTGCz9p-nQ <br>提取码：37re </p>
<h2>第二步：程序引入第三方类库</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201908/1504448-20190820200951599-390269364.png" alt="" /></p>
<h2>第三步：配置app.config</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> &lt;?xml version=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">1.0</span><span style="color: rgba(128, 0, 0, 1)">"</span> encoding=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">utf-8</span><span style="color: rgba(128, 0, 0, 1)">"</span>?&gt;
<span style="color: rgba(0, 128, 128, 1)"> 2</span> &lt;configuration&gt;
<span style="color: rgba(0, 128, 128, 1)"> 3</span>   &lt;log4net&gt;
<span style="color: rgba(0, 128, 128, 1)"> 4</span>     &lt;logger name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">logerror</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)"> 5</span>       &lt;level value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ERROR</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)"> 6</span>       &lt;appender-<span style="color: rgba(0, 0, 255, 1)">ref</span> <span style="color: rgba(0, 0, 255, 1)">ref</span>=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ErrorAppender</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)"> 7</span>     &lt;/logger&gt;
<span style="color: rgba(0, 128, 128, 1)"> 8</span>     &lt;logger name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">loginfo</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)"> 9</span>       &lt;level value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">INFO</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">10</span>       &lt;appender-<span style="color: rgba(0, 0, 255, 1)">ref</span> <span style="color: rgba(0, 0, 255, 1)">ref</span>=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">InfoAppender</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">11</span>     &lt;/logger&gt;
<span style="color: rgba(0, 128, 128, 1)">12</span>     &lt;appender name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ErrorAppender</span><span style="color: rgba(128, 0, 0, 1)">"</span> type=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">log4net.Appender.RollingFileAppender</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)">13</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">File</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Log\\LogError\\</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">14</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">AppendToFile</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">true</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">15</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">MaxSizeRollBackups</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">100</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">16</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">MaxFileSize</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">10240</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">17</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">StaticLogFileName</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">false</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">18</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">DatePattern</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">yyyyMMdd&amp;quot;.txt&amp;quot;</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">19</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">RollingStyle</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Date</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">20</span>       &lt;layout type=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">log4net.Layout.PatternLayout</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)">21</span>         &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ConversionPattern</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">%n异常时间：%d %n异常级别：%-5p%n异常内容：%m%n</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">22</span>       &lt;/layout&gt;
<span style="color: rgba(0, 128, 128, 1)">23</span>       &lt;!--&amp;lt; &amp;gt; = &lt;&gt; %n = 回车--&gt;
<span style="color: rgba(0, 128, 128, 1)">24</span>     &lt;/appender&gt;
<span style="color: rgba(0, 128, 128, 1)">25</span>     &lt;appender name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">InfoAppender</span><span style="color: rgba(128, 0, 0, 1)">"</span> type=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">log4net.Appender.RollingFileAppender</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)">26</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">File</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Log\\LogInfo\\</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">27</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">AppendToFile</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">true</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">28</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">MaxFileSize</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">10240</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">29</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">MaxSizeRollBackups</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">100</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">30</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">StaticLogFileName</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">false</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">31</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">DatePattern</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">yyyyMMdd&amp;quot;.txt&amp;quot;</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">32</span>       &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">RollingStyle</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Date</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">33</span>       &lt;layout type=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">log4net.Layout.PatternLayout</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)">34</span>         &lt;param name=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ConversionPattern</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">日志时间：%d %n日志级别：%-5p  %n日志内容：%m%n%n</span><span style="color: rgba(128, 0, 0, 1)">"</span> /&gt;
<span style="color: rgba(0, 128, 128, 1)">35</span>       &lt;/layout&gt;
<span style="color: rgba(0, 128, 128, 1)">36</span>     &lt;/appender&gt;
<span style="color: rgba(0, 128, 128, 1)">37</span>   &lt;/log4net&gt;
<span style="color: rgba(0, 128, 128, 1)">38</span> &lt;/configuration&gt;</pre>
