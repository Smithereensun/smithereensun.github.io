---
title: "Microsoft Compatibility telemetry占cpu资源高"
date: 2023-05-31
description: "1、在Windows10系统卡的时候，打开任务管理器，发现Microsoft Compatibility telemetry占用了大量的系统资源，特别是CPU占用率非常高。 位置：控制面板-&gt;管理工具-&gt;任务计划程序 2、右键点开【这台电脑】，点【管理】，点【服务和应用程序】点【服务】，"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12365879.html"
---

<p>1、在Windows10系统卡的时候，打开任务管理器，发现Microsoft Compatibility telemetry占用了大量的系统资源，特别是CPU占用率非常高。</p>
<p>位置：控制面板-&gt;管理工具-&gt;任务计划程序</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202002/1504448-20200226112431679-1340990014.png" alt="" /></p>
<p>&nbsp;</p>
<p>2、右键点开【这台电脑】，点【管理】，点【服务和应用程序】点【服务】，在右边框里把【superfetch】</p>
<p>位置：运行-&gt;regedit</p>
<p>【windows search】<br>【HomeGroupListener】</p>
<p>【HomeGroupProvider】的启动类型设置成【禁用】</p>
<p>3、通过注册表定位并修改了HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\UnistoreSvc等类似项的start值为4，unistack服务就没开机运行啦啦啦，空闲时的硬盘占用下来了……</p>
