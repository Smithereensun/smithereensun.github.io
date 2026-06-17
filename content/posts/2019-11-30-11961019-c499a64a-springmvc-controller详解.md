{

  "title": "springmvc Controller详解",
  "date": "2019-11-30",
  "description": "简介 在SpringMVC 中，控制器Controller 负责处理由DispatcherServlet 分发的请求，它把用户请求的数据经过业务处理层处理之后封装成一个Model ，然后再把该Model 返回给对应的View 进行展示。 示例 不适用注解修饰 返回ModelAndView contr",
  "tags": [
    "Spring",
    "JAVA",
    "Spring MVC"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11961019.html"

}

# 简介

　　在SpringMVC 中，控制器Controller 负责处理由DispatcherServlet 分发的请求，它把用户请求的数据经过业务处理层处理之后封装成一个Model ，然后再把该Model 返回给对应的View 进行展示。

# 示例

## 不适用注解修饰

### 返回ModelAndView

controller方法中定义ModelAndView对象并返回，对象中可添加model数据、指定view。

```text
package com.cyb.ssm.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import com.cyb.ssm.po.Item;
import com.cyb.ssm.service.ItemService;

@Controller
public class ItemController {
    @Autowired
    private ItemService Service;

    @RequestMapping("queryItem")
    public ModelAndView queryItem() {
        List<Item> itemList = Service.queryItemList();
        ModelAndView mvAndView = new ModelAndView();
        mvAndView.addObject("itemList", itemList);
        mvAndView.setViewName("item/item-list");
        return mvAndView;
    }
}
```

### 返回void

　　在controller**方法形参上可以定义request和response**，使用request或response指定响应结果：

```text
void service(HttpServletRequest request,HttpServletResponse response){}
```

1、使用request转发向页面，如下：

```text
request.getRequestDispatcher("页面路径").forward(request, response);
```

2、也可以通过response页面重定向：

```text
response.sendRedirect("url")
```

3、也可以通过response指定响应结果，例如：

```text
response.setCharacterEncoding("utf-8");
response.setContentType("application/json;charset=utf-8");
response.getWriter().write("json串");
```

### 返回字符串

```text
    public String queryItem(HttpServletRequest request,Model model) {
        //查询数据库，用静态数据模拟
        List<Item> itemList = Service.queryItemList();
        //方式一，使用Request的API
//        request.setAttribute("itemList", itemList);
        //方式二，使用Model接口的API
        model.addAttribute("itemList", itemList);
        return "item/item-list";
    }
```

#### 逻辑视图名

```text
return "item/item-list";
```

#### redirect重定向

```text
return "redirect:testRedirect";
```

redirect：

　　相当于“response.sendRedirect()”

　　游览器URL发生改变

　　Request域不能共享

### forward转发

```text
return "forward:testForward";
```

forward：

　　相当于“request.getRequestDispatcher().forward(request,response)”

　　浏览器URL不发送改变

　　Request域可以共享

```text
    @RequestMapping("queryItem")
    public String queryItem(HttpServletRequest request,Model model) {
        //查询数据库，用静态数据模拟
        List<Item> itemList = Service.queryItemList();
        //方式一，使用Request的API
//        request.setAttribute("itemList", itemList);
        //方式二，使用Model接口的API
        model.addAttribute("itemList", itemList);
//        return "item/item-list";
        //转发和重定向使用的代码
        request.setAttribute("id", 1);
//        return "redirect:testRedirect";
        return "forward:testForward";

    }
    //请求重定向测试
    @RequestMapping("testRedirect")
    public String testRedirect(HttpServletRequest request){
        String id = (String) request.getAttribute("id");
        System.out.println("request域的id："+id);
        return "";
    }
    //请求转发测试
    @RequestMapping("testForward")
    public String testForward(HttpServletRequest request){
        Integer id = (Integer) request.getAttribute("id");
        System.out.println("request域的id："+id);
        return "";
    }
```

## 使用注解修饰

### 返回带ResponseBody注解的值

### @ResponseBody注解和@RequestBody注解介绍

@ResponseBody的作用：

**ResponseBody**注解可以通过内置9种**HttpMessageConverter**，匹配不同的**Controller****返回值类型**，然后进行不同的**消息转换处理**

　　将转换之后的数据放到HttpServletResponse对象的**响应体**返回到页面，

　　不同的HttpMessageConverter处理的数据，指定的**ContentType值**也不同。

**@RequestBody**注解的作用和@ResponseBody注解正好相反，它是处理**请求参数**的Http消息转换的。

```text
    @RequestMapping("queryItemById")
    public @ResponseBody Item queryItemById() {
        Item item=Service.queryItemById(1);
        return item;
    }
//    @RequestMapping("queryItemById")
//    @ResponseBody
//    public  Item queryItemById2() {
//        Item item=Service.queryItemById(1);
//        return item;
//    }
```

```text
//@RestController相当于@Controller和@ResponseBody的组合
//该类所有方法的返回值都将被@ResponseBody注解给修饰
@RestController
public class RestItemController {
    @Autowired
    private ItemService Service;

    @RequestMapping("queryItemByIdWithRest")
    public Item queryItemById() {
        Item item = Service.queryItemById(1);
        return item;
    }
}
```

### 常用的 HttpMessageConverter

**MappingJacksonHttpMessageConverter处理POJO类型返回值**

 MappingJacksonHttpMessageConverter是专门处理POJO类型的。

默认使用**MappingJackson**的JSON处理能力，将后台返回的Java对象(POJO类型)，转为JSON格式输出到页面。

将响应体的**Content-Type**设置为**application/json**;charset=utf-8

**StringHttpMessageConverter处理String类型返回值**

StringHttpMessageConverter是专门处理**String**类型的。

调用response.getWriter()方法将String类型的字符串写回给调用者。

将响应体的**Content-Type**设置为**text/plain**;charset=utf-8

## @RequestMapping

　　通过RequestMapping注解可以定义不同的处理器映射规则

### URL路径映射

　　@RequestMapping(**value**="/item")或@RequestMapping("/item")

　　value的值是数组，可以将多个url映射到同一个方法

　　@RequestMapping(value={**"/item","/queryItem"**})

### 窄化请求映射

　　在**class上添加@RequestMapping(url)**指定通用**请求前缀**，限制此类下的所有方法的访问请求url必须以**请求前缀**开头，通过此方法对url进行**模块化分类**管理。

#### example

　　商品模块

　　　　/**item**/add

　　　　/**item**/update

　　　　/**item**/delete

　　用户模块

　　　　/**user**/add

　　　　/**user**/update

　　　　/**user**/delete

### 请求方法限定

#### 　　限定GET方法

　　@RequestMapping(**method**=RequestMethod.**GET**)

如果通过Post访问则报错：

　　HTTP Status 405 - Request method 'POST' not supported

例如：

　　@RequestMapping(value="/editItem",mtthod=RequestMethod.GET)

#### 　　限定POST方法

　　@RequestMapping(**method**=RequestMethod.**POST**)

如何通过Post访问则报错:

　　HTTP Status 405 - Request method 'GET' not supported

#### 　　GET和POST都可以

　　@RequestMapping(mthod={RequestMethod.GET,RequestMethod.POST})
