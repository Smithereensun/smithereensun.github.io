{

  "title": "C#后台HttpWebRequest模拟跨域Ajax请求，注册Windows服务到服务器上",
  "date": "2019-07-23",
  "description": "项目需求，暂且叫A、B公司吧。我们公司需要从A公司哪里读取机器上的数据，放到我们数据库中。然后再将数据库中存的数据，提供一个接口，B公司来调用，大概这个意思。 好了，言归正传。这个是之前做好的界面，用户需要手动点击“开始”，然后写了个定时器，不停的来回调用 部分源码(5秒调用后台处理)** 一天晚上",
  "tags": [
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11231024.html"

}

项目需求，暂且叫A、B公司吧。我们公司需要从A公司哪里读取机器上的数据，放到我们数据库中。然后再将数据库中存的数据，提供一个接口，B公司来调用，大概这个意思。

　　好了，言归正传。这个是之前做好的界面，用户需要手动点击“开始”，然后写了个定时器，不停的来回调用

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_001_83582a117009.png)

**　　部分源码(5秒调用后台处理)**

```text
 1     function refreshCount() {
 2         if (prj.is_port_state_1 == false) {
 3             var grid_down = query_panel.grid_down;
 4             var RequestData = { "macName": "" };
 5             $.ajax({
 6                 url: "http://172.30.16.254:8080/IWFM_HuaLian/dataDock/getMacState",
 7                 type: 'POST',
 8                 dataType: "JSON",
 9                 contentType: 'application/json; charset=UTF-8',
10                 crossDomain: true,
11                 data: JSON.stringify(RequestData),
12                 xhrFields: {
13                     'Access-Control-Allow-Origin': '*'
14                 },
15                 success: function (resData) {
16                     var res = JSON.stringify(resData);
17                     Ext.Ajax.request({
18                         url: "WC030Handlers.csx",
19                         params: {
20                             tag: 'GetMacState',
21                             data: res
22                         },
23                         success: function (response, p) {
24                             grid_down.getStore().load();
25                         }
26                     });
27                 }
28             });
29         }
30     }
31
32     Ext.Msg.alert(MsgMrg.OptMsg, "开始运行！");
33     t1 = window.setInterval(refreshCount, 5000);
```

　　一天晚上，项目老总打电话过来说：这个功能需要优化下，不能让用户去手动点，应该写个Windows服务，注册到客户的服务器本地上，电脑一开机自动运行该服务。我：“好的，到时候功能优化下”。

　　好了，这就是为啥写这篇博客的由来，下面开始演示DEMO

## 第一步：创建C# Winform服务

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_002_f8c6f37cb355.png)

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_003_e80340e12938.png)

## 第二步：添加安装服务

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_004_36415712e2eb.png)

## 第三步：设置服务的信息

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_005_8f0b5cb33ddf.png)

## 第四步：选择本地服务

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_006_f8509bf4eae0.png)

## 第五步：写业务逻辑(**随性发挥**)

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_007_ddd5d74b9c0a.png)

## 第六步：生成项目,并创建二个bat文件

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_008_27d4e9ff6056.png)

**安装服务**

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_009_e6219c8bf7a4.png)

```text
1 格式:C:\\WINDOWS\\Microsoft.NET\\Framework\\v4.0.30319\\InstallUtil.exe  程序名称
```

**卸载服务**

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_010_dbfaac81773c.png)

```text
1 格式:C:\\WINDOWS\\Microsoft.NET\\Framework\\v4.0.30319\\InstallUtil.exe /u 项目名
```

## **注：安装Windows服务，请用管理员身份运行**

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_011_580ae237e5e2.png)

### 　　好了，上面注册Windows服务已经会配置了，下面演示利用HttpWebRequest模拟Ajax请求

** DEMO**
![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_012_33a382040a46.png)

![](/imported/posts/2019-07-23-11231024-b7309cce-c-后台httpwebrequest模拟跨域ajax请求-注册windows服务到服务器上/images/img_013_f613c85eab20.png)

** 源码**

```text
 1         private void Button1_Click(object sender, EventArgs e)
 2         {
 3             string res= PostWebRequest("http://172.30.16.254:8080/IWFM_HuaLian/dataDock/getMacState", "{ \"macName\": \"\" }", Encoding.UTF8);
 4         }
 5         /// <summary>
 6         /// Post数据接口
 7         /// </summary>
 8         /// <param name="postUrl">接口地址</param>
 9         /// <param name="paramData">提交json数据</param>
10         /// <param name="dataEncode">编码方式(Encoding.UTF8)</param>
11         /// <returns></returns>
12         private static string PostWebRequest(string postUrl, string paramData, Encoding dataEncode)
13         {
14             string responseContent = string.Empty;
15             try
16             {
17                 byte[] byteArray = dataEncode.GetBytes(paramData); //转化
18                 HttpWebRequest webReq = (HttpWebRequest)WebRequest.Create(new Uri(postUrl));
19                 webReq.Method = "POST";
20                 webReq.ContentType = "application/json; charset=UTF-8";
21                 webReq.Accept = "application/json, text/javascript, */*; q=0.01"; //注：调试的过程中，报415，这里可能需要修改下
22                 webReq.ContentLength = byteArray.Length;
23                 using (Stream reqStream = webReq.GetRequestStream())
24                 {
25                     reqStream.Write(byteArray, 0, byteArray.Length);//写入参数
26                     //reqStream.Close();
27                 }
28                 using (HttpWebResponse response = (HttpWebResponse)webReq.GetResponse())
29                 {
30                     using (Stream myResponseStream = response.GetResponseStream())
31                     {
32                         using (StreamReader myStreamReader = new StreamReader(myResponseStream, Encoding.UTF8))
33                         {
34                             responseContent = myStreamReader.ReadToEnd().ToString();
35                         }
36                     }
37                 }
38             }
39             catch (Exception ex)
40             {
41                 return ex.Message;
42             }
43             return responseContent;
44         }
```
