---
title: "Django与MySQL数据库版本兼容问题"
date: 2020-03-08
description: "第一个Python与Django的兼容关系 1、python2.7支持到2020年 2、Django2.0后均不再支持python2 3、Django2.0是最后一个支持Python3.4的版本 4.目前为止开发学习最好用Django2.1 第二个Django与MySQL的兼容关系 1、Django"
tags:
  - "Django"
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10628646.html"
---

<p>第一个Python与Django的兼容关系</p>
<p>1、python2.7支持到2020年</p>
<p>2、Django2.0后均不再支持python2</p>
<p>3、Django2.0是最后一个支持Python3.4的版本</p>
<p>4.目前为止开发学习最好用Django2.1</p>
<p>第二个Django与MySQL的兼容关系</p>
<p>1、Django1无所谓</p>
<p>2、Django2.1不再支持MySQL5.5，必须5.6版本以上(<span style="color: rgba(255, 0, 0, 1)"><strong>这就是我写这个博客的原因，花费我很多时间</strong></span>)</p>
<div class="cnblogs_code"><img id="code_img_closed_a95ccc2e-4278-4fbe-8c48-413b41f8907d" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_a95ccc2e-4278-4fbe-8c48-413b41f8907d" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_a95ccc2e-4278-4fbe-8c48-413b41f8907d" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span> <span style="color: rgba(0, 0, 0, 1)">cmd状态下
</span><span style="color: rgba(0, 128, 128, 1)">2</span> <span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> django
</span><span style="color: rgba(0, 128, 128, 1)">3</span> django.VERSION()</pre>
