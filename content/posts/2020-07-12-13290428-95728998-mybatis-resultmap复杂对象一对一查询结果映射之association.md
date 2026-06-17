{

  "title": "Mybatis ResultMap复杂对象一对一查询结果映射之association",
  "date": "2020-07-12",
  "description": "Mybatis复杂对象映射配置ResultMap的association association：映射到POJO的某个复杂类型属性，比如订单order对象里面包含user对象 表结构 项目结构 pom.xml mybatis-config-xml db.properties VideoOrderMa",
  "tags": [
    "MyBatis"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13290428.html"

}

# Mybatis复杂对象映射配置ResultMap的association

- association：映射到POJO的某个复杂类型属性，比如订单order对象里面包含user对象

## 表结构

![](/imported/posts/2020-07-12-13290428-95728998-mybatis-resultmap复杂对象一对一查询结果映射之association/images/img_001_c3da78431d6f.png)

![](/imported/posts/2020-07-12-13290428-95728998-mybatis-resultmap复杂对象一对一查询结果映射之association/images/img_002_bf0a3a665c61.png)

## 项目结构

![](/imported/posts/2020-07-12-13290428-95728998-mybatis-resultmap复杂对象一对一查询结果映射之association/images/img_003_6b29f71d1ef4.png)

## pom.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>net.cyb</groupId>
    <artifactId>cyb-mybatis</artifactId>
    <version>1.0-SNAPSHOT</version>
    <dependencies>
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.4</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.20</version>
        </dependency>
        <dependency>
            <groupId>org.slf4j</groupId>
            <artifactId>slf4j-log4j12</artifactId>
            <version>1.7.30</version>
        </dependency>
    </dependencies>
</project>
```

## mybatis-config-xml

```text
<!DOCTYPE configuration
        PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-config.dtd">
<configuration>
    <!-- 引入外部配置文件 -->
    <properties resource="config/db.properties"></properties>
    <!--下划线自动映射驼峰字段-->
<!--    <settings>-->
<!--        <setting name="mapUnderscoreToCamelCase" value="true"/>-->
<!--    </settings>-->
    <!-- 数据库链接相关 -->
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC" />
            <dataSource type="POOLED">
                <property name="driver" value="${db.driver}" />
                <property name="url" value="${db.url}" />
                <property name="username" value="${db.username}" />
                <property name="password" value="${db.password}" />
            </dataSource>
        </environment>
    </environments>
    <mappers>
        <!-- 添加映射文件 -->
        <mapper resource="mapper/VideoMapper.xml" />
        <mapper resource="mapper/VideoOrderMapper.xml" />
    </mappers>
</configuration>
```

### db.properties

```text
db.driver=com.mysql.cj.jdbc.Driver
db.url=jdbc:mysql://127.0.0.1:3306/cybclass
db.username=root
db.password=root
```

## VideoOrderMapper.xml

```text
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
        PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<!--
namespace：名称空间，一般需要保持全局唯一，最好是和dao层的java接口一致。可以映射sql语句到对应的方法名称和参数、返回类型
-->
<mapper namespace="net.cybclass.online.dao.VideoOrderMapper">
    <resultMap id="VideoOrderResultMap" type="net.cybclass.online.domain.VideoOrder">
        <id column="id" property="id"></id>
        <result column="user_id" property="user_id"></result>
        <result column="out_trade_no" property="out_trade_no"></result>
        <result column="create_time" property="create_time"></result>
        <result column="state" property="state"></result>
        <result column="total_fee" property="total_fee"></result>
        <result column="video_id" property="video_id"></result>
        <result column="video_title" property="video_title"></result>
        <result column="video_img" property="video_img"></result>
        <!--
        配置属性一对一
        property：对应VideoOrder里面的user属性名
        javaType：这个属性的类型
        -->
        <association property="user" javaType="net.cybclass.online.domain.User">
            <id column="user_id" property="id"></id>
            <result column="name" property="name"></result>
            <result column="pwd" property="pwd"></result>
            <result column="phone" property="phone"></result>
            <result column="head_img" property="head_img"></result>
            <result column="create_time_u" property="create_time"></result>
        </association>
    </resultMap>
    <!--一对一关联查询订单，订单内容包含用户属性-->
    <select id="queryVideoOrderList" resultMap="VideoOrderResultMap">
        select
            v.id,
            v.out_trade_no,
            v.create_time,
            v.state,
            v.total_fee,
            v.video_id,
            v.video_title,
            v.user_id,
            v.video_img,
            u.name,
            u.pwd,
            u.phone,
            u.head_img,
            u.create_time create_time_u
        from video_order v left join user u on v.user_id=u.id
    </select>
</mapper>
```

## VideoOrder.java

```text
package net.cybclass.online.domain;

import java.util.Date;

public class VideoOrder {
    private int id;
    private String out_trade_no;
    private int state;
    private int total_fee;
    private int video_id;
    private String video_title;
    private String video_img;
    private int user_id;
    private Date create_time;
    private User user;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getOut_trade_no() {
        return out_trade_no;
    }

    public void setOut_trade_no(String out_trade_no) {
        this.out_trade_no = out_trade_no;
    }

    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }

    public int getTotal_fee() {
        return total_fee;
    }

    public void setTotal_fee(int total_fee) {
        this.total_fee = total_fee;
    }

    public int getVideo_id() {
        return video_id;
    }

    public void setVideo_id(int video_id) {
        this.video_id = video_id;
    }

    public String getVideo_title() {
        return video_title;
    }

    public void setVideo_title(String video_title) {
        this.video_title = video_title;
    }

    public String getVideo_img() {
        return video_img;
    }

    public void setVideo_img(String video_img) {
        this.video_img = video_img;
    }

    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }

    public Date getCreate_time() {
        return create_time;
    }

    public void setCreate_time(Date create_time) {
        this.create_time = create_time;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

    @Override
    public String toString() {
        return "VideoOrder{" +
                "id=" + id +
                ", out_trade_no='" + out_trade_no + '\'' +
                ", state=" + state +
                ", total_fee=" + total_fee +
                ", video_id=" + video_id +
                ", video_title='" + video_title + '\'' +
                ", video_img='" + video_img + '\'' +
                ", user_id=" + user_id +
                ", create_time=" + create_time +
                ", user=" + user +
                '}';
    }
}
```

## User.java

```text
package net.cybclass.online.domain;

import java.util.Date;

public class User {
    //内码
    private int id;
    //用户
    private String name;
    //密码
    private String pwd;
    //手机号
    private String phone;
    //头像
    private String head_img;
    //创建时间
    private Date create_time;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getPwd() {
        return pwd;
    }

    public void setPwd(String pwd) {
        this.pwd = pwd;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getHead_img() {
        return head_img;
    }

    public void setHead_img(String head_img) {
        this.head_img = head_img;
    }

    public Date getCreate_time() {
        return create_time;
    }

    public void setCreate_time(Date create_time) {
        this.create_time = create_time;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", pwd='" + pwd + '\'' +
                ", phone='" + phone + '\'' +
                ", head_img='" + head_img + '\'' +
                ", create_time=" + create_time +
                '}';
    }
}
```

## VideoOrderMapper.java

```text
package net.cybclass.online.dao;

import net.cybclass.online.domain.VideoOrder;

import java.util.List;

public interface VideoOrderMapper {
    /**
     * 查询全部订单，关联用户信息
     * @return
     */
    List<VideoOrder> queryVideoOrderList();
}
```

## SqlSessionDemo.java

```text
package net.cybclass.online;

import net.cybclass.online.dao.VideoMapper;
import net.cybclass.online.dao.VideoOrderMapper;
import net.cybclass.online.domain.Video;
import net.cybclass.online.domain.VideoOrder;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import java.io.IOException;
import java.io.InputStream;
import java.util.*;

public class SqlSessionDemo {
    public static void main(String[] args) throws IOException {
        String resouce="config/mybatis-config.xml";
        InputStream resourceAsStream = Resources.getResourceAsStream(resouce);
        SqlSessionFactory build = new SqlSessionFactoryBuilder().build(resourceAsStream);
        try(SqlSession session=build.openSession()){
            VideoOrderMapper mapper = session.getMapper(VideoOrderMapper.class);
            //resultMap association关联查询
            List<VideoOrder> list=mapper.queryVideoOrderList();
            System.out.println(list);
        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
```
