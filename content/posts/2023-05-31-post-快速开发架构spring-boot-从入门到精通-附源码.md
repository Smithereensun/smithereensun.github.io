---
title: "快速开发架构Spring Boot 从入门到精通 附源码"
date: 2023-05-31
description: "导读 篇幅较长，干货十足，阅读需花费点时间。珍惜原创，转载请注明出处，谢谢！ Spring Boot基础 Spring Boot简介 Spring Boot是由Pivotal团队提供的全新框架，其设计目的是用来简化新Spring应用的初始搭建以及开发过程。该框架使用了特定的方式来进行配置，从而使开发"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12132757.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　篇幅较长，干货十足，阅读需花费点时间。珍惜原创，转载请注明出处，谢谢！</p>
<h1 style="text-align: center">Spring Boot基础</h1>
<h2>Spring Boot简介</h2>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>Spring Boot</strong></span>是<span style="color: rgba(255, 0, 0, 1)"><strong>由Pivotal团队</strong></span>提供的<span style="color: rgba(255, 0, 0, 1)"><strong>全新框架</strong></span>，其设计<span style="color: rgba(255, 0, 0, 1)"><strong>目的</strong></span>是用来<span style="color: rgba(255, 0, 0, 1)"><strong>简化新Spring应用</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>初始搭建以及开发过程</strong></span>。该框架使用了特定的方式来进行配置，从而使开发人员不再需要定义样板化的配置。通过这种方式，Spring Boot<span style="color: rgba(255, 0, 0, 1)"><strong>致力于</strong></span>在蓬勃发展的<span style="color: rgba(255, 0, 0, 1)"><strong>快速应用开发领域</strong></span>(rapid application development)成为领导者。</p>
<p>　　简单来说，<span style="color: rgba(255, 0, 0, 1)"><strong>SpringBoot</strong></span>可以<span style="color: rgba(255, 0, 0, 1)"><strong>简化应用程序的开发</strong></span>，使我们<span style="color: rgba(255, 0, 0, 1)"><strong>不</strong></span>再需要<span style="color: rgba(255, 0, 0, 1)"><strong>spring配置文件及web.xml</strong></span>。</p>
<h1 style="text-align: center">SpringBoot工程和创建</h1>
<h2>IDEA中的创建</h2>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200102132547226-1985752372.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200102132726976-584729436.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200102132817621-1421924448.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200102132924806-2078294795.png" alt="" /></p>
<h3>工程编辑</h3>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>系统会</strong></span>在前面设置的包中<span style="color: rgba(255, 0, 0, 1)"><strong>自动生成</strong></span>一个<span style="color: rgba(255, 0, 0, 1)"><strong>启动类</strong></span>。</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200102235136277-1864578751.png" alt="" /></p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>在启动类</strong></span>所在的<span style="color: rgba(255, 0, 0, 1)"><strong>包下</strong></span>再<span style="color: rgba(255, 0, 0, 1)"><strong>创建</strong></span>一个<span style="color: rgba(255, 0, 0, 1)"><strong>子包</strong></span>，在其中编写SpringMvc的处理器类。</p>
<p>　　注意，要求<span style="color: rgba(255, 0, 0, 1)"><strong>代码</strong></span>所在的<span style="color: rgba(255, 0, 0, 1)"><strong>包必须</strong></span>是<span style="color: rgba(255, 0, 0, 1)"><strong>启动类所在的包的子孙宝</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>不能是同级包</strong></span>。&nbsp;</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200102235243202-1252740090.png" alt="" /></p>
<h3>启动</h3>
<h3>ide方式</h3>
<p><img src="https://img2018.cnblogs.com/common/1504448/202001/1504448-20200103085014073-112460820.gif" alt="" /></p>
<h3>mac控制台方式(需maven打包)</h3>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200103141502163-1473993288.png" alt="" /></p>
<h2>官网创建</h2>
<p>地址：<a href="https://start.spring.io/" target="_blank" rel="noopener nofollow">https://start.spring.io/</a></p>
<h3>配置及生成</h3>
<p><img src="https://img2018.cnblogs.com/common/1504448/202001/1504448-20200105152728876-702610902.gif" alt="" /></p>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>配置项配置完成</strong></span>后，点击<span style="color: rgba(255, 0, 0, 1)"><strong>Generate</strong></span>按钮后，<span style="color: rgba(255, 0, 0, 1)"><strong>即可</strong></span>打开一个<span style="color: rgba(255, 0, 0, 1)"><strong>下载</strong></span>对话框。<span style="color: rgba(255, 0, 0, 1)"><strong>官网将配置好的</strong></span>Spring Boot<span style="color: rgba(255, 0, 0, 1)"><strong>工程生成</strong></span>一个zip<span style="color: rgba(255, 0, 0, 1)"><strong>压缩文件</strong></span>，只要我们将<span style="color: rgba(255, 0, 0, 1)"><strong>下载后的文件解压并添加到工程即可使用</strong></span>。</p>
<h2>基于war的Spring Boot工程</h2>
<p>　　前面2种方式创建的Spring Boot工程最终被打为了jar包，是以可执行文件的形式出现的，他们都使用了Spring Boot内嵌的Tomcat作为web服务器来运行web应用的。新版的Dubbo的监控中心工程就是典型的应用。但在实际生产环境下，对于web工程，很多时候我们需要的是war包，然后部署到企业级web服务器中。下面来演示如何使用Spring Boot将工程打为war包。</p>
<h3>工程创建</h3>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200106092644411-1715208625.png" alt="" /></p>
<p>我们看一下pom.xml文件，可以知道，Tomcat打包的时候不打进去</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200106101127711-1573766614.png" alt="" /></p>
<p>将项目打包后，仍到Tomcat的wabapps目录下</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200106102115806-620679704.png" alt="" /></p>
<h3>启动Tomcat</h3>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200106104420390-1769046799.png" alt="" /></p>
<p>接下来我们查看Tomcat目录</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200106104505190-308488175.png" alt="" /></p>
<p>打开网页，注意加上项目名</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200106104543665-1448317689.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/202001/1504448-20200106104638345-768567414.png" alt="" /></p>
<p>&nbsp;</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>注：mac启动Tomcat过程中遇到点麻烦，1、需要赋予文件夹权限；2、执行shell脚本报错:Operation not permitted，博主参考了下面2个链接配成成功哒</strong></span></p>
<h3>大概配置步骤</h3>
<div class="cnblogs_code">
<pre>1<span style="color: rgba(0, 0, 0, 1)">、切换Tomcat的bin目录下
    sudo chmod </span>755 *<span style="color: rgba(0, 0, 0, 1)">.sh

</span>2<span style="color: rgba(0, 0, 0, 1)">、解决Operation not permitted
    xattr </span>-d com.apple.quarantine .<span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">

3、启动Tomcat
    sudo sh ./startup.sh
<br>4、停止Tomcat<br>　　sudo sh ./shutdown.sh</span></pre>
<pre><span style="color: rgba(0, 128, 0, 1)">参考链接： 注：第一、二链接，赋权限，第三个链接解决Operation not permitted<br><br></span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">https://blog.csdn.net/caoxiaohong1005/article/details/53463443</span> <br><br><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">https://blog.csdn.net/F_Feng0628/article/details/60583250</span> <br><br><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">https://blog.csdn.net/default7/article/details/80172340</span></pre>
