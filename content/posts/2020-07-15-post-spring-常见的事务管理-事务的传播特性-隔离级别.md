---
title: "Spring 常见的事务管理、事务的传播特性、隔离级别"
date: 2020-07-15
description: "事务管理 事务：多个操作，要么同时成功，要么失败后一起回滚 具备ACID四种特性 Atomic(原子性) Consistency(一致性) lsolation(隔离性) Durablility(持久性) 常见的Spring事务管理方式有那些 编程式事务 代码调用beginTransaction()、"
tags:
  - "Spring"
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13308689.html"
---

<h1 style="text-align: center">事务管理</h1>
<p>事务：多个操作，要么同时成功，要么失败后一起回滚</p>
<p>具备ACID四种特性</p>
<ul>
<li>Atomic(原子性)</li>
<li>Consistency(一致性)</li>
<li>lsolation(隔离性)</li>
<li>Durablility(持久性)</li>
</ul>
<p>常见的Spring事务管理方式有那些</p>
<ul>
<li><strong><span style="color: rgba(255, 0, 0, 1)">编程式事务</span></strong>
<ul>
<li>代码调用beginTransaction()、commit()、rollback()等事务管理相关的方法，通过TransactionTempalte手动管理事务(很少用)</li>
</ul>
</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>声明式事务管理(推荐)</strong></span>
<ul>
<li>通过AOP实现，可配置文件方式或注解方式实现事务的管理控制(较常见)</li>
</ul>
</li>
</ul>
<p>声明式事务管理本质</p>
<p>　　本质是对方法前后进行拦截，底层是建立在AOP的基础上</p>
<p>　　在目标方法开始之前创建或者加入一个事务，在执行完目标方法之后根据执行情况提交或者回滚事务</p>
<h1 style="text-align: center">事务传播行为</h1>
<p>　　如果在开始当前事务之前，一个事务上下文已经存在，此时有若干选项可以指定一个事务性方法的执行行为</p>
<ul>
<li>Transactional(propagation=Propagation.REQUIRED)：如果有事务，那么加入事务，没有的话新建一个（默认情况下）</li>
<li>@Transactional(propagation=Propagation.NOT_SUPPORTED)：不为这个方法开始事务</li>
<li>@Transactional(propagation=Propagation.REQUIRES_NEW)：不管是否存在事务，都创建一个新的事务，原来的挂起，新的执行完毕，继续执行老的事务</li>
<li>@Transactional(propagation=Propagation.MANDATORY)：必须在一个已有的事务中执行，否则抛出异常</li>
<li>@Transactional(propagation=Propagation.NEVER)：必须在一个没有事务中执行，否则抛出异常(与Propagation.MANDATORY相反)</li>
<li>@Transactional(propagation=Propagation.SUPPORTS)：如果其他bean调用这个方法，在其他bean中声明事务，那就用事务，如果其他bean没有声明事务，那就不用事务</li>
<li>@Transactional(propagation=Propagation.NESTED)：如果当前存在事务，则创建一个事务作为当前事务的嵌套事务来运行；如果当前没有事务，则该取值等价于Propagation.REQUIRED</li>
</ul>
<h1 style="text-align: center">事务隔离级别</h1>
<p>　　若干个并发的事务之间的隔离程度</p>
<ul>
<li>@Transactional(isolation=isolation.READ_UNCOMMITTED)：读取未提交数据(会出现脏读，不可重复读)基本不使用</li>
<li>@Transactional(isolation=isolation.READ_COMMITTED)：读取已提交数据(会出现不可重复读和幻读)</li>
<li>@Transactional(isolation=isolation.REPEATABLE_READ)：可重复读(会出现幻读)</li>
<li>@Transactional(isolation=isolation.SERIALIZABLE)：串行化</li>
</ul>
<p><strong><span style="color: rgba(255, 0, 0, 1)">MYSQL：默认为REPEATABLE_READ级别</span></strong></p>
<p>&nbsp;</p>
