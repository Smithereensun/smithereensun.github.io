---
title: "mybatis 逆行工程 附源码"
date: 2023-05-31
description: "导读 逆向工程说白了，就可以简化开发工作量，自动生成一些死板的东西，比如POJO、映射文件等等，然后在将代码拷贝至实际工程，直接拿来用！ 项目结构 GeneratorSqlMap.java import java.io.File; import java.util.ArrayList; import"
tags:
  - "MyBatis"
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12923277.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　逆向工程说白了，就可以简化开发工作量，自动生成一些死板的东西，比如POJO、映射文件等等，然后在将代码拷贝至实际工程，直接拿来用！</p>
<h2>项目结构</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200520135532474-342252726.png" alt="" /></p>
<p>&nbsp;</p>
<h3>GeneratorSqlMap.java</h3>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.File;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.ArrayList;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.List;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.mybatis.generator.api.MyBatisGenerator;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.mybatis.generator.config.Configuration;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.mybatis.generator.config.xml.ConfigurationParser;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.mybatis.generator.internal.DefaultShellCallback;

</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> GeneratorSqlmap {

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> generator() <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception{

        List</span>&lt;String&gt; warnings = <span style="color: rgba(0, 0, 255, 1)">new</span> ArrayList&lt;String&gt;<span style="color: rgba(0, 0, 0, 1)">();
        </span><span style="color: rgba(0, 0, 255, 1)">boolean</span> overwrite = <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">指定 逆向工程配置文件</span>
        File configFile = <span style="color: rgba(0, 0, 255, 1)">new</span> File("generatorConfig.xml"<span style="color: rgba(0, 0, 0, 1)">); 
        ConfigurationParser cp </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> ConfigurationParser(warnings);
        Configuration config </span>=<span style="color: rgba(0, 0, 0, 1)"> cp.parseConfiguration(configFile);
        DefaultShellCallback callback </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> DefaultShellCallback(overwrite);
        MyBatisGenerator myBatisGenerator </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> MyBatisGenerator(config,
                callback, warnings);
        myBatisGenerator.generate(</span><span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">);

    } 
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span> main(String[] args) <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {
        </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
            GeneratorSqlmap generatorSqlmap </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> GeneratorSqlmap();
            generatorSqlmap.generator();
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception e) {
            e.printStackTrace();
        }
    }
}</span></pre>
