---
title: "jconsole监听linux上的springboot工程"
date: 2022-08-28
description: "启动参数 nohup java -Xms128M -Xmx256M -Djava.rmi.server.hostname=47.116.143.16 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=18899 -D"
tags:
  - "Spring Boot"
  - "多线程并发编程"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/jconsole.html"
---

<h1 style="text-align: center">启动参数</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">nohup java  -Xms128M -Xmx256M  -Djava.rmi.server.hostname=47.116.143.16 -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=18899 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -jar lunch-0.0.1-SNAPSHOT.jar



说明 

-Djava.rmi.server.hostname为java程序运行所在的机器ip
-Dcom.sun.management.jmxremote.port为端口，自定义，保证是未使用的端口即可。jconsole通过这个端口来连接。
-Dcom.sun.management.jmxremote.authenticate=false表示在jconsole连接时可以不用输入账号和密码</span></pre>
