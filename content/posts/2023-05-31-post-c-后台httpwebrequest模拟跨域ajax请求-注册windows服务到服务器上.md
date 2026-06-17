---
title: "C#后台HttpWebRequest模拟跨域Ajax请求，注册Windows服务到服务器上"
date: 2023-05-31
description: "项目需求，暂且叫A、B公司吧。我们公司需要从A公司哪里读取机器上的数据，放到我们数据库中。然后再将数据库中存的数据，提供一个接口，B公司来调用，大概这个意思。 好了，言归正传。这个是之前做好的界面，用户需要手动点击“开始”，然后写了个定时器，不停的来回调用 部分源码(5秒调用后台处理) 1 func"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11231024.html"
---

<p><span style="font-family: &quot;Microsoft YaHei&quot;">　　项目需求，暂且叫A、B公司吧。我们公司需要从A公司哪里读取机器上的数据，放到我们数据库中。然后再将数据库中存的数据，提供一个接口，B公司来调用，大概这个意思。</span></p>
<p><span style="font-family: &quot;Microsoft YaHei&quot;">　　好了，言归正传。这个是之前做好的界面，用户需要手动点击“开始”，然后写了个定时器，不停的来回调用</span></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190723104604397-171255655.png" alt="" /></p>
<p><span style="color: rgba(255, 0, 255, 1); font-family: &quot;Microsoft YaHei&quot;"><strong>　　部分源码(5秒调用后台处理)</strong></span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)">    function refreshCount() {
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">        if (prj.is_port_state_1 == false) {
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 0, 1)">            var grid_down = query_panel.grid_down;
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">            var RequestData = { "macName": "" };
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 0, 1)">            $.ajax({
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">                url: "http://172.30.16.254:8080/IWFM_HuaLian/dataDock/getMacState",
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 0, 1)">                type: 'POST',
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">                dataType: "JSON",
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">                contentType: 'application/json; charset=UTF-8',
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">                crossDomain: true,
</span><span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">                data: JSON.stringify(RequestData),
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">                xhrFields: {
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">                    'Access-Control-Allow-Origin': '*'
</span><span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 0, 1)">                },
</span><span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 0, 1)">                success: function (resData) {
</span><span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 0, 1)">                    var res = JSON.stringify(resData);
</span><span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 0, 1)">                    Ext.Ajax.request({
</span><span style="color: rgba(0, 128, 128, 1)">18</span> <span style="color: rgba(0, 0, 0, 1)">                        url: "WC030Handlers.csx",
</span><span style="color: rgba(0, 128, 128, 1)">19</span> <span style="color: rgba(0, 0, 0, 1)">                        params: {
</span><span style="color: rgba(0, 128, 128, 1)">20</span> <span style="color: rgba(0, 0, 0, 1)">                            tag: 'GetMacState',
</span><span style="color: rgba(0, 128, 128, 1)">21</span> <span style="color: rgba(0, 0, 0, 1)">                            data: res
</span><span style="color: rgba(0, 128, 128, 1)">22</span> <span style="color: rgba(0, 0, 0, 1)">                        },
</span><span style="color: rgba(0, 128, 128, 1)">23</span> <span style="color: rgba(0, 0, 0, 1)">                        success: function (response, p) {
</span><span style="color: rgba(0, 128, 128, 1)">24</span> <span style="color: rgba(0, 0, 0, 1)">                            grid_down.getStore().load();
</span><span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">                        }
</span><span style="color: rgba(0, 128, 128, 1)">26</span> <span style="color: rgba(0, 0, 0, 1)">                    });
</span><span style="color: rgba(0, 128, 128, 1)">27</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">28</span> <span style="color: rgba(0, 0, 0, 1)">            });
</span><span style="color: rgba(0, 128, 128, 1)">29</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">30</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">31</span> 
<span style="color: rgba(0, 128, 128, 1)">32</span> <span style="color: rgba(0, 0, 0, 1)">    Ext.Msg.alert(MsgMrg.OptMsg, "开始运行！");
</span><span style="color: rgba(0, 128, 128, 1)">33</span>     t1 = window.setInterval(refreshCount, 5000);</pre>
