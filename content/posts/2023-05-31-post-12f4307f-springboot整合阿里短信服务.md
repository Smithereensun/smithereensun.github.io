---
title: "SpringBoot整合阿里短信服务"
date: 2023-05-31
description: "导读 由于最近手头上需要做个Message Gateway，涉及到：邮件(点我直达)、短信、公众号(点我直达)等推送功能，网上学习下，整理下来以备以后使用。 步骤 点我直达 登录短信服务控制台 点我直达 开通短信服务 快速学习 测试短信发送 发送短息 报一下错误信息 抱歉！发送出错了。错误码Code"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14061055.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　由于最近手头上需要做个Message Gateway，涉及到：邮件(<a href="https://www.cnblogs.com/chenyanbin/p/14042642.html" target="_blank">点我直达</a>)、短信、公众号(<a href="https://www.cnblogs.com/chenyanbin/p/14047389.html" target="_blank">点我直达</a>)等推送功能，网上学习下，整理下来以备以后使用。</p>
<h2>步骤</h2>
<p>　　<a href="https://help.aliyun.com/document_detail/108064.html?spm=a2c4g.11186623.6.556.2db321b5POCHI1" target="_blank" rel="noopener nofollow">点我直达</a></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202011/1504448-20201130093638792-294678416.png" alt="" loading="lazy" /></p>
<h3>登录短信服务控制台</h3>
<p>　　<a href="https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fdysms.console.aliyun.com%2F%3Fspm%3Da2c4g.11186623.2.17.14cd6d88xDoH2l" target="_blank" rel="noopener nofollow">点我直达</a></p>
<h3>开通短信服务</h3>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202011/1504448-20201130093826183-1401979650.png" alt="" loading="lazy" /></p>
<h3>快速学习</h3>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202011/1504448-20201130093942043-654059497.png" alt="" loading="lazy" /></p>
<h3>测试短信发送</h3>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202011/1504448-20201130094537180-93974928.png" alt="" loading="lazy" /></p>
<h3>发送短息</h3>
<p>　　报一下错误信息</p>
<div class="cnblogs_code">
<pre>抱歉！发送出错了。错误码Code：isv.AMOUNT_NOT_ENOUGH。建议前往“短信接口调用错误码”帮助文档，根据错误码查询错误原因及建议。</pre>
