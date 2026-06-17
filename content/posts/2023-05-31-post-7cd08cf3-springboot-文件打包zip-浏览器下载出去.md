---
title: "SpringBoot 文件打包zip，浏览器下载出去"
date: 2023-05-31
description: "本地文件打包 /** * 下载压缩包 * * @param response */ @ResponseBody @GetMapping(&quot;/downloadZip&quot;) public void downloadZip(HttpServletResponse response, //"
tags:
  - "Spring"
  - "JAVA"
  - "Spring Boot"
  - "Spring Cloud"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/17347823.html"
---

<h1 style="text-align: center">本地文件打包</h1>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 128, 0, 1)">/**</span><span style="color: rgba(0, 128, 0, 1)">
     * 下载压缩包
     *
     * </span><span style="color: rgba(128, 128, 128, 1)">@param</span><span style="color: rgba(0, 128, 0, 1)"> response
     </span><span style="color: rgba(0, 128, 0, 1)">*/</span><span style="color: rgba(0, 0, 0, 1)">
    @ResponseBody
    @GetMapping(</span>"/downloadZip"<span style="color: rgba(0, 0, 0, 1)">)
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> downloadZip(HttpServletResponse response,
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">            @RequestBody AssetInfoDownloadZipParam zipParam,</span>
                            @RequestParam("agreementsIdList") List&lt;Long&gt; agreementsIdList, @RequestParam("attachmentsIdList") List&lt;Long&gt;<span style="color: rgba(0, 0, 0, 1)"> attachmentsIdList) {
        </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
            response.setContentType(</span>"application/octet-stream"<span style="color: rgba(0, 0, 0, 1)">);
            response.setHeader(</span>"Content-Disposition", "attachment;fileName=" + URLEncoder.encode("资产信息.zip", "UTF-8"<span style="color: rgba(0, 0, 0, 1)">));
            ServletOutputStream os </span>=<span style="color: rgba(0, 0, 0, 1)"> response.getOutputStream();
            ZipOutputStream zos </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> ZipOutputStream(os);
            </span><span style="color: rgba(0, 0, 255, 1)">byte</span>[] buf = <span style="color: rgba(0, 0, 255, 1)">new</span> <span style="color: rgba(0, 0, 255, 1)">byte</span>[1024 * 2<span style="color: rgba(0, 0, 0, 1)">];
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">资产附件列表</span>
            List&lt;AssetInfoAgreements&gt; assetInfoAgreementsList =<span style="color: rgba(0, 0, 0, 1)"> assetInfoService.getAgreementsListByIds(agreementsIdList);
            </span><span style="color: rgba(0, 0, 255, 1)">for</span><span style="color: rgba(0, 0, 0, 1)"> (AssetInfoAgreements agreements : assetInfoAgreementsList) {
                </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (StringUtils.isNotBlank(agreements.getFilePath())) {
                    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> Users/chenyanbin/Desktop/2023/05/11/test付款审批表____3LGPAc.pdf</span>
                    String fileName =<span style="color: rgba(0, 0, 0, 1)"> agreements.getFilePath();
                    File file </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> File(fileName);
                    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">判断文件是否存在</span>
                    <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (file.exists()) {
                        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">将文件重命名</span>
                        zos.putNextEntry(<span style="color: rgba(0, 0, 255, 1)">new</span> ZipEntry("资产附件" + File.separator + file.getName().substring(0, file.getName().indexOf("____")) + file.getName().substring(file.getName().indexOf("."<span style="color: rgba(0, 0, 0, 1)">), file.getName().length())));
                        FileInputStream fis </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> FileInputStream(file);
                        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">使用字节缓冲输入流</span>
                        BufferedInputStream bis = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> BufferedInputStream(fis);
                        </span><span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> len;
                        </span><span style="color: rgba(0, 0, 255, 1)">while</span> ((len = bis.read(buf)) != -1<span style="color: rgba(0, 0, 0, 1)">) {
                            zos.write(buf, </span>0<span style="color: rgba(0, 0, 0, 1)">, len);
                        }
                        zos.closeEntry();
                        bis.close();
                    }
                }
            }
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">资产文件列表</span>
            List&lt;AssetInfoAttachments&gt; attachmentsList =<span style="color: rgba(0, 0, 0, 1)"> assetInfoService.getAttachmentsListByIds(attachmentsIdList);
            </span><span style="color: rgba(0, 0, 255, 1)">for</span><span style="color: rgba(0, 0, 0, 1)"> (AssetInfoAttachments attachments : attachmentsList) {
                </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (StringUtils.isNotBlank(attachments.getFilePath())) {
                    String fileName </span>=<span style="color: rgba(0, 0, 0, 1)"> attachments.getFilePath();
                    File file </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> File(fileName);
                    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">判断文件是否存在</span>
                    <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (file.exists()) {
                        zos.putNextEntry(</span><span style="color: rgba(0, 0, 255, 1)">new</span> ZipEntry("资产文件" + File.separator + file.getName().substring(0, file.getName().indexOf("____")) + file.getName().substring(file.getName().indexOf("."<span style="color: rgba(0, 0, 0, 1)">), file.getName().length())));
                        FileInputStream fis </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> FileInputStream(file);
                        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">使用字节缓冲输入流</span>
                        BufferedInputStream bis = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> BufferedInputStream(fis);
                        </span><span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> len;
                        </span><span style="color: rgba(0, 0, 255, 1)">while</span> ((len = bis.read(buf)) != -1<span style="color: rgba(0, 0, 0, 1)">) {
                            zos.write(buf, </span>0<span style="color: rgba(0, 0, 0, 1)">, len);
                        }
                        zos.closeEntry();
                        bis.close();
                    }
                }
            }
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 没有文件，不需要文件的copy</span>
<span style="color: rgba(0, 0, 0, 1)">            zos.closeEntry();
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">必须要执行 zos.finish(); close()时内部会调用finish()</span>
<span style="color: rgba(0, 0, 0, 1)">            zos.close();
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception e) {
            e.printStackTrace();
            log.error(</span>"资产信息下载zip异常：{}"<span style="color: rgba(0, 0, 0, 1)">, e);
        }
    }</span></pre>
