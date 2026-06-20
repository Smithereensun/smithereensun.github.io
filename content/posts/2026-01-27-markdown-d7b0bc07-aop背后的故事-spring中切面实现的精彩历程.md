{

  "title": "AOP背后的故事：Spring中切面实现的精彩历程",
  "has_date": true,
  "description": "AOP是基于IOC的Bean加载来实现的，所以理解Spring AOP的初始化必须要先理解Spring IOC的初始化。然后就能找到**初始化的流程和aop对应的handler**，即parseCustomElement方法找到parse aop:aspectj-autoproxy的handler(",
  "tags": [
    "框架",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/spring/aop2-implementationofcrosssections - AOP背后的故事：Spring中切面实现的精彩历程.md",
  "date": "2026-01-27"

}

AOP是基于IOC的Bean加载来实现的，所以理解Spring AOP的初始化必须要先理解Spring IOC的初始化。然后就能找到**初始化的流程和aop对应的handler**，即parseCustomElement方法找到parse aop:aspectj-autoproxy的handler(org.springframework.aop.config.AopNamespaceHandler)

## [aop配置标签的解析](#aop配置标签的解析)

AopNamespaceHandler，其实就是注册BeanDefinition的解析器BeanDefinitionParser，将`aop:xxxxxx`配置标签交给指定的parser来处理。

### [config配置标签的解析](#config配置标签的解析)

`&lt;aop:config/&gt;`由ConfigBeanDefinitionParser这个类处理，作为parser类最重要的就是parse方法

parseAspect的方法如下

### [aspectj-autoproxy配置标签的解析](#aspectj-autoproxy配置标签的解析)

`&lt;aop:aspectj-autoproxy/&gt;`则由AspectJAutoProxyBeanDefinitionParser这个类处理的，我们看下parse 方法

AopNamespaceUtils.registerAspectJAnnotationAutoProxyCreatorIfNecessary方法对应如下

AopConfigUtils.registerAspectJAnnotationAutoProxyCreatorIfNecessary对应如下

到这里，我们发现AOP的创建工作是交给AnnotationAwareAspectJAutoProxyCreator来完成的。

## [注解切面代理创建类(AnnotationAwareAspectJAutoProxyCreator)](#注解切面代理创建类-annotationawareaspectjautoproxycreator)

AnnotationAwareAspectJAutoProxyCreator是如何工作的呢？这时候我们就要看AnnotationAwareAspectJAutoProxyCreator类结构关系了。

如下是类结构关系
![](/imported/markdown/2026-01-27-markdown-d7b0bc07-aop背后的故事-spring中切面实现的精彩历程/images/b022f4004c7b-202404281432100.png)
它实现了两类接口：

- BeanFactoryAware属于**Bean级生命周期接口方法**

- InstantiationAwareBeanPostProcessor 和 BeanPostProcessor 这两个接口实现，一般称它们的实现类为“后处理器”，是**容器级生命周期接口方法**；

结合前文Spring Bean生命周期的流程
![](/imported/markdown/2026-01-27-markdown-d7b0bc07-aop背后的故事-spring中切面实现的精彩历程/images/dfc73bab9d1d-202404281433256.png)
我们就可以定位到核心的初始化方法肯定在postProcessBeforeInstantiation和postProcessAfterInitialization中。

### [postProcessBeforeInstantiation](#postprocessbeforeinstantiation)

如下是上述类结构中postProcessBeforeInstantiation的方法，读者在自己看代码的时候建议打个断点看，可以方便理解
![](/imported/markdown/2026-01-27-markdown-d7b0bc07-aop背后的故事-spring中切面实现的精彩历程/images/419fc0a6a701-202404281433617.png)
#### [判断是否是aop基础类](#判断是否是aop基础类)

是否是aop基础类的判断方法 isInfrastructureClass 如下

父类判断它是否是aop基础类的方法 super.isInfrastructureClass(beanClass), 本质上就是判断该类是否实现了Advice, Pointcut, Advisor或者AopInfrastructureBean接口。

#### [是否应该跳过shouldSkip](#是否应该跳过shouldskip)

通过断点辅助，candidateAdvisors是就是xml配置的通知是对应的
![](/imported/markdown/2026-01-27-markdown-d7b0bc07-aop背后的故事-spring中切面实现的精彩历程/images/0ab2b5d15a6d-202404281434457.png)
#### [切面方法转成Advisor](#切面方法转成advisor)

findCandidateAdvisors方法如下：

在当前的bean Factory中通过AspectJ注解的方式生成Advisor类，buildAspectJAdvisors方法如下

上述方法本质上的思路是：用DCL双重锁的单例实现方式，拿到切面类里的切面方法，将其转换成advisor（并放入缓存中）。

转换的成advisor的方法是：this.advisorFactory.getAdvisors

getAdvisor方法如下

#### [获取表达式的切点](#获取表达式的切点)

获取表达式的切点的方法getPointcut如下：

AbstractAspectJAdvisorFactory.findAspectJAnnotationOnMethod的方法如下

findAnnotation方法如下

AnnotationUtils.findAnnotation 获取注解方法如下

#### [封装成Advisor](#封装成advisor)

注：Advisor 是 advice的包装器，包含了advice及其它信息

由InstantiationModelAwarePointcutAdvisorImpl构造完成

通过pointcut获取advice

交给aspectJAdvisorFactory获取

### [postProcessAfterInitialization](#postprocessafterinitialization)

有了Adisor, 注入到合适的位置并交给代理（cglib和jdk)实现了。

## [小结](#小结)

主要是处理使用了@Aspect注解的切面类，然后将切面类的所有切面方法根据使用的注解生成对应Advice，并将Advice连同切入点匹配器和切面类等信息一并封装到Advisor的过程。

1. 由IOC Bean加载方法栈中找到parseCustomElement方法，找到parse aop:aspectj-autoproxy的handler(org.springframework.aop.config.AopNamespaceHandler)

1. AopNamespaceHandler注册了aop:aspectj-autoproxy/的解析类是AspectJAutoProxyBeanDefinitionParser

1. AspectJAutoProxyBeanDefinitionParser的parse 方法 通过AspectJAwareAdvisorAutoProxyCreator类去创建

1. AspectJAwareAdvisorAutoProxyCreator实现了两类接口，BeanFactoryAware和BeanPostProcessor；根据Bean生命周期方法找到两个核心方法：postProcessBeforeInstantiation和postProcessAfterInitialization

  - postProcessBeforeInstantiation：主要是处理使用了@Aspect注解的切面类，然后将切面类的所有切面方法根据使用的注解生成对应Advice，并将Advice连同切入点匹配器和切面类等信息一并封装到Advisor

  - postProcessAfterInitialization：主要负责将Advisor注入到合适的位置，创建代理（cglib或jdk)，为后面给代理进行增强实现做准备。
