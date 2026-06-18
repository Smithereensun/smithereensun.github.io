{

  "title": "@ConfigurationProperties 还能这样用",
  "date": "2020-08-11",
  "description": "在编写项目代码时，我们要求更灵活的配置，更好的模块化整合。在 Spring Boot 项目中，为满足以上要求，我们将大量的参数配置在 application.properties 或 application.yml 文件中，通过 注解，我们可以方便的获取这些参数值 使用 @Configuration",
  "tags": [
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13473486.html"

}

在编写项目代码时，我们要求更灵活的配置，更好的模块化整合。在 Spring Boot 项目中，为满足以上要求，我们将大量的参数配置在 application.properties 或 application.yml 文件中，通过 `@ConfigurationProperties` 注解，我们可以方便的获取这些参数值

## 使用 @ConfigurationProperties 配置模块

　　假设我们正在搭建一个发送邮件的模块。在本地测试，我们不想该模块真的发送邮件，所以我们需要一个参数来「开关」 disable 这个功能。另外，我们希望为这些邮件配置一个默认的主题，这样，当我们查看邮件收件箱，通过邮件主题可以快速判断出这是测试邮件

在 application.properties 文件中创建这些参数:

![](/imported/posts/2020-08-11-13473486-b1191974-configurationproperties-还能这样用/images/img_001_f00081e69207.png)

我们可以使用 `@Value` 注解或着使用 Spring `Environment` bean 访问这些属性，是这种注入配置方式有时显得很笨重。我们将使用更安全的方式(`@ConfigurationProperties` )来获取这些属性

![](/imported/posts/2020-08-11-13473486-b1191974-configurationproperties-还能这样用/images/img_002_59b6c5e7c158.png)

`@ConfigurationProperties` 的基本用法非常简单:我们为每个要捕获的外部属性提供一个带有字段的类。请注意以下几点:

- 前缀定义了哪些外部属性将绑定到类的字段上
- 根据 Spring Boot 宽松的绑定规则，类的属性名称必须与外部属性的名称匹配
- 我们可以简单地用一个值初始化一个字段来定义一个默认值
- 类本身可以是包私有的
- 类的字段必须有公共 setter 方法
