---
title: "mybatis #{}和${}区别"
date: 2023-05-31
description: "区别1 #{}：相当于JDBC Sql语句中的占位符?(PreparedStatement)，可以防止Sql注入 ${}：相当于JDBC Sql语句中的连接符号+(Statement)，不能防止Sql注入 区别2 #{}：进行输入映射的时候，会对参数进行类型解析(如果是String类型，那么Sql语"
tags:
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12901693.html"
---

<h1>区别1</h1>
<ul>
<li>#{}：相当于JDBC Sql语句中的占位符<span style="color: rgba(255, 0, 0, 1)"><strong>?</strong></span>(<span style="color: rgba(255, 0, 0, 1)"><strong>PreparedStatement</strong></span>)，<span style="color: rgba(255, 0, 0, 1)"><strong>可以防止Sql注入</strong></span></li>
<li>${}：相当于JDBC Sql语句中的连接符号<span style="color: rgba(255, 0, 0, 1)"><strong>+</strong></span>(<span style="color: rgba(255, 0, 0, 1)"><strong>Statement</strong></span>)，<span style="color: rgba(255, 0, 0, 1)"><strong>不能防止Sql注入</strong></span></li>
</ul>
<h1>区别2</h1>
<ul>
<li>#{}：进行输入映射的时候，会对参数进行<span style="color: rgba(255, 0, 0, 1)"><strong>类型解析(</strong></span>如果是String类型，那么Sql语句会自动加上' ')</li>
<li>${}：进行输入映射的时候，将参数<span style="color: rgba(255, 0, 0, 1)"><strong>原样输出到SQL语句中</strong></span> --&gt;<strong><span style="color: rgba(255, 0, 0, 1)">相当于replace替换相应位置的值</span></strong></li>
</ul>
<p>　　<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1)"><strong>注：模糊搜索时，注意使用的是${}，如果使用的是#{}，会在两头加上''，此时sql语句变成：select * from user where username like '%'张三'%'；这样不就报错了嘛</strong></span></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200516183707779-45430324.png" alt="" /></p>
<h1>区别3</h1>
<ul>
<li>#{}：如果进行<span style="color: rgba(255, 0, 0, 1)"><strong>简单类型</strong></span>(String、Date、8种基本类型的包装类)的输入映射时，#{}中参数名称可以任意</li>
<li>${}：如果进行<span style="color: rgba(255, 0, 0, 1)"><strong>简单类型</strong></span>(String、Date、8种基本类型的包装类)的输入映射时，#{}中参数名称<span style="color: rgba(255, 0, 0, 1)"><strong>必须是value</strong></span></li>
</ul>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200516192605640-1137886110.png" alt="" /></p>
<p>&nbsp;</p>
