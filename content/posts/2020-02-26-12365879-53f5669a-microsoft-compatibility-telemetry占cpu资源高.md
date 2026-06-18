{

  "title": "Microsoft Compatibility telemetry占cpu资源高",
  "date": "2020-02-26",
  "description": "、在Windows10系统卡的时候，打开任务管理器，发现Microsoft Compatibility telemetry占用了大量的系统资源，特别是CPU占用率非常高。 位置：控制面板->管理工具->任务计划程序 、右键点开【这台电脑】，点【管理】，点【服务和应用程序】点【服务】，在右边框里把【s",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12365879.html"

}

1、在Windows10系统卡的时候，打开任务管理器，发现Microsoft Compatibility telemetry占用了大量的系统资源，特别是CPU占用率非常高。

位置：控制面板->管理工具->任务计划程序

![](/imported/posts/2020-02-26-12365879-53f5669a-microsoft-compatibility-telemetry占cpu资源高/images/img_001_9f4d1ec53e66.png)

2、右键点开【这台电脑】，点【管理】，点【服务和应用程序】点【服务】，在右边框里把【superfetch】

位置：运行->regedit

【windows search】
【HomeGroupListener】

【HomeGroupProvider】的启动类型设置成【禁用】

3、通过注册表定位并修改了HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\UnistoreSvc等类似项的start值为4，unistack服务就没开机运行啦啦啦，空闲时的硬盘占用下来了……
