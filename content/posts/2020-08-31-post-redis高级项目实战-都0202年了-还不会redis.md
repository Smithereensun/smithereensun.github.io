---
title: "Redis高级项目实战，都0202年了，还不会Redis？"
date: 2020-08-31
description: "导读 大家都听过1万小时定律，可事实真的是这样吗？做了1万小时的CRUD，不还只会CRUD吗，这年头不适当的更新自身下技术栈，出门和别人聊天吹牛的时候，都没拿的出手的，(⊙o⊙)…Redis没入门的童鞋不推荐往下看，先去脑补下Redis入门(点我直达)，SpringBoot整合Redis的教程(点我"
tags:
  - "技术干货"
  - "NoSql"
  - "Redis"
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13506946.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　大家都听过<span style="color: rgba(255, 0, 0, 1)"><strong>1万小时定律</strong></span>，可事实真的是这样吗？做了<span style="color: rgba(255, 0, 0, 1)"><strong>1万小时的CRUD</strong></span>，不还只会CRUD吗，这年头<span style="color: rgba(255, 0, 0, 1)"><strong>不</strong></span>适当的<strong><span style="color: rgba(255, 0, 0, 1)">更新自身下技术栈</span></strong>，<span style="color: rgba(255, 0, 0, 1)"><strong>出门</strong></span>和别人<span style="color: rgba(255, 0, 0, 1)"><strong>聊天吹牛</strong></span>的时候，都没拿的出手的，(⊙o⊙)…<span style="color: rgba(255, 0, 0, 1)"><strong>Redis没入门的童鞋不推荐往下看</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>先去脑补下Redis入门</strong></span>(<a href="https://www.cnblogs.com/chenyanbin/p/12073107.html" target="_blank">点我直达</a>)，<span style="color: rgba(255, 0, 0, 1)"><strong>SpringBoot整合Redis的教程</strong></span>(<a href="https://www.cnblogs.com/chenyanbin/p/13515268.html" target="_blank">点我直达</a>)，<strong><span style="color: rgba(255, 0, 0, 1)">Redis实战秒杀</span></strong>(<a href="https://www.cnblogs.com/chenyanbin/p/13587508.html" target="_blank">点我直达</a>)，这篇不会讲浅的知识点！！！！</p>
<h2>面试专题</h2>
<h3><span style="color: rgba(255, 0, 0, 1)"><strong>什么是分布式锁？</strong></span></h3>
<p>　　首先，为了确保分布式锁可用，至少要满足以下三个条件</p>
<ol>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>互斥性</strong></span>。在任意时刻，只有一个客户端能持有锁</li>
<li><strong><span style="color: rgba(255, 0, 0, 1)">不会发生死锁</span></strong>。即便有一个客户端在持有锁的期间奔溃而没有主动解锁，也能保证后续其他客户端能加锁</li>
<li>解铃还须系铃人。<span style="color: rgba(255, 0, 0, 1)"><strong>加锁</strong></span>和<span style="color: rgba(255, 0, 0, 1)"><strong>解锁必须是同一个客户端</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>客户端</strong></span>自己<span style="color: rgba(255, 0, 0, 1)"><strong>不能把别人加的锁给解了</strong></span></li>
</ol>
<h3><span style="color: rgba(255, 0, 0, 1)"><strong>实现分布式锁方式？</strong></span></h3>
<p>　　两种实现，下面都会有讲到</p>
<ol>
<li>采用<span style="color: rgba(255, 0, 0, 1)"><strong>lua脚本</strong></span>操作分布式锁</li>
<li>采用<span style="color: rgba(255, 0, 0, 1)"><strong>setnx、setex命令连用</strong></span>的方式实现分布式锁</li>
</ol>
<h1 style="text-align: center">分布式锁的场景</h1>
<h2>什么是分布式锁？</h2>
<ul>
<li><strong><span style="color: rgba(255, 0, 0, 1)">分布式锁</span></strong>是<span style="color: rgba(255, 0, 0, 1)"><strong>控制分布式系统</strong></span>或<span style="color: rgba(255, 0, 0, 1)"><strong>不同系统</strong></span>之间<span style="color: rgba(255, 0, 0, 1)"><strong>共同访问共享资源的</strong></span>一种<span style="color: rgba(255, 0, 0, 1)"><strong>锁</strong></span>实现</li>
<li>如果不同的系统或同一个系统的不同主机之间共享了某个资源时，往往通过互斥来防止彼此干扰</li>
</ul>
<h2>为什么要有分布式锁？</h2>
<p>　　可以<span style="color: rgba(255, 0, 0, 1)"><strong>保证</strong></span>在<span style="color: rgba(255, 0, 0, 1)"><strong>分布式</strong></span>部署的<span style="color: rgba(255, 0, 0, 1)"><strong>应用集群</strong></span>中，<span style="color: rgba(255, 0, 0, 1)"><strong>同</strong></span>一个<span style="color: rgba(255, 0, 0, 1)"><strong>方法</strong></span>在同一<span style="color: rgba(255, 0, 0, 1)"><strong>操作</strong></span>只能<span style="color: rgba(255, 0, 0, 1)"><strong>被</strong><strong>一台机器</strong></span>上的<span style="color: rgba(255, 0, 0, 1)"><strong>一个线程执行</strong></span>。</p>
<h3>设计要求</h3>
<ol>
<li>可<span style="color: rgba(255, 0, 0, 1)"><strong>重入</strong></span>锁(避免死锁)</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>获取</strong></span>锁和<span style="color: rgba(255, 0, 0, 1)"><strong>释放</strong></span>锁<strong><span style="color: rgba(255, 0, 0, 1)">高可用</span></strong></li>
<li><strong><span style="color: rgba(255, 0, 0, 1)">获取</span></strong>锁和<strong><span style="color: rgba(255, 0, 0, 1)">释放</span></strong>锁<span style="color: rgba(255, 0, 0, 1)"><strong>高性能</strong></span></li>
</ol>
<h2>实现方案</h2>
<ol>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>获取锁</strong></span>，使用<span style="color: rgba(255, 0, 0, 1)"><strong>setnx()</strong></span>：SETNX key val：当且仅当key不存在时，set一个key为val的字符串，返回1</li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>若<span style="color: rgba(255, 0, 0, 1)">k</span>ey存在，则什么都不做</strong></span>，返回【0】加锁，锁的value值为当前占有锁服务器内网IP编号拼接任务标识</li>
<li>在<span style="color: rgba(255, 0, 0, 1)"><strong>释放锁</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>时</strong></span>候进行判断。并<span style="color: rgba(255, 0, 0, 1)"><strong>使用expire</strong></span>命令<span style="color: rgba(255, 0, 0, 1)"><strong>为锁添加一个超时时间</strong></span>，超过该时间则<span style="color: rgba(255, 0, 0, 1)"><strong>自动释放锁</strong></span></li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>返回1</strong></span>则<span style="color: rgba(255, 0, 0, 1)"><strong>成功获取锁</strong></span>。<span style="color: rgba(255, 0, 0, 1)"><strong>还设置</strong></span>一个<span style="color: rgba(255, 0, 0, 1)"><strong>获取</strong></span>的<span style="color: rgba(255, 0, 0, 1)"><strong>超时时间</strong></span>，若<span style="color: rgba(255, 0, 0, 1)"><strong>超过</strong></span>这个<span style="color: rgba(255, 0, 0, 1)"><strong>时间</strong></span>则<span style="color: rgba(255, 0, 0, 1)"><strong>放弃获取锁</strong></span>，<span style="color: rgba(255, 0, 0, 1)"><strong>setex</strong></span>(key,value,expire)过期<span style="color: rgba(255, 0, 0, 1)"><strong>以秒为单位</strong></span></li>
<li><span style="color: rgba(255, 0, 0, 1)"><strong>释放锁</strong></span>的时候，<span style="color: rgba(255, 0, 0, 1)"><strong>判断</strong></span>是不是该<span style="color: rgba(255, 0, 0, 1)"><strong>锁</strong></span>(即value为当前服务器内网IP编号拼接任务标识)，若是该锁，则<strong><span style="color: rgba(255, 0, 0, 1)">执行delete</span></strong>进行<span style="color: rgba(255, 0, 0, 1)"><strong>锁释放</strong></span></li>
</ol>
<h1 style="text-align: center">Redis分布式锁的实现</h1>
<h2>创建一个SpringBoot工程</h2>
<p>网址：https://start.spring.io/</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200814222311751-1772794455.png" alt="" loading="lazy" /></p>
<h3>步骤</h3>
<p>　　1、启动类上加上注解@EnableScheduling</p>
<p>　　2、执行方法上加上注解@Scheduled</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200814230859253-524877502.png" alt="" loading="lazy" /></p>
<h2>打包并上传至Linux服务器中启动</h2>
<p>　　准备3台Linux服务器，并将打好的jar包，上传至3台服务器中，然后启动</p>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202008/1504448-20200814231810279-2069054679.png" alt="" loading="lazy" /></p>
<h3>nohub之持久化启动方式&nbsp;</h3>
<div class="cnblogs_code">
<pre>nohup java -jar jar名称 &amp;</pre>
