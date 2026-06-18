{

  "title": "Docker 实战",
  "date": "2021-01-12",
  "description": "Docker入门 概述 Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。 容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。 Docker 从 17",
  "tags": [
    "Docker"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/docker.html"

}

# Docker入门

## 概述

　　Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。

　　容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

　　Docker 从 17.03 版本之后分为 **CE**（Community Edition: 社区版） 和 **EE**（Enterprise Edition: 企业版），我们用社区版就可以了。

## 注意事项

- Linux内核版本必须大于：**3.8.+**
- 查看内核版本：uname -r

![](./images/images/img_001_e1c28f1afa74.gif)

## Docker下载及安装

```text
1、关闭防火墙
systemctl stop firewalld.service

2、修改为SELINUX=disabled
vim /etc/selinux/config
SELINUX=disabled

3、安装wget
 yum -y install wget

4、查看docker版本
yum list|grep docker

5、安装docker
yum install -y docker.x86_64

6、安装docker ce社区版
cd /etc/yum.repos.d/
wget http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo

7、下载社区版本
yum -y install docker-ce-cli.x86_64

8、设置开机启动
systemctl enable docker

9、更新xfsprogs
yum update xfsprogs

10、启动docker服务
systemctl start docker

11、查看docker版本
docker version

12、查看docker详细信息
docker info
```

![](./images/images/img_002_0720c039af5c.png)

## Docker镜像的搜索及查看删除

### 查看本地镜像

```text
docker images
```

### 搜索镜像

```text
docker search centos

docker search 名字
```

![](./images/images/img_003_4f947d560bce.gif)

### 搜索镜像并过滤是官方的

```text
docker search --filter "is-official=true" centos
```

![](./images/images/img_004_df5e56fc29a1.gif)

### 搜索镜像并过滤大于多少颗星星的

```text
docker search --filter stars=10 centos
```

![](./images/images/img_005_0a8b39560ef3.gif)

### 下载Centos7镜像

```text
docker pull centos:7

docker pull 项目:版本号
```

![](./images/images/img_006_7838a991ec9c.gif)

### 修改本地镜像名字(小写)

```text
docker tag centos:7 mycentos:1
```

### 本地镜像的删除

```text
方式一
docker rmi centos:7

方式二
docker rmi IMAGE ID
```

## 配置阿里云镜像加速

![](./images/images/img_007_7b6fcc8d6933.gif)

## Docker基本操作

### 构建容器

- -i：表示以交互模式运行容器(让容器的标准输入保持打开)
- -d：表示后台运行容器，并返回容器id
- -t：为容器重新分配一个伪输入终端
- --name：为容器指定名称

![](./images/images/img_008_3fb7ab8a5508.gif)

```text
docker run -itd --name=mycontos centos:7
```

### 查看本地所有的容器

```text
docker ps -a
```

![](./images/images/img_009_2d16dbd26b07.png)

### 查看本地正在运行的容器

```text
docker ps
```

![](./images/images/img_010_2809f01fe6d8.png)

### 停止容器

```text
方式一
docker stop NAMES

方式二
docker stop CONTAINER ID
```

![](./images/images/img_011_36f649041d8f.gif)

### 一次性停止所有容器

```text
docker stop $(docker ps -a -q)
```

![](./images/images/img_012_a5202d06a427.gif)

### 一次性全部启动

```text
docker ps -a -q
docker start $(docker ps -a -q)
```

![](./images/images/img_013_499629576a01.gif)

### 启动容器

```text
docker start CONTAINER_ID / CONTAINER_NAME
```

### 重启容器

```text
docker restart CONTAINER_ID / CONTAINER_NAME
```

![](./images/images/img_014_e9aa552e0298.gif)

### 删除容器

```text
docker rm CONTAINER_ID / CONTAINER_NAME
```

必须先停止，才能删除

![](./images/images/img_015_4fdfcdf31b6d.gif)

### 强制删除镜像

```text
docker rm -f CONTAINER_ID / CONTAINER_NAME
```

![](./images/images/img_016_108cec70e3ee.gif)

### 查看容器详细信息

```text
docker inspect CONTAINER_ID / CONTAINER_NAME
```

![](./images/images/img_017_6cb4d91bb9b9.gif)

### 进入容器

```text
docker exec -it 0ad5d7b2c3a4 /bin/bash
```

![](./images/images/img_018_d0da06eabb2a.gif)

退出容器

```text
exit
```

## 容器的文件复制于挂载

### 从宿主机复制到容器

```text
docker cp 宿主机本地路径 容器名称:容器路径
```

![](./images/images/img_019_1b816086fb4c.gif)

### 从容器复制到宿主机

```text
docker cp 容器名称:容器路径 宿主机本地路径
```

　　这个就不演示了，操作跟上面👆那个相反。

### 宿主机文件挂载到容器里(重要)

```text
docker run -itd -v --name=mycentos77 /root/cyb/:/home centos:7
```

　　可以将mysql存储文件路径，挂载到容器里

![](./images/images/img_020_cf1730190ee5.gif)

# Docker自定义镜像

## 制作镜像方式

- 基于Docker Commit制作镜像
- 基于dockerfile制作镜像，Dockerfile方式为主流的制作镜像方式

## Commit构建自定义镜像

```text
方式一
docker commit 9bdb420d8ea0  mycentos:v1

语法：docker commit CONTAINER ID PEPOSITORY:TAG

方式二
docker commit -a "chenyanbin" -m "mkdir /home/chenyanbin" 9bdb420d8ea0  mycentos:v2

    -a：标注作者
    -m：说明解释

查看详细信息
docker inspect CONTAINER ID

查看本地镜像
docker images
```

![](./images/images/img_021_1cfe696ca1a5.png)

## dockerfile构建自定义镜像 

![](./images/images/img_022_bab08c301ddf.gif)

```text
vi dockerfile

FROM centos:7
MAINTAINER ybchen 543210188@qq.com
RUN echo "正在构建镜像！！！"
WORKDIR /home/chenyanbin
COPY 123.txt /home/chenyanbin
RUN yum install -y net-tools

构建：docker build -t mycentos:v1 .

查看：docker images

启动：docker run -itd mycentos:v1

进入镜像：docker exec -it mycentos:v1 /bin/bash
```

### FROM

**基于那个镜像**

### MAINTAINER

**注明作者**

### COPY

**复制**文件进行镜像(**只能用作相对路径，不能用绝对路径**)

### ADD

**复制**文件进入镜像(**如果是.tar.gz文件会解压**)

### WORKDIR

**指定工作目录**，假如路径不存在会创建路径

### ENV

**设置环境变量**

### EXPOSE

**暴露容器端口**

### RUN

　　在**构件镜像的时候执行**，作用于镜像层面

### ENTRYPOINT

　　在容器启动的时候执行，作用于容器层，dockerfile里有多条时**只允许执行最后一条**

### CMD

　　在容器启动的时候执行，作用于容器层，dockerfile里有多条时**只允许执行最后一条**

　　容器启动后执行默认的命令或参数，允许被修改

命令格式

　　sheel命令格式：RUN yum install -y net-tools

　　exec命令格式：RUN ["yum","install","-y","net-tools"]

# Dockerfile实战

## 构建jdk8

### 在宿主机中执行如下命令

```text
1、解压
tar -xf jdk-8u261-linux-x64.tar.gz

2、移动
mv jdk1.8.0_261 /usr/local/jdk

3、打开：/etc/profile
vi /etc/profile

4、在最下面追加如下命令
export JAVA_HOME=/usr/local/jdk
export JRE_HOME=$JAVA_HOME/jre
export CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
export PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH

5、让配置文件生效
source /etc/profile
```

### 编辑dockerfile

```text
1、jdk包必须放到/root的文件夹下

2、编辑dockerfile
vi dockerfile

FROM centos:7
ADD jdk-8u261-linux-x64.tar.gz /usr/local
RUN mv /usr/local/jdk1.8.0_261 /usr/local/jdk
ENV JAVA_HOME=/usr/local/jdk
ENV JRE_HOME=$JAVA_HOME/jre
ENV CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
ENV PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH

3、构建dockerfile
docker build -t mycentos:jdk .

4、启动
docker run -itd mycentos:jdk

5、进入容器
docker exec -it xxx /bin/bash
```

![](./images/images/img_023_052663996f23.gif)

![](./images/images/img_024_8f900a89c634.gif)
![](./images/images/img_025_961ddebeb323.gif)

```text
FROM centos:7
ADD jdk-8u211-linux-x64.tar.gz /usr/local
RUN mv /usr/local/jdk1.8.0_211 /usr/local/jdk
ENV JAVA_HOME=/usr/local/jdk
ENV JRE_HOME=$JAVA_HOME/jre
ENV CLASSPATH=$JAVA_HOME/lib:$JRE_HOME/lib:$CLASSPATH
ENV PATH=$JAVA_HOME/bin:$JRE_HOME/bin:$PATH
ADD apache-tomcat-8.5.35.tar.gz /usr/local
RUN mv /usr/local/apache-tomcat-8.5.35 /usr/local/tomcat
EXPOSE 8080
ENTRYPOINT ["/usr/local/tomcat/bin/catalina.sh","run"]

启动容器
docker run -itd -p 80:8080 -v /root/test/ROOT:/usr/local/tomcat/webapps/ROOT mycentos:jdk /bin/bash
```

View Code

## 构建nginx

```text
1、dockerfile
FROM centos:7
ADD nginx-1.18.0.tar.gz /usr/local
COPY nginx_install.sh /usr/local
RUN sh /usr/local/nginx_install.sh
EXPOSE 80

2、sheel脚本，vi nginx_install.sh
#!/bin/bash
yum install -y gcc gcc-c++ make pcre pcre-devel zlib zlib-devel
cd /usr/local/nginx-1.18.0
./configure --prefix=/usr/local/nginx && make && make install

3、构建dockerfile
docker build -t mycentos:nginx .

4、启动，-p 宿主port:容器port
# -p 映射端口
docker run -itd -p 80:80 mycentos:nginx /usr/local/nginx/sbin/nginx -g "daemon off;"

5、进入容器
docker exec -it xxx /bin/bash

6、查看防火墙
firewall-cmd --state

7、停止防火墙
systemctl stop firewalld.service

8、禁止防火墙开机启动
systemctl disable firewalld.service

9、开启防火墙
systemctl start firewalld.service
```

注：如果访问不到，查看防火墙是否开启

![](./images/images/img_026_162ff23d3c46.gif)

![](./images/images/img_027_9fedb6528b68.gif)

## 构建Redis

```text
1、编辑：vi redis_install.sh
#!/bin/bash
yum install -y gcc gcc-c++ make openssl openssl-devel
cd /home/redis-4.0.11
make && make PREFIX=/usr/local/redis install
mkdir -p /usr/local/redis/conf/
cp /home/redis-4.0.11/redis.conf /usr/local/redis/conf/
sed -i '69s/127.0.0.1/0.0.0.0/' /usr/local/redis/conf/redis.conf
sed -i '88s/protected-mode yes/protected-mode no/' /usr/local/redis/conf/redis.conf

2、编写dockerfile
FROM centos:7
ADD redis-4.0.11.tar.gz /home
COPY redis_install.sh /home
RUN sh /home/redis_install.sh
ENTRYPOINT /usr/local/redis/bin/redis-server /usr/local/redis/conf/redis.conf

3、构建容器：
docker build -t mycentos:redis .

4、启动容器： #6380是宿主机端口，6379是容器的端口
docker run -itd -p 6380:6379 mycentos:redis

5、进入容器
docker exec -it xxx /bin/bash

6、测试redis
/usr/local/redis/bin/redis-cli
```

![](./images/images/img_028_34a02fd15e2c.gif)

![](./images/images/img_029_77855c5d4828.gif)

## 构建Mysql

### 方式一

```text
1、docker 拉取mysql5.7
docker pull mysql:5.7

2、官网地址
https://hub.docker.com/

3、启动mysql
docker run --name some-mysql -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root -d mysql:5.7

4、进入容器
docker exec -it some-mysql env LANG=C.UTF-8 /bin/bash

5、进入mysql
mysql -uroot -proot

6、创库
create database `db_student`;

7、进入库
use db_student;

8、建表
drop table if exists `user`;
CREATE TABLE user (
id tinyint(5) zerofill auto_increment not null comment '学生学号',
name varchar(20) default null comment '学生姓名',
age tinyint default null comment '学生年龄',
class varchar(20) default null comment '学生班级',
sex char(5) not null comment '学生性别',
unique key (id) ) engine=innodb charset=utf8;

9、插入几条记录
insert into user values('1','小明','15','初三','男');
insert into user values('2','小红','13','初二','女');
```

![](./images/images/img_030_61a9bd38b1b8.png)

![](./images/images/img_031_5c894a7ff2a9.gif)

![](./images/images/img_032_41ceba45c3e4.gif)

### 方式二

```text
1、编辑：init.sql
vi init.sql

create database `db_student`;
use db_student;
drop table if exists `user`;
CREATE TABLE user (
id tinyint(5) zerofill auto_increment not null comment '学生学号',
name varchar(20) default null comment '学生姓名',
age tinyint default null comment '学生年龄',
class varchar(20) default null comment '学生班级',
sex char(5) not null comment '学生性别',
unique key (id) ) engine=innodb charset=utf8;
insert into user values('1','小明','15','初三','男');

2、编写dockerfile
vi dockerfile

FROM mysql:5.7
WORKDIR /docker-entrypoint-initdb.d
ENV LANG=C.UTF-8
ADD init.sql .

3、构建镜像
docker build -t my-mysql:5.7 .

3、启动mysql
docker run --name some-mysql -p 3307:3306 -e MYSQL_ROOT_PASSWORD=root -d my-mysql:5.7

4、进入容器
docker exec -it some-mysql env LANG=C.UTF-8 /bin/bash

5、进入mysql
mysql -uroot -proot

6、切换库
use db_student;

7、查看
select * from user;
```
