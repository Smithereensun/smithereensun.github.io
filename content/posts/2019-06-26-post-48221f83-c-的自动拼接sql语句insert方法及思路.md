---
title: "C#的自动拼接Sql语句Insert方法及思路"
date: 2019-06-26
description: "思路： 1、想想插入语句，大概是这样的一个框架:INSERT INTO 表名 (数据库列名) values (值) 2、这里要3个变量是不固定的，分别是：表名、数据库列名、值； a.表名我们这里很容易可以获取到 b.数据库列名，我们可以遍历容器获取控件的Name属性 c.值，我们可以遍历容器获取控件"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10201465.html"
---

<p>思路：</p>
<p>　　1、想想插入语句，大概是这样的一个框架:INSERT INTO 表名 (数据库列名) values (值)</p>
<p>　　2、这里要3个变量是不固定的，分别是：表名、数据库列名、值；</p>
<p>　　　　a.表名我们这里很容易可以获取到</p>
<p>　　　　b.数据库列名，我们可以遍历容器获取控件的Name属性</p>
<p>　　　　c.值，我们可以遍历容器获取控件的Text属性</p>
<div class="cnblogs_code"><img id="code_img_closed_c9102796-a9de-4a8e-a635-8419ccbb624d" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_c9102796-a9de-4a8e-a635-8419ccbb624d" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_c9102796-a9de-4a8e-a635-8419ccbb624d" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">static</span> Dictionary&lt;<span style="color: rgba(0, 0, 255, 1)">string</span>, <span style="color: rgba(0, 0, 255, 1)">string</span>&gt;<span style="color: rgba(0, 0, 0, 1)"> GetDicKeyValue(Control controlBox)
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">遍历容器获取控件的Name属性和Text属性，存放到键值中，用于以下的拼接sql</span>
<span style="color: rgba(0, 128, 128, 1)"> 4</span>             Dictionary&lt;<span style="color: rgba(0, 0, 255, 1)">string</span>, <span style="color: rgba(0, 0, 255, 1)">string</span>&gt; dic = <span style="color: rgba(0, 0, 255, 1)">new</span> Dictionary&lt;<span style="color: rgba(0, 0, 255, 1)">string</span>, <span style="color: rgba(0, 0, 255, 1)">string</span>&gt;<span style="color: rgba(0, 0, 0, 1)">();
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>             <span style="color: rgba(0, 0, 255, 1)">foreach</span> (Control item <span style="color: rgba(0, 0, 255, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> controlBox.Controls)
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (item <span style="color: rgba(0, 0, 255, 1)">is</span> Label || item <span style="color: rgba(0, 0, 255, 1)">is</span><span style="color: rgba(0, 0, 0, 1)"> PictureBox)
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>                     <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">11</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (item <span style="color: rgba(0, 0, 255, 1)">is</span><span style="color: rgba(0, 0, 0, 1)"> TextBox)
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">13</span>                     dic.Add(item.Name.Substring(<span style="color: rgba(128, 0, 128, 1)">3</span>, item.Name.Length - <span style="color: rgba(128, 0, 128, 1)">3</span><span style="color: rgba(0, 0, 0, 1)">), item.Text.Trim());
</span><span style="color: rgba(0, 128, 128, 1)">14</span>                     <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">16</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (item <span style="color: rgba(0, 0, 255, 1)">is</span><span style="color: rgba(0, 0, 0, 1)"> ComboBox)
</span><span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">18</span>                     dic.Add(item.Name.Substring(<span style="color: rgba(128, 0, 128, 1)">3</span>, item.Name.Length - <span style="color: rgba(128, 0, 128, 1)">3</span><span style="color: rgba(0, 0, 0, 1)">), item.Text);
</span><span style="color: rgba(0, 128, 128, 1)">19</span>                     <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">20</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">21</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (item <span style="color: rgba(0, 0, 255, 1)">is</span><span style="color: rgba(0, 0, 0, 1)"> DateTimePicker)
</span><span style="color: rgba(0, 128, 128, 1)">22</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">23</span>                     dic.Add(item.Name.Substring(<span style="color: rgba(128, 0, 128, 1)">3</span>, item.Name.Length - <span style="color: rgba(128, 0, 128, 1)">3</span><span style="color: rgba(0, 0, 0, 1)">), item.Text);
</span><span style="color: rgba(0, 128, 128, 1)">24</span>                     <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">26</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (item <span style="color: rgba(0, 0, 255, 1)">is</span><span style="color: rgba(0, 0, 0, 1)"> CheckBox)
</span><span style="color: rgba(0, 128, 128, 1)">27</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">28</span>                     <span style="color: rgba(0, 0, 255, 1)">string</span> result = ((CheckBox)item).Checked ? <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">1</span><span style="color: rgba(128, 0, 0, 1)">"</span> : <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">0</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">29</span>                     dic.Add(item.Name.Substring(<span style="color: rgba(128, 0, 128, 1)">3</span>, item.Name.Length - <span style="color: rgba(128, 0, 128, 1)">3</span><span style="color: rgba(0, 0, 0, 1)">), result);
</span><span style="color: rgba(0, 128, 128, 1)">30</span>                     <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">31</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">32</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">33</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> dic;
</span><span style="color: rgba(0, 128, 128, 1)">34</span>         }</pre>
