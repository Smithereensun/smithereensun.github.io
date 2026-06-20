{

  "title": "JDBC连接数据库的核心原理",
  "has_date": true,
  "description": "JDBC实现及原理 JDBC（Java DataBase Connectivity）是Java和数据库之间的一个桥梁，是一个「规范」而不是一个实现，能够执行SQL语句。JDBC由一组用Java语言编写的类和接口组成。各种不同类型的数据库都有相应的实现，注意：本文中的代码都是针对MySQL数据库实现的",
  "tags": [
    "框架",
    "ORM"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/orm/basement-jdbc - JDBC连接数据库的核心原理.md",
  "date": "2026-02-20"

}

## [JDBC实现及原理](#jdbc实现及原理)

JDBC（Java DataBase Connectivity）是Java和数据库之间的一个桥梁，是一个「规范」而不是一个实现，能够执行SQL语句。JDBC由一组用Java语言编写的类和接口组成。各种不同类型的数据库都有相应的实现，注意：本文中的代码都是针对MySQL数据库实现的。

先看一个案例：

JDBC 步骤如下：

1. 数据库驱动：Class.forName("com.mysql.jdbc.Driver");

1. 获取链接：Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);

1. 创建Statement或者PreparedStatement对象： Statement stmt = conn.createStatement();

1. 执行sql数据库查询：ResultSet rs = stmt.executeQuery("SELECT id, name, age FROM m_user where id =1");

1. 解析结果集：System.out.println("name: "+rs.getString("name")+" ：年龄"+rs.getInt("age"));

1. 最后就是各种资源的关闭。

### [数据库驱动](#数据库驱动)

安装好数据库之后，应用程序是不能直接使用数据库的，必须要通过相应的数据库驱动程序，通过驱动程序去和数据库打交道。其实也就是数据库厂商的JDBC接口实现，即对Connection等接口的实现类的jar文件。

Driver接口：此接口是提供给数据库厂商实现的。比如说MySQL的，需要依赖对应的jar包

MySQL数据库对应的实现驱动实现类：

DriverManager是rt.jar包下的类，（rt=runtime），把程序需要驱动类注册进去。

类似的，可以加载其它厂商的驱动

- Oracle驱动：Class.forName("oracle.jdbc.driver.OracleDriver");

- Sql Server驱动：Class.forName("com.microsoft.jdbc.sqlserver.SQLServerDriver");

### [获取连接](#获取连接)

看起来只有这一行代码

Connection conn = DriverManager.getConnection(URL, USER, PASSWORD);

深入聊聊这行代码，到底底层是怎么连接数据库的？

方法三个参数：链接地址，用户名和密码。

获取连接的关键代码aDriver.driver.connect(url,info); 这个方法是每个数据库驱动自己的实现的。

获取连接的关键代码aDriver.driver.connect(url,info); 这个方法是每个数据库驱动自己的实现的。

ConnectionImpl构造方法里有调用createNewIO方法：

com.mysql.cj.protocol.a.NativeSocketConnection#connect

这里的socketFactory是StandardSocketFactory。所以也就是调用的是StandardSocketFactory的connect方法：

### [小结](#小结)

数据库驱动依赖SPI类加载机制

获取连接是通过socket与数据库取得连接的

## [使用JDBC原生API面对的问题](#使用jdbc原生api面对的问题)

- 需要手动管理资源

- 代码重复

- 业务逻辑与数据操作的代码耦合

- 结果集需要手动处理

## [更简单的操作数据库的方式？](#更简单的操作数据库的方式)

### [JdbcTemplate](#jdbctemplate)

`JdbcTemplate` 是 Spring Framework 提供的一个核心类，用于简化 JDBC 编程。它的主要作用包括：

- 自动管理数据库连接（获取、释放）

- 自动处理异常（将 SQLException 转换为 Spring 的 DataAccessException）

- 简化 SQL 执行（增删改查）

- 自动映射结果集（ResultSet）到 Java 对象

- 避免样板代码（如 try-catch-finally、资源关闭等）

`JdbcTemplate`的核心设计是**模板方法模式**，将固定的操作流程（如获取连接、执行语句、释放资源）封装起来，而将可变部分（如 SQL 语句、参数设置、结果映射）通过回调接口留给我们开发者

1. 引入依赖

1. Spring Boot 配置（application.properties）

1. 在 Spring Boot 中，配置数据源后，可直接注入 `JdbcTemplate`

1. 执行 DML 操作（增、删、改）

使用 `update()`方法执行 `INSERT`, `UPDATE`, `DELETE`操作。它返回受影响的行数

1. 执行 DQL 操作（查询）及结果集映射

这是 JdbcTemplate 最强大的功能之一，提供了多种灵活的映射方式。

- 使用 `RowMapper&lt;T&gt;` 自定义映射

`RowMapper`接口用于将结果集的每一行映射为一个 Java 对象。需要实现 `mapRow`方法

- 使用 `BeanPropertyRowMapper&lt;T&gt;`（推荐）

这是最常用的映射方式。如果数据库字段名（或下划线命名）和 Java 对象的属性名（驼峰命名）能够对应，Spring 会自动完成映射

- 使用BaseRowMapper工具类，通用映射器，可以彻底告别为每个实体类编写重复的 `RowMapper`实现

### [工具小结](#工具小结)

工具类解决了

- 方法封装

- 支持数据源

- 映射结果集，实现从数据库到对象的映射

没解决

- SQL语句硬编码

- 参数只能按顺序传入(占位符)

- 没有实现对象到数据库记录的映射

- 没有实现缓存等功能

## [什么是ORM框架](#什么是orm框架)

ORM : Object Relational Mapping

ORM解决的是 程序对象 和关系型数据库的 数据映射的问题

mybatis特性

- 使用连接池对连接进行管理

- SQL和代码分离，集中管理

- 参数映射和动态SQL

- 结果集映射

- 缓存管理

- 重复SQL的提取`&lt;sql&gt;`

- 插件机制
