---
title: "SpringBoot通过 JsonSerializer实现自定义序列化"
date: 2024-11-04
description: "介绍 JsonSerializer 是 Jackson 库中的一个类，用于自定义 Java 对象到 JSON 字符串的序列化过程。在使用 Jackson 进行对象序列化时，有时候需要对某些特定类型的字段进行定制化的序列化处理，这时就可以使用 JsonSerializer 来实现自定义的序列化逻辑。"
tags:
  - "JAVA"
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/18173927"
---

<h1 style="text-align: center">介绍</h1>
<p><code>　　JsonSerializer</code> 是 Jackson 库中的一个类，用于自定义 Java 对象到 JSON 字符串的序列化过程。在使用 Jackson 进行对象序列化时，有时候需要对某些特定类型的字段进行定制化的序列化处理，这时就可以使用 <code>JsonSerializer</code> 来实现自定义的序列化逻辑。</p>
<h1 style="text-align: center">使用</h1>
<p>继承JsonSerializer&lt;T&gt;</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.ybchen.seria;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.fasterxml.jackson.core.JsonGenerator;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.fasterxml.jackson.databind.JsonSerializer;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.fasterxml.jackson.databind.SerializerProvider;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.apache.commons.lang3.StringUtils;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.IOException;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @description: 图片序列化
 * </span><span style="color: rgba(128, 128, 128, 1)">@author</span><span style="color: rgba(0, 128, 0, 1)">: alex
 * @create: 2024-05-05 21:10
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
<span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> PictureJsonSerializer <span style="color: rgba(0, 0, 255, 1)">extends</span> JsonSerializer&lt;String&gt;<span style="color: rgba(0, 0, 0, 1)"> {
    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> serialize(String str, JsonGenerator gen, SerializerProvider serializerProvider) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> IOException {
        </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (StringUtils.isNotEmpty(str)){
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">转换图片加签</span>
            gen.writeString(str+"xxx.jpg"<span style="color: rgba(0, 0, 0, 1)">);
        }
    }
}</span></pre>
