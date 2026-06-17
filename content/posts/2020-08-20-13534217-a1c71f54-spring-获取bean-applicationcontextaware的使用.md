{

  "title": "Spring 获取Bean ApplicationContextAware的使用",
  "date": "2020-08-20",
  "description": "创建类继承ApplicationContextAware** 使用",
  "tags": [
    "Spring Boot",
    "JAVA",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13534217.html"

}

## **创建类继承ApplicationContextAware**

```text
package net.ybclass.online_ybclass.utils;

import org.springframework.beans.BeansException;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationContextAware;
import org.springframework.stereotype.Component;

/**
 * @ClassName：AppUtil
 * @Description：获取bean工具类
 * @Author：chenyb
 * @Date：2020/8/20 11:39 上午
 * @Versiion：1.0
 */
@Component
public class AppUtil implements ApplicationContextAware {
    private static ApplicationContext applicationContext;
    @Override
    public void setApplicationContext(ApplicationContext args) throws BeansException {
        this.applicationContext=args;
    }
    public static Object getObject(String id){
        return applicationContext.getBean(id);
    }
}
```

## 使用

```text
@RestController
public class TestController {
    @GetMapping("test")
    public JsonData test()
    {
        VideoService videoService= (VideoService)AppUtil.getObject("videoServiceImpl");
        return JsonData.buildSuccess(videoService.listVideo());
    }
}
```
