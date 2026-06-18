{

  "title": "SpringBoot整合Shiro权限框架实战",
  "date": "2021-01-05",
  "description": "什么是ACL和RBAC ACL Access Control list：访问控制列表 优点：简单易用，开发便捷 缺点：用户和权限直接挂钩，导致在授予时的复杂性，比较分散，不便于管理 例子：常见的文件系统权限设计，直接给用户加权限 RBAC Role Based Access Control：基于角色",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/shiro.html"

}

# 什么是ACL和RBAC

## ACL

- Access Control list：访问控制列表
- 优点：简单易用，开发便捷
- 缺点：用户和权限直接挂钩，导致在授予时的复杂性，比较分散，不便于管理
- 例子：常见的文件系统权限设计，直接给用户加权限

## RBAC

- Role Based Access Control：基于角色的访问控制
- 权限与角色相关联，用户通过成为适当角色的成员而得到这些角色的权限
- 优点：简化了用户与权限的管理，通过对用户进行分类，使得角色与权限关联起来
- 缺点：开发比ACL相对复杂
- 例子：基于RBAC模型的权限验证框架，Apache Shiro

# 什么是Apache Shiro

## 官网地址

[点我直达](https://shiro.apache.org/)

## 介绍

　　Apache Shiro是一个强大且易用的Java安全框架,执行身份**验证、授权、密码和会话管理**。使用Shiro的易于理解的API,您可以快速、轻松地获得任何应用程序,从最小的移动应用程序到最大的网络和企业应用程序。

## 什么是身份认证

　　Authentication，身份认证，一般就是登陆校验

## 什么是授权

　　Authorization，给用户分配角色或者访问某些资源的权限

## 什么是会话管理

　　Session Management，用户的会话管理员，多数情况下是web session

## 什么是加密

　　Cryptography，数据加密，比如密码加解密

## 核心概念

### Subject

　　我们把**用户或者程序称为主体**，主体去访问系统或者资源

### SecurityManager

**安全管理器**，Subject的认证和授权都要在安全管理器下进行

### Realm

　　数据域，**Shiro和安全数据的连接器**，通过realm获取认证授权相关信息

### Authenticator

　　认证器，主要**负责Subject的认证**

### Authorizer

　　授权器，主要负责Subject的授权，**控制Subject拥有的角色或者权限**

### Crytography

**加解密**，Shiro的包含易于使用和理解的数据加解密方法，简化了很多复杂的API

### Cache Manager

**缓存管理器**，比如认证或授权信息，通过缓存进行管理，提高性能

# 快速上手

## 构建项目

![](./images/images/img_001_bd24f0df2aee.png)

## 认证和授权

![](./images/images/img_002_e41a4bfb5e1b.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.mgt.DefaultSecurityManager;
import org.apache.shiro.realm.SimpleAccountRealm;
import org.apache.shiro.subject.Subject;
import org.junit.Before;
import org.junit.Test;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/27 7:43 下午
 * @Versiion：1.0
 */
public class QuickStartTest {
    private DefaultSecurityManager defaultSecurityManager = new DefaultSecurityManager();
    private SimpleAccountRealm accountRealm = new SimpleAccountRealm();

    @Before
    public void init() {
        //初始化数据源，模拟从数据库中取的数据
        accountRealm.addAccount("laochen", "123");
        accountRealm.addAccount("laowang", "123456");
        //构建环境
        defaultSecurityManager.setRealm(accountRealm);
    }

    @Test
    public void testAuthentication() {
        //设置上下文
        SecurityUtils.setSecurityManager(defaultSecurityManager);
        //获取当前主体
        Subject subject = SecurityUtils.getSubject();
        //模拟用户登录，账户、密码
        UsernamePasswordToken usernamePasswordToken = new UsernamePasswordToken("laowang", "123456");
        subject.login(usernamePasswordToken);
        //判断是否成功
        boolean authenticated = subject.isAuthenticated();
        System.out.println("认证结果：" + authenticated);
    }

}
```

QuickStartTest.java

### 常用API

```text
        //是否有对应的角色
        subject.hasRole("root");
        //获取subject名
        subject.getPrincipal();
        //检查是否有对应的角色，无返回值，直接在SecurityManager里面进行判断
        subject.checkRole("admin");
        //检查是否有对应的角色
        subject.hasRole("admin");
        //退出登录
        subject.logout();
```

![](./images/images/img_005_76c31c854a37.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.mgt.DefaultSecurityManager;
import org.apache.shiro.realm.SimpleAccountRealm;
import org.apache.shiro.subject.Subject;
import org.junit.Before;
import org.junit.Test;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/27 7:43 下午
 * @Versiion：1.0
 */
public class QuickStartAPITest {
    private DefaultSecurityManager defaultSecurityManager = new DefaultSecurityManager();
    private SimpleAccountRealm accountRealm = new SimpleAccountRealm();

    @Before
    public void init() {
        //初始化数据源，模拟从数据库中取的数据
        accountRealm.addAccount("laochen", "123","root","admin");
        accountRealm.addAccount("laowang", "123456","user");
        //构建环境
        defaultSecurityManager.setRealm(accountRealm);
    }

    @Test
    public void testAuthentication() {
        //设置上下文
        SecurityUtils.setSecurityManager(defaultSecurityManager);
        //获取当前主体
        Subject subject = SecurityUtils.getSubject();
        //模拟用户登录，账户、密码
        UsernamePasswordToken usernamePasswordToken = new UsernamePasswordToken("laochen", "123");
        subject.login(usernamePasswordToken);
        //判断是否成功
        boolean authenticated = subject.isAuthenticated();
        System.out.println("认证结果：" + authenticated);
        //是否有对应的角色
        System.out.println("是否有对应的root角色："+subject.hasRole("root"));
        //获取subject名
        System.out.println("获取subject名："+subject.getPrincipal());
        //检查是否有对应的角色，无返回值，直接在SecurityManager里面进行判断，没有的话，直接报错
        subject.checkRole("admin");
        //检查是否有对应的角色
        System.out.println("是否存在admin角色："+subject.hasRole("admin"));
        //退出登录
        subject.logout();
        System.out.println("退出登录后，认证结果：" + authenticated);
    }

}
```

QuickStartAPITest.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.4.1</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.ybchen</groupId>
    <artifactId>springboot_shiro</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springboot_shiro</name>
    <description>SpringBoot整合Shiro</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.2.3</version>
        </dependency>
        <!--Shiro-->
        <dependency>
            <groupId>org.apache.shiro</groupId>
            <artifactId>shiro-spring</artifactId>
            <version>1.7.0</version>
        </dependency>

    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

pom.xml

# realm实战

## 作用

　　Shiro从Realm获取安全数据

## 概念

- principal：主体的标识，可以有多个，但是需要具有唯一性，如：手机号、邮箱
- credential：凭证，一般就是密码

## 内置ini realm

![](./images/images/img_006_bf3a6a09202a.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.junit.Before;
import org.junit.Test;

/**
 * @Description：从ini配置文件中读取用户与角色
 * @Author：chenyanbin
 * @Date：2020/12/27 8:52 下午
 * @Versiion：1.0
 */
public class QuickStartIniTest {
    @Before
    public void init() {

    }

    @Test
    public void testAuthentication() {
        //创建SecurityManager工厂，通过配置文件ini创建
        Factory<SecurityManager> factory = new IniSecurityManagerFactory("classpath:shiro.ini");
        SecurityManager securityManager=factory.getInstance();
        //将securityManager设置到当前运行环境中
        SecurityUtils.setSecurityManager(securityManager);
        //获取主体
        Subject subject = SecurityUtils.getSubject();
        //模拟用户登录，账户、密码
        UsernamePasswordToken usernamePasswordToken = new UsernamePasswordToken("laochen", "123");
        subject.login(usernamePasswordToken);
        //判断是否成功
        //判断是否成功
        boolean authenticated = subject.isAuthenticated();
        System.out.println("认证结果：" + authenticated);
        //是否有对应的角色
        System.out.println("是否有对应的root角色："+subject.hasRole("root"));
        //获取subject名
        System.out.println("获取subject名："+subject.getPrincipal());
        //检查是否有对应的角色，无返回值，直接在SecurityManager里面进行判断，没有的话，直接报错
        subject.checkRole("admin");
        //检查是否有对应的角色
        System.out.println("是否存在admin角色："+subject.hasRole("admin"));
        //退出登录
        subject.logout();
        System.out.println("退出登录后，认证结果：" + authenticated);
    }
}
```

QuickStartIniTest.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
# 格式 name=password,role1,role2,..roleN
[users]
# 账户=laochen；密码=123；角色=admin
laochen = 123, admin
laowang = 456, user

# 格式 role=permission1,permission2...permissionN 也可以用通配符
# 下面配置user的权限为所有video:find,video:buy，如果需要配置video全部操作crud 则 user = video:*
[roles]
user = video:find,video:buy
# 'admin' role has all permissions, indicated by the wildcard '*'
admin = *
```

shiro.ini

### 校验权限

![](./images/images/img_007_fecbfed275a8.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.junit.Before;
import org.junit.Test;

/**
 * @Description：从ini配置文件中读取用户与角色
 * @Author：chenyanbin
 * @Date：2020/12/27 8:52 下午
 * @Versiion：1.0
 */
public class QuickStartIniTest {
    @Before
    public void init() {

    }

    @Test
    public void testAuthentication() {
        //创建SecurityManager工厂，通过配置文件ini创建
        Factory<SecurityManager> factory = new IniSecurityManagerFactory("classpath:shiro.ini");
        SecurityManager securityManager=factory.getInstance();
        //将securityManager设置到当前运行环境中
        SecurityUtils.setSecurityManager(securityManager);
        //获取主体
        Subject subject = SecurityUtils.getSubject();
        //模拟用户登录，账户、密码
        UsernamePasswordToken usernamePasswordToken = new UsernamePasswordToken("laochen", "123");
        subject.login(usernamePasswordToken);
        //判断是否成功
        //判断是否成功
        boolean authenticated = subject.isAuthenticated();
        System.out.println("认证结果：" + authenticated);
        //是否有对应的角色
        System.out.println("是否有对应的root角色："+subject.hasRole("root"));
        //获取subject名
        System.out.println("获取subject名："+subject.getPrincipal());
        //检查是否有对应的角色，无返回值，直接在SecurityManager里面进行判断，没有的话，直接报错
        subject.checkRole("admin");
        //检查是否有对应的角色
        System.out.println("是否存在admin角色："+subject.hasRole("admin"));
        //================权限，没有的话直接报错================
        subject.checkPermission("video:delete");
        System.out.println("是否有video:delete权限："+subject.isPermitted("video:delete"));
        //退出登录
        subject.logout();
        System.out.println("退出登录后，认证结果：" + subject.isAuthenticated());
    }
}
```

QuickStartIniTest.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
# 格式 name=password,role1,role2,..roleN
[users]
# 账户=laochen；密码=123；角色=admin
laochen = 123, admin
laowang = 456, user

# 格式 role=permission1,permission2...permissionN 也可以用通配符
# 下面配置user的权限为所有video:find,video:buy，如果需要配置video全部操作crud 则 user = video:*
[roles]
user = video:find,video:buy
# 'admin' role has all permissions, indicated by the wildcard '*'
admin = *
```

shiro.ini

**注：配置文件必须ini结尾**

## 内置JdbcRealm

## 方式一

![](./images/images/img_008_9477181344bf.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.config.IniSecurityManagerFactory;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.Factory;
import org.junit.Test;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/27 10:40 下午
 * @Versiion：1.0
 */
public class QuickStartJdbcIniTest {
    @Test
    public void testAuthentication(){
        //创建SecurityManager工厂，通过配置文件ini创建
        Factory<SecurityManager> factory = new IniSecurityManagerFactory("classpath:jdbcrealm.ini");
        SecurityManager securityManager=factory.getInstance();
        //将securityManager设置到当前运行环境中
        SecurityUtils.setSecurityManager(securityManager);
        //获取主体
        Subject subject = SecurityUtils.getSubject();
        //模拟用户登录，账户、密码
        UsernamePasswordToken usernamePasswordToken = new UsernamePasswordToken("laochen", "123");
        subject.login(usernamePasswordToken);
        //判断是否成功
        boolean authenticated = subject.isAuthenticated();
        System.out.println("认证结果：" + authenticated);
        //是否有对应的角色
        System.out.println("是否有对应的root角色："+subject.hasRole("root"));
        //获取subject名
        System.out.println("获取subject名："+subject.getPrincipal());
        //检查是否有对应的角色，无返回值，直接在SecurityManager里面进行判断，没有的话，直接报错
        subject.checkRole("role1");
        //检查是否有对应的角色
        System.out.println("是否存在role1角色："+subject.hasRole("role1"));
        //================权限，没有的话直接报错================
        //subject.checkPermission("video:delete");
        System.out.println("是否有video:buy权限："+subject.isPermitted("video:buy"));
        //退出登录
        subject.logout();
        System.out.println("退出登录后，认证结果：" + subject.isAuthenticated());
    }
}
```

QuickStartJdbcIniTest.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
#声明Realm，指定realm类型
jdbcRealm=org.apache.shiro.realm.jdbc.JdbcRealm
#配置数据源
#dataSource=com.mchange.v2.c3p0.ComboPooledDataSource
dataSource=com.alibaba.druid.pool.DruidDataSource
# mysql-connector-java 5 用的驱动url是com.mysql.jdbc.Driver，mysql-connector-java6以后用的是com.mysql.cj.jdbc.Driver
dataSource.driverClassName=com.mysql.cj.jdbc.Driver
#避免安全警告
dataSource.url=jdbc:mysql://127.0.0.1:3306/shiro?characterEncoding=UTF-8&serverTimezone=UTC&useSSL=false
#账号、密码
dataSource.username=root
dataSource.password=root
#指定数据源
jdbcRealm.dataSource=$dataSource
#开启查找权限, 默认是false
jdbcRealm.permissionsLookupEnabled=true
#指定SecurityManager的Realms实现，设置realms，可以有多个，用逗号隔开
securityManager.realms=$jdbcRealm
```

jdbcrealm.ini

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50731
 Source Host           : localhost:3306
 Source Schema         : shiro

 Target Server Type    : MySQL
 Target Server Version : 50731
 File Encoding         : 65001

 Date: 27/12/2020 23:06:45
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for roles_permissions
-- ----------------------------
DROP TABLE IF EXISTS `roles_permissions`;
CREATE TABLE `roles_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `role_name` varchar(100) DEFAULT NULL COMMENT '角色名',
  `permission` varchar(100) DEFAULT NULL COMMENT '权限名',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_roles_permissions` (`role_name`,`permission`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of roles_permissions
-- ----------------------------
BEGIN;
INSERT INTO `roles_permissions` VALUES (4, 'admin', 'video:*');
INSERT INTO `roles_permissions` VALUES (3, 'role1', 'video:buy');
INSERT INTO `roles_permissions` VALUES (2, 'role1', 'video:find');
INSERT INTO `roles_permissions` VALUES (5, 'role2', '*');
INSERT INTO `roles_permissions` VALUES (1, 'root', '*');
COMMIT;

-- ----------------------------
-- Table structure for user_roles
-- ----------------------------
DROP TABLE IF EXISTS `user_roles`;
CREATE TABLE `user_roles` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(100) DEFAULT NULL COMMENT '用户名',
  `role_name` varchar(100) DEFAULT NULL COMMENT '角色名',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_user_roles` (`username`,`role_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_roles
-- ----------------------------
BEGIN;
INSERT INTO `user_roles` VALUES (1, 'laochen', 'role1');
INSERT INTO `user_roles` VALUES (2, 'laochen', 'role3');
INSERT INTO `user_roles` VALUES (4, 'laowang', 'admin');
INSERT INTO `user_roles` VALUES (3, 'laowang', 'root');
COMMIT;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(100) DEFAULT NULL COMMENT '用户名',
  `password` varchar(100) DEFAULT NULL COMMENT '密码',
  `password_salt` varchar(100) DEFAULT NULL COMMENT '密码加盐规则',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idx_users_username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users
-- ----------------------------
BEGIN;
INSERT INTO `users` VALUES (1, 'laochen', '123', NULL);
INSERT INTO `users` VALUES (2, 'laowang', '456', NULL);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
```

建表语句.sql

### 注意

**表名和字段要对应上，否则自定义定，继承：AuthorizingRealm，重写sql查询语句！！！！并重新指定realm类型！！！！**

![](./images/images/img_009_aa54cb584637.gif)

## 方式二

![](./images/images/img_010_e7fcf8f492a7.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import com.alibaba.druid.pool.DruidDataSource;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.mgt.DefaultSecurityManager;
import org.apache.shiro.realm.jdbc.JdbcRealm;
import org.apache.shiro.subject.Subject;
import org.junit.Test;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/27 10:40 下午
 * @Versiion：1.0
 */
public class QuickStartJdbc2Test {
    @Test
    public void testAuthentication() {
        DefaultSecurityManager securityManager = new DefaultSecurityManager();
        DruidDataSource ds = new DruidDataSource();
        ds.setDriverClassName("com.mysql.cj.jdbc.Driver");
        ds.setUrl("jdbc:mysql://127.0.0.1:3306/shiro?characterEncoding=UTF-8&serverTimezone=UTC&useSSL=false");
        ds.setUsername("root");
        ds.setPassword("root");
        JdbcRealm jdbcRealm = new JdbcRealm();
        //开启查找权限, 默认是false
        jdbcRealm.setPermissionsLookupEnabled(true);
        //配置数据源
        jdbcRealm.setDataSource(ds);
        //jdbc与DefaultSecurityManager关联
        securityManager.setRealm(jdbcRealm);
        //=======================下面内容相同==============================
        //将securityManager设置到当前运行环境中
        SecurityUtils.setSecurityManager(securityManager);
        //获取主体
        Subject subject = SecurityUtils.getSubject();
        //模拟用户登录，账户、密码
        UsernamePasswordToken usernamePasswordToken = new UsernamePasswordToken("laochen", "123");
        subject.login(usernamePasswordToken);
        //判断是否成功
        boolean authenticated = subject.isAuthenticated();
        System.out.println("认证结果：" + authenticated);
        //是否有对应的角色
        System.out.println("是否有对应的root角色：" + subject.hasRole("root"));
        //获取subject名
        System.out.println("获取subject名：" + subject.getPrincipal());
        //检查是否有对应的角色，无返回值，直接在SecurityManager里面进行判断，没有的话，直接报错
        subject.checkRole("role1");
        //检查是否有对应的角色
        System.out.println("是否存在role1角色：" + subject.hasRole("role1"));
        //================权限，没有的话直接报错================
        //subject.checkPermission("video:delete");
        System.out.println("是否有video:buy权限：" + subject.isPermitted("video:buy"));
        //退出登录
        subject.logout();
        System.out.println("退出登录后，认证结果：" + subject.isAuthenticated());
    }
}
```

QuickStartJdbc2Test.java

## 自定义realm

**继承AuthorizingRealm**，**重写授权**方法**doGetAuthorizationInfo**、**重写认证**方法**doGetAuthenticationInfo**。

**UsernamePasswordToken**：对应就是**shiro**的**token**中有**Principal**和**Credential**。

**SimpleAuthorizationInfo**：代表用户角色权限信息

**SimpleAuthenticationInfo**：代表该用户的认证信息

![](./images/images/img_011_9b8dcb3beea7.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.apache.shiro.authc.AuthenticationException;
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authc.SimpleAuthenticationInfo;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * @Description：自定义Realm
 * @Author：chenyanbin
 * @Date：2020/12/28 8:41 下午
 * @Versiion：1.0
 */
public class CustomRealm extends AuthorizingRealm {
    private final Map<String, String> userInfoMap = new HashMap<>();
    //role-->permission
    private final Map<String, Set<String>> permissionMap = new HashMap<>();
    //user-->role
    private final Map<String, Set<String>> roleMap = new HashMap<>();

    /**
     * 代码块初始化数据
     */
    {
        userInfoMap.put("laochen", "123");
        userInfoMap.put("laowang", "456");
        //================================
        Set<String> set1 = new HashSet<>();
        set1.add("video:find");
        set1.add("video:buy");
        Set<String> set2 = new HashSet<>();
        set2.add("video:add");
        set2.add("video:delete");
        permissionMap.put("laochen", set1);
        permissionMap.put("laowang", set2);
        //================================
        Set<String> set3 = new HashSet<>();
        Set<String> set4 = new HashSet<>();
        set3.add("role1");
        set3.add("role2");
        set4.add("root");
        roleMap.put("laochen", set3);
        roleMap.put("laowang", set4);
    }

    /**
     * 授权认证
     *
     * @param principals
     * @return
     */
    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principals) {
        System.out.println("授权 AuthorizationInfo");
        String name = (String) principals.getPrimaryPrincipal();
        //权限
        Set<String> permissions = getPermissionsByNameFromDB(name);
        //角色
        Set<String> roles = getRoleByNameFromDB(name);
        SimpleAuthorizationInfo simpleAuthorizationInfo=new SimpleAuthorizationInfo();
        simpleAuthorizationInfo.setRoles(roles);
        simpleAuthorizationInfo.setStringPermissions(permissions);
        return simpleAuthorizationInfo;
    }

    /**
     * 模拟从数据库中取角色
     *
     * @param name
     * @return
     */
    private Set<String> getRoleByNameFromDB(String name) {
        return roleMap.get(name);
    }

    /**
     * 模拟从数据库中取权限
     *
     * @param name
     * @return
     */
    private Set<String> getPermissionsByNameFromDB(String name) {
        return permissionMap.get(name);
    }

    /**
     * 登录认证
     *
     * @param token
     * @return
     * @throws AuthenticationException
     */
    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token) throws AuthenticationException {
        System.out.println("认证 doGetAuthenticationInfo");
        //用户名
        String name = (String) token.getPrincipal();
        //从DB中根据用户取密码
        String pwd = getPwdByUserNameFromDB(name);
        if (pwd == null || "".equals(pwd)) {
            return null;
        }
        SimpleAuthenticationInfo simpleAuthenticationInfo = new SimpleAuthenticationInfo(name, pwd, this.getName());
        return simpleAuthenticationInfo;
    }

    /**
     * 模拟从数据库中取密码
     *
     * @param name
     * @return
     */
    private String getPwdByUserNameFromDB(String name) {
        return userInfoMap.get(name);
    }
}
```

CustomRealm.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.mgt.DefaultSecurityManager;
import org.apache.shiro.subject.Subject;
import org.junit.Before;
import org.junit.Test;

/**
 * @Description：自定义realm
 * @Author：chenyanbin
 * @Date：2020/12/28 8:43 下午
 * @Versiion：1.0
 */
public class QuickCustomRealmTest {
    private CustomRealm customRealm=new CustomRealm();
    private DefaultSecurityManager defaultSecurityManager=new DefaultSecurityManager();

    @Before
    public void init() {
        //构建环境
        defaultSecurityManager.setRealm(customRealm);
        SecurityUtils.setSecurityManager(defaultSecurityManager);
    }

    @Test
    public void testAuthentication(){
        //获取当前操作的主体
        Subject subject = SecurityUtils.getSubject();
        //用户输入账号、密码
        UsernamePasswordToken usernamePasswordToken=new UsernamePasswordToken("laochen","123");
        subject.login(usernamePasswordToken);
        System.out.println("认证结果："+subject.isAuthenticated());
        //拿到主体标识属性
        System.out.println("获取subject名："+subject.getPrincipal());
        //是否有role1角色，没有则报错
        subject.checkRole("role1");
        //是否有对应的角色
        System.out.println("是否有对应的角色："+subject.hasRole("role1"));
        //是否有对应的权限
        System.out.println("是否有对应的权限："+subject.isPermitted("video:find"));
    }
}
```

QuickCustomRealmTest.java

# Filter过滤器

- 核心过滤器

  - DefaultFilter，配置那个路径对应那个拦截器进行处理

- authc：org.apache.shiro.web.filter.authc.FormAuthenticationFilter

  - 需要认证登录才能访问

- user：org.apache.shiro.web.filter.authc.UseerrFilter

  - 用户拦截器，表示必须存在用户

- anon：org.apache.shiro.web.filter.authc.AnonymoousFilter

  - 匿名拦截器，不需要登录即可访问的资源，匿名用户或游客，一般用于过滤静态资源。

- roles：org.apache.shiro.web.filter.authz.RolesAuthorizationFilter

  - 角色授权拦截器，验证用户是否拥有角色
  - 参数可写多个，表示某些角色才能通过，多个参数时，写roles["root,role1"]，当有多个参数时必须每个参数都通过才算通过

- perms：org.apache.shiro.web.filter.authz.PermissionsAuthorizationFilter

  - 权限授权拦截器，验证用户是否拥有权限
  - 参数可写多个，表示需要某些权限才能通过，多个参数写perms["user,admin"]，当有多个参数时必须每个参数都通过才算可以

- authcBasci：org.apache.shiro.web.filter.authc.BasicHttpAuthenticationFilter

  - httpBasic，身份验证拦截器

- logout：org.apache.shiro.web.filter.authc.LogoutFilter

  - 退出拦截器，执行后会直接跳转到shiroFilterFactoryBean.setLoginUrl()，设置的url

- port：org.apache.shiro.web.filter.authz.PortFilter

  - 端口拦截器，可通过的端口

- ssl：org.apache.shiro.web.filter.authz.SslFilter

  - ssl拦截器，只有请求协议是https才能通过

![](./images/images/img_012_7f5aed35c65c.png)

## Filter配置路径

- 路径通配符支持?、*、**，注意通配符匹配不包含目录分隔符“/”
- *：可以匹配所有，不加*，可以进行前缀匹配，但多个冒号就需要多个*来匹配

```text
url权限采取第一次匹配优先的方式
?：匹配一个字符，如：/user?，匹配：/user1，但不匹配：/user/
*：匹配零个或多个字符串，如：/add*，匹配：/addtest，但不匹配：/user/1
**：匹配路径中的零个或多个路径，如：/user/**将匹配：/user/xxx/yyy
```

## Shiro权限控制注解

### 注解方式

- @RequiresRoles(value={"admin","editor"},logical=Logical.AND)

  - 需要角色：admin和editor两个角色，AND表示两个同时成立

- RequiresPermissions(value={"user:add","user:del"},logical.OR)

  - 需要权限user:add或user:del权限其中一个，OR是或的意思

- @RequiresAuthentication

  - 已经授过权，调用Subject.isAuthenticated()返回true

- @RequiresUser

  - 身份验证或通过记住我登录过的

![](./images/images/img_013_88665d38429b.png)

### 使用文件的方式

　　使用ShiroConfig。

### 编程方式

![](./images/images/img_014_fd9eac7b4881.png)

# SpringBoot整合Shiro

## 技术栈

　　前后端分离+SpringBoot+Mysql+Mybatis+Shiro+Redis+JDK8

## 数据库表

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50731
 Source Host           : localhost:3306
 Source Schema         : shiro_2

 Target Server Type    : MySQL
 Target Server Version : 50731
 File Encoding         : 65001

 Date: 03/01/2021 22:36:28
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for permission
-- ----------------------------
DROP TABLE IF EXISTS `permission`;
CREATE TABLE `permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(255) DEFAULT NULL COMMENT '权限名称',
  `url` varchar(255) DEFAULT NULL COMMENT '路径',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COMMENT='权限';

-- ----------------------------
-- Records of permission
-- ----------------------------
BEGIN;
INSERT INTO `permission` VALUES (1, 'video_update', '/api/video/update');
INSERT INTO `permission` VALUES (2, 'video_delete', '/api/video/delete');
INSERT INTO `permission` VALUES (3, 'video_add', '/api/video/add');
INSERT INTO `permission` VALUES (4, 'order_list', '/api/order/list');
INSERT INTO `permission` VALUES (5, 'user_list', '/api/user/list');
COMMIT;

-- ----------------------------
-- Table structure for role
-- ----------------------------
DROP TABLE IF EXISTS `role`;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(255) DEFAULT NULL COMMENT '角色名称',
  `description` varchar(255) DEFAULT NULL COMMENT '描述',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='角色';

-- ----------------------------
-- Records of role
-- ----------------------------
BEGIN;
INSERT INTO `role` VALUES (1, 'admin', '系统管理员');
INSERT INTO `role` VALUES (2, 'root', '超级管理员');
INSERT INTO `role` VALUES (3, 'user', '普通用户');
COMMIT;

-- ----------------------------
-- Table structure for role_permission
-- ----------------------------
DROP TABLE IF EXISTS `role_permission`;
CREATE TABLE `role_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `role_id` int(11) DEFAULT NULL COMMENT '角色id',
  `permission_id` int(11) DEFAULT NULL COMMENT '权限id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COMMENT='角色-权限';

-- ----------------------------
-- Records of role_permission
-- ----------------------------
BEGIN;
INSERT INTO `role_permission` VALUES (1, 1, 1);
INSERT INTO `role_permission` VALUES (2, 1, 2);
INSERT INTO `role_permission` VALUES (3, 2, 1);
INSERT INTO `role_permission` VALUES (4, 2, 2);
INSERT INTO `role_permission` VALUES (5, 2, 3);
INSERT INTO `role_permission` VALUES (6, 2, 4);
INSERT INTO `role_permission` VALUES (7, 2, 5);
INSERT INTO `role_permission` VALUES (8, 3, 5);
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(255) DEFAULT NULL COMMENT '用户名',
  `password` varchar(255) DEFAULT NULL COMMENT '密码',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `salt` varchar(255) DEFAULT NULL COMMENT '加盐',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='用户';

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES (1, 'laochen', '123', NULL, NULL);
INSERT INTO `user` VALUES (2, 'laowang', '456', NULL, NULL);
INSERT INTO `user` VALUES (3, 'laoli', '789', NULL, NULL);
COMMIT;

-- ----------------------------
-- Table structure for user_role
-- ----------------------------
DROP TABLE IF EXISTS `user_role`;
CREATE TABLE `user_role` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `role_id` int(11) DEFAULT NULL COMMENT '角色id',
  `user_id` int(11) DEFAULT NULL COMMENT '用户id',
  `remark` varchar(255) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COMMENT='角色-用户关联表';

-- ----------------------------
-- Records of user_role
-- ----------------------------
BEGIN;
INSERT INTO `user_role` VALUES (1, 1, 1, 'laochen是系统管理员');
INSERT INTO `user_role` VALUES (2, 2, 2, 'laowang是超级管理员');
INSERT INTO `user_role` VALUES (3, 3, 3, 'laoli是普通用户');
INSERT INTO `user_role` VALUES (4, 1, 2, 'laowang是系统管理员');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
```

shiro_2.sql

## 项目结构

![](./images/images/img_015_2e79593548a2.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.config;

import com.ybchen.springboot_shiro.domain.Role;
import com.ybchen.springboot_shiro.domain.User;
import com.ybchen.springboot_shiro.service.UserService;
import org.apache.shiro.authc.AuthenticationException;
import org.apache.shiro.authc.AuthenticationInfo;
import org.apache.shiro.authc.AuthenticationToken;
import org.apache.shiro.authc.SimpleAuthenticationInfo;
import org.apache.shiro.authz.AuthorizationInfo;
import org.apache.shiro.authz.SimpleAuthorizationInfo;
import org.apache.shiro.realm.AuthorizingRealm;
import org.apache.shiro.subject.PrincipalCollection;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Description：自定义realm
 * @Author：chenyanbin
 * @Date：2021/1/2 11:16 下午
 * @Versiion：1.0
 */
public class CustomRealm extends AuthorizingRealm {
    @Autowired
    private UserService userService;

    /**
     * 进行权限校验的时候会调用
     *
     * @param principals
     * @return
     */
    @Override
    protected AuthorizationInfo doGetAuthorizationInfo(PrincipalCollection principals) {
        System.out.println("CustomRealm doGetAuthorizationInfo 授权");
        //获取用户名
        String userName = (String) principals.getPrimaryPrincipal();
        User user = userService.findAllUserInfoByUserName(userName);
        if (user == null) {
            return null;
        }
        //角色集合
        List<String> stringRoleList = new ArrayList<>();
        //权限集合
        List<String> stringPermissionList = new ArrayList<>();
        List<Role> roleList = user.getRoleList();
        stringRoleList = roleList.stream().map(
                obj -> {
                    stringPermissionList.addAll(obj.getPermissionList()
                            .stream()
                            .map(per ->
                                    per.getName()).collect(Collectors.toList()));
                    return obj.getName();
                }).collect(Collectors.toList());
        SimpleAuthorizationInfo simpleAuthorizationInfo = new SimpleAuthorizationInfo();
        simpleAuthorizationInfo.addRoles(stringRoleList);
        simpleAuthorizationInfo.addStringPermissions(stringPermissionList);
        return simpleAuthorizationInfo;
    }

    /**
     * 用户登录的时候会调用
     *
     * @param token
     * @return
     * @throws AuthenticationException
     */
    @Override
    protected AuthenticationInfo doGetAuthenticationInfo(AuthenticationToken token) throws AuthenticationException {
        System.out.println("CustomRealm doGetAuthenticationInfo 认证");
        //从token中获取用户信息
        String uesrName = (String) token.getPrincipal();
        User user = userService.findAllUserInfoByUserName(uesrName);
        if (user == null) {
            return null;
        }
        //密码
        String pwd = user.getPassword();
        if (pwd == null || "".equals(pwd)) {
            return null;
        }
        return new SimpleAuthenticationInfo(uesrName, pwd, this.getClass().getName());
    }
}
```

CustomRealm.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.config;

import org.apache.shiro.web.servlet.ShiroHttpServletRequest;
import org.apache.shiro.web.session.mgt.DefaultWebSessionManager;
import org.apache.shiro.web.util.WebUtils;

import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import java.io.Serializable;

/**
 * @Description：自定义SessionManager
 * @Author：chenyanbin
 * @Date：2021/1/3 4:54 下午
 * @Versiion：1.0
 */
public class CustomSessionManager extends DefaultWebSessionManager {
    public static final String AUTHORIZATION="token";

    public CustomSessionManager() {
        super();
    }

    @Override
    protected Serializable getSessionId(ServletRequest request, ServletResponse response) {
        //获取sessionId
        String sessionId= WebUtils.toHttp(request).getHeader(AUTHORIZATION);
        if (sessionId!=null){
            request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_SOURCE,
                    ShiroHttpServletRequest.COOKIE_SESSION_ID_SOURCE);
            request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID, sessionId);
            request.setAttribute(ShiroHttpServletRequest.REFERENCED_SESSION_ID_IS_VALID, Boolean.TRUE);
            return sessionId;
        }else {
            return super.getSessionId(request,response);
        }
    }
}
```

CustomSessionManager.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.config;

import org.apache.shiro.authc.credential.HashedCredentialsMatcher;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.session.mgt.SessionManager;
import org.apache.shiro.spring.web.ShiroFilterFactoryBean;
import org.apache.shiro.web.mgt.DefaultWebSecurityManager;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 4:12 下午
 * @Versiion：1.0
 */
@Configuration
public class ShiroConfig {
    @Bean
    public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
        System.out.println("ShiroConfig ShiroFilterFactoryBean 执行");
        ShiroFilterFactoryBean shiroFilterFactoryBean = new ShiroFilterFactoryBean();
        //设置SecurityManager
        shiroFilterFactoryBean.setSecurityManager(securityManager);
        //如果访问需要登录的某个接口，却没有登录，则调用此接口(如果不是前后端分离，则跳转页面)
        shiroFilterFactoryBean.setLoginUrl("/pub/need_login");
        //shiroFilterFactoryBean.setLoginUrl("/xxx.jsp");
        //登录成功后，跳转的链接，若前后端分离，没必要设置这个
        //shiroFilterFactoryBean.setSuccessUrl("");
        //登录成功，未授权会调用此方法
        shiroFilterFactoryBean.setUnauthorizedUrl("/pub/not_permit");
        //拦截路径，必须使用:LinkedHashMap，要不然拦截效果会时有时无，因为使用的是无序的Map
        Map<String, String> filterChainDefinitionMap = new LinkedHashMap<>();
        //key=正则表达式路径，value=org.apache.shiro.web.filter.mgt.DefaultFilter
        //退出过滤器
        filterChainDefinitionMap.put("/logout", "logout");
        //匿名可以访问，游客模式
        filterChainDefinitionMap.put("/pub/**", "anon");
        //登录用户才可以访问
        filterChainDefinitionMap.put("/authc/**", "authc");
        //管理员角色才能访问
        filterChainDefinitionMap.put("/admin/**", "roles[admin]");
        //有编辑权限才能访问
        filterChainDefinitionMap.put("/video/update", "perms[video_update]");
        //authc：url必须通过认证才可以访问
        //anon：url可以匿名访问
        //过滤链是顺序执行，从上而下，一般把/**，放到最下面
        filterChainDefinitionMap.put("/**", "authc");
        shiroFilterFactoryBean.setFilterChainDefinitionMap(filterChainDefinitionMap);
        return shiroFilterFactoryBean;
    }

    @Bean
    public SecurityManager securityManager() {
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager();
        //如果不是前后端分离，不用设置setSessionManager
        securityManager.setSessionManager(sessionManager());
        securityManager.setRealm(customRealm());
        return securityManager;
    }

    /**
     * 自定义realm
     *
     * @return
     */
    @Bean
    public CustomRealm customRealm() {
        CustomRealm customRealm = new CustomRealm();
        //因为数据库密码存的是明文，所以无需使用双重md5校验
//        customRealm.setCredentialsMatcher(hashedCredentialsMatcher());
        return customRealm;
    }

    /**
     * 密码验证器，双重md5
     *
     * @return
     */
    @Bean
    public HashedCredentialsMatcher hashedCredentialsMatcher() {
        HashedCredentialsMatcher hashedCredentialsMatcher = new HashedCredentialsMatcher();
        //设置散列算法，使用md5算法
        hashedCredentialsMatcher.setHashAlgorithmName("md5");
        //散列次数，使用2次md5算法，相当于md5(md5(xxx))
        hashedCredentialsMatcher.setHashIterations(2);
        return hashedCredentialsMatcher;
    }

    /**
     * 自定义SessionManager
     *
     * @return
     */
    @Bean
    public SessionManager sessionManager() {
        CustomSessionManager customSessionManager = new CustomSessionManager();
        //超时时间，默认 30分钟，会话超时，单位毫秒
//        customSessionManager.setGlobalSessionTimeout(200000);
        return customSessionManager;
    }
}
```

ShiroConfig.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.controller;

import com.ybchen.springboot_shiro.utils.JsonData;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 7:22 下午
 * @Versiion：1.0
 */
@RestController
@RequestMapping("admin")
public class AdminController {
    @GetMapping("/video/video_list")
    public JsonData videoList() {
        List<String> list = Arrays.asList("docker", "k8s", "jenkins");
        return JsonData.buildSuccess(list);
    }
}
```

AdminController.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.controller;

import org.springframework.web.bind.annotation.RestController;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 10:01 下午
 * @Versiion：1.0
 */
@RestController
public class LogoutController {
//    /**
//     * 退出，没必要能这个，退出时，前端直接将token清空即可
//     * 还需要获取前端传来的token，然后从shiro从清空指定的session_id
//     * @return
//     */
//    @GetMapping("logout")
//    public JsonData logout(){
//        Subject subject= SecurityUtils.getSubject();
//        subject.logout();
//        return JsonData.buildSuccess("退出成功");
//    }
}
```

LogoutController.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.controller;

import com.ybchen.springboot_shiro.utils.JsonData;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 6:28 下午
 * @Versiion：1.0
 */
@RestController
@RequestMapping("authc")
public class OrderController {
    /**
     * 购买记录
     * @return
     */
    @GetMapping("/video/play_record")
    public JsonData findMyPlayRecord(){
        Map<String,String> recordMap=new HashMap<>();
        recordMap.put("1","SpringBoot");
        recordMap.put("2","SpringMvc");
        return JsonData.buildSuccess(recordMap);
    }
}
```

OrderController.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.controller;

import com.ybchen.springboot_shiro.utils.JsonData;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 9:20 下午
 * @Versiion：1.0
 */
@RestController
public class OtherController {
    @GetMapping("a")
    public JsonData a(){
        return JsonData.buildSuccess("ok");
    }
}
```

OtherController.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.controller;

import com.ybchen.springboot_shiro.domain.UserQuery;
import com.ybchen.springboot_shiro.utils.JsonData;
import org.apache.shiro.SecurityUtils;
import org.apache.shiro.authc.UsernamePasswordToken;
import org.apache.shiro.subject.Subject;
import org.springframework.web.bind.annotation.*;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 1:12 上午
 * @Versiion：1.0
 */
@RestController
@RequestMapping("pub")
public class PublicController {
    /**
     * 需要登录
     *
     * @return
     */
    @GetMapping("need_login")
    public JsonData needLogin() {
        return JsonData.buildSuccess(-1, "温馨提示：请使用对应的账号登录");
    }

    /**
     * 没权限
     *
     * @return
     */
    @GetMapping("not_permit")
    public JsonData notPermit() {
        return JsonData.buildSuccess(-1, "温馨提示：拒绝访问，没权限");
    }

    /**
     * 首页
     *
     * @return
     */
    @GetMapping("index")
    public JsonData index() {
        List<String> list = Arrays.asList("SpringBoot", "SpringMvc", "Mysql", "Redis");
        return JsonData.buildSuccess(list);
    }

    /**
     * 登录接口
     *
     * @param userQuery
     * @param request
     * @param response
     * @return
     */
    @PostMapping("login")
    public JsonData login(@RequestBody UserQuery userQuery, HttpServletRequest request, HttpServletResponse response) {
        //拿到主体
        Subject subject = SecurityUtils.getSubject();
        try {
            UsernamePasswordToken usernamePasswordToken = new UsernamePasswordToken(userQuery.getUserName(), userQuery.getPassword());
            subject.login(usernamePasswordToken);
            Map<String,Object> info=new HashMap<>();
            info.put("msg","登录成功");
            info.put("session_id",subject.getSession().getId());
            return JsonData.buildSuccess(info);
        }catch (Exception e){
            e.printStackTrace();
            return JsonData.buildError("账号或密码错误");
        }
    }
}
```

PublicController.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.controller;

import com.ybchen.springboot_shiro.utils.JsonData;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 9:41 下午
 * @Versiion：1.0
 */
@RestController
@RequestMapping("video")
public class VideoController {
    @GetMapping("update")
    public JsonData updateVideo() {
        return JsonData.buildSuccess("更新成功");
    }
    @GetMapping("add")
    public JsonData add(){
        return JsonData.buildSuccess("添加成功");
    }
}
```

VideoController.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.dao;

import com.ybchen.springboot_shiro.domain.Permission;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

/**
 * 权限
 */
public interface PermissionMapper {
    /**
     * 根据roleId查询所有权限
     * @param roleId
     * @return
     */
    @Select("select p.id id,p.name name,p.url url from role_permission rp " +
            "left join permission p on rp.permission_id=p.id " +
            "where rp.role_id=#{roleId}")
    List<Permission> findByPermissionListByRoleId(@Param("roleId") int roleId);
}
```

PermissionMapper.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.dao;

import com.ybchen.springboot_shiro.domain.Role;
import org.apache.ibatis.annotations.*;
import org.apache.ibatis.mapping.FetchType;

import java.util.List;

/**
 * 角色
 */
public interface RoleMapper {
    /**
     * 根据用户查询所有的角色
     *
     * @param userId 用户id
     * @return
     */
    @Select("select r.id id,r.name name,r.description description  from  user_role ur " +
            "left join role r on ur.role_id=r.id " +
            "where ur.user_id=#{userId}")
    @Results(
            value = {
                    @Result(id = true, property = "id", column = "id"),
                    @Result(property = "name", column = "name"),
                    @Result(property = "description", column = "description"),
                    @Result(property = "permissionList", column = "id",
                            many = @Many(select = "com.ybchen.springboot_shiro.dao.PermissionMapper.findByPermissionListByRoleId",
                                    fetchType = FetchType.DEFAULT))
            }
    )
    List<Role> findRoleListByUserId(@Param("userId") int userId);
}
```

RoleMapper.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.dao;

import com.ybchen.springboot_shiro.domain.User;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

/**
 * 用户
 */
public interface UserMapper {
    /**
     * 根据用户名查询用户
     *
     * @param userName 用户名
     * @return
     */
    @Select("select * from user where username=#{userName}")
    User findByUserName(@Param("userName") String userName);

    /**
     * 根据主键查询用户
     *
     * @param id 主键
     * @return
     */
    @Select("select * from user where id=#{userId}")
    User findById(@Param("userId") int id);

    /**
     * 根据用户名和密码查询用户
     *
     * @param userName 用户名
     * @param password 密码
     * @return
     */
    @Select("select * from user where userName=#{userName} and password=#{password}")
    User findByUserNameAndPassword(@Param("userName") String userName, @Param("password") String password);
}
```

UserMapper.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.domain;

/**
 * @Description：权限
 * @Author：chenyanbin
 * @Date：2021/1/2 11:47 下午
 * @Versiion：1.0
 */
public class Permission {
    /**
     * 主键
     */
    private int id;
    /**
     * 权限名称
     */
    private String name;
    /**
     * 路径
     */
    private String url;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    @Override
    public String toString() {
        return "Permission{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", url='" + url + '\'' +
                '}';
    }
}
```

Permission.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.domain;

import java.util.ArrayList;
import java.util.List;

/**
 * @Description：角色
 * @Author：chenyanbin
 * @Date：2021/1/2 11:43 下午
 * @Versiion：1.0
 */
public class Role {
    /**
     * 主键
     */
    private int id;
    /**
     * 角色名称
     */
    private String name;
    /**
     * 描述
     */
    private String description;
    /**
     * 权限集合
     */
    private List<Permission> permissionList=new ArrayList<>();

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<Permission> getPermissionList() {
        return permissionList;
    }

    public void setPermissionList(List<Permission> permissionList) {
        this.permissionList = permissionList;
    }

}
```

Role.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.domain;

/**
 * @Description：角色权限
 * @Author：chenyanbin
 * @Date：2021/1/2 11:44 下午
 * @Versiion：1.0
 */
public class RolePermission {
    /**
     * 主键
     */
    private int id;
    /**
     * 角色id
     */
    private int roleId;
    /**
     * 权限id
     */
    private int permissiionId;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getRoleId() {
        return roleId;
    }

    public void setRoleId(int roleId) {
        this.roleId = roleId;
    }

    public int getPermissiionId() {
        return permissiionId;
    }

    public void setPermissiionId(int permissiionId) {
        this.permissiionId = permissiionId;
    }

    @Override
    public String toString() {
        return "RolePermission{" +
                "id=" + id +
                ", roleId=" + roleId +
                ", permissiionId=" + permissiionId +
                '}';
    }
}
```

RolePermission.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.domain;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

/**
 * @Description：用户表
 * @Author：chenyanbin
 * @Date：2021/1/2 11:41 下午
 * @Versiion：1.0
 */
public class User {
    /**
     * 主键
     */
    private int id;
    /**
     * 用户名
     */
    private String username;
    /**
     * 密码
     */
    private String password;
    /**
     * 创建时间
     */
    private Date createTime;
    /**
     * 密码加盐
     */
    private String salt;
    /**
     * 角色集合
     */
    private List<Role> roleList=new ArrayList<>();

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    public Date getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Date createTime) {
        this.createTime = createTime;
    }

    public String getSalt() {
        return salt;
    }

    public void setSalt(String salt) {
        this.salt = salt;
    }

    public List<Role> getRoleList() {
        return roleList;
    }

    public void setRoleList(List<Role> roleList) {
        this.roleList = roleList;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", password='" + password + '\'' +
                ", createTime=" + createTime +
                ", salt='" + salt + '\'' +
                ", roleList=" + roleList +
                '}';
    }
}
```

User.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.domain;

import java.io.Serializable;

/**
 * @Description：接收用户名和密码
 * @Author：chenyanbin
 * @Date：2021/1/3 6:19 下午
 * @Versiion：1.0
 */
public class UserQuery implements Serializable {
    private String userName;
    private String password;

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    @Override
    public String toString() {
        return "UserQuery{" +
                "userName='" + userName + '\'' +
                ", password='" + password + '\'' +
                '}';
    }
}
```

UserQuery.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.domain;

/**
 * @Description：用户角色
 * @Author：chenyanbin
 * @Date：2021/1/2 11:46 下午
 * @Versiion：1.0
 */
public class UserRole {
    /**
     * 主键
     */
    private int id;
    /**
     * 角色id
     */
    private int roleId;
    /**
     * 用户id
     */
    private int userId;
    /**
     * 备注
     */
    private String remark;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getRoleId() {
        return roleId;
    }

    public void setRoleId(int roleId) {
        this.roleId = roleId;
    }

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getRemark() {
        return remark;
    }

    public void setRemark(String remark) {
        this.remark = remark;
    }

    @Override
    public String toString() {
        return "UserRole{" +
                "id=" + id +
                ", roleId=" + roleId +
                ", userId=" + userId +
                ", remark='" + remark + '\'' +
                '}';
    }
}
```

UserRole.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.exception;

/**
 * @Description：自定义异常
 * @Author：chenyanbin
 * @Date：2021/1/3 7:31 下午
 * @Versiion：1.0
 */
public class CustomException extends RuntimeException{
    private Integer code;
    private String msg;

    public CustomException(Integer code, String msg) {
        this.code = code;
        this.msg = msg;
    }

    public Integer getCode() {
        return code;
    }

    public void setCode(Integer code) {
        this.code = code;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    @Override
    public String toString() {
        return "CustomException{" +
                "code=" + code +
                ", msg='" + msg + '\'' +
                '}';
    }
}
```

CustomException.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.exception;

import com.ybchen.springboot_shiro.utils.JsonData;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * @ClassName：GlobalExceptiions
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/12/9 11:34 上午
 * @Versiion：1.0
 */
@ControllerAdvice
public class GlobalExceptiions {
    private final Logger logger = LoggerFactory.getLogger(getClass());

    @ExceptionHandler(value = Exception.class)
    @ResponseBody
    public JsonData handle(Exception ex) {
        logger.info("[ 全局异常 ] ===============》 {}", ex);
        if (ex instanceof CustomException) {
            CustomException customException = (CustomException) ex;
            return JsonData.buildError(customException.getCode(), customException.getMsg());
        }
        return JsonData.buildError("系统内部错误，请联系管理员！");
    }
}
```

GlobalExceptiions.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.service.impl;

import com.ybchen.springboot_shiro.dao.RoleMapper;
import com.ybchen.springboot_shiro.dao.UserMapper;
import com.ybchen.springboot_shiro.domain.Role;
import com.ybchen.springboot_shiro.domain.User;
import com.ybchen.springboot_shiro.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 1:15 上午
 * @Versiion：1.0
 */
@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserMapper userMapper;
    @Autowired
    private RoleMapper roleMapper;

    @Override
    public User findAllUserInfoByUserName(String userName) {
        User user = userMapper.findByUserName(userName);
        //用户角色的集合
        List<Role> roleList = roleMapper.findRoleListByUserId(user.getId());
        user.setRoleList(roleList);
        return user;
    }

    @Override
    public User findSimpleUserInfoById(int userId) {
        return userMapper.findById(userId);
    }

    @Override
    public User findSimpleUserInfoByUserName(String userName) {
        return userMapper.findByUserName(userName);
    }
}
```

UserServiceImpl.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.service;

import com.ybchen.springboot_shiro.domain.User;

public interface UserService {
    /**
     * 获取全部用户信息，包括角色、权限
     * @param userName
     * @return
     */
    User findAllUserInfoByUserName(String userName);

    /**
     * 获取用户基本信息
     * @param userId
     * @return
     */
    User findSimpleUserInfoById(int userId);

    /**
     * 根据用户名查询用户信息
     * @param userName
     * @return
     */
    User findSimpleUserInfoByUserName(String userName);
}
```

UserService.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.utils;

import java.io.Serializable;

public class JsonData implements Serializable {
    private static final long serialVersionUID = 1L;
    /**
     * 状态码，0表示成功过，1表示处理中，-1表示失败
     */
    private Integer code;
    /**
     * 业务数据
     */
    private Object data;
    /**
     * 信息描述
     */
    private String msg;

    public JsonData() {
    }

    public JsonData(Integer code, Object data, String msg) {
        this.code = code;
        this.data = data;
        this.msg = msg;
    }

    /**
     * 成功，不用返回数据
     *
     * @return
     */
    public static JsonData buildSuccess() {
        return new JsonData(0, null, null);
    }

    /**
     * 成功，返回数据
     *
     * @param data 返回数据
     * @return
     */
    public static JsonData buildSuccess(Object data) {
        return new JsonData(0, data, null);
    }

    /**
     * 成功，返回数据
     *
     * @param code 状态码
     * @param data 返回数据
     * @return
     */
    public static JsonData buildSuccess(int code, Object data) {
        return new JsonData(code, data, null);
    }

    /**
     * 失败，返回信息
     *
     * @param msg 返回信息
     * @return
     */
    public static JsonData buildError(String msg) {
        return new JsonData(-1, null, msg);
    }

    /**
     * 失败，返回信息和状态码
     *
     * @param code 状态码
     * @param msg  返回信息
     * @return
     */
    public static JsonData buildError(Integer code, String msg) {
        return new JsonData(code, null, msg);
    }

    public Integer getCode() {
        return code;
    }

    public void setCode(Integer code) {
        this.code = code;
    }

    public Object getData() {
        return data;
    }

    public void setData(Object data) {
        this.data = data;
    }

    public String getMsg() {
        return msg;
    }

    public void setMsg(String msg) {
        this.msg = msg;
    }

    @Override
    public String toString() {
        return "JsonData{" +
                "code=" + code +
                ", data=" + data +
                ", msg='" + msg + '\'' +
                '}';
    }
}
```

JsonData.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
//扫描mapper
@MapperScan(value = "com.ybchen.springboot_shiro.dao")
public class SpringbootShiroApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringbootShiroApplication.class, args);
    }

}
```

SpringbootShiroApplication.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
server.port=12888
#============数据库=================
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/shiro_2?useUnicode=true&characterEncoding=utf-8&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
# 使用阿里巴巴druid数据源，默认使用自带的
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
# 开启控制台打印sql
mybatis.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
# mybatis下划线转驼峰配置
mybatis.configuration.map-underscore-to-camel-case=true
```

application.properties

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro;

import org.apache.shiro.crypto.hash.SimpleHash;
import org.junit.Test;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 10:12 下午
 * @Versiion：1.0
 */
public class Md5Test {
    @Test
    public void testMd5(){
        String hashName="md5";
        String pwd="123";
        SimpleHash simpleHash = new SimpleHash(hashName, pwd, null, 2);
        System.out.println(simpleHash);
    }
}
```

Md5Test.java

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.4.1</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.ybchen</groupId>
    <artifactId>springboot_shiro</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springboot_shiro</name>
    <description>SpringBoot整合Shiro</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <scope>test</scope>
        </dependency>
        <!--druid-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.2.3</version>
        </dependency>
        <!--mysql-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!--shiro-->
        <dependency>
            <groupId>org.apache.shiro</groupId>
            <artifactId>shiro-spring</artifactId>
            <version>1.7.0</version>
        </dependency>
        <!--mybatis-->
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>2.1.4</version>
        </dependency>

    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

pom.xml

## 项目源码

```text
链接: https://pan.baidu.com/s/1adjwICKge83YcPycE8ZaEQ  密码: if9s
```

## 项目postman测试

```text
127.0.0.1:12888/pub/index

127.0.0.1:12888/pub/not_permit

127.0.0.1:12888/pub/need_login

127.0.0.1:12888/pub/login

127.0.0.1:12888/authc/video/play_record

127.0.0.1:12888/admin/video/video_list

127.0.0.1:12888/video/add

127.0.0.1:12888/video/update
```

![](./images/images/img_016_781c1f1cb7c4.gif)

### 备注

　　因为链接较多，就不一一做gif动图了，直接导入项目源码，请求的时候，在header上加入token即可~

## Filter过滤器

### 业务需求

- 一个接口，可以让2个角色中的任意一个访问
- 自定义一个类，继承：AuthorizationFilter

```text
package com.ybchen.springboot_shiro.config;

import org.apache.shiro.subject.Subject;
import org.apache.shiro.util.CollectionUtils;
import org.apache.shiro.web.filter.authz.AuthorizationFilter;

import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import java.util.Set;

/**
 * @Description：自定义Filter
 * @Author：chenyanbin
 * @Date：2021/1/4 11:14 下午
 * @Versiion：1.0
 */
public class CustomRolesOrAuthorizationFilter extends AuthorizationFilter {
    @Override
    protected boolean isAccessAllowed(ServletRequest request, ServletResponse response, Object mappedValue) throws Exception {
        Subject subject = getSubject(request, response);
        //filterChainDefinitionMap.put("/admin/**", "roles[admin,user]"); mappedValue <==> admin,user
        String[] rolesArray = (String[]) mappedValue;
        if (rolesArray == null || rolesArray.length == 0) {
            return true;
        }
        Set<String> roles = CollectionUtils.asSet(rolesArray);
        //当前subject是roles中的任意一个，则有权限访问
        for (String role : roles) {
            if (subject.hasRole(role)) {
                return true;
            }
        }
        return false;
    }
}
```

![](./images/images/img_017_9412d1869148.gif)

```text
    @Bean
    public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
        System.out.println("ShiroConfig ShiroFilterFactoryBean 执行");
        ShiroFilterFactoryBean shiroFilterFactoryBean = new ShiroFilterFactoryBean();
        //设置SecurityManager
        shiroFilterFactoryBean.setSecurityManager(securityManager);
        //如果访问需要登录的某个接口，却没有登录，则调用此接口(如果不是前后端分离，则跳转页面)
        shiroFilterFactoryBean.setLoginUrl("/pub/need_login");
        //shiroFilterFactoryBean.setLoginUrl("/xxx.jsp");
        //登录成功后，跳转的链接，若前后端分离，没必要设置这个
        //shiroFilterFactoryBean.setSuccessUrl("");
        //登录成功，未授权会调用此方法
        shiroFilterFactoryBean.setUnauthorizedUrl("/pub/not_permit");

        //设置自定义Filter
        Map<String, Filter> filterMap=new LinkedHashMap<>();
        filterMap.put("roleOrFilter",new CustomRolesOrAuthorizationFilter());
        shiroFilterFactoryBean.setFilters(filterMap);

        //拦截路径，必须使用:LinkedHashMap，要不然拦截效果会时有时无，因为使用的是无序的Map
        Map<String, String> filterChainDefinitionMap = new LinkedHashMap<>();
        //key=正则表达式路径，value=org.apache.shiro.web.filter.mgt.DefaultFilter
        //退出过滤器
        filterChainDefinitionMap.put("/logout", "logout");
        //匿名可以访问，游客模式
        filterChainDefinitionMap.put("/pub/**", "anon");
        //登录用户才可以访问
        filterChainDefinitionMap.put("/authc/**", "authc");
        //管理员角色才能访问
//        filterChainDefinitionMap.put("/admin/**", "roles[admin,user]");
        filterChainDefinitionMap.put("/admin/**", "roleOrFilter[admin,user]");
        //有编辑权限才能访问
        filterChainDefinitionMap.put("/video/update", "perms[video_update]");
        //authc：url必须通过认证才可以访问
        //anon：url可以匿名访问
        //过滤链是顺序执行，从上而下，一般把/**，放到最下面
        filterChainDefinitionMap.put("/**", "authc");
        shiroFilterFactoryBean.setFilterChainDefinitionMap(filterChainDefinitionMap);
        return shiroFilterFactoryBean;
    }
```

## Redis整合CacheManager

### 原因

　　授权的时候每次都去查询数据库，对于频繁访问的接口，性能和响应速度比较慢，此处可以使用缓存，提高响应速度，也可以使用**Guava**(**本地内存缓存**)。

**Redis**(**分布式缓存**)还不了解的小伙伴，在这里我就不一一讲解了，可以看我以前写过的博客。

- Redis 从**入门到精通**：[点我直达](https://www.cnblogs.com/chenyanbin/p/12073107.html)
- Redis 微信**抢红包**，电商场景下**秒杀**系统设计：[点我直达](https://www.cnblogs.com/chenyanbin/p/13587508.html)
- Redis **高级**项目**实战**：[点我直达](https://www.cnblogs.com/chenyanbin/p/13506946.html)

### 添加依赖

```text
        <!--shiro+redis-->
        <dependency>
            <groupId>org.crazycake</groupId>
            <artifactId>shiro-redis</artifactId>
            <version>3.3.1</version>
        </dependency>
```

在ShiroConfig中添加如下代码

```text
//使用自定义cacheManager
    securityManager.setCacheManager(cacheManager());

    /**
     * 配置redisManager
     * @return
     */
    public RedisManager getRedisManager(){
        RedisManager redisManager=new RedisManager();
        redisManager.setHost("127.0.0.1:6379");
        //连接那个数据库
        redisManager.setDatabase(0);
        //设置密码
//        redisManager.setPassword("123");
        return redisManager;
    }

    /**
     * 设置具体cache实现类
     * @return
     */
    public RedisCacheManager cacheManager(){
        RedisCacheManager redisCacheManager=new RedisCacheManager();
        redisCacheManager.setRedisManager(getRedisManager());
        return redisCacheManager;
    }
```

![](./images/images/img_018_df03f2a506cd.png)

修改CustomRealm

![](./images/images/img_019_f51ef251ba08.gif)

设置redis缓存过期时间

![](./images/images/img_020_7efc3caab0f3.gif)

## Redis整合SessionManager

### 为啥Session也要持久化

　　重启应用，用户无感知，可以继续以原先的状态继续访问。

修改shiroconfig

![](./images/images/img_021_871af8849bb2.png)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.springboot_shiro.config;

import org.apache.shiro.authc.credential.HashedCredentialsMatcher;
import org.apache.shiro.mgt.SecurityManager;
import org.apache.shiro.session.mgt.SessionManager;
import org.apache.shiro.spring.web.ShiroFilterFactoryBean;
import org.apache.shiro.web.mgt.DefaultWebSecurityManager;
import org.crazycake.shiro.RedisCacheManager;
import org.crazycake.shiro.RedisManager;
import org.crazycake.shiro.RedisSessionDAO;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.servlet.Filter;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/1/3 4:12 下午
 * @Versiion：1.0
 */
@Configuration
public class ShiroConfig {
    @Bean
    public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
        System.out.println("ShiroConfig ShiroFilterFactoryBean 执行");
        ShiroFilterFactoryBean shiroFilterFactoryBean = new ShiroFilterFactoryBean();
        //设置SecurityManager
        shiroFilterFactoryBean.setSecurityManager(securityManager);
        //如果访问需要登录的某个接口，却没有登录，则调用此接口(如果不是前后端分离，则跳转页面)
        shiroFilterFactoryBean.setLoginUrl("/pub/need_login");
        //shiroFilterFactoryBean.setLoginUrl("/xxx.jsp");
        //登录成功后，跳转的链接，若前后端分离，没必要设置这个
        //shiroFilterFactoryBean.setSuccessUrl("");
        //登录成功，未授权会调用此方法
        shiroFilterFactoryBean.setUnauthorizedUrl("/pub/not_permit");

        //设置自定义Filter
        Map<String, Filter> filterMap=new LinkedHashMap<>();
        filterMap.put("roleOrFilter",new CustomRolesOrAuthorizationFilter());
        shiroFilterFactoryBean.setFilters(filterMap);

        //拦截路径，必须使用:LinkedHashMap，要不然拦截效果会时有时无，因为使用的是无序的Map
        Map<String, String> filterChainDefinitionMap = new LinkedHashMap<>();
        //key=正则表达式路径，value=org.apache.shiro.web.filter.mgt.DefaultFilter
        //退出过滤器
        filterChainDefinitionMap.put("/logout", "logout");
        //匿名可以访问，游客模式
        filterChainDefinitionMap.put("/pub/**", "anon");
        //登录用户才可以访问
        filterChainDefinitionMap.put("/authc/**", "authc");
        //管理员角色才能访问
//        filterChainDefinitionMap.put("/admin/**", "roles[admin,user]");
        filterChainDefinitionMap.put("/admin/**", "roleOrFilter[admin,user]");
        //有编辑权限才能访问
        filterChainDefinitionMap.put("/video/update", "perms[video_update]");
        //authc：url必须通过认证才可以访问
        //anon：url可以匿名访问
        //过滤链是顺序执行，从上而下，一般把/**，放到最下面
        filterChainDefinitionMap.put("/**", "authc");
        shiroFilterFactoryBean.setFilterChainDefinitionMap(filterChainDefinitionMap);
        return shiroFilterFactoryBean;
    }

    @Bean
    public SecurityManager securityManager() {
        DefaultWebSecurityManager securityManager = new DefaultWebSecurityManager();
        //如果不是前后端分离，不用设置setSessionManager
        securityManager.setSessionManager(sessionManager());
        //使用自定义cacheManager
        securityManager.setCacheManager(cacheManager());
        securityManager.setRealm(customRealm());
        return securityManager;
    }

    /**
     * 配置redisManager
     * @return
     */
    public RedisManager getRedisManager(){
        RedisManager redisManager=new RedisManager();
        redisManager.setHost("127.0.0.1:6379");
        //连接那个数据库
        redisManager.setDatabase(0);
        //设置密码
//        redisManager.setPassword("123");
        return redisManager;
    }

    /**
     * 设置具体cache实现类
     * @return
     */
    public RedisCacheManager cacheManager(){
        RedisCacheManager redisCacheManager=new RedisCacheManager();
        redisCacheManager.setRedisManager(getRedisManager());
        //设置缓存过期时间
        redisCacheManager.setExpire(20);
        return redisCacheManager;
    }

    /**
     * 自定义realm
     *
     * @return
     */
    @Bean
    public CustomRealm customRealm() {
        CustomRealm customRealm = new CustomRealm();
        //因为数据库密码存的是明文，所以无需使用双重md5校验
//        customRealm.setCredentialsMatcher(hashedCredentialsMatcher());
        return customRealm;
    }

    /**
     * 密码验证器，双重md5
     *
     * @return
     */
    @Bean
    public HashedCredentialsMatcher hashedCredentialsMatcher() {
        HashedCredentialsMatcher hashedCredentialsMatcher = new HashedCredentialsMatcher();
        //设置散列算法，使用md5算法
        hashedCredentialsMatcher.setHashAlgorithmName("md5");
        //散列次数，使用2次md5算法，相当于md5(md5(xxx))
        hashedCredentialsMatcher.setHashIterations(2);
        return hashedCredentialsMatcher;
    }

    /**
     * 自定义SessionManager
     *
     * @return
     */
    @Bean
    public SessionManager sessionManager() {
        CustomSessionManager customSessionManager = new CustomSessionManager();
        //超时时间，默认 30分钟，会话超时，单位毫秒
//        customSessionManager.setGlobalSessionTimeout(200000);
        //配置session持久化
        customSessionManager.setSessionDAO(redisSessionDAO());
        return customSessionManager;
    }

    /**
     * 自定义session持久化
     * @return
     */
    public RedisSessionDAO redisSessionDAO(){
        RedisSessionDAO redisSessionDAO=new RedisSessionDAO();
        redisSessionDAO.setRedisManager(getRedisManager());
        return redisSessionDAO;
    }
}
```

ShiroConfig.java

## Shiro整合Redis后的源码

```text
链接: https://pan.baidu.com/s/1cNQfBiw50A-U5izzOQclpw  密码: 6wqt
```
