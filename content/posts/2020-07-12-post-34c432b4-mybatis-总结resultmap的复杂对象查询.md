---
title: "Mybatis 总结ResultMap的复杂对象查询"
date: 2020-07-12
description: "association：映射的是一个POJO类，处理一对一的关联关系 collection：映射的一个集合列表，处理的是一对多的关联关系 模版 &lt;!--column不做限制，可以为任意表的字段，而property须为type，定义的pojo属性--&gt; &lt;resultMap id=&"
tags:
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13290797.html"
---

<ul>
<li>association：映射的是一个POJO类，处理一对一的关联关系</li>
<li>collection：映射的一个集合列表，处理的是一对多的关联关系</li>
</ul>
<p>模版</p>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)">column不做限制，可以为任意表的字段，而property须为type，定义的pojo属性</span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">resultMap </span><span style="color: rgba(255, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">="唯一的标识"</span><span style="color: rgba(255, 0, 0, 1)"> type</span><span style="color: rgba(0, 0, 255, 1)">="映射的POJO对象"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">id </span><span style="color: rgba(255, 0, 0, 1)">column</span><span style="color: rgba(0, 0, 255, 1)">="表的一个字段"</span><span style="color: rgba(255, 0, 0, 1)"> jdbcType</span><span style="color: rgba(0, 0, 255, 1)">="字段类型"</span><span style="color: rgba(255, 0, 0, 1)"> property</span><span style="color: rgba(0, 0, 255, 1)">="映射到POJO对象的一个属性"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">association </span><span style="color: rgba(255, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">="POJO的一个对象属性"</span><span style="color: rgba(255, 0, 0, 1)"> javaType</span><span style="color: rgba(0, 0, 255, 1)">="POJO关联的POJO对象"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">id </span><span style="color: rgba(255, 0, 0, 1)">column</span><span style="color: rgba(0, 0, 255, 1)">="关联POJO对象对应表的主键字段"</span><span style="color: rgba(255, 0, 0, 1)"> jdbcType</span><span style="color: rgba(0, 0, 255, 1)">="字段类型"</span><span style="color: rgba(255, 0, 0, 1)"> property</span><span style="color: rgba(0, 0, 255, 1)">="关联POJO对象的属性"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">result </span><span style="color: rgba(255, 0, 0, 1)">column</span><span style="color: rgba(0, 0, 255, 1)">="表的字段"</span><span style="color: rgba(255, 0, 0, 1)"> jdbcType</span><span style="color: rgba(0, 0, 255, 1)">="字段类型"</span><span style="color: rgba(255, 0, 0, 1)"> property</span><span style="color: rgba(0, 0, 255, 1)">="关联POJO对象的属性"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">result</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">association</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 128, 0, 1)">&lt;!--</span><span style="color: rgba(0, 128, 0, 1)"> 集合中的property需要为ofType定义的POJO对象的属性 </span><span style="color: rgba(0, 128, 0, 1)">--&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">collection </span><span style="color: rgba(255, 0, 0, 1)">property</span><span style="color: rgba(0, 0, 255, 1)">="POJO的集合属性名称"</span><span style="color: rgba(255, 0, 0, 1)"> ofType</span><span style="color: rgba(0, 0, 255, 1)">="集合中单个的POJO对象类型"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">id </span><span style="color: rgba(255, 0, 0, 1)">column</span><span style="color: rgba(0, 0, 255, 1)">="集合中POJO对象对应在表的主键字段"</span><span style="color: rgba(255, 0, 0, 1)"> jdbcType</span><span style="color: rgba(0, 0, 255, 1)">="字段类型"</span><span style="color: rgba(255, 0, 0, 1)"> property</span><span style="color: rgba(0, 0, 255, 1)">="集合中POJO对象的主键属性"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">id</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
            <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">result </span><span style="color: rgba(255, 0, 0, 1)">column</span><span style="color: rgba(0, 0, 255, 1)">="任意表的字段"</span><span style="color: rgba(255, 0, 0, 1)"> jdbcType</span><span style="color: rgba(0, 0, 255, 1)">="字段类型"</span><span style="color: rgba(255, 0, 0, 1)"> property</span><span style="color: rgba(0, 0, 255, 1)">="集合中的POJO对象的属性"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">result</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
        <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">collection</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
    <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">resultMap</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
