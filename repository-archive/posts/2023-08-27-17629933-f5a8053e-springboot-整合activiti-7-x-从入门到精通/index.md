{

  "title": "SpringBoot 整合Activiti 7.X 从入门到精通",
  "date": "2023-08-27",
  "description": "简介 Activiti 是一个轻量级工作流程和业务流程管理 (BPM) 平台，面向业务人员、开发人员和系统管理员。其核心是一个超快且坚如磐石的 Java BPMN 2 流程引擎。它是开源的，并根据 Apache 许可证分发。Activiti 可以在任何 Java 应用程序、服务器、集群或云中运行。它",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/activiti.html"

}

# 简介

　　Activiti 是一个轻量级工作流程和业务流程管理 (BPM) 平台，面向业务人员、开发人员和系统管理员。其核心是一个超快且坚如磐石的 Java BPMN 2 流程引擎。它是开源的，并根据 Apache 许可证分发。Activiti 可以在任何 Java 应用程序、服务器、集群或云中运行。它与 Spring 完美集成，非常轻量级并且基于简单的概念。

# Idea 设计器

![](./images/images/img_001_f5e671fce02a.gif)

## 绘制一个简单流程图

![](./images/images/img_002_084dfba3751a.gif)

![](./images/images/img_003_f75bd433da02.png)

# SpringBoot整合Activiti 7.X

## 添加依赖

```text
<!-- Activiti 7.x依赖 -->
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-spring-boot-starter</artifactId>
            <version>7.0.0.GA</version>
            <!-- 由于activiti7是使用mybatis作为orm框架，我这里整合mybatis-plus，所以需要排除mybatis -->
            <exclusions>
                <exclusion>
                    <groupId>org.mybatis</groupId>
                    <artifactId>mybatis</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <!-- mysql 驱动 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
```

完整依赖

![](./images/images/img_004_8f900a89c634.gif)
![](./images/images/img_005_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.5</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.ybchen</groupId>
    <artifactId>ybchen-activiti7</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>ybchen-activiti7</name>
    <description>SpringBoot 整合Activiti 7.X</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
        </dependency>

        <!-- Activiti 7.x依赖 -->
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-spring-boot-starter</artifactId>
            <version>7.0.0.GA</version>
            <!-- 由于activiti7是使用mybatis作为orm框架，我这里整合mybatis-plus，所以需要排除mybatis -->
            <exclusions>
                <exclusion>
                    <groupId>org.mybatis</groupId>
                    <artifactId>mybatis</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <!-- mysql 驱动 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>

        <!-- MyBatis-Plus依赖包 -->
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
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```

pom.xml

## 配置类

```text
server.port=18080
# 数据库链接信息
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/activiti?useUnicode=true&characterEncoding=utf-8&useSSL=false&serverTimezone=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=rootroot

# 配置mybatis plus打印sql日志
mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl

# activiti配置
## 检测历史表是否存在 activiti7默认没有开启数据库历史记录 启动数据库历史记录
spring.activiti.db-history-used=true
# 记录历史等级 可配置的历史级别有none, activity, audit, full
## none：不保存任何的历史数据，因此，在流程执行过程中，这是最高效的。
## activity：级别高于none，保存流程实例与流程行为，其他数据不保存。
## audit：除activity级别会保存的数据外，还会保存全部的流程任务及其属性。audit为history的默认值。
## full：保存历史数据的最高级别，除了会保存audit级别的数据外，还会保存其他全部流程相关的细节数据，包括一些流程参数等
spring.activiti.history-level=full
## 1.false：默认值。activiti在启动时，对比数据库表中保存的版本，如果没有表或者版本不匹配，将抛出异常
## 2.true： activiti会对数据库中所有表进行更新操作。如果表不存在，则自动创建
## 3.create_drop： 在activiti启动时创建表，在关闭时删除表（必须手动关闭引擎，才能删除表）
## 4.drop-create： 在activiti启动时删除原来的旧表，然后在创建新表（不需要手动关闭引擎）
spring.activiti.database-schema-update=true
# 校验流程文件，默认校验resources下的processes文件夹里的流程文件
spring.activiti.check-process-definitions=false
```

![](./images/images/img_006_97c3493d7e8a.gif)

- 启动类

```text
package com.ybchen;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.actuate.autoconfigure.security.servlet.ManagementWebSecurityAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.security.servlet.SecurityAutoConfiguration;

@SpringBootApplication(exclude = {
        //activiti 默认整合security，屏蔽Security认证
        SecurityAutoConfiguration.class,
        ManagementWebSecurityAutoConfiguration.class
})
public class ActivitiApplication {

    public static void main(String[] args) {
        SpringApplication.run(ActivitiApplication.class, args);
    }

}
```

# Activiti表介绍

Activiti 的表都以 ACT_ 开头。

Activiti 使用到的表都是 ACT_ 开头的。表名的第二部分用两个字母表明表的用途。

- ACT_GE_ （GE） 表示 general 全局通用数据及设置，各种情况都使用的数据。
- ACT_HI_ （HI） 表示 history 历史数据表，包含着程执行的历史相关数据，如结束的流程实例，变量，任务，等等
- ACT_ID_ （ID） 表示 identity 组织机构，用户记录，流程中使用到的用户和组。这些表包含标识的信息，如用户，用户组，等等。
- ACT_RE_ （RE） 表示 repository 存储，包含的是静态信息，如，流程定义，流程的资源（图片，规则等）。
- ACT_RU_ （RU） 表示 runtime 运行时，运行时的流程变量，用户任务，变量，职责（job）等运行时的数据。Activiti 只存储实例执行期间的运行时数据，当流程实例结束时，将删除这些记录。这就保证了这些运行时的表小且快。

## 数据表介绍

<table class="ne-table"> <tbody> <tr> <td width="167">

表分类

</td> <td width="250">

表名

</td> <td width="561">

解释

</td> </tr> <tr> <td width="167">

一般数据

</td> <td width="250">

</td> <td width="561">

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_GE_BYTEARRAY]

</td> <td width="561">

二进制数据表，存储通用的流程定义和流程资源。

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_GE_PROPERTY]

</td> <td width="561">

系统相关属性，属性数据表存储整个流程引擎级别的数据，初始化表结构时，会默认插入三条记录。

</td> </tr> <tr> <td width="167">

流程历史记录

</td> <td width="250">

</td> <td width="561">

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_HI_ACTINST]

</td> <td width="561">

历史节点表

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_HI_ATTACHMENT]

</td> <td width="561">

历史附件表

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_HI_COMMENT]

</td> <td width="561">

历史的说明性信息

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_HI_DETAIL]

</td> <td width="561">

历史的流程运行中的细节信息

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_HI_IDENTITYLINK]

</td> <td width="561">

历史的流程运行过程中用户关系

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_HI_PROCINST]

</td> <td width="561">

历史的流程实例

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_HI_TASKINST]

</td> <td width="561">

历史的任务实例

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_HI_VARINST]

</td> <td width="561">

历史的流程运行中的变量信息

</td> </tr> <tr> <td width="167">

流程定义表

</td> <td width="250">

</td> <td width="561">

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RE_DEPLOYMENT]

</td> <td width="561">

部署单元信息

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RE_MODEL]

</td> <td width="561">

模型信息

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RE_PROCDEF]

</td> <td width="561">

已部署的流程定义

</td> </tr> <tr> <td width="167">

运行实例表

</td> <td width="250">

</td> <td width="561">

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RU_EVENT_SUBSCR]

</td> <td width="561">

运行时事件

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RU_EXECUTION]

</td> <td width="561">

运行时流程执行实例

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RU_IDENTITYLINK]

</td> <td width="561">

运行时用户关系信息，存储任务节点与参与者的相关信息

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RU_JOB]

</td> <td width="561">

运行时作业

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RU_TASK]

</td> <td width="561">

运行时任务

</td> </tr> <tr> <td width="167">

</td> <td width="250">

[ACT_RU_VARIABLE]

</td> <td width="561">

运行时变量表

</td> </tr> </tbody> </table>

### act_ge_bytearray

- 二进制数据表，存储通用的流程定义和流程资源

<table class="ne-table"> <tbody> <tr> <td width="153">

字段名称

</td> <td width="127">

字段描述

</td> <td width="124">

数据类型

</td> <td width="65">

主键

</td> <td width="65">

为空

</td> <td width="261">

取值说明

</td> </tr> <tr> <td width="153">

ID_

</td> <td width="127">

ID_

</td> <td width="124">

nvarchar(64)

</td> <td width="65">

Y

</td> <td width="65"> </td> <td width="261">

主键ID

</td> </tr> <tr> <td width="153">

REV_

</td> <td width="127">

乐观锁

</td> <td width="124">

int

</td> <td width="65"> </td> <td width="65">

Y

</td> <td width="261">

Version(版本)

</td> </tr> <tr> <td width="153">

NAME_

</td> <td width="127">

名称

</td> <td width="124">

nvarchar(255)

</td> <td width="65"> </td> <td width="65">

Y

</td> <td width="261">

部署的文件名称，如：leave.bpmn.png,leave.bpmn20.xml

</td> </tr> <tr> <td width="153">

DEPLOYMENT_ID_

</td> <td width="127">

部署ID

</td> <td width="124">

nvarchar(64)

</td> <td width="65"> </td> <td width="65">

Y

</td> <td width="261">

部署表ID

</td> </tr> <tr> <td width="153">

BYTES_

</td> <td width="127">

字节

</td> <td width="124">

varbinary(max)

</td> <td width="65"> </td> <td width="65">

Y

</td> <td width="261">

部署文件

</td> </tr> <tr> <td width="153">

GENERATED_

</td> <td width="127">

是否是引擎生成

</td> <td width="124">

tinyint

</td> <td width="65"> </td> <td width="65">

Y

</td> <td width="261">

0为用户生成，1为activiti生成

</td> </tr> </tbody> </table>

### act_ge_property

- 属性数据表：属性数据表。存储整个流程引擎级别的数据。

<table class="ne-table"> <tbody> <tr> <td width="83">

字段名称

</td> <td width="89">

字段描述

</td> <td width="125">

数据类型

</td> <td width="56">

主键

</td> <td width="69">

为空

</td> <td width="111">

取值说明

</td> </tr> <tr> <td width="83">

NAME_

</td> <td width="89">

名称

</td> <td width="125">

nvarchar(64)

</td> <td width="56">

√

</td> <td width="69"> </td> <td width="111"> </td> </tr> <tr> <td width="83">

VALUE_

</td> <td width="89">

值

</td> <td width="125">

nvarchar(300)

</td> <td width="56"> </td> <td width="69">

√

</td> <td width="111">

5.create(5.)

</td> </tr> <tr> <td width="83">

REV_

</td> <td width="89">

乐观锁

</td> <td width="125">

int

</td> <td width="56"> </td> <td width="69">

√

</td> <td width="111">

version

</td> </tr> </tbody> </table>

### act_hi_actinst

- 历史节点表：历史活动信息。这里记录流程流转过的所有节点，与HI_TASKINST不同的是，taskinst只记录usertask内容

<table id="VpQjA" class="ne-table"> <tbody> <tr> <td width="137">

字段名称

</td> <td width="137">

字段描述

</td> <td width="137">

数据类型

</td> <td width="67">

主键

</td> <td width="79">

为空

</td> <td width="232">

取值说明

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="67">

√

</td> <td width="79"> </td> <td width="232"> </td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137">

流程定义ID

</td> <td width="137">

nvarchar(64)

</td> <td width="67"> </td> <td width="79"> </td> <td width="232"> </td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="67"> </td> <td width="79"> </td> <td width="232"> </td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="67"> </td> <td width="79"> </td> <td width="232"> </td> </tr> <tr> <td width="137">

ACT_ID_

</td> <td width="137">

节点ID

</td> <td width="137">

nvarchar(225)

</td> <td width="67"> </td> <td width="79"> </td> <td width="232">

节点定义ID

</td> </tr> <tr> <td width="137">

TASK_ID_

</td> <td width="137">

任务实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="67"> </td> <td width="79">

√

</td> <td width="232">

任务实例ID 其他节点类型实例ID在这里为空

</td> </tr> <tr> <td width="137">

CALL_PROC_INST_ID_

</td> <td width="137">

调用外部的流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="67"> </td> <td width="79">

√

</td> <td width="232">

调用外部流程的流程实例ID’

</td> </tr> <tr> <td width="137">

ACT_NAME_

</td> <td width="137">

节点名称

</td> <td width="137">

nvarchar(225)

</td> <td width="67"> </td> <td width="79">

√

</td> <td width="232">

节点定义名称

</td> </tr> <tr> <td width="137">

ACT_TYPE_

</td> <td width="137">

节点类型

</td> <td width="137">

nvarchar(225)

</td> <td width="67"> </td> <td width="79"> </td> <td width="232">

如startEvent、userTask

</td> </tr> <tr> <td width="137">

ASSIGNEE_

</td> <td width="137">

签收人

</td> <td width="137">

nvarchar(64)

</td> <td width="67"> </td> <td width="79">

√

</td> <td width="232">

节点签收人

</td> </tr> <tr> <td width="137">

START_TIME_

</td> <td width="137">

开始时间

</td> <td width="137">

datetime

</td> <td width="67"> </td> <td width="79"> </td> <td width="232"> </td> </tr> <tr> <td width="137">

END_TIME_

</td> <td width="137">

结束时间

</td> <td width="137">

datetime

</td> <td width="67"> </td> <td width="79">

√

</td> <td width="232"> </td> </tr> <tr> <td width="137">

DURATION_

</td> <td width="137">

耗时

</td> <td width="137">

numeric(19,0)

</td> <td width="67"> </td> <td width="79">

√

</td> <td width="232">

毫秒值

</td> </tr> <tr> <td width="137">

DELETE_REASON_

</td> <td width="137"> </td> <td width="137">

nvarchar(4000)

</td> <td width="67"> </td> <td width="79"> </td> <td width="232"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

nvarchar(225)

</td> <td width="67"> </td> <td width="79"> </td> <td width="232"> </td> </tr> </tbody> </table>

### act_hi_attachment

- 历史附件表

<table class="ne-table"> <tbody> <tr> <td width="137">

字段名称

</td> <td width="137">

字段描述

</td> <td width="137">

数据类型

</td> <td width="137">

主键

</td> <td width="137">

为空

</td> <td width="138">

取值说明

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

主键ID

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

乐观锁

</td> <td width="137">

integer

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

Version

</td> </tr> <tr> <td width="137">

USER_ID_

</td> <td width="137">

用户ID

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

用户ID

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

名称

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

附件名称

</td> </tr> <tr> <td width="137">

DESCRIPTION_

</td> <td width="137">

描述

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

描述

</td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137">

类型

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

附件类型

</td> </tr> <tr> <td width="137">

TASK_ID_

</td> <td width="137">

任务实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

节点实例ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

URL_

</td> <td width="137">

URL_

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

附件地址

</td> </tr> <tr> <td width="137">

CONTENT_ID_

</td> <td width="137">

字节表的ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

ACT_GE_BYTEARRAY的ID

</td> </tr> <tr> <td width="137">

TIME_

</td> <td width="137"> </td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> </tbody> </table>

### act_hi_comment

- 历史意见表

<table class="ne-table"> <tbody> <tr> <td width="129">

字段名称

</td> <td width="106">

字段描述

</td> <td width="137">

数据类型

</td> <td width="64">

主键

</td> <td width="86">

为空

</td> <td width="274">

取值说明

</td> </tr> <tr> <td width="129">

ID_

</td> <td width="106">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="64">

√

</td> <td width="86"> </td> <td width="274">

主键ID

</td> </tr> <tr> <td width="129">

TYPE_

</td> <td width="106">

类型

</td> <td width="137">

nvarchar(255)

</td> <td width="64"> </td> <td width="86">

√

</td> <td width="274">

类型：event（事件）comment（意见）

</td> </tr> <tr> <td width="129">

TIME_

</td> <td width="106">

时间

</td> <td width="137">

datetime

</td> <td width="64"> </td> <td width="86"> </td> <td width="274">

填写时间’

</td> </tr> <tr> <td width="129">

USER_ID_

</td> <td width="106">

用户ID

</td> <td width="137">

nvarchar(64)

</td> <td width="64"> </td> <td width="86">

√

</td> <td width="274">

填写人

</td> </tr> <tr> <td width="129">

TASK_ID_

</td> <td width="106">

节点任务ID

</td> <td width="137">

nvarchar(64)

</td> <td width="64"> </td> <td width="86">

√

</td> <td width="274">

节点实例ID

</td> </tr> <tr> <td width="129">

PROC_INST_ID_

</td> <td width="106">

流程实例ID

</td> <td width="137">

nvarchar(255)

</td> <td width="64"> </td> <td width="86">

√

</td> <td width="274">

流程实例ID

</td> </tr> <tr> <td width="129">

ACTION_

</td> <td width="106">

行为类型

</td> <td width="137">

nvarchar(64)

</td> <td width="64"> </td> <td width="86">

√

</td> <td width="274">

见备注1

</td> </tr> <tr> <td width="129">

MESSAGE_

</td> <td width="106">

基本内容

</td> <td width="137">

nvarchar(4000)

</td> <td width="64"> </td> <td width="86">

√

</td> <td width="274">

用于存放流程产生的信息，比如审批意见

</td> </tr> <tr> <td width="129">

FULL_MSG_

</td> <td width="106">

全部内容

</td> <td width="137">

varbinary(max)

</td> <td width="64"> </td> <td width="86">

√

</td> <td width="274">

附件地址

</td> </tr> </tbody> </table>

### act_hi_detail 

- 历史详情表：流程中产生的变量详细，包括控制流程流转的变量，业务表单中填写的流程需要用到的变量等。

<table class="ne-table"> <tbody> <tr> <td width="137">

字段名称

</td> <td width="137">

字段描述

</td> <td width="137">

数据类型

</td> <td width="73">

主键

</td> <td width="70">

为空

</td> <td width="138">

取值说明

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="73">

√

</td> <td width="70"> </td> <td width="138">

主键

</td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137">

类型

</td> <td width="137">

nvarchar(255)

</td> <td width="73"> </td> <td width="70"> </td> <td width="138">

见备注2

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

执行实例ID

</td> </tr> <tr> <td width="137">

TASK_ID_

</td> <td width="137">

任务实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

任务实例ID

</td> </tr> <tr> <td width="137">

ACT_INST_ID_

</td> <td width="137">

节点实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

ACT_HI_ACTINST表的ID

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

名称

</td> <td width="137">

nvarchar(255)

</td> <td width="73"> </td> <td width="70"> </td> <td width="138">

名称

</td> </tr> <tr> <td width="137">

VAR_TYPE_

</td> <td width="137">

参数类型

</td> <td width="137">

nvarchar(255)

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

见备注3

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

乐观锁

</td> <td width="137">

int

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

Version

</td> </tr> <tr> <td width="137">

TIME_

</td> <td width="137">

时间戳

</td> <td width="137">

datetime

</td> <td width="73"> </td> <td width="70"> </td> <td width="138">

创建时间

</td> </tr> <tr> <td width="137">

BYTEARRAY_ID_

</td> <td width="137">

字节表ID

</td> <td width="137">

nvarchar

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

ACT_GE_BYTEARRAY表的ID

</td> </tr> <tr> <td width="137">

DOUBLE_

</td> <td width="137">

DOUBLE_

</td> <td width="137">

double precision

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

存储变量类型为Double

</td> </tr> <tr> <td width="137">

LONG_

</td> <td width="137">

LONG_

</td> <td width="137">

numeric

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

存储变量类型为long

</td> </tr> <tr> <td width="137">

TEXT_

</td> <td width="137">

TEXT_

</td> <td width="137">

nvarchar

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

存储变量值类型为String

</td> </tr> <tr> <td width="137">

TEXT2_

</td> <td width="137">

TEXT2_

</td> <td width="137">

nvarchar

</td> <td width="73"> </td> <td width="70">

√

</td> <td width="138">

此处存储的是JPA持久化对象时，才会有值。此值为对象ID

</td> </tr> </tbody> </table>

### act_ru_identitylink 

- 历史流程人员表：任务参与者数据表。主要存储历史节点参与者的信息

<table class="ne-table"> <tbody> <tr> <td width="137">

字段名称

</td> <td width="137">

字段描述

</td> <td width="137">

数据类型

</td> <td width="137">

主键

</td> <td width="137">

为空

</td> <td width="138">

取值说明

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

ID_

</td> </tr> <tr> <td width="137">

GROUP_ID_

</td> <td width="137">

组ID

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

组ID

</td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137">

类型

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

备注4

</td> </tr> <tr> <td width="137">

USER_ID_

</td> <td width="137">

用户ID

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

用户ID

</td> </tr> <tr> <td width="137">

TASK_ID_

</td> <td width="137">

节点实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

节点实例ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> </tbody> </table>

### act_hi_procinst

- 历史流程实例表

<table class="ne-table"> <tbody> <tr> <td width="137">

字段名称

</td> <td width="137">

字段描述

</td> <td width="137">

数据类型

</td> <td width="137">

主键

</td> <td width="137">

为空

</td> <td width="138">

取值说明

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

主键ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

BUSINESS_KEY_

</td> <td width="137">

业务主键

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

业务主键，业务表单的ID

</td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137">

流程定义ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

流程定义ID

</td> </tr> <tr> <td width="137">

START_TIME_

</td> <td width="137">

开始时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

开始时间

</td> </tr> <tr> <td width="137">

END_TIME_

</td> <td width="137">

结束时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

结束时间

</td> </tr> <tr> <td width="137">

DURATION_

</td> <td width="137">

耗时

</td> <td width="137">

Numeric(19)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

耗时

</td> </tr> <tr> <td width="137">

START_USER_ID_

</td> <td width="137">

起草人

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

起草人

</td> </tr> <tr> <td width="137">

START_ACT_ID_

</td> <td width="137">

开始节点ID

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

起草环节ID

</td> </tr> <tr> <td width="137">

END_ACT_ID_

</td> <td width="137">

结束节点ID

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

结束环节ID

</td> </tr> <tr> <td width="137">

SUPER_PROCESS_INSTANCE_ID_

</td> <td width="137">

父流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

父流程实例ID

</td> </tr> <tr> <td width="137">

DELETE_REASON_

</td> <td width="137">

删除原因

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

删除原因

</td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137"> </td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> </tbody> </table>

### act_hi_taskinst

- 历史任务实例表

<table class="ne-table"> <tbody> <tr> <td width="137">

字段名称

</td> <td width="137">

字段描述

</td> <td width="137">

数据类型

</td> <td width="137">

主键

</td> <td width="137">

为空

</td> <td width="138">

取值说明

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

主键ID

</td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137">

流程定义ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程定义ID

</td> </tr> <tr> <td width="137">

TASK_DEF_KEY_

</td> <td width="137">

节点定义ID

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

节点定义ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

执行实例ID

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

名称

</td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

名称

</td> </tr> <tr> <td width="137">

PARENT_TASK_ID_

</td> <td width="137">

父节点实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

父节点实例ID

</td> </tr> <tr> <td width="137">

DESCRIPTION_

</td> <td width="137">

描述

</td> <td width="137">

nvarchar(400)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

描述

</td> </tr> <tr> <td width="137">

OWNER_

</td> <td width="137">

实际签收人 任务的拥有者

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

签收人（默认为空，只有在委托时才有值）

</td> </tr> <tr> <td width="137">

ASSIGNEE_

</td> <td width="137">

签收人或被委托

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

签收人或被委托

</td> </tr> <tr> <td width="137">

START_TIME_

</td> <td width="137">

开始时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

开始时间

</td> </tr> <tr> <td width="137">

CLAIM_TIME_

</td> <td width="137">

提醒时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

提醒时间

</td> </tr> <tr> <td width="137">

END_TIME_

</td> <td width="137">

结束时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

结束时间

</td> </tr> <tr> <td width="137">

DURATION_

</td> <td width="137">

耗时

</td> <td width="137">

numeric(19)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

耗时

</td> </tr> <tr> <td width="137">

DELETE_REASON_

</td> <td width="137">

删除原因

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

删除原因(completed,deleted)

</td> </tr> <tr> <td width="137">

PRIORITY_

</td> <td width="137">

优先级别

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

优先级别

</td> </tr> <tr> <td width="137">

DUE_DATE_

</td> <td width="137">

过期时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

过期时间，表明任务应在多长时间内完成

</td> </tr> <tr> <td width="137">

FORM_KEY_

</td> <td width="137">

节点定义的formkey

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

desinger节点定义的form_key属性

</td> </tr> <tr> <td width="137">

CATEGORY_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> </tbody> </table>

### act_hi_varinst

- 历史变量表

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

ID_

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

执行实例ID

</td> </tr> <tr> <td width="137">

TASK_ID_

</td> <td width="137">

任务实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

任务实例ID

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

名称

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

参数名称(英文)

</td> </tr> <tr> <td width="137">

VAR_TYPE_

</td> <td width="137">

参数类型

</td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

备注5

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

乐观锁

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

乐观锁 Version

</td> </tr> <tr> <td width="137">

BYTEARRAY_ID_

</td> <td width="137">

字节表ID

</td> <td width="137">

nvarchar(400)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

ACT_GE_BYTEARRAY表的主键

</td> </tr> <tr> <td width="137">

DOUBLE_

</td> <td width="137">

DOUBLE_

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

存储DoubleType类型的数据

</td> </tr> <tr> <td width="137">

LONG_

</td> <td width="137">

LONG_

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

存储LongType类型的数据

</td> </tr> <tr> <td width="137">

TEXT_

</td> <td width="137">

TEXT_

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

备注6

</td> </tr> <tr> <td width="137">

TEXT2_

</td> <td width="137">

TEXT2_

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

此处存储的是JPA持久化对象时，才会有值。此值为对象ID

</td> </tr> <tr> <td width="137">

CREATE_TIME_

</td> <td width="137"> </td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

LAST_UPDATED_TIME_

</td> <td width="137"> </td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> </tbody> </table>

### act_re_deployment 

- 部署信息表：部署流程定义时需要被持久化保存下来的信息。

<table id="NpkY0" class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

主键ID

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

部署名称

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

部署文件名

</td> </tr> <tr> <td width="137">

CATEGORY_

</td> <td width="137">

分类

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

类别

</td> </tr> <tr> <td width="137">

KEY_

</td> <td width="137"> </td> <td width="137"> </td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137"> </td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

DEPLOY_TIME_

</td> <td width="137">

部署时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

部署时间

</td> </tr> <tr> <td width="137">

ENGINE_VERSION_

</td> <td width="137"> </td> <td width="137"> </td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> </tbody> </table>

### act_re_model

- 流程设计模型部署表：流程设计器设计流程后，保存数据到该表。

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

ID_

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

乐观锁

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

乐观锁

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

名称

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

名称

</td> </tr> <tr> <td width="137">

KEY_

</td> <td width="137">

KEY_

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

key

</td> </tr> <tr> <td width="137">

CATEGORY_

</td> <td width="137">

分类

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

分类

</td> </tr> <tr> <td width="137">

CREATE_TIME_

</td> <td width="137">

创建时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

创建时间

</td> </tr> <tr> <td width="137">

LAST_UPDATE_TIME_

</td> <td width="137">

最新修改时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

最新修改时间

</td> </tr> <tr> <td width="137">

VERSION_

</td> <td width="137">

版本

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

版本

</td> </tr> <tr> <td width="137">

META_INFO_

</td> <td width="137">

META_INFO_

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

以json格式保存流程定义的信息

</td> </tr> <tr> <td width="137">

DEPLOYMENT_ID_

</td> <td width="137">

部署ID

</td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

部署ID

</td> </tr> <tr> <td width="137">

EDITOR_SOURCE_VALUE_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EDITOR_SOURCE_EXTRA_VALUE_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> </tbody> </table>

### act_re_procdef 

- 流程定义数据表：业务流程定义数据表。此表和 ACT_RE_DEPLOYMENT 是多对一的关系，即，一个部署的bar包里可能包含多个流程定义文件，每个流程定义文件都会有一条记录在 ACT_REPROCDEF 表内，每个流程定义的数据，都会对于 ACT_GE_BYTEARRAY 表内的一个资源文件和 PNG 图片文件。和 ACT_GE_BYTEARRAY 的关联是通过程序用ACT_GE_BYTEARRAY.NAME 与 ACT_RE_PROCDEF.NAME 完成的，在数据库表结构中没有体现。

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

ID_

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

乐观锁

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

乐观锁

</td> </tr> <tr> <td width="137">

CATEGORY_

</td> <td width="137">

分类

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程定义的Namespace就是类别

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

名称

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

名称

</td> </tr> <tr> <td width="137">

KEY_

</td> <td width="137">

定义的KEY

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

流程定义ID

</td> </tr> <tr> <td width="137">

VERSION_

</td> <td width="137">

版本

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

版本

</td> </tr> <tr> <td width="137">

DEPLOYMENT_ID_

</td> <td width="137">

部署表ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

部署表ID

</td> </tr> <tr> <td width="137">

RESOURCE_NAME_

</td> <td width="137">

bpmn文件名称

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程bpmn文件名称

</td> </tr> <tr> <td width="137">

DGRM_RESOURCE_NAME_

</td> <td width="137">

png图片名称

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程图片名称

</td> </tr> <tr> <td width="137">

DESCRIPTION_

</td> <td width="137">

描述

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

描述

</td> </tr> <tr> <td width="137">

HAS_START_FORM_KEY

</td> <td width="137">

是否存在开始节点formKey

</td> <td width="137">

tinyint

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

start节点是否存在formKey 0否 1是

</td> </tr> <tr> <td width="137">

SUSPENSION_STATE_

</td> <td width="137">

是否挂起

</td> <td width="137">

tinyint

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

1 激活 2挂起

</td> </tr> <tr> <td width="137">

HAS_GRAPHICAL_NOTATION_

</td> <td width="137"> </td> <td width="137">

tinyint

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

ENGINE_VERSION_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_deadletter_job

<table id="nJFAR" class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

varchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

ID_

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137"> </td> <td width="137">

int

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCLUSIVE_

</td> <td width="137"> </td> <td width="137">

tinyint(1)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

PROCESS_INSTANCE_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCEPTION_STACK_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCEPTION_MSG_

</td> <td width="137"> </td> <td width="137">

varchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

DUEDATE_

</td> <td width="137"> </td> <td width="137">

timestamp

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

REPEAT_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

HANDLER_TYPE_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

HANDLER_CFG_

</td> <td width="137"> </td> <td width="137">

varchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_event_subscr

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

事件ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

事件ID

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

版本

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

乐观锁Version

</td> </tr> <tr> <td width="137">

EVENT_TYPE_

</td> <td width="137">

事件类型

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

事件类型

</td> </tr> <tr> <td width="137">

EVENT_NAME_

</td> <td width="137">

事件名称

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

事件名称

</td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

执行实例ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

ACTIVITY_ID_

</td> <td width="137">

活动实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

活动实例ID

</td> </tr> <tr> <td width="137">

CONFIGURATION_

</td> <td width="137">

配置

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

配置

</td> </tr> <tr> <td width="137">

CREATED_

</td> <td width="137">

是否创建

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

默认值 当前系统时间戳CURRENT_TIMESTAMP

</td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_execution

- 运行时流程执行实例表

<table id="C5AFR" class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

事件ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

事件ID

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

版本

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

乐观锁Version

</td> </tr> <tr> <td width="137">

EVENT_TYPE_

</td> <td width="137">

事件类型

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

事件类型

</td> </tr> <tr> <td width="137">

EVENT_NAME_

</td> <td width="137">

事件名称

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

事件名称

</td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

执行实例ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

ACTIVITY_ID_

</td> <td width="137">

活动实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

活动实例ID

</td> </tr> <tr> <td width="137">

CONFIGURATION_

</td> <td width="137">

配置

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

配置

</td> </tr> <tr> <td width="137">

CREATED_

</td> <td width="137">

是否创建

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

默认值 当前系统时间戳CURRENT_TIMESTAMP

</td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_identitylink

- 运行时流程人员表：任务参与者数据表。主要存储当前节点参与者的信息。

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

ID_

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

乐观锁

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

乐观锁

</td> </tr> <tr> <td width="137">

GROUP_ID_

</td> <td width="137">

组ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

组ID

</td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137">

类型

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

备注7

</td> </tr> <tr> <td width="137">

USER_ID_

</td> <td width="137">

用户ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

用户ID

</td> </tr> <tr> <td width="137">

TASK_ID_

</td> <td width="137">

节点实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

节点实例ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137">

流程定义ID

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程定义ID

</td> </tr> </tbody> </table>

### act_ru_integration

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

PROCESS_INSTANCE_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

FLOW_NODE_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

CREATED_DATE_

</td> <td width="137"> </td> <td width="137">

timestamp

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_job

- 运行时定时任务数据表( act_ru_job )

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

标识

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

标识

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

版本

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

版本

</td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137">

类型

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

类型

</td> </tr> <tr> <td width="137">

LOCK_EXP_TIME_

</td> <td width="137">

锁定释放时间

</td> <td width="137">

锁定释放时间

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

锁定释放时间

</td> </tr> <tr> <td width="137">

LOCK_OWNER_

</td> <td width="137">

挂起者

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

挂起者

</td> </tr> <tr> <td width="137">

EXCLUSIVE_

</td> <td width="137"> </td> <td width="137">

bit

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

执行实例ID

</td> </tr> <tr> <td width="137">

PROCESS_INSTANCE_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137">

流程定义ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程定义ID

</td> </tr> <tr> <td width="137">

RETRIES_

</td> <td width="137"> </td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCEPTION_STACK_ID_

</td> <td width="137">

异常信息ID

</td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

异常信息ID

</td> </tr> <tr> <td width="137">

EXCEPTION_MSG_

</td> <td width="137">

异常信息

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

异常信息

</td> </tr> <tr> <td width="137">

DUEDATE_

</td> <td width="137">

到期时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

到期时间

</td> </tr> <tr> <td width="137">

REPEAT_

</td> <td width="137">

重复

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

重复

</td> </tr> <tr> <td width="137">

HANDLER_TYPE_

</td> <td width="137">

处理类型

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

处理类型

</td> </tr> <tr> <td width="137">

HANDLER_CFG_

</td> <td width="137"> </td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

标识

</td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_suspended_job

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

REV_

</td> <td width="137"> </td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCLUSIVE_

</td> <td width="137"> </td> <td width="137">

tinyint(1)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

PROCESS_INSTANCE_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

RETRIES_

</td> <td width="137"> </td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCEPTION_STACK_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCEPTION_MSG_

</td> <td width="137"> </td> <td width="137">

varchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

DUEDATE_

</td> <td width="137"> </td> <td width="137">

timestamp

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

REPEAT_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

HANDLER_TYPE_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

HANDLER_CFG_

</td> <td width="137"> </td> <td width="137">

varchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_task 

- 运行时任务节点表

<table class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

ID_

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

乐观锁

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

乐观锁

</td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

执行实例ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137">

流程定义ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程定义ID

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

节点定义名称

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

节点定义名称

</td> </tr> <tr> <td width="137">

PARENT_TASK_ID_

</td> <td width="137">

父节点实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

父节点实例ID

</td> </tr> <tr> <td width="137">

DESCRIPTION_

</td> <td width="137">

节点定义描述

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

节点定义描述

</td> </tr> <tr> <td width="137">

TASK_DEF_KEY_

</td> <td width="137">

节点定义的KEY

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

任务定义的ID

</td> </tr> <tr> <td width="137">

OWNER_

</td> <td width="137">

实际签收人

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

拥有者（一般情况下为空，只有在委托时才有值）

</td> </tr> <tr> <td width="137">

ASSIGNEE_

</td> <td width="137">

签收人或委托人

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

签收人或委托人

</td> </tr> <tr> <td width="137">

DELEGATION_

</td> <td width="137">

委托类型

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

备注8

</td> </tr> <tr> <td width="137">

PRIORITY_

</td> <td width="137">

优先级别

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

优先级别，默认为：50

</td> </tr> <tr> <td width="137">

CREATE_TIME_

</td> <td width="137">

创建时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

创建时间

</td> </tr> <tr> <td width="137">

DUE_DATE_

</td> <td width="137">

过期时间

</td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

耗时

</td> </tr> <tr> <td width="137">

CATEGORY_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

SUSPENSION_STATE_

</td> <td width="137">

是否挂起

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

1代表激活 2代表挂起

</td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> <tr> <td width="137">

FORM_KEY_

</td> <td width="137">

节点表单KEY

</td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

节点表单key

</td> </tr> <tr> <td width="137">

CLAIM_TIME_

</td> <td width="137"> </td> <td width="137">

datetime

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_timer_job

<table id="W2Ueh" class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

REV_

</td> <td width="137"> </td> <td width="137">

int

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

LOCK_EXP_TIME_

</td> <td width="137"> </td> <td width="137">

timestamp

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

LOCK_OWNER_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCLUSIVE_

</td> <td width="137"> </td> <td width="137">

tinyint(1)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

PROCESS_INSTANCE_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

PROC_DEF_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

RETRIES_

</td> <td width="137"> </td> <td width="137">

int

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCEPTION_STACK_ID_

</td> <td width="137"> </td> <td width="137">

varchar(64)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

EXCEPTION_MSG_

</td> <td width="137"> </td> <td width="137">

varchar(4000)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

DUEDATE_

</td> <td width="137"> </td> <td width="137">

timestamp

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

REPEAT_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

HANDLER_TYPE_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

HANDLER_CFG_

</td> <td width="137"> </td> <td width="137">

varchar(4000)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> <tr> <td width="137">

TENANT_ID_

</td> <td width="137"> </td> <td width="137">

varchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138"> </td> </tr> </tbody> </table>

### act_ru_variable 

- 运行时流程变量数据表

<table id="Jfn8J" class="ne-table"> <tbody> <tr> <td width="137">

**字段名称**

</td> <td width="137">

**字段描述**

</td> <td width="137">

**数据类型**

</td> <td width="137">

**主键**

</td> <td width="137">

**为空**

</td> <td width="138">

**取值说明**

</td> </tr> <tr> <td width="137">

ID_

</td> <td width="137">

ID_

</td> <td width="137">

nvarchar(64)

</td> <td width="137">

√

</td> <td width="137"> </td> <td width="138">

主键标识

</td> </tr> <tr> <td width="137">

REV_

</td> <td width="137">

乐观锁

</td> <td width="137">

int

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

乐观锁

</td> </tr> <tr> <td width="137">

TYPE_

</td> <td width="137">

类型

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

备注9

</td> </tr> <tr> <td width="137">

NAME_

</td> <td width="137">

名称

</td> <td width="137">

nvarchar(255)

</td> <td width="137"> </td> <td width="137"> </td> <td width="138">

变量名称

</td> </tr> <tr> <td width="137">

EXECUTION_ID_

</td> <td width="137">

执行实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

执行的ID

</td> </tr> <tr> <td width="137">

PROC_INST_ID_

</td> <td width="137">

流程实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

流程实例ID

</td> </tr> <tr> <td width="137">

TASK_ID_

</td> <td width="137">

节点实例ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

节点实例ID(Local）

</td> </tr> <tr> <td width="137">

BYTEARRAY_ID_

</td> <td width="137">

字节表ID

</td> <td width="137">

nvarchar(64)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

字节表的ID（ACT_GE_BYTEARRAY）

</td> </tr> <tr> <td width="137">

DOUBLE_

</td> <td width="137">

DOUBLE_

</td> <td width="137">

float

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

存储变量类型为Double

</td> </tr> <tr> <td width="137">

LONG_

</td> <td width="137">

LONG_

</td> <td width="137">

numeric(19)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

存储变量类型为long

</td> </tr> <tr> <td width="137">

TEXT_

</td> <td width="137">

TEXT_

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

‘存储变量值类型为String 如此处存储持久化对象时，值jpa对象的class

</td> </tr> <tr> <td width="137">

TEXT2_

</td> <td width="137">

TEXT2_

</td> <td width="137">

nvarchar(4000)

</td> <td width="137"> </td> <td width="137">

√

</td> <td width="138">

此处存储的是JPA持久化对象时，才会有值。此值为对象ID

</td> </tr> </tbody> </table>

# 通过zip部署流程

```text
    //提供对流程定义和部署存储库的访问服务
    @Autowired
    RepositoryService repositoryService;

    /**
     * 部署流程
     * <p>
     * 1、设计器设计流程xml/png
     * 2、部署流程
     * 3、发起流程
     * 4、执行流程
     *
     * @param file 上传流程压缩包
     */
    @ApiOperation("zip部署流程")
    @PostMapping("deploy")
    public ReturnData deploy(@RequestPart("file") MultipartFile file){
        try {
            if (file.isEmpty()) {
                throw new NullPointerException("部署压缩包不能为空");
            }
            DeploymentBuilder deploymentBuilder = repositoryService.createDeployment();
            //压缩流
            ZipInputStream zip = new ZipInputStream(file.getInputStream());
            deploymentBuilder.addZipInputStream(zip);
            //设置部署流程名称
            deploymentBuilder.name("请假审批");
            //部署流程
            Deployment deploy = deploymentBuilder.deploy();
            return ReturnData.buildSuccess(deploy);

        }catch (Exception e){
            e.printStackTrace();
            return ReturnData.buildError(e.toString());
        }
    }
```

## 画流程图&保存png图片

![](./images/images/img_007_0f3bd05a953e.gif)

## 压缩zip&部署流程

![](./images/images/img_008_f06be696f0fd.gif)

```text
2023-08-20 19:10:39.112  INFO 39701 --- [           main] trationDelegate$BeanPostProcessorChecker : Bean 'org.springframework.security.access.expression.method.DefaultMethodSecurityExpressionHandler@17e8caf2' of type [org.springframework.security.access.expression.method.DefaultMethodSecurityExpressionHandler] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
2023-08-20 19:10:39.115  INFO 39701 --- [           main] trationDelegate$BeanPostProcessorChecker : Bean 'methodSecurityConfig' of type [org.activiti.spring.boot.MethodSecurityConfig$$EnhancerBySpringCGLIB$$a8f968cd] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
2023-08-20 19:10:39.123  INFO 39701 --- [           main] trationDelegate$BeanPostProcessorChecker : Bean 'methodSecurityMetadataSource' of type [org.springframework.security.access.method.DelegatingMethodSecurityMetadataSource] is not eligible for getting processed by all BeanPostProcessors (for example: not eligible for auto-proxying)
2023-08-20 19:10:39.408  INFO 39701 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port(s): 18080 (http)
2023-08-20 19:10:39.418  INFO 39701 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2023-08-20 19:10:39.418  INFO 39701 --- [           main] org.apache.catalina.core.StandardEngine  : Starting Servlet engine: [Apache Tomcat/9.0.53]
2023-08-20 19:10:39.500  INFO 39701 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2023-08-20 19:10:39.501  INFO 39701 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 2084 ms
2023-08-20 19:10:39.726  INFO 39701 --- [           main] .s.s.UserDetailsServiceAutoConfiguration :

Using generated security password: 044aa1fe-2275-4b80-8959-303f5c589ddb

2023-08-20 19:10:40.026  INFO 39701 --- [           main] o.a.e.i.c.ProcessEngineConfigurationImpl : Found 1 Process Engine Configurators in total:
2023-08-20 19:10:40.027  INFO 39701 --- [           main] o.a.e.i.c.ProcessEngineConfigurationImpl : class org.activiti.spring.process.autoconfigure.ProcessExtensionsConfiguratorAutoConfiguration$$EnhancerBySpringCGLIB$$f9f5906b (priority:10000)
2023-08-20 19:10:40.028  INFO 39701 --- [           main] o.a.e.i.c.ProcessEngineConfigurationImpl : Executing beforeInit() of class org.activiti.spring.process.autoconfigure.ProcessExtensionsConfiguratorAutoConfiguration$$EnhancerBySpringCGLIB$$f9f5906b (priority:10000)
2023-08-20 19:10:40.038  INFO 39701 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Starting...
2023-08-20 19:10:40.203  INFO 39701 --- [           main] com.zaxxer.hikari.HikariDataSource       : HikariPool-1 - Start completed.
2023-08-20 19:10:40.862  INFO 39701 --- [           main] o.a.e.i.c.ProcessEngineConfigurationImpl : Executing configure() of class org.activiti.spring.process.autoconfigure.ProcessExtensionsConfiguratorAutoConfiguration$$EnhancerBySpringCGLIB$$f9f5906b (priority:10000)
2023-08-20 19:10:40.905  INFO 39701 --- [           main] o.activiti.engine.impl.db.DbSqlSession   : performing create on engine with resource org/activiti/db/create/activiti.mysql.create.engine.sql
2023-08-20 19:10:40.906  INFO 39701 --- [           main] o.activiti.engine.impl.db.DbSqlSession   : Found MySQL: majorVersion=8 minorVersion=0
2023-08-20 19:10:41.974  INFO 39701 --- [           main] o.activiti.engine.impl.db.DbSqlSession   : performing create on history with resource org/activiti/db/create/activiti.mysql.create.history.sql
2023-08-20 19:10:41.974  INFO 39701 --- [           main] o.activiti.engine.impl.db.DbSqlSession   : Found MySQL: majorVersion=8 minorVersion=0
2023-08-20 19:10:42.145  INFO 39701 --- [           main] o.a.engine.impl.ProcessEngineImpl        : ProcessEngine default created
2023-08-20 19:10:42.162 DEBUG 39701 --- [           main] o.a.e.i.p.e.P.selectProperty             : ==>  Preparing: select * from ACT_GE_PROPERTY where NAME_ = ?
2023-08-20 19:10:42.180 DEBUG 39701 --- [           main] o.a.e.i.p.e.P.selectProperty             : ==> Parameters: cfg.execution-related-entities-count(String)
2023-08-20 19:10:42.198 DEBUG 39701 --- [           main] o.a.e.i.p.e.P.selectProperty             : <==      Total: 0
2023-08-20 19:10:42.200 DEBUG 39701 --- [           main] o.a.e.i.p.e.P.insertProperty             : ==>  Preparing: insert into ACT_GE_PROPERTY ( NAME_, VALUE_, REV_ ) values ( ?, ?, 1 )
2023-08-20 19:10:42.202 DEBUG 39701 --- [           main] o.a.e.i.p.e.P.insertProperty             : ==> Parameters: cfg.execution-related-entities-count(String), false(String)
2023-08-20 19:10:42.204 DEBUG 39701 --- [           main] o.a.e.i.p.e.P.insertProperty             : <==    Updates: 1
2023-08-20 19:10:42.682  INFO 39701 --- [           main] o.s.b.a.e.web.EndpointLinksResolver      : Exposing 1 endpoint(s) beneath base path '/actuator'
Logging initialized using 'class org.apache.ibatis.logging.stdout.StdOutImpl' adapter.
Property 'mapperLocations' was not specified.
 _ _   |_  _ _|_. ___ _ |    _
| | |\/|_)(_| | |_\  |_)||_|_\
     /               |
                        3.4.0
2023-08-20 19:10:43.588  INFO 39701 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 18080 (http) with context path ''
2023-08-20 19:10:43.754  INFO 39701 --- [           main] com.ybchen.ActivitiApplication           : Started ActivitiApplication in 6.844 seconds (JVM running for 7.78)
2023-08-20 19:10:43.783 DEBUG 39701 --- [           main] .selectProcessDefinitionsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_PROCDEF RES order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 19:10:43.784 DEBUG 39701 --- [           main] .selectProcessDefinitionsByQueryCriteria : ==> Parameters: 2147483647(Integer), 0(Integer)
2023-08-20 19:10:43.785 DEBUG 39701 --- [           main] .selectProcessDefinitionsByQueryCriteria : <==      Total: 0
2023-08-20 19:10:43.921  INFO 39701 --- [on(2)-127.0.0.1] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring DispatcherServlet 'dispatcherServlet'
2023-08-20 19:10:43.921  INFO 39701 --- [on(2)-127.0.0.1] o.s.web.servlet.DispatcherServlet        : Initializing Servlet 'dispatcherServlet'
2023-08-20 19:10:43.923  INFO 39701 --- [on(2)-127.0.0.1] o.s.web.servlet.DispatcherServlet        : Completed initialization in 2 ms
2023-08-20 19:10:50.456 DEBUG 39701 --- [io-18080-exec-1] p.e.P.selectLatestProcessDefinitionByKey : ==>  Preparing: select * from ACT_RE_PROCDEF where KEY_ = ? and (TENANT_ID_ = '' or TENANT_ID_ is null) and VERSION_ = (select max(VERSION_) from ACT_RE_PROCDEF where KEY_ = ? and (TENANT_ID_ = '' or TENANT_ID_ is null))
2023-08-20 19:10:50.457 DEBUG 39701 --- [io-18080-exec-1] p.e.P.selectLatestProcessDefinitionByKey : ==> Parameters: test01(String), test01(String)
2023-08-20 19:10:50.458 DEBUG 39701 --- [io-18080-exec-1] p.e.P.selectLatestProcessDefinitionByKey : <==      Total: 0
2023-08-20 19:10:50.465 DEBUG 39701 --- [io-18080-exec-1] bByTypeAndProcessDefinitionKeyNoTenantId : ==>  Preparing: select J.* from ACT_RU_TIMER_JOB J inner join ACT_RE_PROCDEF P on J.PROC_DEF_ID_ = P.ID_ where J.HANDLER_TYPE_ = ? and P.KEY_ = ? and (P.TENANT_ID_ = '' or P.TENANT_ID_ is null)
2023-08-20 19:10:50.465 DEBUG 39701 --- [io-18080-exec-1] bByTypeAndProcessDefinitionKeyNoTenantId : ==> Parameters: timer-start-event(String), test01(String)
2023-08-20 19:10:50.466 DEBUG 39701 --- [io-18080-exec-1] bByTypeAndProcessDefinitionKeyNoTenantId : <==      Total: 0
2023-08-20 19:10:50.466  INFO 39701 --- [io-18080-exec-1] o.a.e.impl.bpmn.deployer.BpmnDeployer    : Process deployed: {id: test01:1:38967bc9-3f4a-11ee-9292-8629a6918075, key: test01, name: test01 }
2023-08-20 19:10:50.469 DEBUG 39701 --- [io-18080-exec-1] ocessDefinitionInfoByProcessDefinitionId : ==>  Preparing: select * from ACT_PROCDEF_INFO where PROC_DEF_ID_ = ?
2023-08-20 19:10:50.469 DEBUG 39701 --- [io-18080-exec-1] ocessDefinitionInfoByProcessDefinitionId : ==> Parameters: test01:1:38967bc9-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:10:50.469 DEBUG 39701 --- [io-18080-exec-1] ocessDefinitionInfoByProcessDefinitionId : <==      Total: 0
2023-08-20 19:10:50.470 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.P.insertProcessDefinition    : ==>  Preparing: insert into ACT_RE_PROCDEF(ID_, REV_, CATEGORY_, NAME_, KEY_, VERSION_, DEPLOYMENT_ID_, RESOURCE_NAME_, DGRM_RESOURCE_NAME_, DESCRIPTION_, HAS_START_FORM_KEY_, HAS_GRAPHICAL_NOTATION_ , SUSPENSION_STATE_, TENANT_ID_, ENGINE_VERSION_) values (?, 1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
2023-08-20 19:10:50.471 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.P.insertProcessDefinition    : ==> Parameters: test01:1:38967bc9-3f4a-11ee-9292-8629a6918075(String), http://www.activiti.org/processdef(String), test01(String), test01(String), 1(Integer), 388034a6-3f4a-11ee-9292-8629a6918075(String), test01.bpmn20.xml(String), test01.png(String), null, false(Boolean), true(Boolean), 1(Integer), (String), null
2023-08-20 19:10:50.472 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.P.insertProcessDefinition    : <==    Updates: 1
2023-08-20 19:10:50.472 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.D.insertDeployment           : ==>  Preparing: insert into ACT_RE_DEPLOYMENT(ID_, NAME_, CATEGORY_, KEY_, TENANT_ID_, DEPLOY_TIME_, ENGINE_VERSION_) values(?, ?, ?, ?, ?, ?, ?)
2023-08-20 19:10:50.477 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.D.insertDeployment           : ==> Parameters: 388034a6-3f4a-11ee-9292-8629a6918075(String), 请假审批(String), null, null, (String), 2023-08-20 19:10:50.312(Timestamp), null
2023-08-20 19:10:50.478 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.D.insertDeployment           : <==    Updates: 1
2023-08-20 19:10:50.481 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.R.bulkInsertResource         : ==>  Preparing: INSERT INTO ACT_GE_BYTEARRAY(ID_, REV_, NAME_, BYTES_, DEPLOYMENT_ID_, GENERATED_) VALUES (?, 1, ?, ?, ?, ?) , (?, 1, ?, ?, ?, ?)
2023-08-20 19:10:50.482 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.R.bulkInsertResource         : ==> Parameters: 38805bb7-3f4a-11ee-9292-8629a6918075(String), test01.bpmn20.xml(String), java.io.ByteArrayInputStream@59c2252b(ByteArrayInputStream), 388034a6-3f4a-11ee-9292-8629a6918075(String), false(Boolean), 388082c8-3f4a-11ee-9292-8629a6918075(String), test01.png(String), java.io.ByteArrayInputStream@598b95ef(ByteArrayInputStream), 388034a6-3f4a-11ee-9292-8629a6918075(String), false(Boolean)
2023-08-20 19:10:50.485 DEBUG 39701 --- [io-18080-exec-1] o.a.e.i.p.e.R.bulkInsertResource         : <==    Updates: 2
```

![](./images/images/img_009_a04bbe3a80c3.png)

# 查询流程部署信息

```text
    //提供对流程定义和部署存储库的访问服务
    @Autowired
    RepositoryService repositoryService;

    @ApiOperation("查询流程部署信息")
    @PostMapping("queryDeploymentInfo")
    public ReturnData queryDeploymentInfo() {
        //也可以设置查询部署筛选条件，自行查询API，基本上都是见名知意的
        List<Deployment> list = repositoryService.createDeploymentQuery().list();
        log.info("流程部署信息：{}", list);
        return ReturnData.buildSuccess(list.toString());
    }
```

![](./images/images/img_010_1a0147385810.gif)

![](./images/images/img_011_8d8cb27d5007.png)

# 查询流程定义信息

```text
    //提供对流程定义和部署存储库的访问服务
    @Autowired
    RepositoryService repositoryService;

    @ApiOperation("查询流程定义信息")
    @PostMapping("queryProcessInfo")
    public ReturnData queryProcessInfo() {
        //也可以设置查询流程定义筛选条件，自行查询API，基本上都是见名知意的
        List<ProcessDefinition> list = repositoryService.createProcessDefinitionQuery().list();
        log.info("流程定义信息：{}", list);
        return ReturnData.buildSuccess(list.toString());
    }
```

![](./images/images/img_012_d466c20379e5.gif)

![](./images/images/img_013_bc03470c3879.png)

# 删除流程定义

```text
    //提供对流程定义和部署存储库的访问服务
    @Autowired
    RepositoryService repositoryService;

    @ApiOperation("根据部署id删除流程部署")
    @GetMapping("deleteDeploymentById")
    public ReturnData deleteDeploymentById(
            @ApiParam(value = "流程部署id", required = true) String deploymentId
    ) {
        List<Deployment> list = repositoryService.createDeploymentQuery().deploymentId(deploymentId).list();
        if (list.size() != 1) {
            return ReturnData.buildError("流程定义未找到");
        }
        //根据部署id删除流程部署
        repositoryService.deleteDeployment(deploymentId);
        return ReturnData.buildSuccess("删除成功");
    }
```

![](./images/images/img_014_ee30820d1ca6.gif)

```text
2023-08-20 19:51:07.956 DEBUG 60519 --- [io-18080-exec-6] i.p.e.D.selectDeploymentsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_DEPLOYMENT RES WHERE RES.ID_ = ? order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 19:51:07.957 DEBUG 60519 --- [io-18080-exec-6] i.p.e.D.selectDeploymentsByQueryCriteria : ==> Parameters: 1(String), 2147483647(Integer), 0(Integer)
2023-08-20 19:51:07.958 DEBUG 60519 --- [io-18080-exec-6] i.p.e.D.selectDeploymentsByQueryCriteria : <==      Total: 0
2023-08-20 19:51:21.511 DEBUG 60519 --- [io-18080-exec-7] i.p.e.D.selectDeploymentsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_DEPLOYMENT RES order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 19:51:21.511 DEBUG 60519 --- [io-18080-exec-7] i.p.e.D.selectDeploymentsByQueryCriteria : ==> Parameters: 2147483647(Integer), 0(Integer)
2023-08-20 19:51:21.514 TRACE 60519 --- [io-18080-exec-7] i.p.e.D.selectDeploymentsByQueryCriteria : <==    Columns: ID_, NAME_, CATEGORY_, KEY_, TENANT_ID_, DEPLOY_TIME_, ENGINE_VERSION_
2023-08-20 19:51:21.514 TRACE 60519 --- [io-18080-exec-7] i.p.e.D.selectDeploymentsByQueryCriteria : <==        Row: 388034a6-3f4a-11ee-9292-8629a6918075, 请假审批, null, null, , 2023-08-20 19:10:50.312, null
2023-08-20 19:51:21.515 DEBUG 60519 --- [io-18080-exec-7] i.p.e.D.selectDeploymentsByQueryCriteria : <==      Total: 1
2023-08-20 19:51:21.516  INFO 60519 --- [io-18080-exec-7] c.ybchen.controller.ActivitiController   : 流程部署信息：[DeploymentEntity[id=388034a6-3f4a-11ee-9292-8629a6918075, name=请假审批]]
2023-08-20 19:51:32.288 DEBUG 60519 --- [io-18080-exec-8] i.p.e.D.selectDeploymentsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_DEPLOYMENT RES WHERE RES.ID_ = ? order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 19:51:32.289 DEBUG 60519 --- [io-18080-exec-8] i.p.e.D.selectDeploymentsByQueryCriteria : ==> Parameters: 388034a6-3f4a-11ee-9292-8629a6918075(String), 2147483647(Integer), 0(Integer)
2023-08-20 19:51:32.289 TRACE 60519 --- [io-18080-exec-8] i.p.e.D.selectDeploymentsByQueryCriteria : <==    Columns: ID_, NAME_, CATEGORY_, KEY_, TENANT_ID_, DEPLOY_TIME_, ENGINE_VERSION_
2023-08-20 19:51:32.290 TRACE 60519 --- [io-18080-exec-8] i.p.e.D.selectDeploymentsByQueryCriteria : <==        Row: 388034a6-3f4a-11ee-9292-8629a6918075, 请假审批, null, null, , 2023-08-20 19:10:50.312, null
2023-08-20 19:51:32.290 DEBUG 60519 --- [io-18080-exec-8] i.p.e.D.selectDeploymentsByQueryCriteria : <==      Total: 1
2023-08-20 19:51:32.292 DEBUG 60519 --- [io-18080-exec-8] o.a.e.i.p.e.D.selectDeployment           : ==>  Preparing: select * from ACT_RE_DEPLOYMENT where ID_ = ?
2023-08-20 19:51:32.292 DEBUG 60519 --- [io-18080-exec-8] o.a.e.i.p.e.D.selectDeployment           : ==> Parameters: 388034a6-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:51:32.293 TRACE 60519 --- [io-18080-exec-8] o.a.e.i.p.e.D.selectDeployment           : <==    Columns: ID_, NAME_, CATEGORY_, KEY_, TENANT_ID_, DEPLOY_TIME_, ENGINE_VERSION_
2023-08-20 19:51:32.293 TRACE 60519 --- [io-18080-exec-8] o.a.e.i.p.e.D.selectDeployment           : <==        Row: 388034a6-3f4a-11ee-9292-8629a6918075, 请假审批, null, null, , 2023-08-20 19:10:50.312, null
2023-08-20 19:51:32.294 DEBUG 60519 --- [io-18080-exec-8] o.a.e.i.p.e.D.selectDeployment           : <==      Total: 1
2023-08-20 19:51:32.295 DEBUG 60519 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_PROCDEF RES WHERE RES.DEPLOYMENT_ID_ = ? order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 19:51:32.295 DEBUG 60519 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : ==> Parameters: 388034a6-3f4a-11ee-9292-8629a6918075(String), 2147483647(Integer), 0(Integer)
2023-08-20 19:51:32.296 TRACE 60519 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==    Columns: ID_, REV_, CATEGORY_, NAME_, KEY_, VERSION_, DEPLOYMENT_ID_, RESOURCE_NAME_, DGRM_RESOURCE_NAME_, DESCRIPTION_, HAS_START_FORM_KEY_, HAS_GRAPHICAL_NOTATION_, SUSPENSION_STATE_, TENANT_ID_, ENGINE_VERSION_
2023-08-20 19:51:32.296 TRACE 60519 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==        Row: test01:1:38967bc9-3f4a-11ee-9292-8629a6918075, 1, http://www.activiti.org/processdef, test01, test01, 1, 388034a6-3f4a-11ee-9292-8629a6918075, test01.bpmn20.xml, test01.png, null, 0, 1, 1, , null
2023-08-20 19:51:32.296 DEBUG 60519 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==      Total: 1
2023-08-20 19:51:32.299 DEBUG 60519 --- [io-18080-exec-8] .a.e.i.p.e.M.selectModelsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_MODEL RES WHERE RES.DEPLOYMENT_ID_ = ? order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 19:51:32.299 DEBUG 60519 --- [io-18080-exec-8] .a.e.i.p.e.M.selectModelsByQueryCriteria : ==> Parameters: 388034a6-3f4a-11ee-9292-8629a6918075(String), 2147483647(Integer), 0(Integer)
2023-08-20 19:51:32.301 DEBUG 60519 --- [io-18080-exec-8] .a.e.i.p.e.M.selectModelsByQueryCriteria : <==      Total: 0
2023-08-20 19:51:32.302 DEBUG 60519 --- [io-18080-exec-8] ocessDefinitionInfoByProcessDefinitionId : ==>  Preparing: select * from ACT_PROCDEF_INFO where PROC_DEF_ID_ = ?
2023-08-20 19:51:32.302 DEBUG 60519 --- [io-18080-exec-8] ocessDefinitionInfoByProcessDefinitionId : ==> Parameters: test01:1:38967bc9-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:51:32.303 DEBUG 60519 --- [io-18080-exec-8] ocessDefinitionInfoByProcessDefinitionId : <==      Total: 0
2023-08-20 19:51:32.305 DEBUG 60519 --- [io-18080-exec-8] lectTimerJobByTypeAndProcessDefinitionId : ==>  Preparing: select J.* from ACT_RU_TIMER_JOB J where J.HANDLER_TYPE_ = ? and J.PROC_DEF_ID_ = ?
2023-08-20 19:51:32.306 DEBUG 60519 --- [io-18080-exec-8] lectTimerJobByTypeAndProcessDefinitionId : ==> Parameters: timer-start-event(String), test01:1:38967bc9-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:51:32.308 DEBUG 60519 --- [io-18080-exec-8] lectTimerJobByTypeAndProcessDefinitionId : <==      Total: 0
2023-08-20 19:51:32.309 DEBUG 60519 --- [io-18080-exec-8] p.e.P.selectLatestProcessDefinitionByKey : ==>  Preparing: select * from ACT_RE_PROCDEF where KEY_ = ? and (TENANT_ID_ = '' or TENANT_ID_ is null) and VERSION_ = (select max(VERSION_) from ACT_RE_PROCDEF where KEY_ = ? and (TENANT_ID_ = '' or TENANT_ID_ is null))
2023-08-20 19:51:32.309 DEBUG 60519 --- [io-18080-exec-8] p.e.P.selectLatestProcessDefinitionByKey : ==> Parameters: test01(String), test01(String)
2023-08-20 19:51:32.310 TRACE 60519 --- [io-18080-exec-8] p.e.P.selectLatestProcessDefinitionByKey : <==    Columns: ID_, REV_, CATEGORY_, NAME_, KEY_, VERSION_, DEPLOYMENT_ID_, RESOURCE_NAME_, DGRM_RESOURCE_NAME_, DESCRIPTION_, HAS_START_FORM_KEY_, HAS_GRAPHICAL_NOTATION_, SUSPENSION_STATE_, TENANT_ID_, ENGINE_VERSION_
2023-08-20 19:51:32.310 TRACE 60519 --- [io-18080-exec-8] p.e.P.selectLatestProcessDefinitionByKey : <==        Row: test01:1:38967bc9-3f4a-11ee-9292-8629a6918075, 1, http://www.activiti.org/processdef, test01, test01, 1, 388034a6-3f4a-11ee-9292-8629a6918075, test01.bpmn20.xml, test01.png, null, 0, 1, 1, , null
2023-08-20 19:51:32.311 DEBUG 60519 --- [io-18080-exec-8] p.e.P.selectLatestProcessDefinitionByKey : <==      Total: 1
2023-08-20 19:51:32.312 DEBUG 60519 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_PROCDEF RES WHERE RES.KEY_ = ? and RES.VERSION_ < ? and (RES.TENANT_ID_ = '' or RES.TENANT_ID_ is null) order by RES.VERSION_ desc LIMIT ? OFFSET ?
2023-08-20 19:51:32.312 DEBUG 60519 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : ==> Parameters: test01(String), 1(Integer), 1(Integer), 0(Integer)
2023-08-20 19:51:32.313 DEBUG 60519 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==      Total: 0
2023-08-20 19:51:32.313 DEBUG 60519 --- [io-18080-exec-8] .e.i.p.e.R.deleteResourcesByDeploymentId : ==>  Preparing: delete from ACT_GE_BYTEARRAY where DEPLOYMENT_ID_ = ?
2023-08-20 19:51:32.313 DEBUG 60519 --- [io-18080-exec-8] .e.i.p.e.R.deleteResourcesByDeploymentId : ==> Parameters: 388034a6-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:51:32.318 DEBUG 60519 --- [io-18080-exec-8] .e.i.p.e.R.deleteResourcesByDeploymentId : <==    Updates: 2
2023-08-20 19:51:32.318 DEBUG 60519 --- [io-18080-exec-8] o.a.e.i.p.e.D.deleteDeployment           : ==>  Preparing: delete from ACT_RE_DEPLOYMENT where ID_ = ?
2023-08-20 19:51:32.318 DEBUG 60519 --- [io-18080-exec-8] o.a.e.i.p.e.D.deleteDeployment           : ==> Parameters: 388034a6-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:51:32.320 DEBUG 60519 --- [io-18080-exec-8] o.a.e.i.p.e.D.deleteDeployment           : <==    Updates: 1
2023-08-20 19:51:32.320 DEBUG 60519 --- [io-18080-exec-8] teEventSubscriptionsForProcessDefinition : ==>  Preparing: delete from ACT_RU_EVENT_SUBSCR where PROC_DEF_ID_ = ? and EXECUTION_ID_ is null and PROC_INST_ID_ is null
2023-08-20 19:51:32.320 DEBUG 60519 --- [io-18080-exec-8] teEventSubscriptionsForProcessDefinition : ==> Parameters: test01:1:38967bc9-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:51:32.321 DEBUG 60519 --- [io-18080-exec-8] teEventSubscriptionsForProcessDefinition : <==    Updates: 0
2023-08-20 19:51:32.321 DEBUG 60519 --- [io-18080-exec-8] .a.e.i.p.e.I.deleteIdentityLinkByProcDef : ==>  Preparing: delete from ACT_RU_IDENTITYLINK where PROC_DEF_ID_ = ?
2023-08-20 19:51:32.322 DEBUG 60519 --- [io-18080-exec-8] .a.e.i.p.e.I.deleteIdentityLinkByProcDef : ==> Parameters: test01:1:38967bc9-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:51:32.324 DEBUG 60519 --- [io-18080-exec-8] .a.e.i.p.e.I.deleteIdentityLinkByProcDef : <==    Updates: 0
2023-08-20 19:51:32.324 DEBUG 60519 --- [io-18080-exec-8] P.deleteProcessDefinitionsByDeploymentId : ==>  Preparing: delete from ACT_RE_PROCDEF where DEPLOYMENT_ID_ = ?
2023-08-20 19:51:32.324 DEBUG 60519 --- [io-18080-exec-8] P.deleteProcessDefinitionsByDeploymentId : ==> Parameters: 388034a6-3f4a-11ee-9292-8629a6918075(String)
2023-08-20 19:51:32.325 DEBUG 60519 --- [io-18080-exec-8] P.deleteProcessDefinitionsByDeploymentId : <==    Updates: 1
```

# 发起流程

```text
    //提供对流程定义和部署存储库的访问服务
    @Autowired
    RepositoryService repositoryService;
    //运行时的接口
    @Autowired
    RuntimeService runtimeService;

    @ApiOperation("发起流程")
    @GetMapping("startProcess")
    public ReturnData startProcess(
            @ApiParam(value = "流程定义id",required = true) String processDefinitionId
    ) {
        log.info("发起流程，processDefinitionId：{}", processDefinitionId);
        List<ProcessDefinition> list = repositoryService.createProcessDefinitionQuery().processDefinitionId(processDefinitionId).list();
        if (list.size() != 1) {
            return ReturnData.buildError("流程定义不存在");
        }
        //通过流程定义ID启动一个流程实例
        ProcessInstance processInstance = runtimeService.startProcessInstanceById(processDefinitionId);
        log.info("流程实例：{}", processInstance);
        return ReturnData.buildSuccess("发起成功");
    }
```

![](./images/images/img_015_5f0a81ad6731.gif)

```text
2023-08-20 20:10:28.593 DEBUG 70687 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_PROCDEF RES order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 20:10:28.594 DEBUG 70687 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : ==> Parameters: 2147483647(Integer), 0(Integer)
2023-08-20 20:10:28.594 TRACE 70687 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==    Columns: ID_, REV_, CATEGORY_, NAME_, KEY_, VERSION_, DEPLOYMENT_ID_, RESOURCE_NAME_, DGRM_RESOURCE_NAME_, DESCRIPTION_, HAS_START_FORM_KEY_, HAS_GRAPHICAL_NOTATION_, SUSPENSION_STATE_, TENANT_ID_, ENGINE_VERSION_
2023-08-20 20:10:28.594 TRACE 70687 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==        Row: test01:1:70466829-3f50-11ee-82fb-8629a6918075, 1, http://www.activiti.org/processdef, test01, test01, 1, 7038faa6-3f50-11ee-82fb-8629a6918075, test01.bpmn20.xml, test01.png, null, 0, 1, 1, , null
2023-08-20 20:10:28.595 TRACE 70687 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==        Row: test01:2:71bf739d-3f50-11ee-82fb-8629a6918075, 1, http://www.activiti.org/processdef, test01, test01, 2, 71bba30a-3f50-11ee-82fb-8629a6918075, test01.bpmn20.xml, test01.png, null, 0, 1, 1, , null
2023-08-20 20:10:28.595 TRACE 70687 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==        Row: test01:3:72a47c71-3f50-11ee-82fb-8629a6918075, 1, http://www.activiti.org/processdef, test01, test01, 3, 729c8d2e-3f50-11ee-82fb-8629a6918075, test01.bpmn20.xml, test01.png, null, 0, 1, 1, , null
2023-08-20 20:10:28.595 DEBUG 70687 --- [io-18080-exec-8] .selectProcessDefinitionsByQueryCriteria : <==      Total: 3
2023-08-20 20:10:28.596  INFO 70687 --- [io-18080-exec-8] c.ybchen.controller.ActivitiController   : 流程定义信息：[ProcessDefinitionEntity[test01:1:70466829-3f50-11ee-82fb-8629a6918075], ProcessDefinitionEntity[test01:2:71bf739d-3f50-11ee-82fb-8629a6918075], ProcessDefinitionEntity[test01:3:72a47c71-3f50-11ee-82fb-8629a6918075]]
2023-08-20 20:10:48.480  INFO 70687 --- [io-18080-exec-9] c.ybchen.controller.ActivitiController   : 发起流程，processDefinitionId：test01:1:70466829-3f50-11ee-82fb-8629a6918075
2023-08-20 20:10:48.481 DEBUG 70687 --- [io-18080-exec-9] .selectProcessDefinitionsByQueryCriteria : ==>  Preparing: select distinct RES.* from ACT_RE_PROCDEF RES WHERE RES.ID_ = ? order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 20:10:48.482 DEBUG 70687 --- [io-18080-exec-9] .selectProcessDefinitionsByQueryCriteria : ==> Parameters: test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), 2147483647(Integer), 0(Integer)
2023-08-20 20:10:48.483 TRACE 70687 --- [io-18080-exec-9] .selectProcessDefinitionsByQueryCriteria : <==    Columns: ID_, REV_, CATEGORY_, NAME_, KEY_, VERSION_, DEPLOYMENT_ID_, RESOURCE_NAME_, DGRM_RESOURCE_NAME_, DESCRIPTION_, HAS_START_FORM_KEY_, HAS_GRAPHICAL_NOTATION_, SUSPENSION_STATE_, TENANT_ID_, ENGINE_VERSION_
2023-08-20 20:10:48.483 TRACE 70687 --- [io-18080-exec-9] .selectProcessDefinitionsByQueryCriteria : <==        Row: test01:1:70466829-3f50-11ee-82fb-8629a6918075, 1, http://www.activiti.org/processdef, test01, test01, 1, 7038faa6-3f50-11ee-82fb-8629a6918075, test01.bpmn20.xml, test01.png, null, 0, 1, 1, , null
2023-08-20 20:10:48.483 DEBUG 70687 --- [io-18080-exec-9] .selectProcessDefinitionsByQueryCriteria : <==      Total: 1
2023-08-20 20:10:48.485 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.P.selectProcessDefinition    : ==>  Preparing: select * from ACT_RE_PROCDEF where ID_ = ?
2023-08-20 20:10:48.485 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.P.selectProcessDefinition    : ==> Parameters: test01:1:70466829-3f50-11ee-82fb-8629a6918075(String)
2023-08-20 20:10:48.486 TRACE 70687 --- [io-18080-exec-9] o.a.e.i.p.e.P.selectProcessDefinition    : <==    Columns: ID_, REV_, CATEGORY_, NAME_, KEY_, VERSION_, DEPLOYMENT_ID_, RESOURCE_NAME_, DGRM_RESOURCE_NAME_, DESCRIPTION_, HAS_START_FORM_KEY_, HAS_GRAPHICAL_NOTATION_, SUSPENSION_STATE_, TENANT_ID_, ENGINE_VERSION_
2023-08-20 20:10:48.486 TRACE 70687 --- [io-18080-exec-9] o.a.e.i.p.e.P.selectProcessDefinition    : <==        Row: test01:1:70466829-3f50-11ee-82fb-8629a6918075, 1, http://www.activiti.org/processdef, test01, test01, 1, 7038faa6-3f50-11ee-82fb-8629a6918075, test01.bpmn20.xml, test01.png, null, 0, 1, 1, , null
2023-08-20 20:10:48.487 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.P.selectProcessDefinition    : <==      Total: 1
2023-08-20 20:10:48.490 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.ExecutionEntityManagerImpl   : Child execution Execution[ id '992e98b5-3f52-11ee-ae7f-8629a6918075' ] - parent '992e2384-3f52-11ee-ae7f-8629a6918075' created with parent 992e2384-3f52-11ee-ae7f-8629a6918075
2023-08-20 20:10:48.511 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.V.selectVariablesByTaskId    : ==>  Preparing: select * from ACT_RU_VARIABLE where TASK_ID_ = ?
2023-08-20 20:10:48.512 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.V.selectVariablesByTaskId    : ==> Parameters: 9931cd08-3f52-11ee-ae7f-8629a6918075(String)
2023-08-20 20:10:48.513 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.V.selectVariablesByTaskId    : <==      Total: 0
2023-08-20 20:10:48.515 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.H.insertHistoricTaskInstance : ==>  Preparing: insert into ACT_HI_TASKINST ( ID_, PROC_DEF_ID_, PROC_INST_ID_, EXECUTION_ID_, NAME_, PARENT_TASK_ID_, DESCRIPTION_, OWNER_, ASSIGNEE_, START_TIME_, CLAIM_TIME_, END_TIME_, DURATION_, DELETE_REASON_, TASK_DEF_KEY_, FORM_KEY_, PRIORITY_, DUE_DATE_, CATEGORY_, TENANT_ID_ ) values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
2023-08-20 20:10:48.516 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.H.insertHistoricTaskInstance : ==> Parameters: 9931cd08-3f52-11ee-ae7f-8629a6918075(String), test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), 992e2384-3f52-11ee-ae7f-8629a6918075(String), 992e98b5-3f52-11ee-ae7f-8629a6918075(String), 经理审批(String), null, null, null, null, 2023-08-20 20:10:48.511(Timestamp), null, null, null, null, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794(String), null, 50(Integer), null, null, (String)
2023-08-20 20:10:48.518 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.H.insertHistoricTaskInstance : <==    Updates: 1
2023-08-20 20:10:48.518 DEBUG 70687 --- [io-18080-exec-9] .e.i.p.e.H.insertHistoricProcessInstance : ==>  Preparing: insert into ACT_HI_PROCINST ( ID_, PROC_INST_ID_, BUSINESS_KEY_, PROC_DEF_ID_, START_TIME_, END_TIME_, DURATION_, START_USER_ID_, START_ACT_ID_, END_ACT_ID_, SUPER_PROCESS_INSTANCE_ID_, DELETE_REASON_, TENANT_ID_, NAME_ ) values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
2023-08-20 20:10:48.519 DEBUG 70687 --- [io-18080-exec-9] .e.i.p.e.H.insertHistoricProcessInstance : ==> Parameters: 992e2384-3f52-11ee-ae7f-8629a6918075(String), 992e2384-3f52-11ee-ae7f-8629a6918075(String), null, test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), 2023-08-20 20:10:48.487(Timestamp), null, null, null, sid-7bcd1c8f-20cb-4c36-9756-7c380d1158d0(String), null, null, null, (String), null
2023-08-20 20:10:48.520 DEBUG 70687 --- [io-18080-exec-9] .e.i.p.e.H.insertHistoricProcessInstance : <==    Updates: 1
2023-08-20 20:10:48.527 DEBUG 70687 --- [io-18080-exec-9] p.e.H.bulkInsertHistoricActivityInstance : ==>  Preparing: insert into ACT_HI_ACTINST ( ID_, PROC_DEF_ID_, PROC_INST_ID_, EXECUTION_ID_, ACT_ID_, TASK_ID_, CALL_PROC_INST_ID_, ACT_NAME_, ACT_TYPE_, ASSIGNEE_, START_TIME_, END_TIME_, DURATION_, DELETE_REASON_, TENANT_ID_ ) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) , (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
2023-08-20 20:10:48.529 DEBUG 70687 --- [io-18080-exec-9] p.e.H.bulkInsertHistoricActivityInstance : ==> Parameters: 992ee6d6-3f52-11ee-ae7f-8629a6918075(String), test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), 992e2384-3f52-11ee-ae7f-8629a6918075(String), 992e98b5-3f52-11ee-ae7f-8629a6918075(String), sid-7bcd1c8f-20cb-4c36-9756-7c380d1158d0(String), null, null, 开始(String), startEvent(String), null, 2023-08-20 20:10:48.492(Timestamp), 2023-08-20 20:10:48.494(Timestamp), 2(Long), null, (String), 992f8317-3f52-11ee-ae7f-8629a6918075(String), test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), 992e2384-3f52-11ee-ae7f-8629a6918075(String), 992e98b5-3f52-11ee-ae7f-8629a6918075(String), sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794(String), 9931cd08-3f52-11ee-ae7f-8629a6918075(String), null, 经理审批(String), userTask(String), null, 2023-08-20 20:10:48.496(Timestamp), null, null, null, (String)
2023-08-20 20:10:48.532 DEBUG 70687 --- [io-18080-exec-9] p.e.H.bulkInsertHistoricActivityInstance : <==    Updates: 2
2023-08-20 20:10:48.534 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.E.bulkInsertExecution        : ==>  Preparing: insert into ACT_RU_EXECUTION (ID_, REV_, PROC_INST_ID_, BUSINESS_KEY_, PROC_DEF_ID_, ACT_ID_, IS_ACTIVE_, IS_CONCURRENT_, IS_SCOPE_,IS_EVENT_SCOPE_, IS_MI_ROOT_, PARENT_ID_, SUPER_EXEC_, ROOT_PROC_INST_ID_, SUSPENSION_STATE_, TENANT_ID_, NAME_, START_TIME_, START_USER_ID_, IS_COUNT_ENABLED_, EVT_SUBSCR_COUNT_, TASK_COUNT_, JOB_COUNT_, TIMER_JOB_COUNT_, SUSP_JOB_COUNT_, DEADLETTER_JOB_COUNT_, VAR_COUNT_, ID_LINK_COUNT_) values (?, 1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) , (?, 1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
2023-08-20 20:10:48.536 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.E.bulkInsertExecution        : ==> Parameters: 992e2384-3f52-11ee-ae7f-8629a6918075(String), 992e2384-3f52-11ee-ae7f-8629a6918075(String), null, test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), null, true(Boolean), false(Boolean), true(Boolean), false(Boolean), false(Boolean), null, null, 992e2384-3f52-11ee-ae7f-8629a6918075(String), 1(Integer), (String), null, 2023-08-20 20:10:48.487(Timestamp), null, false(Boolean), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 992e98b5-3f52-11ee-ae7f-8629a6918075(String), 992e2384-3f52-11ee-ae7f-8629a6918075(String), null, test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794(String), true(Boolean), false(Boolean), false(Boolean), false(Boolean), false(Boolean), 992e2384-3f52-11ee-ae7f-8629a6918075(String), null, 992e2384-3f52-11ee-ae7f-8629a6918075(String), 1(Integer), (String), null, 2023-08-20 20:10:48.49(Timestamp), null, false(Boolean), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer)
2023-08-20 20:10:48.545 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.E.bulkInsertExecution        : <==    Updates: 2
2023-08-20 20:10:48.545 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.TaskEntityImpl.insertTask    : ==>  Preparing: insert into ACT_RU_TASK (ID_, REV_, NAME_, PARENT_TASK_ID_, DESCRIPTION_, PRIORITY_, CREATE_TIME_, OWNER_, ASSIGNEE_, DELEGATION_, EXECUTION_ID_, PROC_INST_ID_, PROC_DEF_ID_, TASK_DEF_KEY_, DUE_DATE_, CATEGORY_, SUSPENSION_STATE_, TENANT_ID_, FORM_KEY_, CLAIM_TIME_) values (?, 1, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
2023-08-20 20:10:48.546 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.TaskEntityImpl.insertTask    : ==> Parameters: 9931cd08-3f52-11ee-ae7f-8629a6918075(String), 经理审批(String), null, null, 50(Integer), 2023-08-20 20:10:48.496(Timestamp), null, null, null, 992e98b5-3f52-11ee-ae7f-8629a6918075(String), 992e2384-3f52-11ee-ae7f-8629a6918075(String), test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794(String), null, null, 1(Integer), (String), null, null
2023-08-20 20:10:48.548 DEBUG 70687 --- [io-18080-exec-9] o.a.e.i.p.e.TaskEntityImpl.insertTask    : <==    Updates: 1
2023-08-20 20:10:48.550  INFO 70687 --- [io-18080-exec-9] c.ybchen.controller.ActivitiController   : 流程实例：ProcessInstance[992e2384-3f52-11ee-ae7f-8629a6918075]
```

```text
-- 插入以下5张表
insert into ACT_HI_TASKINST
insert into ACT_HI_PROCINST
insert into ACT_HI_ACTINST
insert into ACT_RU_EXECUTION
insert into ACT_RU_TASK

-- 返回流程实例id
流程实例：ProcessInstance[992e2384-3f52-11ee-ae7f-8629a6918075]
```

# 完成任务

```text
    //提供对流程定义和部署存储库的访问服务
    @Autowired
    RepositoryService repositoryService;
    //运行时的接口
    @Autowired
    RuntimeService runtimeService;
    // 任务处理接口
    @Autowired
    TaskService taskService;

    @ApiOperation("完成任务")
    @GetMapping("completeTask")
    public ReturnData completeTask(
            @ApiParam(value = "流程实例id", required = true) String processInstanceId
    ) {
        //根据流程实例id，查询任务
        List<Task> taskList = taskService.createTaskQuery().processInstanceId(processInstanceId).list();
        if (taskList.size() != 1) {
            return ReturnData.buildError("当前没有任务");
        }
        log.info("任务列表：{}", taskList);
        //根据任务id，完成任务
        taskService.complete(taskList.get(0).getId());
        return ReturnData.buildSuccess("完成任务");
    }
```

![](./images/images/img_016_6c617b6edae2.gif)

```text
2023-08-20 20:31:08.167 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTaskByQueryCriteria  : ==>  Preparing: select distinct RES.* from ACT_RU_TASK RES WHERE RES.PROC_INST_ID_ = ? order by RES.ID_ asc LIMIT ? OFFSET ?
2023-08-20 20:31:08.167 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTaskByQueryCriteria  : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String), 2147483647(Integer), 0(Integer)
2023-08-20 20:31:08.168 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTaskByQueryCriteria  : <==    Columns: ID_, REV_, EXECUTION_ID_, PROC_INST_ID_, PROC_DEF_ID_, NAME_, PARENT_TASK_ID_, DESCRIPTION_, TASK_DEF_KEY_, OWNER_, ASSIGNEE_, DELEGATION_, PRIORITY_, CREATE_TIME_, DUE_DATE_, CATEGORY_, SUSPENSION_STATE_, TENANT_ID_, FORM_KEY_, CLAIM_TIME_
2023-08-20 20:31:08.168 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTaskByQueryCriteria  : <==        Row: 503080b9-3f55-11ee-a4b7-8629a6918075, 1, 502e5dd6-3f55-11ee-a4b7-8629a6918075, 502e5dd5-3f55-11ee-a4b7-8629a6918075, test01:1:70466829-3f50-11ee-82fb-8629a6918075, 经理审批, null, null, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794, null, null, null, 50, 2023-08-20 20:30:14.507, null, null, 1, , null, null
2023-08-20 20:31:08.169 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTaskByQueryCriteria  : <==      Total: 1
2023-08-20 20:31:08.169  INFO 80145 --- [io-18080-exec-4] c.ybchen.controller.ActivitiController   : 任务列表：[Task[id=503080b9-3f55-11ee-a4b7-8629a6918075, name=经理审批]]
2023-08-20 20:31:08.170 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.TaskEntityImpl.selectTask    : ==>  Preparing: select * from ACT_RU_TASK where ID_ = ?
2023-08-20 20:31:08.171 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.TaskEntityImpl.selectTask    : ==> Parameters: 503080b9-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.171 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.TaskEntityImpl.selectTask    : <==    Columns: ID_, REV_, EXECUTION_ID_, PROC_INST_ID_, PROC_DEF_ID_, NAME_, PARENT_TASK_ID_, DESCRIPTION_, TASK_DEF_KEY_, OWNER_, ASSIGNEE_, DELEGATION_, PRIORITY_, CREATE_TIME_, DUE_DATE_, CATEGORY_, SUSPENSION_STATE_, TENANT_ID_, FORM_KEY_, CLAIM_TIME_
2023-08-20 20:31:08.172 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.TaskEntityImpl.selectTask    : <==        Row: 503080b9-3f55-11ee-a4b7-8629a6918075, 1, 502e5dd6-3f55-11ee-a4b7-8629a6918075, 502e5dd5-3f55-11ee-a4b7-8629a6918075, test01:1:70466829-3f50-11ee-82fb-8629a6918075, 经理审批, null, null, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794, null, null, null, 50, 2023-08-20 20:30:14.507, null, null, 1, , null, null
2023-08-20 20:31:08.172 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.TaskEntityImpl.selectTask    : <==      Total: 1
2023-08-20 20:31:08.173 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : ==>  Preparing: select E.*, S.PROC_INST_ID_ AS PARENT_PROC_INST_ID_ from ACT_RU_EXECUTION E LEFT OUTER JOIN ACT_RU_EXECUTION S ON E.SUPER_EXEC_ = S.ID_ where E.ID_ = ?
2023-08-20 20:31:08.173 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.174 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : <==    Columns: ID_, REV_, PROC_INST_ID_, BUSINESS_KEY_, PARENT_ID_, PROC_DEF_ID_, SUPER_EXEC_, ROOT_PROC_INST_ID_, ACT_ID_, IS_ACTIVE_, IS_CONCURRENT_, IS_SCOPE_, IS_EVENT_SCOPE_, IS_MI_ROOT_, SUSPENSION_STATE_, CACHED_ENT_STATE_, TENANT_ID_, NAME_, START_TIME_, START_USER_ID_, LOCK_TIME_, IS_COUNT_ENABLED_, EVT_SUBSCR_COUNT_, TASK_COUNT_, JOB_COUNT_, TIMER_JOB_COUNT_, SUSP_JOB_COUNT_, DEADLETTER_JOB_COUNT_, VAR_COUNT_, ID_LINK_COUNT_, PARENT_PROC_INST_ID_
2023-08-20 20:31:08.174 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : <==        Row: 502e5dd5-3f55-11ee-a4b7-8629a6918075, 1, 502e5dd5-3f55-11ee-a4b7-8629a6918075, null, null, test01:1:70466829-3f50-11ee-82fb-8629a6918075, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075, null, 1, 0, 1, 0, 0, 1, null, , null, 2023-08-20 20:30:14.505, null, null, 0, 0, 0, 0, 0, 0, 0, 0, 0, null
2023-08-20 20:31:08.175 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : <==      Total: 1
2023-08-20 20:31:08.175 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.V.selectVariablesByTaskId    : ==>  Preparing: select * from ACT_RU_VARIABLE where TASK_ID_ = ?
2023-08-20 20:31:08.175 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.V.selectVariablesByTaskId    : ==> Parameters: 503080b9-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.176 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.V.selectVariablesByTaskId    : <==      Total: 0
2023-08-20 20:31:08.176 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByParentTaskId  : ==>  Preparing: select * from ACT_RU_TASK where PARENT_TASK_ID_ = ?
2023-08-20 20:31:08.176 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByParentTaskId  : ==> Parameters: 503080b9-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.177 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByParentTaskId  : <==      Total: 0
2023-08-20 20:31:08.177 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.I.selectIdentityLinksByTask  : ==>  Preparing: select * from ACT_RU_IDENTITYLINK where TASK_ID_ = ?
2023-08-20 20:31:08.177 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.I.selectIdentityLinksByTask  : ==> Parameters: 503080b9-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.177 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.I.selectIdentityLinksByTask  : <==      Total: 0
2023-08-20 20:31:08.178 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.H.selectHistoricTaskInstance : ==>  Preparing: select * from ACT_HI_TASKINST where ID_ = ?
2023-08-20 20:31:08.178 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.H.selectHistoricTaskInstance : ==> Parameters: 503080b9-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.178 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.H.selectHistoricTaskInstance : <==    Columns: ID_, PROC_DEF_ID_, TASK_DEF_KEY_, PROC_INST_ID_, EXECUTION_ID_, NAME_, PARENT_TASK_ID_, DESCRIPTION_, OWNER_, ASSIGNEE_, START_TIME_, CLAIM_TIME_, END_TIME_, DURATION_, DELETE_REASON_, PRIORITY_, DUE_DATE_, FORM_KEY_, CATEGORY_, TENANT_ID_
2023-08-20 20:31:08.178 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.H.selectHistoricTaskInstance : <==        Row: 503080b9-3f55-11ee-a4b7-8629a6918075, test01:1:70466829-3f50-11ee-82fb-8629a6918075, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794, 502e5dd5-3f55-11ee-a4b7-8629a6918075, 502e5dd6-3f55-11ee-a4b7-8629a6918075, 经理审批, null, null, null, null, 2023-08-20 20:30:14.519, null, null, null, null, 50, null, null, null,
2023-08-20 20:31:08.179 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.H.selectHistoricTaskInstance : <==      Total: 1
2023-08-20 20:31:08.179 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : ==>  Preparing: select E.*, S.PROC_INST_ID_ AS PARENT_PROC_INST_ID_ from ACT_RU_EXECUTION E LEFT OUTER JOIN ACT_RU_EXECUTION S ON E.SUPER_EXEC_ = S.ID_ where E.ID_ = ?
2023-08-20 20:31:08.179 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.180 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : <==    Columns: ID_, REV_, PROC_INST_ID_, BUSINESS_KEY_, PARENT_ID_, PROC_DEF_ID_, SUPER_EXEC_, ROOT_PROC_INST_ID_, ACT_ID_, IS_ACTIVE_, IS_CONCURRENT_, IS_SCOPE_, IS_EVENT_SCOPE_, IS_MI_ROOT_, SUSPENSION_STATE_, CACHED_ENT_STATE_, TENANT_ID_, NAME_, START_TIME_, START_USER_ID_, LOCK_TIME_, IS_COUNT_ENABLED_, EVT_SUBSCR_COUNT_, TASK_COUNT_, JOB_COUNT_, TIMER_JOB_COUNT_, SUSP_JOB_COUNT_, DEADLETTER_JOB_COUNT_, VAR_COUNT_, ID_LINK_COUNT_, PARENT_PROC_INST_ID_
2023-08-20 20:31:08.180 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : <==        Row: 502e5dd6-3f55-11ee-a4b7-8629a6918075, 1, 502e5dd5-3f55-11ee-a4b7-8629a6918075, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075, test01:1:70466829-3f50-11ee-82fb-8629a6918075, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794, 1, 0, 0, 0, 0, 1, null, , null, 2023-08-20 20:30:14.505, null, null, 0, 0, 0, 0, 0, 0, 0, 0, 0, null
2023-08-20 20:31:08.180 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.selectExecution            : <==      Total: 1
2023-08-20 20:31:08.180 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByExecutionId   : ==>  Preparing: select distinct T.* from ACT_RU_TASK T where T.EXECUTION_ID_ = ?
2023-08-20 20:31:08.180 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByExecutionId   : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.181 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByExecutionId   : <==    Columns: ID_, REV_, EXECUTION_ID_, PROC_INST_ID_, PROC_DEF_ID_, NAME_, PARENT_TASK_ID_, DESCRIPTION_, TASK_DEF_KEY_, OWNER_, ASSIGNEE_, DELEGATION_, PRIORITY_, CREATE_TIME_, DUE_DATE_, CATEGORY_, SUSPENSION_STATE_, TENANT_ID_, FORM_KEY_, CLAIM_TIME_
2023-08-20 20:31:08.181 TRACE 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByExecutionId   : <==        Row: 503080b9-3f55-11ee-a4b7-8629a6918075, 1, 502e5dd6-3f55-11ee-a4b7-8629a6918075, 502e5dd5-3f55-11ee-a4b7-8629a6918075, test01:1:70466829-3f50-11ee-82fb-8629a6918075, 经理审批, null, null, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794, null, null, null, 50, 2023-08-20 20:30:14.507, null, null, 1, , null, null
2023-08-20 20:31:08.181 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByExecutionId   : <==      Total: 1
2023-08-20 20:31:08.182 DEBUG 80145 --- [io-18080-exec-4] ActivityInstanceExecutionIdAndActivityId : ==>  Preparing: select * from ACT_HI_ACTINST RES where EXECUTION_ID_ = ? and ACT_ID_ = ? and END_TIME_ is null
2023-08-20 20:31:08.182 DEBUG 80145 --- [io-18080-exec-4] ActivityInstanceExecutionIdAndActivityId : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String), sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794(String)
2023-08-20 20:31:08.182 TRACE 80145 --- [io-18080-exec-4] ActivityInstanceExecutionIdAndActivityId : <==    Columns: ID_, PROC_DEF_ID_, PROC_INST_ID_, EXECUTION_ID_, ACT_ID_, TASK_ID_, CALL_PROC_INST_ID_, ACT_NAME_, ACT_TYPE_, ASSIGNEE_, START_TIME_, END_TIME_, DURATION_, DELETE_REASON_, TENANT_ID_
2023-08-20 20:31:08.182 TRACE 80145 --- [io-18080-exec-4] ActivityInstanceExecutionIdAndActivityId : <==        Row: 502eabf8-3f55-11ee-a4b7-8629a6918075, test01:1:70466829-3f50-11ee-82fb-8629a6918075, 502e5dd5-3f55-11ee-a4b7-8629a6918075, 502e5dd6-3f55-11ee-a4b7-8629a6918075, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794, 503080b9-3f55-11ee-a4b7-8629a6918075, null, 经理审批, userTask, null, 2023-08-20 20:30:14.507, null, null, null,
2023-08-20 20:31:08.183 DEBUG 80145 --- [io-18080-exec-4] ActivityInstanceExecutionIdAndActivityId : <==      Total: 1
2023-08-20 20:31:08.183 DEBUG 80145 --- [io-18080-exec-4] ActivityInstanceExecutionIdAndActivityId : ==>  Preparing: select * from ACT_HI_ACTINST RES where EXECUTION_ID_ = ? and ACT_ID_ = ? and END_TIME_ is null
2023-08-20 20:31:08.183 DEBUG 80145 --- [io-18080-exec-4] ActivityInstanceExecutionIdAndActivityId : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String), sid-566d983a-089b-4ce0-9935-4e422e72c219(String)
2023-08-20 20:31:08.184 DEBUG 80145 --- [io-18080-exec-4] ActivityInstanceExecutionIdAndActivityId : <==      Total: 0
2023-08-20 20:31:08.184 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.V.selectVariablesByExecutionId : ==>  Preparing: select * from ACT_RU_VARIABLE where EXECUTION_ID_ = ? and TASK_ID_ is null
2023-08-20 20:31:08.184 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.V.selectVariablesByExecutionId : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.184 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.V.selectVariablesByExecutionId : <==      Total: 0
2023-08-20 20:31:08.185 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.T.selectTimerJobsByExecutionId : ==>  Preparing: select * from ACT_RU_TIMER_JOB J where J.EXECUTION_ID_ = ?
2023-08-20 20:31:08.185 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.T.selectTimerJobsByExecutionId : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.185 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.T.selectTimerJobsByExecutionId : <==      Total: 0
2023-08-20 20:31:08.185 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.J.selectJobsByExecutionId    : ==>  Preparing: select * from ACT_RU_JOB J where J.EXECUTION_ID_ = ?
2023-08-20 20:31:08.185 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.J.selectJobsByExecutionId    : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.186 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.J.selectJobsByExecutionId    : <==      Total: 0
2023-08-20 20:31:08.186 DEBUG 80145 --- [io-18080-exec-4] i.p.e.S.selectSuspendedJobsByExecutionId : ==>  Preparing: select * from ACT_RU_SUSPENDED_JOB J where J.EXECUTION_ID_ = ?
2023-08-20 20:31:08.186 DEBUG 80145 --- [io-18080-exec-4] i.p.e.S.selectSuspendedJobsByExecutionId : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.187 DEBUG 80145 --- [io-18080-exec-4] i.p.e.S.selectSuspendedJobsByExecutionId : <==      Total: 0
2023-08-20 20:31:08.187 DEBUG 80145 --- [io-18080-exec-4] .p.e.D.selectDeadLetterJobsByExecutionId : ==>  Preparing: select * from ACT_RU_DEADLETTER_JOB J where J.EXECUTION_ID_ = ?
2023-08-20 20:31:08.187 DEBUG 80145 --- [io-18080-exec-4] .p.e.D.selectDeadLetterJobsByExecutionId : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.187 DEBUG 80145 --- [io-18080-exec-4] .p.e.D.selectDeadLetterJobsByExecutionId : <==      Total: 0
2023-08-20 20:31:08.188 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectEventSubscriptionsByExecution : ==>  Preparing: select * from ACT_RU_EVENT_SUBSCR where (EXECUTION_ID_ = ?)
2023-08-20 20:31:08.188 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectEventSubscriptionsByExecution : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.188 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectEventSubscriptionsByExecution : <==      Total: 0
2023-08-20 20:31:08.188 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectExecutionsByParentExecutionId : ==>  Preparing: select E.*, S.PROC_INST_ID_ AS PARENT_PROC_INST_ID_ from ACT_RU_EXECUTION E LEFT OUTER JOIN ACT_RU_EXECUTION S ON E.SUPER_EXEC_ = S.ID_ where E.PARENT_ID_ = ?
2023-08-20 20:31:08.188 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectExecutionsByParentExecutionId : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.189 TRACE 80145 --- [io-18080-exec-4] .e.E.selectExecutionsByParentExecutionId : <==    Columns: ID_, REV_, PROC_INST_ID_, BUSINESS_KEY_, PARENT_ID_, PROC_DEF_ID_, SUPER_EXEC_, ROOT_PROC_INST_ID_, ACT_ID_, IS_ACTIVE_, IS_CONCURRENT_, IS_SCOPE_, IS_EVENT_SCOPE_, IS_MI_ROOT_, SUSPENSION_STATE_, CACHED_ENT_STATE_, TENANT_ID_, NAME_, START_TIME_, START_USER_ID_, LOCK_TIME_, IS_COUNT_ENABLED_, EVT_SUBSCR_COUNT_, TASK_COUNT_, JOB_COUNT_, TIMER_JOB_COUNT_, SUSP_JOB_COUNT_, DEADLETTER_JOB_COUNT_, VAR_COUNT_, ID_LINK_COUNT_, PARENT_PROC_INST_ID_
2023-08-20 20:31:08.189 TRACE 80145 --- [io-18080-exec-4] .e.E.selectExecutionsByParentExecutionId : <==        Row: 502e5dd6-3f55-11ee-a4b7-8629a6918075, 1, 502e5dd5-3f55-11ee-a4b7-8629a6918075, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075, test01:1:70466829-3f50-11ee-82fb-8629a6918075, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794, 1, 0, 0, 0, 0, 1, null, , null, 2023-08-20 20:30:14.505, null, null, 0, 0, 0, 0, 0, 0, 0, 0, 0, null
2023-08-20 20:31:08.190 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectExecutionsByParentExecutionId : <==      Total: 1
2023-08-20 20:31:08.190 DEBUG 80145 --- [io-18080-exec-4] selectChildExecutionsByProcessInstanceId : ==>  Preparing: select E.*, S.PROC_INST_ID_ AS PARENT_PROC_INST_ID_ from ACT_RU_EXECUTION E LEFT OUTER JOIN ACT_RU_EXECUTION S ON E.SUPER_EXEC_ = S.ID_ where E.PROC_INST_ID_ = ? and E.PARENT_ID_ is not null
2023-08-20 20:31:08.190 DEBUG 80145 --- [io-18080-exec-4] selectChildExecutionsByProcessInstanceId : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.191 TRACE 80145 --- [io-18080-exec-4] selectChildExecutionsByProcessInstanceId : <==    Columns: ID_, REV_, PROC_INST_ID_, BUSINESS_KEY_, PARENT_ID_, PROC_DEF_ID_, SUPER_EXEC_, ROOT_PROC_INST_ID_, ACT_ID_, IS_ACTIVE_, IS_CONCURRENT_, IS_SCOPE_, IS_EVENT_SCOPE_, IS_MI_ROOT_, SUSPENSION_STATE_, CACHED_ENT_STATE_, TENANT_ID_, NAME_, START_TIME_, START_USER_ID_, LOCK_TIME_, IS_COUNT_ENABLED_, EVT_SUBSCR_COUNT_, TASK_COUNT_, JOB_COUNT_, TIMER_JOB_COUNT_, SUSP_JOB_COUNT_, DEADLETTER_JOB_COUNT_, VAR_COUNT_, ID_LINK_COUNT_, PARENT_PROC_INST_ID_
2023-08-20 20:31:08.191 TRACE 80145 --- [io-18080-exec-4] selectChildExecutionsByProcessInstanceId : <==        Row: 502e5dd6-3f55-11ee-a4b7-8629a6918075, 1, 502e5dd5-3f55-11ee-a4b7-8629a6918075, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075, test01:1:70466829-3f50-11ee-82fb-8629a6918075, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794, 1, 0, 0, 0, 0, 1, null, , null, 2023-08-20 20:30:14.505, null, null, 0, 0, 0, 0, 0, 0, 0, 0, 0, null
2023-08-20 20:31:08.191 DEBUG 80145 --- [io-18080-exec-4] selectChildExecutionsByProcessInstanceId : <==      Total: 1
2023-08-20 20:31:08.192 DEBUG 80145 --- [io-18080-exec-4] lectSubProcessInstanceBySuperExecutionId : ==>  Preparing: select * from ACT_RU_EXECUTION where SUPER_EXEC_ = ?
2023-08-20 20:31:08.192 DEBUG 80145 --- [io-18080-exec-4] lectSubProcessInstanceBySuperExecutionId : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.193 DEBUG 80145 --- [io-18080-exec-4] lectSubProcessInstanceBySuperExecutionId : <==      Total: 0
2023-08-20 20:31:08.193 DEBUG 80145 --- [io-18080-exec-4] e.I.selectIdentityLinksByProcessInstance : ==>  Preparing: select * from ACT_RU_IDENTITYLINK where PROC_INST_ID_ = ?
2023-08-20 20:31:08.193 DEBUG 80145 --- [io-18080-exec-4] e.I.selectIdentityLinksByProcessInstance : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.194 DEBUG 80145 --- [io-18080-exec-4] e.I.selectIdentityLinksByProcessInstance : <==      Total: 0
2023-08-20 20:31:08.194 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.V.selectVariablesByExecutionId : ==>  Preparing: select * from ACT_RU_VARIABLE where EXECUTION_ID_ = ? and TASK_ID_ is null
2023-08-20 20:31:08.194 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.V.selectVariablesByExecutionId : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.195 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.V.selectVariablesByExecutionId : <==      Total: 0
2023-08-20 20:31:08.195 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByExecutionId   : ==>  Preparing: select distinct T.* from ACT_RU_TASK T where T.EXECUTION_ID_ = ?
2023-08-20 20:31:08.195 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByExecutionId   : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.196 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.T.selectTasksByExecutionId   : <==      Total: 0
2023-08-20 20:31:08.196 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.T.selectTimerJobsByExecutionId : ==>  Preparing: select * from ACT_RU_TIMER_JOB J where J.EXECUTION_ID_ = ?
2023-08-20 20:31:08.196 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.T.selectTimerJobsByExecutionId : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.197 DEBUG 80145 --- [io-18080-exec-4] a.e.i.p.e.T.selectTimerJobsByExecutionId : <==      Total: 0
2023-08-20 20:31:08.198 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.J.selectJobsByExecutionId    : ==>  Preparing: select * from ACT_RU_JOB J where J.EXECUTION_ID_ = ?
2023-08-20 20:31:08.198 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.J.selectJobsByExecutionId    : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.199 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.J.selectJobsByExecutionId    : <==      Total: 0
2023-08-20 20:31:08.199 DEBUG 80145 --- [io-18080-exec-4] i.p.e.S.selectSuspendedJobsByExecutionId : ==>  Preparing: select * from ACT_RU_SUSPENDED_JOB J where J.EXECUTION_ID_ = ?
2023-08-20 20:31:08.199 DEBUG 80145 --- [io-18080-exec-4] i.p.e.S.selectSuspendedJobsByExecutionId : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.200 DEBUG 80145 --- [io-18080-exec-4] i.p.e.S.selectSuspendedJobsByExecutionId : <==      Total: 0
2023-08-20 20:31:08.200 DEBUG 80145 --- [io-18080-exec-4] .p.e.D.selectDeadLetterJobsByExecutionId : ==>  Preparing: select * from ACT_RU_DEADLETTER_JOB J where J.EXECUTION_ID_ = ?
2023-08-20 20:31:08.200 DEBUG 80145 --- [io-18080-exec-4] .p.e.D.selectDeadLetterJobsByExecutionId : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.200 DEBUG 80145 --- [io-18080-exec-4] .p.e.D.selectDeadLetterJobsByExecutionId : <==      Total: 0
2023-08-20 20:31:08.200 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectEventSubscriptionsByExecution : ==>  Preparing: select * from ACT_RU_EVENT_SUBSCR where (EXECUTION_ID_ = ?)
2023-08-20 20:31:08.201 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectEventSubscriptionsByExecution : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.201 DEBUG 80145 --- [io-18080-exec-4] .e.E.selectEventSubscriptionsByExecution : <==      Total: 0
2023-08-20 20:31:08.201 DEBUG 80145 --- [io-18080-exec-4] .e.i.p.e.H.selectHistoricProcessInstance : ==>  Preparing: select * from ACT_HI_PROCINST where PROC_INST_ID_ = ?
2023-08-20 20:31:08.201 DEBUG 80145 --- [io-18080-exec-4] .e.i.p.e.H.selectHistoricProcessInstance : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.202 TRACE 80145 --- [io-18080-exec-4] .e.i.p.e.H.selectHistoricProcessInstance : <==    Columns: ID_, PROC_INST_ID_, BUSINESS_KEY_, PROC_DEF_ID_, START_TIME_, END_TIME_, DURATION_, START_USER_ID_, START_ACT_ID_, END_ACT_ID_, SUPER_PROCESS_INSTANCE_ID_, DELETE_REASON_, TENANT_ID_, NAME_
2023-08-20 20:31:08.202 TRACE 80145 --- [io-18080-exec-4] .e.i.p.e.H.selectHistoricProcessInstance : <==        Row: 502e5dd5-3f55-11ee-a4b7-8629a6918075, 502e5dd5-3f55-11ee-a4b7-8629a6918075, null, test01:1:70466829-3f50-11ee-82fb-8629a6918075, 2023-08-20 20:30:14.505, null, null, null, sid-7bcd1c8f-20cb-4c36-9756-7c380d1158d0, null, null, null, , null
2023-08-20 20:31:08.202 DEBUG 80145 --- [io-18080-exec-4] .e.i.p.e.H.selectHistoricProcessInstance : <==      Total: 1
2023-08-20 20:31:08.203 DEBUG 80145 --- [io-18080-exec-4] e.i.p.e.H.insertHistoricActivityInstance : ==>  Preparing: insert into ACT_HI_ACTINST ( ID_, PROC_DEF_ID_, PROC_INST_ID_, EXECUTION_ID_, ACT_ID_, TASK_ID_, CALL_PROC_INST_ID_, ACT_NAME_, ACT_TYPE_, ASSIGNEE_, START_TIME_, END_TIME_, DURATION_, DELETE_REASON_, TENANT_ID_ ) values ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )
2023-08-20 20:31:08.204 DEBUG 80145 --- [io-18080-exec-4] e.i.p.e.H.insertHistoricActivityInstance : ==> Parameters: 702cfaba-3f55-11ee-a4b7-8629a6918075(String), test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), 502e5dd5-3f55-11ee-a4b7-8629a6918075(String), 502e5dd6-3f55-11ee-a4b7-8629a6918075(String), sid-566d983a-089b-4ce0-9935-4e422e72c219(String), null, null, 结束(String), endEvent(String), null, 2023-08-20 20:31:08.183(Timestamp), 2023-08-20 20:31:08.183(Timestamp), 0(Long), null, (String)
2023-08-20 20:31:08.205 DEBUG 80145 --- [io-18080-exec-4] e.i.p.e.H.insertHistoricActivityInstance : <==    Updates: 1
2023-08-20 20:31:08.205 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.H.updateHistoricTaskInstance : ==>  Preparing: update ACT_HI_TASKINST set PROC_DEF_ID_ = ?, EXECUTION_ID_ = ?, NAME_ = ?, PARENT_TASK_ID_ = ?, DESCRIPTION_ = ?, OWNER_ = ?, ASSIGNEE_ = ?, CLAIM_TIME_ = ?, END_TIME_ = ?, DURATION_ = ?, DELETE_REASON_ = ?, TASK_DEF_KEY_ = ?, FORM_KEY_ = ?, PRIORITY_ = ?, DUE_DATE_ = ?, CATEGORY_ = ? where ID_ = ?
2023-08-20 20:31:08.205 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.H.updateHistoricTaskInstance : ==> Parameters: test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), 502e5dd6-3f55-11ee-a4b7-8629a6918075(String), 经理审批(String), null, null, null, null, null, 2023-08-20 20:31:08.179(Timestamp), 53660(Long), null, sid-26ae1c3f-b024-49d3-bb5c-4c86a1033794(String), null, 50(Integer), null, null, 503080b9-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.206 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.H.updateHistoricTaskInstance : <==    Updates: 1
2023-08-20 20:31:08.207 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.updateExecution            : ==>  Preparing: update ACT_RU_EXECUTION set REV_ = ?, BUSINESS_KEY_ = ?, PROC_DEF_ID_ = ?, ACT_ID_ = ?, IS_ACTIVE_ = ?, IS_CONCURRENT_ = ?, IS_SCOPE_ = ?, IS_EVENT_SCOPE_ = ?, IS_MI_ROOT_ = ?, PARENT_ID_ = ?, SUPER_EXEC_ = ?, ROOT_PROC_INST_ID_ = ?, SUSPENSION_STATE_ = ?, NAME_ = ?, IS_COUNT_ENABLED_ = ?, EVT_SUBSCR_COUNT_ = ?, TASK_COUNT_ = ?, JOB_COUNT_ = ?, TIMER_JOB_COUNT_ = ?, SUSP_JOB_COUNT_ = ?, DEADLETTER_JOB_COUNT_ = ?, VAR_COUNT_ = ?, ID_LINK_COUNT_ = ? where ID_ = ? and REV_ = ?
2023-08-20 20:31:08.207 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.updateExecution            : ==> Parameters: 2(Integer), null, test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), sid-566d983a-089b-4ce0-9935-4e422e72c219(String), false(Boolean), false(Boolean), false(Boolean), false(Boolean), false(Boolean), 502e5dd5-3f55-11ee-a4b7-8629a6918075(String), null, 502e5dd5-3f55-11ee-a4b7-8629a6918075(String), 1(Integer), null, false(Boolean), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 502e5dd6-3f55-11ee-a4b7-8629a6918075(String), 1(Integer)
2023-08-20 20:31:08.208 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.updateExecution            : <==    Updates: 1
2023-08-20 20:31:08.208 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.updateExecution            : ==>  Preparing: update ACT_RU_EXECUTION set REV_ = ?, BUSINESS_KEY_ = ?, PROC_DEF_ID_ = ?, ACT_ID_ = ?, IS_ACTIVE_ = ?, IS_CONCURRENT_ = ?, IS_SCOPE_ = ?, IS_EVENT_SCOPE_ = ?, IS_MI_ROOT_ = ?, PARENT_ID_ = ?, SUPER_EXEC_ = ?, ROOT_PROC_INST_ID_ = ?, SUSPENSION_STATE_ = ?, NAME_ = ?, IS_COUNT_ENABLED_ = ?, EVT_SUBSCR_COUNT_ = ?, TASK_COUNT_ = ?, JOB_COUNT_ = ?, TIMER_JOB_COUNT_ = ?, SUSP_JOB_COUNT_ = ?, DEADLETTER_JOB_COUNT_ = ?, VAR_COUNT_ = ?, ID_LINK_COUNT_ = ? where ID_ = ? and REV_ = ?
2023-08-20 20:31:08.209 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.updateExecution            : ==> Parameters: 2(Integer), null, test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), null, false(Boolean), false(Boolean), true(Boolean), false(Boolean), false(Boolean), null, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075(String), 1(Integer), null, false(Boolean), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 0(Integer), 502e5dd5-3f55-11ee-a4b7-8629a6918075(String), 1(Integer)
2023-08-20 20:31:08.209 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.updateExecution            : <==    Updates: 1
2023-08-20 20:31:08.210 DEBUG 80145 --- [io-18080-exec-4] .e.i.p.e.H.updateHistoricProcessInstance : ==>  Preparing: update ACT_HI_PROCINST set PROC_DEF_ID_ = ?, BUSINESS_KEY_ = ?, START_TIME_ = ?, END_TIME_ = ?, DURATION_ = ?, END_ACT_ID_ = ?, DELETE_REASON_ = ?, NAME_ = ? where ID_ = ?
2023-08-20 20:31:08.210 DEBUG 80145 --- [io-18080-exec-4] .e.i.p.e.H.updateHistoricProcessInstance : ==> Parameters: test01:1:70466829-3f50-11ee-82fb-8629a6918075(String), null, 2023-08-20 20:30:14.505(Timestamp), 2023-08-20 20:31:08.202(Timestamp), 53697(Long), sid-566d983a-089b-4ce0-9935-4e422e72c219(String), null, null, 502e5dd5-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.211 DEBUG 80145 --- [io-18080-exec-4] .e.i.p.e.H.updateHistoricProcessInstance : <==    Updates: 1
2023-08-20 20:31:08.211 DEBUG 80145 --- [io-18080-exec-4] e.i.p.e.H.updateHistoricActivityInstance : ==>  Preparing: update ACT_HI_ACTINST set EXECUTION_ID_ = ?, ASSIGNEE_ = ?, END_TIME_ = ?, DURATION_ = ?, DELETE_REASON_ = ? where ID_ = ?
2023-08-20 20:31:08.211 DEBUG 80145 --- [io-18080-exec-4] e.i.p.e.H.updateHistoricActivityInstance : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String), null, 2023-08-20 20:31:08.183(Timestamp), 53676(Long), null, 502eabf8-3f55-11ee-a4b7-8629a6918075(String)
2023-08-20 20:31:08.212 DEBUG 80145 --- [io-18080-exec-4] e.i.p.e.H.updateHistoricActivityInstance : <==    Updates: 1
2023-08-20 20:31:08.212 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.TaskEntityImpl.deleteTask    : ==>  Preparing: delete from ACT_RU_TASK where ID_ = ? and REV_ = ?
2023-08-20 20:31:08.212 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.TaskEntityImpl.deleteTask    : ==> Parameters: 503080b9-3f55-11ee-a4b7-8629a6918075(String), 1(Integer)
2023-08-20 20:31:08.213 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.TaskEntityImpl.deleteTask    : <==    Updates: 1
2023-08-20 20:31:08.213 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.deleteExecution            : ==>  Preparing: delete from ACT_RU_EXECUTION where ID_ = ? and REV_ = ?
2023-08-20 20:31:08.213 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.deleteExecution            : ==> Parameters: 502e5dd6-3f55-11ee-a4b7-8629a6918075(String), 2(Integer)
2023-08-20 20:31:08.214 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.deleteExecution            : <==    Updates: 1
2023-08-20 20:31:08.214 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.deleteExecution            : ==>  Preparing: delete from ACT_RU_EXECUTION where ID_ = ? and REV_ = ?
2023-08-20 20:31:08.214 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.deleteExecution            : ==> Parameters: 502e5dd5-3f55-11ee-a4b7-8629a6918075(String), 2(Integer)
2023-08-20 20:31:08.215 DEBUG 80145 --- [io-18080-exec-4] o.a.e.i.p.e.E.deleteExecution            : <==    Updates: 1
```

```text
insert into ACT_HI_ACTINST
delete from ACT_RU_TASK
delete from ACT_RU_EXECUTION
```

# 查询历史数据

## 历史流程实例

```text
    // 历史处理接口
    @Autowired
    HistoryService historyService;

    @ApiOperation("查询历史流程实例")
    @GetMapping("queryHistoryProcessInstance")
    public ReturnData queryHistoryProcessInstance() {
        //也可以设置查询条件，自行查询API
        List<HistoricProcessInstance> list = historyService.createHistoricProcessInstanceQuery().list();
        log.info("查询历史流程实例 {}", list);
        return ReturnData.buildSuccess(list.toString());
    }
```

![](./images/images/img_017_cddc6190a42e.gif)

```text
select
    distinct RES.* ,
    DEF.KEY_ as PROC_DEF_KEY_,
    DEF.NAME_ as PROC_DEF_NAME_,
    DEF.VERSION_ as PROC_DEF_VERSION_,
    DEF.DEPLOYMENT_ID_ as DEPLOYMENT_ID_
from
    ACT_HI_PROCINST RES
left outer join
    ACT_RE_PROCDEF DEF
        on RES.PROC_DEF_ID_ = DEF.ID_
order by
    RES.ID_ asc LIMIT 2147483647 OFFSET 0;
```

![](./images/images/img_018_8e07bf9f26f7.png)

## 历史任务

```text
    // 历史处理接口
    @Autowired
    HistoryService historyService;

    @ApiOperation("查询历史任务")
    @GetMapping("queryHistoryTask")
    public ReturnData queryHistoryTask() {
        //也可以设置查询条件，自行查询API
        List<HistoricTaskInstance> list = historyService.createHistoricTaskInstanceQuery().list();
        log.info("查询历史任务 {}", list);
        return ReturnData.buildSuccess(list.toString());
    }
```

![](./images/images/img_019_46c833ae02cd.gif)

```text
select
    distinct RES.*
from
    ACT_HI_TASKINST RES
order by
    RES.ID_ asc LIMIT 2147483647 OFFSET 0;
```

![](./images/images/img_020_b04cb20b6cb6.png)

## 历史活动实例

```text
    // 历史处理接口
    @Autowired
    HistoryService historyService;

    @ApiOperation("查看历史活动流程实例")
    @GetMapping("queryActivityInstance")
    public ReturnData queryActivityInstance() {
        List<HistoricActivityInstance> list = historyService.createHistoricActivityInstanceQuery().list();
        log.info("查看历史活动流程实例 {}", list);
        return ReturnData.buildSuccess(list.toString());
    }
```

![](./images/images/img_021_0feed7d14fe2.gif)

```text
select
    RES.*
from
    ACT_HI_ACTINST RES
order by
    RES.ID_ asc LIMIT 2147483647 OFFSET 0;
```

![](./images/images/img_022_86dd52ddc1cc.png)

# 任务代办人

**Assignee**指定办理人模式：即设置办理人，就是设置Assignee。Assignee 受让人; 受托人，代理人; 被指定人;办理人只能指定一个人，不能使用逗号分隔。

![](./images/images/img_023_6f755c3a9062.png)

## 操作步骤

1. 画流程图
2. 部署流程
3. 启动流程
4. 查询代办人代办任务

![](./images/images/img_024_bb0d0bdf60ac.gif)

```text
    // 任务处理接口
    @Autowired
    TaskService taskService;

    @ApiOperation("根据代办人查询任务")
    @GetMapping("queryByAssigneeTask")
    public ReturnData queryByAssigneeTask(
            @ApiParam(value = "代办人", required = true) String assignee
    ) {
        List<Task> taskList = taskService.createTaskQuery()
                //代办人姓名
                .taskAssignee(assignee)
                //活动状态
                .active()
                .list();
        log.info("根据代办人查询任务 {}", taskList);
        return ReturnData.buildSuccess(taskList.toString());
    }
```

![](./images/images/img_025_f506f7659c26.gif)

```text
select
    distinct RES.*
from
    ACT_RU_TASK RES
WHERE
    RES.ASSIGNEE_ = '陈彦斌'
    and RES.SUSPENSION_STATE_ = 1
order by
    RES.ID_ asc LIMIT 2147483647 OFFSET 0;
```

```text
根据代办人查询任务 [Task[id=0b8b10c2-3f5f-11ee-89f9-8629a6918075, name=经理审批]]
```

## 修改某个任务节点审批人【重要】

　　eg：公司内部某个审批节点当事人，由于个人原因离职，导致流程中的节点，没法进行下去，此时需要使用该功能！！！！！！！！！

```text
    // 任务处理接口
    @Autowired
    TaskService taskService;

    @ApiOperation("按任务id更新代办人")
    @GetMapping("updateAssigneeByTaskId")
    public ReturnData updateAssigneeByTaskId(
            @ApiParam(value = "任务id", required = true) String taskId,
            @ApiParam(value = "新代办人", required = true) String assignee
    ) {

        Task task = taskService.createTaskQuery().taskId(taskId).singleResult();
        if (task == null) {
            return ReturnData.buildError("任务不存在");
        }
        //更新当前任务的代办人
        taskService.setAssignee(taskId, assignee);
        return ReturnData.buildSuccess("更新成功");
    }
```

## 动态设置任务审批人【重要】

　　eg：实际业务中，不太可能把assignee写硬编码，一般都会写成一个变量，占位符形式，如何设置呢，如图

![](./images/images/img_026_044fd058d53d.png)

- 启动流程时，需要传所有流程节点中的占位符

```text
        //流程节点中变量，替换占位符
        Map<String, Object> variablesMap = new HashMap<>();
        variablesMap.put("userName","老陈同学");
        //通过流程定义ID启动一个流程实例
        ProcessInstance processInstance = runtimeService.startProcessInstanceById(processDefinitionId, variablesMap);
```

# 添加审批人意见

```text
    @ApiOperation("添加审批人意见")
    @GetMapping("addComment")
    public ReturnData addComment(
            @ApiParam(value = "任务id", required = true) String taskId,
            @ApiParam(value = "流程实例id", required = true) String processInstanceId,
            @ApiParam(value = "意见内容", required = true) String message
    ) {
        Task task = taskService.createTaskQuery()
                .taskId(taskId)
                .processInstanceId(processInstanceId)
                .singleResult();
        if (task == null) {
            return ReturnData.buildError("任务不存在");
        }
        taskService.addComment(taskId, processInstanceId, message);
        return ReturnData.buildSuccess("添加成功");
    }
```

![](./images/images/img_027_6673c3dbb394.gif)

```text
insert into ACT_HI_COMMENT
```

## 查询审批意见

```text
    // 任务处理接口
    @Autowired
    TaskService taskService;

    @ApiOperation("查询个人审批意见")
    @GetMapping("queryComment")
    public ReturnData queryComment(
            @ApiParam(value = "任务id") String taskId
    ) {
        //注意，这里也可以使用type做搜索，通过添加意见的第三个参数，指定用户id
        //taskService.addComment("任务id", "流程实例id", "自定义变量type，可以用作用户id", "意见");
        List<Comment> taskComments = taskService.getTaskComments(taskId);
        //taskService.getTaskComments(taskId,"自定义变量type，可以用作用户id");
        log.info("查询个人审批意见 {}", taskComments);
        return ReturnData.buildSuccess(taskComments.toString());
    }
```

# 候选人拾取任务 & 完成任务

## 候选人 CandidateUsers

　　当任务可以被多人处理的时候，可能会发生并发，所以添加候选人，让候选人去获取任务，之后就变成这个候选人的任务了。

### 画候选人流程图

![](./images/images/img_028_5599ced024ac.gif)

![](./images/images/img_029_f3aa1485a42b.png)

## 操作步骤

　　为了节省时间，以下不在演示

- 保存png图片
- 压缩成xxx.zip
- 部署zip
- 开启任务
- 查询候选人任务
- 拾取任务
- 完成任务

### 查询候选人任务

```text
    // 任务处理接口
    @Autowired
    TaskService taskService;

    @ApiOperation("根据候选人查询任务")
    @GetMapping("queryTaskByCandidateUser")
    public ReturnData queryTaskByCandidateUser(
            @ApiParam(value = "候选人名称") String userName
    ){
        List<Task> taskList = taskService.createTaskQuery()
                //候选人名称
                .taskCandidateUser(userName)
                .list();
        return ReturnData.buildSuccess(taskList);
    }
```

### 拾取任务

```text
    // 任务处理接口
    @Autowired
    TaskService taskService;

    /**
     * 拾取任务，拾取后的任务，该候选人才可以完成任务
     *
     * @param taskId   任务id
     * @param userName 候选人名称
     * @return
     */
    @ApiOperation("候选人拾取任务，拾取后的任务，候选人才可以完成")
    @GetMapping("claimTask")
    public ReturnData claimTask(
            @ApiParam(value = "任务id") String taskId,
            @ApiParam(value = "候选人名称") String userName
    ) {
        Task task = taskService.createTaskQuery()
                //任务id
                .taskId(taskId)
                //候选人名称
                .taskCandidateUser(userName)
                .singleResult();
        if (task == null) {
            return ReturnData.buildError("任务不存在");
        }
        //拾取任务
        taskService.claim(taskId, userName);
        return ReturnData.buildSuccess("拾取任务成功");
    }
```

# 流程监听器ExecutionListener【重点】

任务监听器只能监听UserTask，流程监听器用在流程的不同的阶段上：

- 开始事件和结束事件的开始和结束
- 经过输出顺序流
- 流程活动的开始和结束
- 流程网关的开始和结束
- 中间事假的开始和结束

## 画执行器流程图

![](./images/images/img_030_cfe8121a9635.png)

![](./images/images/img_031_e4b4564b8eb2.png)

## 后续流程

- 保存xxx.png
- 压缩xxx.zip
- 部署xxx.zip
- 启动xxx.zip

## 执行器监听类

**需要实现ExecutionListener接口**

```text
package com.ybchen.listener;

import lombok.extern.slf4j.Slf4j;
import org.activiti.engine.delegate.DelegateExecution;
import org.activiti.engine.delegate.ExecutionListener;

/**
 * @description: Activiti 经理审批监听器
 * @author: Alex
 * @create: 2023-08-23 22:26
 */
@Slf4j
public class MangerExecutionListener implements ExecutionListener {

    @Override
    public void notify(DelegateExecution execution) {
        log.error("\r\n *****************MangerExecutionListener流程监听器*****************" +
                        "\r\n execution.getCurrentFlowElement().getId()：【{}】," +
                        "\r\n execution.getCurrentFlowElement().getName():【{}】，" +
                        "\r\n execution.getEventName()：【{}】，" +
                        "\r\n execution.getProcessDefinitionId()：【{}】，" +
                        "\r\n execution.getProcessInstanceId()：【{}】，" +
                        "\r\n execution：【{}】",
                execution.getCurrentFlowElement().getId(),
                execution.getCurrentFlowElement().getName(),
                execution.getEventName(),
                execution.getProcessDefinitionId(),
                execution.getProcessInstanceId(),
                execution
        );
    }
}
```

## 演示

![](./images/images/img_032_6d761ceac495.gif)

# 流程变量【重点】

　　流程变量就是if(条件)中使用到的变量用于参与条件表达式的计算。

## 画流程图

![](./images/images/img_033_8c676a1ea670.gif)

![](./images/images/img_034_62bd662f9f08.png)

## 操作步骤

- 保存xxx.png
- 压缩xxx.zip
- 部署xxx.zip
- 开启流程（**设置流程变量**）
- 完成审批

## 启动时设置全局变量day

```text
    //提供对流程定义和部署存储库的访问服务
    @Autowired
    RepositoryService repositoryService;
    //运行时的接口
    @Autowired
    RuntimeService runtimeService;

    @ApiOperation("发起流程")
    @GetMapping("startProcess")
    public ReturnData startProcess(
            @ApiParam(value = "流程定义id", required = true) String processDefinitionId
    ) {
        log.info("发起流程，processDefinitionId：{}", processDefinitionId);
        List<ProcessDefinition> list = repositoryService.createProcessDefinitionQuery().processDefinitionId(processDefinitionId).list();
        if (list.size() != 1) {
            return ReturnData.buildError("流程定义不存在");
        }
        //流程节点中变量，替换占位符
        Map<String, Object> variablesMap = new HashMap<>();
        //流程变量day
        variablesMap.put("day", "8");
        //通过流程定义ID启动一个流程实例
        ProcessInstance processInstance = runtimeService.startProcessInstanceById(processDefinitionId, variablesMap);
        log.info("流程实例：{}", processInstance);
        return ReturnData.buildSuccess("发起成功 " + processInstance);
    }
```

## 演示

![](./images/images/img_035_b31cb5226dde.gif)

![](./images/images/img_036_a369ee6d9c74.gif)

![](./images/images/img_004_8f900a89c634.gif)
![](./images/images/img_005_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:activiti="http://activiti.org/bpmn" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" typeLanguage="http://www.w3.org/2001/XMLSchema" expressionLanguage="http://www.w3.org/1999/XPath" targetNamespace="http://www.activiti.org/processdef">
  <process id="test05" name="test05" isExecutable="true">
    <startEvent id="sid-9af1bcbe-1166-4edf-b3b9-e667db8b5630"/>
    <userTask id="sid-28d932f0-521b-45b4-bbbf-8b0dbcca367f" name="请假申请"/>
    <userTask id="sid-822fb684-6af8-497b-a63b-31195792eb4e" name="经理审批"/>
    <userTask id="sid-188f743b-8218-4992-bec3-fb3c7583bac9" name="CEO审批"/>
    <userTask id="sid-f0cfc954-4633-4db1-a89a-fd4435eae38b" name="老板审批"/>
    <endEvent id="sid-e9083353-168b-4e2e-8b34-cf2ef5e276ef" name="结束"/>
    <sequenceFlow id="sid-ccd34aac-4437-4926-a805-e7300fe1455d" sourceRef="sid-9af1bcbe-1166-4edf-b3b9-e667db8b5630" targetRef="sid-28d932f0-521b-45b4-bbbf-8b0dbcca367f"/>
    <sequenceFlow id="sid-6b052bb3-4ce3-4477-b344-af050dcbd328" sourceRef="sid-28d932f0-521b-45b4-bbbf-8b0dbcca367f" targetRef="sid-822fb684-6af8-497b-a63b-31195792eb4e" name="5天以下">
      <conditionExpression>${day&lt;5}</conditionExpression>
    </sequenceFlow>
    <sequenceFlow id="sid-82f19739-09bf-4e54-950c-c61b7f2b1f0e" sourceRef="sid-28d932f0-521b-45b4-bbbf-8b0dbcca367f" targetRef="sid-188f743b-8218-4992-bec3-fb3c7583bac9" name="5天到10天">
      <conditionExpression>${day&gt;=5 &amp;&amp; day&lt;=10}</conditionExpression>
    </sequenceFlow>
    <sequenceFlow id="sid-98670c9f-e136-4858-8487-e78db03f15a2" sourceRef="sid-28d932f0-521b-45b4-bbbf-8b0dbcca367f" targetRef="sid-f0cfc954-4633-4db1-a89a-fd4435eae38b" name="10天以上">
      <conditionExpression>${day&gt;10}</conditionExpression>
    </sequenceFlow>
    <sequenceFlow id="sid-96dbc59f-922c-44b8-ae35-22bda9befa31" sourceRef="sid-822fb684-6af8-497b-a63b-31195792eb4e" targetRef="sid-e9083353-168b-4e2e-8b34-cf2ef5e276ef"/>
    <sequenceFlow id="sid-b8e0cf5a-3d6a-4596-9e13-712d592908ed" sourceRef="sid-188f743b-8218-4992-bec3-fb3c7583bac9" targetRef="sid-e9083353-168b-4e2e-8b34-cf2ef5e276ef"/>
    <sequenceFlow id="sid-c16e6f68-322d-4918-8d41-ae9f67dd62db" sourceRef="sid-f0cfc954-4633-4db1-a89a-fd4435eae38b" targetRef="sid-e9083353-168b-4e2e-8b34-cf2ef5e276ef"/>
  </process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_test05">
    <bpmndi:BPMNPlane bpmnElement="test05" id="BPMNPlane_test05">
      <bpmndi:BPMNShape id="shape-99a08710-b856-431c-9bd1-bc536da39a40" bpmnElement="sid-9af1bcbe-1166-4edf-b3b9-e667db8b5630">
        <omgdc:Bounds x="-175.0" y="-32.5" width="30.0" height="30.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-e046609d-16cb-45f2-8904-ff5d20dace8f" bpmnElement="sid-28d932f0-521b-45b4-bbbf-8b0dbcca367f">
        <omgdc:Bounds x="-60.0" y="-45.0" width="60.000004" height="55.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-a6629b15-e1fa-416e-a669-ada0e1f8d928" bpmnElement="sid-822fb684-6af8-497b-a63b-31195792eb4e">
        <omgdc:Bounds x="95.0" y="-120.0" width="75.0" height="50.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="sid-c973c137-567a-42ac-88e3-c59d714e8727" bpmnElement="sid-188f743b-8218-4992-bec3-fb3c7583bac9">
        <omgdc:Bounds x="95.0" y="-42.5" width="75.0" height="50.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="sid-9196f27f-33ad-4553-b6e7-a346630bdf71" bpmnElement="sid-f0cfc954-4633-4db1-a89a-fd4435eae38b">
        <omgdc:Bounds x="95.0" y="64.75" width="75.0" height="50.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-c22f75c2-6d79-4170-94d4-4f19283649a8" bpmnElement="sid-e9083353-168b-4e2e-8b34-cf2ef5e276ef">
        <omgdc:Bounds x="290.0" y="-32.5" width="30.0" height="30.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="edge-945c6902-078b-41ad-bdb4-92c668c9aef7" bpmnElement="sid-ccd34aac-4437-4926-a805-e7300fe1455d">
        <omgdi:waypoint x="-145.0" y="-17.5"/>
        <omgdi:waypoint x="-60.0" y="-17.5"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-01f80fb1-9d06-4e04-9e53-364b3d652044" bpmnElement="sid-6b052bb3-4ce3-4477-b344-af050dcbd328">
        <omgdi:waypoint x="-29.999996" y="-45.0"/>
        <omgdi:waypoint x="-29.999996" y="-95.0"/>
        <omgdi:waypoint x="95.0" y="-95.0"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-2089777f-3235-4e40-a96b-0875b83bc440" bpmnElement="sid-82f19739-09bf-4e54-950c-c61b7f2b1f0e">
        <omgdi:waypoint x="3.8146973E-6" y="-17.5"/>
        <omgdi:waypoint x="95.0" y="-17.5"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-1a22b955-c3d1-4219-b480-1ac7d798a5e7" bpmnElement="sid-98670c9f-e136-4858-8487-e78db03f15a2">
        <omgdi:waypoint x="-29.999996" y="10.0"/>
        <omgdi:waypoint x="-29.999992" y="89.75"/>
        <omgdi:waypoint x="95.0" y="89.75"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-5ad4a187-18cc-4fe1-8a7b-282c5b56206e" bpmnElement="sid-96dbc59f-922c-44b8-ae35-22bda9befa31">
        <omgdi:waypoint x="170.0" y="-82.5"/>
        <omgdi:waypoint x="290.0" y="-25.0"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-8ee89227-cad2-4ffb-b252-ecc911305e26" bpmnElement="sid-b8e0cf5a-3d6a-4596-9e13-712d592908ed">
        <omgdi:waypoint x="170.0" y="-17.5"/>
        <omgdi:waypoint x="290.0" y="-17.5"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-9a9aece1-2574-4328-a368-6785da193b9c" bpmnElement="sid-c16e6f68-322d-4918-8d41-ae9f67dd62db">
        <omgdi:waypoint x="170.0" y="77.25"/>
        <omgdi:waypoint x="290.0" y="-10.0"/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</definitions>
```

test05.bpmn20.xml

# ExclusiveGateway 排它网关【重要】

　　所谓网关就是条件分支语句if() else if () ，排它网关会执行所有条件找到一个为true的执行，如果有多个条件为true那么会执行优先定义的（Id较小的那个UserTask），如果条件都为false则抛出异常。

排它网关和直接在连线上设置条件的区别：

- 条件分支不满条件抛异常，如果都满足都执行。
- 排它网关不满足条件抛异常，如果都满足只执行Id较小的任务（即先绘制的任务）。

```text
if(day < 3) {

} else if (day > 3) {

} else {
    throw new Exception();
}
```

- day大于等于3天走部门经理审批，大于小于3天直接走人事审批。
- 修改条件，分别改为day>=3和day>=2，传值day=3，抛异常ActivitiException

## 画流程图

![](./images/images/img_037_75946543d7ce.gif)

## 操作步骤

- 保存xxx.png
- 压缩xxx.zip
- 部署xxx.zip
- 启动流程
- 完成任务

```text
    //提供对流程定义和部署存储库的访问服务
    @Autowired
    RepositoryService repositoryService;
    //运行时的接口
    @Autowired
    RuntimeService runtimeService;

    @ApiOperation("发起流程")
    @GetMapping("startProcess")
    public ReturnData startProcess(
            @ApiParam(value = "流程定义id", required = true) String processDefinitionId
    ) {
        log.info("发起流程，processDefinitionId：{}", processDefinitionId);
        List<ProcessDefinition> list = repositoryService.createProcessDefinitionQuery().processDefinitionId(processDefinitionId).list();
        if (list.size() != 1) {
            return ReturnData.buildError("流程定义不存在");
        }
        //流程节点中变量，替换占位符
        Map<String, Object> variablesMap = new HashMap<>();
        //设置流程变量
        variablesMap.put("userName", "老陈同学");
        variablesMap.put("day", "5");
        //通过流程定义ID启动一个流程实例
        ProcessInstance processInstance = runtimeService.startProcessInstanceById(processDefinitionId, variablesMap);
        log.info("流程实例：{}", processInstance);
        return ReturnData.buildSuccess("发起成功 " + processInstance);
    }
```

## 演示

![](./images/images/img_038_d6c14c15bcf1.gif)

```text
org.activiti.engine.ActivitiException: No outgoing sequence flow of the exclusive gateway 'sid-5cb4c263-7708-47ab-b909-18c9e52ef09c' could be selected for continuing the process
```

![](./images/images/img_039_db5cc289451f.gif)

# ParallelGateway 并行网关

　　并行网关没有条件，写了条件也会被忽略，【全部都会执行，这里可以通过在人事审批、CTO审批上添加监听器，看监听器会发现全部执行】，前面做fork分支，后面做join汇聚。

```text
if(true){
    // UserTask
}

if(true){
    // UserTask
}
```

## 画流程图

![](./images/images/img_040_56ab4c933eaf.gif)

![](./images/images/img_004_8f900a89c634.gif)
![](./images/images/img_005_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:activiti="http://activiti.org/bpmn" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" typeLanguage="http://www.w3.org/2001/XMLSchema" expressionLanguage="http://www.w3.org/1999/XPath" targetNamespace="http://www.activiti.org/processdef">
  <process id="test07" name="test07" isExecutable="true">
    <startEvent id="sid-b1a8630f-949c-488f-9c3d-adbda402ba7d" name="开始"/>
    <userTask id="sid-a0e65b29-8aa4-40f3-88f9-ff7455a5ba0e" name="经理审批"/>
    <parallelGateway id="sid-2d9234eb-334d-4444-bd03-73997b51bcd8"/>
    <userTask id="sid-91b56876-6968-4339-9387-e2f892556d87" name="人事审批"/>
    <userTask id="sid-a492a69e-7eaa-4f81-8463-923bdb220059" name="CEO审批"/>
    <endEvent id="sid-0f289cee-662f-487b-ae9f-ae11e2ee2cf7" name="结束"/>
    <sequenceFlow id="sid-b77131ec-3247-435c-ade0-8f683c0a30be" sourceRef="sid-b1a8630f-949c-488f-9c3d-adbda402ba7d" targetRef="sid-a0e65b29-8aa4-40f3-88f9-ff7455a5ba0e"/>
    <sequenceFlow id="sid-40a668a6-391d-464b-a4a9-799e17cd506a" sourceRef="sid-a0e65b29-8aa4-40f3-88f9-ff7455a5ba0e" targetRef="sid-2d9234eb-334d-4444-bd03-73997b51bcd8"/>
    <sequenceFlow id="sid-d7911d86-483f-41d0-a7c9-1acb6553e651" sourceRef="sid-2d9234eb-334d-4444-bd03-73997b51bcd8" targetRef="sid-91b56876-6968-4339-9387-e2f892556d87">
      <conditionExpression xsi:type="tFormalExpression"/>
    </sequenceFlow>
    <sequenceFlow id="sid-51759f80-5a69-47db-962c-c6c0ecc541ef" sourceRef="sid-2d9234eb-334d-4444-bd03-73997b51bcd8" targetRef="sid-a492a69e-7eaa-4f81-8463-923bdb220059">
      <conditionExpression xsi:type="tFormalExpression"/>
    </sequenceFlow>
    <sequenceFlow id="sid-1764255b-59d4-46c7-ba10-dd4a81f12c22" sourceRef="sid-a492a69e-7eaa-4f81-8463-923bdb220059" targetRef="sid-0f289cee-662f-487b-ae9f-ae11e2ee2cf7"/>
    <sequenceFlow id="sid-289e958c-2eca-4018-898c-68fb4c102c07" sourceRef="sid-91b56876-6968-4339-9387-e2f892556d87" targetRef="sid-0f289cee-662f-487b-ae9f-ae11e2ee2cf7"/>
  </process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_test07">
    <bpmndi:BPMNPlane bpmnElement="test07" id="BPMNPlane_test07">
      <bpmndi:BPMNShape id="shape-f19574eb-05f4-4a1f-9d5f-4aea21b2f88e" bpmnElement="sid-b1a8630f-949c-488f-9c3d-adbda402ba7d">
        <omgdc:Bounds x="-230.0" y="-30.0" width="30.0" height="30.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-d365cf96-89d5-4340-9759-8b0e1c141853" bpmnElement="sid-a0e65b29-8aa4-40f3-88f9-ff7455a5ba0e">
        <omgdc:Bounds x="-150.0" y="-30.0" width="60.0" height="55.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-cbc5a0eb-cde6-4af1-98ef-a65409607ef4" bpmnElement="sid-2d9234eb-334d-4444-bd03-73997b51bcd8">
        <omgdc:Bounds x="5.0" y="-30.0" width="40.0" height="40.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-6d24e7a8-9819-4b5a-a05d-2ac731efe2b2" bpmnElement="sid-91b56876-6968-4339-9387-e2f892556d87">
        <omgdc:Bounds x="110.0" y="-110.0" width="65.0" height="55.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-9ffc227d-9d03-42c5-afdc-d722f9af7081" bpmnElement="sid-a492a69e-7eaa-4f81-8463-923bdb220059">
        <omgdc:Bounds x="107.5" y="30.0" width="70.0" height="55.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-c7b35536-a98f-44ad-a947-a54f37b2800c" bpmnElement="sid-0f289cee-662f-487b-ae9f-ae11e2ee2cf7">
        <omgdc:Bounds x="270.0" y="-25.0" width="30.0" height="30.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="edge-12740e53-ee92-435f-8261-1950f4bc0ab8" bpmnElement="sid-b77131ec-3247-435c-ade0-8f683c0a30be">
        <omgdi:waypoint x="-200.0" y="-15.0"/>
        <omgdi:waypoint x="-150.0" y="-16.25"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-9d45bb1f-2c8c-4f31-88df-10bbe4f8709d" bpmnElement="sid-40a668a6-391d-464b-a4a9-799e17cd506a">
        <omgdi:waypoint x="-90.0" y="-16.25"/>
        <omgdi:waypoint x="5.0" y="-10.0"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-636c4d72-5e5a-44dd-bc02-92f64a49353c" bpmnElement="sid-d7911d86-483f-41d0-a7c9-1acb6553e651">
        <omgdi:waypoint x="45.0" y="-10.0"/>
        <omgdi:waypoint x="110.0" y="-68.75"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-c4cb3824-5855-468c-b070-5e66601d97ba" bpmnElement="sid-51759f80-5a69-47db-962c-c6c0ecc541ef">
        <omgdi:waypoint x="25.0" y="10.0"/>
        <omgdi:waypoint x="107.5" y="43.75"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-24167aaa-57fb-4b34-b59e-4a31e048618c" bpmnElement="sid-1764255b-59d4-46c7-ba10-dd4a81f12c22">
        <omgdi:waypoint x="177.5" y="43.75"/>
        <omgdi:waypoint x="270.0" y="-2.5"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-5743d318-facd-4848-8f31-a48c8964d9f7" bpmnElement="sid-289e958c-2eca-4018-898c-68fb4c102c07">
        <omgdi:waypoint x="175.0" y="-68.75"/>
        <omgdi:waypoint x="270.0" y="-17.5"/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</definitions>
```

test07.bpmn20.xml

## 操作步骤

- 保存xxx.png
- 压缩xxx.zip
- 部署xxx.zip
- 发起流程
- 完成流程

## 演示

　　当【经理审批】完接下来就会同时插入两条任务(人事审批、CTO审批)，两个经理审核完后就结束。

![](./images/images/img_041_719f99097b7c.gif)

# 任务委派【重要】

　　任务委派只是任务人将当前的任务交给接收人进行审批，完成任务后又重新回到任务人身上。委派人查询任务与完成任务与正常的有区别。

```text
    // 任务处理接口
    @Autowired
    TaskService taskService;

    @ApiOperation("任务委派")
    @GetMapping("delegateTask")
    public ReturnData delegateTask(
            @ApiParam(value = "任务id", required = true) @RequestParam("taskId") String taskId,
            @ApiParam(value = "新代办人", required = true) @RequestParam("userName") String userName
    ) {
        Task task = taskService.createTaskQuery().taskId(taskId).singleResult();
        if (task == null) {
            return ReturnData.buildError("任务不存在");
        }
        taskService.delegateTask(taskId, userName);
        return ReturnData.buildSuccess();
    }
```

## 画流程图

![](./images/images/img_042_09f7271156a2.gif)

## 演示

![](./images/images/img_043_d5aa1da5ef43.gif)

```text
insert into ACT_HI_IDENTITYLINK
insert into ACT_RU_IDENTITYLINK

update ACT_HI_ACTINST
update ACT_HI_TASKINST
update ACT_RU_TASK
```

**注：后续由委派人处理这个任务！！！**

# 任务转办【适用于审批人离职，重要】

　　任务转办和任务委派类似，任务转办适用于公司领导离职，这个任务没人处理了，将这个任务转办给其他人处理

```text
    // 任务处理接口
    @Autowired
    TaskService taskService;

    @ApiOperation("任务转办")
    @GetMapping("setAssignee")
    public ReturnData setAssignee(
            @ApiParam(value = "任务id", required = true) @RequestParam("taskId") String taskId,
            @ApiParam(value = "新代办人", required = true) @RequestParam("userName") String userName
    ) {
        Task task = taskService.createTaskQuery().taskId(taskId).singleResult();
        if (task == null) {
            return ReturnData.buildError("任务不存在");
        }
        taskService.setAssignee(taskId, userName);
        return ReturnData.buildSuccess();
    }
```

## 演示

![](./images/images/img_044_67a215cba129.gif)

```text
insert into ACT_HI_IDENTITYLINK
insert into ACT_RU_IDENTITYLINK
insert into ACT_HI_COMMENT

update ACT_HI_ACTINST
update ACT_HI_TASKINST
update ACT_RU_TASK
```

# 子流程

## 画子流程图

![](./images/images/img_045_53041951f2c7.gif)

 注：后续流程，跟之前一样，所以不做演示~~~

# 流程驳回

　　我们可以通过变量控制来控制流程走向，达到拒绝效果。

## 画流程图

![](./images/images/img_046_c5a9c6c66c8e.gif)

![](./images/images/img_004_8f900a89c634.gif)
![](./images/images/img_005_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<definitions xmlns="http://www.omg.org/spec/BPMN/20100524/MODEL" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:activiti="http://activiti.org/bpmn" xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI" xmlns:omgdc="http://www.omg.org/spec/DD/20100524/DC" xmlns:omgdi="http://www.omg.org/spec/DD/20100524/DI" typeLanguage="http://www.w3.org/2001/XMLSchema" expressionLanguage="http://www.w3.org/1999/XPath" targetNamespace="http://www.activiti.org/processdef">
  <process id="test10" name="test10" isExecutable="true">
    <startEvent id="sid-4ca9415c-f5f0-4d44-85ca-dc2ec7c5aff6" name="开始"/>
    <userTask id="sid-2107235f-29c5-49d3-b411-d3bb743e624d" name="经理审批"/>
    <userTask id="sid-e1897543-e371-4e6c-a549-70e1e04c9d2b" name="人事审批"/>
    <endEvent id="sid-674ee529-88ae-4650-805d-eed2612d9cff" name="结束"/>
    <userTask id="sid-84df6af9-354d-4812-9557-b9f09490e3c0" name="拒绝"/>
    <sequenceFlow id="sid-5826816d-a559-46d9-8ef1-cbee1f25131e" sourceRef="sid-4ca9415c-f5f0-4d44-85ca-dc2ec7c5aff6" targetRef="sid-2107235f-29c5-49d3-b411-d3bb743e624d"/>
    <sequenceFlow id="sid-278815fe-54e1-4b0a-a7f2-2fc48e57a10a" sourceRef="sid-2107235f-29c5-49d3-b411-d3bb743e624d" targetRef="sid-e1897543-e371-4e6c-a549-70e1e04c9d2b" name="pmtype=1">
      <conditionExpression>${pmtype==1}</conditionExpression>
    </sequenceFlow>
    <sequenceFlow id="sid-173ad315-1b5d-4367-b069-6afc7b3ed163" sourceRef="sid-e1897543-e371-4e6c-a549-70e1e04c9d2b" targetRef="sid-674ee529-88ae-4650-805d-eed2612d9cff" name="hrtype=1">
      <conditionExpression>${hrtype==1}</conditionExpression>
    </sequenceFlow>
    <sequenceFlow id="sid-68df7892-7c16-4325-90e0-6079edee7929" sourceRef="sid-2107235f-29c5-49d3-b411-d3bb743e624d" targetRef="sid-84df6af9-354d-4812-9557-b9f09490e3c0" name="pmtype=0">
      <conditionExpression>${pmtype==0}</conditionExpression>
    </sequenceFlow>
    <sequenceFlow id="sid-0b1f53ed-fbb4-490a-bd1d-ba14bfc16030" sourceRef="sid-e1897543-e371-4e6c-a549-70e1e04c9d2b" targetRef="sid-84df6af9-354d-4812-9557-b9f09490e3c0" name="hrtype=0">
      <conditionExpression>${hrtype==0}</conditionExpression>
    </sequenceFlow>
    <sequenceFlow id="sid-fec66f4c-574d-4bf3-bc93-c93730663cbb" sourceRef="sid-84df6af9-354d-4812-9557-b9f09490e3c0" targetRef="sid-674ee529-88ae-4650-805d-eed2612d9cff"/>
  </process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_test10">
    <bpmndi:BPMNPlane bpmnElement="test10" id="BPMNPlane_test10">
      <bpmndi:BPMNShape id="shape-b167c146-3493-4060-b201-47fdc0360b81" bpmnElement="sid-4ca9415c-f5f0-4d44-85ca-dc2ec7c5aff6">
        <omgdc:Bounds x="-170.0" y="-70.0" width="30.0" height="30.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-f68690d2-a9ee-400b-bd69-795537a86b9d" bpmnElement="sid-2107235f-29c5-49d3-b411-d3bb743e624d">
        <omgdc:Bounds x="-80.0" y="-90.0" width="85.0" height="60.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-2751d43c-a5fd-4bcd-b5b8-3d3ba3de9c21" bpmnElement="sid-e1897543-e371-4e6c-a549-70e1e04c9d2b">
        <omgdc:Bounds x="95.0" y="-92.5" width="90.0" height="65.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-9e1a642c-1a1b-4bc6-ac83-5555842765a9" bpmnElement="sid-674ee529-88ae-4650-805d-eed2612d9cff">
        <omgdc:Bounds x="295.0" y="-75.0" width="30.0" height="30.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="shape-806d7082-618c-43d3-badd-575ceaf01471" bpmnElement="sid-84df6af9-354d-4812-9557-b9f09490e3c0">
        <omgdc:Bounds x="45.0" y="50.0" width="100.0" height="80.0"/>
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="edge-56c7a36e-ec3d-45ee-9544-b5aef4b8507b" bpmnElement="sid-5826816d-a559-46d9-8ef1-cbee1f25131e">
        <omgdi:waypoint x="-140.0" y="-62.5"/>
        <omgdi:waypoint x="-80.0" y="-60.0"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-a83efc0d-a920-4f5e-b231-3681333795a4" bpmnElement="sid-278815fe-54e1-4b0a-a7f2-2fc48e57a10a">
        <omgdi:waypoint x="5.0" y="-60.0"/>
        <omgdi:waypoint x="95.0" y="-60.0"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-e7940e8a-0832-48c3-9ff7-6fea9a3ad154" bpmnElement="sid-173ad315-1b5d-4367-b069-6afc7b3ed163">
        <omgdi:waypoint x="185.0" y="-60.0"/>
        <omgdi:waypoint x="295.0" y="-60.0"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-3e1767bc-ddeb-42e1-986d-3fa17ca64099" bpmnElement="sid-68df7892-7c16-4325-90e0-6079edee7929">
        <omgdi:waypoint x="5.0" y="-45.0"/>
        <omgdi:waypoint x="70.0" y="50.0"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-430b3e8f-9943-4432-914c-1e63984cd3b8" bpmnElement="sid-0b1f53ed-fbb4-490a-bd1d-ba14bfc16030">
        <omgdi:waypoint x="117.5" y="-27.5"/>
        <omgdi:waypoint x="120.0" y="50.0"/>
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="edge-b8a4e3cb-34e1-441c-ad3f-57f451a78165" bpmnElement="sid-fec66f4c-574d-4bf3-bc93-c93730663cbb">
        <omgdi:waypoint x="145.0" y="70.0"/>
        <omgdi:waypoint x="295.0" y="-52.5"/>
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</definitions>
```

test10.bpmn20.xml

- 经理审批

  - pmtype==1：同意
  - pmtype==0：拒绝

- 人事审批

  - hrtype==1：同意
  - hrtype==0：拒绝

## 经理审批时，需要设置环境变量

```text
    // 任务处理接口
    @Autowired
    TaskService taskService;

    @ApiOperation("完成任务")
    @GetMapping("completeTask")
    public ReturnData completeTask(
            @ApiParam(value = "流程实例id", required = true) String processInstanceId
    ) {
        //根据流程实例id，查询任务
        List<Task> taskList = taskService.createTaskQuery().processInstanceId(processInstanceId).list();
        if (taskList.size() != 1) {
            return ReturnData.buildError("当前没有任务");
        }
        log.info("任务列表：{}", taskList);
        //经理审批，添加环境变量pmtype
        Map<String, Object> variables = new HashMap<>();
        variables.put("pmtype", 1);
        //根据任务id，完成任务
        taskService.complete(taskList.get(0).getId(), variables);
        return ReturnData.buildSuccess("完成任务");
    }
```

其他人审核，同理

# 项目源码

[https://gitee.com/yenbin_chen/ybchen-activiti7](https://gitee.com/yenbin_chen/ybchen-activiti7)

# 升级activiti版本踩坑

```text
org.activiti.engine.ActivitiException: Could not update Activiti database schema: unknown version from database: '7.1.0-M6'
```

### 原因：

　　Activiti相关的jar版本和表act_ge_property中schema.version所存储的版本不一致造成的

![](./images/images/img_047_2f7f1c5b70f4.png)

查看activiti相关jar包版本修改数据库中的版本就可(ProcessEngine所在的包下)

```text
UPDATE act_ge_property SET VALUE_='7.0.0.0' WHERE NAME_='schema.version';
```

![](./images/images/img_048_1e792c607b46.png)
