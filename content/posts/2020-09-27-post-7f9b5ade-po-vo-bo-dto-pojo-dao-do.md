---
title: "PO、VO、BO、DTO、POJO、DAO、DO"
date: 2020-09-27
description: "DO： domain object持久对象就是从现实世界中抽象出来的有形或无形的业务实体。 PO：persistant object持久对象最形象的理解就是一个PO就是数据库中的一条记录。好处是可以把一条记录作为一个对象处理，可以方便的转为其它对象。 BO：business object业务对象主要"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13741039.html"
---

<p>DO：</p>
<p><em id="__mceDel">domain object持久对象<br>就是从现实世界中抽象出来的有形或无形的业务实体。</em></p>
<p>PO：<br>persistant object持久对象<br>最形象的理解就是一个PO就是数据库中的一条记录。<br>好处是可以把一条记录作为一个对象处理，可以方便的转为其它对象。</p>
<p>BO：<br>business object业务对象<br>主要作用是把业务逻辑封装为一个对象。这个对象可以包括一个或多个其它的对象。<br>比如一个简历，有教育经历、工作经历、社会关系等等。<br>我们可以把教育经历对应一个PO，工作经历对应一个PO，社会关系对应一个PO。<br>建立一个对应简历的BO对象处理简历，每个BO包含这些PO。<br>这样处理业务逻辑时，我们就可以针对BO去处理。</p>
<p>VO ：<br>value object值对象<br>ViewObject表现层对象<br>主要对应界面显示的数据对象。对于一个WEB页面，或者SWT、SWING的一个界面，用一个VO对象对应整个界面的值。</p>
<p>DTO ：<br>Data Transfer Object数据传输对象<br>主要用于远程调用等需要大量传输对象的地方。<br>比如我们一张表有100个字段，那么对应的PO就有100个属性。<br>但是我们界面上只要显示10个字段，<br>客户端用WEB service来获取数据，没有必要把整个PO对象传递到客户端，<br>这时我们就可以用只有这10个属性的DTO来传递结果到客户端，这样也不会暴露服务端表结构.到达客户端以后，如果用这个对象来对应界面显示，那此时它的身份就转为VO</p>
<p>POJO ：<br>plain ordinary java object 简单ava对象<br>个人感觉POJO是最参见最多变的对象，是一个中间对象，也是我们最常打交道的对象。<br>一个POJO持久化以后就是PO<br>直接用它传递、传递过程中就是DTO<br>直接用来对应表示层就是VO</p>
<p>DAO：<br>data access object数据访问对象<br>这个大家最熟悉，和上面几个O区别最大，基本没有互相转化的可能性和必要.<br>主要用来封装对数据库的访问。通过它可以把POJO持久化为PO，用PO组装出来VO、DTO</p>
