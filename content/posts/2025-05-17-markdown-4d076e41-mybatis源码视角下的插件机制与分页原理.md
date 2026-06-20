{

  "title": "MyBatis源码视角下的插件机制与分页原理",
  "has_date": true,
  "description": "插件机制 首先我们看下MyBatis拦截器的接口定义： 比较简单，只有3个方法。 MyBatis默认没有一个拦截器接口的实现类，开发者们可以实现符合自己需求的拦截器。下面的MyBatis官网的一个拦截器实例： 全局xml配置： 这个拦截器拦截Executor接口的update方法（其实也就是SqlS",
  "tags": [
    "框架",
    "ORM"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/orm/mybatis-principleofpluginmechanism - MyBatis源码视角下的插件机制与分页原理.md",
  "date": "2025-05-17"

}

## [插件机制](#插件机制)

首先我们看下MyBatis拦截器的接口定义：

比较简单，只有3个方法。 MyBatis默认没有一个拦截器接口的实现类，开发者们可以实现符合自己需求的拦截器。下面的MyBatis官网的一个拦截器实例：

全局xml配置：

这个拦截器拦截Executor接口的update方法（其实也就是SqlSession的新增，删除，修改操作），所有执行executor的update方法都会被该拦截器拦截到。

首先从源头-&gt;配置文件开始分析：

XMLConfigBuilder解析MyBatis全局配置文件的pluginElement私有方法：

具体的解析代码其实比较简单，就不贴了，主要就是通过反射实例化plugin节点中的interceptor属性表示的类。然后调用全局配置类Configuration的addInterceptor方法。

这个interceptorChain是Configuration的内部属性，类型为InterceptorChain，也就是一个拦截器链，我们来看下它的定义：

现在我们理解了拦截器配置的解析以及拦截器的归属，现在我们回过头看下为何拦截器会拦截这些方法（Executor，ParameterHandler，ResultSetHandler，StatementHandler的部分方法）：

以上4个方法都是Configuration的方法。这些方法在MyBatis的一个操作(新增，删除，修改，查询)中都会被执行到，执行的先后顺序是Executor，ParameterHandler，ResultSetHandler，StatementHandler(其中ParameterHandler和ResultSetHandler的创建是在创建StatementHandler 3个可用的实现类CallableStatementHandler,PreparedStatementHandler,SimpleStatementHandler的时候，其构造函数调用的这3个实现类的构造函数其实都调用了父类BaseStatementHandler的构造函数)。

这4个方法实例化了对应的对象之后，都会调用interceptorChain的pluginAll方法，InterceptorChain的pluginAll刚才已经介绍过了，就是遍历所有的拦截器，然后调用各个拦截器的plugin方法。注意：拦截器的plugin方法的返回值会直接被赋值给原先的对象。

由于可以拦截StatementHandler，这个接口主要处理sql语法的构建，因此比如分页的功能，可以用拦截器实现，只需要在拦截器的plugin方法中处理StatementHandler接口实现类中的sql即可，可使用反射实现。

MyBatis还提供了@Intercepts和 @Signature关于拦截器的注解。官网的例子就是使用了这2个注解，还包括了Plugin类的使用：

### [代理链的生成](#代理链的生成)

Mybatis支持对Executor、StatementHandler、ParameterHandler和ResultSetHandler进行拦截，也就是说会对这4种对象进行代理。通过查看Configuration类的源代码我们可以看到，每次都对目标对象进行代理链的生成。

下面以Executor为例。Mybatis在创建Executor对象时会执行下面一行代码：

InterceptorChain里保存了所有的拦截器，它在mybatis初始化的时候创建。上面这句代码的含义是调用拦截器链里的每个拦截器依次对executor进行plugin（插入？）代码如下：

下面以一个简单的例子来看看这个plugin方法里到底发生了什么：

**每一个拦截器都必须实现上面的三个方法**，其中：

- `Object intercept(Invocation invocation)`是实现拦截逻辑的地方，内部要通过invocation.proceed()显式地推进责任链前进，也就是调用下一个拦截器拦截目标方法。

- `Object plugin(Object target)` 就是用当前这个拦截器生成对目标target的代理，实际是通过Plugin.wrap(target,this)来完成的，把目标target和拦截器this传给了包装函数。

- `setProperties(Properties properties)`用于设置额外的参数，参数配置在拦截器的Properties节点里。

注解里描述的是指定拦截方法的签名 [type,method,args] （即对哪种对象的哪种方法进行拦截），它在拦截前用于决断。

定义自己的Interceptor最重要的是要实现plugin方法和intercept方法，在plugin方法中我们可以决定是否要进行拦截进而决定要返回一个什么样的目标对象。而intercept方法就是要进行拦截的时候要执行的方法。

对于plugin方法而言，其实Mybatis已经为我们提供了一个实现。Mybatis中有一个叫做Plugin的类，里面有一个静态方法wrap(Object target,Interceptor interceptor)，通过该方法可以决定要返回的对象是目标对象还是对应的代理。这里我们先来看一下Plugin的源码：

下面是俩个注解类的定义源码：

### [Plugin.wrap方法](#plugin-wrap方法)

从前面可以看出，每个拦截器的plugin方法是通过调用Plugin.wrap方法来实现的。代码如下：

这个Plugin类有三个属性：

**getSignatureMap方法**：

**getSignatureMap方法解释**：首先会拿到拦截器这个类的 @Interceptors注解，然后拿到这个注解的属性 @Signature注解集合，然后遍历这个集合，遍历的时候拿出 @Signature注解的type属性(Class类型)，然后根据这个type得到带有method属性和args属性的Method。由于 @Interceptors注解的 @Signature属性是一个属性，所以最终会返回一个以type为key，value为`Set&lt;Method&gt;`的Map。

比如这个 @Interceptors注解会返回一个key为Executor，value为集合(这个集合只有一个元素，也就是Method实例，这个Method实例就是Executor接口的update方法，且这个方法带有MappedStatement和Object类型的参数)。这个Method实例是根据 @Signature的method和args属性得到的。如果args参数跟type类型的method方法对应不上，那么将会抛出异常。

**getAllInterfaces方法**：

**getAllInterfaces方法解释**： 根据目标实例target(这个target就是之前所说的MyBatis拦截器可以拦截的类，Executor,ParameterHandler,ResultSetHandler,StatementHandler)和它的父类们，返回signatureMap中含有target实现的接口数组。

所以Plugin这个类的作用就是根据 @Interceptors注解，得到这个注解的属性 @Signature数组，然后根据每个 @Signature注解的type，method，args属性使用反射找到对应的Method。最终根据调用的target对象实现的接口决定是否返回一个代理对象替代原先的target对象。

我们再次结合(Executor)interceptorChain.pluginAll(executor)这个语句来看，这个语句内部对executor执行了多次plugin,第一次plugin后通过Plugin.wrap方法生成了第一个代理类，姑且就叫executorProxy1，这个代理类的target属性是该executor对象。第二次plugin后通过Plugin.wrap方法生成了第二个代理类，姑且叫executorProxy2，这个代理类的target属性是executorProxy1...这样通过每个代理类的target属性就构成了一个代理链（从最后一个executorProxyN往前查找，通过target属性可以找到最原始的executor类）。

### [代理链上的拦截](#代理链上的拦截)

代理链生成后，对原始目标的方法调用都转移到代理者的invoke方法上来了。Plugin作为InvocationHandler的实现类，他的invoke方法是怎么样的呢？

比如MyBatis官网的例子，当Configuration调用newExecutor方法的时候，由于Executor接口的update(MappedStatement ms, Object parameter)方法被拦截器被截获。因此最终返回的是一个代理类Plugin，而不是Executor。这样调用方法的时候，如果是个代理类，那么会执行：

没错，如果找到对应的方法被代理之后，那么会执行Interceptor接口的interceptor方法。

在invoke里，如果方法签名和拦截中的签名一致，就调用拦截器的拦截方法。我们看到传递给拦截器的是一个Invocation对象，这个对象是什么样子的，他的功能又是什么呢？

可以看到，Invocation类保存了代理对象的目标类，执行的目标类方法以及传递给它的参数。

在每个拦截器的intercept方法内，最后一个语句一定是return invocation.proceed()（不这么做的话拦截器链就断了，你的mybatis基本上就不能正常工作了）。invocation.proceed()只是简单的调用了下target的对应方法，如果target还是个代理，就又回到了上面的Plugin.invoke方法了。这样就形成了拦截器的调用链推进。

### [小结](#小结)

MyBatis拦截器接口提供的3个方法中，plugin方法用于某些处理器(Handler)的构建过程。interceptor方法用于处理代理类的执行。setProperties方法用于拦截器属性的设置。

其实MyBatis官网提供的使用 @Interceptors和 @Signature注解以及Plugin类这样处理拦截器的方法，我们不一定要直接这样使用。我们也可以抛弃这3个类，直接在plugin方法内部根据target实例的类型做相应的操作。

总体来说MyBatis拦截器还是很简单的，拦截器本身不需要太多的知识点，但是学习拦截器需要对MyBatis中的各个接口很熟悉，因为拦截器涉及到了各个接口的知识点。

我们假设在MyBatis配置了一个插件，在运行时会发生什么？

- 所有可能被拦截的处理类都会生成一个代理

- 处理类代理在执行对应方法时，判断要不要执行插件中的拦截方法

- 执行插接中的拦截方法后，推进目标的执行

- 如果有N个插件，就有N个代理，每个代理都要执行上面的逻辑。这里面的层层代理要多次生成动态代理，是比较影响性能的。虽然能指定插件拦截的位置，但这个是在执行方法时动态判断，初始化的时候就是简单的把插件包装到了所有可以拦截的地方。

因此，在**编写插件时需注意以下几个原则**：

- 不编写不必要的插件；

- 实现plugin方法时判断一下目标类型，是本插件要拦截的对象才执行Plugin.wrap方法，否者直接返回目标本省，这样可以减少目标被代理的次数。

## [分页机制](#分页机制)

### [为什么在StatementHandler拦截](#为什么在statementhandler拦截)

在前面章节介绍了一次sqlsession的完整执行过程，从中可以知道sql的解析是在StatementHandler里完成的，所以为了重写sql需要拦截StatementHandler。

### [MetaObject简介](#metaobject简介)

在实现里大量使用了MetaObject这个对象，因此有必要先介绍下它。MetaObject是Mybatis提供的一个的工具类，通过它包装一个对象后可以获取或设置该对象的原本不可访问的属性（比如那些私有属性）。它有个三个重要方法经常用到：

- MetaObject forObject(Object object,ObjectFactory objectFactory, ObjectWrapperFactory objectWrapperFactory) 用于包装对象；

- Object getValue(String name) 用于获取属性的值（支持OGNL的方法）；

- void setValue(String name, Object value) 用于设置属性的值（支持OGNL的方法）；

### [拦截器签名](#拦截器签名)

从签名里可以看出，要拦截的目标类型是StatementHandler（注意：type只能配置成接口类型），拦截的方法是名称为prepare参数为Connection类型的方法。

### [intercept实现](#intercept实现)

StatementHandler的默认实现类是RoutingStatementHandler，因此拦截的实际对象是它。RoutingStatementHandler的主要功能是分发，它根据配置Statement类型创建真正执行数据库操作的StatementHandler，并将其保存到delegate属性里。由于delegate是一个私有属性并且没有提供访问它的方法，因此需要借助MetaObject的帮忙。通过MetaObject的封装后我们可以轻易的获得想要的属性。

在上面的方法里有个两个循环，通过他们可以分离出原始的RoutingStatementHandler（而不是代理对象）。

前面提到，签名里配置的要拦截的目标类型是StatementHandler拦截的方法是名称为prepare参数为Connection类型的方法，而这个方法是每次数据库访问都要执行的。因为我是通过重写sql的方式实现分页，为了不影响其他sql（update或不需要分页的query），我采用了通过ID匹配的方式过滤。默认的过滤方式只对id以Page结尾的进行拦截（注意区分大小写），如下：

当然，也可以自定义拦截模式，在mybatis的配置文件里加入以下配置项：

其中，属性dialect指示数据库类型，目前只支持mysql和oracle两种数据库。其中，属性pageSqlId指示拦截的规则，以正则方式匹配。

### [sql重写](#sql重写)

sql重写其实在原始的sql语句上加入分页的参数，目前支持mysql和oracle两种数据库的分页。

**mysql的分页实现**：

**oracle的分页实现**：

### [分页参数重写](#分页参数重写)

有时候会有这种需求，就是不但要查出指定页的结果，还需要知道总的记录数和页数。我通过重写分页参数的方式提供了一种解决方案：

### [plugin实现](#plugin实现)
