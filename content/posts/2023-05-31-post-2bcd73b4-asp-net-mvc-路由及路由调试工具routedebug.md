---
title: "ASP.Net MVC 路由及路由调试工具RouteDebug"
date: 2023-05-31
description: "一、路由规则 1、可以创建多条路由规则，每条路由的name属性不相同 2、路由规则有优先级，最上面的路由规则优先级越高 App_Start文件下的：RouteConfig.cs 1 public static void RegisterRoutes(RouteCollection routes) 2"
tags:
  - "MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11279902.html"
---

<h1>一、路由规则</h1>
<p>　　1、可以创建多条路由规则，每条路由的name属性不相同</p>
<p>　　2、路由规则有优先级，最上面的路由规则优先级越高</p>
<p>App_Start文件下的：RouteConfig.cs</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> RegisterRoutes(RouteCollection routes)
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span>             routes.IgnoreRoute(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">{resource}.axd/{*pathInfo}</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 0, 1)">            routes.MapRoute(
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>                 name: <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Default2</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>                 url: <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">{controller}-{action}</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>                 defaults: <span style="color: rgba(0, 0, 255, 1)">new</span> { controller = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">HomeDemo</span><span style="color: rgba(128, 0, 0, 1)">"</span>, action = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Index</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)"> }
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">            );
</span><span style="color: rgba(0, 128, 128, 1)">10</span> 
<span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">            routes.MapRoute(
</span><span style="color: rgba(0, 128, 128, 1)">12</span>                 name: <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Default</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)">13</span>                 url: <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">{controller}/{action}/{id}</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)">14</span>                 defaults: <span style="color: rgba(0, 0, 255, 1)">new</span> { controller = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">HomeDemo</span><span style="color: rgba(128, 0, 0, 1)">"</span>, action = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Index</span><span style="color: rgba(128, 0, 0, 1)">"</span>, id =<span style="color: rgba(0, 0, 0, 1)"> UrlParameter.Optional }
</span><span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 0, 1)">            );
</span><span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">17</span>     }</pre>
