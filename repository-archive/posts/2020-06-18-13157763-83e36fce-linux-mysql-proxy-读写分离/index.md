{

  "title": "Linux MySQL Proxy 读写分离",
  "date": "2020-06-18",
  "description": "导读 因为**读写分离**是**建立在MySQL集群主从复制的基础上**，还不了解的，先看我另一篇博客：点我直达 MySQL-Proxy简介 mysql-proxy是mysql官方提供的mysql中间件服务，上游可接入若干个mysql-client，后端可连接若干个mysql-server。它使用m",
  "tags": [
    "MySQL",
    "Linux"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13157763.html"

}

# 导读

　　因为**读写分离**是**建立在MySQL集群主从复制的基础上**，还不了解的，先看我另一篇博客：[点我直达](https://www.cnblogs.com/chenyanbin/p/13154225.html)

# MySQL-Proxy简介

　　mysql-proxy是mysql官方提供的mysql中间件服务，上游可接入若干个mysql-client，后端可连接若干个mysql-server。它使用mysql协议，任何使用mysql-client的上游无需修改任何代码，即可迁移至mysql-proxy上。mysql-proxy最基本的用法，就是作为一个请求拦截，请求中转的中间层：

![](./images/images/img_001_89c732205503.png)

　　进一步的，mysql-proxy可以分析与修改请求。拦截查询和修改结果，需要通过编写Lua脚本来完成。mysql-proxy允许用户指定Lua脚本对请求进行拦截，对请求进行分析与修改，它还允许用户指定Lua脚本对服务器的返回结果进行修改，加入一些结果集或者去除一些结果集均可。

　　根本上，mysql-proxy是一个官方提供的框架，具备良好的扩展性，可以用来完成：

1. sql拦截与修改
2. 性能分析与监控
3. 读写分离
4. 请求路由

## 下载

官网链接：[点我直达](https://downloads.mysql.com/archives/proxy/)

```text
百度云盘地址：https://pan.baidu.com/s/1Aw1laIWYJVvHYshHXw4p_Q  密码: 9qif
```

![](./images/images/img_002_5734f5d3fd81.png)

## 需求

1. 1台MySQL-Proxy机器，IP：192.168.1.106
2. 1台MySQl主服务器(**可读可写**)，IP：192.168.1.107
3. 1台MySQL从服务器(**只读**)，IP：192.168.1.109

## 解压MySQL-Proxy

　　在192.168.1.106上解压：mysql-proxy-0.8.5-linux-el6-x86-64bit.tar.gz

![](./images/images/img_003_5fa501ed701f.png)

## 重命名文件

![](./images/images/img_004_8b8f36f644c7.png)

## MySQL配置

### 创建mysql-proxy.cnf

vim mysql-proxy.cnf

```text
[mysql-proxy]
admin-username=root     #admin用户名
admin-password=root      admin密码
proxy-address=192.168.1.106:4040 # 代理地址
proxy-backend-addresses=192.168.1.107:3306     #mysql主服务器ip地址，默认端口3306
proxy-read-only-backend-addresses=192.168.1.109:3306 #mysql从服务器ip地址,有多个逗号隔开 ip:port,ip:port,ip:port
proxy-lua-script=/cyb/soft/mysql-proxy/share/doc/mysql-proxy/rw-splitting.lua       #lua位置
log-file=/cyb/soft/mysql-proxy/log/mysql-proxy.log       #日志文件存储路径
log-level=debug
daemon=true     # mysql-proxy以守护进程方式运行
keepalive=true      #保持连接启动进程会有2个， 一号进程用来监视二号进程
```

![](./images/images/img_005_415f176700de.png)

## 创建log目录

![](./images/images/img_006_028c13e6a30b.png)

## 修改mysql-proxy.cnf文件的权限

```text
chmod 660 mysql-proxy.cnf
```

![](./images/images/img_007_e62933c9a62a.png)

## 修改rw-splitting.lua

```text
vim /cyb/soft/mysql-proxy/share/doc/mysql-proxy/rw-splitting.lua
```

![](./images/images/img_008_c931dc1ef78c.png)

![](./images/images/img_009_2bf564640d84.png)

min_idle_connections：最小闲置连接数

max_idle_connections：最大闲置连接数

## MySQL-Proxy启动

```text
 ./mysql-proxy --defaults-file=/cyb/soft/mysql-proxy.cnf
```

![](./images/images/img_010_b7a3b2f7254b.png)

## 测试

　　在192.168.1.106上关闭防火墙

```text
service iptables stop

chkconfig iptables off
```

![](./images/images/img_011_ba674b721e20.gif)

![](./images/images/img_012_08fdf2b61d73.gif)

　　演示过程中，有2次连不上，原因不明，还有待查证，目前功能是已经实现了，注意，**此时连mysql-proxy的端口已经不是3306了，是4040**
