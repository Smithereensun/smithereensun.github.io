{

  "title": "SpringBoot 整合模板引擎 jetbrick-template",
  "date": "2020-11-30",
  "description": "添加依赖 模板 测试 反射获取对象里的值，组装成Map结构 点我直达",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/14062922.html"

}

# 添加依赖

```text
        <dependency>
            <groupId>com.github.subchen</groupId>
            <artifactId>jetbrick-template</artifactId>
            <version>2.1.10</version>
        </dependency>
        <dependency>
            <groupId>com.mitchellbosecke</groupId>
            <artifactId>pebble</artifactId>
            <version>2.2.0</version>
        </dependency>
```

# 模板

![](/imported/posts/2020-11-30-14062922-c9adc8e8-springboot-整合模板引擎-jetbrick-template/images/img_001_134fd4060bfc.png)

```text
<div>
    <p>亲爱的<b>${username}</b>, 欢迎加入 biezhi!</p>
      <p>当您收到这封信的时候，您已经可以正常登录了。</p>
      <p>请点击链接登录首页: ${url}</p>
      <p>如果您的 email 程序不支持链接点击，请将上面的地址拷贝至您的浏览器(如IE)的地址栏进入。</p>
      <p>如果您还想申请管理员权限，可以联系管理员 ${email}</p>
      <p>我们对您产生的不便，深表歉意。</p>
      <p>希望您在 biezhi 系统度过快乐的时光!</p>
      <p></p>
      <p>-----------------------</p>
      <p></p>
      <p>(这是一封自动产生的email，请勿回复。)</p>
</div>
```

# 测试

![](/imported/posts/2020-11-30-14062922-c9adc8e8-springboot-整合模板引擎-jetbrick-template/images/img_002_ff12684d3a05.png)

```text
    @Test
    void contextLoads() {
        JetEngine engine   = JetEngine.create();
        JetTemplate template = engine.getTemplate("/jet.jet");
        Map<String, Object> context = new HashMap<String, Object>();
        context.put("username", "陈彦斌");
        context.put("email", "543210188@qq.com");
        context.put("url", "<a href='https://www.cnblogs.com/chenyanbin/'>https://www.cnblogs.com/chenyanbin/</a>");
        StringWriter writer = new StringWriter();
        template.render(context, writer);
        String output = writer.toString();
        System.out.println(output);
    }
```

# 反射获取对象里的值，组装成Map结构

[点我直达](https://www.cnblogs.com/chenyanbin/p/14063084.html)
