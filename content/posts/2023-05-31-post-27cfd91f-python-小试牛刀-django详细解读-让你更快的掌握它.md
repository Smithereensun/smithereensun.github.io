---
title: "Python 小试牛刀，Django详细解读，让你更快的掌握它！！！"
date: 2023-05-31
description: "一、MVC和MTV模式 MVC：将web应用分为模型(M)，控制器(C)，视图(V)三层；他们之间以一种插件似的，松耦合的方式连接在一起。 模型负责业务对象与数据库的对象(ORM)，视图负责与用户的交互(页面)，控制器(C)接受用户的输入调用模型和视图完成用户的请求。 Django的MTV模型本质上"
tags:
  - "Django"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10514121.html"
---

<h1>一、MVC和MTV模式</h1>
<p>MVC：将web应用分为模型(M)，控制器(C)，视图(V)三层；他们之间以一种插件似的，松耦合的方式连接在一起。</p>
<p>模型负责业务对象与数据库的对象(ORM)，视图负责与用户的交互(页面)，控制器(C)接受用户的输入调用模型和视图完成用户的请求。</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201903/1504448-20190311235812685-1728066385.png" alt="" /></p>
<p>Django的MTV模型本质上与MVC没有什么差别，也是各组件之间为了保持松耦合关系，只不过定义上有些不同，Django的MTV分别是：</p>
<p>　　• Model(模型)：负责业务对象与数据库的对象(ORM)</p>
<p>　　• Template(模板)：负责如何把页面展示给用户</p>
<p>　　• View(视图)：负责业务逻辑，并在适当的时候调用Model和Template</p>
<p>&nbsp;<img src="https://img2018.cnblogs.com/blog/1504448/201903/1504448-20190312001859096-1808767348.png" alt="" /></p>
<h1>二 Django的流程和命令行工具</h1>
<div class="cnblogs_code"><img id="code_img_closed_c53189ae-23fd-4e35-be7c-22e78e86ac56" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_c53189ae-23fd-4e35-be7c-22e78e86ac56" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_c53189ae-23fd-4e35-be7c-22e78e86ac56" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)">django
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span>     <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">安装： pip3 install django</span>
<span style="color: rgba(0, 128, 128, 1)"> 3</span> 
<span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">          添加环境变量
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> 
<span style="color: rgba(0, 128, 128, 1)"> 6</span>     <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">1  创建project</span>
<span style="color: rgba(0, 128, 128, 1)"> 7</span>        django-<span style="color: rgba(0, 0, 0, 1)">admin startproject mysite
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> 
<span style="color: rgba(0, 128, 128, 1)"> 9</span>        ---<span style="color: rgba(0, 0, 0, 1)">mysite
</span><span style="color: rgba(0, 128, 128, 1)">10</span> 
<span style="color: rgba(0, 128, 128, 1)">11</span>           ---<span style="color: rgba(0, 0, 0, 1)">settings.py
</span><span style="color: rgba(0, 128, 128, 1)">12</span>           ---<span style="color: rgba(0, 0, 0, 1)">url.py
</span><span style="color: rgba(0, 128, 128, 1)">13</span>           ---<span style="color: rgba(0, 0, 0, 1)">wsgi.py
</span><span style="color: rgba(0, 128, 128, 1)">14</span> 
<span style="color: rgba(0, 128, 128, 1)">15</span>        ----<span style="color: rgba(0, 0, 0, 1)"> manage.py(启动文件)  
</span><span style="color: rgba(0, 128, 128, 1)">16</span> 
<span style="color: rgba(0, 128, 128, 1)">17</span>     <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">2  创建APP       </span>
<span style="color: rgba(0, 128, 128, 1)">18</span> <span style="color: rgba(0, 0, 0, 1)">       python mannage.py startapp  app01
</span><span style="color: rgba(0, 128, 128, 1)">19</span> 
<span style="color: rgba(0, 128, 128, 1)">20</span>     <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">3  settings配置</span>
<span style="color: rgba(0, 128, 128, 1)">21</span>     
<span style="color: rgba(0, 128, 128, 1)">22</span> <span style="color: rgba(0, 0, 0, 1)">       TEMPLATES
</span><span style="color: rgba(0, 128, 128, 1)">23</span> 
<span style="color: rgba(0, 128, 128, 1)">24</span>        STATICFILES_DIRS=<span style="color: rgba(0, 0, 0, 1)">(
</span><span style="color: rgba(0, 128, 128, 1)">25</span>             os.path.join(BASE_DIR,<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">statics</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">),
</span><span style="color: rgba(0, 128, 128, 1)">26</span> <span style="color: rgba(0, 0, 0, 1)">        )
</span><span style="color: rgba(0, 128, 128, 1)">27</span> 
<span style="color: rgba(0, 128, 128, 1)">28</span>        STATIC_URL = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">/static/</span><span style="color: rgba(128, 0, 0, 1)">'</span> 
<span style="color: rgba(0, 128, 128, 1)">29</span>        <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">  我们只能用 STATIC_URL，但STATIC_URL会按着你的STATICFILES_DIRS去找#4  根据需求设计代码</span>
<span style="color: rgba(0, 128, 128, 1)">30</span> <span style="color: rgba(0, 0, 0, 1)">           url.py
</span><span style="color: rgba(0, 128, 128, 1)">31</span> <span style="color: rgba(0, 0, 0, 1)">           view.py
</span><span style="color: rgba(0, 128, 128, 1)">32</span> 
<span style="color: rgba(0, 128, 128, 1)">33</span>     <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">5  使用模版</span>
<span style="color: rgba(0, 128, 128, 1)">34</span>        render(req,<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">index.html</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">)   
</span><span style="color: rgba(0, 128, 128, 1)">35</span> 
<span style="color: rgba(0, 128, 128, 1)">36</span>     <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">6  启动项目</span>
<span style="color: rgba(0, 128, 128, 1)">37</span>        python manage.py runserver  127.0.0.1:8090
<span style="color: rgba(0, 128, 128, 1)">38</span> 
<span style="color: rgba(0, 128, 128, 1)">39</span>     <span style="color: rgba(0, 128, 0, 1)">#</span><span style="color: rgba(0, 128, 0, 1)">7  连接数据库，操作数据</span>
<span style="color: rgba(0, 128, 128, 1)">40</span>        model.py</pre>
