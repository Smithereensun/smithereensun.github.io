{

  "title": "SpringBoot中使用Servlet3.0注解开发自定义的拦截器",
  "date": "2020-07-05",
  "description": "使用Servlet3.0的注解进行配置步骤 启动类里面加@ServletComponentScan，进行扫描 新建一个Filter类，implements Filter，并实现对应的接口 @WebFilter标记一个类为filter，被spring扫描 urlPatterns：拦截规则，支持正则 控",
  "tags": [
    "Spring Boot"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13238256.html"

}

# 使用Servlet3.0的注解进行配置步骤

- 启动类里面加@ServletComponentScan，进行扫描
- 新建一个Filter类，implements Filter，并实现对应的接口
- @WebFilter标记一个类为filter，被spring扫描
- urlPatterns：拦截规则，支持正则
- 控制chain.doFilter的方法调用，来实现是否通过放行
- 不放行，web应用resp.sendRedirect("/index.html")或者返回json字符串

## 场景

　　权限控制、用户登陆状态控制，也可以交给拦截器处理等

## 实现

### 项目结构

![](/imported/posts/2020-07-05-13238256-bfb5d6a4-springboot中使用servlet3-0注解开发自定义的拦截器/images/img_001_e3832a39c846.png)

### VideoOrderController.java

```text
package net.cyb.demo.controller;

import net.cyb.demo.utils.JsonData;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/pri/order")
public class VideoOrderController {
    @RequestMapping("save")
    public JsonData saveOrder(){
        return JsonData.buildSuccess("下单成功");
    }
}
```

### User.java

```text
package net.cyb.demo.domain;

public class User {
    private int id;
    private String username;
    private String pwd;
    public User(){}
    public User(int id,String username,String pwd){
        this.id=id;
        this.username=username;
        this.pwd=pwd;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPwd() {
        return pwd;
    }

    public void setPwd(String pwd) {
        this.pwd = pwd;
    }

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", pwd='" + pwd + '\'' +
                '}';
    }
}
```

### LoginFilter.java（拦截规则）

```text
package net.cyb.demo.filter;

import net.cyb.demo.domain.User;
import net.cyb.demo.service.UserService;
import net.cyb.demo.service.impl.UserServiceImpl;
import org.thymeleaf.util.StringUtils;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebFilter(urlPatterns = "/api/v1/pri/*", filterName = "LoginFilter")
public class LoginFilter implements Filter {
    /**
     * 容器加载的时候
     *
     * @param filterConfig
     * @throws ServletException
     */
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.println("init LoginFilter============");
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        System.out.println("doFilter LoginFilter============");
        HttpServletRequest req = (HttpServletRequest) servletRequest;
        HttpServletResponse resp = (HttpServletResponse) servletResponse;
        String token = req.getHeader("token");
        if (StringUtils.isEmpty(token)) {
            token = req.getParameter("token");
        }
        if (StringUtils.isEmpty(token)) {
            return;
        } else {
            //判断token是否合法 TODO
            User user = UserServiceImpl.sessionMap.get(token);
            if (user != null) {
                filterChain.doFilter(servletRequest, servletResponse);
            }
        }
    }

    /**
     * 容器销毁的时候
     */
    @Override
    public void destroy() {
        System.out.println("destroy LoginFilter========");
    }
}
```

方式二

```text
package net.cyb.demo.filter;

import com.fasterxml.jackson.databind.ObjectMapper;
import net.cyb.demo.domain.User;
import net.cyb.demo.service.UserService;
import net.cyb.demo.service.impl.UserServiceImpl;
import net.cyb.demo.utils.JsonData;
import org.thymeleaf.util.StringUtils;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;

@WebFilter(urlPatterns = "/api/v1/pri/*", filterName = "LoginFilter")
public class LoginFilter implements Filter {
    private static final ObjectMapper objectMapper=new ObjectMapper();
    /**
     * 容器加载的时候
     *
     * @param filterConfig
     * @throws ServletException
     */
    @Override
    public void init(FilterConfig filterConfig) throws ServletException {
        System.out.println("init LoginFilter============");
    }

    @Override
    public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {
        System.out.println("doFilter LoginFilter============");
        HttpServletRequest req = (HttpServletRequest) servletRequest;
        HttpServletResponse resp = (HttpServletResponse) servletResponse;
        String token = req.getHeader("token");
        if (StringUtils.isEmpty(token)) {
            token = req.getParameter("token");
        }
        if (StringUtils.isEmpty(token)) {
            JsonData jsonData=JsonData.buildError(-3,"未登陆");
            String jsonStr=objectMapper.writeValueAsString(jsonData);
            renderJson(resp, jsonStr);
        } else {
            //判断token是否合法 TODO
            User user = UserServiceImpl.sessionMap.get(token);
            if (user != null) {
                filterChain.doFilter(servletRequest, servletResponse);
            }else {
                JsonData jsonData=JsonData.buildError(-2,"登陆失败,token无效");
                String jsonStr=objectMapper.writeValueAsString(jsonData);
                renderJson(resp, jsonStr);
            }
        }
    }

    private void renderJson(HttpServletResponse response,String json){
        response.setCharacterEncoding("utf-8");
        response.setContentType("application/json");
        try{
            PrintWriter writer=response.getWriter();
            writer.print(json);
        }catch (Exception e){
            e.printStackTrace();
        }
    }
    /**
     * 容器销毁的时候
     */
    @Override
    public void destroy() {
        System.out.println("destroy LoginFilter========");
    }
}
```

### UserMapper.java

```text
package net.cyb.demo.mapper;

import net.cyb.demo.domain.User;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
@Repository
public class UserMapper {
    private static Map<String, User> userMap = new HashMap<>();
    static {
        userMap.put("alex",new User(1,"alex","123"));
        userMap.put("sa",new User(2,"sa","123"));
        userMap.put("cyb",new User(3,"cyb","123"));
    }
    public User login(String username,String pwd){
        User user=userMap.get(username);
        if (user==null)return null;
        if (user.getPwd().equalsIgnoreCase(pwd))
            return user;
        return null;
    }
    public List<User> listUser(){
        List<User> list=new ArrayList<>();
        list.addAll(userMap.values());
        return list;
    }
}
```

### UserServiceImpl.java

```text
package net.cyb.demo.service.impl;

import net.cyb.demo.domain.User;
import net.cyb.demo.mapper.UserMapper;
import net.cyb.demo.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.UUID;

@Service
public class UserServiceImpl implements UserService {
    public static Map<String, User> sessionMap = new HashMap<>();
    @Autowired
    private UserMapper userMapper;

    @Override
    public String login(String username, String pwd) {
        User user = userMapper.login(username, pwd);
        if (user == null) {
            return null;
        } else {
            String token = UUID.randomUUID().toString();
            System.out.println(token);
            sessionMap.put(token, user);
            return token;
        }
    }

    @Override
    public List<User> listUser() {
        return userMapper.listUser();
    }
}
```

### DemoProject1Application.java(启动类)

```text
package net.cyb.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

@SpringBootApplication
@ServletComponentScan
public class DemoProject1Application {

    public static void main(String[] args) {

        SpringApplication.run(DemoProject1Application.class, args);
    }
}
```

### 测试

![](/imported/posts/2020-07-05-13238256-bfb5d6a4-springboot中使用servlet3-0注解开发自定义的拦截器/images/img_002_34f0372fb6fb.gif)
