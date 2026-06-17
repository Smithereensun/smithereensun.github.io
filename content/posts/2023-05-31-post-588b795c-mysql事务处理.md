---
title: "MySQL事务处理"
date: 2023-05-31
description: "概述 在MySQL中只有使用了InnoDB数据库存储引擎的数据库或表才支持事务。 事务处理可以用来维护数据库的完整性，保证成批的SQL语句要么全部成功，要么全部失败。 事务用来管理DDL、DML、DCL操作，比如：insert、update、delete语句，默认是自动提交的。 一般来讲，事务是必须"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13127927.html"
---

<h1 style="text-align: center">概述</h1>
<ul>
<li>在MySQL中只有使用了<span style="color: rgba(255, 0, 0, 1)"><strong>InnoDB</strong></span>数据库存储引擎的数据库或表<span style="color: rgba(255, 0, 0, 1)"><strong>才支持事务</strong></span>。</li>
<li>事务处理可以用来维护数据库的完整性，保证成批的SQL语句要么全部成功，要么全部失败。</li>
<li>事务用来管理<span style="color: rgba(255, 0, 0, 1)"><strong>DDL、DML、DCL</strong></span>操作，比如：<span style="color: rgba(255, 0, 0, 1)"><strong>insert、update、delete</strong></span>语句，<span style="color: rgba(255, 0, 0, 1)"><strong>默认是自动提交的</strong></span>。</li>
</ul>
<p>一般来讲，事务是必须满足4个条件（ACID）</p>
<ol>
<li>Atomicity(原子性)</li>
<li>Consistency(一致性)</li>
<li>Isolation(隔离性) --&gt;由MVCC的锁机制来实现的<ol>
<li>MVCC：优化读写性能(读不加锁，读写不冲突。不能优化读读和写写这种情况)</li>
</ol></li>
<li>Durabolity(持久性)</li>
</ol>
<p>对于ACID的解释如下：</p>
<ol>
<li>原子性：构成事务的所有操作必须是一个逻辑单元，要么全部成功，要么全部失败。</li>
<li>一致性：数据库再事务执行前后状态都必须是确定的或者是一致的。</li>
<li>隔离性：事务之间不会相互影响。</li>
</ol>
<h1 style="text-align: center">事务支持</h1>
<p>　　在MySQL命令行的<span style="color: rgba(255, 0, 0, 1)"><strong>默认</strong></span>设置下，<span style="color: rgba(255, 0, 0, 1)"><strong>事务都是自动提交的</strong></span>，既执行SQL语句后就会马上执行COMMIT操作，因此要<span style="color: rgba(255, 0, 0, 1)"><strong>显式地开启一个事务</strong></span>必须<span style="color: rgba(255, 0, 0, 1)"><strong>使用命令BEGIN或START TRANSACTION，或者执行命令 SET AUTOCOMMIT=0</strong></span>，用来禁止使用当前会话的自动提交。</p>
<h2>常见的操作</h2>
<ul>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>BEGIN或START TRANSACTION</strong></span>：显式地开启一个事务；</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>COMMIT也可以使用COMMIT WORK</strong></span>，不过二者是等价的，COMMIT会提交事务，并使已对数据库进行的所有修改成为永久性的</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>ROLLBACK也可以使用ROLLBACK WORK</strong></span>，不过二者是等价的，回滚回话结束用户的事务，并撤销正在进行的所有未提交的修改。</li>
</ul>
<h1 style="text-align: center">事务并发问题</h1>
<p>在事务的<span style="color: rgba(255, 0, 0, 1)"><strong>并发操作</strong></span>中可能会出现一些问题：</p>
<ul>
<li>丢失更新：一个事务更新之后，另一个事务也更新了，但是第二个事务回滚了，则第一个事务也被回滚了</li>
<li>脏读：一个事务读取到另一个事务未提交的数据</li>
<li>不可重复读：一个事务因<span style="color: rgba(255, 0, 0, 1)"><strong>读取到另一个事务</strong><strong>已提交的数据</strong></span>，导致对同一条记录读取两次以上的结果不一致，update操作。</li>
<li>幻读：一个事务因读取到另一个事务已提交的数据。导致对同一张表读取两次以上的结果不一致，insert、delete操作</li>
</ul>
<h1 style="text-align: center">事务隔离级别</h1>
<p>　　为了避免上面出现的几种情况，在MySQL规范中，定义了4个事务隔离级别，不同隔离级别对事物的处理不同</p>
<p>由低到高：</p>
<ol>
<li>Read uncommitted(读未提交)：最低级别，任何情况都无法保证。</li>
<li>Read committed(读已提交)：可避免脏读的发生。</li>
<li>Repeatable read(可重复读)：可避免脏读，不可重复读的发生。</li>
<li>Serializable(串行化)：可避免脏读，不可重复读，幻读的发生。</li>
</ol>
<h2>默认隔离级别</h2>
<p>　　大多数据库的默认隔离级别是Read committed</p>
<h2>查看隔离级别</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">select</span> <span style="color: rgba(0, 128, 0, 1); font-weight: bold">@@tx_isolation</span></pre>
