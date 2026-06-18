{

  "title": "Spring5.X bean自动装配Autowire属性",
  "date": "2020-07-15",
  "description": "属性注入 set方法、构造函数、POJO、list、map、ref，属于手工注入，点我直达 Spring自动注入 使用 元素的autowire属性为一个bean定义指定自动装配模式 autowire设置值 no：没有开启 byName：根据bean的id名称，注入到对应的属性里面 byType：根据",
  "tags": [
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13304762.html"

}

# 属性注入

- set方法、构造函数、POJO、list、map、ref，属于手工注入，[点我直达](https://www.cnblogs.com/chenyanbin/p/13303091.html)

# Spring自动注入

- 使用<bean>元素的autowire属性为一个bean定义指定自动装配模式
- autowire设置值

  - no：没有开启
  - byName：根据bean的id名称，注入到对应的属性里面
  - byType：根据bean需要注入的类型，注入到对应的属性里面

    - 如果按照类型注入，存在2个以上bean的话会抛异常
    - expected single matching bean but found 2

  - construcctor：通过构造函数注入，需要这个类型的构造函数

## byName演示

applicationContext.xml

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
    <bean id="videoOrder" class="net.cybclass.sp.domain.VideoOrder" autowire="byName">
        <property name="id" value="8"></property>
        <property name="outTradeNo" value="12312"></property>
    </bean>
</beans>
```

Video.java

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
    public void init()
    {
        System.out.println("Video init 被调用类");
    }
    public void destroy()
    {
        System.out.println("Video destroy 被调用类");
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

    @Override
    public String toString() {
        return "Video{" +
                "id=" + id +
                ", title='" + title + '\'' +
                '}';
    }
}
```

VideoOrder.java

```text
package net.cybclass.sp.domain;

public class VideoOrder {
    private int id;
    //订单号
    private String outTradeNo;
    private Video video;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getOutTradeNo() {
        return outTradeNo;
    }

    public void setOutTradeNo(String outTradeNo) {
        this.outTradeNo = outTradeNo;
    }

    public Video getVideo() {
        return video;
    }

    public void setVideo(Video video) {
        this.video = video;
    }

    @Override
    public String toString() {
        return "VideoOrder{" +
                "id=" + id +
                ", outTradeNo='" + outTradeNo + '\'' +
                ", video=" + video +
                '}';
    }
}
```

![](./images/images/img_001_49e7539ca121.gif)

　　从上我们可以看到byName注入，自动获取bean的id等于video的，当修改bean的id的值为video2的时候，就自动注入不到值类

# byType演示

![](./images/images/img_002_ee4371f4e95c.gif)

下面演示注册2次bean的，会抛异常

![](./images/images/img_003_d0d744917bc1.gif)

**expected single matching bean but found 2: video2,video3**

# constructor演示

为VideoOrder.java添加构造函数

![](./images/images/img_004_82a2016e1388.png)

修改applicationContext.xml

![](./images/images/img_005_aab995297a64.png)

![](./images/images/img_006_b5c6cb2c99ec.gif)

底层也是根据byType注入的

![](./images/images/img_007_cc2ff7138389.gif)
