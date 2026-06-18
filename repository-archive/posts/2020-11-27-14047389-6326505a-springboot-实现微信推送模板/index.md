{

  "title": "SpringBoot 实现微信推送模板",
  "date": "2020-11-27",
  "description": "导读 由于最近手头上需要做个Message Gateway，涉及到：邮件(点我直达)、短信、公众号等推送功能，网上学习下，整理下来以备以后使用。 添加依赖 在SpringBoot项目中添加依赖 控制层代码 去微信公众平台注册一个开发测试账户 个人开发，我们可以去微信公众号平台注册个测试账户点我直达，",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/14047389.html"

}

# 导读

　　由于最近手头上需要做个Message Gateway，涉及到：邮件([点我直达](https://www.cnblogs.com/chenyanbin/p/14042642.html))、短信、公众号等推送功能，网上学习下，整理下来以备以后使用。

# 添加依赖

　　在SpringBoot项目中添加依赖

```text
        <!--微信模版消息推送三方sdk-->
        <dependency>
            <groupId>com.github.binarywang</groupId>
            <artifactId>weixin-java-mp</artifactId>
            <version>3.3.0</version>
        </dependency>
```

# 控制层代码

```text
package com.ybchen.springbootwechart.controller;

import me.chanjar.weixin.mp.api.WxMpInMemoryConfigStorage;
import me.chanjar.weixin.mp.api.WxMpService;
import me.chanjar.weixin.mp.api.impl.WxMpServiceImpl;
import me.chanjar.weixin.mp.bean.template.WxMpTemplateData;
import me.chanjar.weixin.mp.bean.template.WxMpTemplateMessage;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @ClassName：PushController
 * @Description：微信推送
 * @Author：chenyb
 * @Date：2020/11/27 10:33 上午
 * @Versiion：1.0
 */
@RestController
public class PushController {
    /*
     * 微信测试账号推送
     * */
    @GetMapping("/push")
    public String push() {
        //1，配置
        WxMpInMemoryConfigStorage wxStorage = new WxMpInMemoryConfigStorage();
        wxStorage.setAppId("AppId");
        wxStorage.setSecret("Secret");
        WxMpService wxMpService = new WxMpServiceImpl();
        wxMpService.setWxMpConfigStorage(wxStorage);

        //2,推送消息
        WxMpTemplateMessage templateMessage = WxMpTemplateMessage.builder()
                .toUser("ojPPk54RcFkCgGVP3m66v1RM2mvA")//要推送的用户openid
                .templateId("a7RPsASc7fw33zFo7zEfWKE0vrPnUo7VZ82fX3tTfMg")//模版id
                .url("https://www.cnblogs.com/chenyanbin/")//点击模版消息要访问的网址
                .build();
        //3,如果是正式版发送模版消息，这里需要配置你的信息
//                templateMessage.addData(new WxMpTemplateData("name", "value", "#FF00FF"));
//                templateMessage.addData(new WxMpTemplateData(name2, value2, color2));
        try {
            wxMpService.getTemplateMsgService().sendTemplateMsg(templateMessage);
            return "推送成功";
        } catch (Exception e) {
            System.out.println("推送失败：" + e.getMessage());
            e.printStackTrace();
            return "推送失败";
        }
    }
}
```

# 去微信公众平台注册一个开发测试账户

　　个人开发，我们可以去微信公众号平台注册个测试账户[点我直达](https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login)，微信扫码登录，会给我们一个免费的：appID、appsecret，微信扫码关注公众号，会显示关注测试公众号的用户列表。**全局错误码**：[点我直达](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Global_Return_Code.html)

![](./images/images/img_001_5796a5a8c9f5.gif)

# 测试

　　关注测试公众号，创建模板，并发送指定模板内容

![](./images/images/img_002_bd64f6c73684.gif)

![](./images/images/img_003_0290ca7ec175.gif)

# 替换模板内容

## 在微信公众平台创建模板

```text
语法：{{变量名.DATA}}
```

```text
姓名：{{user_name.DATA}}
性别：{{sex.DATA}}
手机号：{{phone.DATA}}
邮箱：{{email.DATA}}
```

![](./images/images/img_004_14bc5948131b.png)

## 控制层修改

![](./images/images/img_005_7beb95b7565f.png)

![](./images/images/img_006_8f900a89c634.gif)
![](./images/images/img_007_961ddebeb323.gif)

```text
package com.ybchen.springbootwechart.controller;

import me.chanjar.weixin.mp.api.WxMpInMemoryConfigStorage;
import me.chanjar.weixin.mp.api.WxMpService;
import me.chanjar.weixin.mp.api.impl.WxMpServiceImpl;
import me.chanjar.weixin.mp.bean.template.WxMpTemplateData;
import me.chanjar.weixin.mp.bean.template.WxMpTemplateMessage;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Map;
import java.util.Objects;

/**
 * @ClassName：PushController
 * @Description：微信推送
 * @Author：chenyb
 * @Date：2020/11/27 10:33 上午
 * @Versiion：1.0
 */
@RestController
public class PushController {
    /*
     * 微信测试账号推送
     * */
    @GetMapping("/push")
    public String push() {
        //1，配置
        WxMpInMemoryConfigStorage wxStorage = new WxMpInMemoryConfigStorage();
        wxStorage.setAppId("wx12db1518efd2302c");
        wxStorage.setSecret("056f31d80a5a22cc0c418cc08f5657ad");
        WxMpService wxMpService = new WxMpServiceImpl();
        wxMpService.setWxMpConfigStorage(wxStorage);
        //2,推送消息
        WxMpTemplateMessage templateMessage = WxMpTemplateMessage.builder()
                .toUser("ojPPk54RcFkCgGVP3m66v1RM2mvA")//要推送的用户openid
                .templateId("O0t0lPP7xRqbNz0-OwPzliSplzGFrkr4-au-OIGhiOE")//模版id
                .url("https://www.cnblogs.com/chenyanbin/")//点击模版消息要访问的网址
                .build();
        //3,如果是正式版发送模版消息，这里需要配置你的信息，替换微信公众号上创建的模板内容
        templateMessage.addData(new WxMpTemplateData("user_name", "陈彦斌", "#CCCCFF"));
        templateMessage.addData(new WxMpTemplateData("sex", "男", "#FF00FF"));
        templateMessage.addData(new WxMpTemplateData("phone", "188888888888", "#CCFF99"));
        templateMessage.addData(new WxMpTemplateData("email", "543210188@qq.com", "#FF0033"));
        try {
            wxMpService.getTemplateMsgService().sendTemplateMsg(templateMessage);
            return "推送成功";
        } catch (Exception e) {
            System.out.println("推送失败：" + e.getMessage());
            e.printStackTrace();
            return "推送失败";
        }
    }
}
```

View Code

## 推送消息

![](./images/images/img_008_4c51be08901f.png)
