---
title: "jQuery Validate表单校验"
date: 2023-05-31
description: "jQuery plugin: Validation 使用说明 学习链接及下载地址：http://www.runoob.com/jquery/jquery-plugin-validate.html 一导入js库&lt;script src=&quot;../js/jquery.js&quot; typ"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11269444.html"
---

<p><strong>jQuery plugin: Validation 使用说明</strong>&nbsp;&nbsp;</p>
<p>学习链接及下载地址：http://www.runoob.com/jquery/jquery-plugin-validate.html</p>
<p><strong>一导入js库</strong><br>&lt;script src="../js/jquery.js" type="text/javascript"&gt;&lt;/script&gt;<br>&lt;script src="../js/jquery.validate.js" type="text/javascript"&gt;&lt;/script&gt;</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190730131150209-776689686.png" alt="" /></p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201907/1504448-20190730131205700-1742256952.png" alt="" /></p>
<h2>默认提示</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)">messages: {
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">    required: "This field is required.",
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 0, 1)">    remote: "Please fix this field.",
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">    email: "Please enter a valid email address.",
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 0, 1)">    url: "Please enter a valid URL.",
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">    date: "Please enter a valid date.",
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 0, 1)">    dateISO: "Please enter a valid date ( ISO ).",
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">    number: "Please enter a valid number.",
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">    digits: "Please enter only digits.",
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">    creditcard: "Please enter a valid credit card number.",
</span><span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">    equalTo: "Please enter the same value again.",
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">    maxlength: $.validator.format( "Please enter no more than {0} characters." ),
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">    minlength: $.validator.format( "Please enter at least {0} characters." ),
</span><span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 0, 1)">    rangelength: $.validator.format( "Please enter a value between {0} and {1} characters long." ),
</span><span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 0, 1)">    range: $.validator.format( "Please enter a value between {0} and {1}." ),
</span><span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 0, 1)">    max: $.validator.format( "Please enter a value less than or equal to {0}." ),
</span><span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 0, 1)">    min: $.validator.format( "Please enter a value greater than or equal to {0}." )
</span><span style="color: rgba(0, 128, 128, 1)">18</span> }</pre>
