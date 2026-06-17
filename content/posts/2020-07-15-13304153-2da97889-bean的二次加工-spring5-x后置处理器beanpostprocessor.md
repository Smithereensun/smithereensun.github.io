{

  "title": "bean的二次加工-Spring5.X后置处理器BeanPostProcessor",
  "date": "2020-07-15",
  "description": "什么是BeanPostProcessor 是Spring IOC容器给我们提供的一个扩展接口 在调用初始化方法前后对Bean进行额外加工，ApplicationContext会自动扫描实现了BeanPostProcessor得bean，并注册这些bean为后置处理器 是Bean的统一前置后置处理而不",
  "tags": [
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13304153.html"

}

# 什么是BeanPostProcessor

- 是Spring IOC容器给我们提供的一个扩展接口
- 在调用初始化方法前后对Bean进行额外加工，ApplicationContext会自动扫描实现了BeanPostProcessor得bean，并注册这些bean为后置处理器
- 是Bean的统一前置后置处理而不是基于某一个bean

## 执行顺序

```text
Spring IOC容器实例化
调用BeanPostProcessor的postProcessBeforeInitialization方法
调用bean实例的初始化方法
调用BeanPostProcessor的postProcessAfterInitialization方法
```

注意：**接口重写的两个方法不能返回null**，如果返回null那么在后续初始化方法将报空指针异常或者通过getBean()方法获取不到bean实例对象

## 可以注册多个BeanPostProcessor顺序

- 在Spring机制中可以指定后置处理器调用顺序，**通过BeanPostProcessor接口实现类实现Ordered接口getOrder方法，该方法返回整数**，默认值为0优先级最高，**值越大优先级越低**

![](/imported/posts/2020-07-15-13304153-2da97889-bean的二次加工-spring5-x后置处理器beanpostprocessor/images/img_001_b4f57c5a49b5.png)

![](/imported/posts/2020-07-15-13304153-2da97889-bean的二次加工-spring5-x后置处理器beanpostprocessor/images/img_002_b4e985e721ca.png)

![](/imported/posts/2020-07-15-13304153-2da97889-bean的二次加工-spring5-x后置处理器beanpostprocessor/images/img_003_478e13914cc5.png)

![](/imported/posts/2020-07-15-13304153-2da97889-bean的二次加工-spring5-x后置处理器beanpostprocessor/images/img_004_13c3f4a4d8a2.png)

![](/imported/posts/2020-07-15-13304153-2da97889-bean的二次加工-spring5-x后置处理器beanpostprocessor/images/img_005_363d91748ff1.png)

### CustomBeanPostProcessor.java实现接口BeanPostProcessor

```text
package net.cybclass.sp.processor;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.config.BeanPostProcessor;

public class CustomBeanPostProcessor implements BeanPostProcessor {
    public Object postProcessBeforeInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("CustomBeanPostProcessor postProcessBeforeInitialization beanName="+beanName);
        return bean;
    }

    public Object postProcessAfterInitialization(Object bean, String beanName) throws BeansException {
        System.out.println("CustomBeanPostProcessor postProcessAfterInitialization beanName="+beanName);
        return bean;
    }
}
```

### applicationContext.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="video" class="net.cybclass.sp.domain.Video">
        <property name="id" value="8"></property>
        <property name="title" value="SpringBoot课程专题"></property>
    </bean>
    <bean class="net.cybclass.sp.processor.CustomBeanPostProcessor"></bean>
</beans>
```

### Video.java

```text
package net.cybclass.sp.domain;

public class Video {
    public Video()
    {
        System.out.println("Video 默认空构造函数被调用");
    }
    {
        System.out.println("Video 构造块被调用");
    }
    static
    {
        System.out.println("Video static 静态代码块被调用");
    }
    private int id;
    private String title;
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
}
```

### app.java

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
        Video video=(Video) applicationContext.getBean("video");
        System.out.println(video);
        ((ClassPathXmlApplicationContext)applicationContext).registerShutdownHook();
    }
}
```

### 验证

![](/imported/posts/2020-07-15-13304153-2da97889-bean的二次加工-spring5-x后置处理器beanpostprocessor/images/img_006_f0c492bbae2c.png)
