{

  "title": "MyBatis中SqlSession背后的秘密",
  "has_date": true,
  "description": "sqlSessionFactory 与 SqlSession 正如其名，Sqlsession对应着一次数据库会话。由于数据库会话不是永久的，因此Sqlsession的生命周期也不应该是永久的，相反，在你每次访问数据库时都需要创建它（当然并不是说在Sqlsession里只能执行一次sql，你可以执行多",
  "tags": [
    "框架",
    "ORM"
  ],
  "source": "local-markdown-library",
  "source_path": "framework/orm/mybatis-sqlsessionexecutionprocess - MyBatis中SqlSession背后的秘密.md",
  "date": "2025-05-17"

}

## [sqlSessionFactory 与 SqlSession](#sqlsessionfactory-与-sqlsession)

正如其名，Sqlsession对应着一次数据库会话。由于数据库会话不是永久的，因此Sqlsession的生命周期也不应该是永久的，相反，在你每次访问数据库时都需要创建它（当然并不是说在Sqlsession里只能执行一次sql，你可以执行多次，当一旦关闭了Sqlsession就需要重新创建它）。

那么咱们就先看看是怎么获取SqlSession的吧：
![](/imported/markdown/2025-05-17-markdown-b1f1e10e-mybatis中sqlsession背后的秘密/images/4666fe9e5411-202404291758405.jpeg)
首先，SqlSessionFactoryBuilder去读取mybatis的配置文件，然后build一个DefaultSqlSessionFactory。源码如下：

当我们获取到SqlSessionFactory之后，就可以通过SqlSessionFactory去获取SqlSession对象。源码如下：

通过以上步骤，咱们已经得到SqlSession对象了。接下来就是该干嘛干嘛去了（话说还能干嘛，当然是执行sql语句咯）。看了上面，咱们也回想一下之前写的Demo：

创建Sqlsession的地方只有一个，那就是SqlsessionFactory的openSession方法：

我们可以看到实际创建SqlSession的地方是openSessionFromDataSource，如下：

可以看出，创建sqlsession经过了以下几个主要步骤：

- 从配置中获取Environment；

- 从Environment中取得DataSource；

- 从Environment中取得TransactionFactory；

- 从DataSource里获取数据库连接对象Connection；

- 在取得的数据库连接上创建事务对象Transaction；

- 创建Executor对象（该对象非常重要，事实上sqlsession的所有操作都是通过它完成的）；

- 创建sqlsession对象。

SqlSession咱们也拿到了，咱们可以调用SqlSession中一系列的select..., insert..., update..., delete...方法轻松自如的进行CRUD操作了。就这样？那咱配置的映射文件去哪儿了？别急，咱们接着往下看。

## [MapperProxy](#mapperproxy)
![](/imported/markdown/2025-05-17-markdown-b1f1e10e-mybatis中sqlsession背后的秘密/images/8d752527966c-202404291758358.png)
在mybatis中，通过MapperProxy动态代理咱们的dao， 也就是说， 当咱们执行自己写的dao里面的方法的时候，其实是对应的mapperProxy在代理。那么，咱们就看看怎么获取MapperProxy对象吧：

通过SqlSession从Configuration中获取。源码如下：

SqlSession把包袱甩给了Configuration, 接下来就看看Configuration。源码如下：

接着调用了MapperRegistry，源码如下：

MapperProxyFactory源码：

通过以上的动态代理，咱们就可以方便地使用dao接口啦， 就像之前咱们写的demo那样：

这下方便多了吧， 呵呵， 貌似mybatis的源码就这么一回事儿啊。具体详细介绍，请参见MyBatis Mapper 接口如何通过JDK动态代理来包装SqlSession 源码分析。别急，还没完， 咱们还没看具体是怎么执行sql语句的呢。

## [Excutor](#excutor)

Executor与Sqlsession的关系就像市长与书记，Sqlsession只是个门面，真正干事的是Executor，Sqlsession对数据库的操作都是通过Executor来完成的。与Sqlsession一样，Executor也是动态创建的：
![](/imported/markdown/2025-05-17-markdown-b1f1e10e-mybatis中sqlsession背后的秘密/images/cd628ce8da34-202404291758891.png)

- **Executor创建的源代码**：

可以看出，

- 如果不开启cache的话，创建的Executor是3种基础类型之一

  - BatchExecutor专门用于执行批量sql操作

  - ReuseExecutor会重用statement执行sql操作

  - SimpleExecutor只是简单执行sql没有什么特别的

- 开启cache的话（默认是开启的并且没有任何理由去关闭它），就会创建CachingExecutor，它以前面创建的Executor作为唯一参数。CachingExecutor在查询数据库前先查找缓存，若没找到的话调用delegate（就是构造时传入的Executor对象）从数据库查询，并将查询结果存入缓存中。

Executor对象是可以被插件拦截的，如果定义了针对Executor类型的插件，最终生成的Executor对象是被各个插件插入后的代理对象。

接下来，去看sql的执行过程。上面，拿到了MapperProxy, 每个MapperProxy对应一个dao接口， 那么在使用的时候，MapperProxy是怎么做的呢？

- **MapperProxy**

我们知道对被代理对象的方法的访问都会落实到代理者的invoke上来，MapperProxy的invoke如下：

- **MapperMethod**

就像是一个分发者，他根据参数和返回值类型选择不同的sqlsession方法来执行。这样mapper对象与sqlsession就真正的关联起来了。

既然又回到SqlSession了，前面提到过，sqlsession只是一个门面，真正发挥作用的是executor，对sqlsession方法的访问最终都会落到executor的相应方法上去。Executor分成两大类，一类是CacheExecutor，另一类是普通Executor。Executor的创建前面已经介绍了，那么咱们就看看SqlSession的CRUD方法了，为了省事，还是就选择其中的一个方法来做分析吧。这儿，咱们选择了selectList方法：

- **CacheExecutor**

CacheExecutor有一个重要属性delegate，它保存的是某类普通的Executor，值在构照时传入。执行数据库update操作时，它直接调用delegate的update方法，执行query方法时先尝试从cache中取值，取不到再调用delegate的查询方法，并将查询结果存入cache中。代码如下：

- **普通Executor**

有3类，他们都继承于BaseExecutor

- BatchExecutor专门用于执行批量sql操作

- ReuseExecutor会重用statement执行sql操作

- SimpleExecutor只是简单执行sql没有什么特别的

下面以SimpleExecutor为例：

然后，通过一层一层的调用，最终会来到doQuery方法， 这儿咱们就随便找个Excutor看看doQuery方法的实现吧，我这儿选择了SimpleExecutor:

Mybatis内置的ExecutorType有3种，默认的是simple，该模式下它为每个语句的执行创建一个新的预处理语句，单条提交sql；而batch模式重复使用已经预处理的语句， 并且批量执行所有更新语句，显然batch性能将更优；

但batch模式也有自己的问题，比如在Insert操作时，在事务没有提交之前，是没有办法获取到自增的id，这在某型情形下是不符合业务要求的；

通过走码和研读spring相关文件发现，在同一事务中batch模式和simple模式之间无法转换，由于本项目一开始选择了simple模式，所以碰到需要批量更新时，只能在单独的事务中进行；

在代码中使用batch模式可以使用以下方式：

上述代码没有使用spring的事务，改手动控制，如果和原spring事务一起使用，将无法回滚，必须注意，最好单独使用；

## [StatementHandler](#statementhandler)

可以看出，Executor本质上也没有进行处理，具体的事情原来是StatementHandler来完成的。当Executor将指挥棒交给StatementHandler后，接下来的工作就是StatementHandler的事了。我们先看看StatementHandler是如何创建的：

可以看到每次创建的StatementHandler都是RoutingStatementHandler，它只是一个分发者，他一个属性delegate用于指定用哪种具体的StatementHandler。可选的StatementHandler有SimpleStatementHandler、PreparedStatementHandler和CallableStatementHandler三种。选用哪种在mapper配置文件的每个statement里指定，默认的是PreparedStatementHandler。同时还要注意到StatementHandler是可以被拦截器拦截的，和Executor一样，被拦截器拦截后的对像是一个代理对象。由于mybatis没有实现数据库的物理分页，众多物理分页的实现都是在这个地方使用拦截器实现的，本文作者也实现了一个分页拦截器，在后续的章节会分享给大家，敬请期待。

StatementHandler创建后需要执行一些初始操作，比如statement的开启和参数设置、对于PreparedStatement还需要执行参数的设置操作等。代码如下：

statement的开启和参数设置没什么特别的地方，handler.parameterize倒是可以看看是怎么回事。handler.parameterize通过调用ParameterHandler的setParameters完成参数的设置，ParameterHandler随着StatementHandler的创建而创建，默认的实现是DefaultParameterHandler：

同Executor和StatementHandler一样，ParameterHandler也是可以被拦截的。DefaultParameterHandler里设置参数的代码如下：

这里面最重要的一句其实就是最后一句代码，它的作用是用合适的TypeHandler完成参数的设置。那么什么是合适的TypeHandler呢，它又是如何决断出来的呢？BaseStatementHandler的构造方法里有这么一句：

它触发了sql 的解析，在解析sql的过程中，TypeHandler也被决断出来了，决断的原则就是根据参数的类型和参数对应的JDBC类型决定使用哪个TypeHandler。比如：参数类型是String的话就用StringTypeHandler，参数类型是整数的话就用IntegerTypeHandler等。

参数设置完毕后，执行数据库操作（update或query）。如果是query最后还有个查询结果的处理过程。

接下来，咱们看看StatementHandler 的一个实现类 PreparedStatementHandler（这也是我们最常用的，封装的是PreparedStatement）, 看看它使怎么去处理的：

结果处理使用ResultSetHandler来完成，默认的ResultSetHandler是FastResultSetHandler，它在创建StatementHandler时一起创建，代码如下：

可以看出ResultSetHandler也是可以被拦截的，可以编写自己的拦截器改变ResultSetHandler的默认行为。ResultSetHandler内部一条记录一条记录的处理，在处理每条记录的每一列时会调用TypeHandler转换结果，如下：

从代码里可以看到，决断TypeHandler使用的是结果参数的属性类型。因此我们在定义作为结果的对象的属性时一定要考虑与数据库字段类型的兼容性。到此， 一次sql的执行流程就完了。
