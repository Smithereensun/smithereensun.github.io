---
title: "SpringBoot获取Resource资源"
date: 2021-05-25
description: "资源文件位置 方式一 使用项目内路径读取，该路径只在开发工具中显示，类似：src/main/resources/2.jpg。只能在开发工具中使用，部署之后无法读取。（不通用） @Test public void testReadFile2() throws IOException { File fi"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14810448.html"
---

<h1 style="text-align: center">资源文件位置</h1>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202105/1504448-20210525203646074-1061322755.png" alt="" loading="lazy" /></p>
<h1 style="text-align: center">方式一</h1>
<p>使用项目内路径读取，该路径只在开发工具中显示，类似：src/main/resources/2.jpg。只能在开发工具中使用，部署之后无法读取。（不通用）</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">@Test
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> testReadFile2() <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> IOException {
        File file </span>= <span style="color: rgba(0, 0, 255, 1)">new</span> File("src/main/resources/2.jpg"<span style="color: rgba(0, 0, 0, 1)">);
        FileInputStream fis </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> FileInputStream(file);
        InputStreamReader isr </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> InputStreamReader(fis);
        BufferedReader br </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> BufferedReader(isr);
        String data </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
        </span><span style="color: rgba(0, 0, 255, 1)">while</span>((data = br.readLine()) != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
            System.out.println(data);
        }
        
        br.close();
        isr.close();
        fis.close();
    }</span></pre>
