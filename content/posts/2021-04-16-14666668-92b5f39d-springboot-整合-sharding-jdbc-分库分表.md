{

  "title": "SpringBoot 整合 Sharding-JDBC 分库分表",
  "date": "2021-04-16",
  "description": "导读 分库分表的技术有：数据库中间件Mycat(点我直达)，当当网开源的Sharding-JDBC；我们公司用的也是sharding-jdbc，自己也搭建一个完整的项目，直接可以拿来用。下面附源码(CRUD，分页，事务等都已测试过) 技术栈 SpringBoot 2.3.9 sharding-jdb",
  "tags": [
    "Spring Boot",
    "Sharding-JDBC"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/14666668.html"

}

# 导读

　　分库分表的技术有：数据库中间件Mycat([点我直达](https://www.cnblogs.com/chenyanbin/p/13159469.html))，当当网开源的Sharding-JDBC；我们公司用的也是sharding-jdbc，自己也搭建一个完整的项目，直接可以拿来用。下面附源码(CRUD，分页，事务等都已测试过)

# 技术栈

- SpringBoot 2.3.9
- sharding-jdbc-core 2.0.3 （官网地址：[点我直达](https://shardingsphere.apache.org/document/legacy/3.x/document/cn/overview/)）
- druid
- mybatis-plus
- lombok
- mybatis | mybatisplus 分页功能
- 统一异常处理器

## 项目结构

![](/imported/posts/2021-04-16-14666668-92b5f39d-springboot-整合-sharding-jdbc-分库分表/images/img_001_7d883cf480ff.png)

### pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.3.9.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.ybchen</groupId>
    <artifactId>springboot-sharding</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>springboot-sharding</name>
    <description>Demo project for Spring Boot</description>
    <properties>
        <java.version>1.8</java.version>
        <maven.compiler.target>1.8</maven.compiler.target>
        <maven.compiler.source>1.8</maven.compiler.source>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
            <exclusions>
                <exclusion>
                    <groupId>org.junit.vintage</groupId>
                    <artifactId>junit-vintage-engine</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <!--sharding-->
        <dependency>
            <groupId>io.shardingjdbc</groupId>
            <artifactId>sharding-jdbc-core</artifactId>
            <version>2.0.3</version>
        </dependency>
        <!--mysql-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!--druid-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.2.5</version>
        </dependency>
        <!--mybatisplus-->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.4.1</version>
        </dependency>
        <!--mybatis pagehelper分页插件-->
        <dependency>
            <groupId>com.github.pagehelper</groupId>
            <artifactId>pagehelper</artifactId>
            <version>5.2.0</version>
        </dependency>
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.20</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
        <resources>
            <resource>
                <directory>src/main/java</directory>
                <includes>
                    <include>**/*.xml</include>
                </includes>
            </resource>
            <resource>
                <directory>src/main/resources</directory>
            </resource>
        </resources>
    </build>
</project>
```

### logback-spring.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<!-- 日志级别从低到高分为TRACE < DEBUG < INFO < WARN < ERROR < FATAL，如果设置为WARN，则低于WARN的信息都不会输出 -->
<!-- scan:当此属性设置为true时，配置文件如果发生改变，将会被重新加载，默认值为true -->
<!-- scanPeriod:设置监测配置文件是否有修改的时间间隔，如果没有给出时间单位，默认单位是毫秒。当scan为true时，此属性生效。默认的时间间隔为1分钟。 -->
<!-- debug:当此属性设置为true时，将打印出logback内部日志信息，实时查看logback运行状态。默认值为false。 -->
<configuration  scan="true" scanPeriod="10 seconds">

    <contextName>logback</contextName>
    <!-- name的值是变量的名称，value的值时变量定义的值。通过定义的值会被插入到logger上下文中。定义变量后，可以使“${}”来使用变量。 -->
    <property name="log.path" value="applog/" />
    <property name="log.name" value="springboot-sharding"/>
    <!--控制台打印格式-->
    <property name="CONSOLE_LOG_PATTERN_FILE" value="%d{yyyy-MM-dd HH:mm:ss.SSS} %C:%M:%L [%thread] %-5level %msg%n"/>
    <!--debug文件打印格式-->
    <property name="DEBUG_LOG_PATTERN_FILE" value="%d{yyyy-MM-dd HH:mm:ss} [%c]-[%p] %m%n"/>

    <!-- 彩色日志 -->
    <!-- 彩色日志依赖的渲染类 -->
    <conversionRule conversionWord="clr" converterClass="org.springframework.boot.logging.logback.ColorConverter" />
    <conversionRule conversionWord="wex" converterClass="org.springframework.boot.logging.logback.WhitespaceThrowableProxyConverter" />
    <conversionRule conversionWord="wEx" converterClass="org.springframework.boot.logging.logback.ExtendedWhitespaceThrowableProxyConverter" />
    <!-- 彩色日志格式 -->
    <property name="CONSOLE_LOG_PATTERN" value="${CONSOLE_LOG_PATTERN:-%clr(%d{yyyy-MM-dd HH:mm:ss.SSS}){faint} %clr(${LOG_LEVEL_PATTERN:-%5p}) %clr(${PID:- }){magenta} %clr(---){faint} %clr([%15.15t]){faint} %clr(%-40.40logger{39}){cyan} %clr(:){faint} %m%n${LOG_EXCEPTION_CONVERSION_WORD:-%wEx}}"/>

    <!--输出到控制台-->
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <!--此日志appender是为开发使用，只配置最底级别，控制台输出的日志级别是大于或等于此级别的日志信息-->
        <filter class="ch.qos.logback.classic.filter.ThresholdFilter">
            <level>debug</level>
        </filter>
        <encoder>
            <Pattern>${CONSOLE_LOG_PATTERN}</Pattern>
            <!-- 设置字符集 -->
            <charset>UTF-8</charset>
        </encoder>
    </appender>

    <!--输出到文件-->
    <!-- 时间滚动输出 level为 INFO 日志 -->
    <appender name="INFO_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 正在记录的日志文件的路径及文件名 -->
        <file>${log.path}/${log.name}/${log.name}_info.log</file>
        <!--日志文件输出格式-->
        <encoder>
            <pattern>${CONSOLE_LOG_PATTERN_FILE}</pattern>
            <charset>UTF-8</charset>
        </encoder>
        <!-- 日志记录器的滚动策略，按日期，按大小记录 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <!-- 每天日志归档路径以及格式 -->
            <fileNamePattern>${log.path}/${log.name}/info/${log.name}-info-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <!--日志文件保留天数-->
            <maxHistory>15</maxHistory>
        </rollingPolicy>
        <!-- 此日志文件只记录info级别的 -->
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>info</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <!-- 时间滚动输出 level为 debug 日志 -->
    <appender name="DEBUG_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 正在记录的日志文件的路径及文件名 -->
        <file>${log.path}/${log.name}/${log.name}_debug.log</file>
        <!--日志文件输出格式-->
        <encoder>
            <pattern>${DEBUG_LOG_PATTERN_FILE}</pattern>
            <charset>UTF-8</charset> <!-- 此处设置字符集 -->
        </encoder>
        <!-- 日志记录器的滚动策略，按日期，按大小记录 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${log.path}/${log.name}/debug/${log.name}-debug-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <!--日志文件保留天数-->
            <maxHistory>15</maxHistory>
        </rollingPolicy>
        <!-- 此日志文件只记录DEBUG级别的 -->
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>DEBUG</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <!-- 时间滚动输出 level为 ERROR 日志 -->
    <appender name="ERROR_FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
        <!-- 正在记录的日志文件的路径及文件名 -->
        <file>${log.path}/${log.name}/${log.name}_error.log</file>
        <!--日志文件输出格式-->
        <encoder>
            <pattern>${CONSOLE_LOG_PATTERN_FILE}</pattern>
            <charset>UTF-8</charset> <!-- 此处设置字符集 -->
        </encoder>
        <!-- 日志记录器的滚动策略，按日期，按大小记录 -->
        <rollingPolicy class="ch.qos.logback.core.rolling.TimeBasedRollingPolicy">
            <fileNamePattern>${log.path}/${log.name}/error/${log.name}-error-%d{yyyy-MM-dd}.%i.log</fileNamePattern>
            <timeBasedFileNamingAndTriggeringPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedFNATP">
                <maxFileSize>100MB</maxFileSize>
            </timeBasedFileNamingAndTriggeringPolicy>
            <!--日志文件保留天数-->
            <maxHistory>15</maxHistory>
        </rollingPolicy>
        <!-- 此日志文件只记录ERROR级别的 -->
        <filter class="ch.qos.logback.classic.filter.LevelFilter">
            <level>ERROR</level>
            <onMatch>ACCEPT</onMatch>
            <onMismatch>DENY</onMismatch>
        </filter>
    </appender>

    <root level="info">
        <appender-ref ref="CONSOLE" />
        <appender-ref ref="INFO_FILE" />
        <appender-ref ref="DEBUG_FILE" />
        <appender-ref ref="ERROR_FILE" />
    </root>
    <logger name="com.ybchen.mapper" level="DEBUG"/>
    <logger name="com.ybchen" level="DEBUG"/>
</configuration>
```

### application.properties

```text
server.port=9999
# ds0
ds0.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
ds0.datasource.url=jdbc:mysql://localhost:3306/online_education?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai
ds0.datasource.username=root
ds0.datasource.password=root
# ds1
ds1.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
ds1.datasource.url=jdbc:mysql://localhost:3306/online_education1?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai
ds1.datasource.username=root
ds1.datasource.password=root
```

### UserMapper.xml

```text
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="com.ybchen.mapper.UserMapper">
    <select id="all" resultType="com.ybchen.domain.UserDO">
        SELECT * FROM t_user
    </select>
    <insert id="add" parameterType="com.ybchen.domain.UserDO">
        INSERT INTO `t_user` (`id`, `user_name`, `age`, `create_time`, `tags`) VALUES (#{id}, #{userName}, #{age}, #{createTime}, #{tags})
    </insert>
    <update id="update" parameterType="com.ybchen.domain.UserDO">
        update t_user set user_name=#{userName} where id=#{id}
    </update>
    <delete id="delete">
        delete from t_user where id=#{id}
    </delete>
</mapper>
```

### SpringBootShardingApplication.java

```text
package com.ybchen;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;
import org.springframework.transaction.annotation.EnableTransactionManagement;

//忽略自动装配DataSource
@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
//扫描Mapper
@MapperScan("com.ybchen.mapper")
//开启事务
@EnableTransactionManagement
public class SpringbootShardingApplication {

    public static void main(String[] args) {
        SpringApplication.run(SpringbootShardingApplication.class, args);
    }

}
```

### DataSourceConfig.java

```text
package com.ybchen;

import com.alibaba.druid.filter.Filter;
import com.alibaba.druid.filter.stat.StatFilter;
import com.alibaba.druid.pool.DruidDataSource;
import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import com.baomidou.mybatisplus.extension.spring.MybatisSqlSessionFactoryBean;
import com.github.pagehelper.PageInterceptor;
import com.google.common.collect.Lists;
import groovy.util.logging.Slf4j;
import io.shardingjdbc.core.api.ShardingDataSourceFactory;
import io.shardingjdbc.core.api.config.ShardingRuleConfiguration;
import io.shardingjdbc.core.api.config.TableRuleConfiguration;
import io.shardingjdbc.core.api.config.strategy.InlineShardingStrategyConfiguration;
import org.apache.ibatis.plugin.Interceptor;
import org.apache.ibatis.session.SqlSessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;
import org.springframework.transaction.annotation.EnableTransactionManagement;

import javax.sql.DataSource;
import java.sql.SQLException;
import java.util.*;

/**
 * @Description：配置参考链接：https://shardingsphere.apache.org/document/legacy/3.x/document/cn/manual/sharding-jdbc/configuration/config-java/
 * @Author：chenyanbin
 * @Date：2021/4/15 上午11:44
 * @Versiion：1.0
 */
@Configuration
@EnableTransactionManagement
@Slf4j
public class DataSourceConfig {
    @Autowired
    private Environment env;

    @Bean
    public Filter statFilter() {
        StatFilter filter = new StatFilter();
        filter.setSlowSqlMillis(5000);
        filter.setLogSlowSql(true);
        filter.setMergeSql(true);
        return filter;
    }

    @Bean("sqlSessionFactory")
    SqlSessionFactory sqlSessionFactory(
    ) throws Exception {
        final MybatisSqlSessionFactoryBean sessionFactory = new MybatisSqlSessionFactoryBean();
        //设置数据源
        sessionFactory.setDataSource(dataSource());
        //设置分页
        sessionFactory.setPlugins(new Interceptor[]{mybatisPlusInterceptor(), pageInterceptor()});
        //mapper扫描路径
        Resource[] r1 = new PathMatchingResourcePatternResolver()
                .getResources("classpath*:com/ybchen/mapper/xml/*.xml");
        Resource[] r2 = new PathMatchingResourcePatternResolver()
                .getResources("classpath*:mapper/*.xml");
        List<Resource> list = new ArrayList<>();
        list.addAll(Arrays.asList(r1));
        list.addAll(Arrays.asList(r2));
        sessionFactory.setMapperLocations(list.toArray(new Resource[list.size()]));
        return sessionFactory.getObject();
    }

    //事务管理
    @Bean
    public DataSourceTransactionManager transactitonManager(@Autowired DataSource dataSource) {
        return new DataSourceTransactionManager(dataSource);
    }

    //mybatis 分页
    public PageInterceptor pageInterceptor() {
        PageInterceptor pi = new PageInterceptor();
        Properties p = new Properties();
        //当该参数设置为 true 时，pageNum<=0 时会查询第一页， pageNum>pages（超过总数时），会查询最后一页
        p.setProperty("reasonable", "true");
        pi.setProperties(p);
        return pi;
    }

    //mybatis plus分页
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        MybatisPlusInterceptor mybatisPlusInterceptor = new MybatisPlusInterceptor();
        mybatisPlusInterceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
        return mybatisPlusInterceptor;
    }

    @Bean
    public DataSource dataSource() throws SQLException {
        ShardingRuleConfiguration shardingRuleConfig = new ShardingRuleConfiguration();
        //添加表
        shardingRuleConfig.getTableRuleConfigs().add(tUserTableRuleConfiguration());
        Properties properties = new Properties();
        //是否开启SQL显示，默认值: false
//        properties.setProperty("sql.show", "true");
        return ShardingDataSourceFactory.createDataSource(createDataSourceMap(), shardingRuleConfig, new HashMap<>(), properties);
    }

    /**
     * 表分片规则配置对象,表：t_user
     * 参考链接：https://shardingsphere.apache.org/document/legacy/3.x/document/cn/manual/sharding-jdbc/configuration/config-java/
     *
     * @return
     */
    TableRuleConfiguration tUserTableRuleConfiguration() {
        TableRuleConfiguration result = new TableRuleConfiguration();
        //逻辑表名称
        result.setLogicTable("t_user");
        //由数据源名 + 表名组成，以小数点分隔。多个表以逗号分隔，支持inline表达式。缺省表示使用已知数据源与逻辑表名称生成数据节点。用于广播表（即每个库中都需要一个同样的表用于关联查询，多为字典表）或只分库不分表且所有库的表结构完全一致的情况
        result.setActualDataNodes("ds${0..1}.t_user");
        //分片列名称
        final String shardingColumn = "tags";
        //分片算法行表达式，需符合groovy语法，表达式参考：https://shardingsphere.apache.org/document/legacy/3.x/document/cn/features/sharding/other-features/inline-expression/
        final String algorithmExpression = "ds${tags%2}";
        //ShardingStrategyConfiguration的实现类，用于配置行表达式分片策略。
        result.setDatabaseShardingStrategyConfig(new InlineShardingStrategyConfiguration(shardingColumn, algorithmExpression));
        //自增列名称，缺省表示不适用自增主键生成器
//        result.setKeyGeneratorColumnName("id");
        return result;
    }

    Map<String, DataSource> createDataSourceMap() {
        Map<String, DataSource> result = new HashMap<>();
        result.put("ds0", dataSource_0());
        result.put("ds1", dataSource_1());
        return result;
    }

    /**
     * 数据源-0
     *
     * @return
     */
    public DataSource dataSource_0() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(env.getProperty("ds0.datasource.driver-class-name"));
        dataSource.setUrl(env.getProperty("ds0.datasource.url"));
        dataSource.setUsername(env.getProperty("ds0.datasource.username"));
        dataSource.setPassword(env.getProperty("ds0.datasource.password"));
        dataSource.setProxyFilters(Lists.newArrayList(statFilter()));
        //每个分区最大的连接数
        dataSource.setMaxActive(20);
        //每个分区最小的连接数
        dataSource.setMinIdle(5);
        return dataSource;
    }

    /**
     * 数据源-1
     *
     * @return
     */
    public DataSource dataSource_1() {
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setDriverClassName(env.getProperty("ds1.datasource.driver-class-name"));
        dataSource.setUrl(env.getProperty("ds1.datasource.url"));
        dataSource.setUsername(env.getProperty("ds1.datasource.username"));
        dataSource.setPassword(env.getProperty("ds1.datasource.password"));
        dataSource.setProxyFilters(Lists.newArrayList(statFilter()));
        //每个分区最大的连接数
        dataSource.setMaxActive(20);
        //每个分区最小的连接数
        dataSource.setMinIdle(5);
        return dataSource;
    }
}
```

### GlobalExceptions.java

```text
package com.ybchen.exception;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;

/**
 * @ClassName：GlobalExceptiions
 * @Description：全局异常
 * @Author：chenyb
 * @Date：2021/4/15 上午11:44
 * @Versiion：1.0
 */
@ControllerAdvice
public class GlobalExceptions {
    private final Logger logger = LoggerFactory.getLogger(getClass());

    @ExceptionHandler(value = Exception.class)
    @ResponseBody
    public Object handle(Exception ex) {
        logger.error("「 全局异常 」 ===============》{}", ex);
        return "「 全局异常 」错误信息:"+ex.getMessage();
    }
}
```

### UserDO.java

```text
package com.ybchen.domain;

import java.util.Date;

/**
 * @Description：mybatis方式实体类
 * @Author：chenyanbin
 * @Date：2021/4/16 上午9:47
 * @Versiion：1.0
 */
public class UserDO {
    private String id;
    private String userName;
    private Integer age;
    private Date createTime;
    private Integer tags;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public Date getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Date createTime) {
        this.createTime = createTime;
    }

    public Integer getTags() {
        return tags;
    }

    public void setTags(Integer tags) {
        this.tags = tags;
    }

    @Override
    public String toString() {
        return "UserDO{" +
                "id='" + id + '\'' +
                ", userName='" + userName + '\'' +
                ", age=" + age +
                ", createTime=" + createTime +
                ", tags=" + tags +
                '}';
    }
}
```

### UserMybatisDO.java

```text
package com.ybchen.domain;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;

import java.util.Date;

/**
 * @Description：mybatis plus方式实体类
 * @Author：chenyanbin
 * @Date：2021/4/16 上午9:47
 * @Versiion：1.0
 */
@TableName("t_user")
public class UserMybatisDO {
    @TableId(value = "id")
    private String id;
    @TableField("user_name")
    private String userName;
    @TableField("age")
    private Integer age;
    @TableField("create_time")
    private Date createTime;
    @TableField("tags")
    private Integer tags;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getUserName() {
        return userName;
    }

    public void setUserName(String userName) {
        this.userName = userName;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public Date getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Date createTime) {
        this.createTime = createTime;
    }

    public Integer getTags() {
        return tags;
    }

    public void setTags(Integer tags) {
        this.tags = tags;
    }

    @Override
    public String toString() {
        return "UserMybatisDO{" +
                "id='" + id + '\'' +
                ", userName='" + userName + '\'' +
                ", age=" + age +
                ", createTime=" + createTime +
                ", tags=" + tags +
                '}';
    }
}
```

### UserMapper.java

```text
package com.ybchen.mapper;

import com.ybchen.domain.UserDO;

import java.util.List;

public interface UserMapper {
    //查询
    List<UserDO> all();

    //添加
    Integer add(UserDO userDO);

    //更新
    Integer update(UserDO userDO);

    //删除
    Integer delete(String id);
}
```

### UserMybatisPlusMapper.java

```text
package com.ybchen.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.ybchen.domain.UserMybatisDO;

public interface UserMybatisPlusMapper extends BaseMapper<UserMybatisDO> {
}
```

### UserService.java

```text
package com.ybchen.service;

import com.ybchen.domain.UserDO;
import com.ybchen.domain.UserMybatisDO;

import java.util.List;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/4/15 下午4:52
 * @Versiion：1.0
 */
public interface UserService {
    //mybatis 查询
    List<UserDO> all();

    //mybatisplus 查询
    List<UserMybatisDO> allMybatisPlus();

    //添加
    Integer add(UserDO userDO);

    //更新
    Integer update(UserDO userDO);

    //删除
    Integer delete(String id);
}
```

### UserServiceImpl.java

```text
package com.ybchen.service.impl;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.github.pagehelper.PageHelper;
import com.ybchen.domain.UserDO;
import com.ybchen.domain.UserMybatisDO;
import com.ybchen.mapper.UserMapper;
import com.ybchen.mapper.UserMybatisPlusMapper;
import com.ybchen.service.UserService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.List;
import java.util.UUID;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/4/15 下午4:53
 * @Versiion：1.0
 */
@Service
@Slf4j
public class UserServiceImpl implements UserService {
    @Autowired
    UserMapper userMapper;
    @Autowired
    UserMybatisPlusMapper userMybatisPlusMapper;

    @Override
    public List<UserDO> all() {
        log.info("---info----");
        log.debug("----debug----");
        log.error("----error----");
        //mybatis 分页
        PageHelper.startPage(4, 3);
        return userMapper.all();
    }

    @Override
    public List<UserMybatisDO> allMybatisPlus() {
        //mybatis plus 分页
        int start = 4;
        int end = 3;
        IPage<UserMybatisDO> page = new Page<>(start, end);
        return userMybatisPlusMapper.selectPage(page, null).getRecords();
    }

    @Override
    //开启事务
    @Transactional
    public Integer add(UserDO userDO) {
        userDO.setId(UUID.randomUUID().toString().replace("-", ""));
        userDO.setTags(LocalDateTime.now().getSecond());
        userMapper.add(userDO);
        //模拟事务失败
        int num = 1 / 0;
        userDO.setAge(99);
        userDO.setId(UUID.randomUUID().toString().replace("-", ""));
        return userMapper.add(userDO);
    }

    @Override
    public Integer update(UserDO userDO) {
        return userMapper.update(userDO);
    }

    @Override
    public Integer delete(String id) {
        return userMapper.delete(id);
    }
}
```

### UserController.java

```text
package com.ybchen.controller;

import com.ybchen.domain.UserDO;
import com.ybchen.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2021/4/15 下午4:52
 * @Versiion：1.0
 */
@RestController
public class UserController {
    @Autowired
    private UserService userService;

    @PostMapping("all")
    public Object all() {
        return userService.all();
    }

    @PostMapping("allMybatisPlus")
    public Object allMybatisPlus() {
        return userService.allMybatisPlus();
    }

    @PostMapping("add")
    public Object add(@RequestBody UserDO userDO) {
        return userService.add(userDO);
    }

    @PostMapping("update")
    public Object update(@RequestBody UserDO userDO) {
        return userService.update(userDO);
    }

    @GetMapping("delete")
    public Object delete(@RequestParam("id") String id) {
        return userService.delete(id);
    }
}
```

## 数据库

![](/imported/posts/2021-04-16-14666668-92b5f39d-springboot-整合-sharding-jdbc-分库分表/images/img_002_82b18fd88726.png)

## 案例源码

```text
链接: https://pan.baidu.com/s/1j8h4YJSShWKYjwCeX56O_w  密码: 8fpe
```
