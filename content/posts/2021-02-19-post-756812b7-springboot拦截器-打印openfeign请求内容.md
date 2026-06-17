---
title: "SpringBoot拦截器 打印OpenFeign请求内容"
date: 2021-02-19
description: "import com.alibaba.nacos.common.utils.HttpMethod; import feign.RequestInterceptor; import feign.RequestTemplate; import lombok.extern.slf4j.Slf4j; imp"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14416754.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.alibaba.nacos.common.utils.HttpMethod;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> feign.RequestInterceptor;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> feign.RequestTemplate;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> lombok.extern.slf4j.Slf4j;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.stereotype.Component;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.context.request.RequestContextHolder;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.context.request.ServletRequestAttributes;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletRequest;

@Slf4j
@Component
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span> CustomerFeignRequestInterceptor <span style="color: rgba(0, 0, 255, 1)">implements</span><span style="color: rgba(0, 0, 0, 1)"> RequestInterceptor {

    @Override
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> apply(RequestTemplate template) {
        ServletRequestAttributes attributes </span>=<span style="color: rgba(0, 0, 0, 1)"> (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();

        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (attributes != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
            HttpServletRequest request </span>=<span style="color: rgba(0, 0, 0, 1)"> attributes.getRequest();
            template.header(</span>"sessionId", request.getHeader("sessionId"<span style="color: rgba(0, 0, 0, 1)">));
        }
        </span><span style="color: rgba(0, 0, 255, 1)">switch</span><span style="color: rgba(0, 0, 0, 1)"> (template.method()) {
            </span><span style="color: rgba(0, 0, 255, 1)">case</span><span style="color: rgba(0, 0, 0, 1)"> HttpMethod.GET:
                log.info(</span>"{}OpenFeign GET请求，请求路径：【{}"<span style="color: rgba(0, 0, 0, 1)">, System.lineSeparator(), template.url());
                </span><span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
            </span><span style="color: rgba(0, 0, 255, 1)">case</span><span style="color: rgba(0, 0, 0, 1)"> HttpMethod.POST:
                log.info(</span>"{}OpenFeign POST请求，请求路径：【{}】，请求参数：【{}】"<span style="color: rgba(0, 0, 0, 1)">,
                        System.lineSeparator(),
                        template.url(),
                        </span><span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> String(template.requestBody().asBytes(), template.requestCharset()));
                </span><span style="color: rgba(0, 0, 255, 1)">break</span><span style="color: rgba(0, 0, 0, 1)">;
            </span><span style="color: rgba(0, 0, 255, 1)">default</span><span style="color: rgba(0, 0, 0, 1)">:
        }
    }
}</span></pre>
