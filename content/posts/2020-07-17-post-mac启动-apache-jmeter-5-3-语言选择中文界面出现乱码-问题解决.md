---
title: "mac启动 Apache JMeter 5.3 语言选择中文界面出现乱码 问题解决"
date: 2020-07-17
description: "问题重现 问题修复 出现这个问题，是因为，语言与外观不兼容导致，语言选“中文”，外观选“Metal” 细心的你，可能发现，为啥要重启2次呢？？?第一次设置完语言后，在设置外观，发现菜单不能选择，第二次重启后，才可以正常操作，估计是个bug 刚才那样只是暂时性中文显示，若想永久显示中文，请看下面 永久"
tags:
  - "压测工具"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13333930.html"
---

<h1>问题重现</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200717221536296-219956658.gif" alt="" loading="lazy" /></p>
<h1>问题修复</h1>
<p>　　出现这个问题，是因为，<span style="color: rgba(255, 0, 0, 1)"><strong>语言与外观不兼容导致</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>语言</strong></span>选“<strong><span style="color: rgba(255, 0, 0, 1)">中文</span></strong>”，<span style="color: rgba(255, 0, 0, 1)"><strong>外观</strong></span>选“<span style="color: rgba(255, 0, 0, 1)"><strong>Metal</strong></span>”</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200717223346857-586134657.gif" alt="" loading="lazy" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200717223422766-571485527.gif" alt="" loading="lazy" /></p>
<p>　　细心的你，可能发现，为啥要重启2次呢？？?第一次设置完语言后，在设置外观，发现菜单不能选择，第二次重启后，才可以正常操作，估计是个bug</p>
<p>　　刚才那样只是暂时性中文显示，若想永久显示中文，请看下面</p>
<h1>永久性中文显示</h1>
<p>位置：apache-jmeter-5.3/bin/jmeter.properties</p>
<p><strong><span style="color: rgba(255, 0, 0, 1)">修改第39行，设置为language=zh_CN</span></strong></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200717224045773-554000084.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>修改1085行，设置为sampleresult.default.encoding=UTF-8</strong></span></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200717224445123-424663840.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>　　对你有小小帮助的话，记得点个推荐哟，不要白嫖哟～～～</p>
