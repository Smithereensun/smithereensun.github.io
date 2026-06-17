{

  "title": "jquery Easy UI Datagrid(数据网格)学习心德，附API",
  "date": "2019-07-11",
  "description": "第一步，引入主要的css样式和js文件 引入主要CSS 引入主要js文件 扩展日期js文件源码 如需下载jquery文件**，百度云盘地址：https://pan.baidu.com/s/17RTAyaY9oFAeRgfjlW0Mew 提取码：uknd 第二步，创建table用于存放数据网格 创建t",
  "tags": [
    "cnblogs"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11173287.html"

}

##

## 第一步，引入主要的css样式和js文件

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_002_961ddebeb323.gif)

```text
1 <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
2     <title></title>
3     <meta charset="utf-8" />
4     <link href="../../Script/jquery-easyui-1.7.0/themes/icon.css" rel="stylesheet" />
5     <!--引入图标css样式-->
6     <link href="../../Script/jquery-easyui-1.7.0/themes/material/easyui.css" rel="stylesheet" />
7     <!--引入总的css样式-->
8 </head>
```

引入主要CSS

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_002_961ddebeb323.gif)

```text
1     <script src="../../Script/jquery.min.js"></script>
2     <!--引入默认jquery ui支持的jquery文件-->
3     <script src="../../Script/jquery.easyui.min.js"></script>
4     <!--引入jquery ui文件-->
5     <script src="../../Script/easyui-lang-zh_CN.js"></script>
6     <!--引入中文字体库-->
7     <script src="../../Script/datapattern.js"></script>
8     <!--引入扩展日期js文件，格式化日期类型-->
```

引入主要js文件

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_002_961ddebeb323.gif)

```text
 1 /**
 2  * 对Date的扩展，将 Date 转化为指定格式的String
 3  * 月(M)、日(d)、12小时(h)、24小时(H)、分(m)、秒(s)、周(E)、季度(q) 可以用 1-2 个占位符
 4  * 年(y)可以用 1-4 个占位符，毫秒(S)只能用 1 个占位符(是 1-3 位的数字)
 5  * eg:
 6  * (new Date()).pattern("yyyy-MM-dd hh:mm:ss.S") ==> 2006-07-02 08:09:04.423
 7  * (new Date()).pattern("yyyy-MM-dd E HH:mm:ss") ==> 2009-03-10 二 20:09:04
 8  * (new Date()).pattern("yyyy-MM-dd EE hh:mm:ss") ==> 2009-03-10 周二 08:09:04
 9  * (new Date()).pattern("yyyy-MM-dd EEE hh:mm:ss") ==> 2009-03-10 星期二 08:09:04
10  * (new Date()).pattern("yyyy-M-d h:m:s.S") ==> 2006-7-2 8:9:4.18
11  */
12 Date.prototype.pattern = function (fmt) {
13     var o = {
14         "M+": this.getMonth() + 1, //月份
15         "d+": this.getDate(), //日
16         "h+": this.getHours() % 12 == 0 ? 12 : this.getHours() % 12, //小时
17         "H+": this.getHours(), //小时
18         "m+": this.getMinutes(), //分
19         "s+": this.getSeconds(), //秒
20         "q+": Math.floor((this.getMonth() + 3) / 3), //季度
21         "S": this.getMilliseconds() //毫秒
22     };
23     var week = {
24         "0": "/u65e5",
25         "1": "/u4e00",
26         "2": "/u4e8c",
27         "3": "/u4e09",
28         "4": "/u56db",
29         "5": "/u4e94",
30         "6": "/u516d"
31     };
32     if (/(y+)/.test(fmt)) {
33         fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
34     }
35     if (/(E+)/.test(fmt)) {
36         fmt = fmt.replace(RegExp.$1, ((RegExp.$1.length > 1) ? (RegExp.$1.length > 2 ? "/u661f/u671f" : "/u5468") : "") + week[this.getDay() + ""]);
37     }
38     for (var k in o) {
39         if (new RegExp("(" + k + ")").test(fmt)) {
40             fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
41         }
42     }
43     return fmt;
44 }
```

扩展日期js文件源码

**如需下载jquery文件**，百度云盘地址：https://pan.baidu.com/s/17RTAyaY9oFAeRgfjlW0Mew 

*提取码：uknd
*

## 第二步，创建table用于存放数据网格

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_002_961ddebeb323.gif)

```text
1     <table id="tt" style="width:700px" title="标题" iconcls="icon-edit">
2
3     </table>
```

创建table

## 第三步，写js脚本，并异步请求后台数据返回JSON格式

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_002_961ddebeb323.gif)

```text
 1     <script type="text/javascript">
 2         initTable();
 3
 4         //初始化表格
 5         function initTable() {
 6             $("#tt").datagrid({
 7                 url: "LoadNews4EasyTable.ashx", //从远程站点请求数据的 URL;rows:10;page:请求当前页；要求返回的数据:{total:200,rows:[{},{}]}
 8                 title: "新闻列表",
 9                 width: 700, //宽度
10                 height: 400, //高度
11                 fitColumns: true, //设置为 true，则会自动扩大或缩小列的尺寸以适应网格的宽度并且防止水平滚动。
12                 idField: "id", //后台返回数据行中的主键列，注意大小写
13                 loadMsg: "正在加载用户数据", //从远程站点加载数据时，显示的提示消息
14                 pagination: true, //设置为true，则在数据网络(datagrid)底部显示分页工具栏
15                 singleSelect: false, //是否允许选中多行
16                 rownumbers: true, //显示带有行号的列
17                 striped:true, //奇偶行不同颜色
18                 pageSize: 10, //初始化页面尺寸，一页多少条
19                 pageNumber: 1, //初始化页码
20                 pageList: [5,10, 20, 30,50,100], //允许，一页多少条的数据
21                 queryParams: {}, //发送异步请求，额外传递的数据
22                 columns: [[
23                     { field: 'ck', checkbox: true, align: 'left', width: 50 }, //CheckBox列
24                     { field: 'id', title: '编号', width: 80 },
25                     { field: 'title', title: '新闻标题', width: 120 },
26                     {
27                         field: 'date', title: '提交时间', width: 80, align: 'center',
28                         formatter: function (value,row,index) {
29                             return (eval(value.replace(/\/Date\((\d+)\)\//gi,"new Date($1)"))).pattern("yyyy-M-d");
30                         }
31                     }
32                 ]],
33                 toolbar: [{
34                     id: 'btnDownShelf',
35                     text: '添加新闻',
36                     iconCls: 'icon-add',
37                     handler: function () {
38                         alert("添加按钮");
39                     }
40                 }]
41             });
42         };
43     </script>
```

js脚本

## 第四步，后台关键代码

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_001_8f900a89c634.gif)
![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_002_961ddebeb323.gif)

```text
 1 using System;
 2 using System.Collections.Generic;
 3 using System.Linq;
 4 using System.Web;
 5 using Model;
 6 using Dll;
 7 using Common;
 8 using System.Web.Script.Serialization;
 9 using System.Data;
10
11 namespace ThreeLayerWebDemo._2019_7_11.EasyCRUD
12 {
13     /// <summary>
14     /// LoadNews4EasyTable 的摘要说明
15     /// </summary>
16     public class LoadNews4EasyTable : IHttpHandler
17     {
18
19         public void ProcessRequest(HttpContext context)
20         {
21             context.Response.ContentType = "text/plain";
22             //注：异步请求，默认会传入后台2个参数，分别为：page；rows
23             int pageSize = int.Parse(context.Request["rows"]??"10"); //拿到前台传入的一页的个数
24             int pageIndex = int.Parse(context.Request["page"] ?? "1"); //拿到前台传入的当前页
25             int total = 0; //总的行数
26             Model.Main m = new Main(); //实体类
27             string sql = m.GetDataPaging(pageSize, pageIndex); //获取分页sql语句
28             List<Main> newsList = Common.ToEntity.DtConvertToModel<Main>(SqlHelper.GetList(sql)); //返回分页数据list集合
29             DataTable dt =SqlHelper.GetList(m.GetAllRowsCount()); //获取数据库中所有的记录数
30             total = Convert.ToInt32(dt.Rows[0][0]); //总的行数
31             var data = new {total=total,rows=newsList }; //匿名类
32             JavaScriptSerializer js = new JavaScriptSerializer();
33             string jsonStr = js.Serialize(data); //转换成json格式，发送给前台
34             context.Response.Write(jsonStr); //发送前台
35         }
36
37         public bool IsReusable
38         {
39             get
40             {
41                 return false;
42             }
43         }
44     }
45 }
```

后台关键代码

**后台传前台json格式**

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_003_9ea2b8f2f71c.png)

## 第六步，效果图

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_004_5e8948fe3297.png)

### 以下jquery ui数据网格完整api截图

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_005_47f8dfd18ecd.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_006_558df2ba4058.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_007_a8a2ea8c0376.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_008_46aa2108a038.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_009_c8d387b57516.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_010_1b7c7f43e711.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_011_35c2af9ae297.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_012_0f5f2e6d3e10.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_013_5f0a79a0df67.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_014_6aefdda09390.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_015_2ee514265c3f.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_016_374b31f6fc30.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_017_ee0b966faa94.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_018_db713f0be860.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_019_00471f5e1c57.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_020_484714dce27e.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_021_549f71c199c6.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_022_a18a9db5b041.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_023_dc1fc746d0d4.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_024_d374a1e89690.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_025_748d006f8a9c.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_026_3f5f7b8911cf.png)

![](/imported/posts/2019-07-11-11173287-58dc9b4c-jquery-easy-ui-datagrid-数据网格-学习心德-附api/images/img_027_25822bd632e9.png)
