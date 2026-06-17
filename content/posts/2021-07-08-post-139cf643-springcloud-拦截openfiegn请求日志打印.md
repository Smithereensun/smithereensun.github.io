---
title: "springcloud 拦截OpenFiegn请求日志打印"
date: 2021-07-08
description: "import feign.RequestInterceptor; import feign.RequestTemplate; import feign.Target; import feign.Target.HardCodedTarget; import lombok.extern.slf4j.Sl"
tags:
  - "Spring Cloud"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14985872.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> feign.RequestInterceptor;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> feign.RequestTemplate;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> feign.Target;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> feign.Target.HardCodedTarget;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> lombok.extern.slf4j.Slf4j;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.nio.charset.Charset;

@Slf4j
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> CustomerFeignRequestInterceptor <span style="color: rgba(0, 0, 255, 1)">implements</span><span style="color: rgba(0, 0, 0, 1)"> RequestInterceptor {

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> apply(RequestTemplate template) {
        String url </span>=<span style="color: rgba(0, 0, 0, 1)"> template.url();
        Target</span>&lt;?&gt; target =<span style="color: rgba(0, 0, 0, 1)"> template.feignTarget();
        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (target <span style="color: rgba(0, 0, 255, 1)">instanceof</span><span style="color: rgba(0, 0, 0, 1)"> HardCodedTarget) {
            HardCodedTarget hardCodedTarget </span>=<span style="color: rgba(0, 0, 0, 1)"> (HardCodedTarget) target;
            url </span>= hardCodedTarget.url() +<span style="color: rgba(0, 0, 0, 1)"> url;
        }
        String method </span>=<span style="color: rgba(0, 0, 0, 1)"> template.method();
        Charset charset </span>=<span style="color: rgba(0, 0, 0, 1)"> template.requestCharset();
        </span><span style="color: rgba(0, 0, 255, 1)">byte</span>[] body =<span style="color: rgba(0, 0, 0, 1)"> template.body();
        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (body == <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
            body </span>= "null"<span style="color: rgba(0, 0, 0, 1)">.getBytes(charset);
        }
        log.info(</span>"\r\n{} {}\r\n{}", method, url, <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> String(body, charset));
    }
}</span></pre>
