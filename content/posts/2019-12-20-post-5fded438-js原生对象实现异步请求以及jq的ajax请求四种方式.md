---
title: "JS原生对象实现异步请求以及JQ的ajax请求四种方式"
date: 2019-12-20
description: "一、JS原生方式异步请求 1 &lt;%@ Page Language=&quot;C#&quot; AutoEventWireup=&quot;true&quot; CodeBehind=&quot;AjaxLogin.aspx.cs&quot; Inherits=&quot;ThreeLayer"
tags:
  - "JavaScript"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11146404.html"
---

<h2>一、JS原生方式异步请求</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> &lt;%@ Page Language=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">C#</span><span style="color: rgba(128, 0, 0, 1)">"</span> AutoEventWireup=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">true</span><span style="color: rgba(128, 0, 0, 1)">"</span> CodeBehind=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">AjaxLogin.aspx.cs</span><span style="color: rgba(128, 0, 0, 1)">"</span> Inherits=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ThreeLayerWebDemo._2019_7_6.Ajax.AjaxLogin</span><span style="color: rgba(128, 0, 0, 1)">"</span> %&gt;
<span style="color: rgba(0, 128, 128, 1)"> 2</span> 
<span style="color: rgba(0, 128, 128, 1)"> 3</span> &lt;!DOCTYPE html&gt;
<span style="color: rgba(0, 128, 128, 1)"> 4</span> 
<span style="color: rgba(0, 128, 128, 1)"> 5</span> &lt;html xmlns=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">http://www.w3.org/1999/xhtml</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)"> 6</span> &lt;head runat=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">server</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)"> 7</span> &lt;meta http-equiv=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Content-Type</span><span style="color: rgba(128, 0, 0, 1)">"</span> content=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">text/html; charset=utf-8</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)"> 8</span>     &lt;title&gt;&lt;/title&gt;
<span style="color: rgba(0, 128, 128, 1)"> 9</span> &lt;/head&gt;
<span style="color: rgba(0, 128, 128, 1)">10</span> &lt;body&gt;
<span style="color: rgba(0, 128, 128, 1)">11</span>     &lt;form id=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">form1</span><span style="color: rgba(128, 0, 0, 1)">"</span> runat=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">server</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)">12</span>     &lt;div&gt;
<span style="color: rgba(0, 128, 128, 1)">13</span>     &lt;table&gt;
<span style="color: rgba(0, 128, 128, 1)">14</span>         &lt;tr&gt;
<span style="color: rgba(0, 128, 128, 1)">15</span>             &lt;td&gt;用户名:&lt;/td&gt;
<span style="color: rgba(0, 128, 128, 1)">16</span>             &lt;td&gt;
<span style="color: rgba(0, 128, 128, 1)">17</span>                 &lt;asp:TextBox ID=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">txtName</span><span style="color: rgba(128, 0, 0, 1)">"</span> runat=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">server</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;&lt;/asp:TextBox&gt;
<span style="color: rgba(0, 128, 128, 1)">18</span>             &lt;/td&gt;            
<span style="color: rgba(0, 128, 128, 1)">19</span>         &lt;/tr&gt;
<span style="color: rgba(0, 128, 128, 1)">20</span>         &lt;tr&gt;
<span style="color: rgba(0, 128, 128, 1)">21</span>             &lt;td&gt;密 码：&lt;/td&gt;
<span style="color: rgba(0, 128, 128, 1)">22</span>             &lt;td&gt;
<span style="color: rgba(0, 128, 128, 1)">23</span>                 &lt;asp:TextBox ID=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">txtPwd</span><span style="color: rgba(128, 0, 0, 1)">"</span> runat=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">server</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;&lt;/asp:TextBox&gt;
<span style="color: rgba(0, 128, 128, 1)">24</span>             &lt;/td&gt;            
<span style="color: rgba(0, 128, 128, 1)">25</span>         &lt;/tr&gt;
<span style="color: rgba(0, 128, 128, 1)">26</span>         &lt;tr&gt;
<span style="color: rgba(0, 128, 128, 1)">27</span>             &lt;td colspan=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">2</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)">28</span>                 &lt;input type=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">button</span><span style="color: rgba(128, 0, 0, 1)">"</span> value=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">提交</span><span style="color: rgba(128, 0, 0, 1)">"</span> id=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">btnLogin</span><span style="color: rgba(128, 0, 0, 1)">"</span>/&gt;
<span style="color: rgba(0, 128, 128, 1)">29</span>             &lt;/td&gt;
<span style="color: rgba(0, 128, 128, 1)">30</span>         &lt;/tr&gt;
<span style="color: rgba(0, 128, 128, 1)">31</span>     &lt;/table&gt;
<span style="color: rgba(0, 128, 128, 1)">32</span>     &lt;/div&gt;
<span style="color: rgba(0, 128, 128, 1)">33</span>     &lt;/form&gt;
<span style="color: rgba(0, 128, 128, 1)">34</span>     &lt;script type=<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">text/javascript</span><span style="color: rgba(128, 0, 0, 1)">"</span>&gt;
<span style="color: rgba(0, 128, 128, 1)">35</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> btn = document.getElementById(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">btnLogin</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">36</span>         btn.onclick =<span style="color: rgba(0, 0, 0, 1)"> function () {
</span><span style="color: rgba(0, 128, 128, 1)">37</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> txtName = document.getElementById(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">txtName</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">38</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> txtPwd = document.getElementById(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">txtPwd</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">39</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> strUrl = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ProcessLogin.aspx?name=</span><span style="color: rgba(128, 0, 0, 1)">"</span> + txtName.value + <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">&amp;pwd=</span><span style="color: rgba(128, 0, 0, 1)">"</span> +<span style="color: rgba(0, 0, 0, 1)"> txtPwd.value;
</span><span style="color: rgba(0, 128, 128, 1)">40</span>             myAjax(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">get</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">, strUrl, function (data) {
</span><span style="color: rgba(0, 128, 128, 1)">41</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (data == <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ok</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">42</span>                     window.location.href = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">../../2019-6-29/CRUD/MainFrame.aspx</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">43</span>                 } <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)">44</span> <span style="color: rgba(0, 0, 0, 1)">                    alert(data);
</span><span style="color: rgba(0, 128, 128, 1)">45</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">46</span> <span style="color: rgba(0, 0, 0, 1)">            });
</span><span style="color: rgba(0, 128, 128, 1)">47</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)">48</span> <span style="color: rgba(0, 0, 0, 1)">        function myAjax(httpMethod,url,callback){
</span><span style="color: rgba(0, 128, 128, 1)">49</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">发送异步请求</span>
<span style="color: rgba(0, 128, 128, 1)">50</span>             <span style="color: rgba(0, 0, 255, 1)">var</span><span style="color: rgba(0, 0, 0, 1)"> xhr;
</span><span style="color: rgba(0, 128, 128, 1)">51</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (XMLHttpRequest) {
</span><span style="color: rgba(0, 128, 128, 1)">52</span>                 xhr = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> XMLHttpRequest();
</span><span style="color: rgba(0, 128, 128, 1)">53</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">54</span>             <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)">55</span>                 xhr = <span style="color: rgba(0, 0, 255, 1)">new</span> ActiveXObject(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Microsoft.XMLHTTP</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">56</span> <span style="color: rgba(0, 0, 0, 1)">            };            
</span><span style="color: rgba(0, 128, 128, 1)">57</span>             xhr.open(httpMethod, url, <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">58</span> <span style="color: rgba(0, 0, 0, 1)">            xhr.send();
</span><span style="color: rgba(0, 128, 128, 1)">59</span>             xhr.onreadystatechange =<span style="color: rgba(0, 0, 0, 1)"> function () {
</span><span style="color: rgba(0, 128, 128, 1)">60</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (xhr.readyState == <span style="color: rgba(128, 0, 128, 1)">4</span> &amp;&amp; xhr.status == <span style="color: rgba(128, 0, 128, 1)">200</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">61</span> <span style="color: rgba(0, 0, 0, 1)">                    callback(xhr.responseText);
</span><span style="color: rgba(0, 128, 128, 1)">62</span> <span style="color: rgba(0, 0, 0, 1)">                }                
</span><span style="color: rgba(0, 128, 128, 1)">63</span> <span style="color: rgba(0, 0, 0, 1)">            };
</span><span style="color: rgba(0, 128, 128, 1)">64</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">65</span>     &lt;/script&gt;
<span style="color: rgba(0, 128, 128, 1)">66</span> &lt;/body&gt;
<span style="color: rgba(0, 128, 128, 1)">67</span> &lt;/html&gt;</pre>
