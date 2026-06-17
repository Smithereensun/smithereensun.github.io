---
title: "java 任务id每天重置并自增"
date: 2021-09-24
description: "生成规则 当前年份（省略年份前三位数）+月份+日期+三位顺序码，比如2021年7月15日第3笔。 此编号对应为：10715003 实现思路 1、使用redis原子自增特性 2、先判断key，是否存在 2.1、存在：顺序码自增 2.2、不存子：重新生成顺序码 代码实现 控制器 import io.sw"
tags:
  - "JAVA"
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/15331479.html"
---

<h1 style="text-align: center">生成规则</h1>
<p>当前年份（省略年份前三位数）+月份+日期+三位顺序码，比如2021年7月15日第3笔。 此编号对应为：10715003</p>
<h1 style="text-align: center">实现思路</h1>
<p>　　1、使用redis原子自增特性</p>
<p>　　2、先判断key，是否存在</p>
<p>　　　　2.1、存在：顺序码自增</p>
<p>　　　　2.2、不存子：重新生成顺序码</p>
<h1 style="text-align: center">代码实现</h1>
<h2>控制器</h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> io.swagger.annotations.Api;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> io.swagger.annotations.ApiOperation;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.beans.factory.annotation.Autowired;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.GetMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RequestMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RestController;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.time.LocalDateTime;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.time.format.DateTimeFormatter;

</span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
 * @Author：chenyanbin
 </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
@RestController
@RequestMapping(</span>"/api/task/v1"<span style="color: rgba(0, 0, 0, 1)">)
@Api(tags </span>= "任务API 测试"<span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> TaskController {
    @Autowired
    RedisService redisService;
    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 自增序号有效期，一天半
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span>
    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">final</span> Long EXPIRE = 60 * 60 * (24 + 12) * 1L<span style="color: rgba(0, 0, 0, 1)">;

    </span><span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 生成任务规则如下
     * 当前年份（省略年份前三位数）+月份+日期+三位顺序码，比如2021年7月15日第3笔。 此编号对应为：10715003
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@return</span>
     <span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    @ApiOperation(</span>"生成任务编号"<span style="color: rgba(0, 0, 0, 1)">)
    @GetMapping(</span>"generator"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> String generateTaskId() {
        LocalDateTime localDateTime </span>=<span style="color: rgba(0, 0, 0, 1)"> LocalDateTime.now();
        DateTimeFormatter dtf </span>= DateTimeFormatter.ofPattern("yMMdd"<span style="color: rgba(0, 0, 0, 1)">);
        String key </span>=<span style="color: rgba(0, 0, 0, 1)"> dtf.format(localDateTime);
        </span><span style="color: rgba(0, 0, 255, 1)">long</span><span style="color: rgba(0, 0, 0, 1)"> incr;
        </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (redisService.exists(key)) {
            incr </span>=<span style="color: rgba(0, 0, 0, 1)"> redisService.incr(key, EXPIRE);
        } </span><span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
            incr </span>=<span style="color: rgba(0, 0, 0, 1)"> redisService.incr(key, EXPIRE);
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span> key.substring(key.length() - 5) + CommonUtil.automaticFilling((<span style="color: rgba(0, 0, 255, 1)">int</span>) incr, 3<span style="color: rgba(0, 0, 0, 1)">);
    }
}</span></pre>
