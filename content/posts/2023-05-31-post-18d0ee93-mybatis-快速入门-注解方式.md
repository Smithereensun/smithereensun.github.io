---
title: "Mybatis 快速入门(注解方式)"
date: 2023-05-31
description: "导读 注解开发的方式只需要程序员开发Mapper接口即可，不需要编写映射文件（XML）。 环境搭建 项目结构 SqlMapConfig.xml &lt;!DOCTYPE configuration PUBLIC &quot;-//mybatis.org//DTD Config 3.0//EN&quo"
tags:
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12924748.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　注解开发的方式只需要程序员<span style="color: rgba(255, 0, 0, 1)"><strong>开发Mapper接口</strong></span>即可，不需要编写映射文件（XML）。</p>
<h2>环境搭建</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200520171207962-2079562277.png" alt="" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200520171222795-457169420.png" alt="" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200520171230626-211249820.png" alt="" /></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200520171242242-2028441817.png" alt="" /></p>
<h2>项目结构</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200520211500028-482413157.png" alt="" /></p>
<h3>SqlMapConfig.xml</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;!</span><span style="color: rgba(255, 0, 255, 1)">DOCTYPE configuration
PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
"http://mybatis.org/dtd/mybatis-3-config.dtd"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">configuration</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 引入外部配置文件 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">properties </span><span style="color: rgba(255, 0, 0, 1)">resource</span><span style="color: rgba(0, 0, 255, 1)">="db.properties"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">properties</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 数据库链接相关 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">environments </span><span style="color: rgba(255, 0, 0, 1)">default</span><span style="color: rgba(0, 0, 255, 1)">="development"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">environment </span><span style="color: rgba(255, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">="development"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">transactionManager </span><span style="color: rgba(255, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">="JDBC"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">dataSource </span><span style="color: rgba(255, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">="POOLED"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="driver"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="${db.driver}"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="url"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="${db.url}"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="username"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="${db.username}"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
                <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="password"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="${db.password}"</span> <span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">dataSource</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">environment</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">environments</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">mappers</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 添加单个接口 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> &lt;mapper class="com.cyb.anno.AnnotationDeptMapper" /&gt; </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 批量添加 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
       <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">package </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="com.cyb.anno"</span><span style="color: rgba(0, 0, 255, 1)">/&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">mappers</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">configuration</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
