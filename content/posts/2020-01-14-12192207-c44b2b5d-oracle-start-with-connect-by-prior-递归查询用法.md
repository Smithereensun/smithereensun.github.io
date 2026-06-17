{

  "title": "Oracle start with connect by prior 递归查询用法",
  "date": "2020-01-14",
  "description": "参考：https://www.cnblogs.com/benbenduo/p/4588612.html 这个子句主要是用于B树结构类型的数据递归查询，给出B树结构类型中的任意一个结点，遍历其最终父结点或者子结点。 先看原始数据： 对应B树结构为： 接下来看一个示例： 要求给出其中一个结点值，求其最终",
  "tags": [
    "SQL"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12192207.html"

}

参考：[https://www.cnblogs.com/benbenduo/p/4588612.html](https://www.cnblogs.com/benbenduo/p/4588612.html)

这个子句主要是用于B树结构类型的数据递归查询，给出B树结构类型中的任意一个结点，遍历其最终父结点或者子结点。

先看原始数据：

```text
create table a_test
( parentid varchar2(10),
  subid    varchar2(10));

insert into a_test values ( '1', '2' );
insert into a_test values ( '1', '3' );
insert into a_test values ( '2', '4' );
insert into a_test values ( '2', '5' );
insert into a_test values ( '3', '6' );
insert into a_test values ( '3', '7' );
insert into a_test values ( '5', '8' );
insert into a_test values ( '5', '9' );
insert into a_test values ( '7', '10' );
insert into a_test values ( '7', '11' );
insert into a_test values ( '10', '12' );
insert into a_test values ( '10', '13' );

commit;

select * from a_test;
```

![](/imported/posts/2020-01-14-12192207-c44b2b5d-oracle-start-with-connect-by-prior-递归查询用法/images/img_001_471da0f6115a.png)

 对应B树结构为：

![](/imported/posts/2020-01-14-12192207-c44b2b5d-oracle-start-with-connect-by-prior-递归查询用法/images/img_002_143f6af9dada.png)

 接下来看一个示例：

要求给出其中一个结点值，求其最终父结点。以7为例，看一下代码

![](/imported/posts/2020-01-14-12192207-c44b2b5d-oracle-start-with-connect-by-prior-递归查询用法/images/img_003_68a5b6e5b38e.png)

start with 子句：遍历起始条件，有个小技巧，如果要查父结点，这里可以用子结点的列，反之亦然。

connect by 子句：连接条件。关键词prior，prior跟父节点列parentid放在一起，就是往父结点方向遍历；prior跟子结点列subid放在一起，则往叶子结点方向遍历，

                         parentid、subid两列谁放在“=”前都无所谓，关键是prior跟谁在一起。

order by 子句：排序，不用多说。

 下面看看往叶子结点遍历的例子：

![](/imported/posts/2020-01-14-12192207-c44b2b5d-oracle-start-with-connect-by-prior-递归查询用法/images/img_004_05b25d8ed742.png)

这里start with 子句用了parentid列，具体区别后面举例说明。

connect by 子句中，prior跟subid在同一边，就是往叶子结点方向遍历去了。因为7有两个子结点，所以第一级中有两个结果（10和11），10有两个子结点（12,13），11无，所以第二级也有两个结果（12，13）。即12,13就是叶子结点。

 下面看下start with子句中选择不同的列的区别：

以查询叶子结点（往下遍历）为例

![](/imported/posts/2020-01-14-12192207-c44b2b5d-oracle-start-with-connect-by-prior-递归查询用法/images/img_005_7c5b1e65ce6a.png)

 结果很明显，原意是要以7为父结点，遍历其子结点，左图取的是父结点列的值，结果符合原意；右图取的是子结点列的值，结果多余的显示了7 的父结点3.

 关于where条件的语句，以后验证后再记录。先留个疑问

![](/imported/posts/2020-01-14-12192207-c44b2b5d-oracle-start-with-connect-by-prior-递归查询用法/images/img_006_9c2a6d0d60bf.png)
