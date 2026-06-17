---
title: "Java 集合元素排序接口Comparable"
date: 2023-05-31
description: "什么是Comparable public interface Comparable&lt;T&gt; { /** * Compares this object with the specified object for order. Returns a * negative integer, zer"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13406976.html"
---

<h1 style="text-align: center">什么是Comparable</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">interface</span> Comparable&lt;T&gt;<span style="color: rgba(0, 0, 0, 1)"> {
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * Compares this object with the specified object for order.  Returns a
     * negative integer, zero, or a positive integer as this object is less
     * than, equal to, or greater than the specified object.
     *
     * &lt;p&gt;The implementor must ensure &lt;tt&gt;sgn(x.compareTo(y)) ==
     * -sgn(y.compareTo(x))&lt;/tt&gt; for all &lt;tt&gt;x&lt;/tt&gt; and &lt;tt&gt;y&lt;/tt&gt;.  (This
     * implies that &lt;tt&gt;x.compareTo(y)&lt;/tt&gt; must throw an exception iff
     * &lt;tt&gt;y.compareTo(x)&lt;/tt&gt; throws an exception.)
     *
     * &lt;p&gt;The implementor must also ensure that the relation is transitive:
     * &lt;tt&gt;(x.compareTo(y)&amp;gt;0 &amp;amp;&amp;amp; y.compareTo(z)&amp;gt;0)&lt;/tt&gt; implies
     * &lt;tt&gt;x.compareTo(z)&amp;gt;0&lt;/tt&gt;.
     *
     * &lt;p&gt;Finally, the implementor must ensure that &lt;tt&gt;x.compareTo(y)==0&lt;/tt&gt;
     * implies that &lt;tt&gt;sgn(x.compareTo(z)) == sgn(y.compareTo(z))&lt;/tt&gt;, for
     * all &lt;tt&gt;z&lt;/tt&gt;.
     *
     * &lt;p&gt;It is strongly recommended, but &lt;i&gt;not&lt;/i&gt; strictly required that
     * &lt;tt&gt;(x.compareTo(y)==0) == (x.equals(y))&lt;/tt&gt;.  Generally speaking, any
     * class that implements the &lt;tt&gt;Comparable&lt;/tt&gt; interface and violates
     * this condition should clearly indicate this fact.  The recommended
     * language is "Note: this class has a natural ordering that is
     * inconsistent with equals."
     *
     * &lt;p&gt;In the foregoing description, the notation
     * &lt;tt&gt;sgn(&lt;/tt&gt;&lt;i&gt;expression&lt;/i&gt;&lt;tt&gt;)&lt;/tt&gt; designates the mathematical
     * &lt;i&gt;signum&lt;/i&gt; function, which is defined to return one of &lt;tt&gt;-1&lt;/tt&gt;,
     * &lt;tt&gt;0&lt;/tt&gt;, or &lt;tt&gt;1&lt;/tt&gt; according to whether the value of
     * &lt;i&gt;expression&lt;/i&gt; is negative, zero or positive.
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)">   o the object to be compared.
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span><span style="color: rgba(0, 128, 0, 1)">  a negative integer, zero, or a positive integer as this object
     *          is less than, equal to, or greater than the specified object.
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@throws</span><span style="color: rgba(0, 128, 0, 1)"> NullPointerException if the specified object is null
     * </span><span style="color: rgba(128, 128, 128, 1)">@throws</span><span style="color: rgba(0, 128, 0, 1)"> ClassCastException if the specified object's type prevents it
     *         from being compared to this object.
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> compareTo(T o);
}</span></pre>
