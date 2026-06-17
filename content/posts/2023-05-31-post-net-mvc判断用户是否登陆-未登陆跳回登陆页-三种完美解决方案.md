---
title: ".Net Mvc判断用户是否登陆、未登陆跳回登陆页、三种完美解决方案"
date: 2023-05-31
description: "开篇先不讲解，如何判断用户是否登陆，我们先来看用户登录的部分代码，账户密码都正确后，先将当前登录的用户名记录下来。 1 public ActionResult ProcessLogin() 2 { 3 try 4 { 5 string user_name = Request[&quot;LoginI"
tags:
  - "MVC"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11397576.html"
---

<p>　　<span style="font-family: &quot;Microsoft YaHei&quot;; font-size: 16px">开篇先不讲解，如何判断用户是否登陆，我们先来看用户登录的部分代码，账户密码都正确后，先将当前登录的用户名记录下来。</span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span>         <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> ActionResult ProcessLogin()
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>                 <span style="color: rgba(0, 0, 255, 1)">string</span> user_name = Request[<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">LoginId</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>                 <span style="color: rgba(0, 0, 255, 1)">string</span> user_pwd = Request[<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">LoginPwd</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>                 UserInfo model = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> UserInfo();
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>                 model.UName =<span style="color: rgba(0, 0, 0, 1)"> user_name;
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>                 model.UPwd =<span style="color: rgba(0, 0, 0, 1)"> user_pwd;
</span><span style="color: rgba(0, 128, 128, 1)">10</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (bllSession.UserInfo.Select(model).Count &gt; <span style="color: rgba(128, 0, 128, 1)">0</span>) <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">判断用户名密码是否正确</span>
<span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">12</span>                     <span style="color: rgba(255, 0, 0, 1); font-size: 16px"><strong>Session["loginUser"] = user_name; //记录当前登录的用户名</strong></span>
<span style="color: rgba(0, 128, 128, 1)">13</span>                     <span style="color: rgba(0, 0, 255, 1)">return</span> Content(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ok</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">15</span>                 <span style="color: rgba(0, 0, 255, 1)">else</span>
<span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">17</span>                     <span style="color: rgba(0, 0, 255, 1)">return</span> Content(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">用户名或密码错误！你会登陆吗？</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">18</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">19</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">20</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)">21</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">22</span>                 <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
</span><span style="color: rgba(0, 128, 128, 1)">23</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">24</span>         }</pre>
