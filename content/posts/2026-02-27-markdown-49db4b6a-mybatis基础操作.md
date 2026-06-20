{

  "title": "Mybatis基础操作",
  "has_date": true,
  "description": "Mybatis基础使用 Mybatis编程式开发 mybatis和MySQL jar包依赖 全局配置文件mybatis-config.xml 配置文件对应标签可以看官方文档：https://mybatis.org/mybatis-3/configuration.html 映射器 Mapper.xml",
  "tags": [
    "框架",
    "ORM"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/orm/mybatis-baseuse - Mybatis基础操作.md",
  "date": "2026-02-27"

}

## [Mybatis基础使用](#mybatis基础使用)

### [Mybatis编程式开发](#mybatis编程式开发)

1. mybatis和MySQL jar包依赖

1. 全局配置文件mybatis-config.xml

配置文件对应标签可以看官方文档：[https://mybatis.org/mybatis-3/configuration.html](https://mybatis.org/mybatis-3/configuration.html)

1. 映射器 Mapper.xml

1. Mapper接口

1. mybatis工具类

1. 编程式使用示例

### [整合Spring](#整合spring)

1. 添加依赖

较编程式开发主要是需要添加spring核心和MyBatis-Spring整合包

1. **mybatis.xml**​ - MyBatis 和事务配置

1. **applicationContext.xml**​ - Spring 主配置文件

1. 测试案例

### [整合SpringBoot](#整合springboot)

1. 添加依赖

1. ​ `application.yml`配置，无需创建`mybatis-config.xml`文件，可直接在yaml文件中配置

1. 配置自动扫描 Mapper 接口

1. 自动注入 Mapper

## [Mybatis代码生成器](#mybatis代码生成器)

[https://github.com/mybatis/generator](https://github.com/mybatis/generator)

## [Mybatis动态sql](#mybatis动态sql)

[https://mybatis.org/mybatis-3/dynamic-sql.html](https://mybatis.org/mybatis-3/dynamic-sql.html)

## [Mybatis批量操作](#mybatis批量操作)

进行批量操作时，有三种方式，操作方式对比：
操作类型适用场景实现方式优点缺点**foreach SQL**​小批量数据插入/更新/删除在 XML 中写 `&lt;foreach&gt;`生成 SQL简单直观，一次性执行SQL 长度有限制，大数据量可能超限**Batch Executor**​大批量数据操作使用 `ExecutorType.BATCH`性能最优，预编译 SQL需要手动管理事务和提交**JDBC Batch**​需要底层控制使用原生 JDBC Batch完全控制，灵活性高代码复杂，需处理底层细节
### [使用 foreach 标签的批量操作案例](#使用-foreach-标签的批量操作案例)

#### [批量插入](#批量插入)

#### [批量更新](#批量更新)

#### [批量删除](#批量删除)

#### [批量查询](#批量查询)

### [使用 foreach 标签的注意事项](#使用-foreach-标签的注意事项)

#### [SQL 长度限制](#sql-长度限制)

#### [事务管理](#事务管理)

## [Mybatis关联查询和延迟加载](#mybatis关联查询和延迟加载)
特性嵌套查询（Nested Query）嵌套结果（Nested Result）**原理**​执行多条SQL查询，在结果映射中引用其他查询执行一条联合查询，在结果映射中处理嵌套对象**SQL数量**​N+1 条（主查询 + N 条关联查询）1 条（联合查询）**性能**​有 N+1 问题，性能较差性能较好，避免 N+1 问题**复杂度**​简单，易于理解和维护复杂，SQL 语句较复杂**适用场景**​关联数据较少，延迟加载场景关联数据较多，需要一次性加载所有数据**内存占用**​较低，按需加载较高，一次性加载所有数据
### [嵌套查询](#嵌套查询)

在查询一个对象时，可以同时通过另一个查询语句来加载关联的另一个对象。例如，查询用户时，通过另一个查询语句来加载该用户的订单。

嵌套查询可能引起N+1问题：因为当我们查询一个列表时，对于列表中的每一条记录，都会执行一次额外的查询来加载关联数据。这样，如果有N条记录，就会执行1次主查询和N次关联查询，即N+1次查询。

### [嵌套结果](#嵌套结果)

通过一次复杂的联表查询，将结果映射到多个对象中。例如，通过一个SQL语句查询用户及其订单，然后通过结果映射将用户和订单的数据分别映射到用户对象和订单对象中。

### [N+1 查询问题详解](#n-1-查询问题详解)

什么是 N+1 问题：当使用嵌套查询时，如果有 N 个主记录，每个主记录都有 M 个关联记录，那么会执行：

- 1 条主查询

- N 条关联查询

总共执行 1 + N 条查询

演示案例：

延迟加载可以解决N+1问题：延迟加载是指在需要使用关联数据时才去加载。在MyBatis中，可以配置延迟加载，这样在查询主对象时，不会立即加载关联对象，只有当访问关联对象时才会执行额外的查询。这样，如果访问了所有关联对象，那么还是会执行N+1次查询，但如果我们只访问部分主对象的关联对象，那么就可以减少查询次数。

#### [延迟加载解决方案](#延迟加载解决方案)

- 配置延迟加载：mybatis-config.xml 配置

application.yml 配置（Spring Boot）

- 在映射中使用延迟加载

但是，延迟加载只是将N+1次查询的时机推迟了，并没有从根本上减少查询次数。要解决N+1问题，更好的方式是使用嵌套结果（即一次联表查询）或者批量加载（MyBatis 3.4.1以上支持关联的批量加载）来减少查询次数。

#### [批量加载](#批量加载)

#### [使用嵌套结果（推荐）](#使用嵌套结果-推荐)

#### [使用子查询 + IN 语句](#使用子查询-in-语句)
