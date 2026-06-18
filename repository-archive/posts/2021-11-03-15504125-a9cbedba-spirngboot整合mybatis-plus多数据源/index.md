{

  "title": "SpirngBoot整合Mybatis Plus多数据源",
  "date": "2021-11-03",
  "description": "导读 有一个这样子的需求，线上正在跑的业务，由于业务发展需要，需重新开发一套新系统，等新系统开发完成后，需要无缝对接切换，当初具体设计见草图。 添加依赖 application.properties 种方式创建DataSource Master配置，使用druid连接池 注：mybatis plus",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/15504125.html"

}

# 导读

　　有一个这样子的需求，线上正在跑的业务，由于业务发展需要，需重新开发一套新系统，等新系统开发完成后，需要无缝对接切换，当初具体设计见草图。

![](./images/images/img_001_75aa0d561f03.png)

# 添加依赖

```text
        <!--lombok-->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.16</version>
            <!--scope=provided，说明它是在编译阶段生效，不需要打入包中，Lombok在编译期将带Lombok注解的Java文件正确编译为完整的Class文件-->
            <scope>provided</scope>
        </dependency>
        <!--mysql-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <!--mybatis plus和spring boot整合-->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.4.0</version>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.10</version>
        </dependency>
```

# application.properties

```text
server.port=9999
spring.datasource.master.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.master.url=jdbc:mysql://127.0.0.1/test?useUnicode=true&characterEncoding=utf-8&useSSL=false
spring.datasource.master.username=root
spring.datasource.master.password=root

spring.datasource.slave.driver-class-name=com.mysql.cj.jdbc.Driver
spring.datasource.slave.jdbc-url=jdbc:mysql://127.0.0.1/test2?useUnicode=true&characterEncoding=utf-8&useSSL=false
spring.datasource.slave.username=root
spring.datasource.slave.password=root
```

# 2种方式创建DataSource

## Master配置，使用druid连接池

```text
import com.alibaba.druid.pool.DruidDataSource;
import com.baomidou.mybatisplus.extension.spring.MybatisSqlSessionFactoryBean;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;
import org.springframework.core.env.Environment;

import javax.sql.DataSource;

/**
 * @Author：chenyanbin
 */
@Configuration
@MapperScan(basePackages = "com.example.demo.mapper", sqlSessionFactoryRef = "masterSqlSessionFactory")
public class MasterDataSourceConfig {
    @Autowired
    private Environment env;

    @Primary
    @Bean(name = "masterDataSource")
//    @ConfigurationProperties("spring.datasource.master")
    public DataSource masterDataSource() {
//        return DataSourceBuilder.create().build();
        DruidDataSource dataSource = new DruidDataSource();
        dataSource.setUrl(env.getProperty("spring.datasource.master.url"));
        dataSource.setUsername(env.getProperty("spring.datasource.master.username"));
        dataSource.setPassword(env.getProperty("spring.datasource.master.password"));
        dataSource.setDriverClassName(env.getProperty("spring.datasource.master.driver-class-name"));
        //配置初始化大小、最小、最大
        dataSource.setMinIdle(10);
        //配置初始化大小、最小、最大
        dataSource.setMaxActive(200);
        //配置初始化大小、最小、最大
        dataSource.setInitialSize(10);
        //配置获取连接等待超时的时间
        dataSource.setMaxWait(60000);
        //配置一个连接在池中最小生存的时间,单位是毫秒
        dataSource.setMinEvictableIdleTimeMillis(300000);
        //配置间隔多久才进行一次检测,检测需要关闭的空闲连接,单位是毫秒
        dataSource.setTimeBetweenEvictionRunsMillis(60000);
        //默认的testWhileIdle=true,testOnBorrow=false,testOnReturn=false
        dataSource.setValidationQuery("SELECT 1");
        //申请连接时执行validationQuery检测连接是否有效
        dataSource.setTestOnBorrow(false);
        //建议配置为true，不影响性能，并且保证安全性。
        dataSource.setTestWhileIdle(true);
        //是否缓存preparedStatement，也就是PSCache
        dataSource.setPoolPreparedStatements(false);
        return dataSource;
    }

    @Bean(name = "masterSqlSessionFactory")
    public SqlSessionFactory sqlSessionFactory(@Qualifier("masterDataSource") DataSource dataSource) throws Exception {
        MybatisSqlSessionFactoryBean sessionFactoryBean = new MybatisSqlSessionFactoryBean();
        sessionFactoryBean.setDataSource(dataSource);

        return sessionFactoryBean.getObject();
    }
}
```

注：mybatis plus枚举值映射不上，加上GlobalConfig、Configuration、枚举值路径

```text
    @Bean(name = "qaSqlSessionFactory")
    public SqlSessionFactory sqlSessionFactory(@Qualifier("qaDataSource") DataSource dataSource,@Qualifier("qaMybatisPlusInterceptor") MybatisPlusInterceptor interceptor) throws Exception {
        MybatisSqlSessionFactoryBean sessionFactoryBean = new MybatisSqlSessionFactoryBean();
        sessionFactoryBean.setDataSource(dataSource);
//        MybatisConfiguration configuration = new MybatisConfiguration();
//        configuration.setLogImpl(org.apache.ibatis.logging.stdout.StdOutImpl.class);
//        sessionFactoryBean.setConfiguration(configuration);
        sessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver()
                .getResources("classpath:mapper/**/*.xml"));
        // 🔥 关键：开启 MP 枚举支持
        GlobalConfig globalConfig = new GlobalConfig();
        sessionFactoryBean.setGlobalConfig(globalConfig);
        MybatisConfiguration configuration = new MybatisConfiguration();
        configuration.setMapUnderscoreToCamelCase(true);
        sessionFactoryBean.setConfiguration(configuration);
        sessionFactoryBean.setTypeEnumsPackage("com.ybchen.enums");
        System.out.println("prod数据源初始化完成.....");
        sessionFactoryBean.setPlugins(interceptor);
        System.out.println("qa数据源初始化完成.....");
        return sessionFactoryBean.getObject();
    }
```

## Slave配置

```text
import com.baomidou.mybatisplus.extension.spring.MybatisSqlSessionFactoryBean;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.boot.jdbc.DataSourceBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;

/**
 * @Author：chenyanbin
 */
@Configuration
@MapperScan(basePackages = "com.example.demo.mapper2",sqlSessionFactoryRef = "slaveSqlSessionFactory")
public class SlaveDataSourceConfig {
    @Bean(name = "slaveDataSource")
    @ConfigurationProperties("spring.datasource.slave")
    public DataSource slaveDataSource(){
        return DataSourceBuilder.create().build();
    }

    @Bean(name = "slaveSqlSessionFactory")
    public SqlSessionFactory sqlSessionFactory(@Qualifier("slaveDataSource") DataSource dataSource) throws Exception {
        MybatisSqlSessionFactoryBean sessionFactoryBean = new MybatisSqlSessionFactoryBean();
        sessionFactoryBean.setDataSource(dataSource);
        return sessionFactoryBean.getObject();
    }
}
```

## 注意

**master和slave扫描不同的mapper包路径！！！！！！**

**如果需要指定.xml文件，需这样配置！！！**

```text
    @Bean(name = "masterSqlSessionFactory")
    public SqlSessionFactory sqlSessionFactory(@Qualifier("masterDataSource") DataSource dataSource) throws Exception {
        MybatisSqlSessionFactoryBean sessionFactoryBean = new MybatisSqlSessionFactoryBean();
        sessionFactoryBean.setDataSource(dataSource);
        sessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver()
                .getResources("classpath:mapper/**/*.xml"));
        return sessionFactoryBean.getObject();
    }
```

![](./images/images/img_002_e930a655e269.png)

## MybatisPlus分页插件设置

```text
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * MybatisPlus分页配置
 *
 * @Author：chenyanbin
 */
@Configuration
public class MybatisPlusPageConfig {

    /**
     * 新版分页插件
     *
     * @return
     */
    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor() {
        MybatisPlusInterceptor mybatisPlusInterceptor = new MybatisPlusInterceptor();
        mybatisPlusInterceptor.addInnerInterceptor(new PaginationInnerInterceptor());
        return mybatisPlusInterceptor;
    }
}
```

```text
    @Bean(name = "masterSqlSessionFactory")
    public SqlSessionFactory sqlSessionFactory(
            @Qualifier("masterDataSource") DataSource dataSource,
            @Qualifier("mybatisPlusInterceptor") MybatisPlusInterceptor mybatisPlusInterceptor
    ) throws Exception {
        MybatisSqlSessionFactoryBean sessionFactoryBean = new MybatisSqlSessionFactoryBean();
        sessionFactoryBean.setDataSource(dataSource);
        sessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver()
                .getResources("classpath:mapper/**/*.xml"));
        sessionFactoryBean.setPlugins(mybatisPlusInterceptor);
        return sessionFactoryBean.getObject();
    }
```

## 设置填充字段

```text
import com.baomidou.mybatisplus.core.handlers.MetaObjectHandler;import org.apache.ibatis.reflection.MetaObject;
import org.springframework.stereotype.Component;

/**
 * @Author：chenyanbin
 */
@Component
public class CustomMetaObjectHandler implements MetaObjectHandler {
    @Override
    public void insertFill(MetaObject metaObject) {
        //属性名称，不是字段名称
        this.setFieldValByName("createTime", CommonUtil.getCurrentDate(), metaObject);
        this.setFieldValByName("createUserId", CommonUtil.getCurrentUserId(), metaObject);
        this.setFieldValByName("createUserName", CommonUtil.getCurrentUserName(), metaObject);
    }

    @Override
    public void updateFill(MetaObject metaObject) {
        //属性名称，不是字段名称
        this.setFieldValByName("updateTime", CommonUtil.getCurrentDate(), metaObject);
        this.setFieldValByName("updateUserId", CommonUtil.getCurrentUserId(), metaObject);
        this.setFieldValByName("updateUserName", CommonUtil.getCurrentUserName(), metaObject);
    }
}
```

```text
/**
 * <p>
 * 角色信息表
 * </p>
 *
 * @author chenyanbin
 * @since 2021-09-28
 */
@Data
@TableName("sys_role")
@ApiModel(value = "SysRoleDO对象", description = "角色信息表")
public class RoleDO implements Serializable {

    private static final long serialVersionUID = 1L;

    @ApiModelProperty(value = "角色ID")
    @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    @ApiModelProperty(value = "角色名称")
    private String roleName;

    @ApiModelProperty(value = "角色状态（0正常 1停用）")
    private byte status;

    @ApiModelProperty(value = "备注")
    private String remark;

    @ApiModelProperty(value = "创建时间")
    @TableField(value = "create_time", fill = FieldFill.INSERT)
    private Date createTime;

    @ApiModelProperty(value = "创建人id")
    @TableField(value = "create_user_id", fill = FieldFill.INSERT)
    private Long createUserId;

    @ApiModelProperty(value = "创建人姓名")
    @TableField(value = "create_user_name", fill = FieldFill.INSERT)
    private String createUserName;

    @ApiModelProperty(value = "修改时间")
    @TableField(value = "update_time", fill = FieldFill.UPDATE)
    private Date updateTime;

    @ApiModelProperty(value = "修改人id")
    @TableField(value = "update_user_id", fill = FieldFill.UPDATE)
    private Long updateUserId;

    @ApiModelProperty(value = "修改人姓名")
    @TableField(value = "update_user_name", fill = FieldFill.UPDATE)
    private String updateUserName;

}
```

```text
    import com.baomidou.mybatisplus.core.config.GlobalConfig;

    @Bean(name = "masterSqlSessionFactory")
    public SqlSessionFactory sqlSessionFactory(
            @Qualifier("masterDataSource") DataSource dataSource,
            @Qualifier("mybatisPlusInterceptor") MybatisPlusInterceptor mybatisPlusInterceptor,
            @Qualifier("customMetaObjectHandler") CustomMetaObjectHandler customMetaObjectHandler
    ) throws Exception {
        MybatisSqlSessionFactoryBean sessionFactoryBean = new MybatisSqlSessionFactoryBean();
        sessionFactoryBean.setDataSource(dataSource);
        sessionFactoryBean.setMapperLocations(new PathMatchingResourcePatternResolver()
                .getResources("classpath:mapper/**/*.xml"));
        //mybatis plus分页插件
        sessionFactoryBean.setPlugins(mybatisPlusInterceptor);
        //自动填充字段
        GlobalConfig globalConfig=new GlobalConfig();
        globalConfig.setMetaObjectHandler(customMetaObjectHandler);
        sessionFactoryBean.setGlobalConfig(globalConfig);
        return sessionFactoryBean.getObject();
    }
```

## 多数据源事务问题

```text
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.jdbc.datasource.DataSourceTransactionManager;

import javax.sql.DataSource;

/**
 * 事务
 *
 * @Author：chenyanbin
 */
@Configuration
public class CustomTransactionHandler {
    @Bean(name = "masterTransaction")
    public DataSourceTransactionManager masterTransaction(
            @Qualifier("masterDataSource") DataSource dataSource
    ) {
        return new DataSourceTransactionManager(dataSource);
    }

    @Bean(name = "historyTransaction")
    public DataSourceTransactionManager historyTransaction(
            @Qualifier("historyDataSource") DataSource dataSource
    ) {
        return new DataSourceTransactionManager(dataSource);
    }
}
```

指定使用那个数据源的事务

```text
@Transactional(transactionManager = "masterTransaction")
public void remove(Long id) {}
```

# 启动类

```text
@SpringBootApplication(
        exclude = {DataSourceAutoConfiguration.class, MybatisPlusAutoConfiguration.class}
)
```

启动类上排查，自动装配，使用我们自定义的多数据源！！！

# 演示

![](./images/images/img_003_6b37bb7224ee.gif)

![](./images/images/img_004_a3f2898127bb.gif)

　　多个数据源，同时也是支持事务的
