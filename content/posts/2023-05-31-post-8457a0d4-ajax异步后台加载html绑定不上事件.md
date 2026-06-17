---
title: "Ajax异步后台加载Html绑定不上事件"
date: 2023-05-31
description: "因项目需要，需要实时从后台动态加载html，开发过程中，遇到事件绑定不上，后来百度一番，大概意思：ajax是异步加载的，页面一开始绑定事件的时候，后台数据还没有传过来，就绑定事件，这个时候找不到这个document元素，所以就绑定不上。 解决方法： 1 $(document).on(&quot;cl"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11268325.html"
---

<h4><span style="font-family: &quot;Microsoft YaHei&quot;">　　因项目需要，需要实时从后台动态加载html，开发过程中，遇到事件绑定不上，后来百度一番，大概意思：ajax是异步加载的，页面一开始绑定事件的时候，后台数据还没有传过来，就绑定事件，这个时候找不到这个document元素，所以就绑定不上。</span></h4>
<h4><span style="font-family: &quot;Microsoft YaHei&quot;">　　解决方法：</span></h4>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)">        $(document).on("click", "div[btn-click]", function () {
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">            debugger;
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 0, 1)">            var strFunc = $(this).attr("btn-click"); //获取当前点击标签、扩展属性的函数名
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">            var strId = $(this).attr("id"); //获取点击标签的Id值
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 0, 1)">            eval(strFunc + "(" + strId + ")"); //调用eval()方法，执行该方法，并传入一个参数:Id
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">        })
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> 
<span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">        function afterClick(id) {
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">            alert(id);
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">            $("#txtMAC_CODE").val("1");
</span><span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">            debugger;
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">13</span> 
<span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(255, 0, 0, 1)"><strong>格式:$(document).on(事件类型, 绑定Dom元素, function () {})</strong></span></pre>
