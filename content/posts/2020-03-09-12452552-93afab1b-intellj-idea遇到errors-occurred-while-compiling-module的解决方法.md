{

  "title": "IntellJ Idea遇到Errors occurred while compiling module的解决方法",
  "date": "2020-03-09",
  "description": "问题描述 解决办法 查看编译环境的JDk版本是否一致 Idea的菜单 Build,Execution,Deployment-Compliler-Java Complier的jdk版本是13 看下菜单File-Project Structure下的Project和modules的编译环境是jdk13",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12452552.html"

}

# 问题描述

```text
Information:java: Errors occurred while compiling module '0-common'
Information:javac 11 was used to compile java sources
Information:2020/3/9, 11:07 下午 - Build completed with 1 error and 0 warnings in 1 s 977 ms
```

# 解决办法

# 查看编译环境的JDk版本是否一致 

Idea的菜单 Build,Execution,Deployment-Compliler-Java Complier的jdk版本是13

![](/imported/posts/2020-03-09-12452552-93afab1b-intellj-idea遇到errors-occurred-while-compiling-module的解决方法/images/img_001_e6be1a00a51d.png)

## 看下菜单File-Project Structure下的Project和modules的编译环境是jdk13 

![](/imported/posts/2020-03-09-12452552-93afab1b-intellj-idea遇到errors-occurred-while-compiling-module的解决方法/images/img_002_109da09e4772.png)

![](/imported/posts/2020-03-09-12452552-93afab1b-intellj-idea遇到errors-occurred-while-compiling-module的解决方法/images/img_003_994e94fd0b0e.png)
