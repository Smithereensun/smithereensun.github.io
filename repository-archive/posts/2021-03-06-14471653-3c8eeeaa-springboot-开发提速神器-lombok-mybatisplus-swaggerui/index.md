{

  "title": "SpringBoot 开发提速神器 Lombok+MybatisPlus+SwaggerUI",
  "date": "2021-03-06",
  "description": "导读 Lombok：可以让你的POJO代码特别简洁，不止简单在BO/VO/DTO/DO等大量使用，还有设计模式，对象对比等 MybatisPlus：增加版Mybatis，基础的数据库CRUD、分页等可以直接生成使用，避免了大量的重复低效代码，还有数据库自动Java类，sql文件等等，比传统的更贱简介",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/mybatis-plus.html"

}

# 导读

- Lombok：可以让你的POJO代码特别简洁，不止简单在BO/VO/DTO/DO等大量使用，还有设计模式，对象对比等
- MybatisPlus：增加版Mybatis，基础的数据库CRUD、分页等可以直接生成使用，避免了大量的重复低效代码，还有数据库自动Java类，sql文件等等，比传统的更贱简介易用
- SwaggerUI：接口文档自动生成，对接前端和测试更加方便，基于业界的OpennApi规范，采用Swagger3.x版本。

## 技术栈

　　SpringBoot2.4+ MybatisPlus+Lombok+Swagger3.x+jdk8+IDEA

# 在线构建项目

[点我直达](https://start.spring.io/)

![](./images/images/img_001_9ce36cae093c.png)

# 什么是lombok

## 官网

[点我直达](https://projectlombok.org/)

　　一个优秀的Java代码库，简化了Java的编码，为Java代码的精简提供了一种方式

## 添加依赖

```text
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.16</version>
            <!--scope=provided，说明它是在编译阶段生效，不需要打入包中，Lombok在编译期将带Lombok注解的Java文件正确编译为完整的Class文件-->
            <scope>provided</scope>
        </dependency>
```

## 常见注解@Getter/@Setter

- 作用类上，生成所有成员变量的getter/setter方法
- 作用于成员变量上，生成该成员变量的getter/setter方法
- 方法控制访问级别set和get注解加上@Getter(AccessLevel.PROTECTED)

### 编译查看字节码

```text
mvn compile
```

![](./images/images/img_002_6b6d072db7c7.gif)

![](./images/images/img_003_b3ceeab6c867.gif)

```text
package com.ybchen.shopmanager.model;

import lombok.AccessLevel;
import lombok.Getter;
import lombok.Setter;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/3/2 下午9:43
 * @Versiion：1.0
 */
@Getter
@Setter
public class User {
    //不想生成get方法
    @Getter(AccessLevel.NONE)
    int id;
    //只会去生成get
    final String name = "alex";
    String phone;
    //静态成员变量不会生成set/get方法
    static final String pwd = "123";
}
```

## @NonNull

- 作用于方法上或者属性，用于非空判断，如果为空则抛异常

![](./images/images/img_004_1f032e6ea439.gif)

## @NoArgsContructor

- 生成无参构造器

![](./images/images/img_005_c1807d6235d4.gif)

## @AllArgsConstructor

- 生成全参构造器

![](./images/images/img_006_480ca1862a29.gif)

## @RequiredArgsConstructor

指定参数的构造函数，有以下的特征的字段

- final类型未被初始化的属性，标记了@NonNull的属性
- 注意：@NoArgsConstructor不能添加

![](./images/images/img_007_4b534c505521.gif)

## @ToString

- List或者其他集合调试不方便
- 控制台或者日志输出对象，默认打印的是内存地址
- 作用于类，覆盖默认的toString()方法

![](./images/images/img_008_2762918764ba.gif)

### 不包括某个字段

@ToString(exclude={"age"})

### 只输出某个字段

@ToString(of={"name"})

![](./images/images/img_009_3669de195510.gif)

## 为什么对象要重写hashcode和equal方法

### HashCode方法

- 顶级类Object里面的方法，所有类都是继承Object的，返回值Int类型
- 根据一定的hash规则(存储地址，字段，或者长度等)，映射成一个数值，即散列值

### Equals方法

- 顶级类Object里面的方法，所有类都是继承Object的，返回值boolean类型
- 根据自定义的匹配规则，用于匹配两个对象是否一样，一般逻辑如下

```text
1、判断地址是否一样
2、非空判断和class类型判断
3、强转
4、对象里面的字段一一匹配
```

### 解析

　　如果两个对象相等，那么它们的hashCode()值一定相同。如果两个对象hashCode()相等，它们并不一定相等。在散列表中hashCode()相等，即两个键值的哈希值相等。然后哈希值相等，并不一定得出键值对相等，就出现所谓的哈希冲突场景，还需要equals方法判断对象是否相等。

### 应用场景

　　当向集合中插入对象时，如何判别在集合中是否已经存在该对象，比如Set确保存储对象的唯一值，并判断是否同一个对象呢？

```text
依据hashCode和equals进行判断
所以Set存储的对象必须重写这两个方法，判断两个对象是否一样
首先判断插入对象的hashCode值是否存在，hashCode值不存在则直接插入集合；值存在则还需要判断equals方法判断对象是否相等
```

![](./images/images/img_010_9ea5ceeb5391.gif)

## @EqualsAndHashCode

- 作用于类，覆盖默认的equals和hashCode，作用于全部属性
- 不包含某个属性

  - @EqualsAndHashCode(exclude={"id"})

- 只输出某个属性

  - @EqualsAndHashCode(of={"id"})

![](./images/images/img_011_6288698ec202.gif)

## @Data

- 作用于类上，是以下注解的集合

  - @ToString
  - @EqualsAndHashCode
  - @Getter
  - @Setter
  - @RequiredArgsConstructor

![](./images/images/img_012_9a280a130723.gif)

## @Builder

- 场景：当一个bean类重载了多个构造方法时，并且参数随机使用时，考虑使用构造者模式

![](./images/images/img_013_269dbd6511e0.gif)

## @Lof/@Slf4j

- 作用于类上，生成日志变量，用于记录日志

![](./images/images/img_014_4beafa06090f.gif)

# MybatisPlus

## 介绍

- 官网：[点我直达](https://mp.baomidou.com/)
- 是一个mybatis的增强工具，在Mybatis的基础上只做强增不做改变，为简化开发，提高效率

## 数据库脚本

![](./images/images/img_015_8f900a89c634.gif)
![](./images/images/img_016_961ddebeb323.gif)

```text
/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50728
 Source Host           : localhost:3306
 Source Schema         : shop

 Target Server Type    : MySQL
 Target Server Version : 50728
 File Encoding         : 65001

 Date: 04/03/2021 22:17:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for address
-- ----------------------------
DROP TABLE IF EXISTS `address`;
CREATE TABLE `address` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) DEFAULT NULL COMMENT '用户id',
  `default_status` int(1) DEFAULT NULL COMMENT '是否默认收货地址：0->否；1->是',
  `receive_name` varchar(64) DEFAULT NULL COMMENT '收发货人姓名',
  `phone` varchar(64) DEFAULT NULL COMMENT '收货人电话',
  `province` varchar(64) DEFAULT NULL COMMENT '省/直辖市',
  `city` varchar(64) DEFAULT NULL COMMENT '市',
  `region` varchar(64) DEFAULT NULL COMMENT '区',
  `detail_address` varchar(200) DEFAULT NULL COMMENT '详细地址',
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='电商-公司收发货地址表';

-- ----------------------------
-- Records of address
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for banner
-- ----------------------------
DROP TABLE IF EXISTS `banner`;
CREATE TABLE `banner` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `img` varchar(524) DEFAULT NULL COMMENT '图片',
  `url` varchar(524) DEFAULT NULL COMMENT '跳转地址',
  `weight` int(11) DEFAULT NULL COMMENT '权重',
  `version` int(11) DEFAULT '1',
  `deleted` int(11) DEFAULT '0' COMMENT '0是未删除，1是已经删除',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of banner
-- ----------------------------
BEGIN;
INSERT INTO `banner` VALUES (1, 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 'https://www.cnblogs.com/chenyanbin/', 1, 2, 1);
INSERT INTO `banner` VALUES (2, 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 'https://www.cnblogs.com/chenyanbin/', 3, 1, 0);
INSERT INTO `banner` VALUES (3, 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 'https://www.cnblogs.com/chenyanbin/', 2, 1, 0);
INSERT INTO `banner` VALUES (7, 'werw', 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 2, 1, 0);
INSERT INTO `banner` VALUES (8, '666666', 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 2, 1, 0);
INSERT INTO `banner` VALUES (9, 'sdfds', 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 2, 1, 0);
INSERT INTO `banner` VALUES (10, '323232', 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 2, 1, 0);
INSERT INTO `banner` VALUES (11, '532', 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 2, 1, 0);
INSERT INTO `banner` VALUES (12, '6666', 'https://images.cnblogs.com/cnblogs_com/chenyanbin/1560326/o_qianxun.jpg', 2, 1, 0);
COMMIT;

-- ----------------------------
-- Table structure for coupon
-- ----------------------------
DROP TABLE IF EXISTS `coupon`;
CREATE TABLE `coupon` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `category` varchar(11) DEFAULT NULL COMMENT '优惠卷类型[NEW_USER注册赠券，TASK任务卷，PROMOTION促销劵]',
  `publish` varchar(11) DEFAULT NULL COMMENT '发布状态, PUBLISH发布，DRAFT草稿，OFFLINE下线',
  `coupon_img` varchar(524) DEFAULT NULL COMMENT '优惠券图片',
  `coupon_title` varchar(128) DEFAULT NULL COMMENT '优惠券标题',
  `price` decimal(16,2) DEFAULT NULL COMMENT '抵扣价格',
  `user_limit` int(11) DEFAULT NULL COMMENT '每人限制张数',
  `start_time` datetime DEFAULT NULL COMMENT '优惠券开始有效时间',
  `end_time` datetime DEFAULT NULL COMMENT '优惠券失效时间',
  `publish_count` int(11) DEFAULT NULL COMMENT '优惠券总量',
  `stock` int(11) DEFAULT '0' COMMENT '库存',
  `add_one` int(11) DEFAULT NULL COMMENT '是否叠加0是不行，1是可以',
  `create_time` datetime DEFAULT NULL,
  `condition_price` decimal(16,2) DEFAULT NULL COMMENT '满多少才可以使用',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of coupon
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(128) DEFAULT NULL COMMENT '标题',
  `cover_img` varchar(128) DEFAULT NULL COMMENT '封面图',
  `detail` varchar(256) DEFAULT '' COMMENT '详情',
  `old_price` decimal(16,2) DEFAULT NULL COMMENT '老价格',
  `price` decimal(16,2) DEFAULT NULL COMMENT '新价格',
  `stock` int(11) DEFAULT NULL COMMENT '库存',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `lock_stock` int(11) DEFAULT '0' COMMENT '锁定库存',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of product
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for product_order
-- ----------------------------
DROP TABLE IF EXISTS `product_order`;
CREATE TABLE `product_order` (
  `id` bigint(11) NOT NULL AUTO_INCREMENT,
  `out_trade_no` varchar(64) DEFAULT NULL COMMENT '订单唯一标识',
  `state` varchar(11) DEFAULT NULL COMMENT 'NEW 未支付订单,PAY已经支付订单,CANCEL超时取消订单',
  `create_time` datetime DEFAULT NULL COMMENT '订单生成时间',
  `total_fee` decimal(16,2) DEFAULT NULL COMMENT '订单总金额',
  `pay_fee` decimal(16,2) DEFAULT NULL COMMENT '订单实际支付价格',
  `pay_type` varchar(64) DEFAULT NULL COMMENT '支付类型，微信-银行-支付宝',
  `nickname` varchar(64) DEFAULT NULL COMMENT '昵称',
  `head_img` varchar(524) DEFAULT NULL COMMENT '头像',
  `user_id` int(11) DEFAULT NULL COMMENT '用户id',
  `del` int(5) DEFAULT '0' COMMENT '0表示未删除，1表示已经删除',
  `update_time` datetime DEFAULT NULL COMMENT '更新时间',
  `order_type` varchar(32) DEFAULT NULL COMMENT '订单类型 DAILY普通单，PROMOTION促销订单',
  `receiver_address` varchar(1024) DEFAULT NULL COMMENT '收货地址 json存储',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of product_order
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for product_order_item
-- ----------------------------
DROP TABLE IF EXISTS `product_order_item`;
CREATE TABLE `product_order_item` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `product_order_id` bigint(11) DEFAULT NULL COMMENT '订单号',
  `out_trade_no` varchar(32) DEFAULT NULL,
  `product_id` bigint(11) DEFAULT NULL COMMENT '产品id',
  `product_name` varchar(128) DEFAULT NULL COMMENT '商品名称',
  `product_img` varchar(524) DEFAULT NULL COMMENT '商品图片',
  `buy_num` int(11) DEFAULT NULL COMMENT '购买数量',
  `create_time` datetime DEFAULT NULL,
  `total_fee` decimal(16,2) DEFAULT NULL COMMENT '购物项商品总价格',
  `pay_fee` decimal(16,0) DEFAULT NULL COMMENT '购物项商品支付总价格',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of product_order_item
-- ----------------------------
BEGIN;
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` bigint(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(128) DEFAULT NULL COMMENT '昵称',
  `pwd` varchar(124) DEFAULT NULL COMMENT '密码',
  `head_img` varchar(524) DEFAULT NULL COMMENT '头像',
  `slogan` varchar(524) DEFAULT NULL COMMENT '用户签名',
  `sex` tinyint(2) DEFAULT '1' COMMENT '0表示女，1表示男',
  `points` int(10) DEFAULT '0' COMMENT '积分',
  `create_time` datetime DEFAULT NULL,
  `mail` varchar(64) DEFAULT NULL COMMENT '邮箱',
  `secret` varchar(12) DEFAULT NULL COMMENT '盐，用于个人敏感信息处理',
  PRIMARY KEY (`id`),
  UNIQUE KEY `mail_idx` (`mail`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
```

建表语句

## 添加依赖

pom.xml

```text
        <!--mysql-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!--mybatis plus和spring boot整合-->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.4.0</version>
        </dependency>
```

![](./images/images/img_015_8f900a89c634.gif)
![](./images/images/img_016_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.4.3</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.ybchen</groupId>
    <artifactId>shop-manager</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>shop-manager</name>
    <description>Demo project for Spring Boot</description>
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
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.16</version>
            <!--scope=provided，说明它是在编译阶段生效，不需要打入包中，Lombok在编译期将带Lombok注解的Java文件正确编译为完整的Class文件-->
            <scope>provided</scope>
        </dependency>
        <!--mysql-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!--mybatis plus和spring boot整合-->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.4.0</version>
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

    <!-- 代码库 -->
    <repositories>
        <repository>
            <id>maven-ali</id>
            <url>http://maven.aliyun.com/nexus/content/groups/public//</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>true</enabled>
                <updatePolicy>always</updatePolicy>
                <checksumPolicy>fail</checksumPolicy>
            </snapshots>
        </repository>
    </repositories>
    <pluginRepositories>
        <pluginRepository>
            <id>public</id>
            <name>aliyun nexus</name>
            <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
            <releases>
                <enabled>true</enabled>
            </releases>
            <snapshots>
                <enabled>false</enabled>
            </snapshots>
        </pluginRepository>
    </pluginRepositories>
</project>
```

完整pom.xml

### 配置文件

application.properties

```text
# 端口号
server.port=9999
#===========数据库相关=============
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1/shop?useUnicode=true&characterEncoding=utf-8&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
```

## 配置SpringBoot扫描路径

　　启动类上添加：@MapperScan("Mapper全包路径")

![](./images/images/img_017_b466dd644ae8.png)

## SpringBoot整合MybatisPlus

### 统一接口返回协议

```text
package com.ybchen.shopmanager.utils;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class JsonData implements Serializable {
    /**
     * 状态码 0 表示成功，1 表示处理中，-1表示失败
     */
    private Integer code;
    /**
     * 数据
     */
    private Object data;
    /**
     * 描述信息
     */
    private String msg;

    /**
     * 成功，无传入数据
     *
     * @return
     */
    public static JsonData buildSuccess() {
        return new JsonData(0, null, null);
    }

    /**
     * 成功，有传入数据
     *
     * @param data 数据
     * @return
     */
    public static JsonData buildSuccess(Object data) {
        return new JsonData(0, data, null);
    }

    /**
     * 失败，有返回错误信息
     *
     * @param msg 描述信息
     * @return
     */
    public static JsonData buildError(String msg) {
        return new JsonData(-1, null, msg);
    }

    /**
     * 失败，有状态码，描述信息
     *
     * @param code 状态码
     * @param msg  描述信息
     * @return
     */
    public static JsonData buildError(Integer code, String msg) {
        return new JsonData(code, null, msg);
    }

    /**
     * 是否返回成功
     * @param jsonData
     * @return
     */
    public static boolean isSuccess(JsonData jsonData) {
        return jsonData.getCode() == 0;
    }
}
```

### 实体类

```text
package com.ybchen.shopmanager.model;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

/**
 * @Description：轮播图
 * @Author：chenyanbin
 * @Date：2021/3/4 下午11:00
 * @Versiion：1.0
 */
@Data
//数据库表名
@TableName("banner")
public class BannerDO {
    /**
     * 主键
     */
    private Integer id;
    /**
     * 图片
     */
    private String img;
    /**
     * url跳转地址
     */
    private String url;
    /**
     * 权重
     */
    private Integer weight;
    /**
     * 版本号
     */
    private Integer version;
    /**
     * 0是未删除，1是已经删除
     */
    private Integer deleted;
}
```

### Service

```text
package com.ybchen.shopmanager.service;

import com.ybchen.shopmanager.model.BannerDO;

import java.util.List;

public interface BannerService {
    List<BannerDO> list();
}
```

```text
package com.ybchen.shopmanager.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.ybchen.shopmanager.mapper.BannerMapper;
import com.ybchen.shopmanager.model.BannerDO;
import com.ybchen.shopmanager.service.BannerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * @Description：轮播图Service
 * @Author：chenyanbin
 * @Date：2021/3/4 下午11:04
 * @Versiion：1.0
 */
@Service
public class BannerServiceImpl implements BannerService {
    @Autowired
    private BannerMapper bannerMapper;
    @Override
    public List<BannerDO> list() {
        return bannerMapper.selectList(new QueryWrapper<>());
    }
}
```

### Controller

```text
package com.ybchen.shopmanager.controller;

import com.ybchen.shopmanager.service.BannerService;
import com.ybchen.shopmanager.utils.JsonData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @Description：轮播图Controller
 * @Author：chenyanbin
 * @Date：2021/3/4 下午11:06
 * @Versiion：1.0
 */
@RestController
@RequestMapping("api/v1/banner")
public class BannerController {
    @Autowired
    private BannerService bannerService;
    @GetMapping("list")
    public JsonData list(){
        return JsonData.buildSuccess(bannerService.list());
    }
}
```

### 测试

![](./images/images/img_018_ee95ab6585ac.gif)

## 单元测试+控制台打印sql

### 单元测试

```text
package com.ybchen.shopmanager;

import com.ybchen.shopmanager.model.BannerDO;
import com.ybchen.shopmanager.service.BannerService;
import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.List;

//classes=启动类.class
@SpringBootTest(classes = ShopManagerApplication.class)
@Slf4j
public class BannerTest {
    @Autowired
    private BannerService bannerService;

    @Test
    public void testBannerTest() {
        List<BannerDO> list = bannerService.list();
        log.info("轮播图列表：{}", list);
    }
}
```

### 配置文件

application.properties

```text
# 配置mybatis plus打印sql日志
mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
```

### 测试

![](./images/images/img_019_c87a3f384c2b.gif)

## BaseMapper

- Mapper继承该接口后，无需编写mapper.xml文件，即可获得CRUD功能

```text
/*
 * Copyright (c) 2011-2020, baomidou (jobob@qq.com).
 * <p>
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy of
 * the License at
 * <p>
 * https://www.apache.org/licenses/LICENSE-2.0
 * <p>
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations under
 * the License.
 */
package com.baomidou.mybatisplus.core.mapper;

import com.baomidou.mybatisplus.core.conditions.Wrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.core.toolkit.Constants;
import org.apache.ibatis.annotations.Param;

import java.io.Serializable;
import java.util.Collection;
import java.util.List;
import java.util.Map;

/*

               :`
                    .:,
                     :::,,.
             ::      `::::::
             ::`    `,:,` .:`
             `:: `::::::::.:`      `:';,`
              ::::,     .:::`   `@++++++++:
               ``        :::`  @+++++++++++#
                         :::, #++++++++++++++`
                 ,:      `::::::;'##++++++++++
                 .@#@;`   ::::::::::::::::::::;
                  #@####@, :::::::::::::::+#;::.
                  @@######+@:::::::::::::.  #@:;
           ,      @@########':::::::::::: .#''':`
           ;##@@@+:##########@::::::::::: @#;.,:.
            #@@@######++++#####'::::::::: .##+,:#`
            @@@@@#####+++++'#####+::::::::` ,`::@#:`
            `@@@@#####++++++'#####+#':::::::::::@.
             @@@@######+++++''#######+##';::::;':,`
              @@@@#####+++++'''#######++++++++++`
               #@@#####++++++''########++++++++'
               `#@######+++++''+########+++++++;
                `@@#####+++++''##########++++++,
                 @@######+++++'##########+++++#`
                @@@@#####+++++############++++;
              ;#@@@@@####++++##############+++,
             @@@@@@@@@@@###@###############++'
           @#@@@@@@@@@@@@###################+:
        `@#@@@@@@@@@@@@@@###################'`
      :@#@@@@@@@@@@@@@@@@@##################,
      ,@@@@@@@@@@@@@@@@@@@@################;
       ,#@@@@@@@@@@@@@@@@@@@##############+`
        .#@@@@@@@@@@@@@@@@@@#############@,
          @@@@@@@@@@@@@@@@@@@###########@,
           :#@@@@@@@@@@@@@@@@##########@,
            `##@@@@@@@@@@@@@@@########+,
              `+@@@@@@@@@@@@@@@#####@:`
                `:@@@@@@@@@@@@@@##@;.
                   `,'@@@@##@@@+;,`
                        ``...``

 _ _     /_ _ _/_. ____  /    _
/ / //_//_//_|/ /_\  /_///_/_\      Talk is cheap. Show me the code.
     _/             /
 */

/**
 * Mapper 继承该接口后，无需编写 mapper.xml 文件，即可获得CRUD功能
 * <p>这个 Mapper 支持 id 泛型</p>
 *
 * @author hubin
 * @since 2016-01-23
 */
public interface BaseMapper<T> extends Mapper<T> {

    /**
     * 插入一条记录
     *
     * @param entity 实体对象
     */
    int insert(T entity);

    /**
     * 根据 ID 删除
     *
     * @param id 主键ID
     */
    int deleteById(Serializable id);

    /**
     * 根据 columnMap 条件，删除记录
     *
     * @param columnMap 表字段 map 对象
     */
    int deleteByMap(@Param(Constants.COLUMN_MAP) Map<String, Object> columnMap);

    /**
     * 根据 entity 条件，删除记录
     *
     * @param wrapper 实体对象封装操作类（可以为 null）
     */
    int delete(@Param(Constants.WRAPPER) Wrapper<T> wrapper);

    /**
     * 删除（根据ID 批量删除）
     *
     * @param idList 主键ID列表(不能为 null 以及 empty)
     */
    int deleteBatchIds(@Param(Constants.COLLECTION) Collection<? extends Serializable> idList);

    /**
     * 根据 ID 修改
     *
     * @param entity 实体对象
     */
    int updateById(@Param(Constants.ENTITY) T entity);

    /**
     * 根据 whereEntity 条件，更新记录
     *
     * @param entity        实体对象 (set 条件值,可以为 null)
     * @param updateWrapper 实体对象封装操作类（可以为 null,里面的 entity 用于生成 where 语句）
     */
    int update(@Param(Constants.ENTITY) T entity, @Param(Constants.WRAPPER) Wrapper<T> updateWrapper);

    /**
     * 根据 ID 查询
     *
     * @param id 主键ID
     */
    T selectById(Serializable id);

    /**
     * 查询（根据ID 批量查询）
     *
     * @param idList 主键ID列表(不能为 null 以及 empty)
     */
    List<T> selectBatchIds(@Param(Constants.COLLECTION) Collection<? extends Serializable> idList);

    /**
     * 查询（根据 columnMap 条件）
     *
     * @param columnMap 表字段 map 对象
     */
    List<T> selectByMap(@Param(Constants.COLUMN_MAP) Map<String, Object> columnMap);

    /**
     * 根据 entity 条件，查询一条记录
     *
     * @param queryWrapper 实体对象封装操作类（可以为 null）
     */
    T selectOne(@Param(Constants.WRAPPER) Wrapper<T> queryWrapper);

    /**
     * 根据 Wrapper 条件，查询总记录数
     *
     * @param queryWrapper 实体对象封装操作类（可以为 null）
     */
    Integer selectCount(@Param(Constants.WRAPPER) Wrapper<T> queryWrapper);

    /**
     * 根据 entity 条件，查询全部记录
     *
     * @param queryWrapper 实体对象封装操作类（可以为 null）
     */
    List<T> selectList(@Param(Constants.WRAPPER) Wrapper<T> queryWrapper);

    /**
     * 根据 Wrapper 条件，查询全部记录
     *
     * @param queryWrapper 实体对象封装操作类（可以为 null）
     */
    List<Map<String, Object>> selectMaps(@Param(Constants.WRAPPER) Wrapper<T> queryWrapper);

    /**
     * 根据 Wrapper 条件，查询全部记录
     * <p>注意： 只返回第一个字段的值</p>
     *
     * @param queryWrapper 实体对象封装操作类（可以为 null）
     */
    List<Object> selectObjs(@Param(Constants.WRAPPER) Wrapper<T> queryWrapper);

    /**
     * 根据 entity 条件，查询全部记录（并翻页）
     *
     * @param page         分页查询条件（可以为 RowBounds.DEFAULT）
     * @param queryWrapper 实体对象封装操作类（可以为 null）
     */
    <E extends IPage<T>> E selectPage(E page, @Param(Constants.WRAPPER) Wrapper<T> queryWrapper);

    /**
     * 根据 Wrapper 条件，查询全部记录（并翻页）
     *
     * @param page         分页查询条件
     * @param queryWrapper 实体对象封装操作类
     */
    <E extends IPage<Map<String, Object>>> E selectMapsPage(E page, @Param(Constants.WRAPPER) Wrapper<T> queryWrapper);
}
```

## Mybatis plus常用注解

- @TableName：用于定义表名
- @TableId：用于定义表的主键

  - value：用于定义主键字段名
  - type：用于定义主键类型（主键策略 IdType）

    - IdType.AUTO：主键自增，系统分配，不需要手动输入
    - IdType.NODE：未设置主键
    - IdType.INPUT：需要自己输入主键值
    - IdType.ASSIGN_ID：系统分配ID，用于数值型数据（Long，对应mysql中的BIGINT类型）
    - IdType.ASSIGN_UUID：系统分配uuid，用于字符串型数据

- TableField：用于定义表的非主键字段

  - value：用于定义非主键字段名，用于别名匹配，假如java对象和数据库属性不一样
  - exist：用于指明是否为数据表的字段，true表示是，false为不是
  - fill：用于指定字段填充策略，一般用于填充：创建时间、修改时间等字段

    - FieldFill.DEFAULT：默认不填充
    - FieldFill.INSERT：插入时填充
    - FieldFill.UPDATE：更新时填充
    - FieldFill.INSERT_UPDATE：插入、更新时填充

## QueryWrapper/LambdaQueryWrapper

　　可以封装sql对象，包括where条件，order by排序

- eq：等于
- ne：不等于
- gt：大于
- ge：大于等于
- lt：小于
- le：小于等于
- or：拼接or
- between：两个值中间
- notBetween：不在两个值中间
- like：模糊匹配
- notLike：不像
- likeLeft：左匹配
- likeRight：右边匹配
- isNull：字段为空
- in：in查询
- groupBy：分组
- orderByAsc：升序
- orderByDesc：降序
- having：having查询

## 分页插件

### 配置类

```text
package com.ybchen.shopmanager.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @Description：分页插件配置
 * @Author：chenyanbin
 * @Date：2021/3/5 下午10:32
 * @Versiion：1.0
 */
@Configuration
public class MybatisPlusPageConfig {

    /**
     * 旧版本
     */
//    @Bean
//    public PaginationInterceptor paginationInterceptor() {
//        PaginationInterceptor paginationInterceptor = new PaginationInterceptor();
//        return paginationInterceptor;
//    }

    /**
     * 新的分页插件，一级和二级缓存遵循mybatis的规则
     * 需要设置 MybatisConfiguration#useDeprecatedExecutor=false 避免缓存出现问题
     */
    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        MybatisPlusInterceptor mybatisPlusInterceptor = new MybatisPlusInterceptor();
        mybatisPlusInterceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
        return mybatisPlusInterceptor;
    }
}
```

### 演示

![](./images/images/img_020_6038f9c0880d.gif)

## 自定义xml的sql脚本

### 新建xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!--这个名称空间是Mapper接口的路径-->
<mapper namespace="com.ybchen.shopmanager.mapper.BannerMapper">
    <select id="getList" resultType="com.ybchen.shopmanager.model.BannerDO">
        select * from banner
    </select>
</mapper>
```

### BannerMapper.java添加方法

```text
package com.ybchen.shopmanager.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.ybchen.shopmanager.model.BannerDO;

import java.util.List;

/**
 * @Description：轮播图Mapper
 * @Author：chenyanbin
 * @Date：2021/3/4 下午11:03
 * @Versiion：1.0
 */
public interface BannerMapper extends BaseMapper<BannerDO> {
    List<BannerDO> getList();
}
```

### 配置文件告诉mapper.xml路径

application.properties

```text
# 默认配置路径
mybatis-plus.mapper-locations=classpath*:/mapper/*Mapper.xml
```

### 测试

![](./images/images/img_021_a48aa687f5b7.gif)

## 全局配置文件

- 注意config-location和configuration不能同时出现

### 修改配置文件

application.properties

```text
#配置全局配置文件！！！！
mybatis-plus.config-location = classpath:mybatis-config.xml
```

### 新建mybatis-config.xml

```text
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN" "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <settings>
        <!--控制台输出日志-->
        <setting name="logImpl" value="STDOUT_LOGGING"/>
    </settings>
</configuration>
```

### 测试

![](./images/images/img_022_9d531687e82c.gif)

### 配置实体类别名

修改application.properties

```text
# 配置实体类别名
mybatis-plus.type-aliases-package=com.ybchen.shopmanager.model
```

### 测试

![](./images/images/img_023_147a74b6a280.gif)

### mybatis plus下划线转驼峰

- 默认就是true

修改application.properties

```text
# mybatis plus下划线转驼峰
mybatis-plus.configuration.map-underscore-to-camel-case=true
```

### 配置全局默认主键类型

- 实体类上就不用加 @TableId(value="id",type=IdType.AUTO)

修改application.properties

```text
# 配置全局默认主键规则
mybatis-plus.global-config.db-config.id-type=auto
```

### 完整application.properties

```text
# 端口号
server.port=9999
#===========数据库相关=============
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1/shop?useUnicode=true&characterEncoding=utf-8&useSSL=false
spring.datasource.username=root
spring.datasource.password=root
# 配置mybatis plus打印sql日志
#mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
# 默认配置路径
mybatis-plus.mapper-locations=classpath*:/mapper/*Mapper.xml
#配置全局配置文件！！！！
mybatis-plus.config-location = classpath:mybatis-config.xml
# 配置实体类别名
mybatis-plus.type-aliases-package=com.ybchen.shopmanager.model
# mybatis plus下划线转驼峰
mybatis-plus.configuration.map-underscore-to-camel-case=true
# 配置全局默认主键规则
mybatis-plus.global-config.db-config.id-type=auto
```

## 乐观锁

　　大多是基于数据版本(Version)记录机制实现。即为数据增加一个版本标识，在基于数据库表的版本解决方案中，一般通过为数据库表增加一个“version”字段来实现。读取数据时，将此版本号一同读出，之后更新时，对此版本号加一。此时，将提交数据的版本数据与数据，库表对应记录的当前版本信息进行比较，如果提交的数据，版本号大于数据库表当前的版本号，则予以更新，否则认为是过期数据。

### 实体类增加@version

![](./images/images/img_024_fa57566e6fb0.png)

### 增加乐观锁插件

![](./images/images/img_025_06a66a5cba4c.png)

![](./images/images/img_015_8f900a89c634.gif)
![](./images/images/img_016_961ddebeb323.gif)

```text
package com.ybchen.shopmanager.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.OptimisticLockerInnerInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @Description：分页插件配置
 * @Author：chenyanbin
 * @Date：2021/3/5 下午10:32
 * @Versiion：1.0
 */
@Configuration
public class MybatisPlusPageConfig {

    /**
     * 旧版本
     */
//    @Bean
//    public PaginationInterceptor paginationInterceptor() {
//        PaginationInterceptor paginationInterceptor = new PaginationInterceptor();
//        return paginationInterceptor;
//    }

    /**
     * 新的分页插件，一级和二级缓存遵循mybatis的规则
     * 需要设置 MybatisConfiguration#useDeprecatedExecutor=false 避免缓存出现问题
     */
    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        MybatisPlusInterceptor mybatisPlusInterceptor = new MybatisPlusInterceptor();
        //分页插件
        mybatisPlusInterceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
        //乐观锁插件
        mybatisPlusInterceptor.addInnerInterceptor(new OptimisticLockerInnerInterceptor());
        return mybatisPlusInterceptor;
    }
}
```

MybatisPlusPageConfig.java

### 使用

![](./images/images/img_026_998e866fef5a.png)

![](./images/images/img_027_e3e0f1a2d350.png)

#### 注意

- 乐观锁数据类型支持int、Integer、long、timestamp
- 仅支持updateById和update方法

## 逻辑删除

　　公司在设计规范中都加入了逻辑删除的强制规定，运营人员可以分析和审查数据，也方便将数据沉淀下来用于商业分析。

　　数据量过多，也会采用数据仓库，通过监听应用数据库的数据变化，进行迁移到数据仓库。

### 方式一

- 数据库增加deleted字段，0是未删除，1表示删除
- 实体类增加属性配置@TableLogic
- 查询的时候会自动拼接上deleted=0的检索条件

![](./images/images/img_028_b73494b78415.png)

![](./images/images/img_029_45e8c3e59018.png)

![](./images/images/img_030_c493e02df21b.png)

### 方式二

修改application.properties

![](./images/images/img_031_6923f79565a8.png)

```text
# 逻辑删除，删除是1
mybatis-plus.global-config.db-config.logic-delete-value=1
# 逻辑删除，未删除是0
mybatis-plus.global-config.db-config.logic-not-delete-value=0
# 如果java实体类没加注解@TableLogic，则可以配置这个，推荐这里配置
mybatis-plus.global-config.db-config.logic-delete-field=deleted
```

## 代码生成器

### 添加依赖

```text
        <!-- 代码自动生成依赖 begin -->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-generator</artifactId>
            <version>3.4.1</version>
        </dependency>
        <!-- velocity -->
        <dependency>
            <groupId>org.apache.velocity</groupId>
            <artifactId>velocity-engine-core</artifactId>
            <version>2.0</version>
        </dependency>
        <!-- 代码自动生成依赖 end-->
```

### 生成器类

```text
package com.ybchen.shopmanager;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.generator.AutoGenerator;
import com.baomidou.mybatisplus.generator.config.DataSourceConfig;
import com.baomidou.mybatisplus.generator.config.GlobalConfig;
import com.baomidou.mybatisplus.generator.config.PackageConfig;
import com.baomidou.mybatisplus.generator.config.StrategyConfig;
import com.baomidou.mybatisplus.generator.config.rules.DateType;
import com.baomidou.mybatisplus.generator.config.rules.NamingStrategy;

/**
 * @Description：代码生成器
 * @Author：chenyanbin
 * @Date：2021/3/6 下午5:10
 * @Versiion：1.0
 */
public class MyBatisPlusGenerator {
    public static void main(String[] args) {
        //1. 全局配置
        GlobalConfig config = new GlobalConfig();
        // 是否支持AR模式
        config.setActiveRecord(true)
                // 作者
                .setAuthor("chenyanbin")
                // 生成路径，最好使用绝对路径，window路径是不一样的
                .setOutputDir("/Users/chenyanbin/IdeaProjects/shop-manager")
                // 文件覆盖
                .setFileOverride(true)
                // 主键策略
                .setIdType(IdType.AUTO)

                .setDateType(DateType.ONLY_DATE)
                // 设置生成的service接口的名字的首字母是否为I，默认Service是以I开头的
                .setServiceName("%sService")

                //实体类结尾名称
                .setEntityName("%sDO")

                //生成基本的resultMap
                .setBaseResultMap(true)

                //不使用AR模式
                .setActiveRecord(false)

                //生成基本的SQL片段
                .setBaseColumnList(true);

        //2. 数据源配置
        DataSourceConfig dsConfig = new DataSourceConfig();
        // 设置数据库类型
        dsConfig.setDbType(DbType.MYSQL)
                .setDriverName("com.mysql.cj.jdbc.Driver")
                .setUrl("jdbc:mysql://127.0.0.1:3306/shop?useSSL=false")
                .setUsername("root")
                .setPassword("root");

        //3. 策略配置globalConfiguration中
        StrategyConfig stConfig = new StrategyConfig();

        //全局大写命名
        stConfig.setCapitalMode(true)
                // 数据库表映射到实体的命名策略
                .setNaming(NamingStrategy.underline_to_camel)

                //使用lombok
                .setEntityLombokModel(true)

                //使用restcontroller注解
                .setRestControllerStyle(true)

                // 生成的表, 支持多表一起生成，以数组形式填写
                .setInclude("product","banner","address","coupon","product_order");

        //4. 包名策略配置
        PackageConfig pkConfig = new PackageConfig();
        pkConfig.setParent("net.mybatisplus")
                .setMapper("mapper")
                .setService("service")
                .setController("controller")
                .setEntity("model")
                .setXml("mapper");

        //5. 整合配置
        AutoGenerator ag = new AutoGenerator();
        ag.setGlobalConfig(config)
                .setDataSource(dsConfig)
                .setStrategy(stConfig)
                .setPackageInfo(pkConfig);

        //6. 执行操作
        ag.execute();
        System.out.println("======= 代码生成完毕  ========");
    }
}
```

### 使用

![](./images/images/img_032_d47e3f253e37.gif)

# SpringBoot整合Swagger 3.x

## 添加依赖

```text
        <!--springBoot整合swagger3.0-->
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-boot-starter</artifactId>
            <version>3.0.0</version>
        </dependency>
```

## 修改application.properties

添加如下信息

```text
spring.application.name=shop-manager
# ===== 自定义swagger配置 ===== #
swagger.enable=true
swagger.application-name= ${spring.application.name}
swagger.application-version=1.0
swagger.application-description=shop api
```

## 配置类

```text
package com.ybchen.shopmanager.config;

import io.swagger.annotations.ApiOperation;
import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.oas.annotations.EnableOpenApi;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;

/**
 * @Description：swagger配置类
 * @Author：chenyanbin
 * @Date：2021/3/5 下午10:32
 * @Versiion：1.0
 */
@Component
@Data
@ConfigurationProperties("swagger")
@EnableOpenApi
public class SwaggerConfiguration {

    /**
     * 是否开启swagger，生产环境一般关闭，所以这里定义一个变量
     */
    private Boolean enable;

    /**
     * 项目应用名
     */
    private String applicationName;

    /**
     * 项目版本信息
     */
    private String applicationVersion;

    /**
     * 项目描述信息
     */
    private String applicationDescription;

    @Bean
    public Docket docket(){

        return new Docket(DocumentationType.OAS_30)
                .pathMapping("/")
                // 定义是否开启swagger，false为关闭，可以通过变量控制，线上关闭
                .enable(enable)
                //配置api文档元信息
                .apiInfo(apiInfo())
                // 选择哪些接口作为swagger的doc发布
                .select()
                //apis() 控制哪些接口暴露给swagger，
                // RequestHandlerSelectors.any() 所有都暴露
                // RequestHandlerSelectors.basePackage("net.ybchen.*")  指定包位置
                // withMethodAnnotation(ApiOperation.class)标记有这个注解 ApiOperation
                .apis(RequestHandlerSelectors.withMethodAnnotation(ApiOperation.class))
                .paths(PathSelectors.any())
                .build();

    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title(applicationName)
                .description(applicationDescription)
                .contact(new Contact("陈彦斌", "https://www.cnblogs.com/chenyanbin/", "543210188@qq.com"))
                .version(applicationVersion)
                .build();
    }

}
```

## 启动测试

　　访问地址：http://localhost:9999/swagger-ui/index.html

　　注意：如果访问不成功，看是否拦截器拦截了相关资源！！！！！

![](./images/images/img_033_0a62745dfea5.gif)

## 常用注解

### @Api

- 用在controller类，描述API接口

```text
 @Api(tags = "用户模块",value = "用户UserController")
    public class UserController {
    }
```

### @ApiOperation

- 接口配置，用在方法上，描述接口方法

```text
@ApiOperation("分页用户列表")
    @GetMapping("list")
    public JsonData list(){
​
        return JsonData.buildSuccess();
    }
```

### @ApiParam

- 方法参数配置，用在入参上面，描述参数

```text
    @ApiOperation("用户登录")
    @PostMapping("login")
    public JsonData login(
            @ApiParam(name = "phone", value = "手机号",example = "13888888888")
            @RequestParam("phone") String phone,
​
            @ApiParam(name = "pwd", value = "密码",example = "123456")
            @RequestParam("pwd")String pwd){
​
        return JsonData.buildSuccess();
    }
```

### @Apilgnore

- 忽略此接口不生成文档

```text
@ApiIgnore
    @ApiOperation("删除用户")
    @DeleteMapping("/delete/{id}")
    public JsonData  deleteById(@PathVariable int id) {
        return JsonData.buildSuccess();
    }
```

### @ApiModel

- 用于类，表示对类进行说明，用于参数，用实体类接收

### @ApiModelProperty

- 用于方法，字段；表示对model属性的说明或者数据操作更改
- value：字段说明
- name：重写属性名称
- dataType：重写属性类型
- required：是否必填
- example：举例说明
- hidden：隐藏

```text
@Data
@ApiModel("用户基本信息")
public class SaveUserRequest {
​
    private int age;
​
    private String pwd;
​
    @ApiModelProperty(value ="【必填】邮箱",required = true)
    private String email;
​
    @ApiModelProperty("【必填】手机号")
    private String phone;
​
    @ApiModelProperty(value="创建时间")
    private Date createTime;
​
}
```

### @ApiResponse

- 描述接口响应

```text
@ApiOperation("用户登录")
    @PostMapping("login")
    @ApiResponses({
            @ApiResponse(responseCode = CodeStatus.SUCCESS, description = "保存成功"),
            @ApiResponse(responseCode = CodeStatus.FAIL, description = "保存失败")
    })
    public JsonData login(
            @ApiParam(name = "phone", value = "手机号",example = "13888888888")
            @RequestParam("phone") String phone,
​
            @ApiParam(name = "pwd", value = "密码",example = "123456")
            @RequestParam("pwd")String pwd){
​
        return JsonData.buildSuccess();
    }
```

# 项目源码下载

```text
链接: https://pan.baidu.com/s/1w9i5T8lqURG4vkVTdlhvdA  密码: ur4q
```

# swagger高级用法

[点我直达](https://www.cnblogs.com/chenyanbin/p/14748465.html)
