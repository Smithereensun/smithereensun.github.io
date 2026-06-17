---
title: ".Net Mvc MyAjaxForm.js异步提交上传图片"
date: 2019-09-08
description: "MyAjaxForm.js源码脚本 1 /*! 2 * jQuery Form Plugin 3 * version: 3.51.0-2014.06.20 4 * Requires jQuery v1.5 or later 5 * Copyright (c) 2014 M. Alsup 6 * Ex"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11489479.html"
---

<p>MyAjaxForm.js源码脚本</p>
<div class="cnblogs_code"><img id="code_img_closed_67abadbb-eb89-4961-9de9-265ed2f41271" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_67abadbb-eb89-4961-9de9-265ed2f41271" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_67abadbb-eb89-4961-9de9-265ed2f41271" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)">   1</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">!
</span><span style="color: rgba(0, 128, 128, 1)">   2</span> <span style="color: rgba(0, 128, 0, 1)"> * jQuery Form Plugin
</span><span style="color: rgba(0, 128, 128, 1)">   3</span> <span style="color: rgba(0, 128, 0, 1)"> * version: 3.51.0-2014.06.20
</span><span style="color: rgba(0, 128, 128, 1)">   4</span> <span style="color: rgba(0, 128, 0, 1)"> * Requires jQuery v1.5 or later
</span><span style="color: rgba(0, 128, 128, 1)">   5</span> <span style="color: rgba(0, 128, 0, 1)"> * Copyright (c) 2014 M. Alsup
</span><span style="color: rgba(0, 128, 128, 1)">   6</span> <span style="color: rgba(0, 128, 0, 1)"> * Examples and documentation at: </span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">http://malsup.com/jquery/form/</span>
<span style="color: rgba(0, 128, 128, 1)">   7</span> <span style="color: rgba(0, 128, 0, 1)"> * Project repository: </span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">https://github.com/malsup/form</span>
<span style="color: rgba(0, 128, 128, 1)">   8</span> <span style="color: rgba(0, 128, 0, 1)"> * Dual licensed under the MIT and GPL licenses.
</span><span style="color: rgba(0, 128, 128, 1)">   9</span> <span style="color: rgba(0, 128, 0, 1)"> * </span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">https://github.com/malsup/form</span><span style="color: rgba(0, 128, 0, 1)">#copyright-and-license
</span><span style="color: rgba(0, 128, 128, 1)">  10</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">  11</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">global ActiveXObject </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">  12</span> 
<span style="color: rgba(0, 128, 128, 1)">  13</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> AMD support</span>
<span style="color: rgba(0, 128, 128, 1)">  14</span> <span style="color: rgba(0, 0, 0, 1)">(function (factory) {
</span><span style="color: rgba(0, 128, 128, 1)">  15</span>     <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">use strict</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">  16</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">typeof</span> define === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">function</span><span style="color: rgba(128, 0, 0, 1)">'</span> &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> define.amd) {
</span><span style="color: rgba(0, 128, 128, 1)">  17</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> using AMD; register as anon module</span>
<span style="color: rgba(0, 128, 128, 1)">  18</span>         define([<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">jquery</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">], factory);
</span><span style="color: rgba(0, 128, 128, 1)">  19</span>     } <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)">  20</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> no AMD; invoke directly</span>
<span style="color: rgba(0, 128, 128, 1)">  21</span>         factory( (<span style="color: rgba(0, 0, 255, 1)">typeof</span>(jQuery) != <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">undefined</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ?<span style="color: rgba(0, 0, 0, 1)"> jQuery : window.Zepto );
</span><span style="color: rgba(0, 128, 128, 1)">  22</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">  23</span> <span style="color: rgba(0, 0, 0, 1)">}
</span><span style="color: rgba(0, 128, 128, 1)">  24</span> 
<span style="color: rgba(0, 128, 128, 1)">  25</span> <span style="color: rgba(0, 0, 0, 1)">(function($) {
</span><span style="color: rgba(0, 128, 128, 1)">  26</span> <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">use strict</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">  27</span> 
<span style="color: rgba(0, 128, 128, 1)">  28</span> <span style="color: rgba(0, 128, 0, 1)">/*</span>
<span style="color: rgba(0, 128, 128, 1)">  29</span> <span style="color: rgba(0, 128, 0, 1)">    Usage Note:
</span><span style="color: rgba(0, 128, 128, 1)">  30</span> <span style="color: rgba(0, 128, 0, 1)">    -----------
</span><span style="color: rgba(0, 128, 128, 1)">  31</span> <span style="color: rgba(0, 128, 0, 1)">    Do not use both ajaxSubmit and ajaxForm on the same form.  These
</span><span style="color: rgba(0, 128, 128, 1)">  32</span> <span style="color: rgba(0, 128, 0, 1)">    functions are mutually exclusive.  Use ajaxSubmit if you want
</span><span style="color: rgba(0, 128, 128, 1)">  33</span> <span style="color: rgba(0, 128, 0, 1)">    to bind your own submit handler to the form.  For example,
</span><span style="color: rgba(0, 128, 128, 1)">  34</span> 
<span style="color: rgba(0, 128, 128, 1)">  35</span> <span style="color: rgba(0, 128, 0, 1)">    $(document).ready(function() {
</span><span style="color: rgba(0, 128, 128, 1)">  36</span> <span style="color: rgba(0, 128, 0, 1)">        $('#myForm').on('submit', function(e) {
</span><span style="color: rgba(0, 128, 128, 1)">  37</span> <span style="color: rgba(0, 128, 0, 1)">            e.preventDefault(); // &lt;-- important
</span><span style="color: rgba(0, 128, 128, 1)">  38</span> <span style="color: rgba(0, 128, 0, 1)">            $(this).ajaxSubmit({
</span><span style="color: rgba(0, 128, 128, 1)">  39</span> <span style="color: rgba(0, 128, 0, 1)">                target: '#output'
</span><span style="color: rgba(0, 128, 128, 1)">  40</span> <span style="color: rgba(0, 128, 0, 1)">            });
</span><span style="color: rgba(0, 128, 128, 1)">  41</span> <span style="color: rgba(0, 128, 0, 1)">        });
</span><span style="color: rgba(0, 128, 128, 1)">  42</span> <span style="color: rgba(0, 128, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">  43</span> 
<span style="color: rgba(0, 128, 128, 1)">  44</span> <span style="color: rgba(0, 128, 0, 1)">    Use ajaxForm when you want the plugin to manage all the event binding
</span><span style="color: rgba(0, 128, 128, 1)">  45</span> <span style="color: rgba(0, 128, 0, 1)">    for you.  For example,
</span><span style="color: rgba(0, 128, 128, 1)">  46</span> 
<span style="color: rgba(0, 128, 128, 1)">  47</span> <span style="color: rgba(0, 128, 0, 1)">    $(document).ready(function() {
</span><span style="color: rgba(0, 128, 128, 1)">  48</span> <span style="color: rgba(0, 128, 0, 1)">        $('#myForm').ajaxForm({
</span><span style="color: rgba(0, 128, 128, 1)">  49</span> <span style="color: rgba(0, 128, 0, 1)">            target: '#output'
</span><span style="color: rgba(0, 128, 128, 1)">  50</span> <span style="color: rgba(0, 128, 0, 1)">        });
</span><span style="color: rgba(0, 128, 128, 1)">  51</span> <span style="color: rgba(0, 128, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">  52</span> 
<span style="color: rgba(0, 128, 128, 1)">  53</span> <span style="color: rgba(0, 128, 0, 1)">    You can also use ajaxForm with delegation (requires jQuery v1.7+), so the
</span><span style="color: rgba(0, 128, 128, 1)">  54</span> <span style="color: rgba(0, 128, 0, 1)">    form does not have to exist when you invoke ajaxForm:
</span><span style="color: rgba(0, 128, 128, 1)">  55</span> 
<span style="color: rgba(0, 128, 128, 1)">  56</span> <span style="color: rgba(0, 128, 0, 1)">    $('#myForm').ajaxForm({
</span><span style="color: rgba(0, 128, 128, 1)">  57</span> <span style="color: rgba(0, 128, 0, 1)">        delegation: true,
</span><span style="color: rgba(0, 128, 128, 1)">  58</span> <span style="color: rgba(0, 128, 0, 1)">        target: '#output'
</span><span style="color: rgba(0, 128, 128, 1)">  59</span> <span style="color: rgba(0, 128, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">  60</span> 
<span style="color: rgba(0, 128, 128, 1)">  61</span> <span style="color: rgba(0, 128, 0, 1)">    When using ajaxForm, the ajaxSubmit function will be invoked for you
</span><span style="color: rgba(0, 128, 128, 1)">  62</span> <span style="color: rgba(0, 128, 0, 1)">    at the appropriate time.
</span><span style="color: rgba(0, 128, 128, 1)">  63</span> <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">  64</span> 
<span style="color: rgba(0, 128, 128, 1)">  65</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">  66</span> <span style="color: rgba(0, 128, 0, 1)"> * Feature detection
</span><span style="color: rgba(0, 128, 128, 1)">  67</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">  68</span> <span style="color: rgba(0, 0, 255, 1)">var</span> feature =<span style="color: rgba(0, 0, 0, 1)"> {};
</span><span style="color: rgba(0, 128, 128, 1)">  69</span> feature.fileapi = $(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">&lt;input type='file'/&gt;</span><span style="color: rgba(128, 0, 0, 1)">"</span>).<span style="color: rgba(0, 0, 255, 1)">get</span>(<span style="color: rgba(128, 0, 128, 1)">0</span>).files !==<span style="color: rgba(0, 0, 0, 1)"> undefined;
</span><span style="color: rgba(0, 128, 128, 1)">  70</span> feature.formdata = window.FormData !==<span style="color: rgba(0, 0, 0, 1)"> undefined;
</span><span style="color: rgba(0, 128, 128, 1)">  71</span> 
<span style="color: rgba(0, 128, 128, 1)">  72</span> <span style="color: rgba(0, 0, 255, 1)">var</span> hasProp = !!<span style="color: rgba(0, 0, 0, 1)">$.fn.prop;
</span><span style="color: rgba(0, 128, 128, 1)">  73</span> 
<span style="color: rgba(0, 128, 128, 1)">  74</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> attr2 uses prop when it can but checks the return type for
</span><span style="color: rgba(0, 128, 128, 1)">  75</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> an expected string.  this accounts for the case where a form 
</span><span style="color: rgba(0, 128, 128, 1)">  76</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> contains inputs with names like "action" or "method"; in those
</span><span style="color: rgba(0, 128, 128, 1)">  77</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> cases "prop" returns the element</span>
<span style="color: rgba(0, 128, 128, 1)">  78</span> $.fn.attr2 =<span style="color: rgba(0, 0, 0, 1)"> function() {
</span><span style="color: rgba(0, 128, 128, 1)">  79</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> ( !<span style="color: rgba(0, 0, 0, 1)"> hasProp ) {
</span><span style="color: rgba(0, 128, 128, 1)">  80</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span>.attr.apply(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, arguments);
</span><span style="color: rgba(0, 128, 128, 1)">  81</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">  82</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> val = <span style="color: rgba(0, 0, 255, 1)">this</span>.prop.apply(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, arguments);
</span><span style="color: rgba(0, 128, 128, 1)">  83</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> ( ( val &amp;&amp; val.jquery ) || <span style="color: rgba(0, 0, 255, 1)">typeof</span> val === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">string</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)"> ) {
</span><span style="color: rgba(0, 128, 128, 1)">  84</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> val;
</span><span style="color: rgba(0, 128, 128, 1)">  85</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">  86</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span>.attr.apply(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, arguments);
</span><span style="color: rgba(0, 128, 128, 1)">  87</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">  88</span> 
<span style="color: rgba(0, 128, 128, 1)">  89</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">  90</span> <span style="color: rgba(0, 128, 0, 1)"> * ajaxSubmit() provides a mechanism for immediately submitting
</span><span style="color: rgba(0, 128, 128, 1)">  91</span> <span style="color: rgba(0, 128, 0, 1)"> * an HTML form using AJAX.
</span><span style="color: rgba(0, 128, 128, 1)">  92</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">  93</span> $.fn.ajaxSubmit =<span style="color: rgba(0, 0, 0, 1)"> function(options) {
</span><span style="color: rgba(0, 128, 128, 1)">  94</span>     <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">jshint scripturl:true </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">  95</span> 
<span style="color: rgba(0, 128, 128, 1)">  96</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> fast fail if nothing selected (</span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">http://dev.jquery.com/ticket/2752</span><span style="color: rgba(0, 128, 0, 1)">)</span>
<span style="color: rgba(0, 128, 128, 1)">  97</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.length) {
</span><span style="color: rgba(0, 128, 128, 1)">  98</span>         log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">ajaxSubmit: skipping submit process - no element selected</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">  99</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 100</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 101</span> 
<span style="color: rgba(0, 128, 128, 1)"> 102</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> method, action, url, $form = <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 103</span> 
<span style="color: rgba(0, 128, 128, 1)"> 104</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">typeof</span> options == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">function</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 105</span>         options =<span style="color: rgba(0, 0, 0, 1)"> { success: options };
</span><span style="color: rgba(0, 128, 128, 1)"> 106</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 107</span>     <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> ( options ===<span style="color: rgba(0, 0, 0, 1)"> undefined ) {
</span><span style="color: rgba(0, 128, 128, 1)"> 108</span>         options =<span style="color: rgba(0, 0, 0, 1)"> {};
</span><span style="color: rgba(0, 128, 128, 1)"> 109</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 110</span> 
<span style="color: rgba(0, 128, 128, 1)"> 111</span>     method = options.type || <span style="color: rgba(0, 0, 255, 1)">this</span>.attr2(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">method</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 112</span>     action = options.url  || <span style="color: rgba(0, 0, 255, 1)">this</span>.attr2(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">action</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 113</span> 
<span style="color: rgba(0, 128, 128, 1)"> 114</span>     url = (<span style="color: rgba(0, 0, 255, 1)">typeof</span> action === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">string</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ? $.trim(action) : <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 115</span>     url = url || window.location.href || <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 116</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (url) {
</span><span style="color: rgba(0, 128, 128, 1)"> 117</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> clean url (don't include hash vaue)</span>
<span style="color: rgba(0, 128, 128, 1)"> 118</span>         url = (url.match(/^([^#]+)/)||[])[<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 119</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 120</span> 
<span style="color: rgba(0, 128, 128, 1)"> 121</span>     options = $.extend(<span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">, {
</span><span style="color: rgba(0, 128, 128, 1)"> 122</span> <span style="color: rgba(0, 0, 0, 1)">        url:  url,
</span><span style="color: rgba(0, 128, 128, 1)"> 123</span> <span style="color: rgba(0, 0, 0, 1)">        success: $.ajaxSettings.success,
</span><span style="color: rgba(0, 128, 128, 1)"> 124</span>         type: method ||<span style="color: rgba(0, 0, 0, 1)"> $.ajaxSettings.type,
</span><span style="color: rgba(0, 128, 128, 1)"> 125</span>         iframeSrc: /^https/i.test(window.location.href || <span style="color: rgba(128, 0, 0, 1)">''</span>) ? <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">javascript:false</span><span style="color: rgba(128, 0, 0, 1)">'</span> : <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">about:blank</span><span style="color: rgba(128, 0, 0, 1)">'</span>
<span style="color: rgba(0, 128, 128, 1)"> 126</span> <span style="color: rgba(0, 0, 0, 1)">    }, options);
</span><span style="color: rgba(0, 128, 128, 1)"> 127</span> 
<span style="color: rgba(0, 128, 128, 1)"> 128</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> hook for manipulating the form data before it is extracted;
</span><span style="color: rgba(0, 128, 128, 1)"> 129</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> convenient for use with rich editors like tinyMCE or FCKEditor</span>
<span style="color: rgba(0, 128, 128, 1)"> 130</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> veto =<span style="color: rgba(0, 0, 0, 1)"> {};
</span><span style="color: rgba(0, 128, 128, 1)"> 131</span>     <span style="color: rgba(0, 0, 255, 1)">this</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">form-pre-serialize</span><span style="color: rgba(128, 0, 0, 1)">'</span>, [<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, options, veto]);
</span><span style="color: rgba(0, 128, 128, 1)"> 132</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (veto.veto) {
</span><span style="color: rgba(0, 128, 128, 1)"> 133</span>         log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">ajaxSubmit: submit vetoed via form-pre-serialize trigger</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 134</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 135</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 136</span> 
<span style="color: rgba(0, 128, 128, 1)"> 137</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> provide opportunity to alter form data before it is serialized</span>
<span style="color: rgba(0, 128, 128, 1)"> 138</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (options.beforeSerialize &amp;&amp; options.beforeSerialize(<span style="color: rgba(0, 0, 255, 1)">this</span>, options) === <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 139</span>         log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">ajaxSubmit: submit aborted via beforeSerialize callback</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 140</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 141</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 142</span> 
<span style="color: rgba(0, 128, 128, 1)"> 143</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> traditional =<span style="color: rgba(0, 0, 0, 1)"> options.traditional;
</span><span style="color: rgba(0, 128, 128, 1)"> 144</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> ( traditional ===<span style="color: rgba(0, 0, 0, 1)"> undefined ) {
</span><span style="color: rgba(0, 128, 128, 1)"> 145</span>         traditional =<span style="color: rgba(0, 0, 0, 1)"> $.ajaxSettings.traditional;
</span><span style="color: rgba(0, 128, 128, 1)"> 146</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 147</span> 
<span style="color: rgba(0, 128, 128, 1)"> 148</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> elements =<span style="color: rgba(0, 0, 0, 1)"> [];
</span><span style="color: rgba(0, 128, 128, 1)"> 149</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> qx, a = <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.formToArray(options.semantic, elements);
</span><span style="color: rgba(0, 128, 128, 1)"> 150</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.data) {
</span><span style="color: rgba(0, 128, 128, 1)"> 151</span>         options.extraData =<span style="color: rgba(0, 0, 0, 1)"> options.data;
</span><span style="color: rgba(0, 128, 128, 1)"> 152</span>         qx =<span style="color: rgba(0, 0, 0, 1)"> $.param(options.data, traditional);
</span><span style="color: rgba(0, 128, 128, 1)"> 153</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 154</span> 
<span style="color: rgba(0, 128, 128, 1)"> 155</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> give pre-submit callback an opportunity to abort the submit</span>
<span style="color: rgba(0, 128, 128, 1)"> 156</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (options.beforeSubmit &amp;&amp; options.beforeSubmit(a, <span style="color: rgba(0, 0, 255, 1)">this</span>, options) === <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 157</span>         log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">ajaxSubmit: submit aborted via beforeSubmit callback</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 158</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 159</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 160</span> 
<span style="color: rgba(0, 128, 128, 1)"> 161</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> fire vetoable 'validate' event</span>
<span style="color: rgba(0, 128, 128, 1)"> 162</span>     <span style="color: rgba(0, 0, 255, 1)">this</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">form-submit-validate</span><span style="color: rgba(128, 0, 0, 1)">'</span>, [a, <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, options, veto]);
</span><span style="color: rgba(0, 128, 128, 1)"> 163</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (veto.veto) {
</span><span style="color: rgba(0, 128, 128, 1)"> 164</span>         log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">ajaxSubmit: submit vetoed via form-submit-validate trigger</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 165</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 166</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 167</span> 
<span style="color: rgba(0, 128, 128, 1)"> 168</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> q =<span style="color: rgba(0, 0, 0, 1)"> $.param(a, traditional);
</span><span style="color: rgba(0, 128, 128, 1)"> 169</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (qx) {
</span><span style="color: rgba(0, 128, 128, 1)"> 170</span>         q = ( q ? (q + <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">&amp;</span><span style="color: rgba(128, 0, 0, 1)">'</span> +<span style="color: rgba(0, 0, 0, 1)"> qx) : qx );
</span><span style="color: rgba(0, 128, 128, 1)"> 171</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 172</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (options.type.toUpperCase() == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">GET</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 173</span>         options.url += (options.url.indexOf(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">?</span><span style="color: rgba(128, 0, 0, 1)">'</span>) &gt;= <span style="color: rgba(128, 0, 128, 1)">0</span> ? <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">&amp;</span><span style="color: rgba(128, 0, 0, 1)">'</span> : <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">?</span><span style="color: rgba(128, 0, 0, 1)">'</span>) +<span style="color: rgba(0, 0, 0, 1)"> q;
</span><span style="color: rgba(0, 128, 128, 1)"> 174</span>         options.data = <span style="color: rgba(0, 0, 255, 1)">null</span>;  <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> data is null for 'get'</span>
<span style="color: rgba(0, 128, 128, 1)"> 175</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 176</span>     <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 177</span>         options.data = q; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> data is the query string for 'post'</span>
<span style="color: rgba(0, 128, 128, 1)"> 178</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 179</span> 
<span style="color: rgba(0, 128, 128, 1)"> 180</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> callbacks =<span style="color: rgba(0, 0, 0, 1)"> [];
</span><span style="color: rgba(0, 128, 128, 1)"> 181</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.resetForm) {
</span><span style="color: rgba(0, 128, 128, 1)"> 182</span> <span style="color: rgba(0, 0, 0, 1)">        callbacks.push(function() { $form.resetForm(); });
</span><span style="color: rgba(0, 128, 128, 1)"> 183</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 184</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.clearForm) {
</span><span style="color: rgba(0, 128, 128, 1)"> 185</span> <span style="color: rgba(0, 0, 0, 1)">        callbacks.push(function() { $form.clearForm(options.includeHidden); });
</span><span style="color: rgba(0, 128, 128, 1)"> 186</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 187</span> 
<span style="color: rgba(0, 128, 128, 1)"> 188</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> perform a load on the target only if dataType is not provided</span>
<span style="color: rgba(0, 128, 128, 1)"> 189</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!options.dataType &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> options.target) {
</span><span style="color: rgba(0, 128, 128, 1)"> 190</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> oldSuccess = options.success ||<span style="color: rgba(0, 0, 0, 1)"> function(){};
</span><span style="color: rgba(0, 128, 128, 1)"> 191</span> <span style="color: rgba(0, 0, 0, 1)">        callbacks.push(function(data) {
</span><span style="color: rgba(0, 128, 128, 1)"> 192</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> fn = options.replaceTarget ? <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">replaceWith</span><span style="color: rgba(128, 0, 0, 1)">'</span> : <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">html</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 193</span> <span style="color: rgba(0, 0, 0, 1)">            $(options.target)[fn](data).each(oldSuccess, arguments);
</span><span style="color: rgba(0, 128, 128, 1)"> 194</span> <span style="color: rgba(0, 0, 0, 1)">        });
</span><span style="color: rgba(0, 128, 128, 1)"> 195</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 196</span>     <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.success) {
</span><span style="color: rgba(0, 128, 128, 1)"> 197</span> <span style="color: rgba(0, 0, 0, 1)">        callbacks.push(options.success);
</span><span style="color: rgba(0, 128, 128, 1)"> 198</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 199</span> 
<span style="color: rgba(0, 128, 128, 1)"> 200</span>     options.success = function(data, status, xhr) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> jQuery 1.4+ passes xhr as 3rd arg</span>
<span style="color: rgba(0, 128, 128, 1)"> 201</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> context = options.context || <span style="color: rgba(0, 0, 255, 1)">this</span> ;    <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> jQuery 1.4+ supports scope context</span>
<span style="color: rgba(0, 128, 128, 1)"> 202</span>         <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">var</span> i=<span style="color: rgba(128, 0, 128, 1)">0</span>, max=callbacks.length; i &lt; max; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 203</span>             callbacks[i].apply(context, [data, status, xhr ||<span style="color: rgba(0, 0, 0, 1)"> $form, $form]);
</span><span style="color: rgba(0, 128, 128, 1)"> 204</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 205</span> <span style="color: rgba(0, 0, 0, 1)">    };
</span><span style="color: rgba(0, 128, 128, 1)"> 206</span> 
<span style="color: rgba(0, 128, 128, 1)"> 207</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.error) {
</span><span style="color: rgba(0, 128, 128, 1)"> 208</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> oldError =<span style="color: rgba(0, 0, 0, 1)"> options.error;
</span><span style="color: rgba(0, 128, 128, 1)"> 209</span>         options.error =<span style="color: rgba(0, 0, 0, 1)"> function(xhr, status, error) {
</span><span style="color: rgba(0, 128, 128, 1)"> 210</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> context = options.context || <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 211</span> <span style="color: rgba(0, 0, 0, 1)">            oldError.apply(context, [xhr, status, error, $form]);
</span><span style="color: rgba(0, 128, 128, 1)"> 212</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)"> 213</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 214</span> 
<span style="color: rgba(0, 128, 128, 1)"> 215</span>      <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.complete) {
</span><span style="color: rgba(0, 128, 128, 1)"> 216</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> oldComplete =<span style="color: rgba(0, 0, 0, 1)"> options.complete;
</span><span style="color: rgba(0, 128, 128, 1)"> 217</span>         options.complete =<span style="color: rgba(0, 0, 0, 1)"> function(xhr, status) {
</span><span style="color: rgba(0, 128, 128, 1)"> 218</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> context = options.context || <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 219</span> <span style="color: rgba(0, 0, 0, 1)">            oldComplete.apply(context, [xhr, status, $form]);
</span><span style="color: rgba(0, 128, 128, 1)"> 220</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)"> 221</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 222</span> 
<span style="color: rgba(0, 128, 128, 1)"> 223</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> are there files to upload?
</span><span style="color: rgba(0, 128, 128, 1)"> 224</span> 
<span style="color: rgba(0, 128, 128, 1)"> 225</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> [value] (issue #113), also see comment:
</span><span style="color: rgba(0, 128, 128, 1)"> 226</span>     <span style="color: rgba(0, 128, 0, 1)">//</span> <span style="color: rgba(0, 128, 0, 1); text-decoration: underline">https://github.com/malsup/form/commit/588306aedba1de01388032d5f42a60159eea9228</span><span style="color: rgba(0, 128, 0, 1)">#commitcomment-2180219</span>
<span style="color: rgba(0, 128, 128, 1)"> 227</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> fileInputs = $(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">input[type=file]:enabled</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(0, 0, 255, 1)">this</span>).filter(function() { <span style="color: rgba(0, 0, 255, 1)">return</span> $(<span style="color: rgba(0, 0, 255, 1)">this</span>).val() !== <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">; });
</span><span style="color: rgba(0, 128, 128, 1)"> 228</span> 
<span style="color: rgba(0, 128, 128, 1)"> 229</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> hasFileInputs = fileInputs.length &gt; <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 230</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> mp = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">multipart/form-data</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 231</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> multipart = ($form.attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">enctype</span><span style="color: rgba(128, 0, 0, 1)">'</span>) == mp || $form.attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">encoding</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ==<span style="color: rgba(0, 0, 0, 1)"> mp);
</span><span style="color: rgba(0, 128, 128, 1)"> 232</span> 
<span style="color: rgba(0, 128, 128, 1)"> 233</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> fileAPI = feature.fileapi &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> feature.formdata;
</span><span style="color: rgba(0, 128, 128, 1)"> 234</span>     log(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">fileAPI :</span><span style="color: rgba(128, 0, 0, 1)">"</span> +<span style="color: rgba(0, 0, 0, 1)"> fileAPI);
</span><span style="color: rgba(0, 128, 128, 1)"> 235</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> shouldUseFrame = (hasFileInputs || multipart) &amp;&amp; !<span style="color: rgba(0, 0, 0, 1)">fileAPI;
</span><span style="color: rgba(0, 128, 128, 1)"> 236</span> 
<span style="color: rgba(0, 128, 128, 1)"> 237</span>     <span style="color: rgba(0, 0, 255, 1)">var</span><span style="color: rgba(0, 0, 0, 1)"> jqxhr;
</span><span style="color: rgba(0, 128, 128, 1)"> 238</span> 
<span style="color: rgba(0, 128, 128, 1)"> 239</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> options.iframe allows user to force iframe mode
</span><span style="color: rgba(0, 128, 128, 1)"> 240</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 06-NOV-09: now defaulting to iframe mode if file input is detected</span>
<span style="color: rgba(0, 128, 128, 1)"> 241</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (options.iframe !== <span style="color: rgba(0, 0, 255, 1)">false</span> &amp;&amp; (options.iframe ||<span style="color: rgba(0, 0, 0, 1)"> shouldUseFrame)) {
</span><span style="color: rgba(0, 128, 128, 1)"> 242</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> hack to fix Safari hang (thanks to Tim Molendijk for this)
</span><span style="color: rgba(0, 128, 128, 1)"> 243</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> see:  </span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">http://groups.google.com/group/jquery-dev/browse_thread/thread/36395b7ab510dd5d</span>
<span style="color: rgba(0, 128, 128, 1)"> 244</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.closeKeepAlive) {
</span><span style="color: rgba(0, 128, 128, 1)"> 245</span>             $.<span style="color: rgba(0, 0, 255, 1)">get</span><span style="color: rgba(0, 0, 0, 1)">(options.closeKeepAlive, function() {
</span><span style="color: rgba(0, 128, 128, 1)"> 246</span>                 jqxhr =<span style="color: rgba(0, 0, 0, 1)"> fileUploadIframe(a);
</span><span style="color: rgba(0, 128, 128, 1)"> 247</span> <span style="color: rgba(0, 0, 0, 1)">            });
</span><span style="color: rgba(0, 128, 128, 1)"> 248</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 249</span>         <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 250</span>             jqxhr =<span style="color: rgba(0, 0, 0, 1)"> fileUploadIframe(a);
</span><span style="color: rgba(0, 128, 128, 1)"> 251</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 252</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 253</span>     <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> ((hasFileInputs || multipart) &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> fileAPI) {
</span><span style="color: rgba(0, 128, 128, 1)"> 254</span>         jqxhr =<span style="color: rgba(0, 0, 0, 1)"> fileUploadXhr(a);
</span><span style="color: rgba(0, 128, 128, 1)"> 255</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 256</span>     <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 257</span>         jqxhr =<span style="color: rgba(0, 0, 0, 1)"> $.ajax(options);
</span><span style="color: rgba(0, 128, 128, 1)"> 258</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 259</span> 
<span style="color: rgba(0, 128, 128, 1)"> 260</span>     $form.removeData(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">jqxhr</span><span style="color: rgba(128, 0, 0, 1)">'</span>).data(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">jqxhr</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, jqxhr);
</span><span style="color: rgba(0, 128, 128, 1)"> 261</span> 
<span style="color: rgba(0, 128, 128, 1)"> 262</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> clear element array</span>
<span style="color: rgba(0, 128, 128, 1)"> 263</span>     <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">var</span> k=<span style="color: rgba(128, 0, 128, 1)">0</span>; k &lt; elements.length; k++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 264</span>         elements[k] = <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 265</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 266</span> 
<span style="color: rgba(0, 128, 128, 1)"> 267</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> fire 'notify' event</span>
<span style="color: rgba(0, 128, 128, 1)"> 268</span>     <span style="color: rgba(0, 0, 255, 1)">this</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">form-submit-notify</span><span style="color: rgba(128, 0, 0, 1)">'</span>, [<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, options]);
</span><span style="color: rgba(0, 128, 128, 1)"> 269</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 270</span> 
<span style="color: rgba(0, 128, 128, 1)"> 271</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> utility fn for deep serialization</span>
<span style="color: rgba(0, 128, 128, 1)"> 272</span> <span style="color: rgba(0, 0, 0, 1)">    function deepSerialize(extraData){
</span><span style="color: rgba(0, 128, 128, 1)"> 273</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> serialized = $.param(extraData, options.traditional).split(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">&amp;</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 274</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> len =<span style="color: rgba(0, 0, 0, 1)"> serialized.length;
</span><span style="color: rgba(0, 128, 128, 1)"> 275</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> result =<span style="color: rgba(0, 0, 0, 1)"> [];
</span><span style="color: rgba(0, 128, 128, 1)"> 276</span>         <span style="color: rgba(0, 0, 255, 1)">var</span><span style="color: rgba(0, 0, 0, 1)"> i, part;
</span><span style="color: rgba(0, 128, 128, 1)"> 277</span>         <span style="color: rgba(0, 0, 255, 1)">for</span> (i=<span style="color: rgba(128, 0, 128, 1)">0</span>; i &lt; len; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 278</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #252; undo param space replacement</span>
<span style="color: rgba(0, 128, 128, 1)"> 279</span>             serialized[i] = serialized[i].replace(/\+/g,<span style="color: rgba(128, 0, 0, 1)">'</span> <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 280</span>             part = serialized[i].split(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">=</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 281</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #278; use array instead of object storage, favoring array serializations</span>
<span style="color: rgba(0, 128, 128, 1)"> 282</span>             result.push([decodeURIComponent(part[<span style="color: rgba(128, 0, 128, 1)">0</span>]), decodeURIComponent(part[<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">])]);
</span><span style="color: rgba(0, 128, 128, 1)"> 283</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 284</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> result;
</span><span style="color: rgba(0, 128, 128, 1)"> 285</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 286</span> 
<span style="color: rgba(0, 128, 128, 1)"> 287</span>      <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> XMLHttpRequest Level 2 file uploads (big hat tip to francois2metz)</span>
<span style="color: rgba(0, 128, 128, 1)"> 288</span> <span style="color: rgba(0, 0, 0, 1)">    function fileUploadXhr(a) {
</span><span style="color: rgba(0, 128, 128, 1)"> 289</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> formdata = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> FormData();
</span><span style="color: rgba(0, 128, 128, 1)"> 290</span> 
<span style="color: rgba(0, 128, 128, 1)"> 291</span>         <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">var</span> i=<span style="color: rgba(128, 0, 128, 1)">0</span>; i &lt; a.length; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 292</span> <span style="color: rgba(0, 0, 0, 1)">            formdata.append(a[i].name, a[i].value);
</span><span style="color: rgba(0, 128, 128, 1)"> 293</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 294</span> 
<span style="color: rgba(0, 128, 128, 1)"> 295</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.extraData) {
</span><span style="color: rgba(0, 128, 128, 1)"> 296</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> serializedData =<span style="color: rgba(0, 0, 0, 1)"> deepSerialize(options.extraData);
</span><span style="color: rgba(0, 128, 128, 1)"> 297</span>             <span style="color: rgba(0, 0, 255, 1)">for</span> (i=<span style="color: rgba(128, 0, 128, 1)">0</span>; i &lt; serializedData.length; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 298</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (serializedData[i]) {
</span><span style="color: rgba(0, 128, 128, 1)"> 299</span>                     formdata.append(serializedData[i][<span style="color: rgba(128, 0, 128, 1)">0</span>], serializedData[i][<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">]);
</span><span style="color: rgba(0, 128, 128, 1)"> 300</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 301</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 302</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 303</span> 
<span style="color: rgba(0, 128, 128, 1)"> 304</span>         options.data = <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 305</span> 
<span style="color: rgba(0, 128, 128, 1)"> 306</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> s = $.extend(<span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">, {}, $.ajaxSettings, options, {
</span><span style="color: rgba(0, 128, 128, 1)"> 307</span>             contentType: <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 308</span>             processData: <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 309</span>             cache: <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 310</span>             type: method || <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">POST</span><span style="color: rgba(128, 0, 0, 1)">'</span>
<span style="color: rgba(0, 128, 128, 1)"> 311</span> <span style="color: rgba(0, 0, 0, 1)">        });
</span><span style="color: rgba(0, 128, 128, 1)"> 312</span> 
<span style="color: rgba(0, 128, 128, 1)"> 313</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.uploadProgress) {
</span><span style="color: rgba(0, 128, 128, 1)"> 314</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> workaround because jqXHR does not expose upload property</span>
<span style="color: rgba(0, 128, 128, 1)"> 315</span>             s.xhr =<span style="color: rgba(0, 0, 0, 1)"> function() {
</span><span style="color: rgba(0, 128, 128, 1)"> 316</span>                 <span style="color: rgba(0, 0, 255, 1)">var</span> xhr =<span style="color: rgba(0, 0, 0, 1)"> $.ajaxSettings.xhr();
</span><span style="color: rgba(0, 128, 128, 1)"> 317</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (xhr.upload) {
</span><span style="color: rgba(0, 128, 128, 1)"> 318</span>                     xhr.upload.addEventListener(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">progress</span><span style="color: rgba(128, 0, 0, 1)">'</span>, function(<span style="color: rgba(0, 0, 255, 1)">event</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 319</span>                         <span style="color: rgba(0, 0, 255, 1)">var</span> percent = <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 320</span>                         <span style="color: rgba(0, 0, 255, 1)">var</span> position = <span style="color: rgba(0, 0, 255, 1)">event</span>.loaded || <span style="color: rgba(0, 0, 255, 1)">event</span>.position; <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">event.position is deprecated</span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 321</span>                         <span style="color: rgba(0, 0, 255, 1)">var</span> total = <span style="color: rgba(0, 0, 255, 1)">event</span><span style="color: rgba(0, 0, 0, 1)">.total;
</span><span style="color: rgba(0, 128, 128, 1)"> 322</span>                         <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">event</span><span style="color: rgba(0, 0, 0, 1)">.lengthComputable) {
</span><span style="color: rgba(0, 128, 128, 1)"> 323</span>                             percent = Math.ceil(position / total * <span style="color: rgba(128, 0, 128, 1)">100</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 324</span> <span style="color: rgba(0, 0, 0, 1)">                        }
</span><span style="color: rgba(0, 128, 128, 1)"> 325</span>                         options.uploadProgress(<span style="color: rgba(0, 0, 255, 1)">event</span><span style="color: rgba(0, 0, 0, 1)">, position, total, percent);
</span><span style="color: rgba(0, 128, 128, 1)"> 326</span>                     }, <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 327</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 328</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> xhr;
</span><span style="color: rgba(0, 128, 128, 1)"> 329</span> <span style="color: rgba(0, 0, 0, 1)">            };
</span><span style="color: rgba(0, 128, 128, 1)"> 330</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 331</span> 
<span style="color: rgba(0, 128, 128, 1)"> 332</span>         s.data = <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 333</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> beforeSend =<span style="color: rgba(0, 0, 0, 1)"> s.beforeSend;
</span><span style="color: rgba(0, 128, 128, 1)"> 334</span>         s.beforeSend =<span style="color: rgba(0, 0, 0, 1)"> function(xhr, o) {
</span><span style="color: rgba(0, 128, 128, 1)"> 335</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">Send FormData() provided by user</span>
<span style="color: rgba(0, 128, 128, 1)"> 336</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (options.formData) {
</span><span style="color: rgba(0, 128, 128, 1)"> 337</span>                 o.data =<span style="color: rgba(0, 0, 0, 1)"> options.formData;
</span><span style="color: rgba(0, 128, 128, 1)"> 338</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 339</span>             <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 340</span>                 o.data =<span style="color: rgba(0, 0, 0, 1)"> formdata;
</span><span style="color: rgba(0, 128, 128, 1)"> 341</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 342</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)">(beforeSend) {
</span><span style="color: rgba(0, 128, 128, 1)"> 343</span>                 beforeSend.call(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, xhr, o);
</span><span style="color: rgba(0, 128, 128, 1)"> 344</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 345</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)"> 346</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> $.ajax(s);
</span><span style="color: rgba(0, 128, 128, 1)"> 347</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 348</span> 
<span style="color: rgba(0, 128, 128, 1)"> 349</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> private function for handling file uploads (hat tip to YAHOO!)</span>
<span style="color: rgba(0, 128, 128, 1)"> 350</span> <span style="color: rgba(0, 0, 0, 1)">    function fileUploadIframe(a) {
</span><span style="color: rgba(0, 128, 128, 1)"> 351</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> form = $form[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">], el, i, s, g, id, $io, io, xhr, sub, n, timedOut, timeoutHandle;
</span><span style="color: rgba(0, 128, 128, 1)"> 352</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> deferred =<span style="color: rgba(0, 0, 0, 1)"> $.Deferred();
</span><span style="color: rgba(0, 128, 128, 1)"> 353</span> 
<span style="color: rgba(0, 128, 128, 1)"> 354</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #341</span>
<span style="color: rgba(0, 128, 128, 1)"> 355</span>         deferred.abort =<span style="color: rgba(0, 0, 0, 1)"> function(status) {
</span><span style="color: rgba(0, 128, 128, 1)"> 356</span> <span style="color: rgba(0, 0, 0, 1)">            xhr.abort(status);
</span><span style="color: rgba(0, 128, 128, 1)"> 357</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)"> 358</span> 
<span style="color: rgba(0, 128, 128, 1)"> 359</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (a) {
</span><span style="color: rgba(0, 128, 128, 1)"> 360</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> ensure that every serialized input is still enabled</span>
<span style="color: rgba(0, 128, 128, 1)"> 361</span>             <span style="color: rgba(0, 0, 255, 1)">for</span> (i=<span style="color: rgba(128, 0, 128, 1)">0</span>; i &lt; elements.length; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 362</span>                 el =<span style="color: rgba(0, 0, 0, 1)"> $(elements[i]);
</span><span style="color: rgba(0, 128, 128, 1)"> 363</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> ( hasProp ) {
</span><span style="color: rgba(0, 128, 128, 1)"> 364</span>                     el.prop(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">disabled</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 365</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 366</span>                 <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 367</span>                     el.removeAttr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">disabled</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 368</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 369</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 370</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 371</span> 
<span style="color: rgba(0, 128, 128, 1)"> 372</span>         s = $.extend(<span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">, {}, $.ajaxSettings, options);
</span><span style="color: rgba(0, 128, 128, 1)"> 373</span>         s.context = s.context ||<span style="color: rgba(0, 0, 0, 1)"> s;
</span><span style="color: rgba(0, 128, 128, 1)"> 374</span>         id = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">jqFormIO</span><span style="color: rgba(128, 0, 0, 1)">'</span> + (<span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> Date().getTime());
</span><span style="color: rgba(0, 128, 128, 1)"> 375</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.iframeTarget) {
</span><span style="color: rgba(0, 128, 128, 1)"> 376</span>             $io =<span style="color: rgba(0, 0, 0, 1)"> $(s.iframeTarget);
</span><span style="color: rgba(0, 128, 128, 1)"> 377</span>             n = $io.attr2(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">name</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 378</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 0, 1)">n) {
</span><span style="color: rgba(0, 128, 128, 1)"> 379</span>                 $io.attr2(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">name</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, id);
</span><span style="color: rgba(0, 128, 128, 1)"> 380</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 381</span>             <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 382</span>                 id =<span style="color: rgba(0, 0, 0, 1)"> n;
</span><span style="color: rgba(0, 128, 128, 1)"> 383</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 384</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 385</span>         <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 386</span>             $io = $(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">&lt;iframe name="</span><span style="color: rgba(128, 0, 0, 1)">'</span> + id + <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">" src="</span><span style="color: rgba(128, 0, 0, 1)">'</span>+ s.iframeSrc +<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">" /&gt;</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 387</span>             $io.css({ position: <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">absolute</span><span style="color: rgba(128, 0, 0, 1)">'</span>, top: <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">-1000px</span><span style="color: rgba(128, 0, 0, 1)">'</span>, left: <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">-1000px</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)"> });
</span><span style="color: rgba(0, 128, 128, 1)"> 388</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 389</span>         io = $io[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 390</span> 
<span style="color: rgba(0, 128, 128, 1)"> 391</span> 
<span style="color: rgba(0, 128, 128, 1)"> 392</span>         xhr = { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> mock object</span>
<span style="color: rgba(0, 128, 128, 1)"> 393</span>             aborted: <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 394</span>             responseText: <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 395</span>             responseXML: <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 396</span>             status: <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 397</span>             statusText: <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">n/a</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 398</span> <span style="color: rgba(0, 0, 0, 1)">            getAllResponseHeaders: function() {},
</span><span style="color: rgba(0, 128, 128, 1)"> 399</span> <span style="color: rgba(0, 0, 0, 1)">            getResponseHeader: function() {},
</span><span style="color: rgba(0, 128, 128, 1)"> 400</span> <span style="color: rgba(0, 0, 0, 1)">            setRequestHeader: function() {},
</span><span style="color: rgba(0, 128, 128, 1)"> 401</span> <span style="color: rgba(0, 0, 0, 1)">            abort: function(status) {
</span><span style="color: rgba(0, 128, 128, 1)"> 402</span>                 <span style="color: rgba(0, 0, 255, 1)">var</span> e = (status === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">timeout</span><span style="color: rgba(128, 0, 0, 1)">'</span> ? <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">timeout</span><span style="color: rgba(128, 0, 0, 1)">'</span> : <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">aborted</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 403</span>                 log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">aborting upload... </span><span style="color: rgba(128, 0, 0, 1)">'</span> +<span style="color: rgba(0, 0, 0, 1)"> e);
</span><span style="color: rgba(0, 128, 128, 1)"> 404</span>                 <span style="color: rgba(0, 0, 255, 1)">this</span>.aborted = <span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 405</span> 
<span style="color: rgba(0, 128, 128, 1)"> 406</span>                 <span style="color: rgba(0, 0, 255, 1)">try</span> { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #214, #257</span>
<span style="color: rgba(0, 128, 128, 1)"> 407</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (io.contentWindow.document.execCommand) {
</span><span style="color: rgba(0, 128, 128, 1)"> 408</span>                         io.contentWindow.document.execCommand(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">Stop</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 409</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)"> 410</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 411</span>                 <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)">(ignore) {}
</span><span style="color: rgba(0, 128, 128, 1)"> 412</span> 
<span style="color: rgba(0, 128, 128, 1)"> 413</span>                 $io.attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">src</span><span style="color: rgba(128, 0, 0, 1)">'</span>, s.iframeSrc); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> abort op in progress</span>
<span style="color: rgba(0, 128, 128, 1)"> 414</span>                 xhr.error =<span style="color: rgba(0, 0, 0, 1)"> e;
</span><span style="color: rgba(0, 128, 128, 1)"> 415</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.error) {
</span><span style="color: rgba(0, 128, 128, 1)"> 416</span> <span style="color: rgba(0, 0, 0, 1)">                    s.error.call(s.context, xhr, e, status);
</span><span style="color: rgba(0, 128, 128, 1)"> 417</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 418</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (g) {
</span><span style="color: rgba(0, 128, 128, 1)"> 419</span>                     $.<span style="color: rgba(0, 0, 255, 1)">event</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ajaxError</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">, [xhr, s, e]);
</span><span style="color: rgba(0, 128, 128, 1)"> 420</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 421</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.complete) {
</span><span style="color: rgba(0, 128, 128, 1)"> 422</span> <span style="color: rgba(0, 0, 0, 1)">                    s.complete.call(s.context, xhr, e);
</span><span style="color: rgba(0, 128, 128, 1)"> 423</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 424</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 425</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)"> 426</span> 
<span style="color: rgba(0, 128, 128, 1)"> 427</span>         g = s.<span style="color: rgba(0, 0, 255, 1)">global</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 428</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> trigger ajax global events so that activity/block indicators work like normal</span>
<span style="color: rgba(0, 128, 128, 1)"> 429</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (g &amp;&amp; <span style="color: rgba(128, 0, 128, 1)">0</span> === $.active++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 430</span>             $.<span style="color: rgba(0, 0, 255, 1)">event</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ajaxStart</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 431</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 432</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (g) {
</span><span style="color: rgba(0, 128, 128, 1)"> 433</span>             $.<span style="color: rgba(0, 0, 255, 1)">event</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ajaxSend</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">, [xhr, s]);
</span><span style="color: rgba(0, 128, 128, 1)"> 434</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 435</span> 
<span style="color: rgba(0, 128, 128, 1)"> 436</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (s.beforeSend &amp;&amp; s.beforeSend.call(s.context, xhr, s) === <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 437</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (s.<span style="color: rgba(0, 0, 255, 1)">global</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 438</span>                 $.active--<span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 439</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 440</span> <span style="color: rgba(0, 0, 0, 1)">            deferred.reject();
</span><span style="color: rgba(0, 128, 128, 1)"> 441</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> deferred;
</span><span style="color: rgba(0, 128, 128, 1)"> 442</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 443</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (xhr.aborted) {
</span><span style="color: rgba(0, 128, 128, 1)"> 444</span> <span style="color: rgba(0, 0, 0, 1)">            deferred.reject();
</span><span style="color: rgba(0, 128, 128, 1)"> 445</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> deferred;
</span><span style="color: rgba(0, 128, 128, 1)"> 446</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 447</span> 
<span style="color: rgba(0, 128, 128, 1)"> 448</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> add submitting element to data if we know it</span>
<span style="color: rgba(0, 128, 128, 1)"> 449</span>         sub =<span style="color: rgba(0, 0, 0, 1)"> form.clk;
</span><span style="color: rgba(0, 128, 128, 1)"> 450</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (sub) {
</span><span style="color: rgba(0, 128, 128, 1)"> 451</span>             n =<span style="color: rgba(0, 0, 0, 1)"> sub.name;
</span><span style="color: rgba(0, 128, 128, 1)"> 452</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (n &amp;&amp; !<span style="color: rgba(0, 0, 0, 1)">sub.disabled) {
</span><span style="color: rgba(0, 128, 128, 1)"> 453</span>                 s.extraData = s.extraData ||<span style="color: rgba(0, 0, 0, 1)"> {};
</span><span style="color: rgba(0, 128, 128, 1)"> 454</span>                 s.extraData[n] =<span style="color: rgba(0, 0, 0, 1)"> sub.value;
</span><span style="color: rgba(0, 128, 128, 1)"> 455</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (sub.type == <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">image</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 456</span>                     s.extraData[n+<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">.x</span><span style="color: rgba(128, 0, 0, 1)">'</span>] =<span style="color: rgba(0, 0, 0, 1)"> form.clk_x;
</span><span style="color: rgba(0, 128, 128, 1)"> 457</span>                     s.extraData[n+<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">.y</span><span style="color: rgba(128, 0, 0, 1)">'</span>] =<span style="color: rgba(0, 0, 0, 1)"> form.clk_y;
</span><span style="color: rgba(0, 128, 128, 1)"> 458</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 459</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 460</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 461</span> 
<span style="color: rgba(0, 128, 128, 1)"> 462</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> CLIENT_TIMEOUT_ABORT = <span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 463</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> SERVER_ABORT = <span style="color: rgba(128, 0, 128, 1)">2</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 464</span>                 
<span style="color: rgba(0, 128, 128, 1)"> 465</span> <span style="color: rgba(0, 0, 0, 1)">        function getDoc(frame) {
</span><span style="color: rgba(0, 128, 128, 1)"> 466</span>             <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)"> it looks like contentWindow or contentDocument do not
</span><span style="color: rgba(0, 128, 128, 1)"> 467</span> <span style="color: rgba(0, 128, 0, 1)">             * carry the protocol property in ie8, when running under ssl
</span><span style="color: rgba(0, 128, 128, 1)"> 468</span> <span style="color: rgba(0, 128, 0, 1)">             * frame.document is the only valid response document, since
</span><span style="color: rgba(0, 128, 128, 1)"> 469</span> <span style="color: rgba(0, 128, 0, 1)">             * the protocol is know but not on the other two objects. strange?
</span><span style="color: rgba(0, 128, 128, 1)"> 470</span> <span style="color: rgba(0, 128, 0, 1)">             * "Same origin policy" </span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">http://en.wikipedia.org/wiki/Same_origin_policy</span>
<span style="color: rgba(0, 128, 128, 1)"> 471</span>              <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 472</span>             
<span style="color: rgba(0, 128, 128, 1)"> 473</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> doc = <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 474</span>             
<span style="color: rgba(0, 128, 128, 1)"> 475</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> IE8 cascading access check</span>
<span style="color: rgba(0, 128, 128, 1)"> 476</span>             <span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 477</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (frame.contentWindow) {
</span><span style="color: rgba(0, 128, 128, 1)"> 478</span>                     doc =<span style="color: rgba(0, 0, 0, 1)"> frame.contentWindow.document;
</span><span style="color: rgba(0, 128, 128, 1)"> 479</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 480</span>             } <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)">(err) {
</span><span style="color: rgba(0, 128, 128, 1)"> 481</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> IE8 access denied under ssl &amp; missing protocol</span>
<span style="color: rgba(0, 128, 128, 1)"> 482</span>                 log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">cannot get iframe.contentWindow document: </span><span style="color: rgba(128, 0, 0, 1)">'</span> +<span style="color: rgba(0, 0, 0, 1)"> err);
</span><span style="color: rgba(0, 128, 128, 1)"> 483</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 484</span> 
<span style="color: rgba(0, 128, 128, 1)"> 485</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (doc) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> successful getting content</span>
<span style="color: rgba(0, 128, 128, 1)"> 486</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> doc;
</span><span style="color: rgba(0, 128, 128, 1)"> 487</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 488</span> 
<span style="color: rgba(0, 128, 128, 1)"> 489</span>             <span style="color: rgba(0, 0, 255, 1)">try</span> { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> simply checking may throw in ie8 under ssl or mismatched protocol</span>
<span style="color: rgba(0, 128, 128, 1)"> 490</span>                 doc = frame.contentDocument ?<span style="color: rgba(0, 0, 0, 1)"> frame.contentDocument : frame.document;
</span><span style="color: rgba(0, 128, 128, 1)"> 491</span>             } <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)">(err) {
</span><span style="color: rgba(0, 128, 128, 1)"> 492</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> last attempt</span>
<span style="color: rgba(0, 128, 128, 1)"> 493</span>                 log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">cannot get iframe.contentDocument: </span><span style="color: rgba(128, 0, 0, 1)">'</span> +<span style="color: rgba(0, 0, 0, 1)"> err);
</span><span style="color: rgba(0, 128, 128, 1)"> 494</span>                 doc =<span style="color: rgba(0, 0, 0, 1)"> frame.document;
</span><span style="color: rgba(0, 128, 128, 1)"> 495</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 496</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> doc;
</span><span style="color: rgba(0, 128, 128, 1)"> 497</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 498</span> 
<span style="color: rgba(0, 128, 128, 1)"> 499</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Rails CSRF hack (thanks to Yvan Barthelemy)</span>
<span style="color: rgba(0, 128, 128, 1)"> 500</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> csrf_token = $(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">meta[name=csrf-token]</span><span style="color: rgba(128, 0, 0, 1)">'</span>).attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">content</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 501</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> csrf_param = $(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">meta[name=csrf-param]</span><span style="color: rgba(128, 0, 0, 1)">'</span>).attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">content</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 502</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (csrf_param &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> csrf_token) {
</span><span style="color: rgba(0, 128, 128, 1)"> 503</span>             s.extraData = s.extraData ||<span style="color: rgba(0, 0, 0, 1)"> {};
</span><span style="color: rgba(0, 128, 128, 1)"> 504</span>             s.extraData[csrf_param] =<span style="color: rgba(0, 0, 0, 1)"> csrf_token;
</span><span style="color: rgba(0, 128, 128, 1)"> 505</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 506</span> 
<span style="color: rgba(0, 128, 128, 1)"> 507</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> take a breath so that pending repaints get some cpu time before the upload starts</span>
<span style="color: rgba(0, 128, 128, 1)"> 508</span> <span style="color: rgba(0, 0, 0, 1)">        function doSubmit() {
</span><span style="color: rgba(0, 128, 128, 1)"> 509</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> make sure form attrs are set</span>
<span style="color: rgba(0, 128, 128, 1)"> 510</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> t = $form.attr2(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">target</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">), 
</span><span style="color: rgba(0, 128, 128, 1)"> 511</span>                 a = $form.attr2(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">action</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">), 
</span><span style="color: rgba(0, 128, 128, 1)"> 512</span>                 mp = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">multipart/form-data</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 513</span>                 et = $form.attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">enctype</span><span style="color: rgba(128, 0, 0, 1)">'</span>) || $form.attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">encoding</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ||<span style="color: rgba(0, 0, 0, 1)"> mp;
</span><span style="color: rgba(0, 128, 128, 1)"> 514</span> 
<span style="color: rgba(0, 128, 128, 1)"> 515</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> update form attrs in IE friendly way</span>
<span style="color: rgba(0, 128, 128, 1)"> 516</span>             form.setAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">target</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,id);
</span><span style="color: rgba(0, 128, 128, 1)"> 517</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (!method || /post/<span style="color: rgba(0, 0, 0, 1)">i.test(method) ) {
</span><span style="color: rgba(0, 128, 128, 1)"> 518</span>                 form.setAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">method</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">POST</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 519</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 520</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (a !=<span style="color: rgba(0, 0, 0, 1)"> s.url) {
</span><span style="color: rgba(0, 128, 128, 1)"> 521</span>                 form.setAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">action</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, s.url);
</span><span style="color: rgba(0, 128, 128, 1)"> 522</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 523</span> 
<span style="color: rgba(0, 128, 128, 1)"> 524</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> ie borks in some cases when setting encoding</span>
<span style="color: rgba(0, 128, 128, 1)"> 525</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (! s.skipEncodingOverride &amp;&amp; (!method || /post/<span style="color: rgba(0, 0, 0, 1)">i.test(method))) {
</span><span style="color: rgba(0, 128, 128, 1)"> 526</span> <span style="color: rgba(0, 0, 0, 1)">                $form.attr({
</span><span style="color: rgba(0, 128, 128, 1)"> 527</span>                     encoding: <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">multipart/form-data</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 528</span>                     enctype:  <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">multipart/form-data</span><span style="color: rgba(128, 0, 0, 1)">'</span>
<span style="color: rgba(0, 128, 128, 1)"> 529</span> <span style="color: rgba(0, 0, 0, 1)">                });
</span><span style="color: rgba(0, 128, 128, 1)"> 530</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 531</span> 
<span style="color: rgba(0, 128, 128, 1)"> 532</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> support timout</span>
<span style="color: rgba(0, 128, 128, 1)"> 533</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.timeout) {
</span><span style="color: rgba(0, 128, 128, 1)"> 534</span>                 timeoutHandle = setTimeout(function() { timedOut = <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">; cb(CLIENT_TIMEOUT_ABORT); }, s.timeout);
</span><span style="color: rgba(0, 128, 128, 1)"> 535</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 536</span> 
<span style="color: rgba(0, 128, 128, 1)"> 537</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> look for server aborts</span>
<span style="color: rgba(0, 128, 128, 1)"> 538</span> <span style="color: rgba(0, 0, 0, 1)">            function checkState() {
</span><span style="color: rgba(0, 128, 128, 1)"> 539</span>                 <span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 540</span>                     <span style="color: rgba(0, 0, 255, 1)">var</span> state =<span style="color: rgba(0, 0, 0, 1)"> getDoc(io).readyState;
</span><span style="color: rgba(0, 128, 128, 1)"> 541</span>                     log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">state = </span><span style="color: rgba(128, 0, 0, 1)">'</span> +<span style="color: rgba(0, 0, 0, 1)"> state);
</span><span style="color: rgba(0, 128, 128, 1)"> 542</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span> (state &amp;&amp; state.toLowerCase() == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">uninitialized</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 543</span>                         setTimeout(checkState,<span style="color: rgba(128, 0, 128, 1)">50</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 544</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)"> 545</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 546</span>                 <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)">(e) {
</span><span style="color: rgba(0, 128, 128, 1)"> 547</span>                     log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">Server abort: </span><span style="color: rgba(128, 0, 0, 1)">'</span> , e, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)"> (</span><span style="color: rgba(128, 0, 0, 1)">'</span>, e.name, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">)</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 548</span> <span style="color: rgba(0, 0, 0, 1)">                    cb(SERVER_ABORT);
</span><span style="color: rgba(0, 128, 128, 1)"> 549</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (timeoutHandle) {
</span><span style="color: rgba(0, 128, 128, 1)"> 550</span> <span style="color: rgba(0, 0, 0, 1)">                        clearTimeout(timeoutHandle);
</span><span style="color: rgba(0, 128, 128, 1)"> 551</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)"> 552</span>                     timeoutHandle =<span style="color: rgba(0, 0, 0, 1)"> undefined;
</span><span style="color: rgba(0, 128, 128, 1)"> 553</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 554</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 555</span> 
<span style="color: rgba(0, 128, 128, 1)"> 556</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> add "extra" data to form if provided in options</span>
<span style="color: rgba(0, 128, 128, 1)"> 557</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> extraInputs =<span style="color: rgba(0, 0, 0, 1)"> [];
</span><span style="color: rgba(0, 128, 128, 1)"> 558</span>             <span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 559</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.extraData) {
</span><span style="color: rgba(0, 128, 128, 1)"> 560</span>                     <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">var</span> n <span style="color: rgba(0, 0, 255, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> s.extraData) {
</span><span style="color: rgba(0, 128, 128, 1)"> 561</span>                         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.extraData.hasOwnProperty(n)) {
</span><span style="color: rgba(0, 128, 128, 1)"> 562</span>                            <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> if using the $.param format that allows for multiple values with the same name</span>
<span style="color: rgba(0, 128, 128, 1)"> 563</span>                            <span style="color: rgba(0, 0, 255, 1)">if</span>($.isPlainObject(s.extraData[n]) &amp;&amp; s.extraData[n].hasOwnProperty(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">name</span><span style="color: rgba(128, 0, 0, 1)">'</span>) &amp;&amp; s.extraData[n].hasOwnProperty(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">value</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">)) {
</span><span style="color: rgba(0, 128, 128, 1)"> 564</span> <span style="color: rgba(0, 0, 0, 1)">                               extraInputs.push(
</span><span style="color: rgba(0, 128, 128, 1)"> 565</span>                                $(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">&lt;input type="hidden" name="</span><span style="color: rgba(128, 0, 0, 1)">'</span>+s.extraData[n].name+<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">"&gt;</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">).val(s.extraData[n].value)
</span><span style="color: rgba(0, 128, 128, 1)"> 566</span>                                    .appendTo(form)[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">]);
</span><span style="color: rgba(0, 128, 128, 1)"> 567</span>                            } <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 568</span> <span style="color: rgba(0, 0, 0, 1)">                               extraInputs.push(
</span><span style="color: rgba(0, 128, 128, 1)"> 569</span>                                $(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">&lt;input type="hidden" name="</span><span style="color: rgba(128, 0, 0, 1)">'</span>+n+<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">"&gt;</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">).val(s.extraData[n])
</span><span style="color: rgba(0, 128, 128, 1)"> 570</span>                                    .appendTo(form)[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">]);
</span><span style="color: rgba(0, 128, 128, 1)"> 571</span> <span style="color: rgba(0, 0, 0, 1)">                           }
</span><span style="color: rgba(0, 128, 128, 1)"> 572</span> <span style="color: rgba(0, 0, 0, 1)">                        }
</span><span style="color: rgba(0, 128, 128, 1)"> 573</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)"> 574</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 575</span> 
<span style="color: rgba(0, 128, 128, 1)"> 576</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 0, 1)">s.iframeTarget) {
</span><span style="color: rgba(0, 128, 128, 1)"> 577</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> add iframe to doc and submit the form</span>
<span style="color: rgba(0, 128, 128, 1)"> 578</span>                     $io.appendTo(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">body</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 579</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 580</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (io.attachEvent) {
</span><span style="color: rgba(0, 128, 128, 1)"> 581</span>                     io.attachEvent(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">onload</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, cb);
</span><span style="color: rgba(0, 128, 128, 1)"> 582</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 583</span>                 <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 584</span>                     io.addEventListener(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">load</span><span style="color: rgba(128, 0, 0, 1)">'</span>, cb, <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 585</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 586</span>                 setTimeout(checkState,<span style="color: rgba(128, 0, 128, 1)">15</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 587</span> 
<span style="color: rgba(0, 128, 128, 1)"> 588</span>                 <span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 589</span> <span style="color: rgba(0, 0, 0, 1)">                    form.submit();
</span><span style="color: rgba(0, 128, 128, 1)"> 590</span>                 } <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)">(err) {
</span><span style="color: rgba(0, 128, 128, 1)"> 591</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> just in case form has element with name/id of 'submit'</span>
<span style="color: rgba(0, 128, 128, 1)"> 592</span>                     <span style="color: rgba(0, 0, 255, 1)">var</span> submitFn = document.createElement(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">form</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">).submit;
</span><span style="color: rgba(0, 128, 128, 1)"> 593</span> <span style="color: rgba(0, 0, 0, 1)">                    submitFn.apply(form);
</span><span style="color: rgba(0, 128, 128, 1)"> 594</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 595</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 596</span>             <span style="color: rgba(0, 0, 255, 1)">finally</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 597</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> reset attrs and remove "extra" input elements</span>
<span style="color: rgba(0, 128, 128, 1)"> 598</span>                 form.setAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">action</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,a);
</span><span style="color: rgba(0, 128, 128, 1)"> 599</span>                 form.setAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">enctype</span><span style="color: rgba(128, 0, 0, 1)">'</span>, et); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #380</span>
<span style="color: rgba(0, 128, 128, 1)"> 600</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)">(t) {
</span><span style="color: rgba(0, 128, 128, 1)"> 601</span>                     form.setAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">target</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, t);
</span><span style="color: rgba(0, 128, 128, 1)"> 602</span>                 } <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 603</span>                     $form.removeAttr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">target</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 604</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 605</span> <span style="color: rgba(0, 0, 0, 1)">                $(extraInputs).remove();
</span><span style="color: rgba(0, 128, 128, 1)"> 606</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 607</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 608</span> 
<span style="color: rgba(0, 128, 128, 1)"> 609</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.forceSync) {
</span><span style="color: rgba(0, 128, 128, 1)"> 610</span> <span style="color: rgba(0, 0, 0, 1)">            doSubmit();
</span><span style="color: rgba(0, 128, 128, 1)"> 611</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 612</span>         <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 613</span>             setTimeout(doSubmit, <span style="color: rgba(128, 0, 128, 1)">10</span>); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> this lets dom updates render</span>
<span style="color: rgba(0, 128, 128, 1)"> 614</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 615</span> 
<span style="color: rgba(0, 128, 128, 1)"> 616</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> data, doc, domCheckCount = <span style="color: rgba(128, 0, 128, 1)">50</span><span style="color: rgba(0, 0, 0, 1)">, callbackProcessed;
</span><span style="color: rgba(0, 128, 128, 1)"> 617</span> 
<span style="color: rgba(0, 128, 128, 1)"> 618</span> <span style="color: rgba(0, 0, 0, 1)">        function cb(e) {
</span><span style="color: rgba(0, 128, 128, 1)"> 619</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (xhr.aborted ||<span style="color: rgba(0, 0, 0, 1)"> callbackProcessed) {
</span><span style="color: rgba(0, 128, 128, 1)"> 620</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 621</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 622</span>             
<span style="color: rgba(0, 128, 128, 1)"> 623</span>             doc =<span style="color: rgba(0, 0, 0, 1)"> getDoc(io);
</span><span style="color: rgba(0, 128, 128, 1)"> 624</span>             <span style="color: rgba(0, 0, 255, 1)">if</span>(!<span style="color: rgba(0, 0, 0, 1)">doc) {
</span><span style="color: rgba(0, 128, 128, 1)"> 625</span>                 log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">cannot access response document</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 626</span>                 e =<span style="color: rgba(0, 0, 0, 1)"> SERVER_ABORT;
</span><span style="color: rgba(0, 128, 128, 1)"> 627</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 628</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (e === CLIENT_TIMEOUT_ABORT &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> xhr) {
</span><span style="color: rgba(0, 128, 128, 1)"> 629</span>                 xhr.abort(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">timeout</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 630</span>                 deferred.reject(xhr, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">timeout</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 631</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 632</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 633</span>             <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (e == SERVER_ABORT &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> xhr) {
</span><span style="color: rgba(0, 128, 128, 1)"> 634</span>                 xhr.abort(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">server abort</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 635</span>                 deferred.reject(xhr, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">error</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">server abort</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 636</span>                 <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 637</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 638</span> 
<span style="color: rgba(0, 128, 128, 1)"> 639</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (!doc || doc.location.href ==<span style="color: rgba(0, 0, 0, 1)"> s.iframeSrc) {
</span><span style="color: rgba(0, 128, 128, 1)"> 640</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> response not received yet</span>
<span style="color: rgba(0, 128, 128, 1)"> 641</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 0, 1)">timedOut) {
</span><span style="color: rgba(0, 128, 128, 1)"> 642</span>                     <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 643</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 644</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 645</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (io.detachEvent) {
</span><span style="color: rgba(0, 128, 128, 1)"> 646</span>                 io.detachEvent(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">onload</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, cb);
</span><span style="color: rgba(0, 128, 128, 1)"> 647</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 648</span>             <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 649</span>                 io.removeEventListener(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">load</span><span style="color: rgba(128, 0, 0, 1)">'</span>, cb, <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 650</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 651</span> 
<span style="color: rgba(0, 128, 128, 1)"> 652</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> status = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">success</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, errMsg;
</span><span style="color: rgba(0, 128, 128, 1)"> 653</span>             <span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 654</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (timedOut) {
</span><span style="color: rgba(0, 128, 128, 1)"> 655</span>                     <span style="color: rgba(0, 0, 255, 1)">throw</span> <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">timeout</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 656</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 657</span> 
<span style="color: rgba(0, 128, 128, 1)"> 658</span>                 <span style="color: rgba(0, 0, 255, 1)">var</span> isXml = s.dataType == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">xml</span><span style="color: rgba(128, 0, 0, 1)">'</span> || doc.XMLDocument ||<span style="color: rgba(0, 0, 0, 1)"> $.isXMLDoc(doc);
</span><span style="color: rgba(0, 128, 128, 1)"> 659</span>                 log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">isXml=</span><span style="color: rgba(128, 0, 0, 1)">'</span>+<span style="color: rgba(0, 0, 0, 1)">isXml);
</span><span style="color: rgba(0, 128, 128, 1)"> 660</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (!isXml &amp;&amp; window.opera &amp;&amp; (doc.body === <span style="color: rgba(0, 0, 255, 1)">null</span> || !<span style="color: rgba(0, 0, 0, 1)">doc.body.innerHTML)) {
</span><span style="color: rgba(0, 128, 128, 1)"> 661</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span> (--<span style="color: rgba(0, 0, 0, 1)">domCheckCount) {
</span><span style="color: rgba(0, 128, 128, 1)"> 662</span>                         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> in some browsers (Opera) the iframe DOM is not always traversable when
</span><span style="color: rgba(0, 128, 128, 1)"> 663</span>                         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> the onload callback fires, so we loop a bit to accommodate</span>
<span style="color: rgba(0, 128, 128, 1)"> 664</span>                         log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">requeing onLoad callback, DOM not available</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 665</span>                         setTimeout(cb, <span style="color: rgba(128, 0, 128, 1)">250</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 666</span>                         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 667</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)"> 668</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> let this fall through because server response could be an empty document
</span><span style="color: rgba(0, 128, 128, 1)"> 669</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">log('Could not access iframe DOM after mutiple tries.');
</span><span style="color: rgba(0, 128, 128, 1)"> 670</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">throw 'DOMException: not available';</span>
<span style="color: rgba(0, 128, 128, 1)"> 671</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 672</span> 
<span style="color: rgba(0, 128, 128, 1)"> 673</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">log('response detected');</span>
<span style="color: rgba(0, 128, 128, 1)"> 674</span>                 <span style="color: rgba(0, 0, 255, 1)">var</span> docRoot = doc.body ?<span style="color: rgba(0, 0, 0, 1)"> doc.body : doc.documentElement;
</span><span style="color: rgba(0, 128, 128, 1)"> 675</span>                 xhr.responseText = docRoot ? docRoot.innerHTML : <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 676</span>                 xhr.responseXML = doc.XMLDocument ?<span style="color: rgba(0, 0, 0, 1)"> doc.XMLDocument : doc;
</span><span style="color: rgba(0, 128, 128, 1)"> 677</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (isXml) {
</span><span style="color: rgba(0, 128, 128, 1)"> 678</span>                     s.dataType = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">xml</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 679</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 680</span>                 xhr.getResponseHeader =<span style="color: rgba(0, 0, 0, 1)"> function(header){
</span><span style="color: rgba(0, 128, 128, 1)"> 681</span>                     <span style="color: rgba(0, 0, 255, 1)">var</span> headers = {<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">content-type</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">: s.dataType};
</span><span style="color: rgba(0, 128, 128, 1)"> 682</span>                     <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> headers[header.toLowerCase()];
</span><span style="color: rgba(0, 128, 128, 1)"> 683</span> <span style="color: rgba(0, 0, 0, 1)">                };
</span><span style="color: rgba(0, 128, 128, 1)"> 684</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> support for XHR 'status' &amp; 'statusText' emulation :</span>
<span style="color: rgba(0, 128, 128, 1)"> 685</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (docRoot) {
</span><span style="color: rgba(0, 128, 128, 1)"> 686</span>                     xhr.status = Number( docRoot.getAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">status</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ) ||<span style="color: rgba(0, 0, 0, 1)"> xhr.status;
</span><span style="color: rgba(0, 128, 128, 1)"> 687</span>                     xhr.statusText = docRoot.getAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">statusText</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ||<span style="color: rgba(0, 0, 0, 1)"> xhr.statusText;
</span><span style="color: rgba(0, 128, 128, 1)"> 688</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 689</span> 
<span style="color: rgba(0, 128, 128, 1)"> 690</span>                 <span style="color: rgba(0, 0, 255, 1)">var</span> dt = (s.dataType || <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">).toLowerCase();
</span><span style="color: rgba(0, 128, 128, 1)"> 691</span>                 <span style="color: rgba(0, 0, 255, 1)">var</span> scr = /(json|script|text)/<span style="color: rgba(0, 0, 0, 1)">.test(dt);
</span><span style="color: rgba(0, 128, 128, 1)"> 692</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (scr ||<span style="color: rgba(0, 0, 0, 1)"> s.textarea) {
</span><span style="color: rgba(0, 128, 128, 1)"> 693</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> see if user embedded response in textarea</span>
<span style="color: rgba(0, 128, 128, 1)"> 694</span>                     <span style="color: rgba(0, 0, 255, 1)">var</span> ta = doc.getElementsByTagName(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">textarea</span><span style="color: rgba(128, 0, 0, 1)">'</span>)[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 695</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (ta) {
</span><span style="color: rgba(0, 128, 128, 1)"> 696</span>                         xhr.responseText =<span style="color: rgba(0, 0, 0, 1)"> ta.value;
</span><span style="color: rgba(0, 128, 128, 1)"> 697</span>                         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> support for XHR 'status' &amp; 'statusText' emulation :</span>
<span style="color: rgba(0, 128, 128, 1)"> 698</span>                         xhr.status = Number( ta.getAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">status</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ) ||<span style="color: rgba(0, 0, 0, 1)"> xhr.status;
</span><span style="color: rgba(0, 128, 128, 1)"> 699</span>                         xhr.statusText = ta.getAttribute(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">statusText</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ||<span style="color: rgba(0, 0, 0, 1)"> xhr.statusText;
</span><span style="color: rgba(0, 128, 128, 1)"> 700</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)"> 701</span>                     <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (scr) {
</span><span style="color: rgba(0, 128, 128, 1)"> 702</span>                         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> account for browsers injecting pre around json response</span>
<span style="color: rgba(0, 128, 128, 1)"> 703</span>                         <span style="color: rgba(0, 0, 255, 1)">var</span> pre = doc.getElementsByTagName(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">pre</span><span style="color: rgba(128, 0, 0, 1)">'</span>)[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 704</span>                         <span style="color: rgba(0, 0, 255, 1)">var</span> b = doc.getElementsByTagName(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">body</span><span style="color: rgba(128, 0, 0, 1)">'</span>)[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 705</span>                         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (pre) {
</span><span style="color: rgba(0, 128, 128, 1)"> 706</span>                             xhr.responseText = pre.textContent ?<span style="color: rgba(0, 0, 0, 1)"> pre.textContent : pre.innerText;
</span><span style="color: rgba(0, 128, 128, 1)"> 707</span> <span style="color: rgba(0, 0, 0, 1)">                        }
</span><span style="color: rgba(0, 128, 128, 1)"> 708</span>                         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (b) {
</span><span style="color: rgba(0, 128, 128, 1)"> 709</span>                             xhr.responseText = b.textContent ?<span style="color: rgba(0, 0, 0, 1)"> b.textContent : b.innerText;
</span><span style="color: rgba(0, 128, 128, 1)"> 710</span> <span style="color: rgba(0, 0, 0, 1)">                        }
</span><span style="color: rgba(0, 128, 128, 1)"> 711</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)"> 712</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 713</span>                 <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (dt == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">xml</span><span style="color: rgba(128, 0, 0, 1)">'</span> &amp;&amp; !xhr.responseXML &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> xhr.responseText) {
</span><span style="color: rgba(0, 128, 128, 1)"> 714</span>                     xhr.responseXML =<span style="color: rgba(0, 0, 0, 1)"> toXml(xhr.responseText);
</span><span style="color: rgba(0, 128, 128, 1)"> 715</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 716</span> 
<span style="color: rgba(0, 128, 128, 1)"> 717</span>                 <span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 718</span>                     data =<span style="color: rgba(0, 0, 0, 1)"> httpData(xhr, dt, s);
</span><span style="color: rgba(0, 128, 128, 1)"> 719</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 720</span>                 <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (err) {
</span><span style="color: rgba(0, 128, 128, 1)"> 721</span>                     status = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">parsererror</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 722</span>                     xhr.error = errMsg = (err ||<span style="color: rgba(0, 0, 0, 1)"> status);
</span><span style="color: rgba(0, 128, 128, 1)"> 723</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 724</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 725</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (err) {
</span><span style="color: rgba(0, 128, 128, 1)"> 726</span>                 log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">error caught: </span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">,err);
</span><span style="color: rgba(0, 128, 128, 1)"> 727</span>                 status = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">error</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 728</span>                 xhr.error = errMsg = (err ||<span style="color: rgba(0, 0, 0, 1)"> status);
</span><span style="color: rgba(0, 128, 128, 1)"> 729</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 730</span> 
<span style="color: rgba(0, 128, 128, 1)"> 731</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (xhr.aborted) {
</span><span style="color: rgba(0, 128, 128, 1)"> 732</span>                 log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">upload aborted</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 733</span>                 status = <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 734</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 735</span> 
<span style="color: rgba(0, 128, 128, 1)"> 736</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (xhr.status) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> we've set xhr.status</span>
<span style="color: rgba(0, 128, 128, 1)"> 737</span>                 status = (xhr.status &gt;= <span style="color: rgba(128, 0, 128, 1)">200</span> &amp;&amp; xhr.status &lt; <span style="color: rgba(128, 0, 128, 1)">300</span> || xhr.status === <span style="color: rgba(128, 0, 128, 1)">304</span>) ? <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">success</span><span style="color: rgba(128, 0, 0, 1)">'</span> : <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">error</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 738</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 739</span> 
<span style="color: rgba(0, 128, 128, 1)"> 740</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> ordering of these callbacks/triggers is odd, but that's how $.ajax does it</span>
<span style="color: rgba(0, 128, 128, 1)"> 741</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (status === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">success</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 742</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.success) {
</span><span style="color: rgba(0, 128, 128, 1)"> 743</span>                     s.success.call(s.context, data, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">success</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, xhr);
</span><span style="color: rgba(0, 128, 128, 1)"> 744</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 745</span>                 deferred.resolve(xhr.responseText, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">success</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, xhr);
</span><span style="color: rgba(0, 128, 128, 1)"> 746</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (g) {
</span><span style="color: rgba(0, 128, 128, 1)"> 747</span>                     $.<span style="color: rgba(0, 0, 255, 1)">event</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ajaxSuccess</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">, [xhr, s]);
</span><span style="color: rgba(0, 128, 128, 1)"> 748</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 749</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 750</span>             <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (status) {
</span><span style="color: rgba(0, 128, 128, 1)"> 751</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (errMsg ===<span style="color: rgba(0, 0, 0, 1)"> undefined) {
</span><span style="color: rgba(0, 128, 128, 1)"> 752</span>                     errMsg =<span style="color: rgba(0, 0, 0, 1)"> xhr.statusText;
</span><span style="color: rgba(0, 128, 128, 1)"> 753</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 754</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.error) {
</span><span style="color: rgba(0, 128, 128, 1)"> 755</span> <span style="color: rgba(0, 0, 0, 1)">                    s.error.call(s.context, xhr, status, errMsg);
</span><span style="color: rgba(0, 128, 128, 1)"> 756</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 757</span>                 deferred.reject(xhr, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">error</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, errMsg);
</span><span style="color: rgba(0, 128, 128, 1)"> 758</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (g) {
</span><span style="color: rgba(0, 128, 128, 1)"> 759</span>                     $.<span style="color: rgba(0, 0, 255, 1)">event</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ajaxError</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">, [xhr, s, errMsg]);
</span><span style="color: rgba(0, 128, 128, 1)"> 760</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 761</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 762</span> 
<span style="color: rgba(0, 128, 128, 1)"> 763</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (g) {
</span><span style="color: rgba(0, 128, 128, 1)"> 764</span>                 $.<span style="color: rgba(0, 0, 255, 1)">event</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ajaxComplete</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">, [xhr, s]);
</span><span style="color: rgba(0, 128, 128, 1)"> 765</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 766</span> 
<span style="color: rgba(0, 128, 128, 1)"> 767</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (g &amp;&amp; ! --<span style="color: rgba(0, 0, 0, 1)">$.active) {
</span><span style="color: rgba(0, 128, 128, 1)"> 768</span>                 $.<span style="color: rgba(0, 0, 255, 1)">event</span>.trigger(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">ajaxStop</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 769</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 770</span> 
<span style="color: rgba(0, 128, 128, 1)"> 771</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.complete) {
</span><span style="color: rgba(0, 128, 128, 1)"> 772</span> <span style="color: rgba(0, 0, 0, 1)">                s.complete.call(s.context, xhr, status);
</span><span style="color: rgba(0, 128, 128, 1)"> 773</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 774</span> 
<span style="color: rgba(0, 128, 128, 1)"> 775</span>             callbackProcessed = <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 776</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (s.timeout) {
</span><span style="color: rgba(0, 128, 128, 1)"> 777</span> <span style="color: rgba(0, 0, 0, 1)">                clearTimeout(timeoutHandle);
</span><span style="color: rgba(0, 128, 128, 1)"> 778</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 779</span> 
<span style="color: rgba(0, 128, 128, 1)"> 780</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> clean up</span>
<span style="color: rgba(0, 128, 128, 1)"> 781</span> <span style="color: rgba(0, 0, 0, 1)">            setTimeout(function() {
</span><span style="color: rgba(0, 128, 128, 1)"> 782</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 0, 1)">s.iframeTarget) {
</span><span style="color: rgba(0, 128, 128, 1)"> 783</span> <span style="color: rgba(0, 0, 0, 1)">                    $io.remove();
</span><span style="color: rgba(0, 128, 128, 1)"> 784</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 785</span>                 <span style="color: rgba(0, 0, 255, 1)">else</span> { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">adding else to clean up existing iframe response.</span>
<span style="color: rgba(0, 128, 128, 1)"> 786</span>                     $io.attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">src</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, s.iframeSrc);
</span><span style="color: rgba(0, 128, 128, 1)"> 787</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 788</span>                 xhr.responseXML = <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 789</span>             }, <span style="color: rgba(128, 0, 128, 1)">100</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 790</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 791</span> 
<span style="color: rgba(0, 128, 128, 1)"> 792</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> toXml = $.parseXML || function(s, doc) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> use parseXML if available (jQuery 1.5+)</span>
<span style="color: rgba(0, 128, 128, 1)"> 793</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (window.ActiveXObject) {
</span><span style="color: rgba(0, 128, 128, 1)"> 794</span>                 doc = <span style="color: rgba(0, 0, 255, 1)">new</span> ActiveXObject(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">Microsoft.XMLDOM</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 795</span>                 doc.<span style="color: rgba(0, 0, 255, 1)">async</span> = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">false</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 796</span> <span style="color: rgba(0, 0, 0, 1)">                doc.loadXML(s);
</span><span style="color: rgba(0, 128, 128, 1)"> 797</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 798</span>             <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 799</span>                 doc = (<span style="color: rgba(0, 0, 255, 1)">new</span> DOMParser()).parseFromString(s, <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">text/xml</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 800</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 801</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> (doc &amp;&amp; doc.documentElement &amp;&amp; doc.documentElement.nodeName != <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">parsererror</span><span style="color: rgba(128, 0, 0, 1)">'</span>) ? doc : <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 802</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)"> 803</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> parseJSON = $.parseJSON ||<span style="color: rgba(0, 0, 0, 1)"> function(s) {
</span><span style="color: rgba(0, 128, 128, 1)"> 804</span>             <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">jslint evil:true </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 805</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> window[<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">eval</span><span style="color: rgba(128, 0, 0, 1)">'</span>](<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">(</span><span style="color: rgba(128, 0, 0, 1)">'</span> + s + <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">)</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 806</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)"> 807</span> 
<span style="color: rgba(0, 128, 128, 1)"> 808</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> httpData = function( xhr, type, s ) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> mostly lifted from jq1.4.4</span>
<span style="color: rgba(0, 128, 128, 1)"> 809</span> 
<span style="color: rgba(0, 128, 128, 1)"> 810</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> ct = xhr.getResponseHeader(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">content-type</span><span style="color: rgba(128, 0, 0, 1)">'</span>) || <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 811</span>                 xml = type === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">xml</span><span style="color: rgba(128, 0, 0, 1)">'</span> || !type &amp;&amp; ct.indexOf(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">xml</span><span style="color: rgba(128, 0, 0, 1)">'</span>) &gt;= <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">,
</span><span style="color: rgba(0, 128, 128, 1)"> 812</span>                 data = xml ?<span style="color: rgba(0, 0, 0, 1)"> xhr.responseXML : xhr.responseText;
</span><span style="color: rgba(0, 128, 128, 1)"> 813</span> 
<span style="color: rgba(0, 128, 128, 1)"> 814</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (xml &amp;&amp; data.documentElement.nodeName === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">parsererror</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 815</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> ($.error) {
</span><span style="color: rgba(0, 128, 128, 1)"> 816</span>                     $.error(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">parsererror</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 817</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 818</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 819</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (s &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> s.dataFilter) {
</span><span style="color: rgba(0, 128, 128, 1)"> 820</span>                 data =<span style="color: rgba(0, 0, 0, 1)"> s.dataFilter(data, type);
</span><span style="color: rgba(0, 128, 128, 1)"> 821</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 822</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">typeof</span> data === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">string</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 823</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (type === <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">json</span><span style="color: rgba(128, 0, 0, 1)">'</span> || !type &amp;&amp; ct.indexOf(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">json</span><span style="color: rgba(128, 0, 0, 1)">'</span>) &gt;= <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 824</span>                     data =<span style="color: rgba(0, 0, 0, 1)"> parseJSON(data);
</span><span style="color: rgba(0, 128, 128, 1)"> 825</span>                 } <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (type === <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">script</span><span style="color: rgba(128, 0, 0, 1)">"</span> || !type &amp;&amp; ct.indexOf(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">javascript</span><span style="color: rgba(128, 0, 0, 1)">"</span>) &gt;= <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 826</span> <span style="color: rgba(0, 0, 0, 1)">                    $.globalEval(data);
</span><span style="color: rgba(0, 128, 128, 1)"> 827</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 828</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 829</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> data;
</span><span style="color: rgba(0, 128, 128, 1)"> 830</span> <span style="color: rgba(0, 0, 0, 1)">        };
</span><span style="color: rgba(0, 128, 128, 1)"> 831</span> 
<span style="color: rgba(0, 128, 128, 1)"> 832</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> deferred;
</span><span style="color: rgba(0, 128, 128, 1)"> 833</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 834</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)"> 835</span> 
<span style="color: rgba(0, 128, 128, 1)"> 836</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)"> 837</span> <span style="color: rgba(0, 128, 0, 1)"> * ajaxForm() provides a mechanism for fully automating form submission.
</span><span style="color: rgba(0, 128, 128, 1)"> 838</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)"> 839</span> <span style="color: rgba(0, 128, 0, 1)"> * The advantages of using this method instead of ajaxSubmit() are:
</span><span style="color: rgba(0, 128, 128, 1)"> 840</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)"> 841</span> <span style="color: rgba(0, 128, 0, 1)"> * 1: This method will include coordinates for &lt;input type="image" /&gt; elements (if the element
</span><span style="color: rgba(0, 128, 128, 1)"> 842</span> <span style="color: rgba(0, 128, 0, 1)"> *    is used to submit the form).
</span><span style="color: rgba(0, 128, 128, 1)"> 843</span> <span style="color: rgba(0, 128, 0, 1)"> * 2. This method will include the submit element's name/value data (for the element that was
</span><span style="color: rgba(0, 128, 128, 1)"> 844</span> <span style="color: rgba(0, 128, 0, 1)"> *    used to submit the form).
</span><span style="color: rgba(0, 128, 128, 1)"> 845</span> <span style="color: rgba(0, 128, 0, 1)"> * 3. This method binds the submit() method to the form for you.
</span><span style="color: rgba(0, 128, 128, 1)"> 846</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)"> 847</span> <span style="color: rgba(0, 128, 0, 1)"> * The options argument for ajaxForm works exactly as it does for ajaxSubmit.  ajaxForm merely
</span><span style="color: rgba(0, 128, 128, 1)"> 848</span> <span style="color: rgba(0, 128, 0, 1)"> * passes the options argument along after properly binding events for submit elements and
</span><span style="color: rgba(0, 128, 128, 1)"> 849</span> <span style="color: rgba(0, 128, 0, 1)"> * the form itself.
</span><span style="color: rgba(0, 128, 128, 1)"> 850</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 851</span> $.fn.ajaxForm =<span style="color: rgba(0, 0, 0, 1)"> function(options) {
</span><span style="color: rgba(0, 128, 128, 1)"> 852</span>     options = options ||<span style="color: rgba(0, 0, 0, 1)"> {};
</span><span style="color: rgba(0, 128, 128, 1)"> 853</span>     options.delegation = options.delegation &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> $.isFunction($.fn.on);
</span><span style="color: rgba(0, 128, 128, 1)"> 854</span> 
<span style="color: rgba(0, 128, 128, 1)"> 855</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> in jQuery 1.3+ we can fix mistakes with the ready state</span>
<span style="color: rgba(0, 128, 128, 1)"> 856</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!options.delegation &amp;&amp; <span style="color: rgba(0, 0, 255, 1)">this</span>.length === <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 857</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> o = { s: <span style="color: rgba(0, 0, 255, 1)">this</span>.selector, c: <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.context };
</span><span style="color: rgba(0, 128, 128, 1)"> 858</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (!$.isReady &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> o.s) {
</span><span style="color: rgba(0, 128, 128, 1)"> 859</span>             log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">DOM not ready, queuing ajaxForm</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 860</span> <span style="color: rgba(0, 0, 0, 1)">            $(function() {
</span><span style="color: rgba(0, 128, 128, 1)"> 861</span> <span style="color: rgba(0, 0, 0, 1)">                $(o.s,o.c).ajaxForm(options);
</span><span style="color: rgba(0, 128, 128, 1)"> 862</span> <span style="color: rgba(0, 0, 0, 1)">            });
</span><span style="color: rgba(0, 128, 128, 1)"> 863</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 864</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 865</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> is your DOM ready?  </span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">http://docs.jquery.com/Tutorials</span><span style="color: rgba(0, 128, 0, 1)">:Introducing_$(document).ready()</span>
<span style="color: rgba(0, 128, 128, 1)"> 866</span>         log(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">terminating; zero elements found by selector</span><span style="color: rgba(128, 0, 0, 1)">'</span> + ($.isReady ? <span style="color: rgba(128, 0, 0, 1)">''</span> : <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)"> (DOM not ready)</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">));
</span><span style="color: rgba(0, 128, 128, 1)"> 867</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 868</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 869</span> 
<span style="color: rgba(0, 128, 128, 1)"> 870</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> ( options.delegation ) {
</span><span style="color: rgba(0, 128, 128, 1)"> 871</span> <span style="color: rgba(0, 0, 0, 1)">        $(document)
</span><span style="color: rgba(0, 128, 128, 1)"> 872</span>             .off(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">submit.form-plugin</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.selector, doAjaxSubmit)
</span><span style="color: rgba(0, 128, 128, 1)"> 873</span>             .off(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">click.form-plugin</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.selector, captureSubmittingElement)
</span><span style="color: rgba(0, 128, 128, 1)"> 874</span>             .on(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">submit.form-plugin</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.selector, options, doAjaxSubmit)
</span><span style="color: rgba(0, 128, 128, 1)"> 875</span>             .on(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">click.form-plugin</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.selector, options, captureSubmittingElement);
</span><span style="color: rgba(0, 128, 128, 1)"> 876</span>         <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 877</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 878</span> 
<span style="color: rgba(0, 128, 128, 1)"> 879</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.ajaxFormUnbind()
</span><span style="color: rgba(0, 128, 128, 1)"> 880</span>         .bind(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">submit.form-plugin</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, options, doAjaxSubmit)
</span><span style="color: rgba(0, 128, 128, 1)"> 881</span>         .bind(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">click.form-plugin</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, options, captureSubmittingElement);
</span><span style="color: rgba(0, 128, 128, 1)"> 882</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)"> 883</span> 
<span style="color: rgba(0, 128, 128, 1)"> 884</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> private event handlers</span>
<span style="color: rgba(0, 128, 128, 1)"> 885</span> <span style="color: rgba(0, 0, 0, 1)">function doAjaxSubmit(e) {
</span><span style="color: rgba(0, 128, 128, 1)"> 886</span>     <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">jshint validthis:true </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 887</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> options =<span style="color: rgba(0, 0, 0, 1)"> e.data;
</span><span style="color: rgba(0, 128, 128, 1)"> 888</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!e.isDefaultPrevented()) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> if event has been canceled, don't proceed</span>
<span style="color: rgba(0, 128, 128, 1)"> 889</span> <span style="color: rgba(0, 0, 0, 1)">        e.preventDefault();
</span><span style="color: rgba(0, 128, 128, 1)"> 890</span>         $(e.target).ajaxSubmit(options); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #365</span>
<span style="color: rgba(0, 128, 128, 1)"> 891</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 892</span> <span style="color: rgba(0, 0, 0, 1)">}
</span><span style="color: rgba(0, 128, 128, 1)"> 893</span> 
<span style="color: rgba(0, 128, 128, 1)"> 894</span> <span style="color: rgba(0, 0, 0, 1)">function captureSubmittingElement(e) {
</span><span style="color: rgba(0, 128, 128, 1)"> 895</span>     <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">jshint validthis:true </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 896</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> target =<span style="color: rgba(0, 0, 0, 1)"> e.target;
</span><span style="color: rgba(0, 128, 128, 1)"> 897</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> $el =<span style="color: rgba(0, 0, 0, 1)"> $(target);
</span><span style="color: rgba(0, 128, 128, 1)"> 898</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!($el.<span style="color: rgba(0, 0, 255, 1)">is</span>(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">[type=submit],[type=image]</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">))) {
</span><span style="color: rgba(0, 128, 128, 1)"> 899</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> is this a child element of the submit el?  (ex: a span within a button)</span>
<span style="color: rgba(0, 128, 128, 1)"> 900</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> t = $el.closest(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">[type=submit]</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 901</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (t.length === <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 902</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 903</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 904</span>         target = t[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 905</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 906</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> form = <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 907</span>     form.clk =<span style="color: rgba(0, 0, 0, 1)"> target;
</span><span style="color: rgba(0, 128, 128, 1)"> 908</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (target.type == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">image</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 909</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (e.offsetX !==<span style="color: rgba(0, 0, 0, 1)"> undefined) {
</span><span style="color: rgba(0, 128, 128, 1)"> 910</span>             form.clk_x =<span style="color: rgba(0, 0, 0, 1)"> e.offsetX;
</span><span style="color: rgba(0, 128, 128, 1)"> 911</span>             form.clk_y =<span style="color: rgba(0, 0, 0, 1)"> e.offsetY;
</span><span style="color: rgba(0, 128, 128, 1)"> 912</span>         } <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">typeof</span> $.fn.offset == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">function</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 913</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> offset =<span style="color: rgba(0, 0, 0, 1)"> $el.offset();
</span><span style="color: rgba(0, 128, 128, 1)"> 914</span>             form.clk_x = e.pageX -<span style="color: rgba(0, 0, 0, 1)"> offset.left;
</span><span style="color: rgba(0, 128, 128, 1)"> 915</span>             form.clk_y = e.pageY -<span style="color: rgba(0, 0, 0, 1)"> offset.top;
</span><span style="color: rgba(0, 128, 128, 1)"> 916</span>         } <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)"> 917</span>             form.clk_x = e.pageX -<span style="color: rgba(0, 0, 0, 1)"> target.offsetLeft;
</span><span style="color: rgba(0, 128, 128, 1)"> 918</span>             form.clk_y = e.pageY -<span style="color: rgba(0, 0, 0, 1)"> target.offsetTop;
</span><span style="color: rgba(0, 128, 128, 1)"> 919</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 920</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 921</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> clear form vars</span>
<span style="color: rgba(0, 128, 128, 1)"> 922</span>     setTimeout(function() { form.clk = form.clk_x = form.clk_y = <span style="color: rgba(0, 0, 255, 1)">null</span>; }, <span style="color: rgba(128, 0, 128, 1)">100</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 923</span> <span style="color: rgba(0, 0, 0, 1)">}
</span><span style="color: rgba(0, 128, 128, 1)"> 924</span> 
<span style="color: rgba(0, 128, 128, 1)"> 925</span> 
<span style="color: rgba(0, 128, 128, 1)"> 926</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> ajaxFormUnbind unbinds the event handlers that were bound by ajaxForm</span>
<span style="color: rgba(0, 128, 128, 1)"> 927</span> $.fn.ajaxFormUnbind =<span style="color: rgba(0, 0, 0, 1)"> function() {
</span><span style="color: rgba(0, 128, 128, 1)"> 928</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span>.unbind(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">submit.form-plugin click.form-plugin</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 929</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)"> 930</span> 
<span style="color: rgba(0, 128, 128, 1)"> 931</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)"> 932</span> <span style="color: rgba(0, 128, 0, 1)"> * formToArray() gathers form element data into an array of objects that can
</span><span style="color: rgba(0, 128, 128, 1)"> 933</span> <span style="color: rgba(0, 128, 0, 1)"> * be passed to any of the following ajax functions: $.get, $.post, or load.
</span><span style="color: rgba(0, 128, 128, 1)"> 934</span> <span style="color: rgba(0, 128, 0, 1)"> * Each object in the array has both a 'name' and 'value' property.  An example of
</span><span style="color: rgba(0, 128, 128, 1)"> 935</span> <span style="color: rgba(0, 128, 0, 1)"> * an array for a simple login form might be:
</span><span style="color: rgba(0, 128, 128, 1)"> 936</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)"> 937</span> <span style="color: rgba(0, 128, 0, 1)"> * [ { name: 'username', value: 'jresig' }, { name: 'password', value: 'secret' } ]
</span><span style="color: rgba(0, 128, 128, 1)"> 938</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)"> 939</span> <span style="color: rgba(0, 128, 0, 1)"> * It is this array that is passed to pre-submit callback functions provided to the
</span><span style="color: rgba(0, 128, 128, 1)"> 940</span> <span style="color: rgba(0, 128, 0, 1)"> * ajaxSubmit() and ajaxForm() methods.
</span><span style="color: rgba(0, 128, 128, 1)"> 941</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)"> 942</span> $.fn.formToArray =<span style="color: rgba(0, 0, 0, 1)"> function(semantic, elements) {
</span><span style="color: rgba(0, 128, 128, 1)"> 943</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> a =<span style="color: rgba(0, 0, 0, 1)"> [];
</span><span style="color: rgba(0, 128, 128, 1)"> 944</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">this</span>.length === <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 945</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> a;
</span><span style="color: rgba(0, 128, 128, 1)"> 946</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 947</span> 
<span style="color: rgba(0, 128, 128, 1)"> 948</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> form = <span style="color: rgba(0, 0, 255, 1)">this</span>[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 949</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> formId = <span style="color: rgba(0, 0, 255, 1)">this</span>.attr(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">id</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 950</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> els = semantic ? form.getElementsByTagName(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">*</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) : form.elements;
</span><span style="color: rgba(0, 128, 128, 1)"> 951</span>     <span style="color: rgba(0, 0, 255, 1)">var</span><span style="color: rgba(0, 0, 0, 1)"> els2;
</span><span style="color: rgba(0, 128, 128, 1)"> 952</span> 
<span style="color: rgba(0, 128, 128, 1)"> 953</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (els &amp;&amp; !/MSIE [<span style="color: rgba(128, 0, 128, 1)">678</span>]/.test(navigator.userAgent)) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #390</span>
<span style="color: rgba(0, 128, 128, 1)"> 954</span>         els = $(els).<span style="color: rgba(0, 0, 255, 1)">get</span>();  <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> convert to standard array</span>
<span style="color: rgba(0, 128, 128, 1)"> 955</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 956</span> 
<span style="color: rgba(0, 128, 128, 1)"> 957</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #386; account for inputs outside the form which use the 'form' attribute</span>
<span style="color: rgba(0, 128, 128, 1)"> 958</span>     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> ( formId ) {
</span><span style="color: rgba(0, 128, 128, 1)"> 959</span>         els2 = $(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">:input[form="</span><span style="color: rgba(128, 0, 0, 1)">'</span> + formId + <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">"]</span><span style="color: rgba(128, 0, 0, 1)">'</span>).<span style="color: rgba(0, 0, 255, 1)">get</span>(); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> hat tip @thet</span>
<span style="color: rgba(0, 128, 128, 1)"> 960</span>         <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> ( els2.length ) {
</span><span style="color: rgba(0, 128, 128, 1)"> 961</span>             els = (els ||<span style="color: rgba(0, 0, 0, 1)"> []).concat(els2);
</span><span style="color: rgba(0, 128, 128, 1)"> 962</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 963</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 964</span> 
<span style="color: rgba(0, 128, 128, 1)"> 965</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!els || !<span style="color: rgba(0, 0, 0, 1)">els.length) {
</span><span style="color: rgba(0, 128, 128, 1)"> 966</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> a;
</span><span style="color: rgba(0, 128, 128, 1)"> 967</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)"> 968</span> 
<span style="color: rgba(0, 128, 128, 1)"> 969</span>     <span style="color: rgba(0, 0, 255, 1)">var</span><span style="color: rgba(0, 0, 0, 1)"> i,j,n,v,el,max,jmax;
</span><span style="color: rgba(0, 128, 128, 1)"> 970</span>     <span style="color: rgba(0, 0, 255, 1)">for</span>(i=<span style="color: rgba(128, 0, 128, 1)">0</span>, max=els.length; i &lt; max; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 971</span>         el =<span style="color: rgba(0, 0, 0, 1)"> els[i];
</span><span style="color: rgba(0, 128, 128, 1)"> 972</span>         n =<span style="color: rgba(0, 0, 0, 1)"> el.name;
</span><span style="color: rgba(0, 128, 128, 1)"> 973</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (!n ||<span style="color: rgba(0, 0, 0, 1)"> el.disabled) {
</span><span style="color: rgba(0, 128, 128, 1)"> 974</span>             <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 975</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 976</span> 
<span style="color: rgba(0, 128, 128, 1)"> 977</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (semantic &amp;&amp; form.clk &amp;&amp; el.type == <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">image</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 978</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> handle image inputs on the fly when semantic == true</span>
<span style="color: rgba(0, 128, 128, 1)"> 979</span>             <span style="color: rgba(0, 0, 255, 1)">if</span>(form.clk ==<span style="color: rgba(0, 0, 0, 1)"> el) {
</span><span style="color: rgba(0, 128, 128, 1)"> 980</span> <span style="color: rgba(0, 0, 0, 1)">                a.push({name: n, value: $(el).val(), type: el.type });
</span><span style="color: rgba(0, 128, 128, 1)"> 981</span>                 a.push({name: n+<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">.x</span><span style="color: rgba(128, 0, 0, 1)">'</span>, value: form.clk_x}, {name: n+<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">.y</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, value: form.clk_y});
</span><span style="color: rgba(0, 128, 128, 1)"> 982</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 983</span>             <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 984</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 985</span> 
<span style="color: rgba(0, 128, 128, 1)"> 986</span>         v = $.fieldValue(el, <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)"> 987</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (v &amp;&amp; v.constructor ==<span style="color: rgba(0, 0, 0, 1)"> Array) {
</span><span style="color: rgba(0, 128, 128, 1)"> 988</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (elements) {
</span><span style="color: rgba(0, 128, 128, 1)"> 989</span> <span style="color: rgba(0, 0, 0, 1)">                elements.push(el);
</span><span style="color: rgba(0, 128, 128, 1)"> 990</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 991</span>             <span style="color: rgba(0, 0, 255, 1)">for</span>(j=<span style="color: rgba(128, 0, 128, 1)">0</span>, jmax=v.length; j &lt; jmax; j++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 992</span> <span style="color: rgba(0, 0, 0, 1)">                a.push({name: n, value: v[j]});
</span><span style="color: rgba(0, 128, 128, 1)"> 993</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 994</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 995</span>         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (feature.fileapi &amp;&amp; el.type == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">file</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)"> 996</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (elements) {
</span><span style="color: rgba(0, 128, 128, 1)"> 997</span> <span style="color: rgba(0, 0, 0, 1)">                elements.push(el);
</span><span style="color: rgba(0, 128, 128, 1)"> 998</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 999</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> files =<span style="color: rgba(0, 0, 0, 1)"> el.files;
</span><span style="color: rgba(0, 128, 128, 1)">1000</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (files.length) {
</span><span style="color: rgba(0, 128, 128, 1)">1001</span>                 <span style="color: rgba(0, 0, 255, 1)">for</span> (j=<span style="color: rgba(128, 0, 128, 1)">0</span>; j &lt; files.length; j++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1002</span> <span style="color: rgba(0, 0, 0, 1)">                    a.push({name: n, value: files[j], type: el.type});
</span><span style="color: rgba(0, 128, 128, 1)">1003</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">1004</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">1005</span>             <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)">1006</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> #180</span>
<span style="color: rgba(0, 128, 128, 1)">1007</span>                 a.push({ name: n, value: <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">, type: el.type });
</span><span style="color: rgba(0, 128, 128, 1)">1008</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">1009</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1010</span>         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (v !== <span style="color: rgba(0, 0, 255, 1)">null</span> &amp;&amp; <span style="color: rgba(0, 0, 255, 1)">typeof</span> v != <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">undefined</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1011</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (elements) {
</span><span style="color: rgba(0, 128, 128, 1)">1012</span> <span style="color: rgba(0, 0, 0, 1)">                elements.push(el);
</span><span style="color: rgba(0, 128, 128, 1)">1013</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">1014</span> <span style="color: rgba(0, 0, 0, 1)">            a.push({name: n, value: v, type: el.type, required: el.required});
</span><span style="color: rgba(0, 128, 128, 1)">1015</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1016</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1017</span> 
<span style="color: rgba(0, 128, 128, 1)">1018</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!semantic &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> form.clk) {
</span><span style="color: rgba(0, 128, 128, 1)">1019</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> input type=='image' are not found in elements array! handle it here</span>
<span style="color: rgba(0, 128, 128, 1)">1020</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> $input = $(form.clk), input = $input[<span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)">1021</span>         n =<span style="color: rgba(0, 0, 0, 1)"> input.name;
</span><span style="color: rgba(0, 128, 128, 1)">1022</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (n &amp;&amp; !input.disabled &amp;&amp; input.type == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">image</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1023</span> <span style="color: rgba(0, 0, 0, 1)">            a.push({name: n, value: $input.val()});
</span><span style="color: rgba(0, 128, 128, 1)">1024</span>             a.push({name: n+<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">.x</span><span style="color: rgba(128, 0, 0, 1)">'</span>, value: form.clk_x}, {name: n+<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">.y</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">, value: form.clk_y});
</span><span style="color: rgba(0, 128, 128, 1)">1025</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1026</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1027</span>     <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> a;
</span><span style="color: rgba(0, 128, 128, 1)">1028</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1029</span> 
<span style="color: rgba(0, 128, 128, 1)">1030</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1031</span> <span style="color: rgba(0, 128, 0, 1)"> * Serializes form data into a 'submittable' string. This method will return a string
</span><span style="color: rgba(0, 128, 128, 1)">1032</span> <span style="color: rgba(0, 128, 0, 1)"> * in the format: name1=value1&amp;amp;name2=value2
</span><span style="color: rgba(0, 128, 128, 1)">1033</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1034</span> $.fn.formSerialize =<span style="color: rgba(0, 0, 0, 1)"> function(semantic) {
</span><span style="color: rgba(0, 128, 128, 1)">1035</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">hand off to jQuery.param for proper encoding</span>
<span style="color: rgba(0, 128, 128, 1)">1036</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> $.param(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.formToArray(semantic));
</span><span style="color: rgba(0, 128, 128, 1)">1037</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1038</span> 
<span style="color: rgba(0, 128, 128, 1)">1039</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1040</span> <span style="color: rgba(0, 128, 0, 1)"> * Serializes all field elements in the jQuery object into a query string.
</span><span style="color: rgba(0, 128, 128, 1)">1041</span> <span style="color: rgba(0, 128, 0, 1)"> * This method will return a string in the format: name1=value1&amp;amp;name2=value2
</span><span style="color: rgba(0, 128, 128, 1)">1042</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1043</span> $.fn.fieldSerialize =<span style="color: rgba(0, 0, 0, 1)"> function(successful) {
</span><span style="color: rgba(0, 128, 128, 1)">1044</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> a =<span style="color: rgba(0, 0, 0, 1)"> [];
</span><span style="color: rgba(0, 128, 128, 1)">1045</span>     <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.each(function() {
</span><span style="color: rgba(0, 128, 128, 1)">1046</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> n = <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.name;
</span><span style="color: rgba(0, 128, 128, 1)">1047</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 0, 1)">n) {
</span><span style="color: rgba(0, 128, 128, 1)">1048</span>             <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1049</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1050</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> v = $.fieldValue(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">, successful);
</span><span style="color: rgba(0, 128, 128, 1)">1051</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (v &amp;&amp; v.constructor ==<span style="color: rgba(0, 0, 0, 1)"> Array) {
</span><span style="color: rgba(0, 128, 128, 1)">1052</span>             <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">var</span> i=<span style="color: rgba(128, 0, 128, 1)">0</span>,max=v.length; i &lt; max; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1053</span> <span style="color: rgba(0, 0, 0, 1)">                a.push({name: n, value: v[i]});
</span><span style="color: rgba(0, 128, 128, 1)">1054</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">1055</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1056</span>         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (v !== <span style="color: rgba(0, 0, 255, 1)">null</span> &amp;&amp; <span style="color: rgba(0, 0, 255, 1)">typeof</span> v != <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">undefined</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1057</span>             a.push({name: <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.name, value: v});
</span><span style="color: rgba(0, 128, 128, 1)">1058</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1059</span> <span style="color: rgba(0, 0, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">1060</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">hand off to jQuery.param for proper encoding</span>
<span style="color: rgba(0, 128, 128, 1)">1061</span>     <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> $.param(a);
</span><span style="color: rgba(0, 128, 128, 1)">1062</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1063</span> 
<span style="color: rgba(0, 128, 128, 1)">1064</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1065</span> <span style="color: rgba(0, 128, 0, 1)"> * Returns the value(s) of the element in the matched set.  For example, consider the following form:
</span><span style="color: rgba(0, 128, 128, 1)">1066</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)">1067</span> <span style="color: rgba(0, 128, 0, 1)"> *  &lt;form&gt;&lt;fieldset&gt;
</span><span style="color: rgba(0, 128, 128, 1)">1068</span> <span style="color: rgba(0, 128, 0, 1)"> *      &lt;input name="A" type="text" /&gt;
</span><span style="color: rgba(0, 128, 128, 1)">1069</span> <span style="color: rgba(0, 128, 0, 1)"> *      &lt;input name="A" type="text" /&gt;
</span><span style="color: rgba(0, 128, 128, 1)">1070</span> <span style="color: rgba(0, 128, 0, 1)"> *      &lt;input name="B" type="checkbox" value="B1" /&gt;
</span><span style="color: rgba(0, 128, 128, 1)">1071</span> <span style="color: rgba(0, 128, 0, 1)"> *      &lt;input name="B" type="checkbox" value="B2"/&gt;
</span><span style="color: rgba(0, 128, 128, 1)">1072</span> <span style="color: rgba(0, 128, 0, 1)"> *      &lt;input name="C" type="radio" value="C1" /&gt;
</span><span style="color: rgba(0, 128, 128, 1)">1073</span> <span style="color: rgba(0, 128, 0, 1)"> *      &lt;input name="C" type="radio" value="C2" /&gt;
</span><span style="color: rgba(0, 128, 128, 1)">1074</span> <span style="color: rgba(0, 128, 0, 1)"> *  &lt;/fieldset&gt;&lt;/form&gt;
</span><span style="color: rgba(0, 128, 128, 1)">1075</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)">1076</span> <span style="color: rgba(0, 128, 0, 1)"> *  var v = $('input[type=text]').fieldValue();
</span><span style="color: rgba(0, 128, 128, 1)">1077</span> <span style="color: rgba(0, 128, 0, 1)"> *  // if no values are entered into the text inputs
</span><span style="color: rgba(0, 128, 128, 1)">1078</span> <span style="color: rgba(0, 128, 0, 1)"> *  v == ['','']
</span><span style="color: rgba(0, 128, 128, 1)">1079</span> <span style="color: rgba(0, 128, 0, 1)"> *  // if values entered into the text inputs are 'foo' and 'bar'
</span><span style="color: rgba(0, 128, 128, 1)">1080</span> <span style="color: rgba(0, 128, 0, 1)"> *  v == ['foo','bar']
</span><span style="color: rgba(0, 128, 128, 1)">1081</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)">1082</span> <span style="color: rgba(0, 128, 0, 1)"> *  var v = $('input[type=checkbox]').fieldValue();
</span><span style="color: rgba(0, 128, 128, 1)">1083</span> <span style="color: rgba(0, 128, 0, 1)"> *  // if neither checkbox is checked
</span><span style="color: rgba(0, 128, 128, 1)">1084</span> <span style="color: rgba(0, 128, 0, 1)"> *  v === undefined
</span><span style="color: rgba(0, 128, 128, 1)">1085</span> <span style="color: rgba(0, 128, 0, 1)"> *  // if both checkboxes are checked
</span><span style="color: rgba(0, 128, 128, 1)">1086</span> <span style="color: rgba(0, 128, 0, 1)"> *  v == ['B1', 'B2']
</span><span style="color: rgba(0, 128, 128, 1)">1087</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)">1088</span> <span style="color: rgba(0, 128, 0, 1)"> *  var v = $('input[type=radio]').fieldValue();
</span><span style="color: rgba(0, 128, 128, 1)">1089</span> <span style="color: rgba(0, 128, 0, 1)"> *  // if neither radio is checked
</span><span style="color: rgba(0, 128, 128, 1)">1090</span> <span style="color: rgba(0, 128, 0, 1)"> *  v === undefined
</span><span style="color: rgba(0, 128, 128, 1)">1091</span> <span style="color: rgba(0, 128, 0, 1)"> *  // if first radio is checked
</span><span style="color: rgba(0, 128, 128, 1)">1092</span> <span style="color: rgba(0, 128, 0, 1)"> *  v == ['C1']
</span><span style="color: rgba(0, 128, 128, 1)">1093</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)">1094</span> <span style="color: rgba(0, 128, 0, 1)"> * The successful argument controls whether or not the field element must be 'successful'
</span><span style="color: rgba(0, 128, 128, 1)">1095</span> <span style="color: rgba(0, 128, 0, 1)"> * (per </span><span style="color: rgba(0, 128, 0, 1); text-decoration: underline">http://www.w3.org/TR/html4/interact/forms.html</span><span style="color: rgba(0, 128, 0, 1)">#successful-controls).
</span><span style="color: rgba(0, 128, 128, 1)">1096</span> <span style="color: rgba(0, 128, 0, 1)"> * The default value of the successful argument is true.  If this value is false the value(s)
</span><span style="color: rgba(0, 128, 128, 1)">1097</span> <span style="color: rgba(0, 128, 0, 1)"> * for each element is returned.
</span><span style="color: rgba(0, 128, 128, 1)">1098</span> <span style="color: rgba(0, 128, 0, 1)"> *
</span><span style="color: rgba(0, 128, 128, 1)">1099</span> <span style="color: rgba(0, 128, 0, 1)"> * Note: This method *always* returns an array.  If no valid value can be determined the
</span><span style="color: rgba(0, 128, 128, 1)">1100</span> <span style="color: rgba(0, 128, 0, 1)"> *    array will be empty, otherwise it will contain one or more values.
</span><span style="color: rgba(0, 128, 128, 1)">1101</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1102</span> $.fn.fieldValue =<span style="color: rgba(0, 0, 0, 1)"> function(successful) {
</span><span style="color: rgba(0, 128, 128, 1)">1103</span>     <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">var</span> val=[], i=<span style="color: rgba(128, 0, 128, 1)">0</span>, max=<span style="color: rgba(0, 0, 255, 1)">this</span>.length; i &lt; max; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1104</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> el = <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">[i];
</span><span style="color: rgba(0, 128, 128, 1)">1105</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> v =<span style="color: rgba(0, 0, 0, 1)"> $.fieldValue(el, successful);
</span><span style="color: rgba(0, 128, 128, 1)">1106</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (v === <span style="color: rgba(0, 0, 255, 1)">null</span> || <span style="color: rgba(0, 0, 255, 1)">typeof</span> v == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">undefined</span><span style="color: rgba(128, 0, 0, 1)">'</span> || (v.constructor == Array &amp;&amp; !<span style="color: rgba(0, 0, 0, 1)">v.length)) {
</span><span style="color: rgba(0, 128, 128, 1)">1107</span>             <span style="color: rgba(0, 0, 255, 1)">continue</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1108</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1109</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (v.constructor ==<span style="color: rgba(0, 0, 0, 1)"> Array) {
</span><span style="color: rgba(0, 128, 128, 1)">1110</span> <span style="color: rgba(0, 0, 0, 1)">            $.merge(val, v);
</span><span style="color: rgba(0, 128, 128, 1)">1111</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1112</span>         <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)">1113</span> <span style="color: rgba(0, 0, 0, 1)">            val.push(v);
</span><span style="color: rgba(0, 128, 128, 1)">1114</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1115</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1116</span>     <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> val;
</span><span style="color: rgba(0, 128, 128, 1)">1117</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1118</span> 
<span style="color: rgba(0, 128, 128, 1)">1119</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1120</span> <span style="color: rgba(0, 128, 0, 1)"> * Returns the value of the field element.
</span><span style="color: rgba(0, 128, 128, 1)">1121</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1122</span> $.fieldValue =<span style="color: rgba(0, 0, 0, 1)"> function(el, successful) {
</span><span style="color: rgba(0, 128, 128, 1)">1123</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> n = el.name, t = el.type, tag =<span style="color: rgba(0, 0, 0, 1)"> el.tagName.toLowerCase();
</span><span style="color: rgba(0, 128, 128, 1)">1124</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (successful ===<span style="color: rgba(0, 0, 0, 1)"> undefined) {
</span><span style="color: rgba(0, 128, 128, 1)">1125</span>         successful = <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1126</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1127</span> 
<span style="color: rgba(0, 128, 128, 1)">1128</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (successful &amp;&amp; (!n || el.disabled || t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">reset</span><span style="color: rgba(128, 0, 0, 1)">'</span> || t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">button</span><span style="color: rgba(128, 0, 0, 1)">'</span> ||
<span style="color: rgba(0, 128, 128, 1)">1129</span>         (t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">checkbox</span><span style="color: rgba(128, 0, 0, 1)">'</span> || t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">radio</span><span style="color: rgba(128, 0, 0, 1)">'</span>) &amp;&amp; !el.<span style="color: rgba(0, 0, 255, 1)">checked</span> ||
<span style="color: rgba(0, 128, 128, 1)">1130</span>         (t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">submit</span><span style="color: rgba(128, 0, 0, 1)">'</span> || t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">image</span><span style="color: rgba(128, 0, 0, 1)">'</span>) &amp;&amp; el.form &amp;&amp; el.form.clk != el ||
<span style="color: rgba(0, 128, 128, 1)">1131</span>         tag == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">select</span><span style="color: rgba(128, 0, 0, 1)">'</span> &amp;&amp; el.selectedIndex == -<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">)) {
</span><span style="color: rgba(0, 128, 128, 1)">1132</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1133</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1134</span> 
<span style="color: rgba(0, 128, 128, 1)">1135</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (tag == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">select</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1136</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> index =<span style="color: rgba(0, 0, 0, 1)"> el.selectedIndex;
</span><span style="color: rgba(0, 128, 128, 1)">1137</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (index &lt; <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1138</span>             <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1139</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1140</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> a = [], ops =<span style="color: rgba(0, 0, 0, 1)"> el.options;
</span><span style="color: rgba(0, 128, 128, 1)">1141</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> one = (t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">select-one</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">1142</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> max = (one ? index+<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)"> : ops.length);
</span><span style="color: rgba(0, 128, 128, 1)">1143</span>         <span style="color: rgba(0, 0, 255, 1)">for</span>(<span style="color: rgba(0, 0, 255, 1)">var</span> i=(one ? index : <span style="color: rgba(128, 0, 128, 1)">0</span>); i &lt; max; i++<span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1144</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> op =<span style="color: rgba(0, 0, 0, 1)"> ops[i];
</span><span style="color: rgba(0, 128, 128, 1)">1145</span>             <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (op.selected) {
</span><span style="color: rgba(0, 128, 128, 1)">1146</span>                 <span style="color: rgba(0, 0, 255, 1)">var</span> v =<span style="color: rgba(0, 0, 0, 1)"> op.value;
</span><span style="color: rgba(0, 128, 128, 1)">1147</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span> (!v) { <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> extra pain for IE...</span>
<span style="color: rgba(0, 128, 128, 1)">1148</span>                     v = (op.attributes &amp;&amp; op.attributes.value &amp;&amp; !(op.attributes.value.specified)) ?<span style="color: rgba(0, 0, 0, 1)"> op.text : op.value;
</span><span style="color: rgba(0, 128, 128, 1)">1149</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">1150</span>                 <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (one) {
</span><span style="color: rgba(0, 128, 128, 1)">1151</span>                     <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> v;
</span><span style="color: rgba(0, 128, 128, 1)">1152</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">1153</span> <span style="color: rgba(0, 0, 0, 1)">                a.push(v);
</span><span style="color: rgba(0, 128, 128, 1)">1154</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">1155</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1156</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> a;
</span><span style="color: rgba(0, 128, 128, 1)">1157</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1158</span>     <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> $(el).val();
</span><span style="color: rgba(0, 128, 128, 1)">1159</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1160</span> 
<span style="color: rgba(0, 128, 128, 1)">1161</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1162</span> <span style="color: rgba(0, 128, 0, 1)"> * Clears the form data.  Takes the following actions on the form's input fields:
</span><span style="color: rgba(0, 128, 128, 1)">1163</span> <span style="color: rgba(0, 128, 0, 1)"> *  - input text fields will have their 'value' property set to the empty string
</span><span style="color: rgba(0, 128, 128, 1)">1164</span> <span style="color: rgba(0, 128, 0, 1)"> *  - select elements will have their 'selectedIndex' property set to -1
</span><span style="color: rgba(0, 128, 128, 1)">1165</span> <span style="color: rgba(0, 128, 0, 1)"> *  - checkbox and radio inputs will have their 'checked' property set to false
</span><span style="color: rgba(0, 128, 128, 1)">1166</span> <span style="color: rgba(0, 128, 0, 1)"> *  - inputs of type submit, button, reset, and hidden will *not* be effected
</span><span style="color: rgba(0, 128, 128, 1)">1167</span> <span style="color: rgba(0, 128, 0, 1)"> *  - button elements will *not* be effected
</span><span style="color: rgba(0, 128, 128, 1)">1168</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1169</span> $.fn.clearForm =<span style="color: rgba(0, 0, 0, 1)"> function(includeHidden) {
</span><span style="color: rgba(0, 128, 128, 1)">1170</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.each(function() {
</span><span style="color: rgba(0, 128, 128, 1)">1171</span>         $(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">input,select,textarea</span><span style="color: rgba(128, 0, 0, 1)">'</span>, <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">).clearFields(includeHidden);
</span><span style="color: rgba(0, 128, 128, 1)">1172</span> <span style="color: rgba(0, 0, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">1173</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1174</span> 
<span style="color: rgba(0, 128, 128, 1)">1175</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1176</span> <span style="color: rgba(0, 128, 0, 1)"> * Clears the selected form elements.
</span><span style="color: rgba(0, 128, 128, 1)">1177</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1178</span> $.fn.clearFields = $.fn.clearInputs =<span style="color: rgba(0, 0, 0, 1)"> function(includeHidden) {
</span><span style="color: rgba(0, 128, 128, 1)">1179</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> re = /^(?:color|date|datetime|email|month|number|password|range|search|tel|text|time|url|week)$/i; <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 'hidden' is not in this list</span>
<span style="color: rgba(0, 128, 128, 1)">1180</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.each(function() {
</span><span style="color: rgba(0, 128, 128, 1)">1181</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> t = <span style="color: rgba(0, 0, 255, 1)">this</span>.type, tag = <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.tagName.toLowerCase();
</span><span style="color: rgba(0, 128, 128, 1)">1182</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (re.test(t) || tag == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">textarea</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1183</span>             <span style="color: rgba(0, 0, 255, 1)">this</span>.value = <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1184</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1185</span>         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">checkbox</span><span style="color: rgba(128, 0, 0, 1)">'</span> || t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">radio</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1186</span>             <span style="color: rgba(0, 0, 255, 1)">this</span>.<span style="color: rgba(0, 0, 255, 1)">checked</span> = <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1187</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1188</span>         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (tag == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">select</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1189</span>             <span style="color: rgba(0, 0, 255, 1)">this</span>.selectedIndex = -<span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1190</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1191</span>         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (t == <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">file</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1192</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (/MSIE/<span style="color: rgba(0, 0, 0, 1)">.test(navigator.userAgent)) {
</span><span style="color: rgba(0, 128, 128, 1)">1193</span>                 $(<span style="color: rgba(0, 0, 255, 1)">this</span>).replaceWith($(<span style="color: rgba(0, 0, 255, 1)">this</span>).clone(<span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">));
</span><span style="color: rgba(0, 128, 128, 1)">1194</span>             } <span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
</span><span style="color: rgba(0, 128, 128, 1)">1195</span>                 $(<span style="color: rgba(0, 0, 255, 1)">this</span>).val(<span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">1196</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">1197</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1198</span>         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (includeHidden) {
</span><span style="color: rgba(0, 128, 128, 1)">1199</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> includeHidden can be the value true, or it can be a selector string
</span><span style="color: rgba(0, 128, 128, 1)">1200</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> indicating a special test; for example:
</span><span style="color: rgba(0, 128, 128, 1)">1201</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">  $('#myForm').clearForm('.special:hidden')
</span><span style="color: rgba(0, 128, 128, 1)">1202</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> the above would clean hidden inputs that have the class of 'special'</span>
<span style="color: rgba(0, 128, 128, 1)">1203</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> ( (includeHidden === <span style="color: rgba(0, 0, 255, 1)">true</span> &amp;&amp; /hidden/.test(t)) ||
<span style="color: rgba(0, 128, 128, 1)">1204</span>                  (<span style="color: rgba(0, 0, 255, 1)">typeof</span> includeHidden == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">string</span><span style="color: rgba(128, 0, 0, 1)">'</span> &amp;&amp; $(<span style="color: rgba(0, 0, 255, 1)">this</span>).<span style="color: rgba(0, 0, 255, 1)">is</span><span style="color: rgba(0, 0, 0, 1)">(includeHidden)) ) {
</span><span style="color: rgba(0, 128, 128, 1)">1205</span>                 <span style="color: rgba(0, 0, 255, 1)">this</span>.value = <span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1206</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">1207</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1208</span> <span style="color: rgba(0, 0, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">1209</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1210</span> 
<span style="color: rgba(0, 128, 128, 1)">1211</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1212</span> <span style="color: rgba(0, 128, 0, 1)"> * Resets the form data.  Causes all form elements to be reset to their original value.
</span><span style="color: rgba(0, 128, 128, 1)">1213</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1214</span> $.fn.resetForm =<span style="color: rgba(0, 0, 0, 1)"> function() {
</span><span style="color: rgba(0, 128, 128, 1)">1215</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.each(function() {
</span><span style="color: rgba(0, 128, 128, 1)">1216</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> guard against an input with the name of 'reset'
</span><span style="color: rgba(0, 128, 128, 1)">1217</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> note that IE reports the reset function as an 'object'</span>
<span style="color: rgba(0, 128, 128, 1)">1218</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">typeof</span> <span style="color: rgba(0, 0, 255, 1)">this</span>.reset == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">function</span><span style="color: rgba(128, 0, 0, 1)">'</span> || (<span style="color: rgba(0, 0, 255, 1)">typeof</span> <span style="color: rgba(0, 0, 255, 1)">this</span>.reset == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">object</span><span style="color: rgba(128, 0, 0, 1)">'</span> &amp;&amp; !<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.reset.nodeType)) {
</span><span style="color: rgba(0, 128, 128, 1)">1219</span>             <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.reset();
</span><span style="color: rgba(0, 128, 128, 1)">1220</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1221</span> <span style="color: rgba(0, 0, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">1222</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1223</span> 
<span style="color: rgba(0, 128, 128, 1)">1224</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1225</span> <span style="color: rgba(0, 128, 0, 1)"> * Enables or disables any matching elements.
</span><span style="color: rgba(0, 128, 128, 1)">1226</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1227</span> $.fn.enable =<span style="color: rgba(0, 0, 0, 1)"> function(b) {
</span><span style="color: rgba(0, 128, 128, 1)">1228</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (b ===<span style="color: rgba(0, 0, 0, 1)"> undefined) {
</span><span style="color: rgba(0, 128, 128, 1)">1229</span>         b = <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1230</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1231</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.each(function() {
</span><span style="color: rgba(0, 128, 128, 1)">1232</span>         <span style="color: rgba(0, 0, 255, 1)">this</span>.disabled = !<span style="color: rgba(0, 0, 0, 1)">b;
</span><span style="color: rgba(0, 128, 128, 1)">1233</span> <span style="color: rgba(0, 0, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">1234</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1235</span> 
<span style="color: rgba(0, 128, 128, 1)">1236</span> <span style="color: rgba(0, 128, 0, 1)">/*</span><span style="color: rgba(0, 128, 0, 1)">*
</span><span style="color: rgba(0, 128, 128, 1)">1237</span> <span style="color: rgba(0, 128, 0, 1)"> * Checks/unchecks any matching checkboxes or radio buttons and
</span><span style="color: rgba(0, 128, 128, 1)">1238</span> <span style="color: rgba(0, 128, 0, 1)"> * selects/deselects and matching option elements.
</span><span style="color: rgba(0, 128, 128, 1)">1239</span>  <span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 128, 128, 1)">1240</span> $.fn.selected = function(<span style="color: rgba(0, 0, 255, 1)">select</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1241</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">select</span> ===<span style="color: rgba(0, 0, 0, 1)"> undefined) {
</span><span style="color: rgba(0, 128, 128, 1)">1242</span>         <span style="color: rgba(0, 0, 255, 1)">select</span> = <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1243</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1244</span>     <span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.each(function() {
</span><span style="color: rgba(0, 128, 128, 1)">1245</span>         <span style="color: rgba(0, 0, 255, 1)">var</span> t = <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.type;
</span><span style="color: rgba(0, 128, 128, 1)">1246</span>         <span style="color: rgba(0, 0, 255, 1)">if</span> (t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">checkbox</span><span style="color: rgba(128, 0, 0, 1)">'</span> || t == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">radio</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1247</span>             <span style="color: rgba(0, 0, 255, 1)">this</span>.<span style="color: rgba(0, 0, 255, 1)">checked</span> = <span style="color: rgba(0, 0, 255, 1)">select</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1248</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1249</span>         <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">this</span>.tagName.toLowerCase() == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">option</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1250</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> $sel = $(<span style="color: rgba(0, 0, 255, 1)">this</span>).parent(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">select</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">1251</span>             <span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">select</span> &amp;&amp; $sel[<span style="color: rgba(128, 0, 128, 1)">0</span>] &amp;&amp; $sel[<span style="color: rgba(128, 0, 128, 1)">0</span>].type == <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">select-one</span><span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(0, 0, 0, 1)">) {
</span><span style="color: rgba(0, 128, 128, 1)">1252</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> deselect all other options</span>
<span style="color: rgba(0, 128, 128, 1)">1253</span>                 $sel.find(<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">option</span><span style="color: rgba(128, 0, 0, 1)">'</span>).selected(<span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">1254</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">1255</span>             <span style="color: rgba(0, 0, 255, 1)">this</span>.selected = <span style="color: rgba(0, 0, 255, 1)">select</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1256</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">1257</span> <span style="color: rgba(0, 0, 0, 1)">    });
</span><span style="color: rgba(0, 128, 128, 1)">1258</span> <span style="color: rgba(0, 0, 0, 1)">};
</span><span style="color: rgba(0, 128, 128, 1)">1259</span> 
<span style="color: rgba(0, 128, 128, 1)">1260</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> expose debug var</span>
<span style="color: rgba(0, 128, 128, 1)">1261</span> $.fn.ajaxSubmit.debug = <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1262</span> 
<span style="color: rgba(0, 128, 128, 1)">1263</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> helper fn for console logging</span>
<span style="color: rgba(0, 128, 128, 1)">1264</span> <span style="color: rgba(0, 0, 0, 1)">function log() {
</span><span style="color: rgba(0, 128, 128, 1)">1265</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (!<span style="color: rgba(0, 0, 0, 1)">$.fn.ajaxSubmit.debug) {
</span><span style="color: rgba(0, 128, 128, 1)">1266</span>         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">1267</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1268</span>     <span style="color: rgba(0, 0, 255, 1)">var</span> msg = <span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">[jquery.form] </span><span style="color: rgba(128, 0, 0, 1)">'</span> + Array.prototype.join.call(arguments,<span style="color: rgba(128, 0, 0, 1)">''</span><span style="color: rgba(0, 0, 0, 1)">);
</span><span style="color: rgba(0, 128, 128, 1)">1269</span>     <span style="color: rgba(0, 0, 255, 1)">if</span> (window.console &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> window.console.log) {
</span><span style="color: rgba(0, 128, 128, 1)">1270</span> <span style="color: rgba(0, 0, 0, 1)">        window.console.log(msg);
</span><span style="color: rgba(0, 128, 128, 1)">1271</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1272</span>     <span style="color: rgba(0, 0, 255, 1)">else</span> <span style="color: rgba(0, 0, 255, 1)">if</span> (window.opera &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> window.opera.postError) {
</span><span style="color: rgba(0, 128, 128, 1)">1273</span> <span style="color: rgba(0, 0, 0, 1)">        window.opera.postError(msg);
</span><span style="color: rgba(0, 128, 128, 1)">1274</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">1275</span> <span style="color: rgba(0, 0, 0, 1)">}
</span><span style="color: rgba(0, 128, 128, 1)">1276</span> 
<span style="color: rgba(0, 128, 128, 1)">1277</span> }));</pre>
