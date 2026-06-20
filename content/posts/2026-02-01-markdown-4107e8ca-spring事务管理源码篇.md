{

  "title": "Spring事务管理源码篇",
  "has_date": true,
  "description": "解析JDBC操作事务的本质 无事务操作 以下代码模拟了一次转账操作：从 ` Eight accounts Eight setAutoCommit(true) @JDKProxyTransactional TransactionInterceptor.invoke() TransactionAspec",
  "tags": [
    "框架",
    "Spring"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/spring/spring-transactions-sourcecode - Spring事务管理源码篇.md",
  "date": "2026-02-01"

}

## [解析JDBC操作事务的本质](#解析jdbc操作事务的本质)

### [无事务操作](#无事务操作)

以下代码模拟了一次转账操作：从 ``的账户向 `Eight`的账户转账 200 元。关键在于，我们**没有开启事务**，并且在两次更新操作之间人为制造了一个异常：

运行上述代码后，你会在控制台看到异常信息，但更重要的是，去数据库检查 `accounts`表，会发现：

- **``的余额变成了 800 元**（成功扣款 200）。

- **`Eight`的余额仍然是 1900 元**（并未收到钱）。

**问题的核心**在于 JDBC 连接的默认设置是 `setAutoCommit(true)`。这意味着**每执行一条 SQL 语句，都会立即被当作一个独立的事务提交到数据库**，无法撤销

### [解决方案：使用事务管理](#解决方案-使用事务管理)

要避免这种问题，核心是**将多个相关的数据库操作绑定成一个原子单位**。以下是正确的做法：

### [基于JDK代理的方式实现事务管理](#基于jdk代理的方式实现事务管理)

我们知道，代理模式可以对目标方法进行增强，因此对于JDK动态代理，可以在InvocationHandler的invoke方法中，在目标方法执行前开启事务，执行后提交，异常时回滚。从而自定义的实现事务管理

#### [定义事务管理器](#定义事务管理器)

- 定义事务注解：用于标记需要事务管理的方法。

引入注解机制，可以灵活控制哪些方法需要事务。这样只需要在方法上添加注解就能自动获得事务支持。

- 数据库连接与线程绑定

事务管理的核心是保证同一个线程内的多个数据库操作使用同一个Connection连接，可以通过ThreadLocal来实现线程绑定。

- 事务管理器：封装基本的事务操作

事务管理器，应该提供beginTransaction、commit、rollback这些基本操作。

- 实现InvocationHandler：JDK动态代理的核心，在这里织入事务逻辑

- 创建代理工厂：提供一个简便的方法来生成代理对象。

#### [如何使用](#如何使用)

- 定义服务接口及其实现：在需要事务管理的方法上添加 `@JDKProxyTransactional`注解。

- 获取代理对象并使用：通过代理工厂获取代理对象，然后调用方法

### [基于AspectJ方式自定义事务实现](#基于aspectj方式自定义事务实现)

同样的，我们也可以基于AspectJ方式来自定义事务实现，这种方式相比 JDK 动态代理更加强大，因为它支持**编译时织入**和**加载时织入**，可以直接拦截**类的任何方法**（包括非 public 方法、静态方法等），而不仅限于接口方法。

#### [定义事务管理器](#定义事务管理器-1)

- 定义事务注解

- 数据库连接和事务管理器

- AspectJ 切面实现

#### [如何使用](#如何使用-1)

业务服务类：不需要实现任何接口，AspectJ可以直接拦截类的方法

## [Spring事务源码分析](#spring事务源码分析)

以下源码均基于Spring4.3.12版本。主要从 创建事务、开启事务、提交事务、事务回滚 的维度来详细分析声明式事务。

### [事务简易流程图](#事务简易流程图)
![](/imported/markdown/2026-02-01-markdown-4107e8ca-spring事务管理源码篇/images/862581127e43-202411160956109.png)
### [代理类生成](#代理类生成)

在Spring框架中，当配置了事务管理器并声明了@Transactional注解时，Spring会在实例化bean时生成事务增强的代理类。创建代理类参考源码路径如下：

### [代理类中方法执行入口](#代理类中方法执行入口)

从`TransactionInterceptor.invoke()`方法开始分析 (获取代理类，调用父类`TransactionAspectSupport.invokeWithinTransaction()`方法，该方法会将代理类的方法纳入事务中)。

### [主要核心逻辑](#主要核心逻辑)

`TransactionAspectSupport.invokeWithinTransaction()`方法负责获取事务属性和事务管理器，然后针对声明式事务和编程式事务区分处理流程（此处源码忽略编程式事务）。

### [开启事务](#开启事务)

`TransactionAspectSupport.createTransactionIfNecessary()` 方法作用是检查当前是否存在事务，如果存在，则根据一定的规则创建一个新的事务。

#### [获取当前事务对象](#获取当前事务对象)

`AbstractPlatformTransactionManager.getTransaction()` 获取当前事务对象。通过这个方法，可以获取到关于事务的详细信息，如事务的状态、相关属性等。

#### [执行获取事务的具体操作](#执行获取事务的具体操作)

`AbstractPlatformTransactionManager.doGetTransaction()` 方法用于执行获取事务的具体操作。它可能会根据一些条件或规则，去查找和获取当前的事务对象，并进行相应的处理。

- `this.dataSource()` 是我们配置DataSourceTransactionManager时传入的。

- `TransactionSynchronizationManager.getResource()` 方法的作用主要是获取与当前事务相关联的资源。TransactionSynchronizationManager 持有一个ThreadLocal的实例，存在一个key为dataSource，value为ConnectionHolder 的Map信息。

#### [判断是否存在正在进行的事务](#判断是否存在正在进行的事务)

`AbstractPlatformTransactionManager.isExistingTransaction()` 方法用于判断是否存在正在进行的事务。它可以帮助我们确定当前的执行环境是否处于事务中，以便进行相应的处理。

#### [挂起事务](#挂起事务)

`AbstractPlatformTransactionManager.suspend()` 挂起事务,对有无同步的事务采取不同方案，`doSuspend()`执行挂起具体操作。

- `AbstractPlatformTransactionManager.doSuspend()`执行挂起操作只是将当前ConnectionHolder设置为null，返回原有事务消息，方便后续恢复原有事务消息，并将当前正在进行的事务信息进行重置。

- `AbstractPlatformTransactionManager.doBegin()`数据库连接获取，当新事务时，则获取新的数据库连接，并为其设置隔离级别，是否只读等属性。

- `AbstractPlatformTransactionManager.prepareTransactionStatus()`创建默认Status,如果不需要开始事务 （比如SUPPORTS），则返回一个默认的状态。

- `AbstractPlatformTransactionManager.handleExistingTransaction()`针对不同的传播行为做不同的处理方法，比如挂起原事务开启新事务等等。

### [回滚事务](#回滚事务)

`TransactionAspectSupport.completeTransactionAfterThrowing()` 判断事务是否存在，如不存在就不需要回滚，如果存在则在判断是否满足回滚条件。

`AbstractPlatformTransactionManager.rollback()`当在事务执行过程中出现异常或其他需要回滚的情况时，就会调用这个方法，将事务进行回滚操作，撤销之前所做的数据库操作，以保证数据的一致性。

`AbstractPlatformTransactionManager.processRollback()`方法主要用于处理事务的回滚操作。通过这个方法，可以确保事务在需要回滚时能够正确地执行回滚操作，保持数据的完整性。

### [提交事务](#提交事务)

`TransactionAspectSupport.commitTransactionAfterReturning()` 基本上和回滚一样，都是先判断是否有事务，在操作提交。

`AbstractPlatformTransactionManager.commit()` 创建默认Status prepareTransactionStatu,发现是否有回滚标记，然后进行回滚。如果判断无需回滚就可以直接提交。

`AbstractPlatformTransactionManager.processCommit()`处理事务的提交操作

### [清除事务信息](#清除事务信息)

`AbstractPlatformTransactionManager.cleanupAfterCompletion()` 这个方法主要用于在事务完成后进行清理工作。它会负责释放资源、清理临时数据等，以确保系统处于良好的状态。

`AbstractPlatformTransactionManager.doCleanupAfterCompletion()`在新事务完成后会调用resetConnectionAfterTransaction方法重置数据库连接信息，并判断如果是新的数据库连接则将其放回连接池。

`AbstractPlatformTransactionManager.resume()` 如果事务执行前有事务挂起，那么当前事务执行结束后需要将挂起的事务恢复，挂起事务时保存了原事务信息，重置了当前事务信息，所以恢复操作就是将当前的事务信息设置为之前保存的原事务信息。

`TransactionAspectSupport.cleanupTransactionInfo()`清除当前节点的事务消息，将旧事务节点信息通过thradLoacl更新到当前线程。

### [小结](#小结)

如果方法正常执行完成且没有异常，调用`commitTransactionAfterReturning()`方法。如果执行中出现异常，调用`completeTransactionAfterThrowing()`方法。

两个方法内部都会判断是否存在事务以及是否满足回滚条件来决定最终执行提交操作还是回滚操作。
