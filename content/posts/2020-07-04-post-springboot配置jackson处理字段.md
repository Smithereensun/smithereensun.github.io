---
title: "SpringBoot配置Jackson处理字段"
date: 2020-07-04
description: "常用框架 阿里fastjson，谷歌gson等 JavaBean序列化为json 性能：Jackson&gt;FastJson&gt;Gson&gt;lib 同个结构 Jackson、Fastjson、Gson等库各有优缺点，各有自己的专长 空间换时间，时间换空间 Jackson处理相关自动 指定字"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13234669.html"
---

<p>常用框架 阿里fastjson，谷歌gson等</p>
<p>JavaBean序列化为json</p>
<ul>
<li>性能：Jackson&gt;FastJson&gt;Gson&gt;lib 同个结构</li>
<li>Jackson、Fastjson、Gson等库各有优缺点，各有自己的专长</li>
<li>空间换时间，时间换空间</li>
</ul>
<p>Jackson处理相关自动</p>
<ul>
<li>指定字段不返回：@JsonIgnore</li>
<li>指定日期格式：@JsonFormat(pattern="yyyy-MM-dd hh:mm:ss",locale="zh",timezone="GMT+8")</li>
<li>空字段不返回：@JsonInclude(JsonInclude.Include.NON_NULL)</li>
<li>指定别名：@JsonProperty("TITLE")</li>
</ul>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.cyb.demo.domain;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.fasterxml.jackson.annotation.JsonFormat;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.fasterxml.jackson.annotation.JsonIgnore;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.fasterxml.jackson.annotation.JsonInclude;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.fasterxml.jackson.annotation.JsonProperty;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.Serializable;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.Date;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.List;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> Video <span style="color: rgba(0, 0, 255, 1)">implements</span><span style="color: rgba(0, 0, 0, 1)"> Serializable {
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> id;
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">设置别名</span>
    @JsonProperty("TITLE"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String title;
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String summary;
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">指定字段不返回</span>
<span style="color: rgba(0, 0, 0, 1)">    @JsonIgnore
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> pricce;
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">空字段不返回</span>
<span style="color: rgba(0, 0, 0, 1)">    @JsonInclude(JsonInclude.Include.NON_NULL)
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String converImg;
    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">指定日期格式</span>
    @JsonFormat(pattern="yyyy-MM-dd hh:mm:ss",locale="zh",timezone="GMT+8"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> Date createTime;
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> List&lt;Chapter&gt;<span style="color: rgba(0, 0, 0, 1)"> chapterList;

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> List&lt;Chapter&gt;<span style="color: rgba(0, 0, 0, 1)"> getChapterList() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> chapterList;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> setChapterList(List&lt;Chapter&gt;<span style="color: rgba(0, 0, 0, 1)"> chapterList) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.chapterList =<span style="color: rgba(0, 0, 0, 1)"> chapterList;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Video() {
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> Video(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> id, String title) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.id =<span style="color: rgba(0, 0, 0, 1)"> id;
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.title =<span style="color: rgba(0, 0, 0, 1)"> title;
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.createTime = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> Date();
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> getId() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> id;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> setId(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> id) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.id =<span style="color: rgba(0, 0, 0, 1)"> id;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getTitle() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> title;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setTitle(String title) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.title =<span style="color: rgba(0, 0, 0, 1)"> title;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getSummary() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> summary;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setSummary(String summary) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.summary =<span style="color: rgba(0, 0, 0, 1)"> summary;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> getPricce() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> pricce;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> setPricce(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> pricce) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.pricce =<span style="color: rgba(0, 0, 0, 1)"> pricce;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getConverImg() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> converImg;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setConverImg(String converImg) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.converImg =<span style="color: rgba(0, 0, 0, 1)"> converImg;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> Date getCreateTime() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> createTime;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setCreateTime(Date createTime) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.createTime =<span style="color: rgba(0, 0, 0, 1)"> createTime;
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String toString() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> "Video{" +
                "id=" + id +
                ", title='" + title + '\'' +
                ", summary='" + summary + '\'' +
                ", pricce=" + pricce +
                ", converImg='" + converImg + '\'' +
                ", createTime=" + createTime +
                ", chapterList=" + chapterList +
                '}'<span style="color: rgba(0, 0, 0, 1)">;
    }
}</span></pre>
