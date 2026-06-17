---
title: "The reference to entity \"characterEncoding\" must end with the ';'"
date: 2023-05-31
description: "在配置数据库连接池数据源时，本来没有错误，结果加上编码转换格式后eclipse突然报错： 这是怎么回事？ 经过查询，发现这个错误其实很好解决。 首先，原因是： .xml文件中 ‘ &amp; ’字符需要进行转义！！！ 看到这里，其实已经恍然大悟，那么，这个字符 ‘&#160;&amp;&#160;’"
tags:
  - "JAVA"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11839321.html"
---

<p>在配置数据库连接池数据源时，本来没有错误，结果加上编码转换格式后eclipse突然报错：</p>
<p>这是怎么回事？</p>
<p>经过查询，发现这个错误其实很好解决。</p>
<p>首先，原因是： <span style="color: rgba(255, 0, 0, 1)"><strong>.xml文件中 ‘ &amp; ’字符需要进行转义！！！</strong></span></p>
<p>看到这里，其实已经恍然大悟，那么，这个字符 ‘&nbsp;&amp;&nbsp;’ 需要怎么转义呢？看下面这张表：</p>
<p>在xml文件中有以下几类字符要进行转义替换：</p>
<p><img src="https://img2018.cnblogs.com/i-beta/1504448/201911/1504448-20191112001519575-807392055.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;<span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>所以，我们在xml文件中不能直接写 ‘ &amp; ’ 字符，而需要写成 ‘ &amp;amp; ’</strong></span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">&lt;?</span><span style="color: rgba(255, 0, 255, 1)">xml version="1.0" encoding="UTF-8"</span><span style="color: rgba(0, 0, 255, 1)">?&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">beans </span><span style="color: rgba(255, 0, 0, 1)">xmlns</span><span style="color: rgba(0, 0, 255, 1)">="http://www.springframework.org/schema/beans"</span><span style="color: rgba(255, 0, 0, 1)">
    xmlns:xsi</span><span style="color: rgba(0, 0, 255, 1)">="http://www.w3.org/2001/XMLSchema-instance"</span><span style="color: rgba(255, 0, 0, 1)">
    xmlns:aop</span><span style="color: rgba(0, 0, 255, 1)">="http://www.springframework.org/schema/aop"</span><span style="color: rgba(255, 0, 0, 1)">
    xsi:schemaLocation</span><span style="color: rgba(0, 0, 255, 1)">="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
        http://www.springframework.org/schema/aop
        http://www.springframework.org/schema/aop/spring-aop.xsd"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 管理DataSource </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">bean </span><span style="color: rgba(255, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">="dataSource"</span><span style="color: rgba(255, 0, 0, 1)">
        class</span><span style="color: rgba(0, 0, 255, 1)">="org.springframework.jdbc.datasource.DriverManagerDataSource"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> set方法注入属性，和类中的成员属性无关，和set方法名称有关，比如有一个属性叫username，但是set方法：setName </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="driverClassName"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="com.mysql.cj.jdbc.Driver"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 转义前 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="url"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="jdbc:mysql://localhost:3306/demo?useUnicode=true&amp;characterEncoding=UTF-8&amp;serverTimezone=Asia/Shanghai"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 转义后 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="url"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="jdbc:mysql://localhost:3306/demo?useUnicode=true&amp;amp;characterEncoding=UTF-8&amp;amp;serverTimezone=Asia/Shanghai"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="username"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="root"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">property </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="password"</span><span style="color: rgba(255, 0, 0, 1)"> value</span><span style="color: rgba(0, 0, 255, 1)">="root"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">bean</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 管理jdbcTemplate </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">bean </span><span style="color: rgba(255, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">="template"</span><span style="color: rgba(255, 0, 0, 1)">
        class</span><span style="color: rgba(0, 0, 255, 1)">="org.springframework.jdbc.core.JdbcTemplate"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">constructor-arg </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="dataSource"</span><span style="color: rgba(255, 0, 0, 1)"> ref</span><span style="color: rgba(0, 0, 255, 1)">="dataSource"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">constructor-arg</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">bean</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">beans</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
