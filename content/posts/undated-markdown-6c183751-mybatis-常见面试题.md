{

  "title": "MyBatis 常见面试题",
  "has_date": false,
  "description": "Mybatis基础 Mybatis是什么？ MyBatis框架是一个开源的数据持久层框架。 它的内部封装了通过JDBC访问数据库的操作，支持普通的SQL查询、存储过程和高级映射，几乎消除了所有的JDBC代码和参数的手工设置以及结果集的检索。 MyBatis作为持久层框架，其主要思想是将程序中的大量S",
  "tags": [
    "面试",
    "框架"
  ],
  "source": "local-markdown-library",
  "source_path": "interview/framework/mybatis - MyBatis 常见面试题.md"

}

---

## [Mybatis基础](#mybatis基础)

### [Mybatis是什么？](#mybatis是什么)

- MyBatis框架是一个开源的数据持久层框架。

- 它的内部封装了通过JDBC访问数据库的操作，支持普通的SQL查询、存储过程和高级映射，几乎消除了所有的JDBC代码和参数的手工设置以及结果集的检索。

- MyBatis作为持久层框架，其主要思想是将程序中的大量SQL语句剥离出来，配置在配置文件当中，实现SQL的灵活配置。

- 这样做的好处是将SQL与程序代码分离，可以在不修改代码的情况下，直接在配置文件当中修改SQL。

### [为什么使用Mybatis代替JDBC？](#为什么使用mybatis代替jdbc)

MyBatis 是一种优秀的 ORM（Object-Relational Mapping）框架，与 JDBC 相比，有以下几点优势：

1. 简化了 JDBC 的繁琐操作：使用 JDBC 进行数据库操作需要编写大量的样板代码，如获取连接、创建 Statement/PreparedStatement，设置参数，处理结果集等。而使用 MyBatis 可以将这些操作封装起来，通过简单的配置文件和 SQL 语句就能完成数据库操作，从而大大简化了开发过程。

1. 提高了 SQL 的可维护性：使用 JDBC 进行数据库操作，SQL 语句通常会散布在代码中的各个位置，当 SQL 语句需要修改时，需要找到所有使用该语句的地方进行修改，这非常不方便，也容易出错。而使用 MyBatis，SQL 语句都可以集中在配置文件中，可以更加方便地修改和维护，同时也提高了 SQL 语句的可读性。

1. 支持动态 SQL：MyBatis 提供了强大的动态 SQL 功能，可以根据不同的条件生成不同的 SQL 语句，这对于复杂的查询操作非常有用。

1. 易于集成：MyBatis 可以与 Spring 等流行的框架集成使用，可以通过 XML 或注解配置进行灵活的配置，同时 MyBatis 也提供了非常全面的文档和示例代码，学习和使用 MyBatis 非常方便。

综上所述，使用 MyBatis 可以大大简化数据库操作的代码，提高 SQL 语句的可维护性和可读性，同时还提供了强大的动态 SQL 功能，易于集成使用。因此，相比于直接使用 JDBC，使用 MyBatis 更为便捷、高效和方便。

然而，也要注意一些缺点：

- 虽然 MyBatis 很强大，但编写 SQL 语句可能会相对繁琐，特别是当涉及多个字段或多个关联表时。这就要求开发人员在 SQL 编写方面有一定的功底。

- 由于 SQL 语句依赖于特定的数据库，如果想要更换数据库，移植性就会受到影响。这意味着不能轻易地更改数据库，可能需要进行一些适应性的修改。

### [ORM是什么](#orm是什么)

ORM（Object Relational Mapping），对象关系映射，是一种为了解决关系型数据库数据与简单Java对象（POJO）的映射关系的技术。简单的说，ORM是通过使用描述对象和数据库之间映射的元数据，将程序中的对象自动持久化到关系型数据库中。

### [Mybatis和Hibernate的区别？](#mybatis和hibernate的区别)

主要有以下几点区别：

1. Hibernate的**开发难度**大于MyBatis，主要由于Hibernate比较复杂，庞大，学习周期比较长。

1. Hibernate属于**全自动**ORM映射工具，使用Hibernate查询关联对象或者关联集合对象时，可以根据对象关系模型直接获取，所以它是全自动的。而Mybatis在查询关联对象或关联集合对象时，需要手动编写sql来完成，所以，称之为半自动ORM映射工具。

1. **数据库扩展性**的区别。Hibernate与数据库具体的关联在XML中，所以HQL对具体是用什么数据库并不是很关心。MyBatis由于所有sql都是依赖数据库书写的，所以扩展性、迁移性比较差。

1. **缓存机制**的区别。Hibernate的二级缓存配置在SessionFactory生成配置文件中进行详细配置，然后再在具体的表对象映射中配置那种缓存。MyBatis的二级缓存配置都是在每个具体的表对象映射中进行详细配置，这样针对不同的表可以自定义不同的缓冲机制，并且MyBatis可以在命名空间中共享相同的缓存配置和实例，通过Cache-ref来实现。

1. **日志系统完善性**的区别。Hibernate日志系统非常健全，涉及广泛，而Mybatis则除了基本记录功能外，功能薄弱很多。

1. **sql的优化上，Mybatis要比Hibernate方便很多**。由于Mybatis的sql都是写在xml里，因此优化sql比Hibernate方便很多。而Hibernate的sql很多都是自动生成的，无法直接维护sql；总之写sql的灵活度上Hibernate不及Mybatis。

### [MyBatis 与 JPA 有哪些不同？](#mybatis-与-jpa-有哪些不同)

JPA是Java Persistence API的简称，中文名Java持久层API，是JDK 5.0注解或XML描述对象－关系表的映射关系，并将运行期的实体对象持久化到数据库中。

首先，我们来聊聊编程模型。MyBatis和JPA采用了不同的方式来处理数据操作。

- MyBatis使用基于SQL的编程模型，这意味着开发人员需要自己编写SQL语句，并将它们映射到Java方法。这给开发人员提供了更大的灵活性，可以精确地控制SQL的编写和执行过程。

- JPA则采用了基于对象的编程模型，你只需定义实体类并使用注解或XML配置来将实体映射到数据库表。JPA会自动生成SQL语句，开发人员不必过多关心底层SQL的细节。

其次，我们来看一下SQL控制。

- 在MyBatis中，可以编写和优化SQL语句，这在需要特定优化或使用数据库特性时非常有用。

- JPA则将大部分SQL细节隐藏起来，自动生成SQL语句。这使得开发人员无需深入了解底层SQL，但在某些情况下可能会影响性能或限制你的操作。

接下来是灵活性和控制

- MyBatis提供了更多的灵活性，适用于需要定制化SQL查询或调用存储过程的场景。

- JPA则提供了更高层次的抽象，用于简化常见数据库操作。然而，这也可能会在某些高级或复杂情况下产生一些限制。

关于查询语言

- MyBatis使用原生SQL作为查询语言，这要求开发人员对SQL有一定了解。

- JPA则引入了JPQL作为查询语言，它更加面向对象，类似于SQL，但操作的是实体对象。

在缓存方面

- MyBatis的缓存控制更精细，可以更准确地控制缓存行为。

- JPA也支持缓存，但通常对缓存的控制较少，更多地由框架自动管理。

总的来说，选择使用MyBatis还是JPA取决于项目需求和团队技术背景。如果你需要更多的SQL控制和定制化，MyBatis可能更适合；如果你希望更快速地进行常见数据库操作，JPA可能更适合

### [为什么说 Mybatis 是半ORM 映射工具？](#为什么说-mybatis-是半orm-映射工具)

首先，Mybatis被称为半ORM框架是因为它在数据库操作方面提供了一些对象关系映射的功能，但相对于全ORM框架，它更加灵活和轻量级。在Mybatis中，我们需要手动编写SQL来执行数据库操作，这跟传统的JDBC方式有点类似。但是，Mybatis通过映射文件来实现Java对象与数据库表之间的映射，这就是它的ORM特性。

区别的话，全ORM框架通常更加自动化，它会完全代替你来生成SQL语句，进行数据库操作。这在某些情况下能够提高开发效率，因为你不需要写太多的SQL代码。但是，全ORM框架也可能在性能方面略有影响，因为它们可能会生成复杂的SQL语句，导致查询效率下降。

相比之下，Mybatis更加灵活，你可以精确地控制要执行的SQL语句，这对于需要优化查询性能的场景很有帮助。另外，Mybatis在映射文件中可以明确指定每个字段的映射关系，这样你能更好地控制数据库表和Java对象之间的对应关系。

### [MyBatis框架的优缺点及其适用的场合](#mybatis框架的优缺点及其适用的场合)

**优点**

1. 与JDBC相比，减少了50%以上的代码量。

1. MyBatis是易学的持久层框架，小巧并且简单易学。

1. MyBatis相当灵活，不会对应用程序或者数据库的现有设计强加任何影响，SQL写在XML文件里，从程序代码中彻底分离，降低耦合度，便于统一的管理和优化，并可重用。

1. 提供XML标签，支持编写动态的SQL，满足不同的业务需求。

1. 提供映射标签，支持对象与数据库的ORM字段关系映射。

**缺点**

1. SQL语句的编写工作量较大，对开发人员编写SQL的能力有一定的要求。

1. SQL语句依赖于数据库，导致数据库不具有好的移植性，不可以随便更换数据库。

**适用场景**

MyBatis专注于SQL自身，是一个足够灵活的DAO层解决方案。对性能的要求很高，或者需求变化较多的项目，例如Web项目，那么MyBatis是不二的选择。

## [Mybatis原理](#mybatis原理)

### [MyBatis的核心组件有哪些？](#mybatis的核心组件有哪些)

- SqlSessionFactoryBuilder：是创建 SqlSessionFactory 的构建器。它使用配置文件或配置类来创建 SqlSessionFactory。SqlSessionFactoryBuilder 本身是一个工具类，通常在应用程序启动时使用一次，之后就可以丢弃。

- SqlSessionFactory，是一个会话工厂，同时也承担了配置数据库连接信息和事务管理的功能。它的任务是创建 SqlSession 对象，这个对象是我们与数据库交互的主要途径。一旦这个工厂被建立起来，它就会加载一些必要的配置和映射文件，为后续的数据库操作提供一个可靠的基础。

- SqlSession，是业务与数据库交互的窗口，能够执行 SQL 语句，提交或回滚事务，还可以获取 Mapper 接口的实例。不过需要注意的是，SqlSession 的生命周期是短暂的，通常在数据库操作完成后就应该关闭它，这样可以释放资源。

- Mapper 接口，MyBatis 通过动态代理的方式，把接口方法和映射文件中的 SQL 语句关联起来，这样我们就可以方便地通过接口来执行数据库操作。

- Mapper 映射文件，可以定义 SQL 语句、参数映射、结果映射等等。里面的 SQL 语句可以包括增删改查等操作，MyBatis 会根据我们调用的方法来选择正确的 SQL 语句来执行。

- Type Handlers：负责将预处理语句中的参数从 Java 类型转换为 JDBC 类型，以及将结果集中的列从 JDBC 类型转换为 Java 类型。MyBatis 内置了许多默认的 Type Handlers，并且允许用户自定义 Type Handler。

- Result Maps：描述了数据库结果集与对象属性之间的映射关系。这是 MyBatis 中最强大的特性之一，允许你处理复杂的映射场景，如嵌套结果和关联查询。

- Caching： MyBatis 支持一级缓存和二级缓存。一级缓存默认开启，作用范围是同一个 SqlSession；二级缓存需要手动配置，可以在不同的 SqlSession 之间共享缓存数据，提高系统性能。

- Transaction Manager：MyBatis 提供了一个简单的事务管理机制，可以与 Spring 框架的事务管理集成。这使得开发者能够以声明式的方式管理事务，而不是编程式地处理事务逻辑。

### [Mybatis的工作原理](#mybatis的工作原理)

- 读取MyBatis配置文件：mybatis-config.xml为MyBatis的全局配置文件，配置了MyBatis的运行环境等信息，例如数据库连接信息。

- 加载映射文件。映射文件即SQL映射文件，该文件中配置了操作数据库的SQL语句，需要在MyBatis配置文件mybatis-config.xml中加载。mybatis-config.xml文件可以加载多个映射文件，每个文件对应数据库中的一张表。

- 构造会话工厂：通过MyBatis的环境等配置信息构建会话工厂SqlSessionFactory。

- 创建会话对象：由会话工厂创建SqlSession对象，该对象中包含了执行SQL语句的所有方法。

- 执行SQL语句：MyBatis底层定义了一个Executor 接口来操作数据库，它将根据SqlSession传递的参数动态地生成需要执行的SQL语句，同时负责查询缓存的维护。

- MappedStatement 对象：在Executor接口的执行方法中有一个MappedStatement类型的参数，该参数是对映射信息的封装，用于存储要映射的SQL语句的id、参数等信息。

- 输入参数映射：输入参数类型可以是Map、List等集合类型，也可以是基本数据类型和POJO类型。输入参数映射过程类似于 JDBC对preparedStatement对象设置参数的过程。

- 输出结果映射：输出结果类型可以是Map、List等集合类型，也可以是基本数据类型和POJO类型。输出结果映射过程类似于 JDBC对结果集的解析过程。

### [能详细说说 MyBatis 的执行流程吗?](#能详细说说-mybatis-的执行流程吗)

MyBatis 的执行原理基于其核心设计思想：通过映射文件(XML 或注解)将 SQL 语句与 Java 对象进行绑定,整个执行流程可以分为以下几个步骤：

1. SqlSessionFactory 的创建：MyBatis 的执行过程从 SqlSessionFactory 开始。SqlSessionFactory 是一个工厂类，负责创建 SqlSession实例，SqlSession 是 MyBatis 与数据库交互的核心对象。SqlSessionFactory 是通过 SqlSessionFactoryBuilder 构建的(通常是通过读取 MyBatis 配置文件 mybatis-config.xml 来初始化)。

1. Sqlsession 的获取：SqlSessionFactory 通过 openSsesion()方法获取一个 SqlSession 对象，Sqlsession 是操作数据库的主要入口，用户通过它执行SQL语句、提交事务等。

1. 执行映射语句：当调用sqlsession的方法(例如selectone、selectlist、insert、update、delete 等)时，MyBatis 会根据传入的 SQL映射语句的 ID，去寻找对应的 SQL语句执行。

1. 命名空间和映射语句的查询：SQL映射语句通过映射文件中的 namespace 和 id 进行定位。MyBatis 会将映射文件解析成一个 MappedStateanent 对象，MappedStateanent 保存了SQL语句、参数类型、返回类型等信息。

1. 参数封装和 SQL语句执行：在SQL执行前，MyBatis会根据映射文件中配置的 parameterType 类型，将传入的参数封装成适当的时象(例如，使用 JavaBean、Map、XML格式等。然后，MyBatis 会很据不同的执行环境(如 MySQL、Oracle 等数据库)，将 SQL语句执行到数据库中，并将查询结果通过映射文件中配置的 resultType 类型返回。

1. 返回结果的映射：MyBatis会将查询结果根据resultType或 resulMap进行转换，将查询结果转换成Java 对象(如List、Map 或指定的 POJO 类)。

1. 事务管理：Matis的事务管理通过 Sqlsession 来处理，Sqlsession 提供了事务的提交和回滚方法，当调用 Sqlsession.commit()时，SQL执行的结果会被提交到数据库；若发生异常，Sqlsession.roolback()，事务会被回滚。

1. 最后关闭 SqlSession：在操作完成后，Sqlsession 会通过 close()方法关闭，释放数据库连接和资源。

### [简述 MyBatis 的插件运行原理，Mybatis的插件能够在哪些地方进行拦截？](#简述-mybatis-的插件运行原理-mybatis的插件能够在哪些地方进行拦截)

MyBatis 的插件机制是通过 动态代理 实现的，主要是在 SQL 执行的关键点(如执行查询、更新、插入)拦截操作并增强功能。

MyBatis的插件可以在MyBatis的执行过程中的多个关键点进行拦截和干预。这些关键点包括：

1. Executor（执行器）层面的拦截： 这是SQL语句的执行层面，插件可以在SQL语句执行前后进行拦截。这包括了SQL的预处理、参数设置、查询结果的映射等。

1. StatementHandler（语句处理器）层面的拦截： 这是对SQL语句的处理层面，插件可以在SQL语句被执行之前进行拦截，你可以在这里修改、替换、生成SQL语句。

1. ParameterHandler（参数处理器）层面的拦截： 这是处理参数的层面，插件可以在参数传递给SQL语句之前进行拦截，你可以在这里修改参数值。

1. ResultSetHandler（结果集处理器）层面的拦截： 这是处理查询结果的层面，插件可以在查询结果返回给调用方之前进行拦截，你可以在这里对查询结果进行修改、处理。

Mybatis使用JDK的动态代理，为需要拦截的接口生成代理对象以实现接口方法拦截功能，每当执行这4种接口对象的方法时，就会进入拦截方法，具体就是`InvocationHandler`的invoke()方法，当然，只会拦截那些你指定需要拦截的方法。

### [如何编写一个插件？](#如何编写一个插件)

插件机制的核心是Interceptor接口，你可以实现这个接口，编写自己的插件逻辑。一个插件主要包括以下几个步骤：

1. 实现Interceptor接口： 创建一个类，实现MyBatis提供的Interceptor接口，该接口包含了intercept和plugin两个方法。

1. 实现intercept方法： intercept方法是插件的核心，它会在方法执行前后进行拦截。你可以在这个方法中编写自己的逻辑。

1. 实现plugin方法： plugin方法用于创建代理对象，将插件包装在目标对象上，使得插件逻辑能够被执行。

1. 配置插件： 在MyBatis的配置文件中，通过`&lt;plugins&gt;`标签配置你的插件。通常需要指定插件类和一些参数。

### [Mybatis 是如何进行分页的？](#mybatis-是如何进行分页的)

Mybatis 使用 RowBounds 对象进行分页，它是针对 ResultSet 结果集执行的内存分页，而非物理分页，先把数据都查出来，然后再做分页。

可以在 sql 内直接书写带有物理分页的参数来完成物理分页功能，也可以使用分页插件来完成物理分页。

常用的分页插件和技巧：

1. PageHelper 插件： PageHelper 是一个流行的 MyBatis 分页插件，它简化了分页查询的操作。只需要在查询方法前调用 PageHelper.startPage(pageNum, pageSize)，然后执行查询语句，PageHelper 就会自动处理分页逻辑。

1. 使用 RowBounds： 在 MyBatis 中，你还可以使用 RowBounds 对象来实现分页查询。通过在查询方法中传递一个 RowBounds 对象，你可以指定从哪一行开始取数据，以及每页显示多少条数据。

1. 自定义分页插件： 如果你有特殊的分页需求，你可以编写自己的分页插件。这可能涉及到在 MyBatis 的拦截器链中插入你自己的逻辑，以实现定制化的分页处理。

### [分页插件的基本原理是什么？](#分页插件的基本原理是什么)

分页插件是一种扩展机制，它允许MyBatis在查询过程中，自动应用分页逻辑而不需要手动编写分页查询语句。分页插件的一般原理如下：

1. 拦截器(Interceptor)：分页插件实际上是MyBatis的一个拦截器，它可以在查询被执行之前或之后进行干预。

1. 处理分页逻辑：在查询执行之前，分页插件会检测是否有分页参数传入。如果有分页参数，插件会根据数据库方言生成适当的分页查询语句。

1. 修改查询参数：插件会修改查询的SQL语句，添加分页的限制条件。同时，它还会修改参数对象，将分页参数替换为实际的分页偏移量（offset）和每页条数（limit）。

1. 执行查询：修改后的查询语句被执行，得到查询结果。

1. 封装分页结果：插件会根据查询结果和分页参数，将查询结果进行切割，得到分页后的结果。

分页插件的基本原理是使用 Mybatis 提供的插件接口，实现自定义插件，在插件的拦截方法内拦截待执行的 sql，然后重写 sql（SQL 拼接 limit），根据 dialect 方言，添加对应的物理分页语句和物理分页参数，用到了 **JDK 动态代理**，用到了**责任链设计模式**。

### [Mybatis 是否支持延迟加载？](#mybatis-是否支持延迟加载)

所谓的延迟加载，其实就是一种优化方法，目标是为了在查数据库的时候，尽量不读取多余的数据，从而提高我们应用的表现和节约资源。在MyBatis里，这个延迟加载的技巧主要是用在处理对象关系映射的时候，也就是ORM。

来个例子帮你理解：假设有两张表，一张是订单表，另一张是商品表。每个订单下面可能有好几个商品。用延迟加载的话，当我们查一个订单的时候，MyBatis不会马上查出这个订单的所有商品，而是等到我们真的要用商品的数据时才去查。这样做就避免了在查订单的时候额外加载了一堆没用的商品。但要注意，虽然延迟加载能提升性能，可别用得过了，免得碰上懒加载的N+1问题，就是要查很多次才能拿到关联数据，结果性能就拖垮了。所以用延迟加载的时候，得根据实际情况合理配置和使用。

Mybatis 仅支持 association 关联对象和 collection 关联集合对象的延迟加载，association 指的就是一对一，collection 指的就是一对多查询。在 Mybatis 配置文件中，可以配置是否启用延迟加载`lazyLoadingEnabled=true|false`。

### [延迟加载的基本原理是什么？](#延迟加载的基本原理是什么)

延迟加载的基本原理是，使用 CGLIB 创建目标对象的代理对象，当调用目标方法时，进入拦截器方法。

比如调用`a.getB().getName()`，拦截器 invoke()方法发现 a.getB()是 null 值，那么就会单独发送事务，先保存好的查询关联 B 对象的 sql，把 B 查询上来，然后调用`a.setB(b)`，于是 a 的对象 b 属性就有值了，接着完成`a.getB().getName()`方法的调用。

当然了，不光是 Mybatis，几乎所有的ORM框架、包括 Hibernate，支持延迟加载的原理都是一样的。

### [MyBatis如何处理懒加载和预加载？](#mybatis如何处理懒加载和预加载)

当谈到MyBatis中的懒加载和预加载时，我们实际上在讨论在获取数据库数据时如何处理关联对象的加载方式。

懒加载是一种延迟加载技术，它在需要访问关联对象的时候才会加载相关数据。这意味着，当你从数据库中获取一个主对象时，它的关联对象并不会立即加载到内存中，只有当你实际调用访问关联对象的方法时，MyBatis才会去数据库中加载并填充这些关联对象的数据。懒加载适用于关联对象较多或者关联对象数据较大的情况，这样可以减少不必要的数据库查询，提升性能。

预加载则是一种在获取主对象时同时加载其关联对象的技术。这样一来，当获取主对象时，它的所有关联对象也会被一并加载到内存中，避免了多次数据库查询。预加载适用于你确定在后续使用中肯定会访问关联对象，这样可以减少每次访问关联对象时的延迟。

选择懒加载还是预加载取决于具体需求和场景。如果希望在尽量少的数据库查询次数下获取数据，懒加载是个不错的选择。如果在获取主对象后会频繁地访问其关联对象，预加载可能更适合，因为它可以减少多次查询带来的性能开销。

两者都是优化数据库访问性能的手段，根据具体的使用场景选择合适的加载方式非常重要。

### [#{}和${}的区别是什么？](#和-的区别是什么)

#{ } 被解析成预编译语句，预编译之后可以直接执行，不需要重新编译sql。

${ } 仅仅为一个字符串替换，每次执行sql之前需要进行编译，存在 sql 注入问题。

### [where 1=1会不会影响性能？](#where-1-1会不会影响性能)

where 1=1 和 `&lt;where&gt;` 标签 两种方案，该如何选择？

- 如果 MySQL Server版本小于 5.7，用了 MyBatis的话，建议使用`&lt;where&gt;` 标签。

- 如果 MySQL版本大于等于 5.7，两个随便选；因为在MySQL5.7后，有一个所谓的（常量折叠优化）可以在编译期消除重言式表达式。

  - 什么是重言式表达式，就是任何时候永远都为true的结果， 就会被优化器识别并优化掉，好奇的话你可以通过show warnings 查看，就会发现1=1没有了。

当然现在 MySQL Server版本基本都是 5.7以上了，不是的话那赶紧升级吧还是。

### [Mybatis的预编译](#mybatis的预编译)

数据库接受到sql语句之后，需要词法和语义解析，优化sql语句，制定执行计划。这需要花费一些时间。如果一条sql语句需要反复执行，每次都进行语法检查和优化，会浪费很多时间。预编译语句就是将sql语句中的`值用占位符替代`，即将`sql语句模板化`。一次编译、多次运行，省去了解析优化等过程。

mybatis是通过`PreparedStatement`和占位符来实现预编译的。

mybatis底层使用`PreparedStatement`，默认情况下，将对所有的 sql 进行预编译，将#{}替换为?，然后将带有占位符?的sql模板发送至mysql服务器，由服务器对此无参数的sql进行编译后，将编译结果缓存，然后直接执行带有真实参数的sql。

预编译的作用：

1. 预编译阶段可以优化 sql 的执行。预编译之后的 sql 多数情况下可以直接执行，数据库服务器不需要再次编译，可以提升性能。

1. 预编译语句对象可以重复利用。把一个 sql 预编译后产生的 `PreparedStatement` 对象缓存下来，下次对于同一个sql，可以直接使用这个缓存的 PreparedState 对象。

1. 防止SQL注入。使用预编译，而其后注入的参数将不会再进行SQL编译。也就是说其后注入进来的参数系统将不会认为它会是一条SQL语句，而默认其是一个参数。

### [MyBatis 如何实现数据库类型和 Java 类型的转换的?](#mybatis-如何实现数据库类型和-java-类型的转换的)

MyBatis 类型转换主要依赖于 MyBatis 的 类型处理器(TypeHandler)机制。

TypeHandler 的核心作用：

- 将 Java 类型转换为 JDBC 类型，用于 SQL参数设置

- 将 JDBC 类型转换为 Java 类型，用于查询结果的映射。

具体操作流程如下：

1. MyBatis 在加载映射文件时，根据字段类型(如 jdbcType)和Java类型(如 resultType确定使用的 TypeHandler。

1. 在执行SQL时，ParameterHandler会使用TypeHandler 将Java 参数转换为JDBC 类型

1. 在解析结果集时，ResultsetHandler使用TypeHandler 将JDBC类型转换为 Java对象

### [说说 MyBatis 的缓存机制?](#说说-mybatis-的缓存机制)

缓存：合理使用缓存是优化中最常见的方法之一，将从数据库中查询出来的数据放入缓存中，下次使用时不必从数据库查询，而是直接从缓存中读取，避免频繁操作数据库，减轻数据库的压力，同时提高系统性能。

Mybatis里面设计了二级缓存来提升数据的检索效率，避免每次数据的访问都需要去查询数据库。

**一级缓存是SqlSession级别的缓存**：Mybatis对缓存提供支持，默认情况下只开启一级缓存，一级缓存作用范围为同一个SqlSession。在SQL和参数相同的情况下，我们使用同一个SqlSession对象调用同一个Mapper方法，往往只会执行一次SQL。因为在使用SqlSession第一次查询后，Mybatis会将结果放到缓存中，以后再次查询时，如果没有声明需要刷新，并且缓存没超时的情况下，SqlSession只会取出当前缓存的数据，不会再次发送SQL到数据库。若使用不同的SqlSession，因为不同的SqlSession是相互隔离的，不会使用一级缓存。

与springboot集成时一级缓存不生效问题：一级缓存是**会话级别**的，要生效的话，必须要在同一个 SqlSession 中。但是与 springboot 集成的 mybatis，默认每次执行sql语句时，都会创建一个新的 SqlSession！所以一级缓存才没有生效。
 解决：加上 `@Transactional` 注解。如果当前线程存在事务，并且存在相关会话，就从 ThreadLocal 中取出。如果没有事务，就重新创建一个 SqlSession 并存储到 ThreadLocal 当中，供下次查询使用。

**二级缓存是mapper级别的缓存**：可以使缓存在各个SqlSession之间共享。当多个用户在查询数据的时候，只要有任何一个SqlSession拿到了数据就会放入到二级缓存里面，其他的SqlSession就可以从二级缓存加载数据。

主要区别就在于作用范围：一级缓存只在一个会话内部有效，而二级缓存可以在不同会话之间共享数据。

二级缓存默认不开启，需要在mybatis-config.xml开启二级缓存：

并在相应的Mapper.xml文件添加cache标签，表示对哪个mapper 开启缓存：

二级缓存要求返回的POJO必须是可序列化的，即要求实现Serializable接口。

当开启二级缓存后，数据的查询执行的流程就是 二级缓存 -&gt; 一级缓存 -&gt; 数据库。

### [为什么不推荐使用 MyBatis 二级缓存？](#为什么不推荐使用-mybatis-二级缓存)

- 有复杂的数据模型或者数据之间的关联关系的会有数据不一致的影响

二级缓存是以 `namespace(mapper)` 为单位的，不同 namespace 下的操作互不影响。且 insert/update/delete 操作会清空所在 `namespace` 下的全部缓存。

那么问题就出来了，假设现在有 `ItemMapper` 以及 `XxxMapper`，在 `XxxMapper` 中做了表关联查询，且做了二级缓存。此时在 `ItemMapper` 中将 item 信息给删了，由于不同 namespace 下的操作互不影响，`XxxMapper` 的二级缓存不会变，那之后再次通过 `XxxMapper` 查询的数据就不对了，非常危险。

例如：

由于 `itemMapper` 与 `xxxMapper` 不是同一个命名空间，所以 `itemMapper` 执行的更新操作不会影响到 `xxxMapper` 的二级缓存；

再次调用 `xxxMapper.getPaymentVO`，发现取出的值是走缓存的，`itemName` 还是老的。但实际上 `itemName` 在上面已经被改了

### [Dao 接口的工作原理是什么？Dao 接口里的方法，参数不同时，方法能重载吗？](#dao-接口的工作原理是什么-dao-接口里的方法-参数不同时-方法能重载吗)

最佳实践中，通常一个 xml 映射文件，都会写一个 Dao 接口与之对应。Dao 接口就是人们常说的 `Mapper` 接口，接口的全限名，就是映射文件中的 namespace 的值，接口的方法名，就是映射文件中 `MappedStatement` 的 id 值，接口方法内的参数，就是传递给 sql 的参数。 `Mapper` 接口是没有实现类的，当调用接口方法时，接口全限名+方法名拼接字符串作为 key 值，可唯一定位一个 `MappedStatement`，举例：`com.mybatis3.mappers.StudentDao.findStudentById`，可以唯一找到 namespace 为 `com.mybatis3.mappers. StudentDao` 下面 `id = findStudentById` 的 `MappedStatement` 。在 MyBatis 中，每一个 `&lt;select&gt;`、 `&lt;insert&gt;`、 `&lt;update&gt;`、 `&lt;delete&gt;` 标签，都会被解析为一个 `MappedStatement` 对象。

Dao 接口里的方法可以重载，但是 Mybatis 的 xml 里面的 ID 不允许重复。并且需要满足以下条件：

1. 仅有一个无参方法和一个有参方法

1. 多个有参方法时，参数数量必须一致。且使用相同的 `@Param`，或者使用 `param1` 这种

Mybatis 版本 3.3.0：

然后在 `StuMapper.xml` 中利用 Mybatis 的动态 sql 就可以实现。

能正常运行，并能得到相应的结果，这样就实现了在 Dao 接口中写重载方法。

**Mybatis 的 Dao 接口可以有多个重载方法，但是多个接口对应的映射必须只有一个，否则启动会报错。**

Dao 接口的工作原理是 JDK 动态代理，MyBatis 运行时会使用 JDK 动态代理为 Dao 接口生成代理 proxy 对象，代理对象 proxy 会拦截接口方法，转而执行 `MappedStatement` 所代表的 sql，然后将 sql 执行结果返回。

### [MyBatis 写个 Xml 映射文件，再写个 DAO 接口就能执行，这个原理是什么?](#mybatis-写个-xml-映射文件-再写个-dao-接口就能执行-这个原理是什么)

核心原理是 JDBC 的能力 和 动态代理，通过解析 XML映射文件和动态生成 DAO 接口实现类来完成 SQL的执行。

以下是详细的执行原理:

1. 加载配置和 Mapper 映射文件:MyBatis 启动时，通过配置文件(mybatis-config.xml)加载数据库连接信息和 Mapper 映射文件(Mapper.xml )XML文件中的 SQL被解析为内部的 MappedStatement 对象，包含 SQL语句、参数映射规则和返回结果映射规则。

1. 动态代理实现 DAO 接口：MyBatis 为每个 DAO 接口生成一个动态代理类(Mapperproxy )，拦截接口方法调用。动态代理的核心是根据方法名和参数匹配到对应的 MappedStatement，然后调用JDBC 来执行 SQL。

1. 通过 JDBC 执行 SQL：MyBatis的 SqlSession 是对JDBC的封装，它的核心是使用PreparedStatement 来完成SQL的执行。根据 XML 中定义的 SQL和 DAO 接口方法传入的参数，生成完整的SQL查询，并将参数通过占位符(?)绑定到 PreparedStatement 。最终通过JDBC执行SQL，并获取Resultset。

1. 结果映射：JDBC的查询结果( Resultset )会被 MyBatis 的 Resultmap 或 resultType 映射为 DAO 接囗方法的返回值类型(如 POJO、Map或 List)。

### [MyBatis 动态 sql有什么用?执行原理?有哪些动态 sq!?](#mybatis-动态-sql有什么用-执行原理-有哪些动态-sq)

动态SQL是在 MyBatis中根据不同的条件、需求动态生成 so!语句的一种机制。它的主要目的是提高 sql 的灵活性和复用性，在复杂的查询或更新场景中，根据参数动态构建不同的 sqL语句，

动态 SQL的执行基于XML映射文件中定义的 SOL片段与标签，如 if、choose、when、otherwise、where、foreach 等，这些标签被解析，在运行时根据传入的参数值评估，最终形成完整的 SQL 语句发送到傲数据库

执行MyBatis 解析动态 SQL 的流程如下：

1. 解析动态 SQL：在映射文件加载时，MyBatis 会解析 XML文件中的动态 SQL 标签。

1. 参数绑定：当执行 SQL语句时，MyBatis 会根据传入的参数绑定具体的值。

1. 生成最终 SQL：根据参数值和动态 SQL 标签生成最终的 SQL语句。

1. 执行 SQL：MyBatis 执行生成的 SQL语句，并返回结果。

常见动态sql：

- if标签允许在 SQL 中根据条件包含不同的部分

- where 标签智能地插入 WHERE 关键字，并在必要时去除多余的 AND 或 OR。

- foreach 标签适用于需要遍历列表或数组，生成重复的 SQL 片段，如批量插入或 IN 条件查询。

- choose, when, otherwise 标签加一起相当于Java 中的 switch 语句，根据多个条件选择一个执行。

## [Mybatis使用](#mybatis使用)

### [使用 MyBatis 的 mapper 接口调用时有哪些要求?](#使用-mybatis-的-mapper-接口调用时有哪些要求)

- 接口方法名与 SQL 映射文件中的 id 要一致。

- 接口的全限定名要作为 xml 文件的命名空间。

- 参数和返回值要与映射文件的配置匹配，同时通过 @Param 注解可以处理多个参数的情况。

- 如果在 Spring 环境中需要进行 Mapper 扫描以注册为 Bean。

### [Mybatis都有哪些Executor执行器？它们之间的区别是什么？](#mybatis都有哪些executor执行器-它们之间的区别是什么)

Mybatis有三种基本的Executor执行器，`SimpleExecutor`、`ReuseExecutor`、`BatchExecutor`。

`SimpleExecutor`：每执行一次update或select，就开启一个Statement对象，用完立刻关闭Statement对象。

`ReuseExecutor`：执行update或select，以sql作为key查找Statement对象，存在就使用，不存在就创建，用完后，不关闭Statement对象，而是放置于Map&lt;String, Statement&gt;内，供下一次使用。简言之，就是重复使用Statement对象。

`BatchExecutor`：执行update（没有select，JDBC批处理不支持select），将所有sql都添加到批处理中（addBatch()），等待统一执行（executeBatch()），它缓存了多个Statement对象，每个Statement对象都是addBatch()完毕后，等待逐一执行executeBatch()批处理。与JDBC批处理相同。

作用范围：Executor的这些特点，都严格限制在SqlSession生命周期范围内。

### [MyBatis中接口绑定有几种实现方式?](#mybatis中接口绑定有几种实现方式)

1. 通过注解绑定，在接口的方法上面加上 @Select@Update等注解里面包含Sql语句来绑定（SQL语句比较简单的时候，推荐注解绑定）

1. 通过xml里面写SQL来绑定, 指定xml映射文件里面的namespace必须为接口的全路径名（SQL语句比较复杂的时候，推荐xml绑定）

### [xml 映射文件中，除了常见的 select、insert、update、delete 标签之外，还有哪些标签？](#xml-映射文件中-除了常见的-select、insert、update、delete-标签之外-还有哪些标签)

除了常见的select、insert、update和delete标签，MyBatis的XML映射文件中还有一些其他标签用于更复杂的操作和配置。以下是一些常见的额外标签：

1. resultMap： 用于定义查询结果与Java对象之间的映射关系，可以在多个查询中重复使用。

1. association和collection： 用于在resultMap中定义关联关系，用于处理一对一和一对多的关系。

1. discriminator： 在resultMap中使用，根据不同的条件选择不同的映射规则，用于处理继承关系的映射。

1. sql： 可以定义可重用的SQL片段，然后在其他地方引用。主要用于减少重复编写SQL语句。

1. include： 用于在SQL语句中引入外部定义的SQL片段，提高可维护性。

1. if、choose、when、otherwise： 用于在SQL语句中进行条件判断和逻辑控制，用于动态SQL的构建。

1. trim、where、set： 用于在SQL语句中添加固定的SQL片段，如where和set关键字，用于动态的条件构建。

1. foreach： 用于在SQL语句中进行集合迭代，适用于生成IN语句等。

1. bind： 用于在SQL语句中声明并绑定一个变量，可以在查询中重复使用。

1. cache： 用于配置二级缓存。

1. selectKey： 用于在插入操作后获取生成的主键值。

1. insert、update、delete的flushCache、useGeneratedKeys、keyProperty属性： 用于配置插入、更新和删除操作的一些属性。

### [MyBatis 的 xml 映射文件中，不同的 xml 映射文件，id 是否可以重复？](#mybatis-的-xml-映射文件中-不同的-xml-映射文件-id-是否可以重复)

不同的 xml 映射文件，如果配置了 namespace，那么 id 可以重复；如果没有配置 namespace，那么 id 不能重复；毕竟 namespace 不是必须的，只是最佳实践而已。

原因就是 namespace+id 是作为 `Map&lt;String, MappedStatement&gt;` 的 key 使用的，如果没有 namespace，就剩下 id，那么，id 重复会导致数据互相覆盖。有了 namespace，自然 id 就可以重复，namespace 不同，namespace+id 自然也就不同。

### [MyBatis 是如何将 sql 执行结果封装为目标对象并返回的？都有哪些映射形式？](#mybatis-是如何将-sql-执行结果封装为目标对象并返回的-都有哪些映射形式)

第一种是使用 `&lt;resultMap&gt;` 标签，逐一定义列名和对象属性名之间的映射关系。第二种是使用 sql 列的别名功能，将列别名书写为对象属性名，比如 T_NAME AS NAME，对象属性名一般是 name，小写，但是列名不区分大小写，MyBatis 会忽略列名大小写，智能找到与之对应对象属性名，你甚至可以写成 T_NAME AS NaMe，MyBatis 一样可以正常工作。

有了列名与属性名的映射关系后，MyBatis 通过反射创建对象，同时使用反射给对象的属性逐一赋值并返回，那些找不到映射关系的属性，是无法完成赋值的。

### [MyBatis 是否可以映射 Enum 枚举类？](#mybatis-是否可以映射-enum-枚举类)

MyBatis 可以映射枚举类，不单可以映射枚举类，MyBatis 可以映射任何对象到表的一列上。映射方式为自定义一个 `TypeHandler`，实现 `TypeHandler` 的 `setParameter()` 和 `getResult()` 接口方法。 `TypeHandler` 有两个作用：

- 一是完成从 javaType 至 jdbcType 的转换；

- 二是完成 jdbcType 至 javaType 的转换，体现为 `setParameter()` 和 `getResult()` 两个方法，分别代表设置 sql 问号占位符参数和获取列查询结果。

### [MyBatis 映射文件中，如果 A 标签通过 include 引用了 B 标签的内容，请问，B 标签能否定义在 A 标签的后面，还是说必须定义在 A 标签的前面？](#mybatis-映射文件中-如果-a-标签通过-include-引用了-b-标签的内容-请问-b-标签能否定义在-a-标签的后面-还是说必须定义在-a-标签的前面)

虽然 MyBatis 解析 xml 映射文件是按照顺序解析的，但是，被引用的 B 标签依然可以定义在任何地方，MyBatis 都可以正确识别。

原理是，MyBatis 解析 A 标签，发现 A 标签引用了 B 标签，但是 B 标签尚未解析到，尚不存在，此时，MyBatis 会将 A 标签标记为未解析状态，然后继续解析余下的标签，包含 B 标签，待所有标签解析完毕，MyBatis 会重新解析那些被标记为未解析的标签，此时再解析 A 标签时，B 标签已经存在，A 标签也就可以正常解析完成了。

### [模糊查询 like 语句该怎么写?](#模糊查询-like-语句该怎么写)

在MyBatis中，要执行模糊查询（使用LIKE语句），可以使用SQL语句的字符串拼接或使用动态SQL来构建查询语句。

假设你要在一个查询中执行模糊查询，搜索用户的用户名包含特定关键字的情况。

字符串拼接方式：

在这个例子中，#{keyword}是参数占位符，表示要搜索的关键字。CONCAT('%', #{keyword}, '%')用于构建模糊匹配的字符串。

动态SQL方式：

在这个例子中，使用了`&lt;if&gt;`标签来创建动态条件。只有在keyword参数不为null时，才会添加AND username LIKE CONCAT('%', #{keyword}, '%')这个条件到查询语句中。

### [MyBatis 自带的连接池有了解过吗?](#mybatis-自带的连接池有了解过吗)

MyBatis 自带的连接池是 PooledDataSource 类实现的，是一个简单的连接池实现，提供了连接复用和基本的资源管理功能

执行原理：

1. 初始化连接池：PooledDataSource 会初始化一定数量的连接，放入空闲连接队列。

1. 获取连接：调用 getconnection()方法时，优先从空闲队列中获取连接，如果空闲队列为空，且活跃连接未达上限，则创建新连接。

1. 回收连接：使用完毕后，通过 pushConnection()方法将连接放回空闲队列。

1. 失效检测：通过 poolPingQuery 定期检查空闲连接的可用性；失效的连接会被丢弃。

关键配置：

- poolMaximumActiveConnections：最大活跃连接数

- poolMaximumIdleConnections：最大空闲连接数。

- poolMaximumCheckouTime：单个连接的最大占用时间，超过时间会被强制回收

- poolPingQuery：检测连接可用性的 SQL。

### [Mybatis 如何实现一对一、一对多的关联查询 ?](#mybatis-如何实现一对一、一对多的关联查询)

在 MyBatis 中，实现一对一和一对多的关联査询主要是通过 resultMap 来完成的。MyBatis 提供了两种方式来处理关联关系

- 嵌套结果映射(Nested Result Mapping)

  - 适用于一次 SQL 查询中同时返回主表和关联表的数据。

  - 使用`&lt;association&gt;`标签表示一对一的关系。

  - 使用`&lt;collection&gt;`标签表示一对多的关系。

- 嵌套查询(Nested Select)

  - 主查询只查主表数据，关联表数据通过单独的 SQL查询获取。

  - 使用`&lt;association&gt;`或`&lt;collection&gt;`的select 属性指定子查询

### [MyBatis如何实现动态数据源切换？](#mybatis如何实现动态数据源切换)

在实现动态数据源切换方面，MyBatis有几种方法，让你能够在不同的数据库之间轻松切换。比如，你可能会在开发环境和生产环境中使用不同的数据库。下面是一些可以考虑的方法：

1. 我们可以通过配置文件来实现切换。可以在MyBatis的配置文件里配置多个数据源，然后根据需要在代码中进行切换。这就涉及到定义多个数据源的连接信息和配置，然后在代码里通过指定数据源的标识来选择要使用哪个数据源。这种方法需要在配置文件中进行一些准备工作，但切换过程相对比较容易。

1. 可以运用AOP切面编程来实现切换。通过使用面向切面编程（AOP），可以在方法调用之前进行拦截，然后根据条件来动态地切换数据源。可以创建一个切面，将切入点设定为需要切换数据源的方法，然后在切面中实现数据源切换的逻辑。这样的做法能够将切换逻辑和业务逻辑分隔开，有助于提高代码的可维护性。

1. 可以使用MyBatis提供的AbstractRoutingDataSource类。这个类允许你创建一个数据源路由器，根据特定的规则来选择数据源。你可以继承这个类，然后实现其中的determineCurrentLookupKey()方法，以返回当前应该使用的数据源标识。这种方式非常灵活，可以根据不同的条件来切换数据源。

1. 使用第三方库。例如Druid和HikariCP等。这些库通常提供了更多的功能和配置选项，可以根据实际需求来选择合适的库。

### [MyBatis 和 MyBatis Plus 有哪些区别？](#mybatis-和-mybatis-plus-有哪些区别)

1. MyBatis Plus 是 MyBatis 的增强工具，提供了许多开箱即用的功能和简化的操作接口。对于单数据表的常见操作（CRUD）提供了自动化的方法，减少了 SQL 代码的编写，但对于复杂查询仍需手动编写。

1. MyBatis 不提供内置的分页功能，通常需要使用第三方分页插件（如 PageHelper）或手动编写 SQL。MyBatis Plus 内置了分页功能，使用非常简单。

就可以看成 MyBatis 能实现的 MyBatis Plus都实现了，是增强版工具
