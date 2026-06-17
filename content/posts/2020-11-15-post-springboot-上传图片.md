---
title: "SpringBoot 上传图片"
date: 2020-11-15
description: "控制层代码 package net.ybchen.demo.controller; import net.ybchen.demo.utils.JsonData; import org.springframework.web.bind.annotation.PostMapping; import or"
tags:
  - "Spring Boot"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13976426.html"
---

<h1 style="text-align: center">控制层代码</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">package</span><span style="color: rgba(0, 0, 0, 1)"> net.ybchen.demo.controller;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> net.ybchen.demo.utils.JsonData;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.PostMapping;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RequestParam;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.bind.annotation.RestController;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> org.springframework.web.multipart.MultipartFile;

</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> javax.servlet.http.HttpServletRequest;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.File;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.FileNotFoundException;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.io.IOException;
</span><span style="color: rgba(0, 0, 255, 1)">import</span><span style="color: rgba(0, 0, 0, 1)"> java.util.UUID;

@RestController
</span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> UploadController {
    @PostMapping(</span>"/upload"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> JsonData uplaod(HttpServletRequest req, @RequestParam("file"<span style="color: rgba(0, 0, 0, 1)">) MultipartFile file) {
        String fileName</span>=<span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
        </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
            </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (file.isEmpty()) {
                </span><span style="color: rgba(0, 0, 255, 1)">return</span> JsonData.buildError("请选择文件！"<span style="color: rgba(0, 0, 0, 1)">);
            }
            fileName </span>=<span style="color: rgba(0, 0, 0, 1)"> file.getOriginalFilename();
            String suffixName </span>= fileName.substring(fileName.lastIndexOf("."<span style="color: rgba(0, 0, 0, 1)">));
            </span><span style="color: rgba(0, 0, 255, 1)">if</span> (suffixName.toLowerCase().equals(".jpg") || suffixName.toLowerCase().equals(".png"<span style="color: rgba(0, 0, 0, 1)">)) {
                File currentFile </span>= <span style="color: rgba(0, 0, 255, 1)">new</span> File(""<span style="color: rgba(0, 0, 0, 1)">);
                String currentFilePath </span>=<span style="color: rgba(0, 0, 0, 1)"> currentFile.getCanonicalPath();
                System.out.println(currentFilePath);
                fileName</span>=UUID.randomUUID().toString().replaceAll("-","") +<span style="color: rgba(0, 0, 0, 1)"> fileName;
                String destFileName </span>= currentFilePath + File.separator + "uploaded" + File.separator +<span style="color: rgba(0, 0, 0, 1)"> fileName;
                File destFile </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> File(destFileName);
                destFile.getParentFile().mkdirs();
                file.transferTo(destFile);
                System.out.println(destFileName);
            } </span><span style="color: rgba(0, 0, 255, 1)">else</span><span style="color: rgba(0, 0, 0, 1)"> {
                </span><span style="color: rgba(0, 0, 255, 1)">return</span> JsonData.buildError("文件后缀不正确，请上传jpg|png格式！"<span style="color: rgba(0, 0, 0, 1)">);
            }
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (FileNotFoundException e) {
            e.printStackTrace();
            </span><span style="color: rgba(0, 0, 255, 1)">return</span> JsonData.buildError("上传失败," +<span style="color: rgba(0, 0, 0, 1)"> e.getMessage());
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (IOException e) {
            e.printStackTrace();
            </span><span style="color: rgba(0, 0, 255, 1)">return</span> JsonData.buildError("上传失败," +<span style="color: rgba(0, 0, 0, 1)"> e.getMessage());
        }
        </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> JsonData.buildSuccess(fileName);
    }
}</span></pre>
