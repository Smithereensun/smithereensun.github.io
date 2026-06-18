{

  "title": "Zookeeper的安装与集群搭建",
  "date": "2020-01-17",
  "description": "简介 Zookeeper下载 官网地址：点我直达 百度云盘：点我直达 踩坑录 官网下载一定要下载带bin的 要不然zookeeper起不起来，找不到加载类，原来从版本3.5.5开始，带有bin名称的包才是我们想要的下载可以直接使用的里面有编译后的二进制的包，而之前的普通的tar.gz的包里面是只是源",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12202048.html"

}

# 简介

![](./images/images/img_001_8bd71f0920b3.png)

# Zookeeper下载

官网地址：[点我直达](https://www.apache.org/dyn/closer.cgi/zookeeper/)

百度云盘：[点我直达](https://pan.baidu.com/s/1uZnWUsePTJSJ-Xkm33xdHQ)

# 踩坑录

官网下载一定要下载带bin的

![](./images/images/img_002_ba718db4339c.png)

要不然zookeeper起不起来，找不到加载类，原来从版本3.5.5开始，带有bin名称的包才是我们想要的下载可以直接使用的里面有编译后的二进制的包，而之前的普通的tar.gz的包里面是只是源码的包无法直接使用。

好想吐槽下啊，Zookeeper的包的变动，源码的包就不能向其他的安装包一样加个src的标识吗？见名知意多好，以避免误下载。

![](./images/images/img_003_49bfc03a01b9.png)

# 单机Zookeeper

## 创建目录及解压

![](./images/images/img_004_d467535cc1da.png)

## 进入解压目录 
![](./images/images/img_005_aa345cc3ae59.png)

## 进入conf 

![](./images/images/img_006_9deaa2957bfe.png)

## 拷贝zoo_sample.cfg(**目标文件，必须zoo.cfg**)
![](./images/images/img_007_c7ee71d6f1ea.png)

## 编译拷贝后的文件:zoo.cfg

![](./images/images/img_008_2cc7f809bfff.png)

![](./images/images/img_009_ed5e08a3535c.png)

注：修改完快照存储目录后，用:**x**

## 建立软连接

![](./images/images/img_010_ad11b0dd8d50.png)

## 环境变量配置

```text
vim /etc/profile
```

![](./images/images/img_011_7d78652ebdd9.png)

使配置生效：`source /etc/profile`

## 启动

```text
./zkServer.sh start
```

![](./images/images/img_012_cf26d0bce687.png)

## 注意

**linux需要有jdk，关闭防火墙**

# 集群Zookeeper

## 准备工作

　　克隆1台上面单机配置好的linux，用于搭建集群。

## 创建myid

　　来到刚才zoo.cfg设置的快照存储目录下，我这里是**/usr/data/zookeeper**

![](./images/images/img_013_04a93410c275.png)

## 进入安装目录

**修改conf/zoo.cfg**

![](./images/images/img_014_d354a4e9ffa8.png)*
*

## 添加所有集群中主机信息

![](./images/images/img_015_793d728e466b.png)

### 格式

```text
server.1=192.168.1.101:2888:3888
server.2=192.168.1.102:2888:3888
server.3=192.168.1.103:2888:3888

格式：
server.myid文件中的值=ip:端口号:端口号

端口号是集群数据交互的端口号，可以瞎写，但不能被占用
```

集群搭建个数，至少2个，最好奇数，这样zookeeper投票可以过半

## 重复克隆2台刚配置过集群主机信息的那台linux

　　注：**别忘记修改myid中对应的值**！！！！

![](./images/images/img_016_191fc3fe9732.png)

## 依次启动zookeeper集群

### 启动第一台

![](./images/images/img_017_228183e4cf77.png)

### 启动第二台

第二台变为了leader

![](./images/images/img_018_a1ab5b226c47.png)

我们查看刚才第一台，此时变为了

![](./images/images/img_019_e5a0dfa0ddcc.png)

### 启动第三台

![](./images/images/img_020_c951f6e3a1da.png)

## 模拟情况

### 第二台关机(模拟实际情况服务器挂了)

![](./images/images/img_021_4b604ccd3267.png)

### 查看第一台

![](./images/images/img_022_9b87aec01d0b.png)

### 查看第三台

![](./images/images/img_023_5405f095d8a9.png)

## 搞定！！！！！
