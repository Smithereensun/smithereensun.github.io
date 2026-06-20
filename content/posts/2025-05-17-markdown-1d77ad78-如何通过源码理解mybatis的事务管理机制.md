{

  "title": "如何通过源码理解MyBatis的事务管理机制",
  "has_date": true,
  "description": "概述 对数据库的事务而言，应该具有以下几点：创建（create）、提交（commit）、回滚（rollback）、关闭（close）。对应地，MyBatis将事务抽象成了Transaction接口： MyBatis的事务管理分为两种形式： 使用JDBC的事务管理机制**：即利用java.sql.Co",
  "tags": [
    "框架",
    "ORM"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/orm/mybatis-transactionmanagementmechanism - 如何通过源码理解MyBatis的事务管理机制.md",
  "date": "2025-05-17"

}

## [概述](#概述)

对数据库的事务而言，应该具有以下几点：创建（create）、提交（commit）、回滚（rollback）、关闭（close）。对应地，MyBatis将事务抽象成了Transaction接口：
![](/imported/markdown/2025-05-17-markdown-1d77ad78-如何通过源码理解mybatis的事务管理机制/images/0001fa15b2c5-202411301324984.png)
MyBatis的事务管理分为两种形式：

- **使用JDBC的事务管理机制**：即利用java.sql.Connection对象完成对事务的提交（commit()）、回滚（rollback()）、关闭（close()）等。

- **使用MANAGED的事务管理机制**：这种机制MyBatis自身不会去实现事务管理，而是让程序的容器如（JBOSS，Weblogic）来实现对事务的管理。

这两者的类图如下所示：
![](/imported/markdown/2025-05-17-markdown-1d77ad78-如何通过源码理解mybatis的事务管理机制/images/88de0460ec11-202411301324045.png)
## [官网关于事务配置的内容](#官网关于事务配置的内容)

在 MyBatis 中有两种类型的事务管理器（也就是 `type="[JDBC|MANAGED]"`）：

- **JDBC** – 这个配置直接使用了 JDBC 的提交和回滚设施，它依赖从数据源获得的连接来管理事务作用域。

- **MANAGED** – 这个配置几乎没做什么。它从不提交或回滚一个连接，而是让容器来管理事务的整个生命周期（比如 JEE 应用服务器的上下文）。 默认情况下它会关闭连接。然而一些容器并不希望连接被关闭，因此需要将 closeConnection 属性设置为 false 来阻止默认的关闭行为。例如:

如果你正在使用 Spring + MyBatis，则没有必要配置事务管理器，因为 Spring 模块会使用自带的管理器来覆盖前面的配置。

这两种事务管理器类型都不需要设置任何属性。它们其实是类型别名，换句话说，你可以用 TransactionFactory 接口实现类的全限定名或类型别名代替它们。

在事务管理器实例化后，所有在 XML 中配置的属性将会被传递给 setProperties() 方法。你的实现还需要创建一个 Transaction 接口的实现类，这个接口也很简单：

使用这两个接口，你可以完全自定义 MyBatis 对事务的处理。

## [事务的配置、创建和使用](#事务的配置、创建和使用)

### [事务的配置](#事务的配置)

我们在使用MyBatis时，一般会在MyBatisXML配置文件中定义类似如下的信息：
![](/imported/markdown/2025-05-17-markdown-1d77ad78-如何通过源码理解mybatis的事务管理机制/images/dd15548fb261-202411301324511.png)
`&lt;environment&gt;`节点定义了连接某个数据库的信息，其子节点`&lt;transactionManager&gt;` 的type 会决定我们用什么类型的事务管理机制。

### [事务工厂的创建](#事务工厂的创建)

MyBatis事务的创建是交给TransactionFactory 事务工厂来创建的，如果我们将`&lt;transactionManager&gt;`的type 配置为"JDBC",那么，在MyBatis初始化解析 `&lt;environment&gt;`节点时，会根据type="JDBC"创建一个JdbcTransactionFactory工厂，其源码如下：

如上述代码所示，如果type = "JDBC",则MyBatis会创建一个JdbcTransactionFactory.class 实例；如果type="MANAGED"，则MyBatis会创建一个MangedTransactionFactory.class实例。

MyBatis对`&lt;transactionManager&gt;`节点的解析会生成TransactionFactory实例；而对`&lt;dataSource&gt;`解析会生成datasouce实例，作为`&lt;environment&gt;`节点，会根据TransactionFactory和DataSource实例创建一个Environment对象，代码如下所示：

Environment表示着一个数据库的连接，生成后的Environment对象会被设置到Configuration实例中，以供后续的使用。
![](/imported/markdown/2025-05-17-markdown-1d77ad78-如何通过源码理解mybatis的事务管理机制/images/118ebd73c3ae-202404291754352.png)
上述一直在讲事务工厂TransactionFactory来创建的Transaction，现在让我们看一下MyBatis中的TransactionFactory的定义吧。

### [事务工厂TransactionFactory](#事务工厂transactionfactory)

事务工厂Transaction定义了创建Transaction的两个方法：一个是通过指定的Connection对象创建Transaction，另外是通过数据源DataSource来创建Transaction。与JDBC 和MANAGED两种Transaction相对应，TransactionFactory有两个对应的实现的子类：
![](/imported/markdown/2025-05-17-markdown-1d77ad78-如何通过源码理解mybatis的事务管理机制/images/805defe81dfe-202411301325563.png)
### [事务Transaction的创建](#事务transaction的创建)

通过事务工厂TransactionFactory很容易获取到Transaction对象实例。我们以JdbcTransaction为例，看一下JdbcTransactionFactory是怎样生成JdbcTransaction的，代码如下：

如上说是，JdbcTransactionFactory会创建JDBC类型的Transaction，即JdbcTransaction。类似地，ManagedTransactionFactory也会创建ManagedTransaction。下面我们会分别深入JdbcTranaction 和ManagedTransaction，看它们到底是怎样实现事务管理的。

### [JdbcTransaction](#jdbctransaction)

JdbcTransaction直接使用JDBC的提交和回滚事务管理机制。它依赖与从dataSource中取得的连接connection 来管理transaction 的作用域，connection对象的获取被延迟到调用getConnection()方法。如果autocommit设置为on，开启状态的话，它会忽略commit和rollback。

直观地讲，就是JdbcTransaction是使用的java.sql.Connection 上的commit和rollback功能，JdbcTransaction只是相当于对java.sql.Connection事务处理进行了一次包装（wrapper），Transaction的事务管理都是通过java.sql.Connection实现的。JdbcTransaction的代码实现如下：

### [ManagedTransaction](#managedtransaction)

ManagedTransaction让容器来管理事务Transaction的整个生命周期，意思就是说，使用ManagedTransaction的commit和rollback功能不会对事务有任何的影响，它什么都不会做，它将事务管理的权利移交给了容器来实现。看如下Managed的实现代码大家就会一目了然：

注意：如果我们使用MyBatis构建本地程序，即不是WEB程序，若将type设置成"MANAGED"，那么，我们执行的任何update操作，即使我们最后执行了commit操作，数据也不会保留，不会对数据库造成任何影响。因为我们将MyBatis配置成了“MANAGED”，即MyBatis自己不管理事务，而我们又是运行的本地程序，没有事务管理功能，所以对数据库的update操作都是无效的。
