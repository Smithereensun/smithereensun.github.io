{

  "title": "Spring的@Configuration和@Bean注解定义第三方bean",
  "date": "2020-07-15",
  "description": "@Configuration和@Bean注解的使用 @Configuration标注在类上，相当于把该类作为spring的xml配置文件中 ，作用为：配置spring容器(应用上下文) @bean注解：用于告诉方法产生一个Bean对象，然后这个Bean对象交给Spring管理，Spring将会将这个",
  "tags": [
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13307323.html"

}

# @Configuration和@Bean注解的使用

- @Configuration标注在类上，相当于把该类作为spring的xml配置文件中<beans>，作用为：配置spring容器(应用上下文)
- @bean注解：用于告诉方法产生一个Bean对象，然后这个Bean对象交给Spring管理，Spring将会将这个Bean对象放在自己的IOC容器中
- 注意：Spring IOC容器管理一个或多个bean，这些bean都需要在@Configuration注解下进行创建

## AppConfig.java

```text
package net.cybclass.sp.config;

import net.cybclass.sp.domain.VideoOrder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;

@Configuration
public class AppConfig {
    //使用@Bean注解，表明这个bean交给spring进行管理，如果没有指定名称，默认采用方法名首字母小写
    //@Bean
    @Bean(value = "videoOrder",initMethod = "init",destroyMethod = "destroy")
    @Scope
    public VideoOrder videoOrder(){
        return new VideoOrder();
    }
}
```

## VideoOrder.java

```text
package net.cybclass.sp.domain;

public class VideoOrder {
    public VideoOrder(){

    }
    public void init(){
        System.out.println("VideoOrder init被调用");
    }
    public void destroy(){
        System.out.println("VideoOrder destroy被调用");
    }
    public VideoOrder(Video video){
        this.video=video;
    }
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

## 演示

![](/imported/posts/2020-07-15-13307323-bc5d9b38-spring的-configuration和-bean注解定义第三方bean/images/img_001_31c124b17d5f.png)
