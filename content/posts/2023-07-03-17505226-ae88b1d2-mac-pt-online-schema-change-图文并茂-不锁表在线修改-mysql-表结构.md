{

  "title": "Mac pt-online-schema-change 图文并茂、不锁表在线修改 MySQL 表结构",
  "date": "2023-07-03",
  "description": "导读 percona-toolkit 源自 Maatkit 和 Aspersa 工具，这两个工具是管理 MySQL 的最有名的工具，但 Maatkit 已经不维护了，全部归并到 percona-toolkit。Percona Toolkit 是一组高级的命令行工具，用来管理 MySQL 和系统任务，",
  "tags": [
    "SQL",
    "Mac系统",
    "pt-online-schema-change"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/17505226.html"

}

# 导读

　　percona-toolkit 源自 Maatkit 和 Aspersa 工具，这两个工具是管理 MySQL 的最有名的工具，但 Maatkit 已经不维护了，全部归并到 percona-toolkit。Percona Toolkit 是一组高级的命令行工具，用来管理 MySQL 和系统任务，主要包括：

- 验证主节点和复制数据的一致性
- 有效的对记录行进行归档
- 找出重复的索引
- 总结 MySQL 服务器
- 从日志和 tcpdump 中分析查询
- 问题发生时收集重要的系统信息
- 在线修改表结构

# 工作原理

- 如果存在外键，根据 `alter-foreign-keys-method` 参数的值，检测外键相关的表，做相应设置的处理。没有使用 alter-foreign-keys-method 指定特定的值，该工具不予执行
- 创建一个新的空表，其命名规则是：下划线 + 原表名 +`_new`
- 根据 alter 语句，更新新表的表结构；
- 创建触发器，用于记录从拷贝数据开始之后，对源数据表继续进行数据修改的操作记录下来，用于数据拷贝结束后，执行这些操作，保证数据不会丢失。如果表中已经定义了触发器这个工具就不能工作了。
- 拷贝数据，从源数据表中拷贝数据到新表中。
- 修改外键相关的子表，根据修改后的数据，修改外键关联的子表。
- rename 源数据表为 old 表，把新表 rename 为源表名，其通过一个 RENAME TABLE 同时处理两个表，实现原子操作。（RENAME TABLE dbteamdb.user TO dbteamdb._user_old, dbteamdb._user_new TO dbteamdb.user）
- 将 old 表删除、删除触发器。

# mac安装

```text
brew install percona-toolkit
```

官网地址：[https://www.percona.com/downloads/percona-toolkit/LATEST/](https://www.percona.com/downloads/percona-toolkit/LATEST/)

　　注：如果mac上安装很慢，请设置国内镜像：[点我直达](https://www.cnblogs.com/chenyanbin/p/17504648.html)

# 使用

## pt-online-schema-change参数

　　语法：**`pt-online-schema-change [OPTIONS]`**

### OPTIONS 参数说明

```text
    --user:
    -u，连接的用户名
    --password：
    -p，连接的密码
    --database：
    -D，连接的数据库
    --port
    -P，连接数据库的端口
    --host:
    -h，连接的主机地址
    --socket:
    -S，连接的套接字文件
    --ask-pass
    隐式输入连接 MySQL 的密码
    --charset
    指定修改的字符集
    --defaults-file
    -F，读取配置文件
    --alter：
    结构变更语句，不需要 alter table 关键字。可以指定多个更改，用逗号分隔。如下场景，需要注意：
        不能用 RENAME 来重命名表。
        列不能通过先删除，再添加的方式进行重命名，不会将数据拷贝到新列。
        如果加入的列非空而且没有默认值，则工具会失败。即其不会为你设置一个默认值，必须显示指定。
        删除外键 (drop foreign key constrain_name) 时，需要指定名称_constraint_name，而不是原始的 constraint_name。
        如：CONSTRAINT `fk_foo` FOREIGN KEY (`foo_id`) REFERENCES `bar` (`foo_id`)，需要指定：--alter "DROP FOREIGN KEY _fk_foo"
    --alter-foreign-keys-method
    如何把外键引用到新表？需要特殊处理带有外键约束的表，以保证它们可以应用到新表。当重命名表的时候，外键关系会带到重命名后的表上。
    该工具有两种方法，可以自动找到子表，并修改约束关系。
    auto： 在 rebuild_constraints 和 drop_swap 两种处理方式中选择一个。
    rebuild_constraints：使用 ALTER TABLE 语句先删除外键约束，然后再添加。如果子表很大的话，会导致长时间的阻塞。
    drop_swap： 执行 FOREIGN_KEY_CHECKS=0, 禁止外键约束，删除原表，再重命名新表。这种方式很快，也不会产生阻塞，但是有风险：
    1, 在删除原表和重命名新表的短时间内，表是不存在的，程序会返回错误。
    2, 如果重命名表出现错误，也不能回滚了。因为原表已经被删除。
    none： 类似"drop_swap"的处理方式，但是它不删除原表，并且外键关系会随着重命名转到老表上面。
    --[no]check-alter
    默认 yes，语法解析。配合 --dry-run 和 --print 一起运行，来检查是否有问题（change column，drop primary key）。
    --max-lag
    默认 1s。每个 chunk 拷贝完成后，会查看所有复制 Slave 的延迟情况。要是延迟大于该值，则暂停复制数据，直到所有从的滞后小于这个值，使用 Seconds_Behind_Master。如果有任何从滞后超过此选项的值，则该工具将睡眠 --check-interval 指定的时间，再检查。如果从被停止，将会永远等待，直到从开始同步，并且延迟小于该值。如果指定 --check-slave-lag，该工具只检查该服务器的延迟，而不是所有服务器。
    --check-slave-lag
    指定一个从库的 DSN 连接地址，如果从库超过 --max-lag 参数设置的值，就会暂停操作。
    --recursion-method
    默认是 show processlist，发现从的方法，也可以是 host，但需要在从上指定 report_host，通过 show slave hosts 来找到，可以指定 none 来不检查 Slave。
    METHOD       USES
    ===========  ==================
    processlist  SHOW PROCESSLIST
    hosts        SHOW SLAVE HOSTS
    dsn=DSN      DSNs from a table
    none         Do not find slaves
    指定 none 则表示不在乎从的延迟。
    --check-interval
    默认是 1。--max-lag 检查的睡眠时间。

    --[no]check-plan
    默认 yes。检查查询执行计划的安全性。

    --[no]check-replication-filters
    默认 yes。如果工具检测到服务器选项中有任何复制相关的筛选，如指定 binlog_ignore_db 和 replicate_do_db 此类。发现有这样的筛选，工具会报错且退出。因为如果更新的表 Master 上存在，而 Slave 上不存在，会导致复制的失败。使用–no-check-replication-filters 选项来禁用该检查。

    --[no]swap-tables
    默认 yes。交换原始表和新表，除非你禁止 --[no]drop-old-table。

    --[no]drop-triggers
    默认 yes，删除原表上的触发器。 --no-drop-triggers 会强制开启 --no-drop-old-table 即：不删除触发器就会强制不删除原表。

    --new-table-name
    复制创建新表的名称，默认 %T_new。

    --[no]drop-new-table
    默认 yes。删除新表，如果复制组织表失败。

    --[no]drop-old-table
    默认 yes。复制数据完成重命名之后，删除原表。如果有错误则会保留原表。

    --max-load
    默认为 Threads_running=25。每个 chunk 拷贝完后，会检查 SHOW GLOBAL STATUS 的内容，检查指标是否超过了指定的阈值。如果超过，则先暂停。这里可以用逗号分隔，指定多个条件，每个条件格式： status 指标 =MAX_VALUE 或者 status 指标：MAX_VALUE。如果不指定 MAX_VALUE，那么工具会这只其为当前值的 120%。

    --critical-load
    默认为 Threads_running=50。用法基本与 --max-load 类似，如果不指定 MAX_VALUE，那么工具会这只其为当前值的 200%。如果超过指定值，则工具直接退出，而不是暂停。

    --default-engine
    默认情况下，新的表与原始表是相同的存储引擎，所以如果原来的表使用 InnoDB 的，那么新表将使用 InnoDB 的。在涉及复制某些情况下，很可能主从的存储引擎不一样。使用该选项会默认使用默认的存储引擎。

    --set-vars
    设置 MySQL 变量，多个用逗号分割。默认该工具设置的是： wait_timeout=10000 innodb_lock_wait_timeout=1 lock_wait_timeout=60

    --chunk-size-limit
    当需要复制的块远大于设置的 chunk-size 大小，就不复制。默认值是 4.0，一个没有主键或唯一索引的表，块大小就是不确定的。

    --chunk-time
    在 chunk-time 执行的时间内，动态调整 chunk-size 的大小，以适应服务器性能的变化，该参数设置为 0, 或者指定 chunk-size, 都可以禁止动态调整。

    --chunk-size
    指定块的大小，默认是 1000 行，可以添加 k,M,G 后缀。这个块的大小要尽量与 --chunk-time 匹配，如果明确指定这个选项，那么每个块就会指定行数的大小。

    --[no]check-plan
    默认 yes。为了安全，检查查询的执行计划。默认情况下，这个工具在执行查询之前会先 EXPLAIN, 以获取一次少量的数据，如果是不好的 EXPLAIN, 那么会获取一次大量的数据，这个工具会多次执行 EXPALIN, 如果 EXPLAIN 不同的结果，那么就会认为这个查询是不安全的。
    --statistics
    打印出内部事件的数目，可以看到复制数据插入的数目。
    --dry-run
    创建和修改新表，但不会创建触发器、复制数据、和替换原表。并不真正执行，可以看到生成的执行语句，了解其执行步骤与细节。--dry-run 与 --execute 必须指定一个，二者相互排斥。和 --print 配合最佳。
    --execute
    确定修改表，则指定该参数。真正执行。--dry-run 与 --execute 必须指定一个，二者相互排斥。
    --print
    打印 SQL 语句到标准输出。指定此选项可以让你看到该工具所执行的语句，和 --dry-run 配合最佳。
    --progress
    复制数据的时候打印进度报告，二部分组成：第一部分是百分比，第二部分是时间。
    --quiet
    -q，不把信息标准输出。
```

## 添加索引

```text
pt-online-schema-change --user=root --password=rootroot --host=127.0.0.1 --port=3306 --alter "ADD INDEX idx_name(user_name) USING BTREE" D=yb_test,t=sys_user --no-check-replication-filters --print --execute --charset=utf8  --max-load=Threads_running=20
```

- user：用户名
- password：密码
- host：主机ip
- port：mysql端口号
- alter：改表语句，注意跟没有指定改表！！！！
- D：数据库
- t：待修改表名
- no-check-replication-filters：不检查复制筛选器
- print：打印SQL
- charset：指定修改的字符集
- max-load：限制20个线程执行，如果超过时，PT暂停操作，默认为25
- execute：执行

### 演示

　　注意：

　　　　1、在旧表中新建触发器

　　　　2、新建一张表命名格式：_原表名_new

　　　　3、将旧表数据，拷贝到新表；如果旧表中有数据CRUD操作，会通过触发器操作到新表

　　　　4、拷贝结束后，将原表改为旧表，新表改为原表，删除旧表，删除触发器

![](/imported/posts/2023-07-03-17505226-ae88b1d2-mac-pt-online-schema-change-图文并茂-不锁表在线修改-mysql-表结构/images/img_001_e3f37b3f79ef.gif)

![](/imported/posts/2023-07-03-17505226-ae88b1d2-mac-pt-online-schema-change-图文并茂-不锁表在线修改-mysql-表结构/images/img_002_cdecbacabe8c.png)

## 添加字段

```text
pt-online-schema-change --user=root --password=rootroot --host=127.0.0.1 --port=3306 --alter "ADD COLUMN t_remark varchar(255) NOT NULL default '' COMMENT '测试备注'" D=yb_test,t=sys_user --print --execute
```

- user：用户名
- password：密码
- host：主机ip
- port：mysql端口号
- alter：改表语句，注意跟没有指定改表！！！！
- D：数据库
- t：待修改表名
- print：打印SQL
- execute：执行

**注意：alter中不能出现``，必须使用''**

### 演示

![](/imported/posts/2023-07-03-17505226-ae88b1d2-mac-pt-online-schema-change-图文并茂-不锁表在线修改-mysql-表结构/images/img_003_fb033bf8e8a8.png)

![](/imported/posts/2023-07-03-17505226-ae88b1d2-mac-pt-online-schema-change-图文并茂-不锁表在线修改-mysql-表结构/images/img_004_ab0f43634b25.gif)

## 修改字段名称和长度(其他都类似)

```text
pt-online-schema-change --user=root --password=rootroot --host=127.0.0.1 --port=3306 --alter "CHANGE COLUMN t_remark t_remark_new varchar(64) NOT NULL DEFAULT '' COMMENT '测试备注-new'" D=yb_test,t=sys_user --no-check-alter --print --execute
```

- user：用户名
- password：密码
- host：主机ip
- port：mysql端口号
- alter：改表语句，注意跟没有指定改表！！！！
- D：数据库
- t：待修改表名
- print：打印SQL
- execute：执行
- no-check-alter：不语法解析

**注意：对于 change column 则需要指定：–no-check-alter**

![](/imported/posts/2023-07-03-17505226-ae88b1d2-mac-pt-online-schema-change-图文并茂-不锁表在线修改-mysql-表结构/images/img_005_066892ff1539.gif)

![](/imported/posts/2023-07-03-17505226-ae88b1d2-mac-pt-online-schema-change-图文并茂-不锁表在线修改-mysql-表结构/images/img_006_854f27786876.png)

## 删除字段

```text
pt-online-schema-change --user=root --password=Dl123456. --host=47.116.143.16 --port=3306 --alter "DROP COLUMN t_remark_new" D=yb_test,t=sys_user --print --execute
```

- user：用户名
- password：密码
- host：主机ip
- port：mysql端口号
- alter：改表语句，注意跟没有指定改表！！！！
- D：数据库
- t：待修改表名
- print：打印SQL
- execute：执行

![](/imported/posts/2023-07-03-17505226-ae88b1d2-mac-pt-online-schema-change-图文并茂-不锁表在线修改-mysql-表结构/images/img_007_e03259c2f6a6.gif)

![](/imported/posts/2023-07-03-17505226-ae88b1d2-mac-pt-online-schema-change-图文并茂-不锁表在线修改-mysql-表结构/images/img_008_7a1f3facdc95.png)
