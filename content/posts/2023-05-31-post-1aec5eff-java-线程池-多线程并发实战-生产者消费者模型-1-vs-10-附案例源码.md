---
title: "java 线程池、多线程并发实战(生产者消费者模型 1 vs 10) 附案例源码"
date: 2023-05-31
description: "导读 前二天写了一篇《Java 多线程并发编程》点我直达，放国庆，在家闲着没事，继续写剩下的东西，开干！ 线程池 为什么要使用线程池 例如web服务器、数据库服务器、文件服务器或邮件服务器之类的。请求的时候，单个任务时间很短，但是请求数量巨大。每一次请求，就会创建一个新线程，然后在新线程中请求服务，"
tags:
  - "多线程并发编程"
  - "JAVA"
  - "技术干货"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13756921.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　前二天写了一篇《Java 多线程并发编程》<a href="https://www.cnblogs.com/chenyanbin/p/13629067.html" target="_blank">点我直达</a>，放国庆，在家闲着没事，继续写剩下的东西，开干！</p>
<h1 style="text-align: center">线程池</h1>
<h2>为什么要使用线程池</h2>
<p>　　例如web服务器、数据库服务器、文件服务器或邮件服务器之类的。请求的时候，单个任务时间很短，但是请求数量巨大。每一次请求，就会创建一个新线程，然后在新线程中请求服务，频繁的创建线程，销毁线程造成系统很大的开销，资源的浪费。</p>
<p>　　线程池为线程生命周期开销问题和资源不足问题提供了解决方案。通过对多个任务重用线程，线程车创建的开销分摊到多个任务上。</p>
<h2>创建与使用</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202009/1504448-20200930232630266-194897221.gif" alt="" loading="lazy" /></p>
<h3>Future</h3>
<p>　　对具体的Runnable或者Callable任务的执行结果进行取消、查询是否完成、获取结果、设置结果。get方法会阻塞，直到任务返回结果。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202009/1504448-20200930234754597-1705309694.gif" alt="" loading="lazy" /></p>
<h3>Callable&amp;FutureTask</h3>
<p>　　Callable与Runnable功能相似，Callable有返回值；Runnable没有返回值；一般情况下，Callable与FutureTask一起使用，或者与线程池一起使用</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202009/1504448-20200930233806888-1172467463.gif" alt="" loading="lazy" /></p>
<h2>线程池核心组成部分</h2>
<ul>
<li>corePoolSize：核心线程池大小</li>
<li>maximumPoolSize：线程池最大容量</li>
<li>KeepAliveTime：当线程数量大于核心时，多余的空闲线程在终止之前等待新任务的最大时间</li>
<li>unit：时间单位</li>
<li>workQueue：工作队列</li>
<li>ThreadFactory：线程工厂</li>
<li>handler：拒绝策略</li>
</ul>
<p>　　ThreadPoolExcutor有6个参数，第一个是核心线程数，如果线程池无事可做，还是会保留这些线程。第二个是最大线程数，超过核心线程数的部分都会在第三个和第四个参数合起来决定的最长空闲存活时间超过后被剔除。第五个参数时阻塞队列，线程忙不过来要去这里面排队。最后一个是线程池工厂，主要决定队列也装不下的线程怎么处理，默认策略时抛出异常。</p>
<p>线程拒绝策略如下</p>
<ol>
<li>CallerRunsPolicy：交由调用方线程运行，比如 main 线程；如果添加到线程池失败，那么主线程会自己去执行该任务，不会等待线程池中的线程去执行。</li>
<li>AbortPolicy：该策略是线程池的默认策略，如果线程池队列满了丢掉这个任务并且抛出RejectedExecutionException异常。</li>
<li>DiscardOldestPolicy：丢弃队列中最老的任务，队列满了，会将最早进入队列的任务删掉腾出空间，再尝试加入队列。</li>
<li>DiscardPolicy：如果线程池队列满了，会直接丢掉这个任务并且不会有任何异常。</li>
<li>自定义拒绝策略，实现RejectedExecutionHandler接口</li>
</ol>
<h2>Executor框架</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201007145951430-377501254.gif" alt="" loading="lazy" /></p>
<h1 style="text-align: center">实战</h1>
<h2>需求分析</h2>
<h3>业务场景</h3>
<p>　　一般系统，多数会与第三方系统的数据进行打交道，而第三方的生产库，并不允许我们直接操作。在企业里面，一般都是通过中间表进行同步，即第三方系统将生产数据放入一张与其生产环境隔离的另一个独立数据库中的独立表，在根据接口协议，增加相应的字段。而我方需要读取该中间表中的数据，并对数据进行同步操作。此时就需要编写相应的程序进行数据同步。</p>
<h3>同步方式</h3>
<ol>
<li>全量同步：每天定时将当天的生产数据全部同步过来(优点：实现检点；缺点：数据同步不及时)</li>
<li>增量同步：每新增一条，便将该数据同步过来(优点：数据接近实时同步；缺点：实现相对困难)</li>
</ol>
<h3>我方需要做的事情</h3>
<p>　　读取中间表的数据，并同步到业务系统中</p>
<h3>模型抽离(<span style="color: rgba(255, 0, 0, 1)">生产者消费者模型</span>)</h3>
<ol>
<li>生产者：读取中间表的数据</li>
<li>消费者：消费生产者生产的数据</li>
</ol>
<h3>接口协议的制定</h3>
<ol>
<li>取我方业务上需要用到的字段</li>
<li>需要有字段记录数据什么时候进入中间表</li>
<li>增加相应的数据标志位，用于标志数据的同步状态</li>
<li>记录数据的同步时间</li>
</ol>
<h3>技术选型</h3>
<ol>
<li>mybatis</li>
<li>单一生产者多消费者</li>
<li>多线程并发操作</li>
</ol>
<h2>中间表设计</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201007202454857-460686864.gif" alt="" loading="lazy" /></p>
<h2>项目搭建</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201007190601220-984849704.gif" alt="" loading="lazy" /></p>
<h3>项目结构</h3>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202010/1504448-20201007222916218-251725079.png" alt="" loading="lazy" /></p>
<h3>pom.xml</h3>
<div class="cnblogs_code"><img src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" id="code_img_closed_7c56deeb-4ee2-478c-a22a-73b3905fb92c" class="code_img_closed" /><img src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" id="code_img_opened_7c56deeb-4ee2-478c-a22a-73b3905fb92c" class="code_img_opened" style="display: none" />
<div id="cnblogs_code_open_7c56deeb-4ee2-478c-a22a-73b3905fb92c" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;?</span><span style="color: rgba(255, 0, 255, 1)">xml version="1.0" encoding="UTF-8"</span><span style="color: rgba(0, 0, 255, 1)">?&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">project </span><span style="color: rgba(255, 0, 0, 1)">xmlns</span><span style="color: rgba(0, 0, 255, 1)">="http://maven.apache.org/POM/4.0.0"</span><span style="color: rgba(255, 0, 0, 1)">
         xmlns:xsi</span><span style="color: rgba(0, 0, 255, 1)">="http://www.w3.org/2001/XMLSchema-instance"</span><span style="color: rgba(255, 0, 0, 1)">
         xsi:schemaLocation</span><span style="color: rgba(0, 0, 255, 1)">="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">modelVersion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>4.0.0<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">modelVersion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>

    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.cyb<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>ybchen_syn<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.0-SNAPSHOT<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependencies</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 添加MyBatis框架 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.mybatis<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>mybatis<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>3.5.6<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span> <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 版本号视情况修改 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 添加MySql驱动包 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>mysql<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>mysql-connector-java<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>8.0.21<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">连接池</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>com.alibaba<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>druid<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.2.1<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">日志</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.slf4j<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>slf4j-log4j12<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>1.7.30<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">单元测试</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>junit<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>junit<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>4.13<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">scope</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>test<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">scope</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependencies</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>

<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">project</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
