{

  "title": ".WrongArgumentException: Malformed database URL, failed to parse the connection string near ';characterEncoding=UTF-8&;serverTimezone=Asia/Shanghai'.)",
  "date": "2019-11-25",
  "description": "连接mysql库报的异常信息： 解决方法 连接的mysql是8.0.18版本，首先更新mysql驱动到对应版本 原先的url 修改后的url",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11928320.html"

}

连接mysql库报的异常信息：

```text
org.springframework.transaction.CannotCreateTransactionException: Could not open JDBC Connection for transaction; nested exception is org.apache.commons.dbcp.SQLNestedException: Cannot create PoolableConnectionFactory (Cannot load connection class because of underlying exception: com.mysql.cj.exceptions.WrongArgumentException: Malformed database URL, failed to parse the connection string near ';characterEncoding=UTF-8&;serverTimezone=Asia/Shanghai'.)
    at org.springframework.jdbc.datasource.DataSourceTransactionManager.doBegin(DataSourceTransactionManager.java:307)
    at org.springframework.transaction.support.AbstractPlatformTransactionManager.getTransaction(AbstractPlatformTransactionManager.java:376)
    at org.springframework.transaction.interceptor.TransactionAspectSupport.createTransactionIfNecessary(TransactionAspectSupport.java:572)
    at org.springframework.transaction.interceptor.TransactionAspectSupport.invokeWithinTransaction(TransactionAspectSupport.java:360)
    at org.springframework.transaction.interceptor.TransactionInterceptor.invoke(TransactionInterceptor.java:99)
    at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
    at org.springframework.aop.interceptor.ExposeInvocationInterceptor.invoke(ExposeInvocationInterceptor.java:93)
    at org.springframework.aop.framework.ReflectiveMethodInvocation.proceed(ReflectiveMethodInvocation.java:186)
    at org.springframework.aop.framework.JdkDynamicAopProxy.invoke(JdkDynamicAopProxy.java:212)
    at com.sun.proxy.$Proxy25.transfer(Unknown Source)
    at com.cyb.ms.service.AccountServiceTest.testTransfer(AccountServiceTest.java:18)
    at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.base/java.lang.reflect.Method.invoke(Method.java:567)
    at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:50)
    at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
    at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:47)
    at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:17)
    at org.springframework.test.context.junit4.statements.RunBeforeTestExecutionCallbacks.evaluate(RunBeforeTestExecutionCallbacks.java:74)
    at org.springframework.test.context.junit4.statements.RunAfterTestExecutionCallbacks.evaluate(RunAfterTestExecutionCallbacks.java:84)
    at org.springframework.test.context.junit4.statements.RunBeforeTestMethodCallbacks.evaluate(RunBeforeTestMethodCallbacks.java:75)
    at org.springframework.test.context.junit4.statements.RunAfterTestMethodCallbacks.evaluate(RunAfterTestMethodCallbacks.java:86)
    at org.springframework.test.context.junit4.statements.SpringRepeat.evaluate(SpringRepeat.java:84)
    at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:325)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:251)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.runChild(SpringJUnit4ClassRunner.java:97)
    at org.junit.runners.ParentRunner$3.run(ParentRunner.java:290)
    at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:71)
    at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:288)
    at org.junit.runners.ParentRunner.access$000(ParentRunner.java:58)
    at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:268)
    at org.springframework.test.context.junit4.statements.RunBeforeTestClassCallbacks.evaluate(RunBeforeTestClassCallbacks.java:61)
    at org.springframework.test.context.junit4.statements.RunAfterTestClassCallbacks.evaluate(RunAfterTestClassCallbacks.java:70)
    at org.junit.runners.ParentRunner.run(ParentRunner.java:363)
    at org.springframework.test.context.junit4.SpringJUnit4ClassRunner.run(SpringJUnit4ClassRunner.java:190)
    at org.eclipse.jdt.internal.junit4.runner.JUnit4TestReference.run(JUnit4TestReference.java:89)
    at org.eclipse.jdt.internal.junit.runner.TestExecution.run(TestExecution.java:41)
    at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.runTests(RemoteTestRunner.java:541)
    at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.runTests(RemoteTestRunner.java:763)
    at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.run(RemoteTestRunner.java:463)
    at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.main(RemoteTestRunner.java:209)
Caused by: org.apache.commons.dbcp.SQLNestedException: Cannot create PoolableConnectionFactory (Cannot load connection class because of underlying exception: com.mysql.cj.exceptions.WrongArgumentException: Malformed database URL, failed to parse the connection string near ';characterEncoding=UTF-8&;serverTimezone=Asia/Shanghai'.)
    at org.apache.commons.dbcp.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:1549)
    at org.apache.commons.dbcp.BasicDataSource.createDataSource(BasicDataSource.java:1388)
    at org.apache.commons.dbcp.BasicDataSource.getConnection(BasicDataSource.java:1044)
    at org.springframework.jdbc.datasource.DataSourceTransactionManager.doBegin(DataSourceTransactionManager.java:263)
    ... 41 more
Caused by: java.sql.SQLNonTransientConnectionException: Cannot load connection class because of underlying exception: com.mysql.cj.exceptions.WrongArgumentException: Malformed database URL, failed to parse the connection string near ';characterEncoding=UTF-8&;serverTimezone=Asia/Shanghai'.
    at com.mysql.cj.jdbc.exceptions.SQLError.createSQLException(SQLError.java:110)
    at com.mysql.cj.jdbc.exceptions.SQLError.createSQLException(SQLError.java:97)
    at com.mysql.cj.jdbc.exceptions.SQLError.createSQLException(SQLError.java:89)
    at com.mysql.cj.jdbc.exceptions.SQLError.createSQLException(SQLError.java:63)
    at com.mysql.cj.jdbc.exceptions.SQLError.createSQLException(SQLError.java:73)
    at com.mysql.cj.jdbc.exceptions.SQLExceptionsMapping.translateException(SQLExceptionsMapping.java:79)
    at com.mysql.cj.jdbc.exceptions.SQLExceptionsMapping.translateException(SQLExceptionsMapping.java:131)
    at com.mysql.cj.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:219)
    at org.apache.commons.dbcp.DriverConnectionFactory.createConnection(DriverConnectionFactory.java:38)
    at org.apache.commons.dbcp.PoolableConnectionFactory.makeObject(PoolableConnectionFactory.java:582)
    at org.apache.commons.dbcp.BasicDataSource.validateConnectionFactory(BasicDataSource.java:1556)
    at org.apache.commons.dbcp.BasicDataSource.createPoolableConnectionFactory(BasicDataSource.java:1545)
    ... 44 more
Caused by: com.mysql.cj.exceptions.UnableToConnectException: Cannot load connection class because of underlying exception: com.mysql.cj.exceptions.WrongArgumentException: Malformed database URL, failed to parse the connection string near ';characterEncoding=UTF-8&;serverTimezone=Asia/Shanghai'.
    at java.base/jdk.internal.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
    at java.base/jdk.internal.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
    at java.base/jdk.internal.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
    at java.base/java.lang.reflect.Constructor.newInstanceWithCaller(Constructor.java:500)
    at java.base/java.lang.reflect.Constructor.newInstance(Constructor.java:481)
    at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:61)
    at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:105)
    ... 49 more
Caused by: com.mysql.cj.exceptions.WrongArgumentException: Malformed database URL, failed to parse the connection string near ';characterEncoding=UTF-8&;serverTimezone=Asia/Shanghai'.
    at java.base/jdk.internal.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
    at java.base/jdk.internal.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
    at java.base/jdk.internal.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
    at java.base/java.lang.reflect.Constructor.newInstanceWithCaller(Constructor.java:500)
    at java.base/java.lang.reflect.Constructor.newInstance(Constructor.java:481)
    at com.mysql.cj.exceptions.ExceptionFactory.createException(ExceptionFactory.java:61)
    at com.mysql.cj.conf.ConnectionUrlParser.processKeyValuePattern(ConnectionUrlParser.java:539)
    at com.mysql.cj.conf.ConnectionUrlParser.parseQuerySection(ConnectionUrlParser.java:519)
    at com.mysql.cj.conf.ConnectionUrlParser.getProperties(ConnectionUrlParser.java:644)
    at com.mysql.cj.conf.ConnectionUrl.collectProperties(ConnectionUrl.java:303)
    at com.mysql.cj.conf.ConnectionUrl.<init>(ConnectionUrl.java:288)
    at com.mysql.cj.conf.url.SingleConnectionUrl.<init>(SingleConnectionUrl.java:47)
    at java.base/jdk.internal.reflect.NativeConstructorAccessorImpl.newInstance0(Native Method)
    at java.base/jdk.internal.reflect.NativeConstructorAccessorImpl.newInstance(NativeConstructorAccessorImpl.java:62)
    at java.base/jdk.internal.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
    at java.base/java.lang.reflect.Constructor.newInstanceWithCaller(Constructor.java:500)
    at java.base/java.lang.reflect.Constructor.newInstance(Constructor.java:481)
    at com.mysql.cj.util.Util.handleNewInstance(Util.java:192)
    at com.mysql.cj.util.Util.getInstance(Util.java:167)
    at com.mysql.cj.util.Util.getInstance(Util.java:174)
    at com.mysql.cj.conf.ConnectionUrl.getConnectionUrlInstance(ConnectionUrl.java:200)
    at com.mysql.cj.jdbc.NonRegisteringDriver.connect(NonRegisteringDriver.java:196)
    ... 48 more
```

解决方法

连接的mysql是8.0.18版本，首先更新mysql驱动到对应版本

```text
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.18</version>
        </dependency>
```

原先的url

```text
jdbc:mysql://localhost:3306/demo?useUnicode=true&;characterEncoding=UTF-8&;serverTimezone=Asia/Shanghai
```

修改后的url

```text
jdbc:mysql://localhost:3306/demo?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai
```
