{

  "title": "Mac mysql 5.7启动报错，解决之道 The server quit without updating PID file",
  "date": "2020-12-15",
  "description": "导读 晚上捣鼓数据库的时候，将mysql服务停止下，然后就死活启动不起来，这下可把我急坏了，自己数据库上有好多自己的个人项目，错误信息如下 网上百度一大堆，比如 /usr/local/mysql/data目录下必须为空 my.cnf中，必须指定存放mysql数据库的目录，在[mysqld]下设置：d",
  "tags": [
    "Mac系统",
    "SQL"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/14136475.html"

}

# 导读

　　晚上捣鼓数据库的时候，将mysql服务停止下，然后就死活启动不起来，这下可把我急坏了，自己数据库上有好多自己的个人项目，错误信息如下

```text
 ERROR! The server quit without updating PID file (/usr/local/mysql/data/chenyanbindeMacBook-Pro.local.pid)
```

```text
2020-12-14T15:53:06.6NZ mysqld_safe Logging to '/usr/local/mysql/data/chenyanbindeMacBook-Pro.local.err'.
2020-12-14T15:53:06.6NZ mysqld_safe Starting mysqld daemon with databases from /usr/local/mysql/data
2020-12-14T15:53:06.507326Z 0 [Note] --secure-file-priv is set to NULL. Operations related to importing and exporting data are disabled
2020-12-14T15:53:06.507468Z 0 [Note] /usr/local/mysql/bin/mysqld (mysqld 5.7.28) starting as process 5613 ...
2020-12-14T15:53:06.511336Z 0 [Note] InnoDB: Mutexes and rw_locks use GCC atomic builtins
2020-12-14T15:53:06.511358Z 0 [Note] InnoDB: Uses event mutexes
2020-12-14T15:53:06.511367Z 0 [Note] InnoDB: GCC builtin __atomic_thread_fence() is used for memory barrier
2020-12-14T15:53:06.511374Z 0 [Note] InnoDB: Compressed tables use zlib 1.2.11
2020-12-14T15:53:06.511620Z 0 [Note] InnoDB: Number of pools: 1
2020-12-14T15:53:06.511725Z 0 [Note] InnoDB: Using CPU crc32 instructions
2020-12-14T15:53:06.512845Z 0 [Note] InnoDB: Initializing buffer pool, total size = 128M, instances = 1, chunk size = 128M
2020-12-14T15:53:06.521779Z 0 [Note] InnoDB: Completed initialization of buffer pool
2020-12-14T15:53:06.534536Z 0 [ERROR] InnoDB: The innodb_system data file 'ibdata1' must be writable
2020-12-14T15:53:06.534618Z 0 [ERROR] InnoDB: The innodb_system data file 'ibdata1' must be writable
2020-12-14T15:53:06.534652Z 0 [ERROR] InnoDB: Plugin initialization aborted with error Generic error
2020-12-14T15:53:06.843208Z 0 [ERROR] Plugin 'InnoDB' init function returned error.
2020-12-14T15:53:06.843285Z 0 [ERROR] Plugin 'InnoDB' registration as a STORAGE ENGINE failed.
2020-12-14T15:53:06.843315Z 0 [ERROR] Failed to initialize builtin plugins.
2020-12-14T15:53:06.843333Z 0 [ERROR] Aborting

2020-12-14T15:53:06.843359Z 0 [Note] Binlog end
2020-12-14T15:53:06.843512Z 0 [Note] Shutting down plugin 'CSV'
2020-12-14T15:53:06.843810Z 0 [Note] /usr/local/mysql/bin/mysqld: Shutdown complete
```

![](/imported/posts/2020-12-15-14136475-2626bb7c-mac-mysql-5-7启动报错-解决之道-the-server-quit-without-updating-pid-/images/img_001_8d2daedf2901.png)

　　网上百度一大堆，比如

1. /usr/local/mysql/data目录下必须为空
2. my.cnf中，必须指定存放mysql数据库的目录，在[mysqld]下设置：datadir=/usr/local/mysql/data
3. 设置mysql data的权限

　　这些都没用，实在没辙了，那就来个简单粗暴的方式吧

## 解决之道

　　将：**/etc/my.cnf，直接删除掉**，然后重启mysql服务即可，我就通过这个方式，将mysql服务重新启动啦~
