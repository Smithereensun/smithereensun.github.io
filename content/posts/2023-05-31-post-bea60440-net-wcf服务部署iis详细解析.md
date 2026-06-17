---
title: ".Net WCF服务部署IIS详细解析"
date: 2023-05-31
description: "官方解析：Windows Communication Foundation(WCF)是由微软开发的一系列支持数据通信的应用程序框架，可以翻译为Windows 通讯开发平台。整合了原有的windows通讯的 .net Remoting，WebService，Socket的机制，并融合有HTTP和FTP"
tags:
  - "WebService"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11583272.html"
---

<p>　　官方解析：Windows Communication Foundation(WCF)是由微软开发的一系列支持数据通信的应用程序框架，可以翻译为Windows 通讯开发平台。整合了原有的windows通讯的 .net Remoting，WebService，Socket的机制，并融合有<a href="http://baike.baidu.com/view/9472.htm" target="_blank" rel="noopener nofollow">HTTP</a>和<a href="http://baike.baidu.com/subview/369/6149695.htm" target="_blank" data-lemmaid="13839" rel="noopener nofollow">FTP</a>的相关技术。</p>
<h1>一、WCF服务的创建</h1>
<h2>第一步：创建WCF项目</h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201909/1504448-20190925084406707-1216685142.png" alt="" /></p>
<p>&nbsp;</p>
<p>&nbsp;创建完成之后，自动帮我们生成这些文件，2个类，一个接口，一个接口的实现，还有一个App.config配置文件(WCF具体的配置信息都在这个目录下)</p>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201909/1504448-20190925084453081-1386609507.png" alt="" /></p>
<p>&nbsp;</p>
<p><span style="color: rgba(255, 0, 255, 1)"><strong>&nbsp;IService1.cs</strong></span></p>
<p><span style="color: rgba(0, 0, 0, 1)">注：等会将WCF发布到IIS上涉及到网络传输，将对象持久化写到磁盘上，那么我们就需要序列化，实体类、自定义属性、类名上打上相应的标签</span></p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Collections.Generic;
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Linq;
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Runtime.Serialization;
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.ServiceModel;
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Text;
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> 
<span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> WCFDemo
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)">10</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 注意: 使用“重构”菜单上的“重命名”命令，可以同时更改代码和配置文件中的接口名“IService1”。</span>
<span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">    [ServiceContract]
</span><span style="color: rgba(0, 128, 128, 1)">12</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">interface</span><span style="color: rgba(0, 0, 0, 1)"> IService1
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 0, 1)">        [OperationContract]
</span><span style="color: rgba(0, 128, 128, 1)">15</span>         <span style="color: rgba(0, 0, 255, 1)">string</span> GetData(<span style="color: rgba(0, 0, 255, 1)">int</span><span style="color: rgba(0, 0, 0, 1)"> value);
</span><span style="color: rgba(0, 128, 128, 1)">16</span> 
<span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 0, 1)">        [OperationContract]
</span><span style="color: rgba(0, 128, 128, 1)">18</span> <span style="color: rgba(0, 0, 0, 1)">        CompositeType GetDataUsingDataContract(CompositeType composite);
</span><span style="color: rgba(0, 128, 128, 1)">19</span> 
<span style="color: rgba(0, 128, 128, 1)">20</span>         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> TODO: 在此添加您的服务操作</span>
<span style="color: rgba(0, 128, 128, 1)">21</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">22</span> 
<span style="color: rgba(0, 128, 128, 1)">23</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 使用下面示例中说明的数据约定将复合类型添加到服务操作。
</span><span style="color: rgba(0, 128, 128, 1)">24</span>     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 可以将 XSD 文件添加到项目中。在生成项目后，可以通过命名空间“WCFDemo.ContractType”直接使用其中定义的数据类型。</span>
<span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">    [DataContract]
</span><span style="color: rgba(0, 128, 128, 1)">26</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> CompositeType
</span><span style="color: rgba(0, 128, 128, 1)">27</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)">28</span>         <span style="color: rgba(0, 0, 255, 1)">bool</span> boolValue = <span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">29</span>         <span style="color: rgba(0, 0, 255, 1)">string</span> stringValue = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Hello </span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)">30</span> 
<span style="color: rgba(0, 128, 128, 1)">31</span> <span style="color: rgba(0, 0, 0, 1)">        [DataMember]
</span><span style="color: rgba(0, 128, 128, 1)">32</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">bool</span><span style="color: rgba(0, 0, 0, 1)"> BoolValue
</span><span style="color: rgba(0, 128, 128, 1)">33</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">34</span>             <span style="color: rgba(0, 0, 255, 1)">get</span> { <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> boolValue; }
</span><span style="color: rgba(0, 128, 128, 1)">35</span>             <span style="color: rgba(0, 0, 255, 1)">set</span> { boolValue =<span style="color: rgba(0, 0, 0, 1)"> value; }
</span><span style="color: rgba(0, 128, 128, 1)">36</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">37</span> 
<span style="color: rgba(0, 128, 128, 1)">38</span> <span style="color: rgba(0, 0, 0, 1)">        [DataMember]
</span><span style="color: rgba(0, 128, 128, 1)">39</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> StringValue
</span><span style="color: rgba(0, 128, 128, 1)">40</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">41</span>             <span style="color: rgba(0, 0, 255, 1)">get</span> { <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> stringValue; }
</span><span style="color: rgba(0, 128, 128, 1)">42</span>             <span style="color: rgba(0, 0, 255, 1)">set</span> { stringValue =<span style="color: rgba(0, 0, 0, 1)"> value; }
</span><span style="color: rgba(0, 128, 128, 1)">43</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">44</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">45</span> }</pre>
