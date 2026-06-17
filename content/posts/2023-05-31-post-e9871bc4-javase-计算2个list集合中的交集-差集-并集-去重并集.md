---
title: "JavaSE 计算2个List集合中的交集、差集、并集、去重并集"
date: 2023-05-31
description: "VideoOrder.java 重写里面的equals和hashCode方法 class VideoOrder { private int price; private String title; public VideoOrder(String title, int price) { this.t"
tags:
  - "JavaSE"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13412669.html"
---

<h1>VideoOrder.java</h1>
<p><span style="color: rgba(255, 0, 0, 1)"><strong>重写里面的equals和hashCode方法</strong></span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> VideoOrder {
    </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> price;
    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String title;

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> VideoOrder(String title, <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> price) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.title =<span style="color: rgba(0, 0, 0, 1)"> title;
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.price =<span style="color: rgba(0, 0, 0, 1)"> price;
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">boolean</span><span style="color: rgba(0, 0, 0, 1)"> equals(Object o) {
        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (<span style="color: rgba(0, 0, 255, 1)">this</span> ==<span style="color: rgba(0, 0, 0, 1)"> o)
            </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (o == <span style="color: rgba(0, 0, 255, 1)">null</span> || getClass() !=<span style="color: rgba(0, 0, 0, 1)"> o.getClass())
            </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
        VideoOrder that </span>=<span style="color: rgba(0, 0, 0, 1)"> (VideoOrder) o;
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> price == that.price &amp;&amp;<span style="color: rgba(0, 0, 0, 1)"> Objects.equals(title, that.title);
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> hashCode() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> Objects.hash(price, title);
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> getPrice() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> price;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> setPrice(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> price) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.price =<span style="color: rgba(0, 0, 0, 1)"> price;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getTitle() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> title;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> setTitle(String title) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.title =<span style="color: rgba(0, 0, 0, 1)"> title;
    }

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String toString() {
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> "VideoOrder{" + "price=" + price + ", title='" + title + '\'' + '}'<span style="color: rgba(0, 0, 0, 1)">;
    }
}</span></pre>
