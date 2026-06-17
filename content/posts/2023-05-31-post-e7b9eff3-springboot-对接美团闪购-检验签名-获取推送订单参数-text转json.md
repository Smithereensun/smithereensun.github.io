---
title: "SpringBoot 对接美团闪购，检验签名，获取推送订单参数，text转json"
date: 2023-05-31
description: "接口文档地址 订单推送(已确定订单)：https://open-shangou.meituan.com/home/docDetail/177 签名算法：https://opendj.meituan.com/home/questionDetail/5730 测试订单：https://opendj.me"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15657414.html"
---

<h1 style="text-align: center">接口文档地址</h1>
<p>订单推送(已确定订单)：<a href="https://open-shangou.meituan.com/home/docDetail/177" target="_blank" rel="noopener nofollow">https://open-shangou.meituan.com/home/docDetail/177</a></p>
<p>签名算法：<a href="https://opendj.meituan.com/home/questionDetail/5730" target="_blank" rel="noopener nofollow">https://opendj.meituan.com/home/questionDetail/5730</a></p>
<p>测试订单：<a href="https://opendj.meituan.com/platform/guide/market/10657" target="_blank" rel="noopener nofollow">https://opendj.meituan.com/platform/guide/market/10657</a></p>
<h1 style="text-align: center">控制器</h1>
<div class="cnblogs_code">
<pre>    @RequestMapping("confirm_order"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> confirmOrder(HttpServletRequest request) {
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">验证美团闪购签名</span>
        Boolean flag = CommonUtil.checkMeiTuanShanGouSign(request, "6bdfc78d4a64e82bc59e2a67d746a06e"<span style="color: rgba(0, 0, 0, 1)">);
        </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (flag) {
            SortedMap</span>&lt;String, String&gt; requestParam =<span style="color: rgba(0, 0, 0, 1)"> CommonUtil.getMeiTuanShanGouRequestParam(request);
            String json </span>=<span style="color: rgba(0, 0, 0, 1)"> JSON.toJSONString(requestParam);
            System.err.println(json);
            MeiTuanShanGouConfirmOrderVo vo </span>= JSON.parseObject(json, MeiTuanShanGouConfirmOrderVo.<span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)">);
            System.out.println(</span>"====================================="<span style="color: rgba(0, 0, 0, 1)">);
            System.err.println(vo);
        }
    }</span></pre>
