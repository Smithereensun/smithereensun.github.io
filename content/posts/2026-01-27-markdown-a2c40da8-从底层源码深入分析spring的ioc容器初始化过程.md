{

  "title": "从底层源码深入分析Spring的IoC容器初始化过程",
  "has_date": true,
  "description": "IOC容器的初始化整体过程 Spring是如何实现将资源配置（以xml配置为例）通过加载，解析，生成BeanDefination并注册到IoC容器中的？这主要会经过以下 4 步： 从XML中读取配置文件，并将配置文件转换为Document 再将Document中的 bean标签解析成 BeanDef",
  "tags": [
    "框架",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/spring/ioc2-initializationprocess - 从底层源码深入分析Spring的IoC容器初始化过程.md",
  "date": "2026-01-27"

}

## [IOC容器的初始化整体过程](#ioc容器的初始化整体过程)

Spring是如何实现将资源配置（以xml配置为例）通过加载，解析，生成BeanDefination并注册到IoC容器中的？这主要会经过以下 4 步：

1. 从XML中读取配置文件，并将配置文件转换为Document

1. 再将Document中的 bean标签解析成 BeanDefinition，如解析 property 元素， 并注入到 BeanDefinition 实例中。

1. 将 BeanDefinition 注册到容器 BeanDefinitionMap 中。

1. BeanFactory 根据 BeanDefinition 的定义信息创建实例化和初始化 bean。

## [启动的入口](#启动的入口)

对于xml配置的Spring应用，在main()方法中实例化ClasspathXmlApplicationContext即可创建一个IoC容器。可以从这个构造方法开始，探究一下IoC容器的初始化过程。

这里的作用就是加载了一个解析配置文件路径的加载器，然后通过系统环境变量拿到这个配置文件，进行一些配置文件的去空格，转换表达式等等操作(注意，这里没有进行解析)；最后通过 refresh方法 完成了几乎所有的工作。
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/1bb0986547ca-202408251043018.png)
### [设置资源解析器和环境](#设置资源解析器和环境)

调用父类容器AbstractApplicationContext的构造方法(`super(parent)`方法)为容器设置好Bean资源加载器

通过AbstractApplicationContext默认构造函数初始化容器id, name, 状态 以及 资源解析器

通过AbstractApplicationContext的`setParent(parent)`方法将父容器的Environment合并到当前容器

### [设置配置路径](#设置配置路径)

在设置容器的资源加载器之后，接下来FileSystemXmlApplicationContet执行setConfigLocations方法通过调用其父类AbstractRefreshableConfigApplicationContext的方法进行对Bean定义资源文件的定位

## [启动的主体流程](#启动的主体流程)

Spring IoC容器对Bean定义资源的载入是从refresh()函数开始的，refresh()是一个模板方法
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/d8666acecdb0-202408251043977.png)
refresh()方法的作用是：在创建IoC容器前，如果已经有容器存在，则需要把已有的容器销毁和关闭，以保证在refresh之后使用的是新建立起来的IoC容器。

refresh的作用类似于对IoC容器的重启，在新建立好的容器中对容器进行初始化，对Bean定义资源进行载入。

这里的设计上是一个非常典型的资源类加载处理型的思路，头脑中需要形成如下图的**顶层思路**（而不是只停留在流水式的方法上面）：

- **模板方法设计模式**，模板方法中使用典型的**钩子方法**

- 将**具体的初始化加载方法**插入到钩子方法之间

- 将初始化的阶段封装，用来记录当前初始化到什么阶段；常见的设计是xxxPhase/xxxStage；

- 资源加载初始化有失败等处理，必然是**try/catch/finally**...

![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/3c988e9be0bf-202404281048285.png)
## [① prepareRefresh 准备上下文环境](#_1-preparerefresh-准备上下文环境)

## [② obtainFreshBeanFactory 创建工厂](#_2-obtainfreshbeanfactory-创建工厂)

这个方法主要就是创建了一个工厂`BeanFactory`，并且解析了配置文件，加载了`Bean`定义信息
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/3537979e80db-202408251041086.png)
AbstractApplicationContext的obtainFreshBeanFactory()方法调用子类容器的refreshBeanFactory()方法，启动容器载入Bean定义资源文件的过程，代码如下：

AbstractApplicationContext类中只抽象定义了refreshBeanFactory()方法，如下：

容器真正调用的是其子类AbstractRefreshableApplicationContext实现的refreshBeanFactory()方法；在创建IoC容器前，如果已经有容器存在，则需要把已有的容器销毁和关闭，以保证在refresh之后使用的是新建立起来的IoC容器。方法的源码如下：

### [loadBeanDefinitions](#loadbeandefinitions)
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/738caeb97f27-202408251050279.png)
AbstractRefreshableApplicationContext 中只定义了抽象的 loadBeanDefinitions 方法，容器真正调用的是其子类 AbstractXmlApplicationContext 对该方法的实现，AbstractXmlApplicationContext 的主要源码如下：

Xml Bean读取器(XmlBeanDefinitionReader)调用其父类AbstractBeanDefinitionReader的 reader.loadBeanDefinitions方法读取Bean定义资源。

由于这里使用 ClassPathXmlApplicationContext 作为例子分析，因此 getConfigResources 的返回值为null，因此程序执行reader.loadBeanDefinitions(configLocations)分支。

### [AbstractBeanDefinitionReader读取Bean定义资源](#abstractbeandefinitionreader读取bean定义资源)

AbstractBeanDefinitionReader的loadBeanDefinitions方法源码如下：

从对AbstractBeanDefinitionReader的loadBeanDefinitions方法源码分析可以看出该方法做了以下两件事：

- 首先，调用资源加载器的获取资源方法resourceLoader.getResource(location)，获取到要加载的资源。

- 其次，真正执行加载功能是其子类XmlBeanDefinitionReader的loadBeanDefinitions方法。

#### [XmlBeanDefinitionReader加载Bean定义资源](#xmlbeandefinitionreader加载bean定义资源)
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/be12c181b8ac-202408251132737.png)
XmlBeanDefinitionReader的loadBeanDefinitions方法主要是调用了 loadBeanDefinitions(Resource …) 方法，可以看到代表bean文件的资源定义以后的载入过程。

通过源码分析，载入Bean定义资源文件的最后一步是将Bean定义资源转换为Document对象，该过程由documentLoader实现

#### [DocumentLoader将Bean定义资源转换为Document对象](#documentloader将bean定义资源转换为document对象)

DocumentLoader将Bean定义资源转换成Document对象的源码如下：

该解析过程调用JavaEE标准的JAXP标准进行处理。

至此Spring IoC容器根据定位的Bean定义资源文件，将其加载读入并转换成为Document对象过程完成。

接下来继续分析Spring IoC容器将载入的Bean定义资源文件转换为Document对象之后，是如何将其解析为Spring IoC管理的Bean对象并将其注册到容器中的。

### [XmlBeanDefinitionReader解析载入的Bean定义资源文件](#xmlbeandefinitionreader解析载入的bean定义资源文件)
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/f3d5c0bd53f9-202408251139671.png)
XmlBeanDefinitionReader类中的doLoadBeanDefinitions方法是从特定XML文件中实际载入Bean定义资源的方法，该方法在载入Bean定义资源之后将其转换为Document对象，接下来调用registerBeanDefinitions启动Spring IoC容器对Bean定义的解析过程，registerBeanDefinitions方法源码如下：

Bean定义资源的载入解析分为以下两个过程：

- 首先，通过调用XML解析器将Bean定义资源文件转换得到Document对象，但是这些Document对象并没有按照Spring的Bean规则进行解析。这一步是载入的过程

- 其次，在完成通用的XML解析之后，按照Spring的Bean规则对Document对象进行解析。

在这个方法中很好地应用了面向对象中**单一职责**的原则，将逻辑处理委托给单一的类进行处理，而这个逻辑处理类就是BeanDefinitionDocumentReader。BeanDefinitionDocumentReader是一个接口，而实例化的工作是在createBeanDefinitionDocumentReader()中完成的，而通过此方法，BeanDefinitionDocumentReader真正的类型其实已经是DefaultBeanDefinitionDocumentReader了。按照Spring的Bean规则对Document对象解析的过程是在接口BeanDefinitionDocumentReader的实现类DefaultBeanDefinitionDocumentReader中实现的。

#### [DefaultBeanDefinitionDocumentReader对Bean定义的Document对象解析](#defaultbeandefinitiondocumentreader对bean定义的document对象解析)

BeanDefinitionDocumentReader接口通过registerBeanDefinitions方法调用其实现类DefaultBeanDefinitionDocumentReader对Document对象进行解析，解析的代码如下：

这里我们注意到在注册Bean的最开始是对PROFILE_ATTRIBUTE属性的解析，有了 profile 这个特性我们就可以同时在配置文件中部署两套配置来适用于生产环境和开发环境，这样可以方便的进行切换开发、部署环境，最常用的就是更换不同的数据库。

首先程序会获取beans节点是否定义了profile属性，如果定义了则会需要到环境变量中去寻找，因为profile是可以同时指定多个的，需要程序对其拆分，并解析每个profile是都符合环境变量中所定义的，不定义则不会浪费性能去解析。

注意：跟进 preProcessXml(root) 和 postProcessXml(root) 后发现代码是空的。
 记住，一个类要么是面向继承设计，要么是final修饰的。而这个类并不是final修饰的，那么就是面向继承设计的，显然这里是用到了模板方法设计模式，如果继承自DefaultBeanDefinitionDocumentReader的子类需要在Bean解析前后做一些处理的话，那么只需要重写这两个方法即可

#### [BeanDefinitionParserDelegate解析Bean定义资源文件生成BeanDefinition](#beandefinitionparserdelegate解析bean定义资源文件生成beandefinition)

处理了profile后就可以进行XML的读取了，跟踪代码进入parseBeanDefinitions(root, this.delegate)。

上面的代码看起来逻辑还是蛮清晰的，因为在Spring的XML配置里面有两大类Bean声明，一个是默认的，如：

另一类就是自定义的，如：

而两种方式的读取及解析差别是非常大的，如果采用Spring默认的配置，Spring当然知道该怎么做，但是如果是自定义的，那么就需要用户实现一些接口及配置了。对于根节点或者子节点如果是默认命名空间的话则采用parseDefaultElement方法进行解析，否则使用delegate.parseCustomElement方法对自定义命名空间进行解析。

而判断是否默认命名空间还是自定义命名空间的办法其实是使用node.getNamespaceURI()获取命名空间，并与Spring中固定的命名空间`http://www.Springframework.org/schema/beans`进行比对。如果一致则认为是默认，否则就认为是自定义。

##### [默认标签的解析](#默认标签的解析)

委托BeanDefinitionDelegate类的parseBeanDefinitionElement方法进行元素解析，返回BeanDefinitionHolder类型的实例bdHolder，经过这个方法后，bdHolder实例已经包含我们配置文件中配置的各种属性了，例如class、name、id、alias之类的属性。

parseBeanDefinitionElement的解析方法 就不一一展开了，无非就是解析XML各种元素，来生成BeanDefinition。解析的过程与mybatis解析xml文件同理，详情可以看这篇文章

##### [自定义标签的解析](#自定义标签的解析)

在实际项目中，较少进行自定义标签，因此这里不展开描述了。

### [解析过后的BeanDefinition在IoC容器中的注册](#解析过后的beandefinition在ioc容器中的注册)

Document对象的解析后得到封装 BeanDefinition 的 BeanDefinitionHold 对象，然后调用 BeanDefinitionReaderUtils 的 registerBeanDefinition 方法向IoC容器注册解析的Bean，BeanDefinitionReaderUtils的注册的源码如下：

当调用BeanDefinitionReaderUtils向IoC容器注册解析的BeanDefinition时，真正完成注册功能的是DefaultListableBeanFactory。

### [DefaultListableBeanFactory向IoC容器注册解析后的BeanDefinition](#defaultlistablebeanfactory向ioc容器注册解析后的beandefinition)
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/0f2b6ff09b58-202408251144850.png)
IOC容器本质上就是一个beanDefinitionMap， 注册即将BeanDefinition put到map中

至此，Bean定义资源文件中配置的Bean被解析过后，已经注册到IoC容器中，被容器管理起来，真正完成了IoC容器初始化所做的全部工作。现在IoC容器中已经建立了整个Bean的配置信息，这些 BeanDefinition 信息已经可以使用，并且可以被检索，IoC容器的作用就是对这些注册的Bean定义信息进行处理和维护。这些的注册的Bean定义信息是IoC容器控制反转的基础，正是有了这些注册的数据，容器才可以进行依赖注入。

### [小结](#小结)

现在通过上面的代码，总结一下IOC容器初始化的基本步骤：
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/7fd6911a589e-202404281053871.png)

- 初始化的入口在容器实现中的 refresh()调用来完成

- 对 bean 定义载入 IOC 容器使用的方法是 loadBeanDefinition，其中的大致过程如下：

  - 通过 ResourceLoader 来完成资源文件位置的定位，DefaultResourceLoader 是默认的实现，同时上下文本身就给出了 ResourceLoader 的实现，可以从类路径，文件系统, URL 等方式来定为资源位置。如果是 XmlBeanFactory作为 IOC 容器，那么需要为它指定 bean 定义的资源，也就是说 bean 定义文件时通过抽象成 Resource 来被 IOC 容器处理的

  - 通过 BeanDefinitionReader来完成定义信息的解析和 Bean 信息的注册, 往往使用的是XmlBeanDefinitionReader 来解析 bean 的 xml 定义文件 — 实际的处理过程是委托给 BeanDefinitionParserDelegate 来完成的，从而得到 bean 的定义信息，这些信息在 Spring 中使用 BeanDefinition 对象来表示

  - 容器解析得到 BeanDefinition 以后，需要把它在 IOC 容器中注册，这由 IOC 实现 BeanDefinitionRegistry 接口来实现。注册过程就是在 IOC 容器内部维护的一个HashMap 来保存得到的 BeanDefinition 的过程。这个 HashMap 是 IoC 容器持有 bean 信息的场所，以后对 bean 的操作都是围绕这个HashMap 来实现的.

- 最后可以通过 BeanFactory 和 ApplicationContext 来享受到 Spring IOC 的服务了，在使用 IOC 容器的时候，除了少量粘合代码，绝大多数以正确 IoC 风格编写的应用程序代码完全不用关心如何到达工厂，因为容器将把这些对象与容器管理的其他对象钩在一起。基本的策略是把工厂放到已知的地方，最好是放在对预期使用的上下文有意义的地方，以及代码将实际需要访问工厂的地方。 Spring 本身提供了对声明式载入 web 应用程序用法的应用程序上下文，并将其存储在ServletContext 中的框架实现。

## [③ prepareBeanFactory 准备Bean工厂](#_3-preparebeanfactory-准备bean工厂)

为`BeanFactory`准备一些环境，方便在实例化的时候使用，同时添加容器自己的`BeanPostProcessor`

## [④ postProcessBeanFactory 子类扩展BeanFactory](#_4-postprocessbeanfactory-子类扩展beanfactory)

## [⑤ invokeBeanFactoryPostProcessors 执行增强的方法](#_5-invokebeanfactorypostprocessors-执行增强的方法)

这个类，涉及到了两个接口。

- `BeanFactoryPostProcessor`

- `BeanDefinitionRegistryPostProcessor`接口，这个接口是`BeanFactoryPostProcessor`的子接口，**它的优先级比`BeanFactoryPostProcessor`更高**

它的总体执行流程是：先执行`BeanDefinitionRegistryPostProcessor`的`BeanFactoryPostProcessor`，然后再执行`BeanFactoryPostProcessor`

下图是`BeanDefinitionRegistryPostProcessor`接口的处理过程：
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/64e242e99120-202408251157353.webp)
**BeanFactoryPostProcessor的处理逻辑**

总逻辑就是先分类，已经处理过的直接跳过，没有处理过的，分类处理，逻辑和上面的相同。

执行BeanFactoryPostProcessor后置处理器的postProcessBeanFactory()增强方法

## [⑥ registerBeanPostProcessors](#_6-registerbeanpostprocessors)

这个方法的逻辑和上面的一样，只不过上面是直接执行了BeanFactoryPostProcessor，而这个仅仅注册没执行。
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/550bcd8901f8-202408251159524.webp)
首先拿到工厂中所有的`BeanPostProcessor`类型的`Bean`，然后分类处理，排序注册。

## [⑦ initMessageSource()](#_7-initmessagesource)

执行国际化内容

## [⑧ initApplicationEventMulticaster](#_8-initapplicationeventmulticaster)

创建了一个多播器，为添加`Listener`提供支持。

**主要逻辑：**

- 容器中是否存在`applicationEventMulticaster`，如果存在直接注册

- 如果不存在，创建一个`SimpleApplicationEventMulticaster`，注册到容器中。

## [⑨ onRefresh()](#_9-onrefresh)

子类扩展

## [⑩ registerListeners()](#_10-registerlisteners)

观察者模式的实现

## [⑪ finishBeanFactoryInitialization](#_11-finishbeanfactoryinitialization)

**下图是创建Bean的主要流程**
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/a3296bd47192-202408251619533.webp)
**按照途中的序号一个一个说：**

1. `BeanDefinition`是否需要合并。`BeanDefinition`根据不同类型的配置文件信息，会将`Bean`封装到不同的`Bean`信息定义类中。比如我们常用的配置文件版的`GenericBeanDefinition`；注解扫描版的`ScannedGenericBeanDefinition`等等。

而在这个过程中就出现了，**父定义和子定义**，我们需要在实际处理定义信息的时候进行合并处理，主要有一下三个方面

- 存在父定义信息，使用父定义信息创建一个`RootBeanDefinition`，然后将自定义信息作为参数传入。

- 不存在父定义信息，并且当前`BeanDefinition`是`RootBeanDefintion`类型的，直接返回一份`RootBeanDefintion`的克隆

- 不存在父定义信息，并且当前`BeanDefintion`不是`RootBeanDefintiton`类型的，直接通过该`BeanDefintion`构建一个`RootBeanDefintion`返回

**上面的流程也是源码中的执行流程**
![](/imported/markdown/2026-01-27-markdown-a2c40da8-从底层源码深入分析spring的ioc容器初始化过程/images/b022b40e8774-202408251619495.webp)

1. `isFactoryBean`。判断是否为`FactoryBean`

**简单介绍一下：**`FactoryBean`是让开发者创建自己需要`Bean`接口。内部提供了三个方法

当我们通过`GetBean`直接该`Bean`的时候，获取到的是该工厂指定返回的`Bean`类型。如果想要获取该`Bean`本身，需要通过一个前缀获得`&`

再来看一个点，这个就是从容器中获取Bean的主要方法，也是解决循环依赖的逻辑，这部分内容详情看这篇文章

## [⑫ finishRefresh](#_12-finishrefresh)

这个方法进行了一系列的资源清理

initLifecycleProcessor，这个方法极具简单，就看一下当前Bean中是否存在生命周期处理器，如果存在直接使用这个，如果不存在则创建一个默认的，并且注册为一个单例的扔到容器中。
