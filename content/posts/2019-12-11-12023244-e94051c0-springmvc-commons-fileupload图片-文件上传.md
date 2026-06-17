{

  "title": "SpringMvc commons-fileupload图片/文件上传",
  "date": "2019-12-11",
  "description": "简介 SpringMvc文件上传的实现，是由commons-fileupload这个jar包实现的。 需求 在修改商品页面，添加上传商品图片功能。 Maven依赖包 pom.xml 配置多部件bean：springmvc.xml 控制层：ItemController.java jsp文件：item-",
  "tags": [
    "MVC",
    "JAVA",
    "Spring MVC"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12023244.html"

}

# 简介

　　SpringMvc文件上传的实现，是由commons-fileupload这个jar包实现的。

# 需求

在修改商品页面，添加上传商品图片功能。

# Maven依赖包

## pom.xml

```text
        <!-- 文件上传 -->
        <dependency>
            <groupId>commons-fileupload</groupId>
            <artifactId>commons-fileupload</artifactId>
            <version>1.4</version>
        </dependency>
```

## 配置多部件bean：springmvc.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:aop="http://www.springframework.org/schema/aop"
    xmlns:mvc="http://www.springframework.org/schema/mvc"
    xmlns:tx="http://www.springframework.org/schema/tx"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd
        http://www.springframework.org/schema/context
        http://www.springframework.org/schema/context/spring-context.xsd
        http://www.springframework.org/schema/tx
        http://www.springframework.org/schema/tx/spring-tx.xsd
        http://www.springframework.org/schema/mvc
        http://www.springframework.org/schema/mvc/spring-mvc.xsd
        http://www.springframework.org/schema/aop
        http://www.springframework.org/schema/aop/spring-aop.xsd">
    <!-- 处理器类的扫描 -->
    <context:component-scan
        base-package="com.cyb.ssm.controller"></context:component-scan>
    <mvc:annotation-driven
        conversion-service="conversionService" />
    <!-- 显示配置视图解析器 -->
    <bean
        class="org.springframework.web.servlet.view.InternalResourceViewResolver">
        <property name="prefix" value="/WEB-INF/jsp/"></property>
        <property name="suffix" value=".jsp"></property>
    </bean>
    <!-- 配置自定义的转换服务 -->
    <bean id="conversionService"
        class="org.springframework.format.support.FormattingConversionServiceFactoryBean">
        <property name="converters">
            <set>
                <!-- 自定义日期类型转换器 -->
                <bean class="com.cyb.ssm.controller.converter.DateConverter"></bean>
            </set>
        </property>
    </bean>
    <!-- 配置异常处理器 -->
    <bean class="com.cyb.ssm.resolver.CustomExceptionResolver"></bean>
    <!-- 配置多部件解析器，id固定值，不能乱写 -->
    <bean id="multipartResolver"
        class="org.springframework.web.multipart.commons.CommonsMultipartResolver">
        <!-- 限制上传文件的大小,单位是byte -->
        <property name="maxUploadSize" value="5000000"></property>
    </bean>
</beans>
```

## 控制层：ItemController.java

```text
package com.cyb.ssm.controller;

import java.io.File;
import java.io.IOException;
import java.util.Date;
import java.util.List;
import java.util.UUID;
import javax.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;
import com.cyb.ssm.exception.CustomException;
import com.cyb.ssm.po.Item;
import com.cyb.ssm.po.ItemQueryVO;
import com.cyb.ssm.service.ItemService;

//@Controller
//RestController:注解相当于Controller注解和ResponseBody注解的结合体
@RestController
@RequestMapping(value = "item", produces = "application/json;charset=utf8")
public class ItemController {
    @Autowired
    private ItemService Service;

    @RequestMapping(value = "updateItem")
    public Item updateItem(Integer id, String name, Float price, Item item, MultipartFile pictureFile) throws Exception {
        System.out.println("1111");
        if (pictureFile != null) {
            //获取上传文件名称
            String originalFilename = pictureFile.getOriginalFilename();
            if (originalFilename != null && !"".contentEquals(originalFilename)) {
                //获取扩展名
                String extName = originalFilename.substring(originalFilename.lastIndexOf("."));
                //重新生成一个文件名称
                String newFileName = UUID.randomUUID().toString()+extName;
                //指定存储文件的根目录
                String baseDir="D:\\temp\\pic\\";
                File dirFile=new File(baseDir);
                if (!dirFile.exists()) {
                    dirFile.mkdirs();
                }
                //将上传的文件复制到新的文件(完整路径)中
                pictureFile.transferTo(new File(baseDir + newFileName));

                //保存文件路径
                item.setPic(newFileName);
            }
        }
        //商品修改
        Service.updateItem(item);
        return item;
    }

    @RequestMapping("showEdit")
    public ModelAndView showEdit(Integer id) {
        Item item = Service.queryItemById(id);
        ModelAndView mvAndView = new ModelAndView();
        mvAndView.addObject("item", item);
        mvAndView.setViewName("item/item-edit");
        return mvAndView;
    }
}
```

## jsp文件：item-edit.jsp

```text
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>修改商品信息</title>
</head>
<body>
    <!-- 上传图片是需要指定属性 enctype="multipart/form-data" -->
    <form id="itemForm"
        action="${pageContext.request.contextPath}/item/updateItem"
        method="post" enctype="multipart/form-data">
        <input type="hidden" name="id" value="${item.id }" /> 修改商品信息：
        <table width="100%" border=1>
            <tr>
                <td>商品名称</td>
                <td><input type="text" name="name" value="${item.name }" /></td>
            </tr>
            <tr>
                <td>商品价格</td>
                <td><input type="text" name="price" value="${item.price }" /></td>
            </tr>
            <tr>
                <td>商品图片</td>
                <td><c:if test="${item.pic !=null}">
                        <img src="http://localhost/pic/${item.pic} " width=100 height=100 />
                        <br />
                    </c:if> <input type="file" name="pictureFile" /></td>
            </tr>
            <tr>
                <td>商品简介</td>
                <td><textarea rows="3" cols="30" name="detail">${item.detail }</textarea>
                </td>
            </tr>
            <tr>
                <td colspan="2" align="center"><input type="submit" value="提交" />
                </td>
            </tr>
        </table>
    </form>
</body>
</html>
```

## 配置tomcat和映射磁盘路径(**注意端口不要冲突**)

![](/imported/posts/2019-12-11-12023244-e94051c0-springmvc-commons-fileupload图片-文件上传/images/img_001_9d87dc43d379.gif)

## 测试

![](/imported/posts/2019-12-11-12023244-e94051c0-springmvc-commons-fileupload图片-文件上传/images/img_002_bbb6b066d726.gif)

## 项目源码

[直接下载](https://files-cdn.cnblogs.com/files/chenyanbin/upload-pic.rar)
