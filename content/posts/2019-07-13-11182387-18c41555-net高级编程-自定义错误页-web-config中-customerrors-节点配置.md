{

  "title": ".Net高级编程-自定义错误页 web.config中<customErrors>节点配置",
  "date": "2019-07-13",
  "description": "错误页 、当页面发生错误的时候，ASP.Net会将错误信息展示出来(Sqlconnection的错误就能暴露连接字符串)，这样一来不好看，二来泄露网站的内部实现信息，给网站带来安全隐患，因此需要定制错误页，发生错误时显示开发人员定制的页面。404页面放点广告也好的嘛。 、配置web.config，配",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11182387.html"

}

# 错误页

　　1、当页面发生错误的时候，ASP.Net会将错误信息展示出来(Sqlconnection的错误就能暴露连接字符串)，这样一来不好看，二来泄露网站的内部实现信息，给网站带来安全隐患，因此需要定制错误页，发生错误时显示开发人员定制的页面。404页面放点广告也好的嘛。

　　2、配置web.config，配置customErrors区域：

```text
1   <system.web>
2     <customErrors mode="on" defaultRedirect="MyErrorPage.aspx">
3       <error statusCode="403" redirect="NoAccess.html"/>
4       <error statusCode="404" redirect="FileNotFound.html"/>
5     </customErrors>
6   </system.web>
```

　　3、mode三个值可选：on：总是显示定制错误页面；off：不显示定制错误页面，直接显示调用堆栈等异常信息；remoteonlu：对于本机的访问显示对战等异常信息，对于外部用户的显示定制错误页面。一般设置为**RemoteOnly**，这样发生错误的话，管理员可以在服务器的浏览器中看详细错误信息，普通用户看不到。
