{

  "title": "MyBatis如何高效加载配置文件？",
  "has_date": true,
  "description": "配置解析主体方法 通过以上源码，就能看出，在mybatis的配置文件中： configuration节点为根节点。 在configuration节点之下，我们可以配置10个子节点， 分别为：properties、typeAliases、plugins、objectFactory、objectWrap",
  "tags": [
    "框架",
    "ORM"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/orm/mybatis-configurationparsingprocess - MyBatis如何高效加载配置文件？.md",
  "date": "2025-05-17"

}

## [配置解析主体方法](#配置解析主体方法)

通过以上源码，就能看出，在mybatis的配置文件中：

- configuration节点为根节点。

- 在configuration节点之下，我们可以配置10个子节点， 分别为：properties、typeAliases、plugins、objectFactory、objectWrapperFactory、settings、environments、databaseIdProvider、typeHandlers、mappers。

## [配置文件元素](#配置文件元素)

### [properties](#properties)

那么，要是两种方法都同时配置了，那么最终会采用什么样的配置呢？

1. 首先会先检查文件中的xml配置 和 外部指定的properties(也就是resource)，如果两个同时配置了，那么就会报异常

1. 接着会加载Java Configuration的配置

  1. 如果有Configuration的配置，那么最终会使用Configuration的配置

  1. 如果没有Configuration的配置，那么最终会使用上一步的xml的配置或resource配置

这是因为配置是存放在Properties，它继承自HashTable类，当依次将上述几种配置源put进去时，后加载的配置会覆盖先加载的配置。所以，最终应用配置时Configuration配置优先级最高，其次是另外两种中的一种。具体可以参考接下来的源码分析。

### [envirements](#envirements)

environments元素节点可以配置多个environment子节点， 怎么理解呢？

假如我们系统的开发环境和正式环境所用的数据库不一样（这是肯定的）， 那么可以设置两个environment, 两个id分别对应开发环境（dev）和正式环境（final），那么通过配置environments的default属性就能选择对应的environment了， 例如，我将environments的deault属性的值配置为dev, 那么就会选择dev的environment。 那么这个是怎么实现的呢？

看源码： mybatis 是通过XMLConfigBuilder这个类在解析mybatis配置文件的，XMLConfigBuilder对于environments的解析：

还有一个问题， 在配置dataSource的时候使用了 ${driver} 这种表达式， 那么这种形式是怎么解析的？其实，是通过PropertyParser这个类解析：

以上就是对于properties 和 environments元素节点的分析，比较重要的都在对于源码的注释中标出。

### [typeAliases](#typealiases)

typeAliases节点主要用来设置别名，其实这是挺好用的一个功能， 通过配置别名，我们不用再指定完整的包名，并且还能取别名。

例如： 我们在使用 com.demo.entity. UserEntity 的时候，我们可以直接配置一个别名user, 这样以后在配置文件中要使用到com.demo.entity.UserEntity的时候，直接使用User即可。

就以上例为例，我们来实现一下，看看typeAliases的配置方法：

再写一段测试代码，看看有没生效：（我只写一段伪代码）

typeAliasesElement:

重要的源码在这儿：TypeAliasRegistry.java

由源码可见，设置别名的原理就这么简单，Mybatis默认给我们设置了不少别名，在上面代码中都可以见到。

### [TypeHandler](#typehandler)

Mybatis中的TypeHandler是什么？

无论是 MyBatis 在预处理语句（PreparedStatement）中设置一个参数时，还是从结果集中取出一个值时，都会用类型处理器将获取的值以合适的方式转换成 Java 类型。Mybatis默认为我们实现了许多TypeHandler, 当我们没有配置指定TypeHandler时，Mybatis会根据参数或者返回结果的不同，默认为我们选择合适的TypeHandler处理。

那么，Mybatis为我们实现了哪些TypeHandler呢? 我们怎么自定义实现一个TypeHandler ? 这些都会在接下来的mybatis的源码中看到。

先看看配置:

typeHandlerElement

老规矩，先从对xml的解析讲起

接下来看看TypeHandler的管理注册类：TypeHandlerRegistry.java

由源码可以看到， mybatis为我们实现了那么多TypeHandler, 随便打开一个TypeHandler，看其源码，都可以看到，它继承自一个抽象类：BaseTypeHandler， 那么我们是不是也能通过继承BaseTypeHandler，从而实现自定义的TypeHandler ? 答案是肯定的，

演示自定义TypeHandler：

然后，就该配置自定义TypeHandler了：

也就是说，我们在自定义TypeHandler的时候，可以在TypeHandler通过@MappedJdbcTypes指定jdbcType, 通过 @MappedTypes 指定javaType, 如果没有使用注解指定，那么我们就需要在配置文件中配置。

### [objectFactory](#objectfactory)

objectFactory是干什么的？ 需要配置吗？

MyBatis 每次创建结果对象的新实例时，它都会使用一个对象工厂（ObjectFactory）实例来完成。默认的对象工厂需要做的仅仅是实例化目标类，要么通过默认构造方法，要么在参数映射存在的时候通过参数构造方法来实例化。默认情况下，我们不需要配置，mybatis会调用默认实现的objectFactory。 除非我们要自定义ObjectFactory的实现， 那么我们才需要去手动配置。

那么怎么自定义实现ObjectFactory？ 怎么配置呢？自定义ObjectFactory只需要去继承DefaultObjectFactory（是ObjectFactory接口的实现类），并重写其方法即可。具体的，本处不多说，后面再具体讲解。

写好了ObjectFactory, 仅需做如下配置：

objectFactoryElement源码：

### [plugins](#plugins)

plugin有何作用？ 需要配置吗？

plugins 是一个可选配置。mybatis中的plugin其实就是个interceptor， 它可以拦截Executor 、ParameterHandler 、ResultSetHandler 、StatementHandler 的部分方法，处理我们自己的逻辑。Executor就是真正执行sql语句的东西， ParameterHandler 是处理我们传入参数的，还记得前面讲TypeHandler的时候提到过，mybatis默认帮我们实现了不少的typeHandler, 当我们不显示配置typeHandler的时候，mybatis会根据参数类型自动选择合适的typeHandler执行，其实就是ParameterHandler 在选择。ResultSetHandler 就是处理返回结果的。

怎么自定义plugin ? 怎么配置？要自定义一个plugin, 需要去实现Interceptor接口，这儿不细说，后面实战部分会详细讲解。定义好之后，配置如下：

pluginElement源码：

### [mappers](#mappers)

mappers, 这下引出mybatis的核心之一了，mappers作用 ? 需要配置吗？

mappers 节点下，配置我们的mapper映射文件， 所谓的mapper映射文件，就是让mybatis 用来建立数据表和javabean映射的一个桥梁。在我们实际开发中，通常一个mapper文件对应一个dao接口， 这个mapper可以看做是dao的实现。所以,mappers必须配置。

mapperElement源码：

### [settings](#settings)

setting节点里配置的值会直接改写Configuration对应的变量值，这些变量描述的是Mybatis的全局运行方式，如果对这些属性的含义不熟悉的话建议不要配置，使用默认值即可。

settingsElement:
