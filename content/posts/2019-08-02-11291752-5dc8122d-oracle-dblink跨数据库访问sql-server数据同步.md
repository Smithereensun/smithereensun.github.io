{

  "title": "Oracle DBLink跨数据库访问SQL server数据同步",
  "date": "2019-08-02",
  "description": "第一步：需要去下载一个透明网管，相当于一个中间件(我们用的Oracle 11g，可能不同的数据库版本要安装不同的透明网管) 需要的朋友请到我的百度云盘上下载** 链接：https://pan.baidu.com/s/1W6rEww1_NxxsMXYi0BOKPQ ** 提取码：sac2 ** 第二步",
  "tags": [
    "SQL"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11291752.html"

}

# 　　第一步：需要去下载一个透明网管，相当于一个中间件(我们用的Oracle 11g，可能不同的数据库版本要安装不同的透明网管)

**需要的朋友请到我的百度云盘上下载**

**链接：https://pan.baidu.com/s/1W6rEww1_NxxsMXYi0BOKPQ **
**提取码：sac2 **

# 　　第二步：安装透明网关

### 1、解压安装包后，点击setup.exe安装

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_001_49d3c5754439.png)

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_002_1fab260e9b79.png)

### 2、下一步(注：貌似一定要和Oracle数据库安装目录一致，第一次安装的时候，就和Oracle安装在不同地方了，最终百度很久发现，要和Oracle安装同一个位置)

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_003_45afcbd27140.png)

### 3、选择组建，选择SQL Server

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_004_8a4f7f378e2c.png)

### 4、填写SQL SERVER的主机名和数据库名称

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_005_1ba798cd117d.png)

### 5、开始安装

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_006_45334c6a8e59.png)

### 6、安装完成后就退出，然后开始配置监听，下面是重点！！！！

#  　　第三步：透明网关配置

## ** 配置说明：**

## **本地Oracle安装目录：D:\Oracle\product\11.2.0\dbhome_1**

## **本地DBLink安装目录:D:\Oracle\product\11.2.0\dbhome_1**

## **SQL Server：账号：sa;密码:password；IP地址:127.0.0.1**

## 1、来到:D:\Oracle\product\11.2.0\dbhome_1\dg4msql\admin;打开initdg4msql.ora

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_007_0517f269ef9b.png)

```text
1 这个目录下可以看到以下initdg4msql.ora文件，上面在安装透明网关的时候有配置的要链接SQL SERVER数据的地址和数据库名称，在这里都可以体现：
```

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_008_68d6c57ffb18.png)

## 配置文件：initdg4msql.ora

```text
 1 # This is a customized agent init file that contains the HS parameters
 2 # that are needed for the Database Gateway for Microsoft SQL Server
 3
 4 #
 5 # HS init parameters
 6 #
 7 HS_FDS_CONNECT_INFO=[127.0.0.1]:1433//DEMO   注：连接其他的SQL Server可修改此处
 8 HS_FDS_TRACE_LEVEL=OFF
 9 HS_FDS_RECOVERY_ACCOUNT=RECOVER
10 HS_FDS_RECOVERY_PWD=RECOVER
```

### **检查一下HS_FDS_CONNECT_INFO是否是我们想要链接的地址，格式为：目标数据库的IP地址：端口//数据库名。SQL SERVER的默认端口是1433。**

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_009_5231fe194b51.png)

## 配置文件:listener.ora.sample(localhost是监听的IP地址，这里我们连的是本地,127.0.0.1也是可以的)

```text
 1 # This is a sample listener.ora that contains the NET8 parameters that are
 2 # needed to connect to an HS Agent
 3
 4 LISTENER =
 5  (ADDRESS_LIST=
 6       (ADDRESS=(PROTOCOL=tcp)(HOST=localhost)(PORT=1521))
 7  )
 8
 9 SID_LIST_LISTENER=
10   (SID_LIST=
11       (SID_DESC=
12          (SID_NAME=dg4msql)
13          (ORACLE_HOME=D:\Oracle\product\11.2.0\dbhome_1)
14          (PROGRAM=dg4msql)
15       )
16   )
17
18 #CONNECT_TIMEOUT_LISTENER = 0
```

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_010_4cfa4617c163.png)

## 配置文件：tnsnames.ora.sample

```text
1 # This is a sample tnsnames.ora that contains the NET8 parameters that are
2 # needed to connect to an HS Agent
3
4 dg4msql  =
5   (DESCRIPTION=
6     (ADDRESS=(PROTOCOL=tcp)(HOST=localhost)(PORT=1521))
7     (CONNECT_DATA=(SID=dg4msql))
8     (HS=OK)
9   )
```

##  2、配置透明网关的监听，来到：D:\Oracle\product\11.2.0\dbhome_1\NETWORK\ADMIN(开始配置这3个文件)

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_011_ad36192ce6f3.png)

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_012_274f7abfa234.png)

## 配置文件：listener.ora

```text
 1 # This is a sample listener.ora that contains the NET8 parameters that are
 2 # needed to connect to an HS Agent
 3 SID_LIST_LISTENER =
 4   (SID_LIST =
 5     (SID_DESC =
 6       (SID_NAME = CLRExtProc)
 7       (ORACLE_HOME = D:\Oracle\product\11.2.0\dbhome_1)
 8       (PROGRAM = extproc)
 9       (ENVS = "EXTPROC_DLLS=ONLY:D:\Oracle\product\11.2.0\dbhome_1\bin\oraclr11.dll")
10     )
11     (SID_DESC=
12          (SID_NAME=dg4msql)
13          (ORACLE_HOME=D:\Oracle\product\11.2.0\dbhome_1)
14          (PROGRAM=dg4msql)
15     )
16   )
17
18 LISTENER =
19   (DESCRIPTION_LIST =
20     (DESCRIPTION =
21       (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))
22       (ADDRESS = (PROTOCOL = TCP)(HOST = YRDLG5GS4G3ODYI)(PORT = 1521))
23       (ADDRESS=(PROTOCOL=tcp)(HOST=127.0.0.1)(PORT=1521))
24     )
25   )
26
27 ADR_BASE_LISTENER = D:\Oracle
28
29 #CONNECT_TIMEOUT_LISTENER = 0
```

```text
1 这里需要注意的主要是一下几点：
2 PROGRAM为dg4msql：因为实例的配置文件在dg4msql目录下，就是上面的initdg4msql.ora文件所在的目录
3 SID_NAME为dg4msql：这个sid就是上面的文件名中的sid，initdg4msql.ora的sid为dg4msql
4 ORACLE_HOME就是我们透明网关的安装目录
5 ORACLE的监听端口是1521，我的oracle和透明网关是安装在同一台机器上的，所以透明网关的监听端口设置为1522。
6 一个initSID.ora文件就对应一个SID_DESC，可以根据想要链接的数据库来配置。
```

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_013_1be5ed24aef5.png)

## 配置文件：sqlnet.ora

```text
 1 # sqlnet.ora Network Configuration File: D:\Oracle\product\11.2.0\dbhome_1\network\admin\sqlnet.ora
 2 # Generated by Oracle configuration tools.
 3
 4 # This file is actually generated by netca. But if customers choose to
 5 # install "Software Only", this file wont exist and without the native
 6 # authentication, they will not be able to connect to the database on NT.
 7
 8 SQLNET.AUTHENTICATION_SERVICES= (NONE)
 9
10 NAMES.DIRECTORY_PATH= (TNSNAMES, EZCONNECT)
```

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_014_5013b43bed2d.png)

## 配置文件：tnsnames.ora

```text
 1 # This is a sample tnsnames.ora that contains the NET8 parameters that are
 2 # needed to connect to an HS Agent
 3 ORCL =
 4   (DESCRIPTION =
 5     (ADDRESS = (PROTOCOL = TCP)(HOST = localhost)(PORT = 1521))
 6     (CONNECT_DATA =
 7       (SERVER = DEDICATED)
 8       (SERVICE_NAME = orcl)
 9     )
10   )
11
12 dg4msql  =
13   (DESCRIPTION=
14     (ADDRESS=(PROTOCOL=tcp)(HOST=127.0.0.1)(PORT=1521))
15     (CONNECT_DATA=(SID=dg4msql))
16     (HS=OK)
17   )
```

### 配置完之后，一定不要忘记重启监听！！！！！！一定不要忘记重启监听！！！！！！一定不要忘记重启监听！！！！！！

```text
1 命令：lsnrctl reload
```

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_015_e2484231e1b2.png)

## 查看监听状态：

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_016_eb78170ffd79.png)

# 　　第四步：Oracle配置DBLink

##  1、先查看哪些用户可以使用DBLink，没有则创建权限

```text
1 SELECT * FROM user_sys_privs where privilege like upper('%DATABASE LINK%')
```

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_017_a27ccf2923b1.png)

## 赋权限配置命令

```text
1 如：grant create public database link to system ;
2 格式：grant create public database link to 用户名 ;
```

## 2、建立DBLink（用户要一定要权限才可以继续往下执行哦！没有的往上看，给用户配置权限）

```text
1 查询dblink：
2 select * from dba_db_links;
3
4 删除dblink：
5 DROP DATABASE LINK [name];
```

```text
 1 create database link DBTEST1
 2   connect to SA identified by "password"
 3   using 'dg4msql';
 4
 5
 6
 7 格式：
 8 create database link **DBLink名称
** 9   connect to SQL Server账户 identified by "**SQL Server密码**"
10   using '**SID**';
```

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_018_17d0a7272093.png)

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_019_0054100e76e8.png)

### 搞定！！！！

#  下面这个报错信息，QQ群问一个遍，很少人知道DBLink这玩意，百度上资料也很少，捣鼓一下午，终于搞定了

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_020_a4193d97a866.png)

# 出现这个问题是因为这6个文件导致的！！！！！！

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_021_e687382dd94e.png)

![](/imported/posts/2019-08-02-11291752-5dc8122d-oracle-dblink跨数据库访问sql-server数据同步/images/img_022_f543cacc8051.png)

 捣鼓一下午，问题找到是因为这6个文件配置出问题了，这次就不再叙述了，修改那个配置文件了，配置文件因人而异，剩下的自己百度去查吧~~~~好了，捣鼓一天了，洗洗睡了，拜~~

## 整理的配置文档：

链接：https://pan.baidu.com/s/1Wdlo7j1NVmbmrvEwYNk1qw
提取码：6esm
