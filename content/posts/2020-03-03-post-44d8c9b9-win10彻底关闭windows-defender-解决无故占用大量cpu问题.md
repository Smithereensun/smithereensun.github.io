---
title: "win10彻底关闭windows defender，解决无故占用大量CPU问题"
date: 2020-03-03
description: "win10彻底关闭defender的方法 首先右键开始菜单按钮，点击“运行”，输入“gpedit.msc”，打开“本地组策略编辑器”。 依次选择“计算机配置”-“管理模板”-“Windows组件”-“Windows Defender防病毒程序”。 找到“关闭Windows Defender防病毒程序"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12402905.html"
---

<h1 style="text-align: center">win10彻底关闭defender的方法</h1>
<ol>
<li><span class="bjh-p">首先右键开始菜单按钮，点击“<span class="bjh-strong">运行”，输入“<span class="bjh-strong">gpedit.msc”，打开“<span class="bjh-strong">本地组策略编辑器”。</span></span></span></span></li>
<li><span class="bjh-p">依次选择<span class="bjh-strong">“计算机配置”-“管理模板”-“Windows组件”-“Windows Defender防病毒程序”。</span></span></li>
<li><span class="bjh-p"><span class="bjh-strong">找到“<span class="bjh-strong">关闭Windows Defender防病毒程序”选项，右键“<span class="bjh-strong">编辑“，选择“<span class="bjh-strong">已启用”，确定即可。</span></span></span></span></span></li>
</ol>
<p><span class="bjh-p"><span class="bjh-strong"><img src="https://img2020.cnblogs.com/i-beta/1504448/202003/1504448-20200303161127777-1882757885.png" alt="" /></span></span></p>
<p>&nbsp;</p>
<p><span class="bjh-p">　　如此一来，Windows Defender的扫描查杀功能就彻底关闭了，不过防火墙和浏览器保护等功能还是开着的。这时候，你再打开任务管理，看看“Antimalware Service Executable”这个一直占用大量cpu的进程是不是消失了呢。</span></p>
<p><span class="bjh-p">好了，笔记本风扇终于不会无故呼呼呼地吹了，整个世界也终于安静了。如果你也受此问题困扰，就赶紧试试此方法吧。</span></p>
