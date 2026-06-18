{

  "title": "cookie和session",
  "date": "2019-04-03",
  "description": "cookie的工作原理是：由服务器产生内容，浏览器收到请求后保存在本地；当浏览器再次访问时，浏览器会自动带上cookie，这样服务器就能通过cookie的内容来判断这个是“谁”了。但是由于cookie本身最大支持4096字节，以及cookie本身保存在客户端，可能被拦截或窃取，因此就需要有一种新的东",
  "tags": [
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/10646429.html"

}

cookie的工作原理是：由服务器产生内容，浏览器收到请求后保存在本地；当浏览器再次访问时，浏览器会自动带上cookie，这样服务器就能通过cookie的内容来判断这个是“谁”了。但是由于cookie本身最大支持4096字节，以及cookie本身保存在客户端，可能被拦截或窃取，因此就需要有一种新的东西，它能支持更多的字节，并且他保存在服务器，有较高的安全性。

　　cookie弥补了http无状态的不足，让服务器知道来的人是“谁”；但是cookie以文本的形式保存在本地，自身安全性较差；所以我们就通过cookie识别不同的用户，对应的在session里保存私密的信息以及超过4096字节的文本。

　　制作一个登陆页面，在验证了用户名和密码的正确性后跳转到后台的页面。但是测试后也发现，如果绕过登陆页面。直接输入后台的url地址也可以直接访问的。这个显然是不合理的。其实我们缺失的就是cookie和session配合的验证。有了这个验证过程，我们就可以实现和其他网站一样必须登录才能进入后台页面了。

　　先说一下这种认证的机制。每当我们使用一款浏览器访问一个登陆页面的时候，一旦我们通过了认证。服务器端就会发送一组随机唯一的字符串（假设是123abc）到浏览器端，这个被存储在浏览端的东西就叫cookie。而服务器端也会自己存储一下用户当前的状态，比如login=true，username=hahaha之类的用户信息。但是这种存储是以字典形式存储的，字典的唯一key就是刚才发给用户的唯一的cookie值。那么如果在服务器端查看session信息的话，理论上就会看到如下样子的字典

{'123abc':{'login':true,'username:hahaha'}}

因为每个cookie都是唯一的，所以我们在电脑上换个浏览器再登陆同一个网站也需要再次验证。那么为什么说我们只是理论上看到这样子的字典呢？因为处于安全性的考虑，其实对于上面那个大字典不光key值123abc是被加密的，value值{'login':true,'username:hahaha'}在服务器端也是一样被加密的。所以我们服务器上就算打开session信息看到的也是类似与以下样子的东西

{'123abc':dasdasdasd1231231da1231231}

　　在templates目录下创建两个html，login.html负责登录页面。backend页面代表后台页面

![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_002_961ddebeb323.gif)

```text
 1 <!DOCTYPE html>
 2 <html lang="en">
 3 <head>
 4     <meta charset="UTF-8">
 5     <title>Title</title>
 6 </head>
 7 <body>
 8 <form action="/login/" method="post">
 9     <p>用户名:<input type="text" name="username"></p>
10     <p>密  码:<input type="password" name="pwd"></p>
11     <p><input type="submit"></p>
12 </form>
13 </body>
14 </html>
```

login.html

![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_002_961ddebeb323.gif)

```text
 1 <!DOCTYPE html>
 2 <html lang="en">
 3 <head>
 4     <meta charset="UTF-8">
 5     <title>Title</title>
 6 </head>
 7 <body>
 8 <h1>登陆用户名:{{ username }}</h1>
 9 <a href="/logout">注销</a>
10 </body>
11 </html>
```

backend.html

![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_002_961ddebeb323.gif)

```text
 1 """COOKIEE_SESSION URL Configuration
 2
 3 The `urlpatterns` list routes URLs to views. For more information please see:
 4     https://docs.djangoproject.com/en/2.2/topics/http/urls/
 5 Examples:
 6 Function views
 7     1. Add an import:  from my_app import views
 8     2. Add a URL to urlpatterns:  path('', views.home, name='home')
 9 Class-based views
10     1. Add an import:  from other_app.views import Home
11     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
12 Including another URLconf
13     1. Import the include() function: from django.urls import include, path
14     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
15 """
16 from django.contrib import admin
17 from django.urls import path
18 from app01 import views
19 from django.conf.urls import url
20
21 urlpatterns = [
22     path('admin/', admin.site.urls),
23     url('login/', views.login),
24     url('backend/', views.backend),
25     url('logout/', views.logout),
26 ]
```

urls.py

![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_002_961ddebeb323.gif)

```text
 1 from django.shortcuts import render, redirect
 2
 3
 4 # Create your views here.
 5 def login(req):
 6     if req.method == "POST":
 7         username = req.POST.get("username")
 8         pwd = req.POST.get("pwd")
 9         if username == "alex" and pwd == "123":
10             # 设置 session内部的字典内容
11             req.session["is_login"] = True
12             req.session["username"] = username
13             return redirect("/backend")
14     return render(req, "login.html")
15
16
17 def backend(req):
18     is_login = req.session.get("is_login", False)  # 若为空，设置默认值False
19     if is_login:
20         # 获取字典的内容
21         cookie_content = req.COOKIES
22         session_content = req.session
23         username = req.session["username"]
24         return render(req, "backend.html", locals())
25     else:
26         return render(req, "/login")
27
28
29 def logout(req):
30     try:
31         # 删除is_login对应的value值
32         del req.session["is_login"]
33     except KeyError:
34         pass
35     # 点击注销用户之后，直接重定向回登陆页面
36     return redirect("/login")
```

views.py

目录结构如下:

![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_003_078ae81952e3.png)

效果图:

![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_004_39c9d2e8f593.png)

![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_005_330041113632.png)

![](/imported/posts/2019-04-03-10646429-acbb56ae-cookie和session/images/img_006_acc61dfd637b.png)
