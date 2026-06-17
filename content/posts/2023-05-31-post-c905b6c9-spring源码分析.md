---
title: "Spring源码分析"
date: 2023-05-31
description: "Spring介绍 什么是Spring？ 百度百科的介绍 Spring官方网址：&#160;http://spring.io/ 我们经常说的Spring其实指的是 Spring Framework (Spring 框架) 为什么学习Spring？ 好处 耦合和内聚介绍 耦合性(Coupling)，也叫"
tags:
  - "JAVA"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11756034.html"
---

<h1 style="text-align: center">Spring介绍</h1>
<h2>什么是Spring？</h2>
<p>百度百科的介绍</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028215017794-796331948.png" alt="" /></p>
<p>&nbsp;</p>
<p>Spring官方网址：&nbsp;<a href="http://spring.io/" rel="noopener nofollow"><span>http</span><span>://spring.io/</span></a></p>
<p>我们经常说的Spring其实指的是 <span style="color: rgba(0, 128, 0, 1)">Spring Framework <span style="color: rgba(0, 0, 0, 1)">(Spring 框架)</span></span></p>
<h2>为什么学习Spring？</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028215334408-1683709027.png" alt="" /></p>
<p>&nbsp;</p>
<h3>&nbsp;好处</h3>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028220053700-10885294.png" alt="" /></p>
<h2><strong>耦合和内聚介绍</strong></h2>
<p>　　<strong>耦合性</strong>(Coupling)，也叫耦合度，是对模块间关联程度的度量。</p>
<p>　　在软件工程中，耦合指的就是对象之间的依赖性。对象之间的耦合越高，维护成本越高。因此对象的设计应使类与架构之间的耦合最小。软件设计中通常用耦合度和内聚度作为衡量模块独立程度的标准。<span style="color: rgba(255, 0, 255, 1)">划分模块的一个准则就是高内聚低耦合。</span></p>
<p>　　<strong>内聚标志</strong>一个模块内各个元素彼此结合的紧密程度，它是信息隐蔽和局部化概念的自然扩展。内聚是从功能角度来度量模块内的联系，一个好的内聚模块应当适当做一件好事。</p>
<p>　　内聚和耦合是密切相关的，同其他模块存在高耦合的模块意味着低内聚，而高内聚的模块意味着该模块同其他模块之间是低耦合。<span style="color: rgba(255, 0, 255, 1)">在进行软件设计时，应力争做到高内聚，低耦合</span>。</p>
<h2>Spring体系结构</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028222226470-2123775062.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;Spring核心概念介绍</h2>
<p>　　<strong>IoC(<span style="color: rgba(255, 0, 255, 1)">核心中的核心</span>)：Inverse of Control，控制反转</strong>。对象的创建权力由程序反转给Spring框架。</p>
<p>　　<strong>AOP：Aspect Oriented Programming，面向切面编程</strong>。在不修改目标对象的源代码情况下，增强IoC容器中Bean的功能。</p>
<p>　　<strong>DI：Dependency Injection，依赖注入</strong>。在Spring框架负责创建Bean对象时，动态的将依赖对象注入到Bean组件中！！</p>
<p>　　<strong>Spring容器：指的就是IoC容器。</strong></p>
<h1 style="text-align: center">&nbsp;Spring IoC原理分析</h1>
<h2>什么是IoC容器？</h2>
<p>　　所谓的IoC容器就是指的是Spring中<strong>Bean工厂</strong>里面的Map存储结构(<span style="color: rgba(255, 0, 0, 1)">存储了Bean的实例</span>)。</p>
<h2>Spring框架中的工厂有哪些？</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)">ApplicationContext</span>接口()</p>
<p>　　　　<span style="color: rgba(255, 0, 0, 1)">实现了BeanFactory接口</span></p>
<p>　　　　实现ApplicationContext接口的工厂，可以获取到容器中具体的Bean对象</p>
<p>　　<span style="color: rgba(255, 0, 0, 1)">BeanFactory</span>工厂(<span style="color: rgba(255, 0, 0, 1)">是Spring架构早期的创建Bean对象的工厂接口</span>)</p>
<p>　　　　实现BeanFactory接口的工厂也可以获取到Bean对象</p>
<p>其实通过源码分析，不管是BeanFactory还是ApplicationContext，其实最终的底层BeanFactory都是<span style="color: rgba(255, 0, 0, 1)">DefaultListableBeanFactory</span></p>
<p>　　ApplicationContext和BeanFactory的区别？</p>
<p>　　创建Bean对象的时机不同：</p>
<p>　　　　BeanFactory采取延迟加载，第一次getBean时才会初始化Bean。</p>
<p>　　　　ApplicationContext是加载完applicationContext.xml时，就创建具体的Bean对象的实例。(<span style="color: rgba(255, 0, 0, 1)">只对BeanDefition中描述为时单例的Bean，才进行饿汉堡式加载</span>)</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028223936891-1185477824.png" alt="" /></p>
<p>&nbsp;</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028223948074-1209081119.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;如何创建Web环境中的IoC容器？</h2>
<h3>创建方式</h3>
<ul>
<li>ApplicationContext接口常用实现类</li>
</ul>
<p>　　　　ClassPathXmlApplicationContext：</p>
<p>　　　　　　它是从类的根路径下加载配置文件　　推荐使用这种</p>
<p>　　　　FileSystemXmlApplicationContext：</p>
<p>　　　　　　它是从磁盘路径上加载配置文件，配置文件可以在磁盘的任意位置。</p>
<p>　　　　AnnotationConfigApplicationContext：</p>
<p>　　　　　　当我们使用注解配置容器对象时，需要使用此类来创建Spring容器。它用来读取注解。</p>
<ul>
<li>Java应用中创建IoC容器：(了解)</li>
</ul>
<p>　　　　ApplicationContext context=<span style="color: rgba(255, 0, 0, 1)">new ClassPathXmlApplicationContext</span>(xml路径);</p>
<ul>
<li>Web应用中创建IoC容器：(重点)</li>
</ul>
<p>　　　　<span style="color: rgba(255, 0, 0, 1)">web.xml中配置ContextLoaderListener接口，并配置ContextConfigLocation参数</span></p>
<p>　　　　web容器启动之后加载web.xml，此时加载<span style="color: rgba(255, 0, 0, 1)">ContextLoaderListener</span>监听器(<span style="color: rgba(255, 0, 0, 1)">实现了ServletContextListener接口，该接口的描述请见下面的《三类八种监听器》</span>)</p>
<p>　　　　ContextLoaderListener监听器会在web容器启动的时候，出发<span style="color: rgba(255, 0, 0, 1)">ContextInitialized</span>()方法</p>
<p>　　　　ContextInitialized()方法会调用<span style="color: rgba(255, 0, 0, 1)">initWebApplicationContext</span>()方法，该方法负责创建Spring容器(<span style="color: rgba(255, 0, 0, 1)">DefaultListableBeanFactory</span>)</p>
<p>【Web三类八种监听器】</p>
<p>　　监听<span style="color: rgba(255, 0, 0, 1)">域对象</span>的生命周期</p>
<p>　　　　ServletContextListener：</p>
<p>　　　　　　创建：服务器启动</p>
<p>　　　　　　销毁：服务器正常关闭</p>
<p>　　　　　　spring ContextLoaderListener(服务器启动时负责加载spring配置文件)</p>
<p>&nbsp;　　　　HttpSessionListener</p>
<p>　　　　　　创建：第一次访问request.getHttpSession()</p>
<p>　　　　　　销毁：调用invalidate()；非法关闭；过期</p>
<p>　　　　ServletRequestListener</p>
<p>　　　　　　创建：每一次访问</p>
<p>　　　　　　销毁：相应结束</p>
<p>　　监听域对象的属性：(添加、删除、替换)</p>
<p>　　　　<span style="color: rgba(255, 0, 0, 1)">ServletContextAttributeListener</span></p>
<p>　　　　HttpSessionAttributeListener</p>
<p>　　　　ServletRequestAttributeListener</p>
<p>　　监听HttpSession中JavaBean的改变：</p>
<p>　　　　HttpSessionBindingListener(HttpSession和JavaBean对象的绑定和解绑)</p>
<p>　　　　HttpSessionActivationListener(HttpSession的序列化，活化，纯化)</p>
<h3>源码分析</h3>
<p>参考资料中的源码中的工程《Spring-sourcecode》</p>
<p><span style="color: rgba(255, 0, 0, 1)">1.web服务器(tomcat)启动会加载web.xml(启动ContextLoaderListener监听器)：</span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028235709442-1953951688.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;2.创建web环境中的Spring容器</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028235745933-418462136.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;3.ContextLoader类中创建Spring容器并初始化容器中的Bean实例</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191028235848126-348415578.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;4.configureAndRefreshWebApplicationContext方法中调用初始化Bean的<span style="color: rgba(255, 0, 0, 1)">refresh</span>方法</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191029000012691-866243021.png" alt="" /></p>
<p>&nbsp;</p>
<h3>&nbsp;图示</h3>
<p>该图主要是分析上面第三步骤中【创建Spring容器】的图示</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201910/1504448-20191029000100390-479051844.png" alt="" /></p>
<p>&nbsp;</p>
<h2>&nbsp;IoC容器如何创建Bean对象？</h2>
<h3>源码分析</h3>
<p>源码来源于<span style="color: rgba(255, 0, 0, 1)">AbstractApplicationContext</span>类：</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">@Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> refresh() <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> BeansException, IllegalStateException {
        </span><span style="color: rgba(0, 0, 255, 1)">synchronized</span> (<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.startupShutdownMonitor) {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Prepare this context for refreshing.</span>
<span style="color: rgba(0, 0, 0, 1)">            prepareRefresh();

              </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">1.创建真正的Spring容器（DefaultListableBeanFactory）
              </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">2.加载BeanDefition（描述要初始化的Bean的信息）
              </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">3.将BeanDefition注册到BeanDefitionRegistry
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Tell the subclass to refresh the internal bean factory.</span>
            ConfigurableListableBeanFactory beanFactory =<span style="color: rgba(0, 0, 0, 1)"> obtainFreshBeanFactory();

            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Prepare the bean factory for use in this context.</span>
<span style="color: rgba(0, 0, 0, 1)">            prepareBeanFactory(beanFactory);

            </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Allows post-processing of the bean factory in context subclasses.</span>
<span style="color: rgba(0, 0, 0, 1)">                postProcessBeanFactory(beanFactory);

                  </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">执行实现了BeanFactoryPostProcessor接口的Bean
                  </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">比如PropertyPlaceHolderConfigurer（context:property-placeholer）就是此处被调用的，替换掉BeanDefition中的占位符（${}）中的内容
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Invoke factory processors registered as beans in the context.</span>
<span style="color: rgba(0, 0, 0, 1)">                invokeBeanFactoryPostProcessors(beanFactory);

                  </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">注册BeanPostProcessor（后置处理器）
                  </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">比如容器自动装载了一个AutowiredAnnotationBeanPostProcessor后置处理器（实现@Autowired注解功能）
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Register bean processors that intercept bean creation.</span>
<span style="color: rgba(0, 0, 0, 1)">                registerBeanPostProcessors(beanFactory);

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Initialize message source for this context.</span>
<span style="color: rgba(0, 0, 0, 1)">                initMessageSource();

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Initialize event multicaster for this context.</span>
<span style="color: rgba(0, 0, 0, 1)">                initApplicationEventMulticaster();

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Initialize other special beans in specific context subclasses.</span>
<span style="color: rgba(0, 0, 0, 1)">                onRefresh();

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Check for listener beans and register them.</span>
<span style="color: rgba(0, 0, 0, 1)">                registerListeners();

                  </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">初始化非懒加载方式的单例Bean实例
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Instantiate all remaining (non-lazy-init) singletons.</span>
<span style="color: rgba(0, 0, 0, 1)">                finishBeanFactoryInitialization(beanFactory);

                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Last step: publish corresponding event.</span>
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
