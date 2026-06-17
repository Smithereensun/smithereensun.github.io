---
title: "WebUi爬虫自动化测试 Selenium4.X+Java教程"
date: 2024-07-08
description: "为什么要学习Selenium 自动化测试 Selenium是最受欢迎的Web应用程序自动化测试工具之一。 通过学习Selenium，可以编写自动化测试脚本，用于自动执行各种任务，例如验证功能、测试用户界面、模拟用户交互 大大提高测试效率，减少手动测试的工作量。 网络爬虫 Selenium可以用于构建"
tags:
  - "Selenium4.X"
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/18288029/selenium"
---

<h1 style="text-align: center">为什么要学习Selenium</h1>
<ul>
<li>
<p>自动化测试</p>
<ul>
<li>
<p>Selenium是最受欢迎的Web应用程序自动化测试工具之一。</p>
</li>
<li>
<p>通过学习Selenium，可以编写自动化测试脚本，用于自动执行各种任务，例如验证功能、测试用户界面、模拟用户交互</p>
</li>
<li>
<p>大大提高测试效率，减少手动测试的工作量。</p>
</li>
</ul>
</li>
<li>
<p>网络爬虫</p>
<ul>
<li>
<p>Selenium可以用于构建网络爬虫，从网页上提取数据。通过模拟用户的交互行为，如点击按钮、填写表单等</p>
</li>
<li>
<p>Selenium能够获取页面上动态生成的内容，而且可以处理JavaScript渲染的网页。</p>
</li>
<li>
<p>这对于需要爬取动态内容的网站很有帮助。</p>
</li>
</ul>
</li>
<li>
<p>自动化操作</p>
<ul>
<li>
<p>Selenium可以用于自动化各种Web应用程序的操作，例如批量提交表单、自动化下载文件、自动化填写信息等。</p>
</li>
<li>
<p>可以减少重复性的任务，并提高工作效率。</p>
</li>
</ul>
</li>
</ul>
<ul>
<li>
<p>官网：<a class="url" href="https://www.selenium.dev/" target="_blank" rel="noopener nofollow">https://www.selenium.dev</a></p>
</li>
</ul>
<h1 style="text-align: center">环境安装</h1>
<h2>谷歌浏览器版本</h2>
<p><img src="https://img2024.cnblogs.com/blog/1504448/202407/1504448-20240707195527426-1891433004.png" alt="" loading="lazy" /></p>
<h2>安装驱动</h2>
<p>　　注意：大版本号要保持一致，否则可能出现兼容性问题（若找不到响应版本，降浏览器版本号）&nbsp;</p>
<ul>
<li>
<p><a class="url" href="https://registry.npmmirror.com/binary.html?path=chromedriver" target="_blank" rel="noopener nofollow">https://registry.npmmirror.com/binary.html?path=chromedriver</a></p>
</li>
<li>
<p><a class="url" href="https://googlechromelabs.github.io/chrome-for-testing/#stable" target="_blank" rel="noopener nofollow">https://googlechromelabs.github.io/chrome-for-testing/#stable</a></p>
</li>
</ul>
<h2>下载驱动</h2>
<p><img src="https://img2024.cnblogs.com/blog/1504448/202407/1504448-20240707200938125-46187295.png" alt="" loading="lazy" /></p>
<h2>创建java工程</h2>
<p><img src="https://img2024.cnblogs.com/blog/1504448/202407/1504448-20240707201827554-1816822973.gif" alt="" /></p>
<div class="cnblogs_code">
<pre>        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> Selenium </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.seleniumhq.selenium<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>selenium-java<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>4.10.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
