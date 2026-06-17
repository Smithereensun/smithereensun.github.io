---
title: ".Net 基于Memcache集群的分布式Session"
date: 2023-05-31
description: "简述 基于Memcache的Session大家都各有各的说法，比方说：当memcached集群发生故障（比如内存溢出）或者维护（比如升级、增加或减少服务器）时，用户会无法登录，或者被踢掉线等等，每种技术各有优缺点，只是适应的场景不同罢了。 知识点补充 服务器Memcache配置：https://ww"
tags:
  - "MVC"
  - "分布式架构"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11442987.html"
---

<h1>简述</h1>
<p><span style="font-family: &quot;Microsoft YaHei&quot;">　　基于Memcache的Session大家都各有各的说法，比方说：当memcached集群发生故障（比如内存溢出）或者维护（比如升级、增加或减少服务器）时，用户会无法登录，或者被踢掉线等等，每种技术各有优缺点，只是适应的场景不同罢了。</span></p>
<h1>知识点补充</h1>
<p>　　服务器Memcache配置：https://www.cnblogs.com/chenyanbin/p/11415368.html</p>
<p>　　<span style="font-family: &quot;Microsoft YaHei&quot;">Memcache集群配置：https://www.cnblogs.com/chenyanbin/p/11441490.html</span></p>
<p><span style="font-family: &quot;Microsoft YaHei&quot;">　　Mvc校验用户是否登陆：https://www.cnblogs.com/chenyanbin/p/11397576.html</span></p>
<p><span style="font-family: &quot;Microsoft YaHei&quot;">　　演示代码使用的其他完整类库：https://www.cnblogs.com/chenyanbin/p/11186495.html</span></p>
<h1>代码演示(.Net的Mvc架构)：</h1>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>登陆页控制器</strong></span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span>         IBllSession bllSession = BllSessionFactory.GetCurrentBllSession(); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">业务层基类</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 处理登陆的表单
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 5</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 6</span>         <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> ActionResult ProcessLogin()
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">10</span>                 <span style="color: rgba(0, 0, 255, 1)">string</span> user_name = Request[<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">LoginId</span><span style="color: rgba(128, 0, 0, 1)">"</span>]; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">用户名</span>
<span style="color: rgba(0, 128, 128, 1)">11</span>                 <span style="color: rgba(0, 0, 255, 1)">string</span> user_pwd = Request[<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">LoginPwd</span><span style="color: rgba(128, 0, 0, 1)">"</span>]; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">密码</span>
<span style="color: rgba(0, 128, 128, 1)">12</span>                 UserInfo model = <span style="color: rgba(0, 0, 255, 1)">new</span> UserInfo(); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">实体类</span>
<span style="color: rgba(0, 128, 128, 1)">13</span>                 model.UName = user_name; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">实体类赋值</span>
<span style="color: rgba(0, 128, 128, 1)">14</span>                 model.UPwd =<span style="color: rgba(0, 0, 0, 1)"> user_pwd; 
</span><span style="color: rgba(0, 128, 128, 1)">15</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (bllSession.UserInfo.Select(model).Count &gt; <span style="color: rgba(128, 0, 128, 1)">0</span>) <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">判断用户名密码是否正确</span>
<span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">17</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">旧方法
</span><span style="color: rgba(0, 128, 128, 1)">18</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">Session["loginUser"] = user_name;
</span><span style="color: rgba(0, 128, 128, 1)">19</span> 
<span style="color: rgba(0, 128, 128, 1)">20</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">新方法
</span><span style="color: rgba(0, 128, 128, 1)">21</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">Memcache+Cookie替代Session登陆
</span><span style="color: rgba(0, 128, 128, 1)">22</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">立即分配一个标志GUID，把标志作为Memcache存储数据的key，把用户对象放到Memcache，把GUID写到客户端cookie里面去</span>
<span style="color: rgba(0, 128, 128, 1)">23</span>                     <span style="color: rgba(0, 0, 255, 1)">string</span> userLoginId = Guid.NewGuid().ToString(); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">生成一个随机GUID
</span><span style="color: rgba(0, 128, 128, 1)">24</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">将用户的数据写入Memcache</span>
<span style="color: rgba(0, 128, 128, 1)">25</span>                     MemcacheHelper.AddCache(userLoginId, user_name, DateTime.Now.AddMinutes(<span style="color: rgba(128, 0, 128, 1)">20</span>)); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">Memcache帮助类
</span><span style="color: rgba(0, 128, 128, 1)">26</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">往客户端写入Cookie</span>
<span style="color: rgba(0, 128, 128, 1)">27</span>                     Response.Cookies[<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">userLoginId</span><span style="color: rgba(128, 0, 0, 1)">"</span>].Value= userLoginId; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">将GUID写入Cookie</span>
<span style="color: rgba(0, 128, 128, 1)">28</span>                     <span style="color: rgba(0, 0, 255, 1)">return</span> Content(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ok</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">29</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">30</span>                 <span style="color: rgba(0, 0, 255, 1)">else</span>
<span style="color: rgba(0, 128, 128, 1)">31</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">32</span>                     <span style="color: rgba(0, 0, 255, 1)">return</span> Content(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">用户名或密码错误！你会登陆吗？</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">33</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">34</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">35</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)">36</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">37</span>                 <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
</span><span style="color: rgba(0, 128, 128, 1)">38</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">39</span>         }            </pre>
