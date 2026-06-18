{

  "title": "元素“context:component-scan”的前缀“context”未绑定",
  "date": "2019-11-02",
  "description": "首先报这个错误，你得明白，是什么原因导致的？ 答：未引入命名空间，和约束文件 解决方法： 标签中加上 约束文件的话，请看：http://www.springframework.org/schema/beans/spring-beans.xsd 若不加上命名空间的话bean得这样写",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11784503.html"

}

首先报这个错误，你得明白，是什么原因导致的？

　　答：未引入命名空间，和约束文件

解决方法：

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"**
    xmlns:context="http://www.springframework.org/schema/context"**
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        **http://www.springframework.org/schema/context
        http://****www.springframework.org/schema/context/spring-context.xsd**">
        <!-- 组件扫描器，主要是spring使用，用来扫描带有指定注解的类，将这些加载成BeanDefinition -->
    <context:component-scan base-package="com.cyb.spring.service" />
</beans>
```

标签中加上

```text
<!--命名空间-->
xmlns:context="http://www.springframework.org/schema/context"
<!--别名和约束文件-->
xsi:schemaLocation="http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context.xsd"
```

![](/imported/posts/2019-11-02-11784503-e596ba87-元素-context-component-scan-的前缀-context-未绑定/images/img_001_0070a3f285e2.png)

约束文件的话，请看：http://www.springframework.org/schema/beans/spring-beans.xsd

```text
<!--别名-->
http://www.springframework.org/schema/context
<!--公网地址-->
http://www.springframework.org/schema/context/spring-context.xsd
```

![](/imported/posts/2019-11-02-11784503-e596ba87-元素-context-component-scan-的前缀-context-未绑定/images/img_002_ed5f0cdcead8.png)

若不加上命名空间的话bean得这样写

```text
<beans:bean id="" class=""></beans>
```
