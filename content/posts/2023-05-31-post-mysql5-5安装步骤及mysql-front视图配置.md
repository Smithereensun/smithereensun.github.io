---
title: "MySql5.5安装步骤及MySql_Front视图配置"
date: 2023-05-31
description: "一、下载文件 有需要的朋友，请自行到百度云下载 链接：https://pan.baidu.com/s/13Cf1VohMz_a0czBI05UqJg 提取码：cmyq 二、安装MySql 2.1、运行安装包：mysql-5.5.25a-winx64.msi 2.2、 接受协议 2.3、选择安装类型"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11648280.html"
---

<h1>一、下载文件</h1>
<p>有需要的朋友，请自行到百度云下载</p>
<p>链接：https://pan.baidu.com/s/13Cf1VohMz_a0czBI05UqJg <br>提取码：cmyq</p>
<h1> 二、安装MySql</h1>
<h2>2.1、运行安装包：mysql-5.5.25a-winx64.msi</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010143629620-867696409.png" alt="" /></p>
<h2>2.2、 接受协议</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010144030729-1582278337.png" alt="" /></p>
<h2>&nbsp;2.3、选择安装类型</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010144645562-993393649.png" alt="" /></p>
<h2>&nbsp;2.4、修改安装路径(可默认)</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010144829034-976827322.png" alt="" /></p>
<h2>&nbsp;2.5、安装</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010144908127-490576730.png" alt="" /></p>
<p>&nbsp;企业介绍(关闭即可)</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010145101730-1510378167.png" alt="" /></p>
<h2>&nbsp;2.6、配置MySql&nbsp;</h2>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010145551550-903775664.png" alt="" /></p>
<h2>&nbsp;2.7、下一步</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010145636986-611133930.png" alt="" /></p>
<h2>&nbsp;2.8、选择配置方式</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010145813091-911384902.png" alt="" /></p>
<h2>&nbsp;2.9、选择服务类型</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010150642946-630479788.png" alt="" /></p>
<h2>&nbsp;2.10、选择数据库的大致用途</h2>
<ul>
<li>“Multifunctional Database（通用多功能型，好）”</li>
<li>“Transactional Database Only（服务器类型，专注于事务处理，一般）”</li>
<li>“Non-Transactional Database Only（非事务处理型，较简单，主要做一些监控、记数用，对MyISAM数据类型的支持仅限于non-transactional）</li>

</ul>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010150933586-265331213.png" alt="" /></p>
<h2>&nbsp;2.11、选择表空间路径</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010151208550-66111308.png" alt="" /></p>
<h2>&nbsp;2.12、选择网站并发数</h2>
<ul>
<li>“Decision Support(DSS)/OLAP（20个左右）”</li>
<li>“Online Transaction Processing(OLTP)（500个左右）”</li>
<li>“Manual Setting（手动设置，自己输一个数）”</li>

</ul>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010151354463-1626373219.png" alt="" /></p>
<h2>&nbsp;2.13、配置TCP/IP</h2>
<p>是否启用TCP/IP连接，设定端口，如果不启用，就只能在自己的机器上访问mysql数据库了，在这个页面上，您还可以选择“启用标准模式”（Enable Strict Mode），这样MySQL就不会允许细小的语法错误。如果是新手，建议您取消标准模式以减少麻烦。但熟悉MySQL以后，尽量使用标准模式，因为它可以降低有害数据进入数据库的可能性。按“Next”继续</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010151633566-940778180.png" alt="" /></p>
<h2>&nbsp;2.14、选择编码格式</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010151904384-568773980.png" alt="" /></p>
<h2>&nbsp;2.15、是否将MySql添加到Windows服务中</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010152141997-665306656.png" alt="" /></p>
<h2>&nbsp;2.16、设置Root密码</h2>
<p>询问是否要修改默认root用户（超级管理）的密码。“Enable root access from remote machines（是否允许root用户在其它的机器上登陆，如果要安全，就不要勾上，如果要方便，就勾上它）”。最后“Create An Anonymous Account（新建一个匿名用户，匿名用户可以连接数据库，不能操作数据，包括查询）”，</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010152517632-1135494629.png" alt="" /></p>
<h2>&nbsp;2.17、执行安装</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010152611664-446328462.png" alt="" /></p>
<p>&nbsp;安装成功</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010152713293-1146484453.png" alt="" /></p>
<h1>&nbsp;三、安装MySql_Front</h1>
<h2>3.1、运行MySQL_Front_Setup.1765185107.exe</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010153031608-1598071478.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;3.2、选择安装目录位置</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010153136847-414949861.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;3.3、选择开始菜单文件夹</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010153229242-1746039868.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;3.4、选择附加任务</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010153312534-1690631585.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;3.5、安装</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010153349131-886116284.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;3.6、配置MySql_Front</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010153603128-1574869538.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;3.7、打开</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010153634729-1721118605.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;3.8、配置成功</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191010153710022-1706238396.png" alt="" /></p>
