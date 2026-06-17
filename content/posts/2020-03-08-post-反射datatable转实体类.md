---
title: "反射DataTable转实体类"
date: 2020-03-08
description: "1 using System; 2 using System.Collections.Generic; 3 using System.Data; 4 using System.Reflection; 5 6 namespace Dll 7 { 8 public static class ToEnti"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11123685.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)">using System;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 0, 1)">using System.Collections.Generic;
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 0, 1)">using System.Data;
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">using System.Reflection;
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> 
<span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">namespace Dll
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span>     <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> static class ToEntity
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)">10</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;</span>summary<span style="color: rgba(128, 128, 128, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">11</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 0, 0, 1)"> 将DataTable转换成实体类
</span><span style="color: rgba(0, 128, 128, 1)">12</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/</span>summary<span style="color: rgba(128, 128, 128, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">13</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;</span>typeparam name<span style="color: rgba(128, 128, 128, 1)">=</span>"T"<span style="color: rgba(128, 128, 128, 1)">&gt;</span>实体类<span style="color: rgba(128, 128, 128, 1)">&lt;/</span>typeparam<span style="color: rgba(128, 128, 128, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">14</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;</span>param name<span style="color: rgba(128, 128, 128, 1)">=</span>"dt"<span style="color: rgba(128, 128, 128, 1)">&gt;</span>DataTable<span style="color: rgba(128, 128, 128, 1)">&lt;/</span>param<span style="color: rgba(128, 128, 128, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">15</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;</span><span style="color: rgba(0, 0, 255, 1)">returns</span><span style="color: rgba(128, 128, 128, 1)">&gt;&lt;/</span><span style="color: rgba(0, 0, 255, 1)">returns</span><span style="color: rgba(128, 128, 128, 1)">&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">16</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> static List<span style="color: rgba(128, 128, 128, 1)">&lt;</span>T<span style="color: rgba(128, 128, 128, 1)">&gt;</span> DtConvertToModel<span style="color: rgba(128, 128, 128, 1)">&lt;</span>T<span style="color: rgba(128, 128, 128, 1)">&gt;</span>(DataTable dt) <span style="color: rgba(0, 0, 255, 1)">where</span><span style="color: rgba(0, 0, 0, 1)"> T:new()
</span><span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">18</span>             List<span style="color: rgba(128, 128, 128, 1)">&lt;</span>T<span style="color: rgba(128, 128, 128, 1)">&gt;</span> ts <span style="color: rgba(128, 128, 128, 1)">=</span> new List<span style="color: rgba(128, 128, 128, 1)">&lt;</span>T<span style="color: rgba(128, 128, 128, 1)">&gt;</span><span style="color: rgba(0, 0, 0, 1)">();
</span><span style="color: rgba(0, 128, 128, 1)">19</span>             foreach (DataRow dr <span style="color: rgba(128, 128, 128, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> dt.Rows)
</span><span style="color: rgba(0, 128, 128, 1)">20</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">21</span>                 T t <span style="color: rgba(128, 128, 128, 1)">=</span><span style="color: rgba(0, 0, 0, 1)"> new T();
</span><span style="color: rgba(0, 128, 128, 1)">22</span>                 foreach (PropertyInfo <span style="color: rgba(255, 0, 255, 1)">pi</span> <span style="color: rgba(128, 128, 128, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> t.GetType().GetProperties())
</span><span style="color: rgba(0, 128, 128, 1)">23</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">24</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span> (dt.Columns.<span style="color: rgba(0, 0, 255, 1)">Contains</span>(<span style="color: rgba(255, 0, 255, 1)">pi</span><span style="color: rgba(0, 0, 0, 1)">.Name))
</span><span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">                    {
</span><span style="color: rgba(0, 128, 128, 1)">26</span>                         <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(255, 0, 255, 1)">pi</span>.CanWrite) <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">27</span>                         <span style="color: rgba(255, 0, 255, 1)">var</span> value <span style="color: rgba(128, 128, 128, 1)">=</span> dr<span style="color: rgba(255, 0, 0, 1)">[</span><span style="color: rgba(255, 0, 0, 1)">pi.Name</span><span style="color: rgba(255, 0, 0, 1)">]</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">28</span>                         <span style="color: rgba(0, 0, 255, 1)">if</span> (value<span style="color: rgba(128, 128, 128, 1)">!=</span><span style="color: rgba(0, 0, 0, 1)"> DBNull.Value)
</span><span style="color: rgba(0, 128, 128, 1)">29</span> <span style="color: rgba(0, 0, 0, 1)">                        {
</span><span style="color: rgba(0, 128, 128, 1)">30</span>                             switch (<span style="color: rgba(255, 0, 255, 1)">pi</span><span style="color: rgba(0, 0, 0, 1)">.PropertyType.FullName)
</span><span style="color: rgba(0, 128, 128, 1)">31</span> <span style="color: rgba(0, 0, 0, 1)">                            {
</span><span style="color: rgba(0, 128, 128, 1)">32</span>                                 <span style="color: rgba(255, 0, 255, 1)">case</span> "System.<span style="color: rgba(0, 0, 255, 1)">Decimal</span><span style="color: rgba(0, 0, 0, 1)">":
</span><span style="color: rgba(0, 128, 128, 1)">33</span>                                     <span style="color: rgba(255, 0, 255, 1)">pi</span>.SetValue(t, <span style="color: rgba(0, 0, 255, 1)">decimal</span>.Parse(value.ToString()), <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">34</span>                                     <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">35</span>                                 <span style="color: rgba(255, 0, 255, 1)">case</span><span style="color: rgba(0, 0, 0, 1)"> "System.String":
</span><span style="color: rgba(0, 128, 128, 1)">36</span>                                     <span style="color: rgba(255, 0, 255, 1)">pi</span>.SetValue(t, value.ToString(), <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">37</span>                                     <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">38</span>                                 <span style="color: rgba(255, 0, 255, 1)">case</span><span style="color: rgba(0, 0, 0, 1)"> "System.Int32":
</span><span style="color: rgba(0, 128, 128, 1)">39</span>                                     <span style="color: rgba(255, 0, 255, 1)">pi</span>.SetValue(t, <span style="color: rgba(0, 0, 255, 1)">int</span>.Parse(value.ToString()), <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">40</span>                                     <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">41</span>                                 <span style="color: rgba(0, 0, 255, 1)">default</span><span style="color: rgba(0, 0, 0, 1)">:
</span><span style="color: rgba(0, 128, 128, 1)">42</span>                                     <span style="color: rgba(255, 0, 255, 1)">pi</span>.SetValue(t, value, <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">43</span>                                     <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">44</span> <span style="color: rgba(0, 0, 0, 1)">                            }
</span><span style="color: rgba(0, 128, 128, 1)">45</span> <span style="color: rgba(0, 0, 0, 1)">                        }
</span><span style="color: rgba(0, 128, 128, 1)">46</span> <span style="color: rgba(0, 0, 0, 1)">                    }                    
</span><span style="color: rgba(0, 128, 128, 1)">47</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">48</span>                 ts.<span style="color: rgba(0, 0, 255, 1)">Add</span><span style="color: rgba(0, 0, 0, 1)">(t);
</span><span style="color: rgba(0, 128, 128, 1)">49</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">50</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> ts;
</span><span style="color: rgba(0, 128, 128, 1)">51</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">52</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">53</span> }</pre>
