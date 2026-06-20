{

  "title": "深度揭秘SpringBoot自动装配的实现原理",
  "has_date": true,
  "description": "引入 先看SpringBoot的主配置类 @SpringBootApplication 点进@SpringBootApplication来看，发现@SpringBootApplication是一个组合注解。 @SpringBootApplication 由 @Configuration、@Enabl",
  "tags": [
    "框架",
    "Spring Boot",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/springboot/principleofautomaticassembly - 深度揭秘SpringBoot自动装配的实现原理.md",
  "date": "2025-05-17"

}

## [引入](#引入)

先看SpringBoot的主配置类

## [@SpringBootApplication](#springbootapplication)

点进@SpringBootApplication来看，发现@SpringBootApplication是一个组合注解。

@SpringBootApplication 由 @Configuration、@EnableAutoConfiguration、@ComponentScan 注解的集合组成：

- @Configuration：允许注册额外的 bean 或导入其他配置类

- @EnableAutoConfiguration：启用 SpringBoot 的自动配置机制

- @ComponentScan：扫描被@Component (@Repository,@Service,@Controller)注解的 bean，注解默认会扫描该类所在的包下所有的类。

### [@SpringBootConfiguration](#springbootconfiguration)

@SpringBootConfiguration 注解源码如下：

可以看到这个注解除了元注解以外，就只有一个@Configuration，那也就是说这个注解相当于@Configuration，所以这两个注解作用是一样的，也就是能够去注册一些额外的Bean，并且导入一些额外的配置。

@Configuration还有一个作用就是把该类变成一个配置类，不需要额外的XML进行配置。所以@SpringBootConfiguration就相当于@Configuration。

进入@Configuration，发现@Configuration核心是@Component，说明Spring的配置类也是Spring的一个组件。

### [@EnableAutoConfiguration](#enableautoconfiguration)

继续看@EnableAutoConfiguration，这个注解是开启自动配置的功能，源码如下：

可以看到它是由 @AutoConfigurationPackage，@Import(EnableAutoConfigurationImportSelector.class)这两个而组成的，

#### [@AutoConfigurationPackage](#autoconfigurationpackage)

先看@AutoConfigurationPackage，这是为了让包中的类以及子包中的类能够被自动扫描到spring容器中。

源码如下：

可以看到，这里使用@Import 来给Spring容器中导入一个组件，这里导入的是Registrar.class。来看下这个Registrar：

就是通过以上这个方法获取扫描的包路径，可以debug查看具体的值：
![](/imported/markdown/2025-05-17-markdown-64b1a66e-深度揭秘springboot自动装配的实现原理/images/a977aa508d7d-202405051211289.webp)
那metadata是什么呢，可以看到是标注在@SpringBootApplication注解上的DemoApplication，也就是主配置类Application：
![](/imported/markdown/2025-05-17-markdown-64b1a66e-深度揭秘springboot自动装配的实现原理/images/3efb7cfd8c20-202405051211130.webp)
其实就是将主配置类（即@SpringBootApplication标注的类）的所在包及子包里面所有组件扫描加载到Spring容器。因此要把DemoApplication放在项目的最高级中（最外层目录）。

#### [@Import(AutoConfigurationImportSelector.class)](#import-autoconfigurationimportselector-class)

看看注解@Import(AutoConfigurationImportSelector.class)，@Import注解就是给Spring容器中导入一些组件，这里传入了一个组件的选择器:AutoConfigurationImportSelector。
![](/imported/markdown/2025-05-17-markdown-64b1a66e-深度揭秘springboot自动装配的实现原理/images/d3de293cc572-202405051211647.webp)
可以从图中看出AutoConfigurationImportSelector 继承了 DeferredImportSelector 继承了 ImportSelector，ImportSelector有一个方法为：selectImports。将所有需要导入的组件以全类名的方式返回，这些组件就会被添加到容器中。

这里会给容器中导入 自动配置类（xxxAutoConfiguration），也就是给容器中导入这个场景需要的所有组件，并配置好这些组件。
![](/imported/markdown/2025-05-17-markdown-64b1a66e-深度揭秘springboot自动装配的实现原理/images/b0e4362c4850-202501191149125.jpg)
有了自动配置类，就免去了手动编写配置注入功能组件等的工作。

那是如何获取到这些配置类的呢，看看下面这个方法：

可以看到getCandidateConfigurations()这个方法，他的作用就是引入系统已经加载好的一些类，那么到底是那些类呢：

会从META-INF/spring.factories中获取资源，然后通过Properties加载资源：

可以知道SpringBoot在启动的时候从类路径下的META-INF/spring.factories中获取EnableAutoConfiguration指定的值，将这些值作为自动配置类导入到容器中，自动配置类就生效，帮我们进行自动配置工作。以前需要自己配置的东西，自动配置类都帮我们完成了。

如下图可以发现Spring常见的一些类已经自动导入。
![](/imported/markdown/2025-05-17-markdown-64b1a66e-深度揭秘springboot自动装配的实现原理/images/0bbb53d6edbc-202405051212942.webp)
### [@ComponentScan](#componentscan)

接下来看@ComponentScan注解，@ComponentScan(excludeFilters = { @Filter(type = FilterType.CUSTOM, classes = TypeExcludeFilter.class), @Filter(type = FilterType.CUSTOM, classes = AutoConfigurationExcludeFilter.class) })，这个注解就是扫描包，然后放入spring容器。

总结下@SpringbootApplication：就是说，他已经把很多东西准备好，具体是否使用取决于我们的程序或者说配置。

### [小结](#小结)

总的来说，SpringBoot的自动装配原理就是 通过`@EnableAutoConfiguration`注解在类路径的META-INF/spring.factories文件中找到所有的对应配置类，然后将这些自动配置类加载到spring容器中

## [run方法](#run方法)

来看下在执行run方法到底有没有用到哪些自动配置的东西，点进run：

那我们关注的就是 refreshContext(context); 刷新context，我们点进来看。

继续点进refresh(context);

会调用 ((AbstractApplicationContext) applicationContext).refresh();方法，点进来看：

由此可知，就是一个spring的bean的加载过程。继续来看一个方法叫做 onRefresh()：

在这里并没有直接实现，找他的具体实现：
![](/imported/markdown/2025-05-17-markdown-64b1a66e-深度揭秘springboot自动装配的实现原理/images/49277cae814d-202405051212682.webp)
比如Tomcat跟web有关，可以看到有个ServletWebServerApplicationContext：

可以看到有一个createWebServer()方法，用于创建web容器，而Tomcat不就是web容器。

那是如何创建的呢：

factory.getWebServer(getSelfInitializer())，显然是通过工厂的方式创建的。

可以看到 它是一个接口，为什么会是接口。因为不止是Tomcat一种web容器，可以看到还有Jetty
![](/imported/markdown/2025-05-17-markdown-64b1a66e-深度揭秘springboot自动装配的实现原理/images/babd584e0ade-202405051212127.webp)
接下来看TomcatServletWebServerFactory：

这块代码，就是要寻找的内置Tomcat，在这个过程当中，可以看到创建Tomcat的一个流程。

也就是：

1. 首先从main找到run()方法，在执行run()方法之前new一个SpringApplication对象

1. 进入run()方法，创建应用监听器SpringApplicationRunListeners开始监听

1. 然后加载SpringBoot配置环境(ConfigurableEnvironment)，然后把配置环境(Environment)加入监听对象中

1. 然后加载应用上下文(ConfigurableApplicationContext)，当做run方法的返回对象

1. 最后创建Spring容器，refreshContext(context)，实现starter自动化配置和bean的实例化等工作。
