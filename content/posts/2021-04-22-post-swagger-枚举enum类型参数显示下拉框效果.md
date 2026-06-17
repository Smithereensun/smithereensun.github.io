---
title: "Swagger 枚举enum类型参数显示下拉框效果"
date: 2021-04-22
description: "枚举值 public enum ProductEnum { BOOK(&quot;书籍&quot;), FOOD(&quot;食物&quot;), OTHER(&quot;其他&quot;); private String type; ProductEnum(String type) { this."
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14689271.html"
---

<p>&nbsp;</p>
<h1 style="text-align: center">枚举值</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">enum</span><span style="color: rgba(0, 0, 0, 1)"> ProductEnum {
    BOOK(</span>"书籍"<span style="color: rgba(0, 0, 0, 1)">),
    FOOD(</span>"食物"<span style="color: rgba(0, 0, 0, 1)">),
    OTHER(</span>"其他"<span style="color: rgba(0, 0, 0, 1)">);

    </span><span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String type;

    ProductEnum(String type) {
        </span><span style="color: rgba(0, 0, 255, 1)">this</span>.type =<span style="color: rgba(0, 0, 0, 1)"> type;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String getType(){
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> type;
    }

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span><span style="color: rgba(0, 0, 0, 1)"> ProductEnum fromType(String type){
        </span><span style="color: rgba(0, 0, 255, 1)">for</span><span style="color: rgba(0, 0, 0, 1)">(ProductEnum typeEnum: values()){
            </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)">(typeEnum.type.equals(type)){
                </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> typeEnum;
            }
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
    }
}</span></pre>
