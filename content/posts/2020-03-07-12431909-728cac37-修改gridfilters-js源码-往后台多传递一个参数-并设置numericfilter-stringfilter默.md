{

  "title": "修改gridfilters.js源码，往后台多传递一个参数，并设置NumericFilter、StringFilter默认提示信息",
  "date": "2020-03-07",
  "description": "创作不易，转载请注明出处！！！ 效果 修改：ext-extend.js源码 在最后面添加3行，重写方法 代码拷贝区 修改：ux-all.js 我这里把js压缩过的代码，格式化过，格式地址：http://lzw.me/pages/jsbeautify/ 修改NumericFiltert提示信息(也就是",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12431909.html"

}

创作不易，转载请注明出处！！！

# 效果

![](/imported/posts/2020-03-07-12431909-728cac37-修改gridfilters-js源码-往后台多传递一个参数-并设置numericfilter-stringfilter默/images/img_001_1e3eb09d1206.png)

![](/imported/posts/2020-03-07-12431909-728cac37-修改gridfilters-js源码-往后台多传递一个参数-并设置numericfilter-stringfilter默/images/img_002_11a20c1af12e.png)

# 修改：ext-extend.js源码

　　在最后面添加3行，重写方法

![](/imported/posts/2020-03-07-12431909-728cac37-修改gridfilters-js源码-往后台多传递一个参数-并设置numericfilter-stringfilter默/images/img_003_54d8a0122ec2.png)

## 代码拷贝区

```text
Ext.override(Ext.ux.grid.GridFilters, {
    menuFilterText: "筛选"
});

Ext.override(Ext.ux.grid.filter.DateFilter, {
    afterText: "大于",
    beforeText: "小于",
    onText: "等于"
});
Ext.override(Ext.ux.grid.filter.String, {
    emptyText: 'Enter Filter Text...'
});
```

# 修改：ux-all.js

　　我这里把js压缩过的代码，格式化过，格式地址：[http://lzw.me/pages/jsbeautify/](http://lzw.me/pages/jsbeautify/)

## 修改NumericFiltert提示信息(也就是input标签中的，placeholder)

　　在源码的第1859行附近

![](/imported/posts/2020-03-07-12431909-728cac37-修改gridfilters-js源码-往后台多传递一个参数-并设置numericfilter-stringfilter默/images/img_004_3d79dd61f779.png)

## 修改addFilters

　　源码的第1463行附近

![](/imported/posts/2020-03-07-12431909-728cac37-修改gridfilters-js源码-往后台多传递一个参数-并设置numericfilter-stringfilter默/images/img_005_897701751100.png)

## 修改getFilterData

　　源码的第1492附近

![](/imported/posts/2020-03-07-12431909-728cac37-修改gridfilters-js源码-往后台多传递一个参数-并设置numericfilter-stringfilter默/images/img_006_7d874bd5ddac.png)

## 修改buildQuery

　　源码的第1522附近

![](/imported/posts/2020-03-07-12431909-728cac37-修改gridfilters-js源码-往后台多传递一个参数-并设置numericfilter-stringfilter默/images/img_007_4d4ab05aef89.png)
