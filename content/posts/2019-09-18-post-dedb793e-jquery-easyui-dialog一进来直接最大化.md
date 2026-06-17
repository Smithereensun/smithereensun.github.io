---
title: "jquery easyui dialog一进来直接最大化"
date: 2019-09-18
description: "扩展自 $.fn.window.defaults。通过 $.fn.dialog.defaults 重写默认的 defaults。 对话框（dialog）是一个特殊类型的窗口，它在顶部有一个工具栏，在底部有一个按钮栏。默认情况下，对话框（dialog）只有一个显示在头部右侧的关闭工具。用户可以配置对话"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11545284.html"
---

<p>&nbsp;</p>
<p>扩展自 $.fn.window.defaults。通过 $.fn.dialog.defaults 重写默认的 defaults。</p>
<p>对话框（dialog）是一个特殊类型的窗口，它在顶部有一个工具栏，在底部有一个按钮栏。默认情况下，对话框（dialog）只有一个显示在头部右侧的关闭工具。用户可以配置对话框行为来显示其他工具（比如：可折叠 collapsible、可最小化 minimizable、可最大化 maximizable，等等）。</p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>代码示例：</strong></span></p>
<p>$("#setActionDialogDiv").dialog({<br>                　　title: '设置特殊权限', //对话框的标题文本<br>                　　modal: true, //是否是模态div<br>                　　width: 600, //宽度<br>                　　height: 400, //高度<br>                　　collapsible: true, //定义是否显示折叠按钮<br>                　　minimizable: true, //定义是否显示最小化按钮<br>                　　maximizable: true, //定义是否显示最大化按钮<br>                　　resizable: true, //定义对话框是否可调整尺寸<br>                　　<span style="color: rgba(255, 0, 0, 1)"><strong>maximized:true, //初始化窗口最大化</strong></span><br>                　　buttons: [{<br>                    　　　　id: 'btnOk',<br>                    　　　　text: '设置',<br>                    　　　　iconCls: 'icon-ok',<br>                    　　　　handler: subSetActionFrm<br>                　　}, {<br>                    　　　　id: 'btnCancel',<br>                    　　　　text: '取消',<br>                    　　　　iconCls: 'icon-cancel',<br>                    　　　　handler: function () {<br>                        　　　　//弹出一个添加的对话框<br>                        　　　　$("#setActionDialogDiv").dialog("close");<br>                    　　}<br>                }]<br>            })</p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>效果：</strong></span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201909/1504448-20190918205151347-1018355843.png" alt="" /></p>
<p>&nbsp;</p>
