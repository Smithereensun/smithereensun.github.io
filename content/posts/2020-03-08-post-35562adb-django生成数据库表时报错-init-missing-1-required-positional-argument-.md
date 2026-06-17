---
title: "Django生成数据库表时报错 __init__() missing 1 required positional argument: 'on_delete'"
date: 2020-03-08
description: "原因： 在django2.0后，定义外键和一对一关系的时候需要加上on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错 例如： owner=models.ForeignKey(UserProfile) &gt;报错 owner=models.ForeignKey(UserPro"
tags:
  - "Django"
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10630875.html"
---

<p><span style="color: rgba(255, 0, 0, 1)"><strong>原因：</strong></span></p>
<p>　　在django2.0后，定义外键和一对一关系的时候需要加上on_delete选项，此参数为了避免两个表里的数据不一致问题，不然会报错</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>例如：</strong></span></p>
<p>　　owner=models.ForeignKey(UserProfile)---&gt;报错</p>
<p>　　owner=models.ForeignKey(UserProfile,on_delete=models.CASCADE) --在老版本这个参数（models.CASCADE）是默认值</p>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>参数说明：</strong></span></p>
<p>　　on_delete有CASCADE、PROTECT、SET_NULL、SET_DEFAULT、SET()五个可选的值</p>
<p>　　　　CASCADE:级联删除。</p>
<p>　　　　PROTECT:报完整性错误。</p>
<p>　　　　SET_NULL:将外键设置为null，前提是允许为null。</p>
<p>　　　　SET_DEFAULT:将外键设置为一个默认值</p>
<p>　　　　SET():调用外面的值，可以是一个函数</p>
<p>　　　　<span style="color: rgba(255, 0, 0, 1)"><strong>注:一般使用CASCADE就可以了。</strong></span></p>
