---
title: "SpringBoot2.X定时任务schedule"
date: 2020-07-06
description: "什么是定时任务和常见定时任务区别？ 某个时间定时处理某个任务 发邮件、短信等 消息提醒 统计报表系统 。。。 常见定时任务 Java自带的java.util.Timer类配置比较麻烦，时间延后问题 Quartz框架：配置更简单，xml或者注解适合分布式或者大型调度作业 SpringBoot框架自带"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13257569.html"
---

<p>什么是定时任务和常见定时任务区别？</p>
<ul>
<li>某个时间定时处理某个任务</li>
<li>发邮件、短信等</li>
<li>消息提醒</li>
<li>统计报表系统</li>
<li>。。。</li>
</ul>
<p>常见定时任务</p>
<ul>
<li>Java自带的java.util.Timer类配置比较麻烦，时间延后问题</li>
<li>Quartz框架：配置更简单，xml或者注解适合分布式或者大型调度作业</li>
<li>SpringBoot框架自带</li>
</ul>
<p>SpringBoot使用注解方式开启定时任务</p>
<ul>
<li>启动类里面加@EnableScheduling<em id="__mceDel">开启定时任务，自动扫描</em></li>
<li>定时任务业务类加注解@Conponent被容器扫描</li>
<li>定时执行的方法上加上注解@Scheduled(fixedRate=2000)定期执行一次</li>
</ul>
<p><strong><span style="color: rgba(255, 0, 0, 1)">cron</span></strong>：定时任务表达式(<span style="color: rgba(255, 0, 0, 1)"><strong>crontab工具：https://tool.lu/crontab</strong></span>)</p>
<p><strong><span style="color: rgba(255, 0, 0, 1)">fixedRate</span></strong>：定时多久执行一次</p>
<p><strong><span style="color: rgba(255, 0, 0, 1)">fixedDelay</span></strong>：上一次执行结果时间点后xx秒再次执行</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706210524117-1702839102.png" alt="" loading="lazy" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706210634608-157057731.png" alt="" loading="lazy" /></p>
<p>演示</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202007/1504448-20200706211029922-2093895905.gif" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
