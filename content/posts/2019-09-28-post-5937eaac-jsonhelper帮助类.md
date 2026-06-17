---
title: "jsonHelper帮助类"
date: 2019-09-28
description: "使用前，需引用开源项目类using Newtonsoft.Json 链接：https://pan.baidu.com/s/1htK784XyRCl2XaGGM7RtEg 提取码：gs2n"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11184648.html"
---

<p>使用前，需引用开源项目类using Newtonsoft.Json</p>
<p>链接：https://pan.baidu.com/s/1htK784XyRCl2XaGGM7RtEg <br>提取码：gs2n </p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">  1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Collections.Generic;
</span><span style="color: rgba(0, 128, 128, 1)">  2</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.IO;
</span><span style="color: rgba(0, 128, 128, 1)">  3</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> Newtonsoft.Json;
</span><span style="color: rgba(0, 128, 128, 1)">  4</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> Newtonsoft.Json.Linq;
</span><span style="color: rgba(0, 128, 128, 1)">  5</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Data;
</span><span style="color: rgba(0, 128, 128, 1)">  6</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Reflection;
</span><span style="color: rgba(0, 128, 128, 1)">  7</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 128, 128, 1)">  8</span> 
<span style="color: rgba(0, 128, 128, 1)">  9</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> Sam.OA.Common
</span><span style="color: rgba(0, 128, 128, 1)"> 10</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)"> 11</span>     <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 12</span>     <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> Json帮助类
</span><span style="color: rgba(0, 128, 128, 1)"> 13</span>     <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 作者：陈彦斌
</span><span style="color: rgba(0, 128, 128, 1)"> 14</span>     <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 最后更新日期：2019年9月28日20:11:36
</span><span style="color: rgba(0, 128, 128, 1)"> 15</span>     <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 使用前需引用开源项目类库：Newtonsoft.Json.dll
</span><span style="color: rgba(0, 128, 128, 1)"> 16</span>     <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 17</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">sealed</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> JsonHelper
</span><span style="color: rgba(0, 128, 128, 1)"> 18</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)"> 19</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 20</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 将实体类序列化字符串
</span><span style="color: rgba(0, 128, 128, 1)"> 21</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 22</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;typeparam name="T"&gt;</span><span style="color: rgba(0, 128, 0, 1)">实体类</span><span style="color: rgba(128, 128, 128, 1)">&lt;/typeparam&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 23</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="t"&gt;&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 24</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 25</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">string</span> SerializeObject&lt;T&gt;<span style="color: rgba(0, 0, 0, 1)">(T t)
</span><span style="color: rgba(0, 128, 128, 1)"> 26</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 27</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 28</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 29</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> JsonConvert.SerializeObject(t);
</span><span style="color: rgba(0, 128, 128, 1)"> 30</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 31</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)"> 32</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 33</span>                 <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
</span><span style="color: rgba(0, 128, 128, 1)"> 34</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 35</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 36</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 37</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 将对象序列化为json格式
</span><span style="color: rgba(0, 128, 128, 1)"> 38</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 39</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="obj"&gt;</span><span style="color: rgba(0, 128, 0, 1)">序列化对象</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 40</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;</span><span style="color: rgba(0, 128, 0, 1)">json字符串</span><span style="color: rgba(128, 128, 128, 1)">&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 41</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">string</span> SerializeObjct(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> obj)
</span><span style="color: rgba(0, 128, 128, 1)"> 42</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 43</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> JsonConvert.SerializeObject(obj);
</span><span style="color: rgba(0, 128, 128, 1)"> 44</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 45</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 46</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 解析JSON字符串生成对象实体
</span><span style="color: rgba(0, 128, 128, 1)"> 47</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 48</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;typeparam name="T"&gt;</span><span style="color: rgba(0, 128, 0, 1)">实体类</span><span style="color: rgba(128, 128, 128, 1)">&lt;/typeparam&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 49</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="json"&gt;</span><span style="color: rgba(0, 128, 0, 1)">JSON字符串</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 50</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 51</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> T JsonConvertObject&lt;T&gt;(<span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> json)
</span><span style="color: rgba(0, 128, 128, 1)"> 52</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 53</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> JsonConvert.DeserializeObject&lt;T&gt;<span style="color: rgba(0, 0, 0, 1)">(json);
</span><span style="color: rgba(0, 128, 128, 1)"> 54</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 55</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 56</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 解析JSON字符串生成对象实体
</span><span style="color: rgba(0, 128, 128, 1)"> 57</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 58</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;typeparam name="T"&gt;</span><span style="color: rgba(0, 128, 0, 1)">对象类型</span><span style="color: rgba(128, 128, 128, 1)">&lt;/typeparam&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 59</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="json"&gt;</span><span style="color: rgba(0, 128, 0, 1)">json字符串</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 60</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 61</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> T DeserializeJsonToObject&lt;T&gt;(<span style="color: rgba(0, 0, 255, 1)">string</span> json) <span style="color: rgba(0, 0, 255, 1)">where</span> T : <span style="color: rgba(0, 0, 255, 1)">class</span>
<span style="color: rgba(0, 128, 128, 1)"> 62</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 63</span>             JsonSerializer serializer = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> JsonSerializer();
</span><span style="color: rgba(0, 128, 128, 1)"> 64</span>             StringReader sr = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> StringReader(json);
</span><span style="color: rgba(0, 128, 128, 1)"> 65</span>             <span style="color: rgba(0, 0, 255, 1)">object</span> obj = serializer.Deserialize(<span style="color: rgba(0, 0, 255, 1)">new</span> JsonTextReader(sr), <span style="color: rgba(0, 0, 255, 1)">typeof</span><span style="color: rgba(0, 0, 0, 1)">(T));
</span><span style="color: rgba(0, 128, 128, 1)"> 66</span>             T t = obj <span style="color: rgba(0, 0, 255, 1)">as</span><span style="color: rgba(0, 0, 0, 1)"> T;
</span><span style="color: rgba(0, 128, 128, 1)"> 67</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> t;
</span><span style="color: rgba(0, 128, 128, 1)"> 68</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 69</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 70</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 解析JSON数组生成对象实体集合
</span><span style="color: rgba(0, 128, 128, 1)"> 71</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 72</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;typeparam name="T"&gt;</span><span style="color: rgba(0, 128, 0, 1)">对象类型</span><span style="color: rgba(128, 128, 128, 1)">&lt;/typeparam&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 73</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="json"&gt;</span><span style="color: rgba(0, 128, 0, 1)">json数组</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 74</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;</span><span style="color: rgba(0, 128, 0, 1)">对象实体集合</span><span style="color: rgba(128, 128, 128, 1)">&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 75</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> List&lt;T&gt; DeserializeJsonToList&lt;T&gt;(<span style="color: rgba(0, 0, 255, 1)">string</span> json) <span style="color: rgba(0, 0, 255, 1)">where</span> T : <span style="color: rgba(0, 0, 255, 1)">class</span>
<span style="color: rgba(0, 128, 128, 1)"> 76</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 77</span>             JsonSerializer serializer = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> JsonSerializer();
</span><span style="color: rgba(0, 128, 128, 1)"> 78</span>             StringReader sr = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> StringReader(json);
</span><span style="color: rgba(0, 128, 128, 1)"> 79</span>             <span style="color: rgba(0, 0, 255, 1)">object</span> obj = serializer.Deserialize(<span style="color: rgba(0, 0, 255, 1)">new</span> JsonTextReader(sr), <span style="color: rgba(0, 0, 255, 1)">typeof</span>(List&lt;T&gt;<span style="color: rgba(0, 0, 0, 1)">));
</span><span style="color: rgba(0, 128, 128, 1)"> 80</span>             List&lt;T&gt; list = obj <span style="color: rgba(0, 0, 255, 1)">as</span> List&lt;T&gt;<span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 81</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> list;
</span><span style="color: rgba(0, 128, 128, 1)"> 82</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 83</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 84</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 将JSON转数组
</span><span style="color: rgba(0, 128, 128, 1)"> 85</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 用法:jsonArr[0]["xxxx"]
</span><span style="color: rgba(0, 128, 128, 1)"> 86</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 87</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="json"&gt;</span><span style="color: rgba(0, 128, 0, 1)">json字符串</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 88</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 89</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> JArray GetToJsonList(<span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> json)
</span><span style="color: rgba(0, 128, 128, 1)"> 90</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 91</span>             JArray jsonArr =<span style="color: rgba(0, 0, 0, 1)"> (JArray)JsonConvert.DeserializeObject(json);
</span><span style="color: rgba(0, 128, 128, 1)"> 92</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> jsonArr;
</span><span style="color: rgba(0, 128, 128, 1)"> 93</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 94</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 95</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 将DataTable转换成实体类
</span><span style="color: rgba(0, 128, 128, 1)"> 96</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 97</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;typeparam name="T"&gt;</span><span style="color: rgba(0, 128, 0, 1)">实体类</span><span style="color: rgba(128, 128, 128, 1)">&lt;/typeparam&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 98</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="dt"&gt;</span><span style="color: rgba(0, 128, 0, 1)">DataTable</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 99</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">100</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> List&lt;T&gt; DtConvertToModel&lt;T&gt;(DataTable dt) <span style="color: rgba(0, 0, 255, 1)">where</span> T : <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)">()
</span><span style="color: rgba(0, 128, 128, 1)">101</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">102</span>             List&lt;T&gt; ts = <span style="color: rgba(0, 0, 255, 1)">new</span> List&lt;T&gt;<span style="color: rgba(0, 0, 0, 1)">();
</span><span style="color: rgba(0, 128, 128, 1)">103</span>             <span style="color: rgba(0, 0, 255, 1)">foreach</span> (DataRow dr <span style="color: rgba(0, 0, 255, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> dt.Rows)
</span><span style="color: rgba(0, 128, 128, 1)">104</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">105</span>                 T t = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> T();
</span><span style="color: rgba(0, 128, 128, 1)">106</span>                 <span style="color: rgba(0, 0, 255, 1)">foreach</span> (PropertyInfo pi <span style="color: rgba(0, 0, 255, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> t.GetType().GetProperties())
</span><span style="color: rgba(0, 128, 128, 1)">107</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">108</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (dt.Columns.Contains(pi.Name))
</span><span style="color: rgba(0, 128, 128, 1)">109</span> <span style="color: rgba(0, 0, 0, 1)">                    {
</span><span style="color: rgba(0, 128, 128, 1)">110</span>                         <span style="color: rgba(0, 0, 255, 1)">if</span> (!pi.CanWrite) <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">111</span>                         <span style="color: rgba(0, 0, 255, 1)">var</span> value =<span style="color: rgba(0, 0, 0, 1)"> dr[pi.Name];
</span><span style="color: rgba(0, 128, 128, 1)">112</span>                         <span style="color: rgba(0, 0, 255, 1)">if</span> (value !=<span style="color: rgba(0, 0, 0, 1)"> DBNull.Value)
</span><span style="color: rgba(0, 128, 128, 1)">113</span> <span style="color: rgba(0, 0, 0, 1)">                        {
</span><span style="color: rgba(0, 128, 128, 1)">114</span>                             <span style="color: rgba(0, 0, 255, 1)">switch</span><span style="color: rgba(0, 0, 0, 1)"> (pi.PropertyType.FullName)
</span><span style="color: rgba(0, 128, 128, 1)">115</span> <span style="color: rgba(0, 0, 0, 1)">                            {
</span><span style="color: rgba(0, 128, 128, 1)">116</span>                                 <span style="color: rgba(0, 0, 255, 1)">case</span> <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">System.Decimal</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">:
</span><span style="color: rgba(0, 128, 128, 1)">117</span>                                     pi.SetValue(t, <span style="color: rgba(0, 0, 255, 1)">decimal</span>.Parse(value.ToString()), <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">118</span>                                     <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">119</span>                                 <span style="color: rgba(0, 0, 255, 1)">case</span> <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">System.String</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">:
</span><span style="color: rgba(0, 128, 128, 1)">120</span>                                     pi.SetValue(t, value.ToString(), <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">121</span>                                     <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">122</span>                                 <span style="color: rgba(0, 0, 255, 1)">case</span> <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">System.Int32</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">:
</span><span style="color: rgba(0, 128, 128, 1)">123</span>                                     pi.SetValue(t, <span style="color: rgba(0, 0, 255, 1)">int</span>.Parse(value.ToString()), <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">124</span>                                     <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">125</span>                                 <span style="color: rgba(0, 0, 255, 1)">default</span><span style="color: rgba(0, 0, 0, 1)">:
</span><span style="color: rgba(0, 128, 128, 1)">126</span>                                     pi.SetValue(t, value, <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">127</span>                                     <span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">128</span> <span style="color: rgba(0, 0, 0, 1)">                            }
</span><span style="color: rgba(0, 128, 128, 1)">129</span> <span style="color: rgba(0, 0, 0, 1)">                        }
</span><span style="color: rgba(0, 128, 128, 1)">130</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)">131</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">132</span> <span style="color: rgba(0, 0, 0, 1)">                ts.Add(t);
</span><span style="color: rgba(0, 128, 128, 1)">133</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">134</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> ts;
</span><span style="color: rgba(0, 128, 128, 1)">135</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">136</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">137</span> }</pre>
