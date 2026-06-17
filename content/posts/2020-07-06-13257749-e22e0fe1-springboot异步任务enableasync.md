{

  "title": "SpringBoot异步任务EnableAsync",
  "date": "2020-07-06",
  "description": "什么是一部任务和使用场景：适用于处理log、发送邮件、短信...等 下单接口->查库存 1000 余额校验 1500 风控用户 1000 启动类里面使用@EnableAsync注解开启功能，自动扫描 定义异步任务类并使用@Component标记组件被容器扫描，异步方法加上@Async TestCon",
  "tags": [
    "Spring Boot"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13257749.html"

}

什么是一部任务和使用场景：适用于处理log、发送邮件、短信...等

- 下单接口->查库存 1000
- 余额校验 1500
- 风控用户 1000

启动类里面使用@EnableAsync注解开启功能，自动扫描

定义异步任务类并使用@Component标记组件被容器扫描，异步方法加上@Async

![](/imported/posts/2020-07-06-13257749-e22e0fe1-springboot异步任务enableasync/images/img_001_721e06a0231b.png)

![](/imported/posts/2020-07-06-13257749-e22e0fe1-springboot异步任务enableasync/images/img_002_f05c452df7f6.png)

TestController.java

![](/imported/posts/2020-07-06-13257749-e22e0fe1-springboot异步任务enableasync/images/img_003_9c2f4b70c4a2.png)

测试

![](/imported/posts/2020-07-06-13257749-e22e0fe1-springboot异步任务enableasync/images/img_004_bb52d7244610.gif)
