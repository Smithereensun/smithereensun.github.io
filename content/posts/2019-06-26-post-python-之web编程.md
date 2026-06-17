---
title: "Python 之Web编程"
date: 2019-06-26
description: "一 、HTML是什么？ htyper text markup language 即超文本标记语言 超文本:就是指页面内可以包含图片、链接、甚至音乐、程序等非文字元素 标记语言：标记(标签)构成的语言 静态网页：静态的资源，如xxx.html 动态网页：html代码是由某种开发语言根据用户请求动态生成"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10454503.html"
---

<h1>一 、HTML是什么？</h1>
<p>　　htyper text markup language 即超文本标记语言</p>
<p>　　超文本:就是指页面内可以包含图片、链接、甚至音乐、程序等非文字元素</p>
<p>　　标记语言：标记(标签)构成的语言</p>
<p>　　静态网页：静态的资源，如xxx.html</p>
<p>　　动态网页：html代码是由某种开发语言根据用户请求动态生成</p>
<p>　　html文档树结构图：</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201903/1504448-20190301090523091-1933826453.png" alt="" /></p>
<h1>二 、 什么是标签？</h1>
<p>　　- 由一对尖括号包裹的单词构成，如&lt;html&gt; 所有标签中的单词不可能从数据开头</p>
<p>　　- 标签不区分大小写&lt;html&gt;和&lt;HTML&gt;，建议使用小写</p>
<p>　　- 标签分两部分：开始标签&lt;a&gt;和结束标签&lt;/a&gt;，两个标签之间的部分，叫标签体</p>
<p>　　- 有些标签功能比较简单，使用一个标签即可，这种标签叫做自闭合标签，如：&lt;br/&gt;、&lt;hr/&gt;、&lt;input/&gt;、&lt;img/&gt;</p>
<p>　　- 标签可以嵌套，但不能交叉嵌套。如:&lt;a&gt;&lt;b&gt;&lt;/a&gt;&lt;/b&gt;</p>
<h1>三 、 标签的属性</h1>
<p>　　- 通常是以键值对形式出现的，例如 name="alex"</p>
<p>　　- 属性只能出现在开始标签 或 自闭合标签中</p>
<p>　　- 属性名字全部小写，属性值必须使用双引号或单引号包裹，如:name="alex"</p>
<p>　　- 如果属性值和属性名完全一样，直接写属性名即可，如:readonly</p>
<h2>&nbsp;1、&lt;head&gt;标签</h2>
<p><span style="color: rgba(0, 0, 255, 1)"><strong>&lt;meta&gt;</strong></span></p>
<p>　　meta标签的组成：meta标签共有两个属性，分别是http-equiv属性和name属性，不同的属性又有不同的参数值，这些不同的参数值就实现不同的网页功能</p>
<p>　　1：name属性主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息和分类信息用的</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">1</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">meta </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="keywords"</span><span style="color: rgba(255, 0, 0, 1)"> content</span><span style="color: rgba(0, 0, 255, 1)">="meta总结"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">2</span>     <span style="color: rgba(0, 0, 255, 1)">&lt;</span><span style="color: rgba(128, 0, 0, 1)">meta </span><span style="color: rgba(255, 0, 0, 1)">name</span><span style="color: rgba(0, 0, 255, 1)">="description"</span><span style="color: rgba(255, 0, 0, 1)"> content</span><span style="color: rgba(0, 0, 255, 1)">="alex是一个中国人"</span><span style="color: rgba(0, 0, 255, 1)">&gt;</span></pre>
