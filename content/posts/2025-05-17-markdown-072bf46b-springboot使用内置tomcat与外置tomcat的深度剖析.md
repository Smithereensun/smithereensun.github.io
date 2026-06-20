{

  "title": "SpringBoot使用内置Tomcat与外置Tomcat的深度剖析",
  "has_date": true,
  "description": "使用内置tomcat启动 配置案例 启动方式 IDEA中main函数启动 mvn springboot-run java -jar XXX.jar 使用这种方式时，为保证服务在后台运行，会使用nohup 使用java -jar默认情况下，不会启动任何嵌入式Application Server，该命令",
  "tags": [
    "框架",
    "Spring Boot",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/springboot/springbootstart-twoway - SpringBoot使用内置Tomcat与外置Tomcat的深度剖析.md",
  "date": "2025-05-17"

}

## [使用内置tomcat启动](#使用内置tomcat启动)

### [配置案例](#配置案例)

#### [启动方式](#启动方式)

1.
IDEA中main函数启动

1.
mvn springboot-run

1.
java -jar XXX.jar
 使用这种方式时，为保证服务在后台运行，会使用nohup

使用java -jar默认情况下，不会启动任何嵌入式Application Server，该命令只是启动一个执行jar main的JVM进程，当spring-boot-starter-web包含嵌入式tomcat服务器依赖项时，执行java -jar则会启动Application Server

#### [配置内置tomcat属性](#配置内置tomcat属性)

关于Tomcat的属性都在 `org.springframework.boot.autoconfigure.web.ServerProperties` 配置类中做了定义，我们只需在application.properties配置属性做配置即可。通用的Servlet容器配置都以 `server` 作为前缀

而Tomcat特有配置都以 `server.tomcat` 作为前缀

注意：使用内置tomcat不需要有tomcat-embed-jasper和spring-boot-starter-tomcat依赖，因为在spring-boot-starter-web依赖中已经集成了tomcat

### [原理](#原理)

#### [从main函数说起](#从main函数说起)

既然我们想知道tomcat在SpringBoot中是怎么启动的，那么run方法中，重点关注创建应用上下文（createApplicationContext）和刷新上下文（refreshContext）。

#### [创建上下文](#创建上下文)

这里会创建AnnotationConfigServletWebServerApplicationContext类。而AnnotationConfigServletWebServerApplicationContext类继承了ServletWebServerApplicationContext，而这个类是最终集成了AbstractApplicationContext。

#### [刷新上下文](#刷新上下文)

这里ServletWebServerFactory接口有4个实现类，对应着四种容器：

而其中我们常用的有两个：TomcatServletWebServerFactory和JettyServletWebServerFactory。

getWebServer这个方法创建了Tomcat对象，并且做了两件重要的事情：把Connector对象添加到tomcat中，configureEngine(tomcat.getEngine());

getWebServer方法返回的是TomcatWebServer。

## [使用外置tomcat部署](#使用外置tomcat部署)

### [配置案例](#配置案例-1)

[外置Tomcat启动SpringBoot源码点击这里](https://github.com//SpringBoot-Demo/tree/master/02-helloworld-tomcat)

#### [继承SpringBootServletInitializer](#继承springbootservletinitializer)

- 外部容器部署的话，就不能依赖于Application的main函数了，而是要以类似于web.xml文件配置的方式来启动Spring应用上下文，此时需要在启动类中继承SpringBootServletInitializer，并重写configure方法；还添加 @SpringBootApplication 注解，这是为了能扫描到所有Spring注解的bean

方式一：启动类继承SpringBootServletInitializer实现configure：

这个类的作用与在web.xml中配置负责初始化Spring应用上下文的监听器作用类似，只不过在这里不需要编写额外的XML文件了。

方式二：新增加一个类继承SpringBootServletInitializer实现configure：

#### [pom.xml修改tomcat相关的配置](#pom-xml修改tomcat相关的配置)

首先需要将 jar 变成war `&lt;packaging&gt;war&lt;/packaging&gt;`

如果要将**最终的打包形式改为war**的话，还需要对pom.xml文件进行修改，因为spring-boot-starter-web中包含内嵌的tomcat容器，所以直接部署在外部容器会冲突报错。因此需要将内置tomcat排除

在这里需要移除对嵌入式Tomcat的依赖，这样打出的war包中，在lib目录下才不会包含Tomcat相关的jar包，否则将会出现启动错误。

但是移除了tomcat后，原始的sevlet也被移除了，因此还需要额外引入servet的包

#### [注意的问题](#注意的问题)

此时打成的包的名称应该和 application.properties 的 server.context-path=/test 保持一致

如果不一样发布到tomcat的webapps下上下文会变化

### [原理](#原理-1)

tomcat不会主动去启动springboot应用，， 所以tomcat启动的时候肯定调用了**SpringBootServletInitializer**的SpringApplicationBuilder， 就会启动springboot。

ServletContainerInitializer的实现放在jar包的META-INF/services文件夹下，有一个名为javax.servlet.ServletContainerInitializer的文件，内容就是ServletContainerInitializer的实现类的全类名。当servlet容器启动时候就会去该文件中找到ServletContainerInitializer的实现类，从而创建它的实例调用onstartUp。这里就是用了SPI机制

#### [HandlesTypes(WebApplicationInitializer.class)](#handlestypes-webapplicationinitializer-class)

- @HandlesTypes传入的类为ServletContainerInitializer感兴趣的

- 容器会自动在classpath中找到 WebApplicationInitializer，会传入到onStartup方法的webAppInitializerClasses中

- `Set&lt;Class&lt;?&gt;&gt; webAppInitializerClasses`这里面也包括之前定义的TomcatStartSpringBoot

#### [SpringBootServletInitializer](#springbootservletinitializer)

① 当调用configure就会来到TomcatStartSpringBoot .configure，将Springboot启动类传入到builder.source

② 调用SpringApplication application = builder.build(); 就会根据传入的Springboot启动类来构建一个SpringApplication

③ 调用 return run(application); 就会启动springboot应用

也就相当于Main函数启动：

之后的流程就与上面 使用内置Tomcat的Main函数一致了
