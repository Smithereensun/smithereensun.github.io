---
title: "JavaSe 统计字符串中字符出现的次数"
date: 2023-05-31
description: "public static void main(String[] args) { // 1、字符串 String str = &quot;*Constructs a new &lt;tt&gt;HashMap&lt;/tt&gt; with the same mappings as the * sp"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13412631.html"
---

<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> main(String[] args) {
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 1、字符串</span>
        String str = "*Constructs a new &lt;tt&gt;HashMap&lt;/tt&gt; with the same mappings as the *  specified &lt;tt&gt;Map&lt;/tt&gt;. The&lt;tt&gt;HashMap&lt;/tt&gt; is created with default load factor (0.75) and aninitial capacity sufficient to*hold the mappings in the specified&lt;tt&gt;Map&lt;/tt&gt;."<span style="color: rgba(0, 0, 0, 1)">;
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 2.把字符串转换为数组</span>
        <span style="color: rgba(0, 0, 255, 1)">char</span>[] charArr =<span style="color: rgba(0, 0, 0, 1)"> str.toCharArray();
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 3.创建一个Map</span>
        Map&lt;Character, Integer&gt; counterMap = <span style="color: rgba(0, 0, 255, 1)">new</span> HashMap&lt;Character, Integer&gt;<span style="color: rgba(0, 0, 0, 1)">();
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 4.遍历一个Map</span>
        <span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = 0; i &lt; charArr.length; i++<span style="color: rgba(0, 0, 0, 1)">) {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 5.拿到的字符作为键到集合中去找值</span>
            Integer value =<span style="color: rgba(0, 0, 0, 1)"> counterMap.get(charArr[i]);
            </span><span style="color: rgba(0, 0, 255, 1)">if</span> (value == <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 把字符作为键，1为值存入集合</span>
                counterMap.put(charArr[i], 1<span style="color: rgba(0, 0, 0, 1)">);
            } </span><span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 把值加1重新写入集合</span>
                value += 1<span style="color: rgba(0, 0, 0, 1)">;
                counterMap.put(charArr[i], value);
            }
        }
        Set</span>&lt;Map.Entry&lt;Character, Integer&gt;&gt; entrySet =<span style="color: rgba(0, 0, 0, 1)"> counterMap.entrySet();
        </span><span style="color: rgba(0, 0, 255, 1)">for</span> (Map.Entry&lt;Character, Integer&gt;<span style="color: rgba(0, 0, 0, 1)"> entry : entrySet) {
            System.out.println(entry.getKey() </span>+ " 字符出现次数=" +<span style="color: rgba(0, 0, 0, 1)"> entry.getValue());
        }
    }</span></pre>
