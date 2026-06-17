---
title: "String字符串工具类"
date: 2023-05-31
description: "字符串类(StringUtil.cs) 1 using System; 2 3 namespace Sam.OA.Common 4 { 5 /// &lt;summary&gt; 6 /// 字符处理工具类 7 /// 作者：陈彦斌 8 /// 更新时间：2019年9月11日00:07:11 9 /"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11312024.html"
---

<h1>字符串类(StringUtil.cs)</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)">  1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 128, 128, 1)">  2</span> 
<span style="color: rgba(0, 128, 128, 1)">  3</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> Sam.OA.Common
</span><span style="color: rgba(0, 128, 128, 1)">  4</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)">  5</span>     <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">  6</span>     <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 字符处理工具类
</span><span style="color: rgba(0, 128, 128, 1)">  7</span>     <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 作者：陈彦斌
</span><span style="color: rgba(0, 128, 128, 1)">  8</span>     <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 更新时间：2019年9月11日00:07:11
</span><span style="color: rgba(0, 128, 128, 1)">  9</span>     <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 10</span> <span style="color: rgba(0, 0, 0, 1)">    [Serializable]
</span><span style="color: rgba(0, 128, 128, 1)"> 11</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> StringUtil
</span><span style="color: rgba(0, 128, 128, 1)"> 12</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)"> 13</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 14</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 判断字符对象为null或者为""
</span><span style="color: rgba(0, 128, 128, 1)"> 15</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 16</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="obj"&gt;</span><span style="color: rgba(0, 128, 0, 1)">字符对象</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 17</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 18</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">bool</span><span style="color: rgba(0, 0, 0, 1)"> isNullOrBlank(Object obj)
</span><span style="color: rgba(0, 128, 128, 1)"> 19</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 20</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (obj == <span style="color: rgba(0, 0, 255, 1)">null</span> || obj.ToString().ToLower() == <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">null</span><span style="color: rgba(128, 0, 0, 1)">"</span> || obj == DBNull.Value || obj.ToString().Trim() == <span style="color: rgba(128, 0, 0, 1)">""</span> || obj.ToString() == <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">undefined</span><span style="color: rgba(128, 0, 0, 1)">"</span> || obj.ToString().Equals(<span style="color: rgba(0, 0, 255, 1)">decimal</span><span style="color: rgba(0, 0, 0, 1)">.MinValue.ToString()))
</span><span style="color: rgba(0, 128, 128, 1)"> 21</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 22</span>             <span style="color: rgba(0, 0, 255, 1)">else</span>
<span style="color: rgba(0, 128, 128, 1)"> 23</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 24</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 25</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 26</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 处理字符串
</span><span style="color: rgba(0, 128, 128, 1)"> 27</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 28</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="obj"&gt;</span><span style="color: rgba(0, 128, 0, 1)">字符串</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 29</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 30</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">string</span> ProcessString(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> obj)
</span><span style="color: rgba(0, 128, 128, 1)"> 31</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 32</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> isNullOrBlank(obj) ? <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">null</span><span style="color: rgba(128, 0, 0, 1)">"</span> : <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">"</span> + obj.ToString().Replace(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">--</span><span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">""</span>) + <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 33</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 34</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 35</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 判断字符串是否为日期
</span><span style="color: rgba(0, 128, 128, 1)"> 36</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 37</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="strDate"&gt;</span><span style="color: rgba(0, 128, 0, 1)">日期字符串</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 38</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 39</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">bool</span> ObjectIsDate(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> strDate)
</span><span style="color: rgba(0, 128, 128, 1)"> 40</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 41</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 42</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 43</span> <span style="color: rgba(0, 0, 0, 1)">                DateTime.Parse(ProcessString(strDate));
</span><span style="color: rgba(0, 128, 128, 1)"> 44</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 45</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 46</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span>
<span style="color: rgba(0, 128, 128, 1)"> 47</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 48</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 49</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 50</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 51</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 52</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 判断字符串是否为decimal
</span><span style="color: rgba(0, 128, 128, 1)"> 53</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 54</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="obj"&gt;&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 55</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 56</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">bool</span> IsDecimal(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> obj)
</span><span style="color: rgba(0, 128, 128, 1)"> 57</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 58</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 59</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 60</span>                 <span style="color: rgba(0, 0, 255, 1)">decimal</span><span style="color: rgba(0, 0, 0, 1)">.Parse(obj.ToString().Trim());
</span><span style="color: rgba(0, 128, 128, 1)"> 61</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 62</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 63</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span>
<span style="color: rgba(0, 128, 128, 1)"> 64</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 65</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 66</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 67</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 68</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 69</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 对象是否为Null并返回三元运算符值
</span><span style="color: rgba(0, 128, 128, 1)"> 70</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 71</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="obj"&gt;</span><span style="color: rgba(0, 128, 0, 1)">对象</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 72</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 73</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">string</span> ObjectIsNull(<span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> obj)
</span><span style="color: rgba(0, 128, 128, 1)"> 74</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 75</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 76</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 77</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> obj == <span style="color: rgba(0, 0, 255, 1)">null</span> ? <span style="color: rgba(128, 0, 0, 1)">""</span> : obj.Replace(<span style="color: rgba(128, 0, 0, 1)">"</span> <span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">""</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 78</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 79</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)"> 80</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 81</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(128, 0, 0, 1)">""</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 82</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 83</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 84</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 85</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 对象是否为空并返回三元运算符值
</span><span style="color: rgba(0, 128, 128, 1)"> 86</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 87</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="obj"&gt;</span><span style="color: rgba(0, 128, 0, 1)">对象</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 88</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)"> 89</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">string</span> ObjectIsBlank(<span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> obj)
</span><span style="color: rgba(0, 128, 128, 1)"> 90</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 91</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 92</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 93</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> obj.Replace(<span style="color: rgba(128, 0, 0, 1)">"</span> <span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">""</span>) == <span style="color: rgba(128, 0, 0, 1)">""</span> ? <span style="color: rgba(128, 0, 0, 1)">""</span> : obj.Replace(<span style="color: rgba(128, 0, 0, 1)">"</span> <span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">""</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 94</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 95</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)"> 96</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 97</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(128, 0, 0, 1)">""</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 98</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 99</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">100</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">101</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 对象是否为Decimal并返回三元运算符值
</span><span style="color: rgba(0, 128, 128, 1)">102</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">103</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="obj"&gt;</span><span style="color: rgba(0, 128, 0, 1)">对象</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">104</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">105</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">decimal</span> ObjectIsDecimal(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> obj)
</span><span style="color: rgba(0, 128, 128, 1)">106</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">107</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)">108</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">109</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> Convert.ToDecimal(obj.ToString().Replace(<span style="color: rgba(128, 0, 0, 1)">"</span> <span style="color: rgba(128, 0, 0, 1)">"</span>, <span style="color: rgba(128, 0, 0, 1)">""</span>) == <span style="color: rgba(128, 0, 0, 1)">""</span> ? <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">0</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)"> : obj);
</span><span style="color: rgba(0, 128, 128, 1)">110</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">111</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)">112</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">113</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">114</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">115</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">116</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">117</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 获取当前月的第一天
</span><span style="color: rgba(0, 128, 128, 1)">118</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">119</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">120</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> DateTime GetFirstDayCurrentMonth()
</span><span style="color: rgba(0, 128, 128, 1)">121</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">122</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)">123</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">124</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> DateTime.Now.AddDays(<span style="color: rgba(128, 0, 128, 1)">1</span> -<span style="color: rgba(0, 0, 0, 1)"> DateTime.Now.Day).Date;
</span><span style="color: rgba(0, 128, 128, 1)">125</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">126</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)">127</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">128</span>                 <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
</span><span style="color: rgba(0, 128, 128, 1)">129</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">130</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">131</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">132</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 获取当前月的最后一天
</span><span style="color: rgba(0, 128, 128, 1)">133</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">134</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">135</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> DateTime GetLastDayCurrentMonth()
</span><span style="color: rgba(0, 128, 128, 1)">136</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">137</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)">138</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">139</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span> DateTime.Now.AddDays(-DateTime.Now.Day).Date.AddMonths(<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">140</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">141</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)">142</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">143</span>                 <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
</span><span style="color: rgba(0, 128, 128, 1)">144</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">145</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">146</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">147</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 获取指定日期，在为一年中为第几周
</span><span style="color: rgba(0, 128, 128, 1)">148</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">149</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="dtWeek"&gt;</span><span style="color: rgba(0, 128, 0, 1)">指定时间</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">150</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;reutrn&gt;</span><span style="color: rgba(0, 128, 0, 1)">返回第几周,1-52周</span><span style="color: rgba(128, 128, 128, 1)">&lt;/reutrn&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">151</span>         <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> GetWeekOfYear(DateTime dtWeek)
</span><span style="color: rgba(0, 128, 128, 1)">152</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">153</span>             System.Globalization.GregorianCalendar gc = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> System.Globalization.GregorianCalendar();
</span><span style="color: rgba(0, 128, 128, 1)">154</span>             <span style="color: rgba(0, 0, 255, 1)">int</span> weekOfYear =<span style="color: rgba(0, 0, 0, 1)"> gc.GetWeekOfYear(dtWeek, System.Globalization.CalendarWeekRule.FirstDay, DayOfWeek.Monday);
</span><span style="color: rgba(0, 128, 128, 1)">155</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> weekOfYear;
</span><span style="color: rgba(0, 128, 128, 1)">156</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">157</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">158</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 计算某日起始日期（礼拜一的日期） 
</span><span style="color: rgba(0, 128, 128, 1)">159</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">160</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="someDate"&gt;</span><span style="color: rgba(0, 128, 0, 1)">该周中任意一天</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">161</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;</span><span style="color: rgba(0, 128, 0, 1)">返回礼拜一日期，无时分秒</span><span style="color: rgba(128, 128, 128, 1)">&lt;/returns&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">162</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> GetMondayDate(DateTime someDate)
</span><span style="color: rgba(0, 128, 128, 1)">163</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">164</span>             <span style="color: rgba(0, 0, 255, 1)">int</span> i = someDate.DayOfWeek -<span style="color: rgba(0, 0, 0, 1)"> DayOfWeek.Monday;
</span><span style="color: rgba(0, 128, 128, 1)">165</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (i == -<span style="color: rgba(128, 0, 128, 1)">1</span>) i = <span style="color: rgba(128, 0, 128, 1)">6</span>;<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> i值 &gt; = 0 ，因为枚举原因，Sunday排在最前，此时Sunday-Monday=-1，必须+7=6。 </span>
<span style="color: rgba(0, 128, 128, 1)">166</span>             TimeSpan ts = <span style="color: rgba(0, 0, 255, 1)">new</span> TimeSpan(i, <span style="color: rgba(128, 0, 128, 1)">0</span>, <span style="color: rgba(128, 0, 128, 1)">0</span>, <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">167</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> someDate.Subtract(ts).ToShortDateString();
</span><span style="color: rgba(0, 128, 128, 1)">168</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">169</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">170</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 计算某日结束日期（礼拜日的日期） 
</span><span style="color: rgba(0, 128, 128, 1)">171</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">172</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="someDate"&gt;</span><span style="color: rgba(0, 128, 0, 1)">该周中任意一天</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">173</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;</span><span style="color: rgba(0, 128, 0, 1)">返回礼拜日日期，无时分秒</span><span style="color: rgba(128, 128, 128, 1)">&lt;/returns&gt;</span> 
<span style="color: rgba(0, 128, 128, 1)">174</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> GetSundayDate(DateTime someDate)
</span><span style="color: rgba(0, 128, 128, 1)">175</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">176</span>             <span style="color: rgba(0, 0, 255, 1)">int</span> i = someDate.DayOfWeek -<span style="color: rgba(0, 0, 0, 1)"> DayOfWeek.Sunday;
</span><span style="color: rgba(0, 128, 128, 1)">177</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (i != <span style="color: rgba(128, 0, 128, 1)">0</span>) i = <span style="color: rgba(128, 0, 128, 1)">7</span> - i;<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 因为枚举原因，Sunday排在最前，相减间隔要被7减。 </span>
<span style="color: rgba(0, 128, 128, 1)">178</span>             TimeSpan ts = <span style="color: rgba(0, 0, 255, 1)">new</span> TimeSpan(i, <span style="color: rgba(128, 0, 128, 1)">0</span>, <span style="color: rgba(128, 0, 128, 1)">0</span>, <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">179</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> someDate.Add(ts).ToShortDateString();
</span><span style="color: rgba(0, 128, 128, 1)">180</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">181</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">182</span>         <span style="color: rgba(128, 128, 128, 1)">///</span><span style="color: rgba(0, 128, 0, 1)"> 获取某月的天数
</span><span style="color: rgba(0, 128, 128, 1)">183</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;/summary&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">184</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;param name="someDate"&gt;</span><span style="color: rgba(0, 128, 0, 1)">日期</span><span style="color: rgba(128, 128, 128, 1)">&lt;/param&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">185</span>         <span style="color: rgba(128, 128, 128, 1)">///</span> <span style="color: rgba(128, 128, 128, 1)">&lt;returns&gt;</span><span style="color: rgba(0, 128, 0, 1)">当月的天数</span><span style="color: rgba(128, 128, 128, 1)">&lt;/returns&gt;</span>
<span style="color: rgba(0, 128, 128, 1)">186</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> GetDaysInMonth(DateTime someDate)
</span><span style="color: rgba(0, 128, 128, 1)">187</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">188</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> System.Threading.Thread.CurrentThread.CurrentUICulture.Calendar.GetDaysInMonth(someDate.Year, someDate.Month);
</span><span style="color: rgba(0, 128, 128, 1)">189</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">190</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">191</span> }</pre>
