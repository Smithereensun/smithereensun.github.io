---
title: "Oracle 安装步骤、安装中错误处理、完整卸载"
date: 2019-06-26
description: "/*************************************************以下ORACLE服务端安装*************************************************************/ 1.&#160;获取Oracle安装程序。 2."
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10683505.html"
---

<p>&nbsp;</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>/*************************************************以下ORACLE服务端安装*************************************************************/</strong></span></p>
<p>&nbsp;</p>
<p>1.&nbsp;<span style="font-family: 宋体">获取</span>Oracle<span style="font-family: 宋体">安装程序。</span></p>
<p class="15">2.&nbsp;<span style="font-family: 宋体">运行安装程序</span>setup.exe<span style="font-family: 宋体">，</span><span style="font-family: 宋体">将启动</span>Oracle&nbsp;Universal Installer<span style="font-family: 宋体">，</span>然后进行先决条件检查。</p>
<p class="15"><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145354551-1691396315.png" alt="" /></p>
<p>3.<span style="font-family: 宋体">可能会出现</span>“环境不满足最低要求”的提示，点击“是”，继续即可。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145418139-295986358.png" alt="" /></p>
<p>4.<span style="font-family: 宋体">配置安全更新。电子邮件可写可不写，取消下面的</span>“我希望通过My&nbsp;Oracle Support<span style="font-family: 宋体">接收安全更新</span>(W)<span style="font-family: 宋体">”，如下图所示，点击“下一步”。</span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145442555-1585551380.png" alt="" /></p>
<p>5.<span style="font-family: 宋体">如果不填写电子邮件，会弹出提示框，如下图所示，点击</span>“是”即可。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145500334-1447297285.png" alt="" /></p>
<p>6.<span style="font-family: 宋体">安装选项。选择默认的</span>“创建和配置数据库”，如下图所示，点击“下一步”。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145515841-1758222359.png" alt="" /></p>
<p>7.<span style="font-family: 宋体">系统类。有“桌面类”和“服务器类”两个选项，这里我们选择“服务器类”，如下图所示，点击“下一步”。</span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145531575-1606642765.png" alt="" /></p>
<p>8.<span style="font-family: 宋体">网格安装选项。选择</span>“单实例数据库安装”，如下图所示，点击“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145546912-1754423877.png" alt="" /></p>
<p>9.<span style="font-family: 宋体">安装类型。选择</span>“高级安装”，如下图所示，点击“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145605171-56241225.png" alt="" /></p>
<p>10.<span style="font-family: 宋体">产品语言。直接默认即可</span>(<span style="font-family: 宋体">简体中文，英语</span><span style="font-family: Calibri">)</span><span style="font-family: 宋体">，如下图所示，点击“下一步”。</span></p>
<p><span style="font-family: 宋体"><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145621551-591817669.png" alt="" /></span></p>
<p>11.<span style="font-family: 宋体">数据库版本。选择</span>“企业版”，如下图所示，点击“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145634518-1374992296.png" alt="" /></p>
<p>12.<span style="font-family: 宋体">安装位置。选择安装位置，这里只需填写</span>“<span style="font-family: Calibri">Orac</span>le<span style="font-family: 宋体">基目录</span>”，“软件位置”会自动生成，如下图所示，点击“下一步”。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145650124-559848545.png" alt="" /></p>
<p>13.<span style="font-family: 宋体">配置类型。选择</span>“一般用途<span style="font-family: Calibri">/</span><span style="font-family: 宋体">事务处理”，如下图所示，点击“下一步”。</span></p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145705303-1834830218.png" alt="" /></p>
<p>14.<span style="font-family: 宋体">数据库标识符。填入</span>“全局数据库名”和“<span style="font-family: Calibri">Oracl</span>e<span style="font-family: 宋体">服务标识符</span>”，如下图所示，点击“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145718710-1580525917.png" alt="" /></p>
<p>15.<span style="font-family: 宋体">配置选项。切换到</span>“字符集”选项卡，选择“使用<span style="font-family: Calibri">Uni</span>code(AL32UTF8)”，其他默认，如下图所示，点击“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145733614-190078355.png" alt="" /></p>
<p>16.<span style="font-family: 宋体">管理选项。如下图所示，不用设置，直接点击</span>“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145747285-952757367.png" alt="" /></p>
<p>17.<span style="font-family: 宋体">数据库存储。可以采用默认参数，如下图所示，点击</span>“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145800823-567432828.png" alt="" /></p>
<p>18.<span style="font-family: 宋体">备份和恢复。选择此项可以启用或禁用数据库的自动备份，如下图所示，这里选择</span>“不启用自动备份”，如下图所示，点击“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145813642-755876781.png" alt="" /></p>
<p>19.<span style="font-family: 宋体">方案口令。为了便于本地测试，这里使用了相同的密码，实际部署时可根据具体情况进行设置，如下图所示，点击</span>“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145832315-983829670.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145839094-868437931.png" alt="" /></p>
<p>20.<span style="font-family: 宋体">概要。完成先决条件检查后，单击</span>“完成”就可以正式安装了，如下图所示。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145851309-960513762.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145900137-1443181761.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145906327-803210539.png" alt="" /></p>
<p>21.<span style="font-family: 宋体">安装产品。安装完成后，会列出相关数据库配置清单，最好截图保存，如下图所示，点击</span>“确定”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145920644-102301375.png" alt="" /></p>
<p>22.<span style="font-family: 宋体">完成。这时安装已经完成，如下图所示，点击</span>“关闭”即可。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410145958641-762549581.png" alt="" /></p>
<p>23.<span style="font-family: 宋体">测试。打开</span>Oracle<span style="font-family: 宋体">自带的</span><span style="font-family: Calibri">SQL PLUS</span><span style="font-family: 宋体">，</span>如下图所示。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410150016175-730208664.png" alt="" /></p>
<p>24.<span style="font-family: 宋体">输入用户名和密码</span>(<span style="font-family: 宋体">就是第</span><span style="font-family: Calibri">19</span><span style="font-family: 宋体">步设置的密码</span><span style="font-family: Calibri">)</span><span style="font-family: 宋体">，如下图所示，测试成功！可以直接输入</span><span style="font-family: Calibri">SQL</span><span style="font-family: 宋体">语句，注意，这里</span><span style="font-family: Calibri">Oracle</span><span style="font-family: 宋体">输入的口令是不显示的。</span></p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410150029591-519983821.png" alt="" /></p>
<p>&nbsp;</p>
<p><strong><span style="color: rgba(255, 0, 0, 1)">/*************************************************以下ORACLE客户端安装*************************************************************/</span><br></strong></p>
<p>1.获取Oracle Client程序。</p>
<p>2.<span style="font-family: 宋体">运行安装程序</span>setup.exe<span style="font-family: 宋体">，将启动</span>Oracle&nbsp;Universal Installer，然后进行先决条件检查。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410151235932-285208483.png" alt="" /></p>
<p><span style="font-family: 宋体">3.选择安装类型。选择</span>“运行时”项，如下图所示，点击“下一步”。</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410151312250-1721255342.png" alt="" /></p>
<p><span style="font-family: 宋体">4.选择产品语言。直接默认即可</span>(<span style="font-family: 宋体">简体中文，英语</span><span style="font-family: Calibri">)</span><span style="font-family: 宋体">，如下图所示，点击“下一步”。</span></p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410151332576-1118478487.png" alt="" /></p>
<p><span style="font-family: 宋体">5.指定安装位置。选择安装位置，这里只需填写</span>“<span style="font-family: Calibri">Oracl</span>e<span style="font-family: 宋体">基目录</span>”，“软件位置”会自动生成，如下图所示，点击“下一步”。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410151353547-815085056.png" alt="" /></p>
<p>6.<span style="font-family: 宋体">执行先决条件检查。如果出现错误，可以勾选</span>“全部忽略”，如下图所示，点击“下一步”。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410151455141-1976760758.png" alt="" /></p>
<p>8.<span style="font-family: 宋体">概要。显示安装概要信息，点击</span>“完成”，开始安装产品，如下图所示。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410151512155-1818820356.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410151521767-183487653.png" alt="" /></p>
<p>9.<span style="font-family: 宋体">完成。安装完成，如下图所示，点击</span>“关闭”。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410151539989-1415266305.png" alt="" /></p>
<p>&nbsp;</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>&nbsp;/*************************************************以下错误处理*************************************************************/</strong></span></p>
<p>&nbsp;</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201904/1504448-20190410150221751-376426354.png" alt="" /></p>
<p>&nbsp;</p>
<p>地址:https://blog.csdn.net/maq2ian0gqi1ang2/article/details/52723908</p>
<p>&nbsp;</p>
<p><span style="color: rgba(255, 0, 0, 1)">/*************************************************以下完整清数据库(包含注册表等)*************************************************************/</span></p>
<p>&nbsp;地址:https://jingyan.baidu.com/article/922554468d4e6b851648f4e3.html</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>oracle百度云盘地址:</p>
<p>服务器</p>
<p>链接：https://pan.baidu.com/s/1Q9T-Swt_uqyTTCrJRNACWQ <br>提取码：hbh9 </p>
<p><br>客户端</p>
<p>链接：https://pan.baidu.com/s/13rIvqudK4c_CHivrABwekw <br>提取码：0jfe <br><br></p>
