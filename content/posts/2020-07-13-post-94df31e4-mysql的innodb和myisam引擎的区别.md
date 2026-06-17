---
title: "Mysql的Innodb和MyISAM引擎的区别"
date: 2020-07-13
description: "区别项 Innodb MyISAM 事务 支持 不支持 锁粒度 行锁，适合高并发 表锁，不适合高并发 是否默认 默认 非默认 支持外键 支持外键 不支持 适合场景 读写均衡，写大于读场景，需要事务 读多写少场景，不需要事务 全文索引 可以通过插件实现，更多使用ElasticSearch 支持全文索引"
tags:
  - "SQL"
  - "SQL优化"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13296539.html"
---

<table border="0">
<tbody>
<tr>
<td>区别项</td>
<td>Innodb</td>
<td>MyISAM</td>
</tr>
<tr>
<td>&nbsp;事务</td>
<td>&nbsp;支持</td>
<td>&nbsp;不支持</td>
</tr>
<tr>
<td>锁粒度&nbsp;</td>
<td>行锁，适合高并发</td>
<td>表锁，不适合高并发&nbsp;</td>
</tr>
<tr>
<td>是否默认&nbsp;</td>
<td>默认&nbsp;</td>
<td>非默认&nbsp;</td>
</tr>
<tr>
<td>支持外键&nbsp;</td>
<td>支持外键&nbsp;</td>
<td>不支持&nbsp;</td>
</tr>
<tr>
<td>适合场景&nbsp;</td>
<td>读写均衡，写大于读场景，需要事务&nbsp;</td>
<td>读多写少场景，不需要事务&nbsp;</td>
</tr>
<tr>
<td>全文索引&nbsp;</td>
<td>可以通过插件实现，更多使用ElasticSearch&nbsp;</td>
<td>支持全文索引&nbsp;</td>
</tr>
</tbody>
</table>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>重点：MyISAM不支持事务，如果需要事务则改为Innodb引擎，更改数据库的表里面的索引</strong></span></p>
