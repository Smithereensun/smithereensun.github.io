{

  "title": "Spring Boot整合ElasticSearch和Mysql 附案例源码",
  "date": "2020-08-12",
  "description": "导读 前二天，写了一篇ElasticSearch7.8.1从入门到精通的（点我直达），但是还没有整合到SpringBoot中，下面演示将ElasticSearch和mysql整合到Spring Boot中，附演示源码。 项目介绍 模仿NBA网站 网址地址：点我直达 接口开发 将数据库数据导入到Ela",
  "tags": [
    "Spring",
    "MySQL"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13473132.html"

}

# 导读

　　前二天，写了一篇ElasticSearch7.8.1从入门到精通的（[点我直达](https://www.cnblogs.com/chenyanbin/p/13419497.html)），但是还没有整合到SpringBoot中，下面演示将ElasticSearch和mysql整合到Spring Boot中，附演示源码。

# 项目介绍

## 模仿NBA网站

网址地址：[点我直达](https://china.nba.com/playerindex/)

![](./images/images/img_001_600b1582115e.png)

## 接口开发

1. 将数据库数据导入到ElasticSearch
2. 通过姓名查找球员
3. 通过国家或者球队查询球员
4. 通过姓名字母查找球员

# 项目搭建

## SpringBoot整合ElasticSearch和Mysql

![](./images/images/img_002_1a2eb57907ff.png)

![](./images/images/img_003_898209fbd30c.png)

![](./images/images/img_004_d0b0a7bf39e1.png)

## 数据库数据

　　将百度云盘里的sql，在mysql上运行即可

```text
链接: https://pan.baidu.com/s/1MJaJy8isfVnPha00tlS8_w  密码: u3dg
```

## 项目结构

![](./images/images/img_005_a25bc2f5e75a.png)

### pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.3.2.RELEASE</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.cyb</groupId>
    <artifactId>yb_search</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>yb_search</name>
    <description>Demo project for Spring Boot</description>

    <properties>
        <java.version>1.8</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <!--ElasticSearch相关开始-->
        <dependency>
            <groupId>org.elasticsearch.client</groupId>
            <artifactId>elasticsearch-rest-high-level-client</artifactId>
            <version>7.8.1</version>
        </dependency>
        <dependency>
            <groupId>org.elasticsearch</groupId>
            <artifactId>elasticsearch</artifactId>
            <version>7.8.1</version>
        </dependency>
        <!--ElasticSearch相关结束-->
        <!--fastjson相关开始-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.73</version>
        </dependency>
        <!--fastjson相关结束-->
        <!--druid相关开始-->
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>druid</artifactId>
            <version>1.1.23</version>
        </dependency>
        <!--druid相关结束-->
        <!--mybatis与springboot兼容包相关开始-->
        <dependency>
            <groupId>org.mybatis.spring.boot</groupId>
            <artifactId>mybatis-spring-boot-starter</artifactId>
            <version>2.1.3</version>
        </dependency>
        <!--mybatis与springboot兼容包相关结束-->
        <!--mysql相关开始-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.21</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.21</version>
        </dependency>

        <!--mysql相关结束-->
        <!--commons-lang3相关开始-->
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-lang3</artifactId>
            <version>3.11</version>
        </dependency>
        <!--commons-lang3相关结束-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
<!--            <exclusions>-->
<!--                <exclusion>-->
<!--                    <groupId>org.junit.vintage</groupId>-->
<!--                    <artifactId>junit-vintage-engine</artifactId>-->
<!--                </exclusion>-->
<!--            </exclusions>-->
        </dependency>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

#### 注意

**我本地安装的ElasticSearch版本是7.8.1，引入pom的ES依赖的话，最好版本一致，否则可能出现版本兼容问题！！！！！！！！！！！**

### application.properties

```text
# 端口号
server.port=8083
# 数据库配置
spring.datasource.url=jdbc:mysql://localhost:3306/nba?useUnicode=true&characterEncoding=UTF-8&serverTimezone=Asia/Shanghai
spring.datasource.username=root
spring.datasource.password=root
# 连接池
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
# 表明使用Druid连接池
spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
#初始化时建立物理连接的个数。
spring.datasource.druid.initial-size=5
#最大连接池数量
spring.datasource.druid.max-active=20
#最小连接池数量
spring.datasource.druid.min-idle=5
#获取连接时最大等待时间，单位毫秒
spring.datasource.druid.max-wait=3000
#是否缓存preparedStatement，也就是PSCache,PSCache对支持游标的数据库性能提升巨大，比如说oracle,在mysql下建议关闭。
spring.datasource.druid.pool-prepared-statements=false
#要启用PSCache，必须配置大于0，当大于0时，poolPreparedStatements自动触发修改为true。在Druid中，不会存在Oracle下PSCache占用内存过多的问题，可以把这个数值配置大一些，比如说100
spring.datasource.druid.max-open-prepared-statements= -1
#配置检测可以关闭的空闲连接间隔时间
spring.datasource.druid.time-between-eviction-runs-millis=60000
# 配置连接在池中的最小生存时间
spring.datasource.druid.min-evictable-idle-time-millis= 300000
spring.datasource.druid.max-evictable-idle-time-millis= 400000
# 日志相关
logging.level.root: info
logging.level.com.cyb.search: debug
# ElasticSearch配置
elasticsearch.host:192.168.199.170
elasticsearch.port=9200
```

### EsConfig.java(ES配置类)

```text
package com.cyb.search.config;

import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

/**
 * @ClassName：EsConfig
 * @Description：ES配置文件
 * @Author：chenyb
 * @Date：2020/8/10 11:25 下午
 * @Versiion：1.0
 */
@Configuration
//获取application.properties或application.yml获取里面的参数值
@ConfigurationProperties(prefix = "elasticsearch")
public class EsConfig {
    private String host;
    private Integer port;
    //初始化RestHighLevelClient
    @Bean(destroyMethod = "close")
    public RestHighLevelClient client(){
        return new RestHighLevelClient(RestClient.builder(
                new HttpHost(host,port,"http")
        ));
    }

    public String getHost() {
        return host;
    }

    public void setHost(String host) {
        this.host = host;
    }

    public Integer getPort() {
        return port;
    }

    public void setPort(Integer port) {
        this.port = port;
    }
}
```

### NBAPlayerDao.java

```text
package com.cyb.search.dao;

import com.cyb.search.model.NBAPlayer;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

@Mapper
public interface NBAPlayerDao {
    @Select("select * from nba_player")
    List<NBAPlayer> selectAll();
}
```

### NBAPlayer.java(实体类)

```text
package com.cyb.search.model;

/**
 * @ClassName：NBAPlayer
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/8/10 11:39 下午
 * @Versiion：1.0
 */
public class NBAPlayer {
    private Integer id;
    private String countryEn;
    private String country;
    private String code;
    private String displayAffiliation;
    private String displayName;
    private Integer draft;
    private String schoolType;
    private String weight;
    private Integer playYear;
    private String jerseyNo;
    private Long birthDay;
    private String birthDayStr;
    private String displayNameEn;
    private String position;
    private Double heightValue;
    private String playerId;
    private String teamCity;
    private String teamCityEn;
    private String teamName;
    private String teamNameEn;
    private String teamConference;
    private String teamConferenceEn;
    private Integer age;
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String getBirthDayStr() {
        return birthDayStr;
    }

    public void setBirthDayStr(String birthDayStr) {
        this.birthDayStr = birthDayStr;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getDisplayAffiliation() {
        return displayAffiliation;
    }

    public void setDisplayAffiliation(String displayAffiliation) {
        this.displayAffiliation = displayAffiliation;
    }

    public String getDisplayName() {
        return displayName;
    }

    public void setDisplayName(String displayName) {
        this.displayName = displayName;
    }

    public Integer getDraft() {
        return draft;
    }

    public void setDraft(Integer draft) {
        this.draft = draft;
    }

    public String getSchoolType() {
        return schoolType;
    }

    public void setSchoolType(String schoolType) {
        this.schoolType = schoolType;
    }

    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }

    public Integer getPlayYear() {
        return playYear;
    }

    public void setPlayYear(Integer playYear) {
        this.playYear = playYear;
    }

    public String getCountryEn() {
        return countryEn;
    }

    public void setCountryEn(String countryEn) {
        this.countryEn = countryEn;
    }

    public String getTeamCityEn() {
        return teamCityEn;
    }

    public void setTeamCityEn(String teamCityEn) {
        this.teamCityEn = teamCityEn;
    }

    public String getTeamNameEn() {
        return teamNameEn;
    }

    public void setTeamNameEn(String teamNameEn) {
        this.teamNameEn = teamNameEn;
    }

    public String getTeamConference() {
        return teamConference;
    }

    public void setTeamConference(String teamConference) {
        this.teamConference = teamConference;
    }

    public String getTeamConferenceEn() {
        return teamConferenceEn;
    }

    public void setTeamConferenceEn(String teamConferenceEn) {
        this.teamConferenceEn = teamConferenceEn;
    }

    public String getJerseyNo() {
        return jerseyNo;
    }

    public void setJerseyNo(String jerseyNo) {
        this.jerseyNo = jerseyNo;
    }

    public Long getBirthDay() {
        return birthDay;
    }

    public void setBirthDay(Long birthDay) {
        this.birthDay = birthDay;
    }

    public String getDisplayNameEn() {
        return displayNameEn;
    }

    public void setDisplayNameEn(String displayNameEn) {
        this.displayNameEn = displayNameEn;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public Double getHeightValue() {
        return heightValue;
    }

    public void setHeightValue(Double heightValue) {
        this.heightValue = heightValue;
    }

    public String getPlayerId() {
        return playerId;
    }

    public void setPlayerId(String playerId) {
        this.playerId = playerId;
    }

    public String getTeamCity() {
        return teamCity;
    }

    public void setTeamCity(String teamCity) {
        this.teamCity = teamCity;
    }

    public String getTeamName() {
        return teamName;
    }

    public void setTeamName(String teamName) {
        this.teamName = teamName;
    }

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }
}
```

### NBAPlayerService.java(接口)

```text
package com.cyb.search.service;

import com.cyb.search.model.NBAPlayer;

import java.io.IOException;

public interface NBAPlayerService {
    boolean addPlayer(NBAPlayer player,String id) throws IOException;
}
```

#### NBAPlayerServiceImpl.java

```text
package com.cyb.search.service.impl;

import com.alibaba.fastjson.JSONObject;
import com.cyb.search.model.NBAPlayer;
import com.cyb.search.service.NBAPlayerService;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.cglib.beans.BeanMap;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

/**
 * @ClassName：NBAPlayerServiceImpl
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/8/11 10:09 下午
 * @Versiion：1.0
 */
@Service
public class NBAPlayerServiceImpl implements NBAPlayerService {
    @Resource
    private RestHighLevelClient client;

    /**
     * 添加
     * @param player 实体类
     * @param id 编号
     * @return
     * @throws IOException
     */
    @Override
    public boolean addPlayer(NBAPlayer player, String id) throws IOException {
        IndexRequest request=new IndexRequest("nba_latest").id(id).source(beanToMap(player));
        IndexResponse response = client.index(request, RequestOptions.DEFAULT);
        System.out.println(JSONObject.toJSON(response));
        return false;
    }

    /**
     * 对象转map
     * @param bean
     * @param <T>
     * @return
     */
    public static <T> Map<String,Object> beanToMap(T bean){
        Map<String,Object> map=new HashMap<>();
        if (bean!=null){
            BeanMap beanMap=BeanMap.create(bean);
            for(Object key:beanMap.keySet()){
                if (beanMap.get(key)!=null){
                    map.put(key+"",beanMap.get(key));
                }
            }
        }
        return map;
    }
}
```

## 基础功能实现

### 往ES中插入一条数据

![](./images/images/img_006_fa862f5839b9.png)

![](./images/images/img_007_811fcb3223f8.png)

### 查看数据库数据

![](./images/images/img_008_d5372ae06e2e.png)

![](./images/images/img_009_b64e8521713d.png)

### 根据ID查ES 
![](./images/images/img_010_532e108bf760.png)

![](./images/images/img_011_05064766e033.png)

#### 单元测试

![](./images/images/img_012_21a9996d60cf.png)

### 修改

![](./images/images/img_013_8585d0501baf.png)

![](./images/images/img_014_52b43831c898.png)

#### 单元测试

![](./images/images/img_015_7955dd4d7aa8.gif)

### 删除

![](./images/images/img_016_e8670f6a5d4f.png)

![](./images/images/img_017_35d30fe4fb96.png)

#### 单元测试

![](./images/images/img_018_3b660bab10d2.png)

## 将数据库中的数据导入ES

![](./images/images/img_019_0648cb39d8be.png)

![](./images/images/img_020_2d00c7fcd470.png)
![](./images/images/img_021_a6a7789f8ab0.png)

## 通过名字查找球员

![](./images/images/img_022_908e08fd10d9.png)

![](./images/images/img_023_a7a4d91ded98.png)

![](./images/images/img_024_5fcd5af53d23.png)

### 测试

![](./images/images/img_025_52626c749b6d.png)

## 通过国家或球队查找球员

![](./images/images/img_026_2e2040c6c0d2.png)

![](./images/images/img_027_adbc5fe49cc7.png)

![](./images/images/img_028_10a2d0baeab2.png)

### 测试

![](./images/images/img_029_91670b83bf70.png)

![](./images/images/img_030_d6f94b97b2f8.png)

## 通过字母查球员

![](./images/images/img_031_e53127be544f.png)

![](./images/images/img_032_40ed34bee386.png)

### 测试

![](./images/images/img_033_2edf1ec7590c.png)

# 项目源码下载

```text
链接: https://pan.baidu.com/s/1QJ8wvjg7TPqGSP-68qpSIQ  密码: d26m
```

# SpringBoot整合ES优化通用工具类 二

## 依赖项

![](./images/images/img_034_8f900a89c634.gif)
![](./images/images/img_035_961ddebeb323.gif)

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>2.5.5</version>
        <relativePath/> <!-- lookup parent from repository -->
    </parent>
    <groupId>com.ybchen</groupId>
    <artifactId>ybchen-es</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>ybchen-es</name>
    <description>SpringBoot 整合ES</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>

        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
        </dependency>

        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-boot-starter</artifactId>
            <version>3.4.0</version>
        </dependency>

        <!-- 代码自动生成依赖 begin -->
        <dependency>
            <groupId>com.baomidou</groupId>
            <artifactId>mybatis-plus-generator</artifactId>
            <version>3.4.1</version>
        </dependency>
        <!-- velocity -->
        <dependency>
            <groupId>org.apache.velocity</groupId>
            <artifactId>velocity-engine-core</artifactId>
            <version>2.0</version>
        </dependency>
        <!-- 代码自动生成依赖 end-->

        <!--springBoot整合swagger3.0-->
        <dependency>
            <groupId>io.springfox</groupId>
            <artifactId>springfox-boot-starter</artifactId>
            <version>3.0.0</version>
        </dependency>

        <!--ElasticSearch相关开始-->
        <dependency>
            <groupId>org.elasticsearch.client</groupId>
            <artifactId>elasticsearch-rest-high-level-client</artifactId>
            <version>7.6.2</version>
        </dependency>
        <dependency>
            <groupId>org.elasticsearch</groupId>
            <artifactId>elasticsearch</artifactId>
            <version>7.6.2</version>
        </dependency>
        <!--ElasticSearch相关结束-->

        <dependency>
            <groupId>com.alibaba.fastjson2</groupId>
            <artifactId>fastjson2</artifactId>
            <version>2.0.18</version>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
                <configuration>
                    <excludes>
                        <exclude>
                            <groupId>org.projectlombok</groupId>
                            <artifactId>lombok</artifactId>
                        </exclude>
                    </excludes>
                </configuration>
            </plugin>
        </plugins>
    </build>

</project>
```

pom.xml

## 配置文件

```text
spring.application.name=es-service
# ===== 自定义swagger配置 ===== #
swagger.enable=true
swagger.application-name= ${spring.application.name}
swagger.application-version=1.0
swagger.application-description=es api
#mysql
spring.datasource.url=jdbc:mysql://localhost:3306/nba?useUnicode=true&characterEncoding=utf8
spring.datasource.username=root
spring.datasource.password=rootroot
spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
#mybatis-plus配置控制台打印完整带参数SQL语句
mybatis-plus.configuration.log-impl=org.apache.ibatis.logging.stdout.StdOutImpl
# ElasticSearch配置
elasticsearch.host=47.116.143.16
elasticsearch.port=9200
elasticsearch.userName=es
elasticsearch.password=es
```

## ES客户端

![](./images/images/img_034_8f900a89c634.gif)
![](./images/images/img_035_961ddebeb323.gif)

```text
package com.ybchen.service;

import lombok.extern.slf4j.Slf4j;
import org.apache.http.HttpHost;
import org.apache.http.auth.AuthScope;
import org.apache.http.auth.UsernamePasswordCredentials;
import org.apache.http.client.CredentialsProvider;
import org.apache.http.impl.client.BasicCredentialsProvider;
import org.apache.http.impl.nio.reactor.IOReactorConfig;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestClientBuilder;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;

/**
 * es 客户端
 * @author: chenyanbin 2022-11-06 14:08
 */
@Service
@Slf4j
public class EsService {
    @Value("${elasticsearch.host}")
    String esHosts;
    @Value("${elasticsearch.port}")
    int esPort;
    @Value("${elasticsearch.userName}")
    String esUserName;
    @Value("${elasticsearch.password}")
    String esPassword;

    private static volatile RestHighLevelClient instance;

    /**
     * 获取es客户端
     *
     * @return
     */
    public RestHighLevelClient getInstance() {
        if (instance == null) {
            synchronized (EsService.class) {
                if (instance == null) {
                    instance = createInstance();
                }
            }
        }
        return instance;
    }

    /**
     * 创建es客户端
     *
     * @return
     */
    private RestHighLevelClient createInstance() {
        List<HttpHost> httpHostsList = new ArrayList<>();
        //填充es数据
        httpHostsList.add(new HttpHost(esHosts, esPort));
        //es客户端构建者
        RestClientBuilder clientBuilder = RestClient.builder(httpHostsList.get(0));
        //异步链接延时配置
        clientBuilder.setRequestConfigCallback(requestConfigBuilder ->
                requestConfigBuilder
                        .setConnectTimeout(5000) //5秒
                        .setSocketTimeout(5000)
                        .setConnectionRequestTimeout(5000)
        );
        //异步链接数配置
        clientBuilder.setHttpClientConfigCallback(httpClientBuilder -> {
            //最大连接数100个
            httpClientBuilder.setMaxConnTotal(100);
            //最大路由连接数
            httpClientBuilder.setMaxConnPerRoute(100);
            //==================ES有账号密码-开始======================
            final CredentialsProvider credentialsProvider = new BasicCredentialsProvider();
            credentialsProvider.setCredentials(AuthScope.ANY, new UsernamePasswordCredentials(esUserName, esPassword));
            httpClientBuilder.setDefaultCredentialsProvider(credentialsProvider);
            //==================ES有账号密码-结束======================
            // 设置KeepAlive为5分钟的时间，不设置默认为-1，也就是持续连接，然而这会受到外界的影响比如Firewall，会将TCP连接单方面断开，从而会导致Connection reset by peer的报错
            // 参考github解决方案：https://github.com/TFdream/Elasticsearch-learning/issues/30
            httpClientBuilder.setKeepAliveStrategy((response, context) -> TimeUnit.MINUTES.toMillis(3))
                    .setDefaultIOReactorConfig(IOReactorConfig.custom().setIoThreadCount(1).setSoKeepAlive(true).build());
            return httpClientBuilder;
        });
        return new RestHighLevelClient(clientBuilder);
    }

    /**
     * 30秒一次检查es状态
     */
    @Scheduled(fixedRate = 30 * 1000)
    public void heartbeatToES() {
        try {
            RequestOptions requestOptions = RequestOptions.DEFAULT.toBuilder().build();
            boolean result = getInstance().ping(requestOptions);
            log.info("检查ES状态:{}", result);
        } catch (Exception e) {
            log.error("检查ES状态发生异常：{}", e);
        }
    }
}
```

EsService.java

## 工具类

![](./images/images/img_034_8f900a89c634.gif)
![](./images/images/img_035_961ddebeb323.gif)

```text
package com.ybchen.service;

import com.ybchen.model.NbaPlayerDO;
import com.ybchen.vo.EsDocumentVo;

import java.util.List;
import java.util.Map;

public interface NbaService {
    /**
     * 添加文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @param jsonBody  json数据
     * @return
     */
    boolean addDoc(
            String indexName,
            String docId,
            String jsonBody
    );

    /**
     * 异步添加文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @param jsonBody  json数据
     * @return
     */
    boolean asyncAddDoc(
            String indexName,
            String docId,
            String jsonBody
    );

    /**
     * 批量添加文档
     *
     * @param indexName      索引名称
     * @param documentVoList 文档对象集合
     * @return
     */
    boolean batchAddDoc(
            String indexName,
            List<EsDocumentVo> documentVoList
    );

    /**
     * 批量异步添加文档
     *
     * @param indexName      索引名称
     * @param documentVoList 文档对象集合
     * @return
     */
    boolean batchAsyncAddDoc(
            String indexName,
            List<EsDocumentVo> documentVoList
    );

    /**
     * 根据文档id搜索文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @return
     */
    Map<String, Object> getDocumentByDocId(
            String indexName,
            String docId
    );

    /**
     * 根据文档id更新文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @param jsonBody  json数据
     * @return
     */
    boolean updateDocumentByDocId(
            String indexName,
            String docId,
            String jsonBody
    );

    /**
     * 批量异步根据文档id更新文档
     *
     * @param indexName      索引名称
     * @param documentVoList 文档对象集合
     * @return
     */
    boolean batchAsyncUpdateDocumentByDocId(
            String indexName,
            List<EsDocumentVo> documentVoList
    );

    /**
     * 根据文档id删除文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @return
     */
    boolean deleteDocumentByDocId(
            String indexName,
            String docId
    );

    /**
     * 根据索引名称全部删除文档
     *
     * @param indexName 索引名称
     * @return
     */
    boolean deleteAllDocumentByIndexName(
            String indexName
    );

    /**
     * 通过名字查找球员
     *
     * @param indexName      索引名称
     * @param key            文档字段
     * @param value          文档值
     * @param pageNum        第几页
     * @param pageSize       一页多少条
     * @param highlightField 高亮字段
     * @return
     */
    List<NbaPlayerDO> searchMatch(
            String indexName,
            String key,
            String value,
            int pageNum,
            int pageSize,
            String highlightField
    );
}
```

NbaService.java

![](./images/images/img_034_8f900a89c634.gif)
![](./images/images/img_035_961ddebeb323.gif)

```text
package com.ybchen.service.impl;

import com.alibaba.fastjson2.JSON;
import com.ybchen.model.NbaPlayerDO;
import com.ybchen.service.EsService;
import com.ybchen.service.NbaService;
import com.ybchen.vo.EsDocumentVo;
import lombok.extern.slf4j.Slf4j;
import org.elasticsearch.action.ActionListener;
import org.elasticsearch.action.admin.indices.delete.DeleteIndexRequest;
import org.elasticsearch.action.bulk.BulkRequest;
import org.elasticsearch.action.bulk.BulkResponse;
import org.elasticsearch.action.delete.DeleteRequest;
import org.elasticsearch.action.get.GetRequest;
import org.elasticsearch.action.get.GetResponse;
import org.elasticsearch.action.index.IndexRequest;
import org.elasticsearch.action.index.IndexResponse;
import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.action.update.UpdateRequest;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.common.text.Text;
import org.elasticsearch.common.xcontent.XContentType;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.SearchHit;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.elasticsearch.search.fetch.subphase.highlight.HighlightBuilder;
import org.elasticsearch.search.fetch.subphase.highlight.HighlightField;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * @author: chenyanbin 2022-11-06 14:36
 */
@Service
@Slf4j
public class NbaServiceImpl implements NbaService {
    @Autowired
    EsService esService;

    /**
     * 添加文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @param jsonBody  json数据
     * @return
     */
    @Override
    public boolean addDoc(
            String indexName,
            String docId,
            String jsonBody
    ) {
        IndexRequest indexRequest = new IndexRequest();
        //添加索引名称
        indexRequest.index(indexName);
        //文档id
        indexRequest.id(docId);
        //json数据
        indexRequest.source(jsonBody, XContentType.JSON);
        try {
            //添加文档
            esService.getInstance().index(
                    indexRequest,
                    RequestOptions.DEFAULT
            );
            log.info("添加文档成功，indexName：{}，docId：{}，jsonBody：{}",
                    indexName,
                    docId,
                    jsonBody
            );
            return true;
        } catch (Exception e) {
            log.error("添加文档失败，indexName：{}，docId：{}，jsonBody：{}，异常信息：{}",
                    indexName,
                    docId,
                    jsonBody,
                    e
            );
        }
        return false;
    }

    /**
     * 异步添加文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @param jsonBody  json数据
     * @return
     */
    @Override
    public boolean asyncAddDoc(
            String indexName,
            String docId,
            String jsonBody
    ) {
        IndexRequest indexRequest = new IndexRequest();
        //添加索引名称
        indexRequest.index(indexName);
        //文档id
        indexRequest.id(docId);
        //json数据
        indexRequest.source(jsonBody, XContentType.JSON);
        //异步批量插入
        esService.getInstance().indexAsync(
                indexRequest,
                RequestOptions.DEFAULT,
                new ActionListener<IndexResponse>() {
                    @Override
                    public void onResponse(IndexResponse indexResponse) {
                        log.info("异步添加文档成功，indexName：{}，docId：{}，jsonBody：{}",
                                indexName,
                                docId,
                                jsonBody
                        );
                    }

                    @Override
                    public void onFailure(Exception e) {
                        log.error("异步添加文档失败，indexName：{}，docId：{}，jsonBody：{}，异常信息：{}",
                                indexName,
                                docId,
                                jsonBody,
                                e
                        );
                    }
                });
        return true;
    }

    /**
     * 批量添加文档
     *
     * @param indexName      索引名称
     * @param documentVoList 文档对象集合
     * @return
     */
    @Override
    public boolean batchAddDoc(
            String indexName,
            List<EsDocumentVo> documentVoList
    ) {
        if (documentVoList == null || documentVoList.size() == 0) {
            return false;
        }
        //批量文档请求对象
        BulkRequest bulkRequest = new BulkRequest();
        for (EsDocumentVo esDocumentVo : documentVoList) {
            IndexRequest indexRequest = new IndexRequest();
            //添加索引名称
            indexRequest.index(indexName);
            //文档id
            indexRequest.id(esDocumentVo.getDocId());
            //json数据
            indexRequest.source(esDocumentVo.getJsonBody(), XContentType.JSON);
            bulkRequest.add(indexRequest);
        }
        try {
            //批量添加
            esService.getInstance().bulk(bulkRequest, RequestOptions.DEFAULT);
            log.info("批量添加文档成功，indexName：{}，documentVoList：{}",
                    indexName,
                    documentVoList
            );
            return true;
        } catch (Exception e) {
            log.error("批量添加文档失败，indexName：{}，documentVoList：{}，异常信息：{}",
                    indexName,
                    documentVoList,
                    e
            );
        }
        return false;
    }

    /**
     * 批量异步添加文档
     *
     * @param indexName      索引名称
     * @param documentVoList 文档对象集合
     * @return
     */
    @Override
    public boolean batchAsyncAddDoc(
            String indexName,
            List<EsDocumentVo> documentVoList
    ) {
        if (documentVoList == null || documentVoList.size() == 0) {
            return false;
        }
        //批量文档请求对象
        BulkRequest bulkRequest = new BulkRequest();
        for (EsDocumentVo esDocumentVo : documentVoList) {
            IndexRequest indexRequest = new IndexRequest();
            //添加索引名称
            indexRequest.index(indexName);
            //文档id
            indexRequest.id(esDocumentVo.getDocId());
            //json数据
            indexRequest.source(esDocumentVo.getJsonBody(), XContentType.JSON);
            bulkRequest.add(indexRequest);
        }
        //批量添加
        esService.getInstance().bulkAsync(bulkRequest, RequestOptions.DEFAULT, new ActionListener<BulkResponse>() {
            @Override
            public void onResponse(BulkResponse bulkItemResponses) {
                log.info("批量异步添加文档成功，indexName：{}，documentVoList：{}",
                        indexName,
                        documentVoList
                );
            }

            @Override
            public void onFailure(Exception e) {
                log.info("批量异步添加文档失败，indexName：{}，documentVoList：{}，异常信息：{}",
                        indexName,
                        documentVoList,
                        e
                );
            }
        });
        return true;
    }

    /**
     * 根据文档id搜索文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @return
     */
    @Override
    public Map<String, Object> getDocumentByDocId(
            String indexName,
            String docId
    ) {
        GetRequest getRequest = new GetRequest();
        getRequest.index(indexName);
        getRequest.id(docId);
        try {
            //查询
            GetResponse response = esService.getInstance().get(getRequest, RequestOptions.DEFAULT);
            return response.getSource();
        } catch (Exception e) {
            log.error("根据文档id搜索文档失败，indexName：{}，docId：{}，异常信息：{}",
                    indexName,
                    docId,
                    e
            );
        }
        return null;
    }

    /**
     * 根据文档id更新文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @param jsonBody  json数据
     * @return
     */
    @Override
    public boolean updateDocumentByDocId(
            String indexName,
            String docId,
            String jsonBody
    ) {
        UpdateRequest updateRequest = new UpdateRequest();
        //添加索引名称
        updateRequest.index(indexName);
        //文档id
        updateRequest.id(docId);
        //json数据
        updateRequest.doc(jsonBody, XContentType.JSON);
        try {
            //更新文档
            esService.getInstance().update(updateRequest, RequestOptions.DEFAULT);
            log.error("根据文档id更新文档成功，indexName：{}，docId：{}，jsonBody：{}",
                    indexName,
                    docId,
                    jsonBody
            );
            return true;
        } catch (Exception e) {
            log.error("根据文档id更新文档失败，indexName：{}，docId：{}，jsonBody：{}，异常信息：{}",
                    indexName,
                    docId,
                    jsonBody,
                    e
            );
        }
        return false;
    }

    /**
     * 批量异步根据文档id更新文档
     *
     * @param indexName      索引名称
     * @param documentVoList 文档对象集合
     * @return
     */
    @Override
    public boolean batchAsyncUpdateDocumentByDocId(
            String indexName,
            List<EsDocumentVo> documentVoList
    ) {
        if (documentVoList == null || documentVoList.size() == 0) {
            return false;
        }
        BulkRequest bulkRequest = new BulkRequest();
        for (EsDocumentVo esDocumentVo : documentVoList) {
            UpdateRequest updateRequest = new UpdateRequest();
            //添加索引名称
            updateRequest.index(indexName);
            //文档id
            updateRequest.id(esDocumentVo.getDocId());
            //json数据
            updateRequest.doc(esDocumentVo.getJsonBody(), XContentType.JSON);
            bulkRequest.add(updateRequest);
        }
        esService.getInstance().bulkAsync(bulkRequest, RequestOptions.DEFAULT, new ActionListener<BulkResponse>() {
            @Override
            public void onResponse(BulkResponse bulkItemResponses) {
                log.info("批量异步根据文档id更新文档成功，indexName：{}，documentVoList：{}",
                        indexName,
                        documentVoList
                );
            }

            @Override
            public void onFailure(Exception e) {
                log.info("批量异步根据文档id更新文档失败，indexName：{}，documentVoList：{}，异常信息：{}",
                        indexName,
                        documentVoList,
                        e
                );
            }
        });
        return true;
    }

    /**
     * 根据文档id删除文档
     *
     * @param indexName 索引名称
     * @param docId     文档id
     * @return
     */
    @Override
    public boolean deleteDocumentByDocId(String indexName, String docId) {
        DeleteRequest deleteRequest = new DeleteRequest();
        //添加索引名称
        deleteRequest.index(indexName);
        //文档id
        deleteRequest.id(docId);
        try {
            esService.getInstance().delete(deleteRequest, RequestOptions.DEFAULT);
            log.error("根据文档id删除文档成功，indexName：{}，docId：{}",
                    indexName,
                    docId
            );
            return true;
        } catch (Exception e) {
            log.error("根据文档id删除文档失败，indexName：{}，docId：{}，异常信息：{}",
                    indexName,
                    docId,
                    e
            );
        }
        return false;
    }

    /**
     * 根据索引名称全部删除文档
     *
     * @param indexName 索引名称
     * @return
     */
    @Override
    public boolean deleteAllDocumentByIndexName(String indexName) {
        DeleteIndexRequest deleteIndexRequest = new DeleteIndexRequest();
        deleteIndexRequest.indices(indexName);
        try {
            esService.getInstance().indices().delete(deleteIndexRequest, RequestOptions.DEFAULT);
            log.error("根据索引名称全部删除文档成功，indexName：{}",
                    indexName
            );
            return true;
        } catch (Exception e) {
            log.error("根据索引名称全部删除文档失败，indexName：{}，异常信息：{}",
                    indexName,
                    e
            );
        }
        return false;
    }

    /**
     * 通过名字查找球员
     *
     * @param indexName      索引名称
     * @param key            文档字段
     * @param value          文档值
     * @param pageNum        第几页
     * @param pageSize       一页多少条
     * @param highlightField 高亮字段
     * @return
     */
    @Override
    public List<NbaPlayerDO> searchMatch(
            String indexName,
            String key,
            String value,
            int pageNum,
            int pageSize,
            String highlightField
    ) {
        //>>>>>>构建查找对象
        SearchRequest searchRequest = new SearchRequest();
        //添加索引名称
        searchRequest.indices(indexName);
        //>>>>>>>类似于查询语句，相当于：where后面的条件
        SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
        //构建查询条件 displayname：查询字段名称
        searchSourceBuilder.query(QueryBuilders.matchQuery(key, value));
        //从第0条开始
        searchSourceBuilder.from((pageNum - 1) * pageSize);
        //查1000条记录
        searchSourceBuilder.size(pageSize);
        //>>>>>>>>>设置高亮样式
        HighlightBuilder highlightBuilder = new HighlightBuilder();
        //设置高亮字段
        highlightBuilder.field(new HighlightBuilder.Field(highlightField));
        //高亮样式，前缀样式；后缀样式
        highlightBuilder.preTags("<span style=color:red>").postTags("</span>");
        searchSourceBuilder.highlighter(highlightBuilder);
        //>>>>>>将筛选条件添加到查找对象中
        searchRequest.source(searchSourceBuilder);
        try {
            SearchResponse response = esService.getInstance().search(searchRequest, RequestOptions.DEFAULT);
            //总共查询出来的数据总条数
            long total = response.getHits().getTotalHits().value;
            //本次数据查询条数
            int length = response.getHits().getHits().length;
            //拿到数据
            SearchHit[] hits = response.getHits().getHits();
            List<NbaPlayerDO> nbaPlayerDOList = new ArrayList<>();
            for (SearchHit hit : hits) {
                //单条记录
                Map<String, Object> sourceAsMap = hit.getSourceAsMap();
                //高亮字段
                Map<String, HighlightField> highlightFields = hit.getHighlightFields();
                HighlightField hField = highlightFields.get(highlightField);
                //>>>>>>>重新组装高亮字段和值
                if (hField != null) {
                    StringBuilder sbValue = new StringBuilder();
                    for (Text text : hField.fragments()) {
                        sbValue.append(text);
                    }
                    sourceAsMap.put(highlightField, sbValue.toString());
                }
                nbaPlayerDOList.add(JSON.parseObject(JSON.toJSONString(sourceAsMap), NbaPlayerDO.class));
            }
            return nbaPlayerDOList;
        } catch (Exception e) {
            log.error("搜索发生了异常：{}", e);
        }
        return new ArrayList<>();
    }

}
```

NbaServiceImpl.java

```text
package com.ybchen.vo;

import lombok.Data;

import java.io.Serializable;

/**
 * ES文档vo
 * @author: chenyanbin 2022-11-07 22:10
 */
@Data
public class EsDocumentVo implements Serializable {
    /**
     * 文档id
     */
    private String docId;

    /**
     * 文档数据
     */
    private String jsonBody;
}
```

## 实体类

![](./images/images/img_034_8f900a89c634.gif)
![](./images/images/img_035_961ddebeb323.gif)

```text
package com.ybchen.model;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import io.swagger.annotations.ApiModel;
import lombok.Data;
import lombok.EqualsAndHashCode;

import java.io.Serializable;
import java.math.BigDecimal;

/**
 * <p>
 *
 * </p>
 *
 * @author chenyanbin
 * @since 2022-11-06
 */
@Data
@EqualsAndHashCode(callSuper = false)
@TableName("nba_player")
@ApiModel(value = "NbaPlayerDO对象", description = "")
public class NbaPlayerDO implements Serializable {

    private static final long serialVersionUID = 1L;

    @TableId(value = "id", type = IdType.AUTO)
    private Integer id;

    @TableField("countryEn")
    private String countryen;

    @TableField("teamName")
    private String teamname;

    @TableField("birthDay")
    private Long birthday;

    private String country;

    @TableField("teamCityEn")
    private String teamcityen;

    private String code;

    @TableField("displayAffiliation")
    private String displayaffiliation;

    @TableField("displayName")
    private String displayname;

    @TableField("schoolType")
    private String schooltype;

    @TableField("teamConference")
    private String teamconference;

    @TableField("teamConferenceEn")
    private String teamconferenceen;

    private String weight;

    @TableField("teamCity")
    private String teamcity;

    @TableField("playYear")
    private Integer playyear;

    @TableField("jerseyNo")
    private String jerseyno;

    @TableField("teamNameEn")
    private String teamnameen;

    private Integer draft;

    @TableField("displayNameEn")
    private String displaynameen;

    @TableField("birthDayStr")
    private String birthdaystr;

    @TableField("heightValue")
    private BigDecimal heightvalue;

    private String position;

    private Integer age;

    @TableField("playerId")
    private String playerid;

}
```

NbaPlayerDO.java

## Mapper

```text
package com.ybchen.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.ybchen.model.NbaPlayerDO;

/**
 * <p>
 *  Mapper 接口
 * </p>
 *
 * @author chenyanbin
 * @since 2022-11-06
 */
public interface NbaPlayerMapper extends BaseMapper<NbaPlayerDO> {

}
```

## 单元测试

```text
package com.ybchen.service.impl;

import com.alibaba.fastjson2.JSON;
import com.ybchen.EsApplication;
import com.ybchen.mapper.NbaPlayerMapper;
import com.ybchen.model.NbaPlayerDO;
import com.ybchen.service.NbaService;
import com.ybchen.vo.EsDocumentVo;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

@SpringBootTest(classes = EsApplication.class)
class NbaServiceImplTest {
    @Autowired
    NbaService nbaService;
    @Autowired
    NbaPlayerMapper nbaPlayerMapper;

    private final String NBA_INDEX_NAME = "nba_player";

    /**
     * 添加文档
     */
    @Test
    public void addDoc() {
        NbaPlayerDO nbaPlayerDO = new NbaPlayerDO();
        nbaPlayerDO.setCountryen("中国");
        boolean flag = nbaService.addDoc(NBA_INDEX_NAME, "188", JSON.toJSONString(nbaPlayerDO));
        System.err.println(flag);
    }

    /**
     * 异步添加文档
     */
    @Test
    public void asyncAddDoc() {
        NbaPlayerDO nbaPlayerDO = new NbaPlayerDO();
        nbaPlayerDO.setCountryen("美国");
        boolean flag = nbaService.asyncAddDoc(NBA_INDEX_NAME, "191", JSON.toJSONString(nbaPlayerDO));
        System.err.println(flag);
        while (true) {

        }
    }

    /**
     * 批量添加文档
     */
    @Test
    public void batchAddDoc() {
        List<EsDocumentVo> list = new ArrayList<EsDocumentVo>() {
            {
                EsDocumentVo vo1 = new EsDocumentVo();
                vo1.setDocId("192");
                NbaPlayerDO nbaPlayerDO1 = new NbaPlayerDO();
                nbaPlayerDO1.setCountryen("中国");
                vo1.setJsonBody(JSON.toJSONString(nbaPlayerDO1));
                this.add(vo1);
                EsDocumentVo vo2 = new EsDocumentVo();
                vo1.setDocId("193");
                NbaPlayerDO nbaPlayerDO2 = new NbaPlayerDO();
                nbaPlayerDO2.setCountryen("俄罗斯");
                vo2.setJsonBody(JSON.toJSONString(nbaPlayerDO2));
                this.add(vo2);
            }
        };
        boolean flag = nbaService.batchAddDoc(NBA_INDEX_NAME, list);
        System.err.println(flag);
    }

    /**
     * 异步批量添加文档
     */
    @Test
    public void batchAsyncAddDoc() {
        List<EsDocumentVo> list = new ArrayList<EsDocumentVo>() {
            {
                EsDocumentVo vo1 = new EsDocumentVo();
                vo1.setDocId("194");
                NbaPlayerDO nbaPlayerDO1 = new NbaPlayerDO();
                nbaPlayerDO1.setCountryen("中国");
                vo1.setJsonBody(JSON.toJSONString(nbaPlayerDO1));
                this.add(vo1);
                EsDocumentVo vo2 = new EsDocumentVo();
                vo1.setDocId("195");
                NbaPlayerDO nbaPlayerDO2 = new NbaPlayerDO();
                nbaPlayerDO2.setCountryen("俄罗斯");
                vo2.setJsonBody(JSON.toJSONString(nbaPlayerDO2));
                this.add(vo2);
            }
        };
        boolean flag = nbaService.batchAsyncAddDoc(NBA_INDEX_NAME, list);
        System.err.println(flag);
        while (true) {

        }
    }

    /**
     * 根据文档id获取文档数据
     */
    @Test
    public void getDocumentByDocId() {
        Map<String, Object> documentByDocId = nbaService.getDocumentByDocId(NBA_INDEX_NAME, "188");
        System.out.println(JSON.toJSON(documentByDocId));
    }

    @Test
    public void updateDocumentByDocId() {
    }

    @Test
    public void batchAsyncUpdateDocumentByDocId() {
    }

    /**
     * 根据文档id删除文档
     */
    @Test
    void deleteDocumentByDocId() {
        boolean flag = nbaService.deleteDocumentByDocId(NBA_INDEX_NAME, "188");
        System.out.println(flag);
    }

    /**
     * 根据索引名称删除所有文档
     */
    @Test
    void deleteAllDocumentByIndexName() {
        boolean flag = nbaService.deleteAllDocumentByIndexName(NBA_INDEX_NAME);
        System.out.println(flag);
    }

    /**
     * 导入所有球员数据到es
     */
    @Test
    public void importAll() {
        List<NbaPlayerDO> nbaPlayerDOList = nbaPlayerMapper.selectList(null);
        List<EsDocumentVo> documentVoList = new ArrayList<>(nbaPlayerDOList.size());
        for (NbaPlayerDO playerDO : nbaPlayerDOList) {
            EsDocumentVo vo = new EsDocumentVo();
            vo.setDocId(playerDO.getId().toString());
            vo.setJsonBody(JSON.toJSONString(playerDO));
            documentVoList.add(vo);
        }
        boolean flag = nbaService.batchAsyncAddDoc(NBA_INDEX_NAME, documentVoList);
        System.err.println(flag);
        while (true) {

        }
    }

    /**
     * 根据名称查找球员
     */
    @Test
    public void searchMatch() {
        List<NbaPlayerDO> nbaPlayerDOList = nbaService.searchMatch(
                NBA_INDEX_NAME,
                "displaynameen",
                "james",
                1,
                1000,
                "displaynameen"
        );
        System.err.println(JSON.toJSON(nbaPlayerDOList));
    }
}
```

## 源码下载

```text
链接: https://pan.baidu.com/s/1NpwqP3YCjLm5nLFKDZFzUQ?pwd=ubiv 提取码: ubiv
```
