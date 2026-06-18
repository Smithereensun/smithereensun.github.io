{

  "title": "java 线程池、多线程并发实战(生产者消费者模型 1 vs 10) 附案例源码",
  "date": "2020-10-07",
  "description": "导读 前二天写了一篇《Java 多线程并发编程》点我直达，放国庆，在家闲着没事，继续写剩下的东西，开干！ 线程池 为什么要使用线程池 例如web服务器、数据库服务器、文件服务器或邮件服务器之类的。请求的时候，单个任务时间很短，但是请求数量巨大。每一次请求，就会创建一个新线程，然后在新线程中请求服务，",
  "tags": [
    "Java"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13756921.html"

}

# 导读

　　前二天写了一篇《Java 多线程并发编程》[点我直达](https://www.cnblogs.com/chenyanbin/p/13629067.html)，放国庆，在家闲着没事，继续写剩下的东西，开干！

# 线程池

## 为什么要使用线程池

　　例如web服务器、数据库服务器、文件服务器或邮件服务器之类的。请求的时候，单个任务时间很短，但是请求数量巨大。每一次请求，就会创建一个新线程，然后在新线程中请求服务，频繁的创建线程，销毁线程造成系统很大的开销，资源的浪费。

　　线程池为线程生命周期开销问题和资源不足问题提供了解决方案。通过对多个任务重用线程，线程车创建的开销分摊到多个任务上。

## 创建与使用

![](./images/images/img_001_3be12d325070.gif)

### Future

　　对具体的Runnable或者Callable任务的执行结果进行取消、查询是否完成、获取结果、设置结果。get方法会阻塞，直到任务返回结果。

![](./images/images/img_002_67f2d315f3cd.gif)

### Callable&FutureTask

　　Callable与Runnable功能相似，Callable有返回值；Runnable没有返回值；一般情况下，Callable与FutureTask一起使用，或者与线程池一起使用

![](./images/images/img_003_bc462e9e9f32.gif)

## 线程池核心组成部分

- corePoolSize：核心线程池大小
- maximumPoolSize：线程池最大容量
- KeepAliveTime：当线程数量大于核心时，多余的空闲线程在终止之前等待新任务的最大时间
- unit：时间单位
- workQueue：工作队列
- ThreadFactory：线程工厂
- handler：拒绝策略

　　ThreadPoolExcutor有6个参数，第一个是核心线程数，如果线程池无事可做，还是会保留这些线程。第二个是最大线程数，超过核心线程数的部分都会在第三个和第四个参数合起来决定的最长空闲存活时间超过后被剔除。第五个参数时阻塞队列，线程忙不过来要去这里面排队。最后一个是线程池工厂，主要决定队列也装不下的线程怎么处理，默认策略时抛出异常。

线程拒绝策略如下

1. CallerRunsPolicy：交由调用方线程运行，比如 main 线程；如果添加到线程池失败，那么主线程会自己去执行该任务，不会等待线程池中的线程去执行。
2. AbortPolicy：该策略是线程池的默认策略，如果线程池队列满了丢掉这个任务并且抛出RejectedExecutionException异常。
3. DiscardOldestPolicy：丢弃队列中最老的任务，队列满了，会将最早进入队列的任务删掉腾出空间，再尝试加入队列。
4. DiscardPolicy：如果线程池队列满了，会直接丢掉这个任务并且不会有任何异常。
5. 自定义拒绝策略，实现RejectedExecutionHandler接口

## Executor框架

![](./images/images/img_004_a39ed50d2440.gif)

# 实战

## 需求分析

### 业务场景

　　一般系统，多数会与第三方系统的数据进行打交道，而第三方的生产库，并不允许我们直接操作。在企业里面，一般都是通过中间表进行同步，即第三方系统将生产数据放入一张与其生产环境隔离的另一个独立数据库中的独立表，在根据接口协议，增加相应的字段。而我方需要读取该中间表中的数据，并对数据进行同步操作。此时就需要编写相应的程序进行数据同步。

### 同步方式

1. 全量同步：每天定时将当天的生产数据全部同步过来(优点：实现检点；缺点：数据同步不及时)
2. 增量同步：每新增一条，便将该数据同步过来(优点：数据接近实时同步；缺点：实现相对困难)

### 我方需要做的事情

　　读取中间表的数据，并同步到业务系统中

### 模型抽离(生产者消费者模型)

1. 生产者：读取中间表的数据
2. 消费者：消费生产者生产的数据

### 接口协议的制定

1. 取我方业务上需要用到的字段
2. 需要有字段记录数据什么时候进入中间表
3. 增加相应的数据标志位，用于标志数据的同步状态
4. 记录数据的同步时间

### 技术选型

1. mybatis
2. 单一生产者多消费者
3. 多线程并发操作

## 中间表设计

![](./images/images/img_005_21b68d92d13a.gif)

## 项目搭建

![](./images/images/img_006_b841e04d204d.gif)

### 项目结构

![](./images/images/img_007_9fe5585ae149.png)

### pom.xml

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.cyb</groupId>
    <artifactId>ybchen_syn</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <!-- 添加MyBatis框架 -->
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.6</version> <!-- 版本号视情况修改 -->
        </dependency>
        <!-- 添加MySql驱动包 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.21</version>
        </dependency>
        <!--连接池-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.2.1</version>
        </dependency>
        <!--日志-->
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>1.7.30</version>
        </dependency>
        <!--单元测试-->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

</project>
```

pom.xml

### log4j.properties

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
### 设置###
log4j.rootLogger = debug,stdout,D,E

### 输出信息到控制抬 ###
log4j.appender.stdout = org.apache.log4j.ConsoleAppender
log4j.appender.stdout.Target = System.out
log4j.appender.stdout.layout = org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern = [%-5p] %d{yyyy-MM-dd HH:mm:ss,SSS} method:%l%n%m%n

### 输出DEBUG 级别以上的日志到=E://logs/error.log ###
log4j.appender.D = org.apache.log4j.DailyRollingFileAppender
log4j.appender.D.File = ./logs/debug.log
log4j.appender.D.Append = true
log4j.appender.D.Threshold = DEBUG
log4j.appender.D.layout = org.apache.log4j.PatternLayout
log4j.appender.D.layout.ConversionPattern = %-d{yyyy-MM-dd HH:mm:ss}  [ %t:%r ] - [ %p ]  %m%n

### 输出ERROR 级别以上的日志到=E://logs/error.log ###
log4j.appender.E = org.apache.log4j.DailyRollingFileAppender
log4j.appender.E.File =./logs/error.log
log4j.appender.E.Append = true
log4j.appender.E.Threshold = ERROR
log4j.appender.E.layout = org.apache.log4j.PatternLayout
log4j.appender.E.layout.ConversionPattern = %-d{yyyy-MM-dd HH:mm:ss}  [ %t:%r ] - [ %p ]  %m%n
```

log4j.properties

### middle-student.xml

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="middle-student">
    <resultMap id="BaseResultMap" type="com.cyb.entity.middle.Student">
        <id column="id" property="id" jdbcType="INTEGER"/>
        <result column="name" property="name" jdbcType="VARCHAR"/>
        <result column="sex" property="sex" jdbcType="VARCHAR"/>
        <result column="birth" property="birth" jdbcType="TIMESTAMP"/>
        <result column="department" property="department" jdbcType="VARCHAR"/>
        <result column="add_time" property="addTime" jdbcType="TIMESTAMP"/>
        <result column="data_status" property="dataStatus" jdbcType="VARCHAR"/>
        <result column="deal_time" property="dealTime" jdbcType="TIMESTAMP"/>
    </resultMap>
    <select id="selectList" resultMap="BaseResultMap">
        SELECT
        *
        FROM student
        WHERE data_status = 'I'  limit #{count}
    </select>
    <update id="updateStatusById">
        update  student
        set data_status = #{dataStatus}, deal_time = #{dealTime}
        where id =#{id}
    </update>
</mapper>
```

middle-student.xml

### test-student.xml

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="test-student">
    <insert id="addStudent">
        insert into student (name,sex,department) values (#{name},#{sex},#{department})
    </insert>
</mapper>
```

test-student.xml

### mybatis-config-middle.xml

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">

<!-- MyBatis的全局配置文件 -->
<configuration >
    <!-- 1.配置开发环境 -->
    <environments default="develop">
        <!-- 这里可以配置多个环境，比如develop，test等 -->
        <environment id="develop">
            <!-- 1.1.配置事务管理方式：JDBC：将事务交给JDBC管理（推荐） -->
            <transactionManager type="JDBC"></transactionManager>
            <!-- 1.2.配置数据源，即连接池方式:JNDI/POOLED/UNPOOLED -->
            <dataSource type="com.cyb.datasource.DruidDataSourceFactory">
                <property name="driverClass" value="com.mysql.cj.jdbc.Driver"/>
                <property name="jdbcUrl" value="jdbc:mysql://localhost:3306/middle?characterEncoding=UTF-8&amp;serverTimezone=Asia/Shanghai&amp;autoReconnect=true"/>
                <property name="username" value="root"/>
                <property name="password" value="root"/>
                <property name="initialSize" value="2"/>
                <property name="maxActive" value="300"/>
                <property name="maxWait" value="60000"/>
                <property name="poolPreparedStatements" value="true"/>
                <property name="maxPoolPreparedStatementPerConnectionSize" value="200"/>
            </dataSource>
        </environment>
    </environments>

    <!-- 2.加载Mapper配置文件,路径以斜杠间隔: xx/xx/../xx.xml -->
    <mappers>
        <mapper resource="middle-student.xml"/>
    </mappers>
</configuration>
```

mybatis-config-middle.xml

### mybatis-config-test.xml

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">

<!-- MyBatis的全局配置文件 -->
<configuration >
    <!-- 1.配置开发环境 -->
    <environments default="develop">
        <!-- 这里可以配置多个环境，比如develop，test等 -->
        <environment id="develop">
            <!-- 1.1.配置事务管理方式：JDBC：将事务交给JDBC管理（推荐） -->
            <transactionManager type="JDBC"></transactionManager>
            <!-- 1.2.配置数据源，即连接池方式:JNDI/POOLED/UNPOOLED -->
            <dataSource type="com.cyb.datasource.DruidDataSourceFactory">
                <property name="driverClass" value="com.mysql.cj.jdbc.Driver"/>
                <property name="jdbcUrl" value="jdbc:mysql://localhost:3306/test?characterEncoding=UTF-8&amp;serverTimezone=Asia/Shanghai&amp;autoReconnect=true"/>
                <property name="username" value="root"/>
                <property name="password" value="root"/>
                <property name="initialSize" value="2"/>
                <property name="maxActive" value="300"/>
                <property name="maxWait" value="60000"/>
                <property name="poolPreparedStatements" value="true"/>
                <property name="maxPoolPreparedStatementPerConnectionSize" value="200"/>
            </dataSource>
        </environment>
    </environments>

    <!-- 2.加载Mapper配置文件,路径以斜杠间隔: xx/xx/../xx.xml -->
    <mappers>
        <mapper resource="test-student.xml"/>
    </mappers>
</configuration>
```

mybatis-config-test.xml

### StudentConst.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.cost;

public class StudentConst {
    //I:第三方系统入库；D:处理中；F:处理完成；E:发生错误或异常
    public static final String INIT="I";
    public static final String DEALING="D";
    public static final String FINISH="F";
    public static final String ERROR="E";
}
```

StudentConst.java

### DruidDataSourceFactory.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.datasource;

import com.alibaba.druid.pool.DruidDataSource;
import org.apache.ibatis.datasource.unpooled.UnpooledDataSourceFactory;

/**
 * @ClassName：DruidDataSourceFactory
 * @Description：Druid连接池工厂类
 * @Author：chenyb
 * @Date：2020/10/7 7:30 下午
 * @Versiion：1.0
 */
public class DruidDataSourceFactory extends UnpooledDataSourceFactory {
    public DruidDataSourceFactory() {
        this.dataSource = new DruidDataSource();
    }
}
```

DruidDataSourceFactory.java

### Student.java(middle包下)

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.entity.middle;

import java.io.Serializable;
import java.util.Date;

public class Student implements Serializable {
    private Integer id;
    private String name;
    private String sex;
    private String address;
    private String department;
    private Date addTime;
    private String dataStatus;
    private Date dealTime;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    public Date getAddTime() {
        return addTime;
    }

    public void setAddTime(Date addTime) {
        this.addTime = addTime;
    }

    public String getDataStatus() {
        return dataStatus;
    }

    public void setDataStatus(String dataStatus) {
        this.dataStatus = dataStatus;
    }

    public Date getDealTime() {
        return dealTime;
    }

    public void setDealTime(Date dealTime) {
        this.dealTime = dealTime;
    }

    @Override
    public String toString() {
        return "Student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", sex='" + sex + '\'' +
                ", address='" + address + '\'' +
                ", department='" + department + '\'' +
                ", addTime=" + addTime +
                ", dataStatus='" + dataStatus + '\'' +
                ", dealTime=" + dealTime +
                '}';
    }
}
```

student.java

### Student.java(test包下)

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.entity.test;

import java.io.Serializable;

public class Student implements Serializable {
    private Integer id;
    private String name;
    private String sex;
    private String department;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    @Override
    public String toString() {
        return "student{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", sex='" + sex + '\'' +
                ", department='" + department + '\'' +
                '}';
    }
}
```

Student.java

### MiddleProcess.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.process;

import com.cyb.entity.middle.Student;

import java.util.List;

public interface MiddleProcess {
    /**
     * 查询数据
     * @param count 一次查询的数量
     * @return
     */
    List<Student> queryList(int count);

    /**
     * 修改数据状态
     * @param data 待修改数据
     * @param status 要修改成的状态
     * @return
     */
    int modifyListStatus(List<Student> data, String status);
}
```

MiddleProcess.java

### TestProcess.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.process;

import com.cyb.entity.middle.Student;

import java.util.List;

public interface TestProcess {
    /**
     * 处理数据
     * @param data
     */
    void hand(List<Student> data);
}
```

TestProcess.java

### MiddleProcessImpl.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.process.impl;

import com.cyb.entity.middle.Student;
import com.cyb.process.MiddleProcess;
import com.cyb.util.SqlSessionUtil;
import org.apache.ibatis.session.SqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Date;
import java.util.List;

public class MiddleProcessImpl implements MiddleProcess {
private static final Logger LOGGER= LoggerFactory.getLogger(MiddleProcess.class);
    @Override
    public List<Student> queryList(int count) {
        SqlSession middleSqlSession = SqlSessionUtil.getSqlSession("middle");
        List<Student> objects =null;
        try {
            objects = middleSqlSession.selectList("middle-student.selectList", count);
        }catch (Exception e){
            LOGGER.error("查询发生异常=======》",e);
        }
        finally {
            //关闭连接
            middleSqlSession.close();
        }
        return objects;
    }

    @Override
    public int modifyListStatus(List<Student> data, String status) {
        data.forEach(stu->{
            stu.setDataStatus(status);
            SqlSession middleSqlSession = SqlSessionUtil.getSqlSession("middle");
            try {
                middleSqlSession.update("middle-student.updateStatusById",stu);
                middleSqlSession.commit();
            }catch (Exception e){
                //回滚当前提交
                middleSqlSession.rollback();
                LOGGER.error("修改状态失败=======》",e);
            }finally {
                middleSqlSession.close();
            }
        });
        return 0;
    }
}
```

MiddleProcessImpl.java

### TestProcessImpl.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.process.impl;

import com.cyb.cost.StudentConst;
import com.cyb.entity.middle.Student;
import com.cyb.process.TestProcess;
import com.cyb.util.SqlSessionUtil;
import org.apache.ibatis.session.SqlSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class TestProcessImpl implements TestProcess {
    private Logger LOGGER = LoggerFactory.getLogger(TestProcess.class);

    @Override
    public void hand(List<Student> data) {
        //将data转换成业务库的实体
        List<com.cyb.entity.test.Student> students = adapter(data);
        //处理数据，并入库
        students.forEach(stu -> {
            stu.setName(stu.getName() + "_test");
            SqlSession testSqlSession = SqlSessionUtil.getSqlSession("test");
            try {
                testSqlSession.insert("test-student.addStudent", stu);
                testSqlSession.commit();
                //修改中间表状态
                modifyMiddle(stu.getId(), StudentConst.FINISH);
            } catch (Exception e) {
                //回滚操作
                testSqlSession.rollback();
                LOGGER.error("处理数据发生异常============》",e);
            } finally {
                testSqlSession.close();
            }
        });
    }

    /**
     * 数据适配器
     *
     * @param data
     * @return
     */
    public List<com.cyb.entity.test.Student> adapter(List<Student> data) {
        List<com.cyb.entity.test.Student> result = new ArrayList<>();
        data.forEach(stu -> {
            com.cyb.entity.test.Student student = new com.cyb.entity.test.Student();
            student.setId(stu.getId());
            student.setName(stu.getName());
            student.setDepartment(stu.getDepartment());
            student.setSex(stu.getSex());
            result.add(student);
        });
        return result;
    }

    /**
     * 修改中间表状态
     * @param id
     * @param status
     */
    private void modifyMiddle(int id, String status) {
        Student student = new Student();
        student.setId(id);
        student.setDataStatus(status);
        student.setDealTime(new Date());
        SqlSession middleSqlSession = SqlSessionUtil.getSqlSession("middle");
        try {
            middleSqlSession.update("middle-student.updateStatusById", student);
            middleSqlSession.commit();
        } catch (Exception e) {
            middleSqlSession.rollback();
            LOGGER.error("修改中间表状态失败===========》",e);
        } finally {
            middleSqlSession.close();
        }
    }
}
```

TestProcessImpl.java

### Consumer.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.start;

import com.cyb.entity.middle.Student;
import com.cyb.process.TestProcess;

import java.util.List;
import java.util.concurrent.LinkedBlockingDeque;

/**
 * @ClassName：Consumer
 * @Description：消费者
 * @Author：chenyb
 * @Date：2020/10/7 9:23 下午
 * @Versiion：1.0
 */
public class Consumer implements Runnable{
    private List<Student> data;
    private TestProcess testProcess;
    private LinkedBlockingDeque<Runnable> consumer;

    public Consumer(TestProcess testProcess, LinkedBlockingDeque<Runnable> consumer) {
        this.testProcess = testProcess;
        this.consumer = consumer;
    }

    @Override
    public void run() {
        try {
            testProcess.hand(data);
        }finally {
            try {
                //添加元素,队列满，进入阻塞状态
                consumer.put(this);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    public void setData(List<Student> data){
        this.data=data;
    }
}
```

Consumer.java

### Producer.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.start;

import com.cyb.cost.StudentConst;
import com.cyb.entity.middle.Student;
import com.cyb.process.MiddleProcess;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.Collections;
import java.util.List;
import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.ThreadPoolExecutor;

/**
 * @ClassName：Producer
 * @Description：提供者
 * @Author：chenyb
 * @Date：2020/10/7 9:22 下午
 * @Versiion：1.0
 */
public class Producer implements Runnable {
    private static final Logger LOGGER = LoggerFactory.getLogger(Producer.class);
    private MiddleProcess middleProcess;
    private LinkedBlockingDeque<Runnable> consumer;
    private ThreadPoolExecutor executor;

    public Producer(MiddleProcess middleProcess, LinkedBlockingDeque<Runnable> consumer, ThreadPoolExecutor executor) {
        this.middleProcess = middleProcess;
        this.consumer = consumer;
        this.executor = executor;
    }

    @Override
    public void run() {
        while (true) {
            //每次生产10条数据
            List<Student> students = middleProcess.queryList(10);
            try {
                if (students != null && students.size() > 0) {
                    //将数据修改为处理中
                    middleProcess.modifyListStatus(students, StudentConst.DEALING);
                    Consumer con = (Consumer) consumer.take();
                    con.setData(students);
                    executor.execute(con);
                } else {
                    //如果没有数据，睡眠5秒
                    try {
                        Thread.sleep(5000L);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }catch (Exception e){
             LOGGER.error("生产者发生异常========>",e);
            }
        }
    }
}
```

Producer.java

### Main.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.start;

import com.cyb.process.MiddleProcess;
import com.cyb.process.TestProcess;
import com.cyb.process.impl.MiddleProcessImpl;
import com.cyb.process.impl.TestProcessImpl;

import java.util.concurrent.LinkedBlockingDeque;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

/**
 * 生产着消费者：1 VS 10
 */
public class Main {
    public static void main(String[] args) {
        TestProcess testProcess=new TestProcessImpl();
        MiddleProcess middleProcess=new MiddleProcessImpl();
        LinkedBlockingDeque<Runnable> runnables=new LinkedBlockingDeque<>(10);
        ThreadPoolExecutor threadPoolExecutor=new ThreadPoolExecutor(10,20,5L, TimeUnit.SECONDS, new LinkedBlockingQueue<>(20));
        //10个消费者
        for (int i = 0; i < 10; i++) {
            try {
                runnables.put(new Consumer(testProcess,runnables));
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        //开启一个线程-》生产者
        Producer producer=new Producer(middleProcess,runnables,threadPoolExecutor);
        new Thread(producer).start();
    }
}
```

Main.java

### SqlSessionUtil.java

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
package com.cyb.util;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.apache.ibatis.session.SqlSession;
import java.io.IOException;
import java.io.Reader;

/**
 * @ClassName：SqlSessionUtil
 * @Description：SqlSession工具类
 * @Author：chenyb
 * @Date：2020/10/7 7:37 下午
 * @Versiion：1.0
 */
public class SqlSessionUtil {
    private static final String MYBATIS_CONFIG_MIDDLE = "mybatis-config-middle.xml";
    private static final String MYBATIS_CONFIG_TEST = "mybatis-config-test.xml";
    private static SqlSessionFactory middleSqlSessionFactory;
    private static SqlSessionFactory testSqlSessionFactory;
    private static Reader middleResourceAsReader =null;
    private static Reader testResourceAsReader =null;
    static {
        try {
            middleResourceAsReader = Resources.getResourceAsReader(MYBATIS_CONFIG_MIDDLE);
            testResourceAsReader = Resources.getResourceAsReader(MYBATIS_CONFIG_TEST);
            middleSqlSessionFactory=new SqlSessionFactoryBuilder().build(middleResourceAsReader);
            testSqlSessionFactory=new SqlSessionFactoryBuilder().build(testResourceAsReader);
        } catch (IOException e) {
            e.printStackTrace();
        }finally {
            try {
                middleResourceAsReader.close();
                testResourceAsReader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
    public static SqlSession getSqlSession(String type){
        if ("test".equals(type)){
            return testSqlSessionFactory.openSession();
        }
        return middleSqlSessionFactory.openSession();
    }
}
```

SqlSessionUtil.java

### sql脚本

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50728
 Source Host           : localhost:3306
 Source Schema         : middle

 Target Server Type    : MySQL
 Target Server Version : 50728
 File Encoding         : 65001

 Date: 07/10/2020 22:42:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(255) NOT NULL COMMENT '姓名',
  `sex` varchar(255) DEFAULT NULL COMMENT '性别',
  `address` varchar(255) DEFAULT NULL COMMENT '地址',
  `department` varchar(255) DEFAULT NULL COMMENT '系',
  `add_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '数据进入中间表时间',
  `data_status` varchar(10) NOT NULL DEFAULT 'I' COMMENT 'I:第三方系统入库；D:处理中；F:处理完成；E:发生错误或异常',
  `deal_time` datetime DEFAULT NULL COMMENT '处理时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of student
-- ----------------------------
BEGIN;
INSERT INTO `student` VALUES (1, '张三', '男', '上海', '英语系', '2020-10-07 22:19:25', 'F', '2020-10-07 22:19:26');
INSERT INTO `student` VALUES (2, '李四', '女', '北京', '中文系', '2020-10-07 22:19:25', 'F', '2020-10-07 22:19:26');
INSERT INTO `student` VALUES (3, '王五', '男', '天津', '计算机系', '2020-10-07 22:19:25', 'F', '2020-10-07 22:19:26');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
```

middle.student

![](./images/images/img_008_8f900a89c634.gif)
![](./images/images/img_009_961ddebeb323.gif)

```text
/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50728
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 50728
 File Encoding         : 65001

 Date: 07/10/2020 22:45:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(255) DEFAULT NULL COMMENT '姓名',
  `sex` varchar(255) DEFAULT NULL COMMENT '性别',
  `department` varchar(255) DEFAULT NULL COMMENT '系',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
```

test.student

## 演示

![](./images/images/img_010_a6fb5a5253f7.gif)

## 项目源码下载

```text
链接: https://pan.baidu.com/s/1C7q7_QRUhRoCZIVZ_Bp3KQ  密码: 7hbf
```

# 部署如何启动指定main

## 修改pom.xml

　　mainClass指定启动包下的main

```text
 <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <!-- 默认启动 程序，mainClass指定启动的main函数的报名 -->
                    <mainClass>com.cyb.start.Main</mainClass>
                    <layout>JAR</layout>
                    <addResources>true</addResources>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>repackage</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
```

## 修改log4j.properties日志输出目录

![](./images/images/img_011_ae7c6ab2f47f.png)

## 部署

![](./images/images/img_012_591d4d482129.gif)

![](./images/images/img_013_1c8286f00728.gif)
