---
title: "docker 容器镜像日志满了，解决方案"
date: 2022-06-02
description: "遇到问题 docker容器日志导致主机磁盘空间满了。docker logs -f container_name噼里啪啦一大堆，很占用空间，不用的日志可以清理掉了。 解决方案 找到日志文件 在linux上，容器日志一般存放在/var/lib/docker/containers/xxxxxx/下面， 以"
tags:
  - "Docker"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/16337223.html"
---

<h1 style="text-align: center">遇到问题</h1>
<p>　　docker容器日志导致主机磁盘空间满了。<code>docker logs -f container_name</code>噼里啪啦一大堆，很占用空间，不用的日志可以清理掉了。</p>
<h1 style="text-align: center">解决方案</h1>
<h2>找到日志文件</h2>
<p>　　在linux上，容器日志一般存放在<code>/var/lib/docker/containers/xxxxxx/</code>下面， 以json.log结尾的文件（业务日志）很大</p>
<h3>编写脚本</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">、新建脚本
touch docker_log_size.sh

</span><span style="color: rgba(128, 0, 128, 1)">2</span><span style="color: rgba(0, 0, 0, 1)">、脚本编写

#</span>!/bin/<span style="color: rgba(0, 0, 0, 1)">sh

echo </span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">======== docker containers logs file size ========</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">  

logs</span>=$(find /<span style="color: rgba(0, 0, 255, 1)">var</span>/lib/docker/containers/ -name *-<span style="color: rgba(0, 0, 0, 1)">json.log)  

</span><span style="color: rgba(0, 0, 255, 1)">for</span> log <span style="color: rgba(0, 0, 255, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> $logs  
        </span><span style="color: rgba(0, 0, 255, 1)">do</span><span style="color: rgba(0, 0, 0, 1)">  
             ls </span>-<span style="color: rgba(0, 0, 0, 1)">lh $log   
        done 


</span><span style="color: rgba(128, 0, 128, 1)">3</span><span style="color: rgba(0, 0, 0, 1)">、修改文件权限
chmod </span>+<span style="color: rgba(0, 0, 0, 1)">x docker_log_size.sh

</span><span style="color: rgba(128, 0, 128, 1)">4</span><span style="color: rgba(0, 0, 0, 1)">、执行脚本
sh docker_log_size.sh</span></pre>
