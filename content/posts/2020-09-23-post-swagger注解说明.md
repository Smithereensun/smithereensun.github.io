---
title: "Swagger注解说明"
date: 2020-09-23
description: "常用注解：&#160;-&#160;@Api()用于类；&#160;表示标识这个类是swagger的资源&#160;-&#160;@ApiOperation()用于方法；&#160;表示一个http请求的操作&#160;-&#160;@ApiParam()用于方法，参数，字段说明；&#160;表示对"
tags:
  - "JAVA"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/13718228.html"
---

<p>常用注解：&nbsp;<br>-&nbsp;<strong>@Api()</strong>用于类；&nbsp;<br>表示标识这个类是swagger的资源&nbsp;<br>-&nbsp;<strong>@ApiOperation()</strong>用于方法；&nbsp;<br>表示一个http请求的操作&nbsp;<br>-&nbsp;<strong>@ApiParam()</strong>用于方法，参数，字段说明；&nbsp;<br>表示对参数的添加元数据（说明或是否必填等）&nbsp;<br>-&nbsp;<strong>@ApiModel()</strong>用于类&nbsp;<br>表示对类进行说明，用于参数用实体类接收&nbsp;<br>-&nbsp;<strong>@ApiModelProperty()</strong>用于方法，字段&nbsp;<br>表示对model属性的说明或者数据操作更改&nbsp;<br>-&nbsp;<strong>@ApiIgnore()</strong>用于类，方法，方法参数&nbsp;<br>表示这个方法或者类被忽略&nbsp;<br>-&nbsp;<strong>@ApiImplicitParam()</strong>&nbsp;用于方法&nbsp;<br>表示单独的请求参数&nbsp;<br>-&nbsp;<strong>@ApiImplicitParams()</strong>&nbsp;用于方法，包含多个 @ApiImplicitParam</p>
<p>具体使用举例说明：&nbsp;<br><strong>@Api()</strong>&nbsp;<br>用于类；表示标识这个类是swagger的资源&nbsp;<br>tags–表示说明&nbsp;<br>value–也是说明，可以使用tags替代&nbsp;</p>
<p><strong>@ApiOperation()</strong>&nbsp;用于方法；表示一个http请求的操作&nbsp;<br>value用于方法描述&nbsp;<br>notes用于提示内容&nbsp;<br>tags可以重新分组（视情况而用）</p>
<p><strong>@ApiParam()</strong>&nbsp;用于方法，参数，字段说明；表示对参数的添加元数据（说明或是否必填等）&nbsp;<br>name–参数名&nbsp;<br>value–参数说明&nbsp;<br>required–是否必填</p>
<p>&nbsp;</p>
