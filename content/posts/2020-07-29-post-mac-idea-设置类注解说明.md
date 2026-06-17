---
title: "mac idea 设置类注解说明"
date: 2020-07-29
description: "类注解 打开file-&gt;setting-&gt;Editor-&gt;File and Code Templates-&gt;Includes-&gt;File Header #if (${PACKAGE_NAME} &amp;&amp; ${PACKAGE_NAME} != &quot;&q"
tags:
  - "IDE"
  - "Mac系统"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13395026.html"
---

<h1 style="text-align: center">类注解</h1>
<p>打开file-&gt;setting-&gt;Editor-&gt;File and Code Templates-&gt;Includes-&gt;File Header</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200729083607048-1430684567.png" alt="" loading="lazy" /></p>
<div class="cnblogs_code">
<pre>#<span style="color: rgba(0, 0, 255, 1)">if</span> (${PACKAGE_NAME} &amp;&amp; ${PACKAGE_NAME} != "")<span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> ${PACKAGE_NAME};#end
#parse(</span>"File Header.java"<span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
  * @ClassName：${NAME}
  * @Description：TODO
  * @Author：${USER}
  * @Date：${DATE} ${TIME}
  * @Versiion：1.0
</span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> ${NAME} {
}</span></pre>
