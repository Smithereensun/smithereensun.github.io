{

  "title": "SpringBoot2.X定时任务schedule",
  "date": "2020-07-06",
  "description": "什么是定时任务和常见定时任务区别？ 某个时间定时处理某个任务 发邮件、短信等 消息提醒 统计报表系统 。。。 常见定时任务 Java自带的java.util.Timer类配置比较麻烦，时间延后问题 Quartz框架：配置更简单，xml或者注解适合分布式或者大型调度作业 SpringBoot框架自带 ",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13257569.html"

}

什么是定时任务和常见定时任务区别？

- 某个时间定时处理某个任务
- 发邮件、短信等
- 消息提醒
- 统计报表系统
- 。。。

常见定时任务

- Java自带的java.util.Timer类配置比较麻烦，时间延后问题
- Quartz框架：配置更简单，xml或者注解适合分布式或者大型调度作业
- SpringBoot框架自带

SpringBoot使用注解方式开启定时任务

- 启动类里面加@EnableScheduling*开启定时任务，自动扫描*
- 定时任务业务类加注解@Conponent被容器扫描
- 定时执行的方法上加上注解@Scheduled(fixedRate=2000)定期执行一次

**cron**：定时任务表达式(**crontab工具：https://tool.lu/crontab**)

**fixedRate**：定时多久执行一次

**fixedDelay**：上一次执行结果时间点后xx秒再次执行

![](/imported/posts/2020-07-06-13257569-ef27d5f5-springboot2-x定时任务schedule/images/img_001_e8b5a8b4d21c.png)

![](/imported/posts/2020-07-06-13257569-ef27d5f5-springboot2-x定时任务schedule/images/img_002_871d3e01b469.png)

演示

![](/imported/posts/2020-07-06-13257569-ef27d5f5-springboot2-x定时任务schedule/images/img_003_8210a9e07ff7.gif)
