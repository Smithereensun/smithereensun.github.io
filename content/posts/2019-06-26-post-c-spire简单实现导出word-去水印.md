---
title: "C# Spire简单实现导出word(去水印)"
date: 2019-06-26
description: "今天老姐打电话，说：下个月一号要换到其他岗位上，到时需要对word操作，小弟我随口答应，这个简单，我给你开发一款小程序，你直接在我程序上录入一些数据，我给你导出到word中。 利用中午空闲时间，百度了一番，发现导出word都是大同小异，npoi,spire等。 原理：利用“word标签”进行替换操作"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11044735.html"
---

<p><span style="font-family: 楷体">　　今天老姐打电话，说：下个月一号要换到其他岗位上，到时需要对word操作，小弟我随口答应，这个简单，我给你开发一款小程序，你直接在我程序上录入一些数据，我给你导出到word中。</span></p>
<p><span style="font-family: 楷体">　　利用中午空闲时间，百度了一番，发现导出word都是大同小异，npoi,spire等。</span></p>
<p><span style="font-family: 楷体">　　原理：利用“word标签”进行替换操作。</span></p>
<p><span style="font-family: 楷体">　　在这里，我们使用<span style="color: rgba(255, 0, 0, 1)"><strong>Spire方法</strong></span>对<span style="color: rgba(255, 0, 0, 1)"><strong>word</strong></span>进行<span style="color: rgba(255, 0, 0, 1)"><strong>操作</strong></span>，百度上大多数下载的类库，导出时都是<strong><span style="color: rgba(255, 0, 0, 1)">有水印</span></strong>的，特意整理了一份<strong><span style="color: rgba(255, 0, 0, 1)">没有水印</span></strong>的<span style="color: rgba(255, 0, 0, 1)"><strong>类库</strong></span>，有需要的宝宝们，请<span style="color: rgba(255, 0, 0, 1)"><strong>自行下载</strong></span>。</span></p>
<p><span style="font-family: 楷体">链接：https://pan.baidu.com/s/1YGefiu6RbLQryJJOv2LI0A </span><br><span style="font-family: 楷体">提取码：0lkk </span></p>
<p><span style="font-family: 楷体">　　废话不多说，直接上代码，有不懂的宝宝们，欢迎下方留言~</span></p>
<h2><span style="font-family: 楷体">word导出模板：</span></h2>
<p><span style="font-family: 楷体"><img src="https://img2018.cnblogs.com/blog/1504448/201906/1504448-20190618133400982-315928194.png" alt="" /></span></p>
<h2>第一步：需引用百度云盘上的4个类，不会的添加外部类库的，请自行百度</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201906/1504448-20190618133702620-140249863.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201906/1504448-20190618133729629-261665194.png" alt="" /></p>
<h2>代码：</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> Spire.Doc;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Collections.Generic;
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.ComponentModel;
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Data;
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Drawing;
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Linq;
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Text;
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Threading.Tasks;
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Windows.Forms;
</span><span style="color: rgba(0, 128, 128, 1)">11</span> 
<span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> app01
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)">14</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">partial</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> Form1 : Form
</span><span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)">16</span>         <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Form1()
</span><span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">18</span> <span style="color: rgba(0, 0, 0, 1)">            InitializeComponent();
</span><span style="color: rgba(0, 128, 128, 1)">19</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">20</span> 
<span style="color: rgba(0, 128, 128, 1)">21</span>         <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> button1_Click(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> sender, EventArgs e)
</span><span style="color: rgba(0, 128, 128, 1)">22</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">23</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">1、需引用命名空间using Spire.Doc;</span>
<span style="color: rgba(0, 128, 128, 1)">24</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> doc = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> Document();
</span><span style="color: rgba(0, 128, 128, 1)">25</span>             <span style="color: rgba(0, 0, 255, 1)">string</span> templatePath = <span style="color: rgba(128, 0, 0, 1)">@"</span><span style="color: rgba(128, 0, 0, 1)">F:\test\app01\老乐山景区团队预定.docx</span><span style="color: rgba(128, 0, 0, 1)">"</span>; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">模板路径</span>
<span style="color: rgba(0, 128, 128, 1)">26</span>             doc.LoadFromFile(templatePath); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">加载模板路径</span>
<span style="color: rgba(0, 128, 128, 1)">27</span>             doc.Replace(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">$[form]$</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">测试</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(0, 0, 255, 1)">true</span>, <span style="color: rgba(0, 0, 255, 1)">true</span>); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第一个参数：模板的占位符；第二个参数：替换的内容；第三个参数：是否区分大小写；第四个参数：是否全字匹配</span>
<span style="color: rgba(0, 128, 128, 1)">28</span>             <span style="color: rgba(0, 0, 255, 1)">string</span> savePath = <span style="color: rgba(128, 0, 0, 1)">@"</span><span style="color: rgba(128, 0, 0, 1)">F:\老乐山景区.docx</span><span style="color: rgba(128, 0, 0, 1)">"</span>; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">导出路径</span>
<span style="color: rgba(0, 128, 128, 1)">29</span> <span style="color: rgba(0, 0, 0, 1)">            doc.SaveToFile(savePath, FileFormat.Docx);
</span><span style="color: rgba(0, 128, 128, 1)">30</span> <span style="color: rgba(0, 0, 0, 1)">            doc.Close();
</span><span style="color: rgba(0, 128, 128, 1)">31</span>             MessageBox.Show(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">导出成功</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">32</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">33</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">34</span> }</pre>
