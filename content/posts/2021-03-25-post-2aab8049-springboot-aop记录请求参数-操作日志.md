---
title: "SpringBoot AOP记录请求参数，操作日志"
date: 2021-03-25
description: "ControllerLogAspect.java import com.alibaba.fastjson.JSON; import org.aspectj.lang.JoinPoint; import org.aspectj.lang.annotation.AfterReturning; impor"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14559780.html"
---

<h1 style="text-align: center">ControllerLogAspect.java</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> com.alibaba.fastjson.JSON;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.JoinPoint;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.annotation.AfterReturning;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.annotation.Aspect;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.annotation.Before;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.aspectj.lang.annotation.Pointcut;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.beans.factory.annotation.Autowired;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.core.annotation.Order;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.stereotype.Component;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.context.request.RequestContextHolder;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.context.request.ServletRequestAttributes;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletRequest;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.BufferedReader;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.Map;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @Description：AOP切入点记录操作日志
 * @Author：chenyanbin
 * @Date：2021/3/19 下午11:30
 * @Versiion：1.0
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
@Aspect
@Order(</span>5<span style="color: rgba(0, 0, 0, 1)">)
@Component
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> ControllerLogAspect {
    @Autowired
    LogTask logTask;

    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">切入点表达式</span>
    @Pointcut("execution(public * com.ybchen.service.trace.controller..*.*(..))"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> controllerLog() {
    }

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 进入controller之前，拿请求参数
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> joinPoint
     * </span><span style="color: rgba(128, 128, 128, 1)">@throws</span><span style="color: rgba(0, 128, 0, 1)"> Throwable
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    @Before(</span>"controllerLog()"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> doBefore(JoinPoint joinPoint) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Throwable {

        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 接收到请求，记录请求内容</span>
        ServletRequestAttributes attributes =<span style="color: rgba(0, 0, 0, 1)"> (ServletRequestAttributes) RequestContextHolder.getRequestAttributes();
        HttpServletRequest request </span>=<span style="color: rgba(0, 0, 0, 1)"> attributes.getRequest();
        String params </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
        String ip </span>=<span style="color: rgba(0, 0, 0, 1)"> request.getRemoteAddr();
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 只记录post方法</span>
        <span style="color: rgba(0, 0, 255, 1)">if</span> ("POST"<span style="color: rgba(0, 0, 0, 1)">.equals(request.getMethod())) {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 记录下请求内容</span>
            System.out.println("请求URL : " +<span style="color: rgba(0, 0, 0, 1)"> request.getRequestURL());
            System.out.println(</span>"请求IP : " +<span style="color: rgba(0, 0, 0, 1)"> request.getRemoteAddr());
            System.out.println(</span>"请求方法 : " + joinPoint.getSignature().getDeclaringTypeName() + "." +<span style="color: rgba(0, 0, 0, 1)"> joinPoint.getSignature().getName());

            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 获取参数, 只取自定义的参数, 自带的HttpServletRequest, HttpServletResponse不管</span>
            BufferedReader br =<span style="color: rgba(0, 0, 0, 1)"> request.getReader();
            String str, wholeStr </span>= ""<span style="color: rgba(0, 0, 0, 1)">;
            </span><span style="color: rgba(0, 0, 255, 1)">while</span> ((str = br.readLine()) != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
                wholeStr </span>+=<span style="color: rgba(0, 0, 0, 1)"> str;
            }
            StringBuilder stringBuilder </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> StringBuilder();
            </span><span style="color: rgba(0, 0, 255, 1)">if</span> (""<span style="color: rgba(0, 0, 0, 1)">.equals(wholeStr)) {
                System.out.println(</span>"不是json提交，重新获取post请求参数"<span style="color: rgba(0, 0, 0, 1)">);
                Map</span>&lt;String, String[]&gt; parameterMap =<span style="color: rgba(0, 0, 0, 1)"> request.getParameterMap();
                parameterMap.forEach((k, v) </span>-&gt;<span style="color: rgba(0, 0, 0, 1)"> {
                    </span><span style="color: rgba(0, 0, 255, 1)">if</span> (v != <span style="color: rgba(0, 0, 255, 1)">null</span> &amp;&amp; v.length &gt; 0<span style="color: rgba(0, 0, 0, 1)">) {
                        </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">int</span> i = 0; i &lt; v.length; i++<span style="color: rgba(0, 0, 0, 1)">) {
                            stringBuilder.append(v[i]);
                        }
                    }
                    System.out.println(</span>"post请求，key= " + k + " ,value= " +<span style="color: rgba(0, 0, 0, 1)"> stringBuilder.toString());
                });
            } </span><span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
                System.out.println(</span>"post请求参数:" +<span style="color: rgba(0, 0, 0, 1)"> wholeStr);
                params </span>=<span style="color: rgba(0, 0, 0, 1)"> wholeStr;
            }
            params </span>=<span style="color: rgba(0, 0, 0, 1)"> stringBuilder.toString();
        }
        </span><span style="color: rgba(0, 0, 255, 1)">if</span> ("GET"<span style="color: rgba(0, 0, 0, 1)">.equals(request.getMethod())) {
            System.out.println(</span>"请求URL : " +<span style="color: rgba(0, 0, 0, 1)"> request.getRequestURL());
            System.out.println(</span>"请求IP : " +<span style="color: rgba(0, 0, 0, 1)"> request.getRemoteAddr());
            System.out.println(</span>"请求参数：" +<span style="color: rgba(0, 0, 0, 1)"> request.getQueryString());
            params </span>=<span style="color: rgba(0, 0, 0, 1)"> request.getQueryString();
        }
        logTask.addLog(ip, params);
    }

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 接口执行之后，获取响应结果
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> ret
     * </span><span style="color: rgba(128, 128, 128, 1)">@throws</span><span style="color: rgba(0, 128, 0, 1)"> Throwable
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    @AfterReturning(returning </span>= "ret", pointcut = "controllerLog()"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> doAfterReturning(Object ret) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Throwable {
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 处理完请求，返回内容</span>
        System.out.println("返回 : " +<span style="color: rgba(0, 0, 0, 1)"> JSON.toJSONString(ret));
    }
}</span></pre>
