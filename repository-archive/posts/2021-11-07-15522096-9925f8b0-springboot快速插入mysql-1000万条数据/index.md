{

  "title": "SpringBoot快速插入Mysql 1000万条数据",
  "date": "2021-11-07",
  "description": "导读 有时候为了验证系统瓶颈，需要往数据库表中插入大量数据，可以写sheel脚本插入，前几天为了插入100万条数据，走的sheel脚本(点我直达)，插入速度简直无法直视，花了3小时，才插入了10万条，后来没辙了，多跑几次sheel脚本(算是多线程操作吧)，最终花了4个多小时才插入100万条记录。今天",
  "tags": [
    "Spring Boot",
    "Spring",
    "MySQL"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/15522096.html"

}

# 导读

　　有时候为了验证系统瓶颈，需要往数据库表中插入大量数据，可以写sheel脚本插入，前几天为了插入100万条数据，走的sheel脚本([点我直达](https://www.cnblogs.com/chenyanbin/p/15497305.html))，插入速度简直无法直视，花了3小时，才插入了10万条，后来没辙了，多跑几次sheel脚本(算是多线程操作吧)，最终花了4个多小时才插入100万条记录。今天使用java程序快速插入1000万条数据，最终只需要3分钟多一点就搞定了，好了下面开始吧~

# 添加依赖

```text
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.16</version>
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
        <!--Druid连接池-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid-spring-boot-starter</artifactId>
            <version>1.1.10</version>
        </dependency>
        <!-- guava -->
        <dependency>
            <groupId>com.google.guava</groupId>
            <artifactId>guava</artifactId>
            <version>31.0.1-jre</version>
        </dependency>
```

# application.properties

```text
# 端口号
server.port=9999
#===========数据库相关=============
#spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
#spring.datasource.url=jdbc:mysql://127.0.0.1/shop?useUnicode=true&characterEncoding=utf-8&useSSL=false
#spring.datasource.username=root
#spring.datasource.password=root
# mybatis plus下划线转驼峰
mybatis-plus.configuration.map-underscore-to-camel-case=true
# 配置mybatis plus打印sql日志
#mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
spring.datasource.name=mysql_test
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
# druid配置
# 监控统计拦截的filters
spring.datasource.druid.filters=stat
spring.datasource.druid.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.druid.url=jdbc:mysql://127.0.0.1/yb_mysql?useUnicode=true&characterEncoding=utf-8&useSSL=false
spring.datasource.druid.username=root
spring.datasource.druid.password=root
#配置初始化大小/最小/最大
spring.datasource.druid.initial-size=1
spring.datasource.druid.min-idle=1
spring.datasource.druid.max-active=20
#获取连接等待超时时间
spring.datasource.druid.max-wait=60000
#间隔多久进行一次检测，检测需要关闭的空闲连接
spring.datasource.druid.min-evictable-idle-time-millis=300000
spring.datasource.druid.validation-query= SELECT 'x'
spring.datasource.druid.test-while-idle=true
spring.datasource.druid.test-on-borrow=true
spring.datasource.druid.test-on-return=false
```

# 数据库表结构

![](./images/images/img_001_6b8df0aaa171.png)

# 实体类

```text
package com.ybchen.domain;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import lombok.EqualsAndHashCode;

import java.io.Serializable;

/**
 * <p>
 * 用户表
 * </p>
 *
 * @author chenyanbin
 * @since 2021-11-07
 */
@Data
@EqualsAndHashCode(callSuper = false)
@TableName("user")
public class UserDO implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 主键
     */
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    /**
     * 姓名
     */
    private String name;

    /**
     * 备注
     */
    private String remark;

}
```

# Mapper

```text
package com.ybchen.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.ybchen.domain.UserDO;
import org.apache.ibatis.annotations.Param;

import java.util.List;

public interface UserMapper extends BaseMapper<UserDO> {
    /**
     * 批量插入
     * @param userList
     * @return
     */
    int batchInsert(@Param("listUser") List<UserDO> userList);
}
```

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.ybchen.mapper.UserMapper">

    <!-- 通用查询映射结果 -->
    <resultMap id="BaseResultMap" type="com.ybchen.domain.UserDO">
        <id column="id" property="id"/>
        <result column="name" property="name"/>
        <result column="remark" property="remark"/>
    </resultMap>

    <!-- 通用查询结果列 -->
    <sql id="Base_Column_List">
        id, name, remark
    </sql>

    <!-- 批量插入 -->
    <insert id="batchInsert">
        insert into user (`name`,`remark`)
        values
        <foreach collection="listUser" item="item" separator=",">
            (#{item.name},#{item.remark})
        </foreach>
    </insert>
</mapper>
```

# Controller

```text
package com.ybchen.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.google.common.collect.Lists;
import com.ybchen.domain.UserDO;
import com.ybchen.mapper.UserMapper;
import com.ybchen.utils.JsonData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CountDownLatch;

/**
 * @Author：chenyanbin
 */
@RestController
public class UserController {
    @Autowired
    UserMapper userMapper;

    @GetMapping("batchInsert")
    public JsonData batchInsert() {
        int num = 2000;
        CountDownLatch latch = new CountDownLatch(1);
        List<UserDO> userList = new ArrayList<>();
        new Thread(() -> {
            for (int i = 0; i < 10000000; i++) {
                UserDO userDO = new UserDO();
                userDO.setName("陈彦斌====》" + i);
                userDO.setRemark("博客地址：https://www.cnblogs.com/chenyanbin/");
                userList.add(userDO);
            }
            latch.countDown();
        }).start();
        try {
            latch.await();
        } catch (InterruptedException e) {
        }
        //2000条为一批，插入1000万条
        List<List<UserDO>> partition = Lists.partition(userList, num);
        partition.stream().forEach(user -> {
            int rows = userMapper.batchInsert(user);
            System.err.println("插入数据成功，rows:" + rows);
        });
        return JsonData.buildSuccess();
    }

    @GetMapping("all")
    public JsonData all(){
        return JsonData.buildSuccess(userMapper.selectList(new LambdaQueryWrapper<>()));
    }
}
```

# 项目结构

![](./images/images/img_002_74dfa99a5282.png)

# 演示

![](./images/images/img_003_974e2dca1c8e.gif)

## 最终耗时

![](./images/images/img_004_1f22aee592b6.png)

![](./images/images/img_005_af1683bc27cf.png)

# 存储过程方式

```text
delimiter ;;
create procedure chenyanbin()
begin
  declare i int;
  set i=1;
  while(i<=3000000)do
    insert into test_excel (name1,name2,name3,name4,name5,name6,name7,name8,name9,name10,name11,name12,name13,name14,name15)
     values(concat('列1-：',i), concat('列2-：',i), concat('列3-：',i), concat('列4-：',i), concat('列5-：',i), concat('列6-：',i), concat('列7-：',i), concat('列8-：',i), concat('列9-：',i), concat('列10-：',i), concat('列11-：',i), concat('列12-：',i), concat('列13-：',i), concat('列14-：',i), concat('列15-：',i));
    set i=i+1;
  end while;
end;;
delimiter ;
call chenyanbin();
```
