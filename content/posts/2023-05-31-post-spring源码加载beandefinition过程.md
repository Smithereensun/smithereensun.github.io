---
title: "Spring源码加载BeanDefinition过程"
date: 2023-05-31
description: "本文主要讲解Spring加载xml配置文件的方式，跟踪加载BeanDefinition的全过程。 源码分析 源码的入口 ClassPathXmlApplicationContext构造函数 new ClassPathXmlApplicationContext(“spring.xml”)用于加载CLA"
tags:
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12054967.html"
---

<p>　　本文主要讲解Spring加载xml配置文件的方式，跟踪加载BeanDefinition的全过程。</p>
<h1 style="text-align: center">源码分析</h1>
<h2>源码的入口</h2>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191217154652077-1451877631.png" alt="" /></p>
<h2>ClassPathXmlApplicationContext构造函数</h2>
<p>　　new ClassPathXmlApplicationContext(“spring.xml”)用于加载CLASSPATH下的Spring配置文件，将配置文件传给构造函数，然后调用类内部的另外一个重载方法。</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191217155059895-688663741.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191217160400451-603687344.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h2>从构造函数中，可以看到一共做了3件事</h2>
<h3>super(parent)</h3>
<p>　　super(parent)的作用是为容器设置Bean资源加载器，层层跟踪，可知实际是由其父类AbstractApplicationContext完成设置的，parent为null，setParent(parent)就不继续跟踪了，这里需要注意的是，该类继承了DefaultResourceLoader，所以该类也作为资源加载器</p>
<p><strong>AbstractApplicationContext.java</strong></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191217161808500-1414437076.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>跟踪该类this()无参构造函数进去看看</p>
<p><strong>AbstractApplicationContext.java</strong></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191217162816905-1977474180.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>AbstractApplicationContext.java</strong></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191217162833293-164523129.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>&nbsp;PathMatchingResourcePatternResolver.java</strong></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191217162911933-1635571664.png" alt="" /></p>
<h3>setConfigLocations(configLocations)</h3>
<p>　　设置Bean定义资源的路径，由其父类AbstractRefreshableConfigApplicationContext完成，resolvePath解析路径，一直跟踪到底层是调用PropertyPlaceholderHelper的parseStringValue完成设置的</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201912/1504448-20191217163855660-1108366176.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<h3>&nbsp;refresh()</h3>
<p>　　这个就是整个Spring Bean加载的核心里面十二大步，用于刷新整个Spring上下文信息，定义了整个Spring上下文加载的流程。</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">@Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> refresh() <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> BeansException, IllegalStateException {
        </span><span style="color: rgba(0, 0, 255, 1)">synchronized</span> (<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.startupShutdownMonitor) {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">1、 Prepare this context for refreshing.</span>
<span style="color: rgba(0, 0, 0, 1)">            prepareRefresh();

               </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建DefaultListableBeanFactory（真正生产和管理bean的容器）
               </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">加载BeanDefition并注册到BeanDefitionRegistry
               </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">通过NamespaceHandler解析自定义标签的功能（比如:context标签、aop标签、tx标签）
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">2、 Tell the subclass to refresh the internal bean factory.</span>
            ConfigurableListableBeanFactory beanFactory =<span style="color: rgba(0, 0, 0, 1)"> obtainFreshBeanFactory();

            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">3、 Prepare the bean factory for use in this context.</span>
<span style="color: rgba(0, 0, 0, 1)">            prepareBeanFactory(beanFactory);

            </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">4、 Allows post-processing of the bean factory in context subclasses.</span>
<span style="color: rgba(0, 0, 0, 1)">                postProcessBeanFactory(beanFactory);

                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">实例化并调用实现了BeanFactoryPostProcessor接口的Bean
                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">比如：PropertyPlaceHolderConfigurer（context:property-placeholer）
                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">就是此处被调用的，作用是替换掉BeanDefinition中的占位符（${}）中的内容
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">5、 Invoke factory processors registered as beans in the context.</span>
<span style="color: rgba(0, 0, 0, 1)">                invokeBeanFactoryPostProcessors(beanFactory);

                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建并注册BeanPostProcessor到BeanFactory中（Bean的后置处理器）
                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">比如：AutowiredAnnotationBeanPostProcessor（实现@Autowired注解功能）
                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">      RequiredAnnotationBeanPostProcessor（实现@d注解功能）
                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">这些注册的BeanPostProcessor
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">6、 Register bean processors that intercept bean creation.</span>
<span style="color: rgba(0, 0, 0, 1)">                registerBeanPostProcessors(beanFactory);

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">7、 Initialize message source for this context.</span>
<span style="color: rgba(0, 0, 0, 1)">                initMessageSource();

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">8、 Initialize event multicaster for this context.</span>
<span style="color: rgba(0, 0, 0, 1)">                initApplicationEventMulticaster();

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">9、 Initialize other special beans in specific context subclasses.</span>
<span style="color: rgba(0, 0, 0, 1)">                onRefresh();

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">10、 Check for listener beans and register them.</span>
<span style="color: rgba(0, 0, 0, 1)">                registerListeners();

                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建非懒加载方式的单例Bean实例（未设置属性）
                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">填充属性
                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">初始化实例（比如调用init-method方法）
                     </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">调用BeanPostProcessor（后置处理器）对实例bean进行后置处理
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">11、 Instantiate all remaining (non-lazy-init) singletons.</span>
<span style="color: rgba(0, 0, 0, 1)">                finishBeanFactoryInitialization(beanFactory);

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">12、 Last step: publish corresponding event.</span>
<span style="color: rgba(0, 0, 0, 1)">                finishRefresh();
            }

            </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (BeansException ex) {
                </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (logger.isWarnEnabled()) {
                    logger.warn(</span>"Exception encountered during context initialization - " +
                            "cancelling refresh attempt: " +<span style="color: rgba(0, 0, 0, 1)"> ex);
                }

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Destroy already created singletons to avoid dangling resources.</span>
<span style="color: rgba(0, 0, 0, 1)">                destroyBeans();

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Reset 'active' flag.</span>
<span style="color: rgba(0, 0, 0, 1)">                cancelRefresh(ex);

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Propagate exception to caller.</span>
                <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
            }

            </span><span style="color: rgba(0, 0, 255, 1)">finally</span><span style="color: rgba(0, 0, 0, 1)"> {
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Reset common introspection caches in Spring's core, since we
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> might not ever need metadata for singleton beans anymore...</span>
<span style="color: rgba(0, 0, 0, 1)">                resetCommonCaches();
            }
        }
    }</span></pre>
