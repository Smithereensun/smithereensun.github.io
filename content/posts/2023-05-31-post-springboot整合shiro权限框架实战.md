---
title: "SpringBoot整合Shiro权限框架实战"
date: 2023-05-31
description: "什么是ACL和RBAC ACL Access Control list：访问控制列表 优点：简单易用，开发便捷 缺点：用户和权限直接挂钩，导致在授予时的复杂性，比较分散，不便于管理 例子：常见的文件系统权限设计，直接给用户加权限 RBAC Role Based Access Control：基于角色"
tags:
  - "Shiro"
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/shiro.html"
---

<h1 style="text-align: center">什么是ACL和RBAC</h1>
<h2>ACL</h2>
<ul>
<li>Access Control list：访问控制列表</li>
<li>优点：简单易用，开发便捷</li>
<li>缺点：用户和权限直接挂钩，导致在授予时的复杂性，比较分散，不便于管理</li>
<li>例子：常见的文件系统权限设计，直接给用户加权限</li>
</ul>
<h2>RBAC</h2>
<ul>
<li>Role Based Access Control：基于角色的访问控制</li>
<li>权限与角色相关联，用户通过成为适当角色的成员而得到这些角色的权限</li>
<li>优点：简化了用户与权限的管理，通过对用户进行分类，使得角色与权限关联起来</li>
<li>缺点：开发比ACL相对复杂</li>
<li>例子：基于RBAC模型的权限验证框架，Apache Shiro</li>
</ul>
<h1 style="text-align: center">什么是Apache Shiro</h1>
<h2>官网地址</h2>
<p><a href="https://shiro.apache.org/" target="_blank" rel="noopener nofollow">点我直达</a></p>
<h2>介绍</h2>
<p>　　Apache Shiro是一个强大且易用的Java安全框架,执行身份<span style="color: rgba(255, 0, 0, 1)"><strong>验证、授权、密码和会话管理</strong></span>。使用Shiro的易于理解的API,您可以快速、轻松地获得任何应用程序,从最小的移动应用程序到最大的网络和企业应用程序。</p>
<h2>什么是身份认证</h2>
<p>　　Authentication，身份认证，一般就是登陆校验</p>
<h2>什么是授权</h2>
<p>　　Authorization，给用户分配角色或者访问某些资源的权限</p>
<h2>什么是会话管理</h2>
<p>　　Session Management，用户的会话管理员，多数情况下是web session</p>
<h2>什么是加密</h2>
<p>　　Cryptography，数据加密，比如密码加解密</p>
<h2>核心概念</h2>
<h3>Subject</h3>
<p>　　我们把<span style="color: rgba(255, 0, 0, 1)"><strong>用户或者程序称为主体</strong></span>，主体去访问系统或者资源</p>
<h3>SecurityManager</h3>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>安全管理器</strong></span>，Subject的认证和授权都要在安全管理器下进行</p>
<h3>Realm</h3>
<p>　　数据域，<span style="color: rgba(255, 0, 0, 1)"><strong>Shiro和安全数据的连接器</strong></span>，通过realm获取认证授权相关信息</p>
<h3>Authenticator</h3>
<p>　　认证器，主要<span style="color: rgba(255, 0, 0, 1)"><strong>负责Subject的认证</strong></span></p>
<h3>Authorizer</h3>
<p>　　授权器，主要负责Subject的授权，<span style="color: rgba(255, 0, 0, 1)"><strong>控制Subject拥有的角色或者权限</strong></span></p>
<h3>Crytography</h3>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>加解密</strong></span>，Shiro的包含易于使用和理解的数据加解密方法，简化了很多复杂的API</p>
<h3>Cache Manager</h3>
<p>　　<span style="color: rgba(255, 0, 0, 1)"><strong>缓存管理器</strong></span>，比如认证或授权信息，通过缓存进行管理，提高性能</p>
<h1 style="text-align: center">快速上手</h1>
<h2>构建项目</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202012/1504448-20201227192333364-2049351510.png" alt="" loading="lazy" /></p>
<h2>认证和授权</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202012/1504448-20201227200058504-924418686.gif" alt="" loading="lazy" /></p>
<div class="cnblogs_code"><img src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" id="code_img_closed_9ce7fee0-8a9f-4fc6-8125-15c9c1500c9f" class="code_img_closed" /><img src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" id="code_img_opened_9ce7fee0-8a9f-4fc6-8125-15c9c1500c9f" class="code_img_opened" style="display: none" />
<div id="cnblogs_code_open_9ce7fee0-8a9f-4fc6-8125-15c9c1500c9f" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.ybchen.springboot_shiro;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.apache.shiro.SecurityUtils;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.apache.shiro.authc.UsernamePasswordToken;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.apache.shiro.mgt.DefaultSecurityManager;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.apache.shiro.realm.SimpleAccountRealm;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.apache.shiro.subject.Subject;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.junit.Before;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.junit.Test;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/27 7:43 下午
 * @Versiion：1.0
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> QuickStartTest {
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> DefaultSecurityManager defaultSecurityManager = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> DefaultSecurityManager();
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> SimpleAccountRealm accountRealm = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> SimpleAccountRealm();

    @Before
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> init() {
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">初始化数据源，模拟从数据库中取的数据</span>
        accountRealm.addAccount("laochen", "123"<span style="color: rgba(0, 0, 0, 1)">);
        accountRealm.addAccount(</span>"laowang", "123456"<span style="color: rgba(0, 0, 0, 1)">);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">构建环境</span>
<span style="color: rgba(0, 0, 0, 1)">        defaultSecurityManager.setRealm(accountRealm);
    }

    @Test
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> testAuthentication() {
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">设置上下文</span>
<span style="color: rgba(0, 0, 0, 1)">        SecurityUtils.setSecurityManager(defaultSecurityManager);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">获取当前主体</span>
        Subject subject =<span style="color: rgba(0, 0, 0, 1)"> SecurityUtils.getSubject();
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">模拟用户登录，账户、密码</span>
        UsernamePasswordToken usernamePasswordToken = <span style="color: rgba(0, 0, 255, 1)">new</span> UsernamePasswordToken("laowang", "123456"<span style="color: rgba(0, 0, 0, 1)">);
        subject.login(usernamePasswordToken);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">判断是否成功</span>
        <span style="color: rgba(0, 0, 255, 1)">boolean</span> authenticated =<span style="color: rgba(0, 0, 0, 1)"> subject.isAuthenticated();
        System.out.println(</span>"认证结果：" +<span style="color: rgba(0, 0, 0, 1)"> authenticated);
    }

}</span></pre>
