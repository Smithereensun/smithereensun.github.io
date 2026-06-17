{

  "title": "SpringBoot 2.5.5整合SpringSecurity+JWT",
  "date": "2022-11-15",
  "description": "目录结构 添加依赖 pom.xml 通用工具类 CommonUtil.java JWTUtil.java RedisUtil.java ReturnT.java vo类 LoginInfo.java UserVo.java 常量 全局异常处理器 SpringSecurity相关 重写UserDeta",
  "tags": [
    "Spring Boot",
    "Spring"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/springsecurity.html"

}

# 目录结构 

![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_001_7840f0024b76.png)

# 添加依赖

```text
<!-- SpringSecurity -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>

        <!-- redis客户端 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>io.lettuce</groupId>
                    <artifactId>lettuce-core</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>redis.clients</groupId>
            <artifactId>jedis</artifactId>
        </dependency>
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-pool2</artifactId>
        </dependency>

        <!-- fastjson2 -->
        <dependency>
            <groupId>com.alibaba.fastjson2</groupId>
            <artifactId>fastjson2</artifactId>
            <version>2.0.19</version>
        </dependency>

        <!-- JWT -->
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt</artifactId>
            <version>0.9.1</version>
        </dependency>

        <!-- lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>
```

![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_002_8f900a89c634.gif)
![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_003_961ddebeb323.gif)

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
    <artifactId>ybchen-SpringSecurity</artifactId>
    <version>0.0.1-SNAPSHOT</version>
    <name>ybchen-SpringSecurity</name>
    <description>SpringBoot整合SpringSecurity</description>
    <properties>
        <java.version>1.8</java.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <!-- 排除tomcat容器 -->
            <exclusions>
                <exclusion>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-starter-tomcat</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <!-- undertow容器 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-undertow</artifactId>
        </dependency>

        <!-- SpringSecurity -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
        </dependency>

        <!-- redis客户端 -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-redis</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>io.lettuce</groupId>
                    <artifactId>lettuce-core</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
        <dependency>
            <groupId>redis.clients</groupId>
            <artifactId>jedis</artifactId>
        </dependency>
        <dependency>
            <groupId>org.apache.commons</groupId>
            <artifactId>commons-pool2</artifactId>
        </dependency>

        <!-- fastjson2 -->
        <dependency>
            <groupId>com.alibaba.fastjson2</groupId>
            <artifactId>fastjson2</artifactId>
            <version>2.0.19</version>
        </dependency>

        <!-- JWT -->
        <dependency>
            <groupId>io.jsonwebtoken</groupId>
            <artifactId>jjwt</artifactId>
            <version>0.9.1</version>
        </dependency>

        <!-- lombok -->
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
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

# 通用工具类

![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_002_8f900a89c634.gif)
![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_003_961ddebeb323.gif)

```text
package com.ybchen.utils;

import com.fasterxml.jackson.databind.ObjectMapper;
import lombok.extern.slf4j.Slf4j;

import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.security.MessageDigest;

/**
 * 公共工具类
 *
 * @author: chenyanbin 2022-11-13 19:17
 */
@Slf4j
public class CommonUtil {
    /**
     * 响应json数据给前端
     *
     * @param response
     * @param content
     */
    public static void sendJsonMessage(HttpServletResponse response, Object content) {
        ObjectMapper objectMapper = new ObjectMapper();
        response.setContentType("application/json;charset=utf-8");
        PrintWriter writer = null;
        try {
            writer = response.getWriter();
            writer.print(objectMapper.writeValueAsString(content));
            response.flushBuffer();
        } catch (IOException e) {
            log.info("响应json数据给前端失败：{}", e.getMessage());
        } finally {
            if (writer != null) {
                writer.close();
            }
        }
    }

    /**
     * md5加密
     *
     * @param data
     * @return
     */
    public static String MD5(String data) {
        try {
            java.security.MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] array = md.digest(data.getBytes("UTF-8"));
            StringBuilder sb = new StringBuilder();
            for (byte item : array) {
                sb.append(Integer.toHexString((item & 0xFF) | 0x100).substring(1, 3));
            }
            return sb.toString().toUpperCase();
        } catch (Exception exception) {
        }
        return null;
    }
}
```

CommonUtil.java

![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_002_8f900a89c634.gif)
![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_003_961ddebeb323.gif)

```text
package com.ybchen.utils;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import lombok.extern.slf4j.Slf4j;

import java.util.Date;

/**
 * jwt工具类
 *
 * @author: chenyanbin 2022-11-13 19:00
 */
@Slf4j
public class JWTUtil {
    /**
     * token过期时间,一般7天
     */
    private static final long EXPIRE = 60 * 1000 * 60 * 24 * 7;

    /**
     * 密钥
     */
    private static final String SECRET = "https://www.cnblogs.com/chenyanbin/";

    /**
     * 令牌前缀
     */
    private static final String TOKEN_PREFIX = "ybchen";

    /**
     * subject
     */
    private static final String SUBJECT = "security_jwt";

    /**
     * 根据用户信息，生成令牌token
     *
     * @param loginInfo 登录信息
     * @return
     */
    public static String geneJsonWebToken(String loginInfo) {
        if (loginInfo == null || "".equalsIgnoreCase(loginInfo)) {
            throw new NullPointerException("loginInfo对象为空");
        }
        String token = Jwts.builder()
                .setSubject(SUBJECT)
                //payLoad，负载
                .claim("loginInfo", loginInfo)
                //颁布时间
                .setIssuedAt(new Date())
                //过期时间
                .setExpiration(new Date(System.currentTimeMillis() + EXPIRE))
                .signWith(SignatureAlgorithm.HS256, SECRET).compact();
        return TOKEN_PREFIX + token;
    }

    /**
     * 校验令牌token
     *
     * @param token
     * @return
     */
    public static Claims checkJwt(String token) {
        try {
            final Claims body = Jwts.parser()
                    //设置签名
                    .setSigningKey(SECRET)
                    .parseClaimsJws(token.replace(TOKEN_PREFIX, ""))
                    .getBody();
            return body;
        } catch (Exception e) {
            log.error("jwt token解密失败，错误信息：{}", e);
            return null;
        }
    }
}
```

JWTUtil.java

![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_002_8f900a89c634.gif)
![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_003_961ddebeb323.gif)

```text
package com.ybchen.utils;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.HashOperations;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.ValueOperations;
import org.springframework.stereotype.Component;

import java.io.Serializable;
import java.util.Collection;
import java.util.concurrent.TimeUnit;

/**
 * redis工具类
 *
 * @author: chenyanbin 2022-11-13 19:05
 */
@Component
@Slf4j
public class RedisUtil {
    @Autowired
    RedisTemplate redisTemplate;

    /**
     * 判断缓存中是否有对应的value
     *
     * @param key
     * @return
     */
    public boolean exists(final String key) {
        return redisTemplate.hasKey(key);
    }

    /**
     * 删除对应的value
     *
     * @param key
     */
    public void remove(final String key) {
        if (exists(key)) {
            redisTemplate.delete(key);
        }
    }

    /**
     * 写入缓存
     *
     * @param key        缓存key
     * @param value      缓存value
     * @param expireTime 过期时间，秒
     * @return
     */
    public boolean set(final String key, Object value, Long expireTime) {
        ValueOperations<Serializable, Object> operations = redisTemplate.opsForValue();
        operations.set(key, value);
        redisTemplate.expire(key, expireTime, TimeUnit.SECONDS);
        return true;
    }

    /**
     * 原子递增
     *
     * @param key        键
     * @param expireTime 过期时间，秒
     * @return
     */
    public Long incr(final String key, Long expireTime) {
        ValueOperations<Serializable, Object> operations = redisTemplate.opsForValue();
        Long increment = operations.increment(key);
        redisTemplate.expire(key, expireTime, TimeUnit.SECONDS);
        return increment;
    }

    /**
     * 原子递增,永不过期
     *
     * @param key 键
     * @return
     */
    public Long incr(final String key) {
        ValueOperations<Serializable, Object> operations = redisTemplate.opsForValue();
        Long increment = operations.increment(key);
        return increment;
    }

    /**
     * 读取缓存
     *
     * @param key
     * @return
     */
    public Object get(final String key) {
        Object result = null;
        ValueOperations<Serializable, Object> operations = redisTemplate.opsForValue();
        result = operations.get(key);
        return result;
    }

    /**
     * 获得缓存的key列表
     * <p>
     * keys token:*
     * </>
     *
     * @param pattern 字符串前缀
     * @return 对象列表
     */
    public Collection<String> keys(final String pattern) {
        return redisTemplate.keys(pattern);
    }

    /**
     * 哈希 添加（Map<Map<key,value>,value>）
     *
     * @param key     第一个Map的key
     * @param hashKey 第二个Map的key
     * @param value   第二个Map的value
     */
    public void hashSet(String key, String hashKey, Object value) {
        HashOperations<String, String, Object> hash = redisTemplate.opsForHash();
        hash.put(key, hashKey, value);
    }

    /**
     * 哈希获取数据（Map<Map<key,value>,value>）
     *
     * @param key     第一个Map的key
     * @param hashKey 第二个Map的key
     * @return
     */
    public Object hashGet(String key, String hashKey) {
        HashOperations<String, String, Object> hash = redisTemplate.opsForHash();
        return hash.get(key, hashKey);
    }

    /**
     * 哈希删除某个key（Map<Map<key,value>,value>）
     *
     * @param key     第一个Map的key
     * @param hashKey 第二个Map的key
     * @return
     */
    public Long hashDelete(String key, String hashKey) {
        HashOperations<String, String, Object> hash = redisTemplate.opsForHash();
        return hash.delete(key, hashKey);
    }
}
```

RedisUtil.java

![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_002_8f900a89c634.gif)
![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_003_961ddebeb323.gif)

```text
package com.ybchen.utils;

import com.alibaba.fastjson2.JSON;

import java.io.Serializable;
import java.util.LinkedHashMap;
import java.util.Map;

/**
 * 统一响应工具类
 *
 * @author: chenyanbin 2022-11-13 18:48
 */
public class ReturnT<T> implements Serializable {
    /**
     * 状态码 0 表示成功，-1表示失败
     */
    private Integer code;
    /**
     * 数据
     */
    private T data;
    /**
     * 描述
     */
    private String msg;

    private ReturnT() {
    }

    private static <T> ReturnT<T> build(Integer code, T data, String msg) {
        ReturnT<T> resultT = new ReturnT<>();
        resultT.code = code;
        resultT.data = data;
        resultT.msg = msg;
        return resultT;
    }

    /**
     * 成功
     *
     * @param data
     * @return
     */
    public static <T> ReturnT<T> success(T data) {
        return build(0, data, null);
    }

    /**
     * 成功
     * @param <T>
     * @return
     */
    public static <T> ReturnT<T> success() {
        return build(0, null, null);
    }

    /**
     * 失败
     *
     * @param msg 错误信息
     * @return
     */
    public static <T> ReturnT<T> error(String msg) {
        return build(-1, null, msg);
    }

    /**
     * 失败
     *
     * @param code 状态码
     * @param msg  错误信息
     * @return
     */
    public static <T> ReturnT<T> error(int code, String msg) {
        return build(code == 0 ? -1 : code, null, msg);
    }

    /**
     * 判断接口响应是否成功
     *
     * @param data
     * @return
     */
    public static boolean isSuccess(ReturnT data) {
        return data.code == 0;
    }

    /**
     * 判断接口响应是否失败
     *
     * @param data
     * @return
     */
    public static boolean isFailure(ReturnT data) {
        return !isSuccess(data);
    }

    public Integer getCode() {
        return code;
    }

    public T getData() {
        return data;
    }

    public String getMsg() {
        return msg;
    }

    @Override
    public String toString() {
        Map<String, Object> resultMap = new LinkedHashMap<>(3);
        resultMap.put("code", this.code);
        resultMap.put("data", this.data);
        resultMap.put("msg", this.msg);
        return JSON.toJSONString(resultMap);
    }
}
```

ReturnT.java

# vo类

![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_002_8f900a89c634.gif)
![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_003_961ddebeb323.gif)

```text
package com.ybchen.vo;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

/**
 * 登录信息
 *
 * @author: chenyanbin 2022-11-14 16:54
 */
public class LoginInfo implements Serializable {
    /**
     * 用户信息
     */
    private UserVo userVo;
    /**
     * 权限信息
     */
    private List<String> permissionsList = new ArrayList<>();

    private LoginInfo() {
    }

    public LoginInfo(UserVo userVo, List<String> permissionsList) {
        this.userVo = userVo;
        this.permissionsList = permissionsList;
    }

    public UserVo getUserVo() {
        return userVo;
    }

    public void setUserVo(UserVo userVo) {
        this.userVo = userVo;
    }

    public List<String> getPermissionsList() {
        return permissionsList;
    }

    public void setPermissionsList(List<String> permissionsList) {
        this.permissionsList = permissionsList;
    }

    @Override
    public String toString() {
        return "LoginInfo{" +
                "userVo=" + userVo +
                ", permissionsList=" + permissionsList +
                '}';
    }
}
```

LoginInfo.java

![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_002_8f900a89c634.gif)
![](/imported/posts/2022-11-15-16886490-bb74ea41-springboot-2-5-5整合springsecurity-jwt/images/img_003_961ddebeb323.gif)

```text
package com.ybchen.vo;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.io.Serializable;

/**
 * 用户对象
 *
 * @author: chenyanbin 2022-11-13 19:19
 */
@Getter
@Setter
@ToString
public class UserVo implements Serializable {
    /**
     * 用户id
     */
    private Integer id;

    /**
     * 用户姓名
     */
    private String userName;

    /**
     * 密码
     */
    private String password;

    private UserVo() {
    }

    public UserVo(Integer id, String userName, String password) {
        this.id = id;
        this.userName = userName;
        this.password = password;
    }
}
```

UserVo.java

# 常量

```text
package com.ybchen.constant;

/**
 * redis常量key
 *
 * @author: chenyanbin 2022-11-13 21:05
 */
public class RedisKeyConstant {
    /**
     * 登录信息key
     */
    public static final String LOGIN_INFO_KEY = "user:login";
}
```

# 全局异常处理器

```text
package com.ybchen.exception;

import com.ybchen.utils.ReturnT;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.access.AccessDeniedException;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.web.HttpRequestMethodNotSupportedException;
import org.springframework.web.bind.MissingServletRequestParameterException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.method.annotation.MethodArgumentTypeMismatchException;
import org.springframework.web.servlet.NoHandlerFoundException;

/**
 * 全局异常拦截器
 *
 * @author: chenyanbin 2022-11-13 19:39
 */
@RestControllerAdvice
@Slf4j
public class GlobalException {

    /**
     * 请求方式有误
     *
     * @param e
     * @return
     */
    @ExceptionHandler(HttpRequestMethodNotSupportedException.class)
    public ReturnT httpRequestMethodNotSupportedException(HttpRequestMethodNotSupportedException e) {
        return ReturnT.error("请求方式有误！");
    }

    /**
     * 请求url不存在，404问题
     *
     * @param e
     * @return
     */
    @ExceptionHandler(NoHandlerFoundException.class)
    public ReturnT noHandlerFoundException(NoHandlerFoundException e) {
        return ReturnT.error("请求url不存在！");
    }

    /**
     * 请求参数转换异常
     * @param e
     * @return
     */
    @ExceptionHandler(MethodArgumentTypeMismatchException.class)
    public ReturnT methodArgumentTypeMismatchException(MethodArgumentTypeMismatchException e) {
        return ReturnT.error("参数转换异常：" + e.toString());
    }

    /**
     * 请求缺失参数
     * @param e
     * @return
     */
    @ExceptionHandler(MissingServletRequestParameterException.class)
    public ReturnT missingServletRequestParameterException(MissingServletRequestParameterException e) {
        return ReturnT.error("缺失请求参数：" + e.toString());
    }

    /**
     * SpringSecurity认证失败处理
     * @param e
     * @return
     */
    @ExceptionHandler(BadCredentialsException.class)
    public ReturnT badCredentialsException(BadCredentialsException e){
        return ReturnT.error(401, "用户认证失败！");
    }

    @ExceptionHandler(AccessDeniedException.class)
    public ReturnT accessDeniedException(AccessDeniedException e){
        return ReturnT.error(403,"你的权限不足！");
    }

    /**
     * 全局异常拦截
     *
     * @param e
     * @return
     */
    @ExceptionHandler(Exception.class)
    public ReturnT exception(Exception e) {
        log.error("全局异常：{}", e);
        return ReturnT.error(e.toString());
    }
}
```

# SpringSecurity相关

## 重写UserDetailsService

　　作用：重写该方法去数据库查找用户信息

```text
package com.ybchen.service;

import com.alibaba.fastjson2.annotation.JSONField;
import com.ybchen.utils.CommonUtil;
import com.ybchen.vo.UserVo;
import lombok.Data;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

/**
 * 默认SpringSecurity是在内存中查找用户的信息(InMemoryUserDetailsManager)，
 * UserDetailsService接口定义了一个根据用户名查询用户信息的方法，
 * 需要重写UserDetailsService，改到去数据库中查询用户信息
 *
 * @author: chenyanbin 2022-11-13 19:24
 */
@Service
public class UserDetailServiceImpl implements UserDetailsService {
    /**
     * 模拟数据库中用户数据
     */
    public static List<UserVo> userVoList = new ArrayList<UserVo>() {{
        // 注意数据库中存储的密码，MD5加密过的，也可以加盐
        this.add(new UserVo(1, "alex", CommonUtil.MD5("alex123")));
        this.add(new UserVo(2, "tom", CommonUtil.MD5("tom123")));
    }};

    /**
     * 获取用户信息
     *
     * @param userName 用户名
     * @return 根据用户名找用户信息，找不到的话，返回null
     * @throws UsernameNotFoundException
     */
    @Override
    public UserDetails loadUserByUsername(String userName) throws UsernameNotFoundException {
        // TODO 去数据库中，查找用户信息
        List<UserVo> collect = userVoList.stream().filter(obj -> obj.getUserName().equalsIgnoreCase(userName)).collect(Collectors.toList());
        // 如果用户不存在
        if (collect.size() == 0) {
            throw new RuntimeException("用户名不存在");
        }
        //TODO 根据用户id查找对应的权限信息
        List<String> permissionsList = Arrays.asList("admin", "test", "hello_test", "ROLE_admin");
        //将数据封装成UserDetails返回
        return new LoginUserSecurity(collect.get(0), permissionsList);
    }

    @Data
    public class LoginUserSecurity implements UserDetails, Serializable {
        /**
         * 用户对象
         */
        private UserVo userVo;

        private List<String> permissionsList;

        @JSONField(serialize = false)
        private List<GrantedAuthority> authorityList;

        /**
         * 无参构造
         */
        private LoginUserSecurity() {
        }

        /**
         * 有参构造
         *
         * @param userVo          用户对象
         * @param permissionsList 权限集合
         */
        public LoginUserSecurity(UserVo userVo, List<String> permissionsList) {
            this.userVo = userVo;
            this.permissionsList = permissionsList;
        }

        /**
         * 权限信息
         *
         * @return
         */
        @Override
        public Collection<? extends GrantedAuthority> getAuthorities() {
            if (authorityList != null) {
                return authorityList;
            }
            //将permissionsList中的String类型的权限信息，封装成SimpleGrantedAuthority对象
            authorityList = permissionsList
                    .stream()
                    .map(SimpleGrantedAuthority::new)
                    .distinct()
                    .collect(Collectors.toList());
            return authorityList;
        }

        /**
         * 密码
         *
         * @return
         */
        @Override
        public String getPassword() {
            return this.userVo.getPassword();
        }

        /**
         * 用户名
         *
         * @return
         */
        @Override
        public String getUsername() {
            return this.userVo.getId().toString();
        }

        /**
         * 账号是否过期
         *
         * @return
         */
        @Override
        public boolean isAccountNonExpired() {
            return true;
        }

        /**
         * 账号是否锁定
         *
         * @return
         */
        @Override
        public boolean isAccountNonLocked() {
            return true;
        }

        /**
         * 密码是否过期
         *
         * @return
         */
        @Override
        public boolean isCredentialsNonExpired() {
            return true;
        }

        /**
         * 账号是否启用
         *
         * @return
         */
        @Override
        public boolean isEnabled() {
            return true;
        }
    }
}
```

　　注：这里默认的用户账号和密码，实际去数据库中查询，这边模拟的数据密码md5加密，所以需要重写密码编码器

```text
package com.ybchen.config;

import com.ybchen.utils.CommonUtil;
import org.springframework.security.crypto.password.PasswordEncoder;

/**
 * 自定义用户密码，重写PasswordEncoder
 *
 * @author: chenyanbin 2022-11-13 19:53
 */
public class Md5PasswordEncoder implements PasswordEncoder {

    /**
     * 加密
     *
     * @param rawPassword 原始密码
     * @return
     */
    @Override
    public String encode(CharSequence rawPassword) {
        return CommonUtil.MD5(rawPassword.toString());
    }

    /**
     * 匹配密码
     *
     * @param rawPassword     原始密码
     * @param encodedPassword 存储的密码
     * @return
     */
    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return CommonUtil.MD5(rawPassword.toString()).equalsIgnoreCase(encodedPassword);
    }
}
```

　　将自定义密码编码器注入spring容器

```text
package com.ybchen.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

/**
 * app配置类
 * @author: chenyanbin 2022-11-13 20:12
 */
@Configuration
public class AppConfig {

    /**
     * 自定义SpringSecurity MD5编码器
     * @return
     */
    @Bean
    public PasswordEncoder passwordEncoder(){
        return new Md5PasswordEncoder();
    }
}
```

## jwt过滤器

```text
package com.ybchen.filter;

import com.alibaba.fastjson2.JSON;
import com.ybchen.constant.RedisKeyConstant;
import com.ybchen.utils.CommonUtil;
import com.ybchen.utils.JWTUtil;
import com.ybchen.utils.RedisUtil;
import com.ybchen.utils.ReturnT;
import com.ybchen.vo.LoginInfo;
import io.jsonwebtoken.Claims;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.stream.Collectors;

/**
 * jwt过滤器
 *
 * @author: chenyanbin 2022-11-13 21:22
 */
@Component
public class JwtFilter extends OncePerRequestFilter {
    @Autowired
    RedisUtil redisUtil;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        //获取token
        String token = request.getHeader("token");
        if (token == null || "".equalsIgnoreCase(token)) {
            token = request.getParameter("token");
        }
        if (token == null || "".equalsIgnoreCase(token)) {
            //放行
            filterChain.doFilter(request, response);
        } else {
            //解析token
            Claims claims = JWTUtil.checkJwt(token);
            if (claims == null) {
                CommonUtil.sendJsonMessage(response, ReturnT.error("token非法"));
                return;
            }
            //从redis中获取用户信息
            Integer id = Integer.parseInt(claims.get("loginInfo").toString());
            Object objValue = redisUtil.hashGet(RedisKeyConstant.LOGIN_INFO_KEY, id + "");
            if (objValue == null) {
                CommonUtil.sendJsonMessage(response, ReturnT.error("token过期或已注销登录"));
                return;
            }
            LoginInfo loginInfo = JSON.parseObject(JSON.toJSONString(objValue), LoginInfo.class);
            //存入SecurityContextHolder
            // 获取权限信息封装到Authentication
            UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(
                    loginInfo,
                    null,
                    loginInfo.getPermissionsList().stream()
                            .map(SimpleGrantedAuthority::new)
                            .distinct()
                            .collect(Collectors.toList())
            );
            SecurityContextHolder.getContext().setAuthentication(authenticationToken);
            //放行
            filterChain.doFilter(request, response);
        }
    }
}
```

## 跨域处理

```text
package com.ybchen.config;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * 跨域配置类
 * @author: chenyanbin 2022-11-14 20:47
 */
@Configuration
public class CorsConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        //设置允许跨域的路径
        registry.addMapping("/**")
                //设置允许跨域请求的域名
                .allowedOriginPatterns("*")
                //是否允许cookie
                .allowCredentials(true)
                //设置允许的请求方式
                .allowedMethods("GET","POST","DELETE","PUT")
                //设置允许的Header属性
                .allowedHeaders("*")
                //跨域允许时间，秒
                .maxAge(3600);
    }
}
```

## redis配置类

```text
package com.ybchen.config;

import com.fasterxml.jackson.annotation.JsonAutoDetect;
import com.fasterxml.jackson.annotation.PropertyAccessor;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.redis.connection.RedisConnectionFactory;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.serializer.Jackson2JsonRedisSerializer;
import org.springframework.data.redis.serializer.StringRedisSerializer;

/**
 * Redis配置类，处理中文乱码
 * @author: chenyanbin 2022-11-13 18:47
 */
@Configuration
public class RedisTemplateConfiguration {
    @Bean
    public RedisTemplate<Object, Object> redisTemplate(RedisConnectionFactory factory) {
        RedisTemplate<Object, Object> redisTemplate = new RedisTemplate<>();
        redisTemplate.setConnectionFactory(factory);
        //配置序列化规则
        Jackson2JsonRedisSerializer serializer = new Jackson2JsonRedisSerializer(Object.class);
        ObjectMapper objectMapper = new ObjectMapper();
        objectMapper.setVisibility(PropertyAccessor.ALL, JsonAutoDetect.Visibility.ANY);
        serializer.setObjectMapper(objectMapper);
        //设置key-value序列化规则
        redisTemplate.setKeySerializer(new StringRedisSerializer());
        redisTemplate.setValueSerializer(serializer);
        //设置hash-value序列化规则
        redisTemplate.setHashKeySerializer(new StringRedisSerializer());
        redisTemplate.setHashValueSerializer(serializer);
        return redisTemplate;
    }
}
```

## SpringSecurity配置类

```text
package com.ybchen.config;

import com.ybchen.filter.JwtFilter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

/**
 * SpringSecurity配置类
 *
 * @author: chenyanbin 2022-11-13 20:36
 */
@Configuration
//开启SpringSecurity的prePostEnabled配置
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class SecurityConfig extends WebSecurityConfigurerAdapter {
    @Autowired
    JwtFilter jwtFilter;
//    @Autowired
//    AuthenticationEntryPoint authenticationEntryPoint;
//    @Autowired
//    AccessDeniedHandler accessDeniedHandler;

    @Override
    @Bean
    public AuthenticationManager authenticationManagerBean() throws Exception {
        return super.authenticationManagerBean();
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                //关闭csrf
                .csrf().disable()
                //不通过Session获取SecurityContext
                .sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                .and()
                .authorizeRequests()
                //对于登录接口，允许匿名访问
                .antMatchers("/api/v1/user/login").anonymous()
                //除了匿名访问的所有请求，全部需要鉴权认证
                .anyRequest().authenticated();
        //添加过滤器
        http.addFilterAfter(jwtFilter, UsernamePasswordAuthenticationFilter.class);
        //配置异常处理器，也可以用全局异常拦截器，拦截：AccessDeniedException，BadCredentialsException
//        http.exceptionHandling()
//                //认证失败处理器
//                .authenticationEntryPoint(authenticationEntryPoint)
//                //授权失败处理器
//                .accessDeniedHandler(accessDeniedHandler);
        //允许跨域
        http.cors();
    }
}
```

　　2个异常处理器，当然也可以使用SpringBoot全局异常拦截处理，也可以写到SpringSecurity配置类中

```text
//package com.ybchen.config;
//
//import com.ybchen.utils.CommonUtil;
//import com.ybchen.utils.ReturnT;
//import lombok.extern.slf4j.Slf4j;
//import org.springframework.security.core.AuthenticationException;
//import org.springframework.security.web.AuthenticationEntryPoint;
//import org.springframework.stereotype.Component;
//
//import javax.servlet.ServletException;
//import javax.servlet.http.HttpServletRequest;
//import javax.servlet.http.HttpServletResponse;
//import java.io.IOException;
//
///**
// * 认证失败处理器
// *
// * @author: chenyanbin 2022-11-14 13:06
// */
//@Component
//@Slf4j
//public class AuthenticationEntryPointImpl implements AuthenticationEntryPoint {
//
//    @Override
//    public void commence(HttpServletRequest request, HttpServletResponse response, AuthenticationException e) throws IOException, ServletException {
//        log.error("认证失败：{}", e);
//        CommonUtil.sendJsonMessage(response, ReturnT.error(401, "用户认证失败"));
//    }
//}
```

```text
//package com.ybchen.config;
//
//import com.ybchen.utils.CommonUtil;
//import com.ybchen.utils.ReturnT;
//import lombok.extern.slf4j.Slf4j;
//import org.springframework.security.access.AccessDeniedException;
//import org.springframework.security.web.access.AccessDeniedHandler;
//import org.springframework.stereotype.Component;
//
//import javax.servlet.ServletException;
//import javax.servlet.http.HttpServletRequest;
//import javax.servlet.http.HttpServletResponse;
//import java.io.IOException;
//
///**
// * 授权失败处理器
// * @author: chenyanbin 2022-11-14 13:11
// */
//@Component
//@Slf4j
//public class AccessDeniedHandlerImpl implements AccessDeniedHandler {
//
//    @Override
//    public void handle(HttpServletRequest request, HttpServletResponse response, AccessDeniedException e) throws IOException, ServletException {
//        log.error("授权失败：{}",e);
//        CommonUtil.sendJsonMessage(response, ReturnT.error(403,"你的权限不足！"));
//    }
//}
```

## 控制层

```text
package com.ybchen.controller;

import com.ybchen.constant.RedisKeyConstant;
import com.ybchen.service.UserDetailServiceImpl;
import com.ybchen.utils.JWTUtil;
import com.ybchen.utils.RedisUtil;
import com.ybchen.utils.ReturnT;
import com.ybchen.vo.LoginInfo;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.Objects;

/**
 * 用户api
 *
 * @author: chenyanbin 2022-11-13 20:27
 */
@RestController
@RequestMapping("/api/v1/user")
@Slf4j
public class UserController {
    @Autowired
    AuthenticationManager authenticationManager;
    @Autowired
    RedisUtil redisUtil;

    /**
     * 用户登录
     *
     * @param userName 用户名
     * @param password 密码
     * @return
     */
    @GetMapping("login")
    public ReturnT login(
            @RequestParam(value = "userName", required = true) String userName,
            @RequestParam(value = "password", required = true) String password
    ) {
        //AuthenticationManager authenticate进行用户认证-----》其实是调用UserDetailsService.loadUserByUsername方法
        UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(userName, password);
        Authentication authenticate = authenticationManager.authenticate(authenticationToken);
        //如果认证没通过，给出对应的提示
        if (Objects.isNull(authenticate)) {
            return ReturnT.error("账号/密码错误");
        }
        //用户id
        UserDetailServiceImpl.LoginUserSecurity loginUser = (UserDetailServiceImpl.LoginUserSecurity) authenticate.getPrincipal();
        Integer userId = loginUser.getUserVo().getId();
        String token = JWTUtil.geneJsonWebToken(userId.toString());
        //token写入redis Hash
        redisUtil.hashSet(RedisKeyConstant.LOGIN_INFO_KEY, userId + "", new LoginInfo(loginUser.getUserVo(), loginUser.getPermissionsList()));
        log.info("token= \n {}", token);
        return ReturnT.success(token);
    }

    /**
     * 注销登录
     *
     * @return
     */
    @GetMapping("logout")
    public ReturnT logout() {
        //获取SecurityContextHolder中的用户id
        UsernamePasswordAuthenticationToken authentication = (UsernamePasswordAuthenticationToken) SecurityContextHolder.getContext().getAuthentication();
        LoginInfo loginInfo = (LoginInfo) authentication.getPrincipal();
        Integer id = loginInfo.getUserVo().getId();
        //删除redis的key
        redisUtil.hashDelete(RedisKeyConstant.LOGIN_INFO_KEY, id + "");
        return ReturnT.success("注销成功");
    }
}
```

```text
package com.ybchen.controller;

import com.ybchen.utils.ReturnT;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

/**
 * @author: chenyanbin 2022-11-13 18:03
 */
@RestController
public class HelloController {
    /**
     * -@PreAuthorize()
     * ---hasAuthority：底层调用的是UserDetailsService.getAuthorities()，也就是我们重写的方法，判断入参是否在Set集合中，true放行，false拦截
     * ---hasAnyAuthority：可以传入多个权限，只有用户有其中任意一个权限都可以访问对应资源
     * ---hasRole：要求有对应的角色才可以访问，但是他内部会把我们传入的参数前面拼接：ROLE_ 后在比较。所以我们定义用户权限也要加这个前缀：ROLE_
     * ---hasAnyRole：可以传入多个角色，有任意一个角色就可以访问资源
     *
     * @return
     */
    @GetMapping("hello")
    //加权限
//    @PreAuthorize("hasAuthority('admin')")
//    @PreAuthorize("hasAnyAuthority('admin','test')")
//    @PreAuthorize("hasRole('admin')")
    @PreAuthorize("hasAnyRole('admin','test')")
    public ReturnT<String> hello() {
        return ReturnT.success("博客地址：https://www.cnblogs.com/chenyanbin/");
    }
}
```

# 项目源码

```text
链接: https://pan.baidu.com/s/1h6NFpZ7HC9DY8s820hctTQ?pwd=h8um 提取码: h8um
```
