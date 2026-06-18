{

  "title": "JAVA MyBatis配置文件用properties引入外部配置文件",
  "date": "2019-10-11",
  "description": "方式一：通过properties 元素的子元素来传递数据 例如： 然后其中的属性就可以在整个配置文件中被用来替换需要动态配置的属性值。比如: 这个例子中的 driver、url、username、password 将会由 properties 元素中的子元素设置的相应值来替换。 注：dataSour",
  "tags": [
    "Java",
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11655095.html"

}

## 方式一：通过properties 元素的子元素来传递数据

例如：

```text
1     <properties>
2         <property name="driver" value="com.mysql.jdbc.Driver" /> <!-- 驱动类型 -->
3         <property name="url" value="jdbc:mysql://localhost:3306/sam" /> <!-- 连接字符串 -->
4         <property name="username" value="root" /> <!-- 用户名 -->
5         <property name="password" value="root" /> <!-- 密码 -->
6     </properties>
```

然后其中的属性就可以在整个配置文件中被用来替换需要动态配置的属性值。比如:

```text
1             <dataSource type="POOLED">
2                 <property name="driver" value="${driver}" /> <!-- 驱动类型 -->
3                 <property name="url" value="${url}" /> <!-- 连接字符串 -->
4                 <property name="username" value="${username}" /> <!-- 用户名 -->
5                 <property name="password" value="${password}" /> <!-- 密码 -->
6             </dataSource>
```

这个例子中的 driver、url、username、password 将会由 properties 元素中的子元素设置的相应值来替换。

**注：dataSource元素下的property的属性value值，需与properties元素下的property的属性name一一对应。**

完整配置文件：myBatis-config.xml

```text
 1 <?xml version="1.0" encoding="UTF-8"?>
 2 <!DOCTYPE configuration
 3   PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
 4   "http://mybatis.org/dtd/mybatis-3-config.dtd">
 5 <configuration>
 6     <properties>
 7         <property name="driver" value="com.mysql.jdbc.Driver" /> <!-- 驱动类型 -->
 8         <property name="url" value="jdbc:mysql://localhost:3306/sam" /> <!-- 连接字符串 -->
 9         <property name="username" value="root" /> <!-- 用户名 -->
10         <property name="password" value="root" /> <!-- 密码 -->
11     </properties>
12     <environments default="development">
13         <environment id="development">
14             <transactionManager type="JDBC" />
15             <dataSource type="POOLED">
16                 <property name="driver" value="${driver}" /> <!-- 驱动类型 -->
17                 <property name="url" value="${url}" /> <!-- 连接字符串 -->
18                 <property name="username" value="${username}" /> <!-- 用户名 -->
19                 <property name="password" value="${password}" /> <!-- 密码 -->
20             </dataSource>
21         </environment>
22     </environments>
23     <mappers>
24         <mapper resource="DeptMapper.xml" /> <!-- 映射SQL语句的XML文件 -->
25     </mappers>
26 </configuration>
```

## 方式二、通过properties的resource属性来引入外部properties配置文件的内容

完整配置文件：myBatis-config.xml

```text
 1 <?xml version="1.0" encoding="UTF-8"?>
 2 <!DOCTYPE configuration
 3   PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
 4   "http://mybatis.org/dtd/mybatis-3-config.dtd">
 5 <configuration>
 6     <!-- 引入外部配置文件 -->
 7     <properties resource="dbconfig.properties">
 8     </properties>
 9     <environments default="development">
10         <environment id="development">
11             <transactionManager type="JDBC" />
12             <dataSource type="POOLED">
13                 <property name="driver" value="${driver}" /> <!-- 驱动类型 -->
14                 <property name="url" value="${url}" /> <!-- 连接字符串 -->
15                 <property name="username" value="${username}" /> <!-- 用户名 -->
16                 <property name="password" value="${password}" /> <!-- 密码 -->
17             </dataSource>
18         </environment>
19     </environments>
20     <mappers>
21         <mapper resource="DeptMapper.xml" /> <!-- 映射SQL语句的XML文件 -->
22     </mappers>
23 </configuration>
```

完整配置文件：dbconfig.properties

```text
1 driver=com.mysql.jdbc.Driver
2 url=jdbc:mysql://localhost:3306/sam
3 username=root
4 password=root
```

注：dbconfig.properties此文件换行时，不能有空格！！！
