{

  "title": "ORA-06502:at \"WMSYS.WM_CONCAT_IMPL\",line 30 解决方法整理",
  "date": "2019-07-09",
  "description": "之前数据量少的时候，用:select wm_concat(字段) from 表 拼接数据量小的话，没有问题，数据量超出4000个就会爆以下错误信息：** 解决方法(Oracle 函数xmlagg拼接): 效果图： SQL语句 拼接出来的语句，最后会多一个“,”，可以使用**substr**截取字符串",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11156228.html"

}

**　　之前数据量少的时候，用:select wm_concat(字段) from 表 拼接数据量小的话，没有问题，数据量超出4000个就会爆以下错误信息：**

![](/imported/posts/2019-07-09-11156228-c838fafc-ora-06502-at-wmsys-wm-concat-impl-line-30-解决方法整理/images/img_001_ebb4e3a8056f.png)

## 解决方法(Oracle 函数xmlagg拼接):

```text
1 语法格式：SELECT xmlagg(xmlparse(content 合并字段||’,’ wellformed) order by 排序字段).getclobval() FROM 表名
```

##  效果图：

![](/imported/posts/2019-07-09-11156228-c838fafc-ora-06502-at-wmsys-wm-concat-impl-line-30-解决方法整理/images/img_002_8f900a89c634.gif)
![](/imported/posts/2019-07-09-11156228-c838fafc-ora-06502-at-wmsys-wm-concat-impl-line-30-解决方法整理/images/img_003_961ddebeb323.gif)

```text
1  select xmlagg(xmlparse(content SECTION_NO||',' wellformed) order by SPS_ID).getclobval() SECTION_NO from REAL_PROJ_SECTION
```

SQL语句

![](/imported/posts/2019-07-09-11156228-c838fafc-ora-06502-at-wmsys-wm-concat-impl-line-30-解决方法整理/images/img_004_e87bdcf4e101.png)

拼接出来的语句，最后会多一个“,”，可以使用**substr**截取字符串和**length**计算字符长度配合使用

```text
 1 格式1： substr(string string, int a, int b);
 2
 3 　　格式2：substr(string string, int a) ;
 4
 5 解释：
 6
 7     格式1：
 8         1、string 需要截取的字符串
 9         2、a 截取字符串的开始位置（注：当a等于0或1时，都是从第一位开始截取）
10         3、b 要截取的字符串的长度
11
12     格式2：
13         1、string 需要截取的字符串
14         2、a 可以理解为从第a个字符开始截取后面所有的字符串。
```

最终sql语句：

```text
1 select substr(xmlagg(xmlparse(content SECTION_NO || ',' wellformed) order by SPS_ID)
2               .getclobval(),
3               0,
4               length(xmlagg(xmlparse(content SECTION_NO || ',' wellformed) order by SPS_ID)
5                      .getclobval()) - 1) SECTION_NO
6   from REAL_PROJ_SECTION
```

问题解决！~~~
