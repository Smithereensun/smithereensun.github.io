{

  "title": "MySQL 性能优化之慢查询",
  "date": "2020-06-15",
  "description": "性能优化的思路 首先需要使用慢查询功能，去获取所有查询时间比较长的SQL语句 其次使用explain命令去查询由问题的SQL的执行计划(脑补链接：点我直达1，点我直达2) 最后可以使用show profile[s] 查看由问题的SQL的性能使用情况 优化SQL语句 介绍 数据库查询快慢是影响项目性能",
  "tags": [
    "MySQL"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13128593.html"

}

# 性能优化的思路

1. 首先需要使用慢查询功能，去获取所有查询时间比较长的SQL语句
2. 其次使用explain命令去查询由问题的SQL的执行计划(脑补链接：[点我直达1](https://www.cnblogs.com/chenyanbin/p/13096937.html)，[点我直达2](https://www.cnblogs.com/chenyanbin/p/13110056.html))
3. 最后可以使用show profile[s] 查看由问题的SQL的性能使用情况
4. 优化SQL语句

# 介绍

　　数据库查询快慢是影响项目性能的一大因素，对于数据库，我们除了要优化SQL，更重要的是得**先找到需要优化的SQL语句**。

　　MySQL数据库有一个“**慢查询日志**”功能，用来**记录**查询时间**超过某个设定值的SQL**，这将极大程度帮助我们**快速定位到问题所在，以便对症下药**。

```text
至于查询时间的多少才算慢，每个项目、业务都有不同的要求。
    比如传统企业的软件允许查询时间高于某个值，但是把这个标准方在互联网项目或者访问量大的网站上，估计就是一个Bug，甚至可能升级为一个功能缺陷。
```

　　MySQL的慢查询日志功能，**默认是关闭的，需要手动开启**。

## 开启慢查询功能

### 查看是否开启慢查询功能

![](./images/images/img_001_43085709b73d.png)

![](./images/images/img_002_e9e0e0c486c2.png)

参数说明:

- **slow_query_log**:是否开启慢查询,on为开启,off为关闭;
- **log-slow-queries**:旧版(5.6以下版本)MySQL数据库慢查询存储路径,可以不设置该参数,系统则会给一个缺省的文件:host_name-slow.log
- **long_query_time**:慢查询阀值,当查询时间多于设置的阀值时,记录日志,单位为秒。

## 临时开启满查询功能

　　在MySQL执行SQL语句设置,但是如果重启MySQL的话会失效。

```text
set global slow_query_log=on;
set global long_query_time=1;
```

## 永久性开启慢查询

　　修改：/etc/my.cnf，添加以下内容，**然后重启MySQL服务**

```text
[mysqld]
lower_case_table_names=1
slow_query_log=ON
slow_query_log_file=/usr/local/mysql/data/chenyanbindeMacBook-Pro-slow.log
long_query_time=1
```

![](./images/images/img_003_cb04f9e7ffed.png)

### 查看满查询启动状态

![](./images/images/img_004_76287cff1c65.gif)

## 演示慢查询

　　为了演示方便，我们让sql睡眠3秒！

![](./images/images/img_005_0c06494a598f.gif)

![](./images/images/img_006_241c432e85f5.png)

格式说明：

- 第一行，SQL查询执行的具体时间
- 第二行，执行SQL查询的连接信息，用户和连接IP
- 第三行，记录了一些我们比较有用的信息，

  - **Query_timme，这条SQL执行的时间，越长则越慢**
  - **Lock_time，在MySQL服务器阶段(不是在存储引擎阶段)等待表锁时间**
  - **Rows_sent，查询返回的行数**
  - **Rows_examined，查询检查的行数，越长就越浪费时间**

- 第四行，设置时间戳，没有实际意义，只是和第一行对应执行时间。
- 第五行，执行的SQL语句记录信息

## 分析满查询日志

### MySQL自带的mysqldumpslow

![](./images/images/img_007_f84e40bc7c92.png)

参数说明：

- **-s**, 是表示按照何种方式排序，c、t、l、r分别是按照记录次数、时间、查询时间、返回的记录数来排序，ac、at、al、ar，表示相应的倒叙；
- **-t**, 是top n的意思，即为返回前面多少条的数据；
- **-g**, 后边可以写一个正则匹配模式，大小写不敏感的；

# MySQL性能fenix语句show profile（**重要**）

## 介绍

- Query Profiler是MySQL自带的一种**query诊断分析工具**，通过它可以分析出一条SQL语句**性能瓶颈**在什么地方。
- **通常使用explain，以及slow query log都无法做到精确分析，但是Query profiler却可以定位出一条SQL执行的各种资源消耗情况，比如CPU、IO等，以及该SQL执行所耗费的时间等。不过该工具只有在MySQL5.0.37以上版本中才有实现**
- **默认的情况下，MySQL的该功能没有打开，需要自己手动打开**

## 语句使用

- **show profile**和**show profiles**语句可以展示当前会话（退出session后，profiling重置为0）中执行语句的资源使用情况。
- **show profiles**：以列表形式显示最近发送到服务器上执行的语句的资源使用情况，显示的记录数由变量：**profiling_history_size**控制，默认15条
- **show profile**：只是最近一条语句执行的消息资源占用信息，默认实现Status和Duration两列

## 开启Profile功能

- Profile功能由MySQL会话变量：**profiling**控制，默认是**OFF**关闭状态。
- 查看是否开启了Profile功能

```text
select @@profiling;

show variables like '%profil%';
```

![](./images/images/img_008_235b827272ae.png)

打开profiling功能

```text
set profiling=1;
```

![](./images/images/img_009_ee16c9323f08.png)

## show profile用法

```text
SHOW PROFILE [type [, type] …… ] [FOR QUERY n] [LIMIT row_count [OFFSET offset]]

type: { ALL | BLOCK IO | CONTEXT SWITCHES | CPU | IPC | MEMORY | PAGE FAULTS | SOURCE | SWAPS }
```

![](./images/images/img_010_03ce7d5bc8a3.png)
