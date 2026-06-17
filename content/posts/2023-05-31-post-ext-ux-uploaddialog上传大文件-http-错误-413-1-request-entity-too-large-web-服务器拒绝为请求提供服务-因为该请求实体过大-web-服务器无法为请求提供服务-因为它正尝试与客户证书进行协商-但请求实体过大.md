---
title: "Ext.ux.UploadDialog上传大文件 HTTP 错误 413.1 - Request Entity Too Large Web 服务器拒绝为请求提供服务，因为该请求实体过大。Web 服务器无法为请求提供服务，因为它正尝试与客户证书进行协商，但请求实体过大。"
date: 2023-05-31
description: "问题描述 问题：HTTP 错误 404.13 - Not Found 请求筛选模块被配置为拒绝超过请求内容长度的请求。 原因：Web 服务器上的请求筛选被配置为拒绝该请求，因为内容长度超过配置的值（IIS 7 默认文件上传大小时30M）。 解决方法 web.config中，添加如下内容 &lt;sy"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11896093.html"
---

<h1 style="text-align: center">问题描述</h1>
<p>问题：HTTP 错误 404.13 - Not Found 请求筛选模块被配置为拒绝超过请求内容长度的请求。</p>
<p>原因：Web 服务器上的请求筛选被配置为拒绝该请求，因为内容长度超过配置的值（IIS 7 默认文件上传大小时30M）。</p>
<h1 style="text-align: center">解决方法</h1>
<h2>web.config中，添加如下内容</h2>
<div class="cnblogs_code">
<pre>  <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">system.webServer</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">security</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
      <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">requestFiltering</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">requestLimits </span><span style="color: rgba(255, 0, 0, 1)">maxQueryString</span><span style="color: rgba(0, 0, 255, 1)">="102400"</span><span style="color: rgba(255, 0, 0, 1)"> maxAllowedContentLength</span><span style="color: rgba(0, 0, 255, 1)">="102400000"</span><span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
      <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">requestFiltering</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">security</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
  <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">system.webServer</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
