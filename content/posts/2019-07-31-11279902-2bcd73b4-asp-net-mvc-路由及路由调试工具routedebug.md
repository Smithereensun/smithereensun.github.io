{

  "title": "ASP.Net MVC 路由及路由调试工具RouteDebug",
  "date": "2019-07-31",
  "description": "一、路由规则 、可以创建多条路由规则，每条路由的name属性不相同 、路由规则有优先级，最上面的路由规则优先级越高 App_Start文件下的：RouteConfig.cs 二、路由调试工具 当为我们的应用程序注册多个路由后，由于注册不当，得不到预期的结果。为什么会发生这种情况，请求具体走了哪个路由",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11279902.html"

}

# 一、路由规则

　　1、可以创建多条路由规则，每条路由的name属性不相同

　　2、路由规则有优先级，最上面的路由规则优先级越高

App_Start文件下的：RouteConfig.cs

```text
 1         public static void RegisterRoutes(RouteCollection routes)
 2         {
 3             routes.IgnoreRoute("{resource}.axd/{*pathInfo}");
 4
 5             routes.MapRoute(
 6                 name: "Default2",
 7                 url: "{controller}-{action}",
 8                 defaults: new { controller = "HomeDemo", action = "Index" }
 9             );
10
11             routes.MapRoute(
12                 name: "Default",
13                 url: "{controller}/{action}/{id}",
14                 defaults: new { controller = "HomeDemo", action = "Index", id = UrlParameter.Optional }
15             );
16         }
17     }
```

# 二、路由调试工具

　　当为我们的应用程序注册多个路由后，由于注册不当，得不到预期的结果。为什么会发生这种情况，请求具体走了哪个路由？这个时候主人公RegisterRoutes上场了。

**第一步：先下载dll类库，没有的请到我百度云盘下载**

链接：https://pan.baidu.com/s/1jJ1W88cOuTrdooLySnGVSg
提取码：097u
**第二步：引入包：RouteDebug**

![](/imported/posts/2019-07-31-11279902-2bcd73b4-asp-net-mvc-路由及路由调试工具routedebug/images/img_001_1bef6851c183.png)

**第三步：到Global.asax中重写测试路径**

```text
 1     public class MvcApplication : System.Web.HttpApplication
 2     {
 3         protected void Application_Start()
 4         {
 5             AreaRegistration.RegisterAllAreas();
 6             FilterConfig.RegisterGlobalFilters(GlobalFilters.Filters);
 7             RouteConfig.RegisterRoutes(RouteTable.Routes);
 8             BundleConfig.RegisterBundles(BundleTable.Bundles);
 9
10             **RouteDebug.RouteDebugger.RewriteRoutesForTesting(RouteTable.Routes);** //重写测试路径
11         }
12     }
```

**第四步：运行网站，进行分析路由规则**

![](/imported/posts/2019-07-31-11279902-2bcd73b4-asp-net-mvc-路由及路由调试工具routedebug/images/img_002_68b3bc84251b.png)

搞定！~~

#  三、路由的约束

```text
 1     public class RouteConfig
 2     {
 3         public static void RegisterRoutes(RouteCollection routes)
 4         {
 5             routes.IgnoreRoute("{resource}.axd/{*pathInfo}");
 6
 7             routes.MapRoute(
 8                 name: "Default2",
 9                 url: "{controller}-{action}",
10                 defaults: new { controller = "HomeDemo", action = "Index" },
11                 **constraints:new {Controller=@"^\d+$" },** //控制器约束
12                 **namespaces:new string[] { "MVCDemo2.Controllers" }** //命名空间约束
13             );
14
15             routes.MapRoute(
16                 name: "Default",
17                 url: "{controller}/{action}/{id}",
18                 defaults: new { controller = "HomeDemo", action = "Index", id = UrlParameter.Optional }
19             );
20         }
21     }
```
