---
title: "C# Stocket"
date: 2019-06-26
description: "介绍 1、TCP/IP(Transmission Control Protocol/Internet Protocol) 即传输控制协议/网间协议，是一个工业标准的协议集，它是为广域网(WANs)设计的。 2、UDP(User Data Protocol，用户数据包协议)是与TCP相对应的协议。它属"
tags:
  - "cnblogs"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11069330.html"
---

<h1><span style="font-family: 隶书">介绍</span></h1>
<p><span style="font-family: 隶书">　　1、TCP/IP(Transmission Control Protocol/Internet Protocol) 即传输控制协议/网间协议，是一个工业标准的协议集，它是为广域网(WANs)设计的。</span></p>
<p><span style="font-family: 隶书">　　2、UDP(User Data Protocol，用户数据包协议)是与TCP相对应的协议。它属于TCP/IP协议族中的一种。</span></p>
<p><span style="font-family: 隶书">　　3、应用层(Application)：应用层是一个很广泛的概念，有一些基本相同的系统级TCP/IP应用以及应用协议，也有许多的企业商业应用和互联网应用。</span></p>
<p><span style="font-family: 隶书">　　4、传输层(Transport)：传输层包括UDP和TCP，UDP几乎不对报文进行检查，而TCP提供传输保证。</span></p>
<p><span style="font-family: 隶书">　　5、网络层(NetWork)：网络层协议由一系列协议组成，包括ICMP、IGMP、RIP、OSPF、IP(v4、v6)等。</span></p>
<p><span style="font-family: 隶书">　　6、链路层(Link)：又称为物理数据网络接口层，负责报文传输。</span></p>
<h1><span style="font-family: 隶书">网络4层协议</span></h1>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201906/1504448-20190622164252818-293835603.png" alt="" /></p>
<h1><span style="font-family: 隶书">&nbsp;原理图</span></h1>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201906/1504448-20190622164724336-420470574.png" alt="" /></p>
<h1>端口的分类</h1>
<p>　　1、公认端口(Well Known Ports)：从0到1023，它们紧密绑定(binding)于一些服务。通常这些端口的通讯，明确了某种服务的协议。例如：80端口实际上总是HTTP通讯。</p>
<p>　　2、注册端口(Registered Ports)：从1024到49151。它们松散地绑定于一些服务。也就是说许多服务绑定于这些端口，这些端口同样用于许多其他目的。例如：许多系统处理动态端口从1024左右开始。</p>
<p>　　3、动态和私有端口(Dynamic and/or Private Ports)：从49152到65535。理论上，不应为服务分配这些端口。实际上，机器通常从1024起分配动态端口，但也有例外：SUN的RPC端口从32768开始。</p>
<h2><span style="font-family: 隶书">&nbsp;服务端界面</span></h2>
<p><img src="https://img2018.cnblogs.com/blog/1504448/201906/1504448-20190622203036634-871722334.png" alt="" /></p>
<div class="cnblogs_code"><img id="code_img_closed_99718ba1-03e4-4b84-8b01-14db106219f4" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_99718ba1-03e4-4b84-8b01-14db106219f4" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_99718ba1-03e4-4b84-8b01-14db106219f4" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)">  1</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System;
</span><span style="color: rgba(0, 128, 128, 1)">  2</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Collections.Generic;
</span><span style="color: rgba(0, 128, 128, 1)">  3</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.ComponentModel;
</span><span style="color: rgba(0, 128, 128, 1)">  4</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Data;
</span><span style="color: rgba(0, 128, 128, 1)">  5</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Drawing;
</span><span style="color: rgba(0, 128, 128, 1)">  6</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Linq;
</span><span style="color: rgba(0, 128, 128, 1)">  7</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Text;
</span><span style="color: rgba(0, 128, 128, 1)">  8</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Windows.Forms;
</span><span style="color: rgba(0, 128, 128, 1)">  9</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Net.Sockets;
</span><span style="color: rgba(0, 128, 128, 1)"> 10</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Net;
</span><span style="color: rgba(0, 128, 128, 1)"> 11</span> <span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> System.Threading;
</span><span style="color: rgba(0, 128, 128, 1)"> 12</span> 
<span style="color: rgba(0, 128, 128, 1)"> 13</span> 
<span style="color: rgba(0, 128, 128, 1)"> 14</span> <span style="color: rgba(0, 0, 255, 1)">namespace</span><span style="color: rgba(0, 0, 0, 1)"> socket网络编程
</span><span style="color: rgba(0, 128, 128, 1)"> 15</span> <span style="color: rgba(0, 0, 0, 1)">{
</span><span style="color: rgba(0, 128, 128, 1)"> 16</span>     <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">partial</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> frmServer : Form
</span><span style="color: rgba(0, 128, 128, 1)"> 17</span> <span style="color: rgba(0, 0, 0, 1)">    {
</span><span style="color: rgba(0, 128, 128, 1)"> 18</span>         <span style="color: rgba(0, 0, 255, 1)">public</span><span style="color: rgba(0, 0, 0, 1)"> frmServer()
</span><span style="color: rgba(0, 128, 128, 1)"> 19</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 20</span> <span style="color: rgba(0, 0, 0, 1)">            InitializeComponent();
</span><span style="color: rgba(0, 128, 128, 1)"> 21</span>             Control.CheckForIllegalCrossThreadCalls = <span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 22</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 23</span> 
<span style="color: rgba(0, 128, 128, 1)"> 24</span>         <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> BtnStart_Click(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> sender, EventArgs e)
</span><span style="color: rgba(0, 128, 128, 1)"> 25</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 26</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 27</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 28</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">Socket服务器端
</span><span style="color: rgba(0, 128, 128, 1)"> 29</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">引入命名空间：using System.Net;
</span><span style="color: rgba(0, 128, 128, 1)"> 30</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">引入命名空间：using System.Net.Sockets;
</span><span style="color: rgba(0, 128, 128, 1)"> 31</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">1、创建Socket</span>
<span style="color: rgba(0, 128, 128, 1)"> 32</span>                 Socket serverSocket = <span style="color: rgba(0, 0, 255, 1)">new</span> Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第一个参数：设置网络寻址协议；第二个参数：设置数据传输方式；第三个参数：设置通信协议
</span><span style="color: rgba(0, 128, 128, 1)"> 33</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">2、绑定IP和端口</span>
<span style="color: rgba(0, 128, 128, 1)"> 34</span>                 <span style="color: rgba(0, 0, 255, 1)">this</span>.txtLog.Text = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">创建服务端Socket对象\r\n</span><span style="color: rgba(128, 0, 0, 1)">"</span>+<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.txtLog.Text;
</span><span style="color: rgba(0, 128, 128, 1)"> 35</span>                 IPAddress ip = IPAddress.Parse(txtIp.Text.Trim()); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">IP地址</span>
<span style="color: rgba(0, 128, 128, 1)"> 36</span>                 <span style="color: rgba(0, 0, 255, 1)">int</span> port = Convert.ToInt32(txtPort.Text.Trim()); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">端口</span>
<span style="color: rgba(0, 128, 128, 1)"> 37</span>                 IPEndPoint ipEndpoint = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> IPEndPoint(ip, port);
</span><span style="color: rgba(0, 128, 128, 1)"> 38</span> <span style="color: rgba(0, 0, 0, 1)">                serverSocket.Bind(ipEndpoint);
</span><span style="color: rgba(0, 128, 128, 1)"> 39</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">3、开启侦听</span>
<span style="color: rgba(0, 128, 128, 1)"> 40</span>                 serverSocket.Listen(<span style="color: rgba(128, 0, 128, 1)">10</span>); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">挂起连接队列的最大长度。
</span><span style="color: rgba(0, 128, 128, 1)"> 41</span>                 <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">4、开始接收客户端连接</span>
<span style="color: rgba(0, 128, 128, 1)"> 42</span>                 <span style="color: rgba(0, 0, 255, 1)">this</span>.txtLog.Text = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">开启接受客户端连接\r\n</span><span style="color: rgba(128, 0, 0, 1)">"</span> + <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.txtLog.Text;
</span><span style="color: rgba(0, 128, 128, 1)"> 43</span>                 ThreadPool.QueueUserWorkItem(<span style="color: rgba(0, 0, 255, 1)">new</span> WaitCallback(<span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.StartAcceptClient), serverSocket);
</span><span style="color: rgba(0, 128, 128, 1)"> 44</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 45</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)"> 46</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 47</span>                 <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
</span><span style="color: rgba(0, 128, 128, 1)"> 48</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 49</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 50</span>         List&lt;Socket&gt; ClientProxSocket = <span style="color: rgba(0, 0, 255, 1)">new</span> List&lt;Socket&gt;<span style="color: rgba(0, 0, 0, 1)">();
</span><span style="color: rgba(0, 128, 128, 1)"> 51</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> StartAcceptClient(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> state)
</span><span style="color: rgba(0, 128, 128, 1)"> 52</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 53</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)"> 54</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 55</span>                 <span style="color: rgba(0, 0, 255, 1)">var</span> serverSocket =<span style="color: rgba(0, 0, 0, 1)"> (Socket)state;
</span><span style="color: rgba(0, 128, 128, 1)"> 56</span>                 <span style="color: rgba(0, 0, 255, 1)">while</span> (<span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 128, 1)"> 57</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)"> 58</span>                     Socket proxSocket = serverSocket.Accept(); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">为新建连接创建新的Socket对象</span>
<span style="color: rgba(0, 128, 128, 1)"> 59</span>                     <span style="color: rgba(0, 0, 255, 1)">this</span>.txtLog.Text = <span style="color: rgba(0, 0, 255, 1)">string</span>.Format(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">客户端:{0}已连接\r\n{1}</span><span style="color: rgba(128, 0, 0, 1)">"</span>, proxSocket.RemoteEndPoint.ToString(), <span style="color: rgba(0, 0, 255, 1)">this</span>.txtLog.Text); <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">proxSocket.RemoteEndPoint：获取连接信息</span>
<span style="color: rgba(0, 128, 128, 1)"> 60</span> <span style="color: rgba(0, 0, 0, 1)">                    ClientProxSocket.Add(proxSocket);
</span><span style="color: rgba(0, 128, 128, 1)"> 61</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">服务端接受客户端的消息</span>
<span style="color: rgba(0, 128, 128, 1)"> 62</span>                     ThreadPool.QueueUserWorkItem(<span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> WaitCallback(RecieveData),proxSocket);
</span><span style="color: rgba(0, 128, 128, 1)"> 63</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">string str = DateTime.Now.ToString();
</span><span style="color: rgba(0, 128, 128, 1)"> 64</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">byte[] data = Encoding.UTF8.GetBytes(str); </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">待发送字节数组
</span><span style="color: rgba(0, 128, 128, 1)"> 65</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">proxSocket.Send(data, 0, data.Length, SocketFlags.None); </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">发送消息,发送的消息必须大于0个字节
</span><span style="color: rgba(0, 128, 128, 1)"> 66</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">proxSocket.Shutdown(SocketShutdown.Both);
</span><span style="color: rgba(0, 128, 128, 1)"> 67</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">this.txtLog.Text = "关闭\r\n" + this.txtLog.Text;
</span><span style="color: rgba(0, 128, 128, 1)"> 68</span>                     <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">proxSocket.Close(); </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">关闭</span>
<span style="color: rgba(0, 128, 128, 1)"> 69</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 70</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 71</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)"> 72</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 73</span>                 <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
</span><span style="color: rgba(0, 128, 128, 1)"> 74</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)"> 75</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)"> 76</span>         <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> RecieveData(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> obj)
</span><span style="color: rgba(0, 128, 128, 1)"> 77</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)"> 78</span>             <span style="color: rgba(0, 0, 255, 1)">var</span> proxSocket =<span style="color: rgba(0, 0, 0, 1)"> (Socket)obj;
</span><span style="color: rgba(0, 128, 128, 1)"> 79</span>             <span style="color: rgba(0, 0, 255, 1)">byte</span>[] data = <span style="color: rgba(0, 0, 255, 1)">new</span> <span style="color: rgba(0, 0, 255, 1)">byte</span>[<span style="color: rgba(128, 0, 128, 1)">1024</span> * <span style="color: rgba(128, 0, 128, 1)">1024</span><span style="color: rgba(0, 0, 0, 1)">];
</span><span style="color: rgba(0, 128, 128, 1)"> 80</span>             <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">方法返回值，实际接受的数据的长度(字节数)</span>
<span style="color: rgba(0, 128, 128, 1)"> 81</span>             <span style="color: rgba(0, 0, 255, 1)">while</span> (<span style="color: rgba(0, 0, 255, 1)">true</span><span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 128, 1)"> 82</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)"> 83</span>                 <span style="color: rgba(0, 0, 255, 1)">try</span> <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">处理客户端异常退出</span>
<span style="color: rgba(0, 128, 128, 1)"> 84</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)"> 85</span>                     <span style="color: rgba(0, 0, 255, 1)">int</span> reallen = proxSocket.Receive(data, <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">, data.Length, SocketFlags.None);
</span><span style="color: rgba(0, 128, 128, 1)"> 86</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span> (reallen == <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">)
</span><span style="color: rgba(0, 128, 128, 1)"> 87</span> <span style="color: rgba(0, 0, 0, 1)">                    {
</span><span style="color: rgba(0, 128, 128, 1)"> 88</span>                         <span style="color: rgba(0, 0, 255, 1)">this</span>.txtLog.Text = <span style="color: rgba(0, 0, 255, 1)">string</span>.Format(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">客户端:{0}退出\r\n{1}</span><span style="color: rgba(128, 0, 0, 1)">"</span>, proxSocket.RemoteEndPoint.ToString(), <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.txtLog.Text);
</span><span style="color: rgba(0, 128, 128, 1)"> 89</span>                         <span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">客户端退出</span>
<span style="color: rgba(0, 128, 128, 1)"> 90</span> <span style="color: rgba(0, 0, 0, 1)">                        proxSocket.Shutdown(SocketShutdown.Both);
</span><span style="color: rgba(0, 128, 128, 1)"> 91</span> <span style="color: rgba(0, 0, 0, 1)">                        proxSocket.Close();
</span><span style="color: rgba(0, 128, 128, 1)"> 92</span> <span style="color: rgba(0, 0, 0, 1)">                        ClientProxSocket.Remove(proxSocket);
</span><span style="color: rgba(0, 128, 128, 1)"> 93</span>                         <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 94</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)"> 95</span>                     <span style="color: rgba(0, 0, 255, 1)">string</span> formClientMsg = Encoding.UTF8.GetString(data, <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">, reallen);
</span><span style="color: rgba(0, 128, 128, 1)"> 96</span>                     <span style="color: rgba(0, 0, 255, 1)">this</span>.txtLog.Text = <span style="color: rgba(0, 0, 255, 1)">string</span>.Format(<span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">接受客户端{0}的消息:{1}\r\n{2}</span><span style="color: rgba(128, 0, 0, 1)">"</span>, proxSocket.RemoteEndPoint.ToString(), formClientMsg, <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.txtLog.Text);
</span><span style="color: rgba(0, 128, 128, 1)"> 97</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)"> 98</span>                 <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)"> 99</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">100</span> 
<span style="color: rgba(0, 128, 128, 1)">101</span> <span style="color: rgba(0, 0, 0, 1)">                }               
</span><span style="color: rgba(0, 128, 128, 1)">102</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">103</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">104</span>         <span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> BtnSend_Click(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> sender, EventArgs e)
</span><span style="color: rgba(0, 128, 128, 1)">105</span> <span style="color: rgba(0, 0, 0, 1)">        {
</span><span style="color: rgba(0, 128, 128, 1)">106</span>             <span style="color: rgba(0, 0, 255, 1)">try</span>
<span style="color: rgba(0, 128, 128, 1)">107</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">108</span>                 <span style="color: rgba(0, 0, 255, 1)">foreach</span> (<span style="color: rgba(0, 0, 255, 1)">var</span> socket <span style="color: rgba(0, 0, 255, 1)">in</span><span style="color: rgba(0, 0, 0, 1)"> ClientProxSocket)
</span><span style="color: rgba(0, 128, 128, 1)">109</span> <span style="color: rgba(0, 0, 0, 1)">                {
</span><span style="color: rgba(0, 128, 128, 1)">110</span>                     <span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (socket.Connected)
</span><span style="color: rgba(0, 128, 128, 1)">111</span> <span style="color: rgba(0, 0, 0, 1)">                    {
</span><span style="color: rgba(0, 128, 128, 1)">112</span>                         <span style="color: rgba(0, 0, 255, 1)">string</span> str = <span style="color: rgba(0, 0, 255, 1)">this</span><span style="color: rgba(0, 0, 0, 1)">.txtMsg.Text.Trim();
</span><span style="color: rgba(0, 128, 128, 1)">113</span>                         <span style="color: rgba(0, 0, 255, 1)">byte</span>[] data =<span style="color: rgba(0, 0, 0, 1)"> Encoding.UTF8.GetBytes(str);
</span><span style="color: rgba(0, 128, 128, 1)">114</span>                         socket.Send(data, <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">, data.Length, SocketFlags.None);
</span><span style="color: rgba(0, 128, 128, 1)">115</span> <span style="color: rgba(0, 0, 0, 1)">                    }
</span><span style="color: rgba(0, 128, 128, 1)">116</span> <span style="color: rgba(0, 0, 0, 1)">                }
</span><span style="color: rgba(0, 128, 128, 1)">117</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">118</span>             <span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
</span><span style="color: rgba(0, 128, 128, 1)">119</span> <span style="color: rgba(0, 0, 0, 1)">            {
</span><span style="color: rgba(0, 128, 128, 1)">120</span>                 <span style="color: rgba(0, 0, 255, 1)">throw</span><span style="color: rgba(0, 0, 0, 1)"> ex;
</span><span style="color: rgba(0, 128, 128, 1)">121</span> <span style="color: rgba(0, 0, 0, 1)">            }
</span><span style="color: rgba(0, 128, 128, 1)">122</span> <span style="color: rgba(0, 0, 0, 1)">        }
</span><span style="color: rgba(0, 128, 128, 1)">123</span> <span style="color: rgba(0, 0, 0, 1)">    }
</span><span style="color: rgba(0, 128, 128, 1)">124</span> }</pre>
