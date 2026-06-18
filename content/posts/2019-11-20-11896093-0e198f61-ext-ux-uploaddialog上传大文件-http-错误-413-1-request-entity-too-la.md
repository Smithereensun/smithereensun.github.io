{

  "title": "Ext.ux.UploadDialog上传大文件 HTTP 错误 413.1 - Request Entity Too Large Web 服务器拒绝为请求提供服务，因为该请求实体过大。Web 服务器无法为请求提供服务，因为它正尝试与客户证书进行协商，但请求实体过大。",
  "date": "2019-11-20",
  "description": "问题描述 问题：HTTP 错误 404.13 - Not Found 请求筛选模块被配置为拒绝超过请求内容长度的请求。 原因：Web 服务器上的请求筛选被配置为拒绝该请求，因为内容长度超过配置的值（IIS 7 默认文件上传大小时30M）。 解决方法 web.config中，添加如下内容",
  "tags": [
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11896093.html"

}

# 问题描述

问题：HTTP 错误 404.13 - Not Found 请求筛选模块被配置为拒绝超过请求内容长度的请求。

原因：Web 服务器上的请求筛选被配置为拒绝该请求，因为内容长度超过配置的值（IIS 7 默认文件上传大小时30M）。

# 解决方法

## web.config中，添加如下内容

```text
  <system.webServer>
    <security>
      <requestFiltering>
        <requestLimits maxQueryString="102400" maxAllowedContentLength="102400000"/>
      </requestFiltering>
    </security>
  </system.webServer>
```
