{

  "title": "Springboot 常见面试题",
  "has_date": false,
  "description": "SpringBoot基础 什么是 Spring Boot? SpringBoot是一个简化 Spring 应用程序开发的框架，它的主要目标是减少 Spring 应用程序的配置和开发复杂性，使我们能够更快地构建、测试和部署 Spring 应用。简单来说，它通过提供默认配置、自动化配置和嵌入式服务器等功",
  "tags": [
    "面试",
    "框架",
    "Spring Boot",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "interview/framework/springboot - Springboot 常见面试题.md"

}

---

## [SpringBoot基础](#springboot基础)

### [什么是 Spring Boot?](#什么是-spring-boot)

SpringBoot是一个简化 Spring 应用程序开发的框架，它的主要目标是减少 Spring 应用程序的配置和开发复杂性，使我们能够更快地构建、测试和部署 Spring 应用。简单来说，它通过提供默认配置、自动化配置和嵌入式服务器等功能，简化了传统Spring 应用的繁琐配置过程。有人将一些依赖关系、默认配置都梳理好了，我们直接一个引用就搞定了，这就是它的本质。

### [Springboot的优点](#springboot的优点)

- 内置Web容器：内置servlet容器，不需要在服务器部署 tomcat。只需要将项目打成 jar 包，使用 java -jar xxx.jar一键式启动项目

- 内置Starter和自动配置：SpringBoot提供了starter，把常用库聚合在一起，简化复杂的环境配置，快速搭建spring应用环境

- 零XML配置： Spring Boot采用JavaConfig的方式进行开发，不需要编写大量的XML配置文件。这种零XML的开发方式让开发更加简洁和可读，同时提高了可维护性。

- 微服务支持： Spring Boot与Spring Cloud结合使用，可以轻松快速构建和部署微服务架构。

- 依赖版本管理： Spring Boot帮助开发人员管理了常用第三方依赖的版本，防止出现版本冲突问题。这样，您可以更专注于业务逻辑，而不用担心依赖的版本兼容性。

- 监控和管理： Spring Boot自带了监控功能，包括应用程序运行状况监控、内存使用情况、线程池状态、HTTP请求统计等。此外，Spring Boot还提供了优雅关闭应用程序的方式，使得应用程序的管理更加便捷。

- SpringBoot总结就是使编码变简单、配置变简单、部署变简单、监控变简单等等

### [Spring Boot 需要独立的容器运行吗？](#spring-boot-需要独立的容器运行吗)

可以不需要，内置了 Tomcat/ Jetty 等容器。

### [Javaweb、spring、springmvc和springboot有什么区别，都是做什么用的？](#javaweb、spring、springmvc和springboot有什么区别-都是做什么用的)

JavaWeb是 Java 语言的 Web 开发技术，主要用于开发 Web 应用程序，包括基于浏览器的客户端和基于服务器的 Web 服务器。

Spring是一个轻量级的开源开发框架，主要用于管理 Java 应用程序中的组件和对象，并提供各种服务，如事务管理、安全控制、面向切面编程和远程访问等。它是一个综合性框架，可应用于所有类型的 Java 应用程序。

SpringMVC是 Spring 框架中的一个模块，用于开发 Web 应用程序并实现 MVC（模型-视图-控制器）设计模式，它将请求和响应分离，从而使得应用程序更加模块化、可扩展和易于维护。

Spring Boot是基于 Spring 框架开发的用于开发 Web 应用程序的框架，它帮助开发人员快速搭建和配置一个独立的、可执行的、基于 Spring 的应用程序，从而减少了繁琐和重复的配置工作。

综上所述，JavaWeb是基于 Java 语言的 Web 开发技术，而 Spring 是一个综合性的开发框架，SpringMVC用于开发 Web 应用程序实现 MVC 设计模式，而 Spring Boot 是基于 Spring 的 Web 应用程序开发框架。

### [运行 SpringBoot 有哪几种方式？](#运行-springboot-有哪几种方式)

相关原理可以查看：两种方式启动原理

1. IDEA中main函数启动

1. 用 Maven/Gradle 插件运行

1. java -jar XXX.jar

### [Spring Boot 打成的 jar 和普通的 jar 有什么区别 ?](#spring-boot-打成的-jar-和普通的-jar-有什么区别)

- Spring Boot 项目最终打包成的 jar 是可执行 jar，这种 jar 可以直接通过 `java -jar xxx.jar` 命令来运行，这种 jar 不可以作为普通的 jar 被其他项目依赖，即使依赖了也无法使用其中的类。

- Spring Boot 的 jar 无法被其他项目依赖，主要还是他和普通 jar 的结构不同。普通的 jar 包，解压后直接就是包名，包里就是我们的代码，而 Spring Boot 打包成的可执行 jar 解压后，在 `\BOOT-INF\classes` 目录下才是我们的代码，因此无法被直接引用。如果非要引用，可以在 pom.xml 文件中增加配置，将 Spring Boot 项目打包成两个 jar，一个可执行，一个可引用。

### [为什么SpringBoot的jar可以直接运行？](#为什么springboot的jar可以直接运行)

Spring Boot的可执行JAR文件之所以可以直接运行，原因如下：

1. Spring Boot提供了一个Maven插件（spring-boot-maven-plugin），用于将应用程序打包成可执行的JAR文件。通过执行mvn clean package等命令，可以轻松生成可执行JAR。

1. 打包生成的JAR文件通常是"Fat JAR"或"Uber JAR"，这意味着它包含了应用程序的所有依赖项，包括第三方库和Spring Boot框架本身。这样，JAR文件就成了一个自包含的单一文件。

1. JAR文件包含一个名为MANIFEST.MF的清单文件，其中包含了关于JAR文件的元数据信息。其中，主要的信息是Main-Class，它指定了启动应用程序的主类。

1. Spring Boot的可执行JAR文件通常由JarLauncher类启动。JarLauncher负责创建一个类加载器（LaunchedURLClassLoader），加载boot-lib目录下的JAR文件，包括Spring Boot loader相关的类。然后，它在一个新线程中启动应用程序的Main方法，实现应用程序的启动。、

1. 当执行Main方法最终会加载Spring容器、进而创建内嵌Tomcat进行阻塞线程使我们jar包完成web应用的启动

### [SpringBoot 常用的 Starter 有哪些？](#springboot-常用的-starter-有哪些)

1. spring-boot-starter-web ：提供 Spring MVC + 内嵌的 Tomcat 。

1. spring-boot-starter-data-jpa ：提供 Spring JPA + Hibernate 。

1. spring-boot-starter-data-Redis ：提供 Redis 。

1. mybatis-spring-boot-starter ：提供 MyBatis 。

### [SpringBoot 中的 starter 到底是什么 ?](#springboot-中的-starter-到底是什么)

- 个人理解SpringBoot就是由各种Starter组合起来的，我们自己也可以开发Starter

- 在sprinBoot启动时由@SpringBootApplication注解会自动去maven中读取每个starter中的spring.factories文件,该文件里配置了所有需要被创建spring容器中的bean，并且进行自动配置把bean注入SpringContext中 //（SpringContext是Spring的配置文件）

- 首先它提供了一个自动化配置类，一般命名为 XXXAutoConfiguration，在这个配置类中通过条件注解来决定一个配置是否生效（条件注解就是 Spring 中原本就有的），然后它还会提供一系列的默认配置，也允许开发者根据实际情况自定义相关配置，然后通过类型安全的属性(spring.factories)注入将这些配置属性注入进来，新注入的属性会代替掉默认属性。正因为如此，很多第三方框架，我们只需要引入依赖就可以直接使用了。当然，开发者也可以自定义 Starter

### [SpringBoot如何自定义Starter](#springboot如何自定义starter)

在开发分布式Springboot项目时， 自定义Starter是一定会用到的。以下是创建自定义Spring Boot Starter的基本步骤：

1. 创建项目结构： 创建一个Maven或Gradle项目，确保项目结构符合标准的约定。通常，项目结构包括src/main/java用于存放Java代码和src/main/resources用于存放资源文件。

1. 编写自动配置类： 创建一个自动配置类，该类负责配置自定义Starter的功能。在自动配置类上使用@Configuration注解，并通过其他注解如@ConditionalOnClass、@ConditionalOnProperty等来定义条件，以确保只有在满足特定条件时才会应用配置。

1. 提供属性配置： 如果您的Starter需要配置属性，可以在src/main/resources/application.properties或src/main/resources/application.yml中定义属性。这些属性可以在自动配置类中使用@Value注解注入。

1. 创建META-INF/spring.factories文件： 在项目的资源目录中创建META-INF/spring.factories文件。在这个文件中，注册您的自动配置类，以便Spring Boot能够自动识别和加载它。

1. 定义Starter依赖： 在自定义Starter的pom.xml文件中，定义Spring Boot的核心依赖以及您的Starter所依赖的其他库。

1. 测试和文档： 编写单元测试和集成测试，以确保自定义Starter的功能和配置正确。同时，提供详细的文档和示例，以便用户能够正确配置和使用您的Starter。

1. 发布到仓库： 将自定义Starter打包，并发布到Maven中央仓库或私有仓库，以便其他项目可以引入和使用。

自定义一个Spring Boot Starter需要遵循上述步骤，其中**创建META-INF/spring.factories文件是关键**，因为它告诉Spring Boot如何自动装配您的功能。这样，其他项目可以方便地引入您的Starter，实现功能的快速集成。

### [SpringBoot与SpringCloud 区别](#springboot与springcloud-区别)

SpringBoot是快速开发的Spring框架，SpringCloud是完整的微服务框架，SpringCloud依赖于SpringBoot。

## [SpringBoot注解](#springboot注解)

### [Spring Boot 的核心注解是哪个？](#spring-boot-的核心注解是哪个)

启动类上面的注解是@SpringBootApplication，它也是 Spring Boot 的核心注解，主要组合包含了以下 3 个注解：

- @SpringBootConfiguration：组合了 @Configuration 注解，实现配置文件的功能。

- @EnableAutoConfiguration：打开自动配置的功能，也可以关闭某个自动配置的选项，如关闭数据源自动配置功能： @SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })。

- @ComponentScan：Spring组件扫描。

### [有哪些常用的SpringBoot注解？](#有哪些常用的springboot注解)

- @SpringBootApplication：这个注解是Spring Boot最核心的注解，用在 Spring Boot的主类上，标识这是一个 Spring Boot 应用，用来开启 Spring Boot 的各项能力

- @SpringBootConfiguration：组合了 @Configuration 注解，实现配置文件的功能。

- @EnableAutoConfiguration：打开自动配置的功能，也可以关闭某个自动配置的选项，如关闭数据源自动配置功能： @SpringBootApplication(exclude = { DataSourceAutoConfiguration.class })。

- @ComponentScan：Spring组件扫描。

- @Repository：用于标注数据访问组件，即DAO组件。

- @Service：一般用于修饰service层的组件

-
**@RestController**：用于标注控制层组件(如struts中的action)，表示这是个控制器bean,并且是将函数的返回值直 接填入HTTP响应体中,是REST风格的控制器；它是@Controller和@ResponseBody的合集。

-
**@ResponseBody**：表示该方法的返回结果直接写入HTTP response body中

-
**@Component**：泛指组件，当组件不好归类的时候，我们可以使用这个注解进行标注。

-
**@Bean**：相当于XML中的`&lt;bean&gt;&lt;/bean&gt;`,放在方法的上面，而不是类，意思是产生一个bean,并交给spring管理。

-
**@AutoWired**：byType方式。把配置好的Bean拿来用，完成属性、方法的组装，它可以对类成员变量、方法及构造函数进行标注，完成自动装配的工作。

-
**@Qualifier**：当有多个同一类型的Bean时，可以用@Qualifier("name")来指定。与@Autowired配合使用

-
**@Resource(name="name",type="type")**：没有括号内内容的话，默认byName。与@Autowired干类似的事。

-
**@RequestMapping**：RequestMapping是一个用来处理请求地址映射的注解；提供路由信息，负责URL到Controller中的具体函数的映射，可用于类或方法上。用于类上，表示类中的所有响应请求的方法都是以该地址作为父路径。

-
**@RequestParam**：用在方法的参数前面。

-
**@RequestBody**：将 HTTP 请求体中的数据绑定到方法参数上。Spring 会将JSON、XML或其他格式的请求体转换为Java 对象，并将其传递给控制器方法的参数。

- @PathVariable：Spring MVC 中用于从URI 模板中提取变量值的注解。它的主要作用是在处理 HTTP请求时，从请求的URL 路径中捕获变量，并将其绑定到控制器方法的参数上

- @Scope：用于声明一个Spring`Bean`实例的作用域

- @Primary：当同一个对象有多个实例时，优先选择该实例。

- @PostConstruct： 用于修饰方法，当对象实例被创建并且依赖注入完成后执行，可用于对象实例的初始化操作。

- @PreDestroy：用于修饰方法，当对象实例将被Spring容器移除时执行，可用于对象实例持有资源的释放。

- @EnableTransactionManagement：启用Spring基于注解的事务管理功能，需要和`@Configuration`注解一起使用。

- @Transactional：表示方法和类需要开启事务，当作用与类上时，类中所有方法均会开启事务，当作用于方法上时，方法开启事务，方法上的注解无法被子类所继承。

- @ControllerAdvice：常与`@ExceptionHandler`注解一起使用，用于捕获全局异常，能作用于所有controller中。

- @ExceptionHandler：修饰方法时，表示该方法为处理全局异常的方法。

- @Profile：用于定义一组 Bean 的配置文件所属的环境，比如 dev 通常表示开发环境，prod 表示生产环境

### [@Validated 和 @Valid 注解有什么区别?](#validated-和-valid-注解有什么区别)

@Validated 和 @Valid 都是用于在 Spring 中执行对象验证的注解，但它们的使用场景和特性有一些区别：

- @Validated：这是标准的 Java Bean Vlidation注解，来自javax.vlidation注解。它通常用于方法参数或类的字段上，以触发基于注解的验证规则，如(@NotNull、@Size等)；在Sping中，它可以用于验证单个对象或嵌套对象。

- @Valid：这是 Sping 特有的注解，来自org.springframework.vlidation.annotation.Vlidated包，它的主要作用是支持分组验证(Group Vlidation)，允许开发者根据不同的场景定义不同的验证逻辑。它也可以用在类级别、方法参数上，触发不同验证组的规则。

### [@Value注解的原理](#value注解的原理)

在 Spring 框架中，@Vàlue 注解用于注入外部化的配置值到 Spring 管理的 Bean 中。通过 @Value 注解，可以将属性文件、环境变量、系统属性等外部资源中的值注入到 Spring Bean 的字段、方法参数或构造函数参数中。

@Value的解析就是在bean初始化阶段。BeanPostProcessor定义了bean初始化前后用户可以对bean进行操作的接口方法，它的一个重要实现类`AutowiredAnnotationBeanPostProcessor`为bean中的@Autowired和@Value注解的注入功能提供支持。

### [@PropertySource 注解的作用是什么?](#propertysource-注解的作用是什么)

是 Spring 中用于加载外部属性文件(如.properties 文件)的注解。

它的主要作用是让 Spring 应用程序可以从外部的属性文件中读取配置，并将这些属性注入到 Spring 的 Environment 中，从而实现应用的外部化配置，使得应用程序在不同环境下更容易管理和维护。方便通过@Value 或 Environment 对象获取属性值

### [@Scheduled 注解的作用是什么?](#scheduled-注解的作用是什么)

这个注解用于在 Spring 应用中定时执行方法。它可以将某个方法标记为一个定时任务，并根据设定的时间间隔、固定速率、或 Cron 表达式来定时触发该方法的执行。

主要作用:

- 定时任务执行： @Scheduled 注解允许开发者定义一个方法，该方法会按照指定的时间规则定期执行。

- 支持多种时间配置：支持固定延迟、固定速率以及基于Cron 表达式的任务调度。

### [@Cacheable 和 @CacheEvict 注解的作用是什么?](#cacheable-和-cacheevict-注解的作用是什么)

@Cacheable 和 @CacheEvict 是Spring中用于缓存操作的两个重要注解，主要用于提高系统性能，通过减少对数据库等外部资源的频繁访问。

- @Cacheable：用于将方法的返回结果缓存起来。下次再调用相同参数的方法时，直接从缓存中获取结果，而不是重新执行该方法。

- @CacheEvict：用于从缓存中移除一项或多项数据，通常在更新或删除操作时使用，确保缓存中的数据保持一致性。

### [@Conditional 注解的作用是什么?](#conditional-注解的作用是什么)

作用于有条件地装配 Bean。

可以根据特定的条件来决定某个 Bean 是否应该被加载到 Spring 容器中。例如可以根据环境(如开发、测试、生产)或特定上下文条件动态装配 Bean，实现动态加载

主要作用:

- 有条件地加载 Bean：@Conditional 根据某个条件来決定某个 Bean 是否需要注入到 Spring 容器中。条件可以是操作系统类型、类路径是否存在某个类、某个属性的值等。

- 实现动态配置：可以根据环境(如开发、测试、生产)或特定上下文条件动态装配 Bean，避免不必要的 Bean 被加载。

### [@Lazy 注解的作用是什么?](#lazy-注解的作用是什么)

@Lazy 的两种用法：

- 和注解 @Component 或 @Bean 一起使用，可以延迟 Bean 的创建时机，当用到这个 Bean 的时候(依赖注入、从 Beanfactory直接获取)，才进行创建

- 和注解 @Autowire 一起使用，Spring 将注入一个代理类

### [@EventListener 注解的作用是什么?](#eventlistener-注解的作用是什么)

通过标注在方法上， @EventListener 可以使方法自动监听特定类型的事件，它用于监听和处理事件。并在事件发布时触发执行，它提供了一种松耦合的方式来处理应用中的事件，避免事件发布者和监听者之间的直接依赖关系，

使用场景：

- 当系统中某个状态变化时触发特定操作。

- 日志记录、监控系统、通知系统等需要响应事件的模块。

### [@Async 注解的原理是什么?](#async-注解的原理是什么)

@Async 注解的核心原理是基于Spring AOP的动态代理机制，结合线程池实现异步任务调度，通过合理的线程池配置和异常处理，可以高效地实现异步操作。

### [@Async 什么时候会失效?](#async-什么时候会失效)

@Async失效的主要原因包括内部调用绕过代理、方法非 public、未启用异步支持、返回值类型不匹配、异常处理不当、线程池配置错误以及对象未被 Spring 管埋等

1. 内部调用：@Async 依赖于 Spring 的动态代理机制(AOP)，而内部调用会绕过代理对象，直接调用原始方法。解决如下：

  - 将异步方法提取到独立的Bean中。

  - 使用 Aopcontext.currentProxy()获取代理对象调用。

  - 注入自身Bean并通过其调用异步方法

1. 非公共方法：Spring AOP 默认只对 public方法生效，非 public 方法不会被代理解决。需要确保被@Async标注的方法是public.

1. 没有启用异步支持：@Async 需要显式启用异步功能，否则 Spring 不会为其生成代理解决。在 Spring Boot 应用的主类或配置类上添加 @EnableAsync 注解。

1. 方法返回值不匹配：@Async 对返回值类型有一定要求，某些情况下可能导致行为异常。需要确保返回值类型符合 @Async 的要求。(返回值为 void、CompletableFuture等)Future

1. 异常处理不当：异步方法中的异常不会直接传播到调用方，可能导致问题被忽略。需要使用 try-catch 捕获异常或者配置全局异常处理器

1. 自定义线程池配置错误：如果自定义线程池配置不当，可能导致异步任务无法正常执行。比如没有正确注册或配置线程池。正确配置并注册 TaskExecutor 就可以了。

1. Spring上下文未加载：@Async 依赖 Spring 容器管理的 Bean，如果对象没有被 Spring 管理，那么代理机制就会失效。确保 Bean 由 Spring 容器管理，不要手动去 new。

### [什么是 JavaConfig？](#什么是-javaconfig)

Spring JavaConfig 是 Spring 社区的产品，Spring 3.0引入了他，它提供了配置 Spring IOC 容器的纯Java 方法。因此它有助于避免使用 XML 配置。

使用 JavaConfig 的优点在于：

- 面向对象的配置。由于配置被定义为 JavaConfig 中的类，因此用户可以充分利用 Java 中的面向对象功能。一个配置类可以继承另一个，重写它的@Bean 方法等。

- 减少或消除 XML 配置。基于依赖注入原则的外化配置的好处已被证明。但是，许多开发人员不希望在 XML 和 Java 之间来回切换。JavaConfig 为开发人员提供了一种纯 Java 方法来配置与 XML 配置概念相似的 Spring 容器。从技术角度来讲，只使用 JavaConfig 配置类来配置容器是可行的，但实际上很多人认为将JavaConfig 与 XML 混合匹配是理想的。

- 类型安全和重构友好。JavaConfig 提供了一种类型安全的方法来配置 Spring容器。由于 Java5.0 对泛型的支持，现在可以按类型而不是按名称检索 bean，不需要任何强制转换或基于字符串的查找。

常用的Java config：

- @Configuration：在类上打上写下此注解，表示这个类是配置类

- @ComponentScan：在配置类上添加 @ComponentScan 注解。该注解默认会扫描该类所在的包下所有的配置类，相当于之前的 `&lt;context:component-scan &gt;`。

- @Bean：bean的注入：相当于以前的`&lt; bean id="objectMapper"class="org.codehaus.jackson.map.ObjectMapper" /&gt;`

- @EnableWebMvc：相当于xml的`&lt;mvc:annotation-driven &gt;

- @ImportResource： 相当于xml的 `&lt; import resource="applicationContextcache.xml"&gt;`

## [实现原理](#实现原理)

### [SpringBoot为什么默认使用CGLIB](#springboot为什么默认使用cglib)

SpringBoot默认使用CGLIB 原因如下：

- 无需接口： CGLIB能够代理那些没有实现接口的类，而JDK动态代理只能代理实现了接口的类。这使得Spring Boot可以更灵活地使用代理，而无需依赖于接口。

- AOP支持： Spring Boot广泛使用AOP（面向切面编程）来处理日志、事务、安全性等横切关注点。CGLIB更适合创建AOP代理，因为它可以代理普通的类而不仅仅是接口，在开发中如果通过反射获得代理目标方法的注解，如果用JDK动态代理将导致无法获取。

- 可以代理本类方法：这意味着即使在同一个类中调用了另一个方法，仍然可以触发代理的行为。这对于某些特定的AOP需求非常有用，因为它允许您在同一类中的方法之间应用切面。这种能力被称为"自我调用"或"内部调用"的代理。

- 方法调用性能： 一旦代理对象创建完成，实际的方法调用性能可能会因代理方式而异。在JDK 1.8之后，JDK动态代理的方法调用性能相对较好，但CGLIB仍然可能更快，因为CGlib是直接调用父类方法即目标方法，无需像JDK代理还要通过反射进行内部方法栈调用才能到目标方法。

### [SpringBoot的启动原理？](#springboot的启动原理)
![](/imported/markdown/undated-markdown-e4dd8299-springboot-常见面试题/images/3a0c6b31e1dd-202509072036055.png)

1. 启动 main()方法：应用从 main()方法启动，并通过SpringApplication.run()引|导应用启动。

1. 创建SpringApplication：应用会创建 springApplication 对象，推断应用类型、设置初始化器、设置启动监听器、、确定主应用类。

1. 准备环境(ConfigurableEnvironment)：Spring Boot 在启动过程中准备应用环境，加载配置文件、系统环境变量以及命令行参数。

1. 创建井刷新 ApplicationContext：创建应用上下文，加载配置类和自动配置类，注册 Bean 并执行依赖注入等初始化操作。

1. 在刷新上下文时启动嵌入式 Web 服务器“对于 Web 应用，Spring Boot 会自动启动嵌入式 Web 容器(如 Tomcat)，并注册相关的 Servlet 和 filter。

1. 发布应用己启动事件：对应监听 stated 事件逻辑会被触发。

1. 执行CommandLineRunner和ApplicationRunner：在应用启动完成后，执行实现了commandLineRunner和ApplicationRunner接口的初始化逻辑。

1. 发布 ready 事件、应用启动完成：触发 ApplicationReadyEvent，应用进入运行状态，处理业务请求或任务

简单版：

1. 创建Spring容器

1. 加载自动配置类

1. 启动内置的Tomcat

### [SpringBoot 是如何通过 main 方法启动 web 项目的?](#springboot-是如何通过-main-方法启动-web-项目的)

SpringBoot 应用的启动流程都封装在 SpringApplication.run方法中，它的大部分逻辑都是复用 Spring 启动的流程，只不过在它的基础上做了大量的扩展在启动的过程中有一个刷新上下文的动作，这个方法内会触发 webserver 的创建，此时就会创建并启动内嵌的 web服务，默认的 web 服务就是 tomcat

Spring Boot 的启动过程几个核心步骤：

1. SpringApplication.run():这是启动的入口，它会创建 Spring 应用上下文，并执行自动配置。

1. 创建应用上下文：为 Web 应用创建 AnnotationConfigServletWebServerApplicationContext 上下文

1. 启动内嵌 Web 服务器：在 refreshContext0) 阶段启动内嵌的 Web 服务器(如Tomcat)。

1. 自动配置：通过 @EnableAutoConfiquration 自动配置各种组件，如 DispatcherServlet

1. 请求处理：内嵌的 DispatcherServet 负责处理 HTTP 请求。

### [自动配置原理](#自动配置原理)

在 application.properties 中设置属性 debug=true，可以在控制台查看已启用和未启用的自动配置。

@SpringBootApplication是@Configuration、@EnableAutoConfiguration和@ComponentScan的组合。

@Configuration表示该类是Java配置类。

@ComponentScan开启自动扫描符合条件的bean（添加了@Controller、@Service等注解）。

@EnableAutoConfiguration会根据类路径中的jar依赖为项目进行自动配置，比如添加了`spring-boot-starter-web`依赖，会自动添加Tomcat和Spring MVC的依赖，然后Spring Boot会对Tomcat和Spring MVC进行自动配置（spring.factories EnableAutoConfiguration配置了`WebMvcAutoConfiguration`）。

EnableAutoConfiguration主要由 @AutoConfigurationPackage，@Import(EnableAutoConfigurationImportSelector.class)这两个注解组成的。

@AutoConfigurationPackage用于将启动类所在的包里面的所有组件注册到spring容器。

@Import 将EnableAutoConfigurationImportSelector注入到spring容器中，EnableAutoConfigurationImportSelector通过SpringFactoriesLoader从类路径下去读取META-INF/spring.factories文件信息，此文件中有一个key为org.springframework.boot.autoconfigure.EnableAutoConfiguration，定义了一组需要自动配置的bean。

这些配置类不是都会被加载，会根据xxxAutoConfiguration上的@ConditionalOnClass等条件判断是否加载，符合条件才会将相应的组件被加载到spring容器。（比如mybatis-spring-boot-starter，会自动配置sqlSessionFactory、sqlSessionTemplate、dataSource等mybatis所需的组件）

全局配置文件中的属性如何生效，比如：server.port=8081，是如何生效的？

@ConfigurationProperties的作用就是将配置文件的属性绑定到对应的bean上。全局配置的属性如：server.port等，通过@ConfigurationProperties注解，绑定到对应的XxxxProperties bean，通过这个 bean 获取相应的属性（serverProperties.getPort()）。

简单总结如下：

- 主要是Spring Boot的启动类上的核心注解SpringBootApplication注解主配置类，有了这个主配置类启动时就会为SpringBoot开启一个@EnableAutoConfiguration注解自动配置功能。

- @EnableAutoConfiguration引入了@Import&lt;这意味着它会导入其他配置类，这些配置类包含了Spring Boot自动配置的逻辑。

- 当Spring容器启动时，会解析@Import注解，并加载相应的配置。

- 接着就会：

  - 读取META-INF/spring.factories文件：从配置文件META_INF/Spring.factories加载可能用到的自动配置类

  - 过滤出AutoConfigurationClass：去重，并将exclude和excludeName属性携带的类排除

  - 条件化加载：过滤，将满足条件（@Conditional）的自动配置类返回

### [实现自动配置](#实现自动配置)

实现当某个类存在时，自动配置这个类的bean，并且可以在application.properties中配置bean的属性。

（1）新建Maven项目spring-boot-starter-hello，修改pom.xml如下：

（2）属性配置

（3）自动配置类

1. @EnableConfigurationProperties 注解开启属性注入，将带有@ConfigurationProperties 注解的类注入为Spring 容器的 Bean。

1. 当 HelloService 在类路径的条件下。

1. 当设置 hello=enabled 的情况下，如果没有设置则默认为 true，即条件符合。

1. 当容器没有这个 Bean 的时候。

（4）注册配置

想要自动配置生效，需要注册自动配置类。在 src/main/resources 下新建 META-INF/spring.factories。添加以下内容：

"\"是为了换行后仍然能读到属性。若有多个自动配置，则用逗号隔开。

（5）使用starter

在 Spring Boot 项目的 pom.xml 中添加：

运行类如下：

在项目中没有配置 HelloService bean，但是我们可以注入这个bean，这是通过自动配置实现的。

在 application.properties 中添加 debug 属性，运行配置类，在控制台可以看到：

可以在 application.properties 中配置 msg 的内容：

## [SpringBoot的使用](#springboot的使用)

### [Spring Boot 中application.properties 和 application.yml 的区别是什么?](#spring-boot-中application-properties-和-application-yml-的区别是什么)

它们两者的区别就在于书写格式，对配置而言效果是一样的，就是个人偏好问题。

- application.properties 使用键值对配置，键和值之间用等号或冒号分隔

- application.yml 使用 YAML (YAML Aint Markup Language)格式，具有层级结构，使用缩进表示嵌套关系。适合复杂配置，阅读性更佳。

### [SpringBoot为什么要禁止循环依赖](#springboot为什么要禁止循环依赖)

循环依赖大家都知道，也被折磨过，在 SpringBoot2.6.0的版本默认禁止了循环依赖，如果程序中出现循环依赖就会报错。

当然并没有一锤子打死，也提供了开启允许循环依赖的配置，只需要在配置文件中开启即可：

那SpringBoot为什么要要禁止呢？我们都知道Spring解决循环依赖的方式是通过三级缓存，光学这个三级缓存我们就煞费苦心，其实说白了他是一种给程序员擦屁股的行为.

其实对象之间的关系如果是互相依赖是一种不合理的设计，避免你做出这种不合理的依赖，SpringBoot进而禁止循环依赖。

### [SpringBoot可以同时处理多少请求？](#springboot可以同时处理多少请求)

详情请看Tomcat线程池详解

SpringBoot默认的内嵌容器是Tomcat，也就是我们的程序实际上是运行在Tomcat里的。所以与其说SpringBoot可以处理多少请求，到不如说Tomcat可以处理多少请求。

在SpringBoot中处理请求数量相关的参数有四个：

- server.tomcat.threads.min-spare：最少的工作线程数，默认大小是10。该参数相当于长期工，如果并发请求的数量达不到10，就会依次使用这几个线程去处理请求。

- server.tomcat.threads.max：最多的工作线程数，默认大小是200。该参数相当于临时工，如果并发请求的数量在10到200之间，就会使用这些临时工线程进行处理。

- server.tomcat.max-connections：最大连接数，默认大小是8192。表示Tomcat可以处理的最大请求数量，超过8192的请求就会被放入到等待队列。

- server.tomcat.accept-count：等待队列的长度，默认大小是100。

### [Spring Boot 支持哪些日志框架？](#spring-boot-支持哪些日志框架)

Spring Boot 支持 Java Util Logging, Log4j2, Lockback 作为日志框架，如果你使用 Starters 启动器，Spring Boot 将使用 Logback 作为默认日志框架，但是不管是那种日志框架他都支持将配置文件输出到控制台或者文件中。

### [SpringBoot事务的使用](#springboot事务的使用)

SpringBoot的事物很简单，首先使用注解EnableTransactionManagement开启事物之后，然后在Service方法上添加注解Transactional便可。

### [Async异步调用方法](#async异步调用方法)

在SpringBoot中使用异步调用是很简单的，只需要在方法上使用@Async注解即可实现方法的异步调用。 注意：需要在启动类加入@EnableAsync使异步调用@Async注解生效。

### [为啥不建议用BeanUtils.copyProperties拷贝数据？](#为啥不建议用beanutils-copyproperties拷贝数据)

- 属性类型不一致导致拷贝失败

  - 同一属性的类型不同：例如ID，可能在Source类中定义的类型为Long，在Target类中定义的类型为String，此时如果使用BeanUtils.copyProperties进行拷贝，就会出现拷贝失败的现象，导致对应的字段为null

  - 同一字段分别使用包装类型和基本类型：例如Source类中定义为Long，在Target类中定义为long,在没有传递实际值的时候，会出现异常

- null值覆盖导致数据异常：Source数据里面如果某些字段有null值存在，但是对应的需要被拷贝过去的数据的相同字段的值并不为null，如果直接使用 BeanUtils.copyProperties 进行数据拷贝，就会出现Source数据的null值覆盖Target的字段，导致原有的数据失效。

- 内部类数据无法成功拷贝：内部类数据无法正常拷贝，即使类型和字段名均相同也无法拷贝成功

- BeanUtils.copyProperties是浅拷贝：一旦在拷贝后修改了原始对象的引用类型的数据，就会导致拷贝数据的值发生异常，这种问题排查起来也比较困难。

- 底层实现为反射拷贝效率低

那应该如何解决？

- **手动复制**：手动编写`setter`方法进行属性复制。这种方式虽然代码量较大，但能提供最好的性能和灵活性

- **构造函数或静态工厂方法**：通过构造函数或静态工厂方法来初始化对象的属性，确保对象在创建时就处于合法状态。

- **使用Lombok的@Builder**（推荐）：可以利用`@Builder`注解提供的Builder模式来简化对象创建和属性赋值。

- **ModelMapper或MapStruct**：

  - **ModelMapper**：一个灵活的对象映射库，适合需要处理复杂映射关系的场景。

  - **MapStruct**：一个代码生成库，在编译时生成类型安全且高性能的映射代码，适合需要高性能的场景。

### [如何在 Spring Boot 启动的时候运行一些特定的代码？](#如何在-spring-boot-启动的时候运行一些特定的代码)

类似的问题：希望将数据库中已有的固定内容，打入到 Redis 缓存中，请问如何处理?

- 实现接口 ApplicationRunner 或者 CommandLineRunner 的run方法，这两个接口实现方式一样，它们都只提供了一个 run 方法

- 使用 @PostConstruct 注解：在服务类中通过@PostConstruct注解标记初始化方法，在 Bean 创建后立即执行数据加载。

- 使用 InitializingBean 接口：InitializingBean 接口提供了 afterPropertiesSet 方法，用于在 Spring 容器初始化 bean 的属性后，执行特定的初始化逻辑

- 使用 Spring 事件监听器：可以通过监听 Spring 的 ContextRefreshedEvent 期事件，在应用启动时执行特定代码。

- 自定义BeanFactoryPostProcessor和BeanPostProcessor：它们都是 Spring 容器启动给的扩展点，可以在 Spring 容器初始化 bean 之前或之后执行特定逻辑。

- 使用 @Cacheable 注解：通过 @cacheable在首次调用方法时触发缓存写入，但需手动触发首次调用才能完成预加载，

### [Spring Boot 有哪几种读取配置的方式？](#spring-boot-有哪几种读取配置的方式)

简单来看可以有三种：

- 使用 @Value 注解：

- 使用 @ConfigurationProperties 注解：

- 使用 Environment 接口：

### [YAML 配置的优势在哪里 ?](#yaml-配置的优势在哪里)

YAML 配置和传统的 properties 配置相比之下，有这些优势：

- 配置有序

- 简洁明了，支持数组，数组中的元素可以是基本数据类型也可以是对象

缺点就是不支持 @PropertySource 注解导入自定义的 YAML 配置。

### [Spring Boot 是否可以使用 XML 配置 ?](#spring-boot-是否可以使用-xml-配置)

Spring Boot 推荐使用 Java 配置而非 XML 配置，但是 Spring Boot 中也可以使用 XML 配置，通过 @ImportResource 注解可以引入一个 XML 配置。

### [spring boot 核心配置文件是什么？bootstrap.properties 和application.properties 有何区别 ?](#spring-boot-核心配置文件是什么-bootstrap-properties-和application-properties-有何区别)

单纯做 Spring Boot 开发，可能不太容易遇到 bootstrap.properties 配置文件，但是在结合Spring Cloud 时，这个配置就会经常遇到了，特别是在需要加载一些远程配置文件的时侯。

spring boot 核心的两个配置文件：

- bootstrap (. yml 或者 . properties)：boostrap 由父 ApplicationContext 加载的，比applicaton 优先加载，配置在应用程序上下文的引导阶段生效。一般来说我们在 SpringCloud 配置就会使用这个文件。且 boostrap 里面的属性不能被覆盖；

- application (. yml 或者 . properties)： 由ApplicatonContext 加载，用于 spring boot 项目的自动化配置。

### [Spring Boot 配置文件加载优先级你知道吗?](#spring-boot-配置文件加载优先级你知道吗)

简单优先级：`命令行参数 &gt; JAR包外的 application-{profile}.properties &gt; JAR包外的 aplitcation.properties &gt; JAR包内的 aplication-{profile}.properties &gt; JAR包内的aplication.properties`

注意：当 application.properties和 application.yml 同时存在，同样的参数，最终生效的是 application.properties 中的配置

Spring Boot 在启动时加载配置属性的完整优先级顺序可参考如下的官方文档：从上到下，优先级逐渐降低，即下面的配置，同样的参数会被上面的配置所覆盖
![](/imported/markdown/undated-markdown-e4dd8299-springboot-常见面试题/images/e59e88c3a625-202509072049817.png)
### [什么是 Spring Profiles？](#什么是-spring-profiles)

在项目的开发中，有些配置文件在开发、测试或者生产等不同环境中可能是不同的，例如数据库连接、redis的配置等等。那我们如何在不同环境中自动实现配置的切换呢？Spring给我们提供了profiles机制给我们提供的就是来回切换配置文件的功能

Spring Profiles 允许用户根据配置文件（dev，test，prod 等）来注册 bean。因此，当应用程序在开发中运行时，只有某些 bean 可以加载，而在 PRODUCTION中，某些其他 bean 可以加载。假设我们的要求是 Swagger 文档仅适用于 QA 环境，并且禁用所有其他文档。这可以使用配置文件来完成。Spring Boot 使得使用配置文件非常简单。

### [在 Spring Boot 中如何实现多数据源配置?](#在-spring-boot-中如何实现多数据源配置)

1. 在配置文件中定义多数据源

1. 为每个数据源配置 DataSource、SqlSessionFactory和TransactionManager

1. 为每个数据源配置独立的 Mapper 扫描路径

1. 使用 @Transactional 指定事务管理器

### [SpringBoot多数据源拆分的思路](#springboot多数据源拆分的思路)

先在properties配置文件中配置两个数据源，创建分包mapper，使用@ConfigurationProperties读取properties中的配置，使用@MapperScan注册到对应的mapper包中 。

### [SpringBoot多数据源事务如何管理](#springboot多数据源事务如何管理)

第一种方式是在service层的@TransactionManager中使用transactionManager指定DataSourceConfig中配置的事务。

第二种是使用jta-atomikos实现分布式事务管理。

### [spring-boot-starter-parent 有什么用 ?](#spring-boot-starter-parent-有什么用)

新创建一个 Spring Boot 项目，默认都是有 parent 的，这个 parent 就是 spring-boot-starter-parent，spring-boot-starter-parent 主要有如下作用：

1. 定义了 Java 编译版本。

1. 使用 UTF-8 格式编码。

1. 执行打包操作的配置。

1. 自动化的资源过滤。

1. 自动化的插件配置。

1. 针对 application.properties 和 application.yml 的资源过滤，包括通过 profile 定义的不同环境的配置文件，例如 application-dev.properties 和 application-dev.yml。

总结就是打包用的

### [Spring Boot 中如何解决跨域问题 ?](#spring-boot-中如何解决跨域问题)

跨域可以在前端通过 JSONP 来解决，但是 JSONP 只可以发送 GET 请求，无法发送其他类型的请求，在 RESTful 风格的应用中，就显得非常鸡肋，因此我们推荐在后端通过 （CORS，Crossorigin resource sharing） 来解决跨域问题。这种解决方案并非 Spring Boot 特有的，在传统的SSM 框架中，就可以通过 CORS 来解决跨域问题

- 局部配置 CORS：在 Controller 上使用 @CrossOrigin 注解。这种方式简单直接，适合对类进行跨域设置。

- 全局配置 CORS：通过实现WebMvcConfigurer接口然后重写addCorsMappings方法解决跨域问题。可以对整个应用程序进行统一的跨域配置

### [Spring Boot 中的监视器是什么？](#spring-boot-中的监视器是什么)

Spring boot actuator 是 spring 启动框架中的重要功能之一。Spring boot 监视器可帮助您访问生产环境中正在运行的应用程序的当前状态。有几个指标必须在生产环境中进行检查和监控。即使一些外部应用程序可能正在使用这些服务来向相关人员触发警报消息。监视器模块公开了一组可直接作为 HTTP URL 访问的REST 端点来检查状态。

### [在 Spring Boot 中你是怎么使用拦截器的?](#在-spring-boot-中你是怎么使用拦截器的)

在项目中我通常是使用拦截器来进行权限校验、日志记录、处理异常等问题。
 具体实现如下：

1. 实现 Handlerinterceptor 接口，并实现接口中的方法，方法里面包括了几个请求时间点：请求前、请求后、整个请求结束后(用于资源清理等操作)。

1. 通过实现 WebMvcConfigurer 的 addInterceptors 方法来添加自定义的拦截器。

### [如何使用 Spring Boot 实现全局异常处理？](#如何使用-spring-boot-实现全局异常处理)

Spring 提供了一种使用 ControllerAdvice 处理异常的非常有用的方法。 我们通过实现一个ControlerAdvice 类，来处理控制器类抛出的所有异常。

### [Spring Boot 中如何实现定时任务 ?](#spring-boot-中如何实现定时任务)

在 Spring Boot 中使用定时任务主要有两种不同的方式，一个就是使用 Spring 中的 @Scheduled注解，另一个则是使用第三方框架 Quartz。使用 Spring 中的 @Scheduled 的方式主要通过 @Scheduled 注解来实现。

### [说说你对 Spring Boot 事件机制的了解?](#说说你对-spring-boot-事件机制的了解)

Spring Boot 的事件机制，实际上是基于 Spring 的事件机制实现的，通过发布-订阅模式，主要用于应用程序中各个组件之间进行消息传递和解耦，通过事件发布和监听机制，实现了不同组件之间的松耦合，简化模块化开发和维护，例如我们可以通过监听 Spring 应用上下文的启动和关闭事件，进行相应的初始化和清理操作，而不需要修改 sping 源码

作用总结：

- 解耦：通过事件机制，可以在不同组件之间传递消息，而不需要它们之间有直接的依赖关系，从而提高了代码的可维护性和扩展性。

- 异步处理：某些事件可以异步处理，从而提高应用程序的响应速度和性能。

- 状态通知：通过事件机制，可以通知应用程序的不同部分发生了某些特定的状态变化，比如启动完成、环境准备就绪等。
