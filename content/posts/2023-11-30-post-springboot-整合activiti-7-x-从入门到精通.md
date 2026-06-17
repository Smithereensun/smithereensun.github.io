---
title: "SpringBoot 整合Activiti 7.X 从入门到精通"
date: 2023-11-30
description: "简介 Activiti 是一个轻量级工作流程和业务流程管理 (BPM) 平台，面向业务人员、开发人员和系统管理员。其核心是一个超快且坚如磐石的 Java BPMN 2 流程引擎。它是开源的，并根据 Apache 许可证分发。Activiti 可以在任何 Java 应用程序、服务器、集群或云中运行。它"
tags:
  - "Activiti 7.X"
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/activiti.html"
---

<h1 style="text-align: center">简介</h1>
<p><span>　　Activiti 是一个轻量级工作流程和业务流程管理 (BPM) 平台，面向业务人员、开发人员和系统管理员。</span><span>其核心是一个超快且坚如磐石的 Java BPMN 2 流程引擎。</span><span>它是开源的，并根据 Apache 许可证分发。</span><span>Activiti 可以在任何 Java 应用程序、服务器、集群或云中运行。</span><span>它与 Spring 完美集成，非常轻量级并且基于简单的概念。</span></p>
<h1 style="text-align: center">Idea 设计器</h1>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202308/1504448-20230814223444602-1729960989.gif" alt="" /></p>
<h2>绘制一个简单流程图</h2>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202308/1504448-20230814224139993-1653767448.gif" alt="" /></p>
<p><img src="https://img2023.cnblogs.com/blog/1504448/202308/1504448-20230814224605124-808627291.png" alt="" loading="lazy" /></p>
<h1 style="text-align: center">SpringBoot整合Activiti 7.X</h1>
<h2>添加依赖</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> Activiti 7.x依赖 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.activiti<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>activiti-spring-boot-starter<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>7.0.0.GA<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">version</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 由于activiti7是使用mybatis作为orm框架，我这里整合mybatis-plus，所以需要排除mybatis </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">exclusions</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">exclusion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>org.mybatis<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>mybatis<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">exclusion</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">exclusions</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>

        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> mysql 驱动 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>mysql<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">groupId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>mysql-connector-java<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">artifactId</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dependency</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
