{

  "title": "The reference to entity \"characterEncoding\" must end with the ';'",
  "date": "2019-11-12",
  "description": "在配置数据库连接池数据源时，本来没有错误，结果加上编码转换格式后eclipse突然报错： 这是怎么回事？ 经过查询，发现这个错误其实很好解决。 首先，原因是： **.xml文件中 ‘ & ’字符需要进行转义！！！** 看到这里，其实已经恍然大悟，那么，这个字符 ‘ & ’ 需要怎么转义呢？看下面这张",
  "tags": [
    "JAVA",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11839321.html"

}

在配置数据库连接池数据源时，本来没有错误，结果加上编码转换格式后eclipse突然报错：

这是怎么回事？

经过查询，发现这个错误其实很好解决。

首先，原因是： **.xml文件中 ‘ & ’字符需要进行转义！！！**

看到这里，其实已经恍然大悟，那么，这个字符 ‘ & ’ 需要怎么转义呢？看下面这张表：

在xml文件中有以下几类字符要进行转义替换：

![](/imported/posts/2019-11-12-11839321-ad16203e-the-reference-to-entity-characterencoding-must-end-with-the/images/img_001_416f3ea10c6b.png)

**所以，我们在xml文件中不能直接写 ‘ & ’ 字符，而需要写成 ‘ & ’**

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:aop="http://www.springframework.org/schema/aop"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
        http://www.springframework.org/schema/aop
        http://www.springframework.org/schema/aop/spring-aop.xsd">
    <!-- 管理DataSource -->
    <bean id="dataSource"
        class="org.springframework.jdbc.datasource.DriverManagerDataSource">
        <!-- set方法注入属性，和类中的成员属性无关，和set方法名称有关，比如有一个属性叫username，但是set方法：setName -->
        <property name="driverClassName" value="com.mysql.cj.jdbc.Driver"></property>
        <!-- 转义前 -->
        <property name="url" value="jdbc:mysql://localhost:3306/demo?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai"></property>
        <!-- 转义后 -->
        <property name="url" value="jdbc:mysql://localhost:3306/demo?useUnicode=true&amp;characterEncoding=UTF-8&amp;serverTimezone=Asia/Shanghai"></property>
        <property name="username" value="root"></property>
        <property name="password" value="root"></property>
    </bean>
    <!-- 管理jdbcTemplate -->
    <bean id="template"
        class="org.springframework.jdbc.core.JdbcTemplate">
        <constructor-arg name="dataSource" ref="dataSource"></constructor-arg>
    </bean>
</beans>
```
