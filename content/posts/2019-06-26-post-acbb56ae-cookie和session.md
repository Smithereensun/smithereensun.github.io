---
title: "cookie和session"
date: 2019-06-26
description: "cookie的工作原理是：由服务器产生内容，浏览器收到请求后保存在本地；当浏览器再次访问时，浏览器会自动带上cookie，这样服务器就能通过cookie的内容来判断这个是“谁”了。但是由于cookie本身最大支持4096字节，以及cookie本身保存在客户端，可能被拦截或窃取，因此就需要有一种新的东"
tags:
  - "Django"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10646429.html"
---

<p>　　cookie的工作原理是：由服务器产生内容，浏览器收到请求后保存在本地；当浏览器再次访问时，浏览器会自动带上cookie，这样服务器就能通过cookie的内容来判断这个是“谁”了。但是由于cookie本身最大支持4096字节，以及cookie本身保存在客户端，可能被拦截或窃取，因此就需要有一种新的东西，它能支持更多的字节，并且他保存在服务器，有较高的安全性。</p>
<p>　　cookie弥补了http无状态的不足，让服务器知道来的人是“谁”；但是cookie以文本的形式保存在本地，自身安全性较差；所以我们就通过cookie识别不同的用户，对应的在session里保存私密的信息以及超过4096字节的文本。</p>
<p>　　制作一个登陆页面，在验证了用户名和密码的正确性后跳转到后台的页面。但是测试后也发现，如果绕过登陆页面。直接输入后台的url地址也可以直接访问的。这个显然是不合理的。其实我们缺失的就是cookie和session配合的验证。有了这个验证过程，我们就可以实现和其他网站一样必须登录才能进入后台页面了。</p>
<p>　　先说一下这种认证的机制。每当我们使用一款浏览器访问一个登陆页面的时候，一旦我们通过了认证。服务器端就会发送一组随机唯一的字符串（假设是123abc）到浏览器端，这个被存储在浏览端的东西就叫cookie。而服务器端也会自己存储一下用户当前的状态，比如login=true，username=hahaha之类的用户信息。但是这种存储是以字典形式存储的，字典的唯一key就是刚才发给用户的唯一的cookie值。那么如果在服务器端查看session信息的话，理论上就会看到如下样子的字典</p>
<p>{'123abc':{'login':true,'username:hahaha'}}</p>
<p>因为每个cookie都是唯一的，所以我们在电脑上换个浏览器再登陆同一个网站也需要再次验证。那么为什么说我们只是理论上看到这样子的字典呢？因为处于安全性的考虑，其实对于上面那个大字典不光key值123abc是被加密的，value值{'login':true,'username:hahaha'}在服务器端也是一样被加密的。所以我们服务器上就算打开session信息看到的也是类似与以下样子的东西</p>
<p>{'123abc':dasdasdasd1231231da1231231}</p>
<p>　　在templates目录下创建两个html，login.html负责登录页面。backend页面代表后台页面</p>
<div class="cnblogs_code"><img id="code_img_closed_1220a39f-0a02-4fee-b2e6-533fc391abf4" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_1220a39f-0a02-4fee-b2e6-533fc391abf4" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_1220a39f-0a02-4fee-b2e6-533fc391abf4" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 255, 1)">&lt;!</span><span style="color: rgba(255, 0, 255, 1)">DOCTYPE html</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">html </span><span style="color: rgba(255, 0, 0, 1)">lang</span><span style="color: rgba(0, 0, 255, 1)">="en"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">head</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 4</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">meta </span><span style="color: rgba(255, 0, 0, 1)">charset</span><span style="color: rgba(0, 0, 255, 1)">="UTF-8"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 5</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">title</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>Title<span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">title</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">head</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">body</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">form </span><span style="color: rgba(255, 0, 0, 1)">action</span><span style="color: rgba(0, 0, 255, 1)">="/login/"</span><span style="color: rgba(255, 0, 0, 1)"> method</span><span style="color: rgba(0, 0, 255, 1)">="post"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 9</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">p</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>用户名:<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">input </span><span style="color: rgba(255, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">="text"</span><span style="color: rgba(255, 0, 0, 1)"> name</span><span style="color: rgba(0, 0, 255, 1)">="username"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">p</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">10</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">p</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>密  码:<span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">input </span><span style="color: rgba(255, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">="password"</span><span style="color: rgba(255, 0, 0, 1)"> name</span><span style="color: rgba(0, 0, 255, 1)">="pwd"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">p</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">11</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">p</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;</span><span style="color: rgba(128, 0, 0, 1)">input </span><span style="color: rgba(255, 0, 0, 1)">type</span><span style="color: rgba(0, 0, 255, 1)">="submit"</span><span style="color: rgba(0, 0, 255, 1)">&gt;&lt;/</span><span style="color: rgba(128, 0, 0, 1)">p</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">form</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">body</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 255, 1)">&lt;/</span><span style="color: rgba(128, 0, 0, 1)">html</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
