{

  "title": "mybatis 逆行工程 附源码",
  "date": "2020-05-20",
  "description": "导读 逆向工程说白了，就可以简化开发工作量，自动生成一些死板的东西，比如POJO、映射文件等等，然后在将代码拷贝至实际工程，直接拿来用！ 项目结构 GeneratorSqlMap.java log4j.properties generatorConfig.xml 数据库表 测试 项目下载",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12923277.html"

}

# 导读

　　逆向工程说白了，就可以简化开发工作量，自动生成一些死板的东西，比如POJO、映射文件等等，然后在将代码拷贝至实际工程，直接拿来用！

## 项目结构

![](./images/images/img_001_4e619c882768.png)

### GeneratorSqlMap.java

```text
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import org.mybatis.generator.api.MyBatisGenerator;
import org.mybatis.generator.config.Configuration;
import org.mybatis.generator.config.xml.ConfigurationParser;
import org.mybatis.generator.internal.DefaultShellCallback;

public class GeneratorSqlmap {

    public void generator() throws Exception{

        List<String> warnings = new ArrayList<String>();
        boolean overwrite = true;
        //指定 逆向工程配置文件
        File configFile = new File("generatorConfig.xml");
        ConfigurationParser cp = new ConfigurationParser(warnings);
        Configuration config = cp.parseConfiguration(configFile);
        DefaultShellCallback callback = new DefaultShellCallback(overwrite);
        MyBatisGenerator myBatisGenerator = new MyBatisGenerator(config,
                callback, warnings);
        myBatisGenerator.generate(null);

    }
    public static void main(String[] args) throws Exception {
        try {
            GeneratorSqlmap generatorSqlmap = new GeneratorSqlmap();
            generatorSqlmap.generator();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### log4j.properties

```text
log4j.rootLogger=DEBUG, Console
#Console
log4j.appender.Console=org.apache.log4j.ConsoleAppender
log4j.appender.Console.layout=org.apache.log4j.PatternLayout
log4j.appender.Console.layout.ConversionPattern=%d [%t] %-5p [%c] - %m%n
log4j.logger.java.sql.ResultSet=INFO
log4j.logger.org.apache=INFO
log4j.logger.java.sql.Connection=DEBUG
log4j.logger.java.sql.Statement=DEBUG
log4j.logger.java.sql.PreparedStatement=DEBUG
```

### generatorConfig.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE generatorConfiguration
        PUBLIC "-//mybatis.org//DTD MyBatis Generator Configuration 1.0//EN"
        "http://mybatis.org/dtd/mybatis-generator-config_1_0.dtd">
<generatorConfiguration>
    <!--数据驱动器-->
    <classPathEntry  location="lib/mysql-connector-java-5.1.28-bin.jar"/>
    <context id="DB2Tables"  targetRuntime="MyBatis3">
        <commentGenerator>
            <property name="suppressDate" value="true"/>
            <!-- 是否自动生成注释-->
            <property name="suppressAllComments" value="true"/>
        </commentGenerator>
        <!-- 数据库连接url，用户名，密码 -->
        <jdbcConnection driverClass="com.mysql.jdbc.Driver" connectionURL="jdbc:mysql://127.0.0.1:3306/cyb" userId="root" password="root">
        </jdbcConnection>
        <javaTypeResolver>
            <property name="forceBigDecimals" value="false"/>
        </javaTypeResolver>
        <!-- 生成模型的包名和位置-->
        <javaModelGenerator targetPackage="com.cyb.po" targetProject="src">
            <property name="enableSubPackages" value="true"/>
            <property name="trimStrings" value="true"/>
        </javaModelGenerator>
        <!-- 生成映射文件的包名和位置-->
        <sqlMapGenerator targetPackage="com.cyb.mapping" targetProject="src">
            <property name="enableSubPackages" value="true"/>
        </sqlMapGenerator>
        <!-- 生成DAO的包名和位置-->
        <javaClientGenerator type="XMLMAPPER" targetPackage="com.cyb.dao" targetProject="src">
            <property name="enableSubPackages" value="true"/>
        </javaClientGenerator>
        <!-- 要生成哪些表-->
        <table tableName="dept"></table>
    </context>
</generatorConfiguration>
```

### 数据库表

![](./images/images/img_002_4e38e18df16e.png)

## 测试

![](./images/images/img_003_1a4eb583d7f9.gif)

## 项目下载

```text
链接: https://pan.baidu.com/s/1BCGAzCTpqBlkQjzA8pYUYA  密码: o5gw
```
