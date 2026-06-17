{

  "title": "Spring里面bean的生命周期里面的init和destroy方法",
  "date": "2020-07-15",
  "description": "Spring里面bean的生命周期里面的init和destroy方法",
  "tags": [
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13303940.html"

}

```text
package net.cybclass.sp;

import net.cybclass.sp.domain.Video;
import net.cybclass.sp.domain.Video2;
import net.cybclass.sp.domain.VideoOrder;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class app {
    public static void main(String[] args) {
        ApplicationContext applicationContext=new ClassPathXmlApplicationContext("applicationContext.xml");
        Video2 video=(Video2) applicationContext.getBean("video2");
        System.out.println(video);
        ((ClassPathXmlApplicationContext)applicationContext).registerShutdownHook();
    }
}
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="video2" class="net.cybclass.sp.domain.Video2" parent="video" init-method="init" destroy-method="destroy">
        <property name="summary" value="这个是summary"></property>
    </bean>
</beans>
```
