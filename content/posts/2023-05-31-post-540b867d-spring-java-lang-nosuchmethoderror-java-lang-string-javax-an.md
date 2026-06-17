---
title: "[Spring]:java.lang.NoSuchMethodError: 'java.lang.String javax.annotation.Resource.lookup()'"
date: 2023-05-31
description: "错误信息 11月 05, 2019 9:32:15 下午 org.springframework.test.context.TestContextManager prepareTestInstance 严重: Caught exception while allowing TestExecution"
tags:
  - "JAVA"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11801803.html"
---

<p>错误信息</p>
<div class="cnblogs_code">
<pre>11月 05, 2019 9:32:15<span style="color: rgba(0, 0, 0, 1)"> 下午 org.springframework.test.context.TestContextManager prepareTestInstance
严重: Caught exception </span><span style="color: rgba(0, 0, 255, 1)">while</span><span style="color: rgba(0, 0, 0, 1)"> allowing TestExecutionListener [org.springframework.test.context.support.DependencyInjectionTestExecutionListener@6e0e048a] to prepare test instance [com.kkb.spring.test.TestSpringIoC2@76b1e9b8]
java.lang.NoSuchMethodError: </span>'java.lang.String javax.annotation.Resource.lookup()'<span style="color: rgba(0, 0, 0, 1)">
    at org.springframework.context.annotation.CommonAnnotationBeanPostProcessor$ResourceElement.</span>&lt;init&gt;(CommonAnnotationBeanPostProcessor.java:609<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.context.annotation.CommonAnnotationBeanPostProcessor.lambda$buildResourceMetadata$</span>0(CommonAnnotationBeanPostProcessor.java:373<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.util.ReflectionUtils.doWithLocalFields(ReflectionUtils.java:</span>692<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.context.annotation.CommonAnnotationBeanPostProcessor.buildResourceMetadata(CommonAnnotationBeanPostProcessor.java:</span>355<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.context.annotation.CommonAnnotationBeanPostProcessor.findResourceMetadata(CommonAnnotationBeanPostProcessor.java:</span>339<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.context.annotation.CommonAnnotationBeanPostProcessor.postProcessPropertyValues(CommonAnnotationBeanPostProcessor.java:</span>316<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.populateBean(AbstractAutowireCapableBeanFactory.java:</span>1350<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.autowireBeanProperties(AbstractAutowireCapableBeanFactory.java:</span>401<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:</span>118<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:</span>83<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:</span>246<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.createTest(SpringJUnit4ClassRunner.java:</span>227<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner$</span>1.runReflectiveCall(SpringJUnit4ClassRunner.java:289<span style="color: rgba(0, 0, 0, 1)">)
    at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:</span>12<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.methodBlock(SpringJUnit4ClassRunner.java:</span>291<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:</span>246<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:</span>97<span style="color: rgba(0, 0, 0, 1)">)
    at org.junit.runners.ParentRunner$</span>3.run(ParentRunner.java:290<span style="color: rgba(0, 0, 0, 1)">)
    at org.junit.runners.ParentRunner$</span>1.schedule(ParentRunner.java:71<span style="color: rgba(0, 0, 0, 1)">)
    at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:</span>288<span style="color: rgba(0, 0, 0, 1)">)
    at org.junit.runners.ParentRunner.access$</span>000(ParentRunner.java:58<span style="color: rgba(0, 0, 0, 1)">)
    at org.junit.runners.ParentRunner$</span>2.evaluate(ParentRunner.java:268<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.junit4.statements.RunBeforeTestClassCallbacks.evaluate(RunBeforeTestClassCallbacks.java:</span>61<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.junit4.statements.RunAfterTestClassCallbacks.evaluate(RunAfterTestClassCallbacks.java:</span>70<span style="color: rgba(0, 0, 0, 1)">)
    at org.junit.runners.ParentRunner.run(ParentRunner.java:</span>363<span style="color: rgba(0, 0, 0, 1)">)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.run(SpringJUnit4ClassRunner.java:</span>190<span style="color: rgba(0, 0, 0, 1)">)
    at org.eclipse.jdt.internal.junit4.runner.JUnit4TestReference.run(JUnit4TestReference.java:</span>89<span style="color: rgba(0, 0, 0, 1)">)
    at org.eclipse.jdt.internal.junit.runner.TestExecution.run(TestExecution.java:</span>41<span style="color: rgba(0, 0, 0, 1)">)
    at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.runTests(RemoteTestRunner.java:</span>541<span style="color: rgba(0, 0, 0, 1)">)
    at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.runTests(RemoteTestRunner.java:</span>763<span style="color: rgba(0, 0, 0, 1)">)
    at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.run(RemoteTestRunner.java:</span>463<span style="color: rgba(0, 0, 0, 1)">)
    at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.main(RemoteTestRunner.java:</span>209<span style="color: rgba(0, 0, 0, 1)">)

11月 </span>05, 2019 9:32:15<span style="color: rgba(0, 0, 0, 1)"> 下午 org.springframework.context.support.AbstractApplicationContext doClose
信息: Closing org.springframework.context.support.GenericApplicationContext@12cdcf4: startup date [Tue Nov </span>05 21:32:15 CST 2019]; root of context hierarchy</pre>
