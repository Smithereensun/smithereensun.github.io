{

  "title": "eclipse配置Tomcat The superclass \"javax.servlet.http.HttpServlet\" was not found on the Java Build Path",
  "date": "2019-11-26",
  "description": "介绍 问题描述 我们在使用Ecplise开发java web时，可能会报错误：***The superclass \"javax.servlet.http.HttpServlet\" was not found on the Java Build *** Path*** 问题原因 项目中找不到***To",
  "tags": [
    "Java"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11936111.html"

}

# 介绍

## 问题描述

　　我们在使用Ecplise开发java web时，可能会报错误：***The superclass "javax.servlet.http.HttpServlet" was not found on the Java Build ***

*** Path***

![](images/img_001_7ddfc2547975.png)

## 问题原因

　　项目中找不到***Tomcat运行时相关类***

# 解决方法

## 下载Tomcat

### 方法一

　　指定Tomcat版本后，让Ecplise自动下载(Download and Install)，具体请看动态图,自动会下载到指定的路径下，下载过程根据个人网速可能会有点差异，耐心等待就好啦

![](images/img_002_cdb337e63891.gif)

## 方式二

　　官网下载：https://tomcat.apache.org/

　　进入官网找到想下载的Tomcat的版本，并适合当前操作系统的文件，下载到指定位置即可，操作步骤请看动态图

![](images/img_003_3c8a2424530d.gif)

## 为项目指定Tomcat

　　找到我们刚才下载后的Tomcat文件，配置请看动态图

![](images/img_004_8fd95dd6fe4f.gif)

搞定！！！
