---
title: "SpringCloud整合分布式事务Seata 1.4.1 支持微服务全局异常拦截"
date: 2023-08-07
description: "项目依赖 SpringBoot 2.5.5 SpringCloud 2020.0.4 Alibaba Spring Cloud 2021.1 Mybatis Plus 3.4.0 Seata 1.4.1（需要与服务器部署的Seata版本保持一致） 。。。。 Seata介绍 什么是Seata 一个开源"
tags:
  - "Spring Boot"
  - "Spring Cloud"
  - "Seata 1.4.x"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/seata.html"
---

<h1 style="text-align: center">项目依赖</h1>
<ul>
<li>SpringBoot 2.5.5</li>
<li>SpringCloud 2020.0.4</li>
<li>Alibaba Spring Cloud 2021.1</li>
<li>Mybatis Plus 3.4.0</li>
<li><strong><span style="color: rgba(255, 0, 0, 1)">Seata 1.4.1<span style="color: rgba(0, 0, 0, 1)">（</span>需要与服务器部署的Seata版本保持一致<span style="color: rgba(0, 0, 0, 1)">）</span></span></strong></li>
<li><strong><span style="color: rgba(255, 0, 0, 1)"><span style="color: rgba(0, 0, 0, 1)">。。。。</span></span></strong></li>
</ul>
<h1 style="text-align: center">Seata介绍</h1>
<h2 id="什么是seata">什么是Seata<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/14802471.html#什么是seata"><br></a></h2>
<ul>
<li>一个开源分布式事务框架，由阿里中间件团队发起的开源项目Fescar，后更名为Seata</li>
<li>中文文档地址：<a href="http://seata.io/zh-cn/docs/user/quickstart.html" rel="noopener nofollow" target="_blank">http://seata.io/zh-cn/docs/user/quickstart.html</a></li>





</ul>
<h2 id="seata三大组件">Seata三大组件<a class="esa-anchor" href="https://www.cnblogs.com/chenyanbin/p/14802471.html#seata三大组件"><br></a></h2>
<ul>
<li>TC：Transaction Coordinator事务协调器，管理全局的分支事务的状态，用于全局性事务的提交和回滚</li>
<li>TM：Transaction Manager 事务管理器，用户开启、提交或者回滚【全局事务】</li>
<li>RM：Resource Manager资源管理器，用于分支事务上的资源管理，向TC注册分支事务，上报分支事务的状态，接收TC的命令来提交或者回滚分支事务
<ul>
<li>传统XA协议实现2PC方案的RM是在数据库层，RM本质上就是数据库自身</li>
<li>Seata的RM是以jar包的形式嵌入在应用程序里面</li>





</ul>





</li>





</ul>
<h4>架构：TC为单独部署的Server服务端，TM和RM为嵌入到应用中的Client客户端</h4>
<p><img src="https://img2022.cnblogs.com/blog/1504448/202210/1504448-20221021094948726-160032493.png" alt="" loading="lazy" /></p>
<p>&nbsp;</p>
<h4>XID</h4>
<ul>
<li>TM请求TC开启一个全局事务，TC会生成一个XID作为该全局事务的编号XID，XID会在微服务的调用链路中传播，保证将多个微服务对的子事务关联在一起</li>





</ul>
<h1 style="text-align: center">Seata部署安装</h1>
<h2>下载Seata地址</h2>
<p><a href="http://seata.io/zh-cn/blog/download.html" rel="noopener nofollow" target="_blank">http://seata.io/zh-cn/blog/download.html</a></p>
<p><img src="https://img2022.cnblogs.com/blog/1504448/202210/1504448-20221021095434610-427572378.png" alt="" loading="lazy" /></p>
<p>　　<span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>注：我这边下载的是1.4.1，seata部署版本需要与SpringBoot依赖的版本相对应！！！！！！</strong></span></p>
<h2>Seata部署</h2>
<h3>前期准备</h3>
<p>　　准备好Nacos、mysql</p>
<p>　　<span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>注：nacos配置中心数据是持久化到mysql的！！！！</strong></span></p>
<h3>部署&amp;修改配置</h3>
<h4>修改存储模式DB</h4>
<p>　　上传至服务器，目录为：/usr/local/software</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)"># 1、创建目录
mkdir -p /usr/local/software

# 2、解压
unzip seata-server-1.4.1.zip

# 3、修改存储模式 DB
cd seata/conf/
vi file.conf</span></pre>
