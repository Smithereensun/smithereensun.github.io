{

  "title": "win10彻底关闭windows defender，解决无故占用大量CPU问题",
  "date": "2020-03-03",
  "description": "win10彻底关闭defender的方法 首先右键开始菜单按钮，点击“运行”，输入“gpedit.msc”，打开“本地组策略编辑器”。 依次选择“计算机配置”-“管理模板”-“Windows组件”-“Windows Defender防病毒程序”。 找到“关闭Windows Defender防病毒程序",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12402905.html"

}

# win10彻底关闭defender的方法

1. 首先右键开始菜单按钮，点击“运行”，输入“gpedit.msc”，打开“本地组策略编辑器”。
2. 依次选择“计算机配置”-“管理模板”-“Windows组件”-“Windows Defender防病毒程序”。
3. 找到“关闭Windows Defender防病毒程序”选项，右键“编辑“，选择“已启用”，确定即可。

![](/imported/posts/2020-03-03-12402905-44d8c9b9-win10彻底关闭windows-defender-解决无故占用大量cpu问题/images/img_001_6cb9972de8e7.png)

　　如此一来，Windows Defender的扫描查杀功能就彻底关闭了，不过防火墙和浏览器保护等功能还是开着的。这时候，你再打开任务管理，看看“Antimalware Service Executable”这个一直占用大量cpu的进程是不是消失了呢。

好了，笔记本风扇终于不会无故呼呼呼地吹了，整个世界也终于安静了。如果你也受此问题困扰，就赶紧试试此方法吧。
