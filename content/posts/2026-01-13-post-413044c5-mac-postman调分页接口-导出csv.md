---
title: "Mac postman调分页接口，导出csv"
date: 2026-01-13
description: "准备后端接口 package com.ybchen.controller; import com.ybchen.utils.JsonData; import lombok.Data; import org.springframework.web.bind.annotation.GetMapping;"
tags:
  - "Spring Boot"
  - "Mac系统"
  - "postman"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/postman.html"
---

<h1 style="text-align: center">准备后端接口</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> com.ybchen.controller;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.ybchen.utils.JsonData;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> lombok.Data;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.GetMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RequestMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RequestParam;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RestController;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.ArrayList;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.Date;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.List;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @description: csv导出后端接口测试
 * </span><span style="color: rgba(128, 128, 128, 1)">@author</span><span style="color: rgba(0, 128, 0, 1)">: Alex
 * @create: 2023-11-16 22:41
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
@RestController
@RequestMapping(</span>"/api/v1/csv"<span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> CavController {
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 分页接口
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> page 页数
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> size 一页多少条
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    @GetMapping(</span>"list"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> JsonData&lt;List&lt;UserInfo&gt;&gt;<span style="color: rgba(0, 0, 0, 1)"> list(
            @RequestParam(value </span>= "page", defaultValue = "1") <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> page,
            @RequestParam(value </span>= "size", defaultValue = "10") <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> size
    ) {
        List</span>&lt;UserInfo&gt; resultList = <span style="color: rgba(0, 0, 255, 1)">new</span> ArrayList&lt;&gt;<span style="color: rgba(0, 0, 0, 1)">(size);
        </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = 0; i &lt; size; i++<span style="color: rgba(0, 0, 0, 1)">) {
            resultList.add(</span><span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> UserInfo(
                    i,
                    </span>"陈彦斌___"+page+"_"+<span style="color: rgba(0, 0, 0, 1)">i,
                    page</span>+size+"@qq.com"<span style="color: rgba(0, 0, 0, 1)">,
                    </span><span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> Date()
            ));
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> JsonData.buildSuccess(resultList);
    }

    @Data
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> UserInfo {
        </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
         * 主键id
         </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> id;

        </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
         * 用户名
         </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String userName;

        </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
         * 邮箱
         </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> String email;

        </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
         * 创建时间
         </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
        <span style="color: rgba(0, 0, 255, 1)">private</span><span style="color: rgba(0, 0, 0, 1)"> Date createTime;

        </span><span style="color: rgba(0, 0, 255, 1)">public</span> UserInfo(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> id, String userName, String email, Date createTime) {
            </span><span style="color: rgba(0, 0, 255, 1)">this</span>.id =<span style="color: rgba(0, 0, 0, 1)"> id;
            </span><span style="color: rgba(0, 0, 255, 1)">this</span>.userName =<span style="color: rgba(0, 0, 0, 1)"> userName;
            </span><span style="color: rgba(0, 0, 255, 1)">this</span>.email =<span style="color: rgba(0, 0, 0, 1)"> email;
            </span><span style="color: rgba(0, 0, 255, 1)">this</span>.createTime =<span style="color: rgba(0, 0, 0, 1)"> createTime;
        }

    }
}</span></pre>
