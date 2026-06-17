---
title: "Mysql数据安全备份"
date: 2023-05-31
description: "数据安全备份的意义 在出现意外的时候(硬盘损坏、断点、黑客攻击)，以便数据的恢复 导出生产的数据以便研发人员或者测试人员测试学习 高权限的人员那操作失误导致数据丢失，以便恢复 备份类型 完全备份：对整个数据库的备份 部分备份：对数据进行部分备份(一张或多张表) 增量备份：是以上一次备份为基础来备份变"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14020293.html"
---

<h1 style="text-align: center">数据安全备份的意义</h1>
<ol>
<li>在出现意外的时候(硬盘损坏、断点、黑客攻击)，以便数据的恢复</li>
<li>导出生产的数据以便研发人员或者测试人员测试学习</li>
<li>高权限的人员那操作失误导致数据丢失，以便恢复</li>
</ol>
<h2>备份类型</h2>
<ul>
<li>完全备份：对整个数据库的备份</li>
<li>部分备份：对数据进行部分备份(一张或多张表)
<ul>
<li>增量备份：是以上一次备份为基础来备份变更数据</li>
<li>差异备份：是以第一次完全备份为基础来备份变更数据</li>
</ul>
</li>
</ul>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202011/1504448-20201122181117015-239488283.png" alt="" loading="lazy" /></p>
<h2>备份方式</h2>
<ul>
<li>逻辑备份：直接生成sql语句，在恢复数据的时候执行sql语句</li>
<li>物理备份：复制相关库文件，进行数据备份(<strong><span style="color: rgba(255, 0, 0, 1)">my.cnf指向的数据存放目录</span></strong>)</li>
</ul>
<h3>区别</h3>
<ol>
<li>逻辑备份效率低，恢复数据效率低，节约空间</li>
<li>物理备份浪费空间，备份数据效率快</li>
</ol>
<h2>备份场景</h2>
<ul>
<li>热备份：备份时，不影响数据库的读写操作</li>
<li>温备份：备份时，可以读，不能写</li>
<li>冷备份：备份时，关闭mysql服务，不能进行任何读写操作</li>
</ul>
<h1 style="text-align: center">Mysqldump备份(跨机器)</h1>
<h2>单库语法</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">备份基础语法：
mysqldump -u用户 -hip -p密码 数据库名 表名 | 压缩方式 &gt; 绝对路径+文件名<br></span></pre>
