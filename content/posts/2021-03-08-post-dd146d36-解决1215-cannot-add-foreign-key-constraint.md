---
title: "解决1215 - cannot add foreign key constraint"
date: 2021-03-08
description: "1215 - cannot add foreign key constraint发生在为数据表添加外键时，一旦发生，还是挺痛苦的。 情况一：数据表存储引擎不一致 我们看到，只有InnoDB是支持外键的。这就要求在指定外键时，两张表的引擎都要保证是InnoDB。如果这两张表任意一张表的引擎不是Inno"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14502355.html"
---

<p><code>1215 - cannot add foreign key constraint</code>发生在为数据表添加外键时，一旦发生，还是挺痛苦的。</p>
<h1 id="item-1" style="text-align: center">情况一：数据表存储引擎不一致</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202103/1504448-20210308212354383-1554151065.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>我们看到，只有InnoDB是支持外键的。这就要求在指定外键时，两张表的引擎都要保证是InnoDB。如果这两张表任意一张表的引擎不是<code>InnoDB</code>，那么都会报<code>1215 - cannot add foreign key constraint</code>错误。</p>
<p>解决方法：在navicat中我们这么查看。数据表-&gt;找到表-&gt;设计表</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202103/1504448-20210308212409720-1667208748.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>&nbsp;两张表，都保证是InnoDb就可以了。</p>
<h1 id="item-2" style="text-align: center">情况二：在父表中，相关的ID不存在</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202103/1504448-20210308212447380-1738158784.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h1 id="item-3" style="text-align: center">情况三：两个字段的类型不一样</h1>
<p>添加外键时要保证类型完全一样，不能一个是<code>int</code>，另一个是<code>bigint</code>。也不能一个是有符号的<code>int</code>，另一个是无符号的<code>int</code>。也不能一样长度为1， 另一个长度为2。在实际的使用中，这种情况会出现在类型与有无符号上。解决的方法也简单：将两个字段的类型、长度、有无符号设置一致了就行了。</p>
<h1 id="item-4" style="text-align: center">情况四：即是外键，也是主键</h1>
<p>比如我们把数据表中的某个字段设置为了主键，那么此主键是必然不能为<code>null</code>。此时，我们又设置其为外键。但在设置删除策略时，却不小把它设置为：删除时设置为<code>null</code>。则会发生上述异常。</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202103/1504448-20210308212536860-721349821.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>原因其实刚才已经阐述了：是主键，则数据必然不能为<code>null</code>,与我们设置的策略：外键对应的表中的数据删除时，将此数据设置为<code>null</code>冲突。解决方法：设置策略为<code>No Action</code>或<code>Restrict</code>，这两个值的意思一样，同为：在删除时检查约束，如果存在外键，则报约束性异常。&nbsp;</p>
<h1 id="item-5" style="text-align: center">情况五：字段属性与删除时触发事件冲突</h1>
<p>比如，我们设置删除时<code>set null</code></p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202103/1504448-20210308212617199-1023889273.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>&nbsp;然后这个字段在本表的属性却为：</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202103/1504448-20210308212628928-137488561.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<p>则也会发生<code>1215 - cannot add foreign key constraint</code>。原因相信大家也猜大了，如果我们这样设置了，一旦发生外键的删除操作，就要按我们的设置将此字段设置为<code>null</code>，但我们同时又设置了此字估不能为<code>null</code>。当然就会发生错误了。为了规避这个错误，<code>mysql</code>&nbsp;会在设置外键时，发生<code>1215 - cannot add foreign key constraint</code>&nbsp;</p>
<h1 style="text-align: center">情况六：主外键字段字符集不一样</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202103/1504448-20210308212733407-73399667.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
