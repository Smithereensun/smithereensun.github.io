---
title: "SpringBoot 整合Mybatis Plus 封装分页工具"
date: 2021-06-24
description: "自定义注解 import java.lang.annotation.*; /** * @Author：chenyanbin */ @Documented @Retention(RetentionPolicy.RUNTIME) @Target(ElementType.FIELD) public @in"
tags:
  - "Spring Boot"
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14926900.html"
---

<h1>自定义注解</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">import</span> java.lang.annotation.*<span style="color: rgba(0, 0, 0, 1)">;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @Author：chenyanbin
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
</span><span style="color: rgba(0, 0, 255, 1)">public</span> @<span style="color: rgba(0, 0, 255, 1)">interface</span><span style="color: rgba(0, 0, 0, 1)"> MybatisPlusPageAnnotation {
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 对应数据库字段名称
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    String value() </span><span style="color: rgba(0, 0, 255, 1)">default</span> ""<span style="color: rgba(0, 0, 0, 1)">;

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 对应数据库字段描述
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    String description() </span><span style="color: rgba(0, 0, 255, 1)">default</span> ""<span style="color: rgba(0, 0, 0, 1)">;

    </span><span style="color: rgba(0, 0, 255, 1)">enum</span><span style="color: rgba(0, 0, 0, 1)"> CompareRule {
        eq, </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">等于 =</span>
        like, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">LIKE '%值%'</span>
        likeLeft, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">LIKE '%值'</span>
        likeRight, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">LIKE '值%'</span>
        gt, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">大于</span>
        lt, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">小于</span>
        ge, <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">大于等于</span>
        le <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">小于等于</span>
<span style="color: rgba(0, 0, 0, 1)">    }

    </span><span style="color: rgba(0, 0, 255, 1)">enum</span><span style="color: rgba(0, 0, 0, 1)"> IfRule {
        isNotBlank,
        isBlank,
        isEmpty
    }

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 比较规则
     * &lt;pre&gt;
     *     LIKE '%值%'
     * &lt;/pre&gt;
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    CompareRule compareRule() </span><span style="color: rgba(0, 0, 255, 1)">default</span><span style="color: rgba(0, 0, 0, 1)"> CompareRule.eq;

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 判断规则
     * &lt;pre&gt;
     *     if (StringUtils.isNotBlank(policyNo)) {
     *
     *         }
     * &lt;/pre&gt;
     * &lt;pre&gt;
     * StringUtils.isNotBlank(null)      = false
     * StringUtils.isNotBlank("")        = false
     * StringUtils.isNotBlank(" ")       = false
     * StringUtils.isNotBlank("bob")     = true
     * StringUtils.isNotBlank("  bob  ") = true
     * &lt;/pre&gt;
     * &lt;pre&gt;
     * StringUtils.isBlank(null)      = true
     * StringUtils.isBlank("")        = true
     * StringUtils.isBlank(" ")       = true
     * StringUtils.isBlank("bob")     = false
     * StringUtils.isBlank("  bob  ") = false
     * &lt;/pre&gt;
     * &lt;pre&gt;
     * StringUtils.isEmpty(null)      = true
     * StringUtils.isEmpty("")        = true
     * StringUtils.isEmpty(" ")       = false
     * StringUtils.isEmpty("bob")     = false
     * StringUtils.isEmpty("  bob  ") = false
     * &lt;/pre&gt;
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    IfRule ifRule() </span><span style="color: rgba(0, 0, 255, 1)">default</span><span style="color: rgba(0, 0, 0, 1)"> IfRule.isNotBlank;
}</span></pre>
