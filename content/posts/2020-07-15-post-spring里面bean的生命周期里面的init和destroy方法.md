---
title: "Spring里面bean的生命周期里面的init和destroy方法"
date: 2020-07-15
description: "package net.cybclass.sp; import net.cybclass.sp.domain.Video; import net.cybclass.sp.domain.Video2; import net.cybclass.sp.domain.VideoOrder; import o"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13303940.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.domain.Video;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.domain.Video2;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> net.cybclass.sp.domain.VideoOrder;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.ApplicationContext;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.context.support.ClassPathXmlApplicationContext;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> app {
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> main(String[] args) {
        ApplicationContext applicationContext</span>=<span style="color: rgba(0, 0, 255, 1)">new</span> ClassPathXmlApplicationContext("applicationContext.xml"<span style="color: rgba(0, 0, 0, 1)">);
        Video2 video</span>=(Video2) applicationContext.getBean("video2"<span style="color: rgba(0, 0, 0, 1)">);
        System.out.println(video);
        ((ClassPathXmlApplicationContext)applicationContext).registerShutdownHook();
    }
}</span></pre>
