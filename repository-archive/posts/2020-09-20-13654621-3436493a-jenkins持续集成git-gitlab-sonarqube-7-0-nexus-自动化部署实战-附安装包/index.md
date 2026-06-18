{

  "title": "Jenkins持续集成git、gitlab、sonarqube(7.0)、nexus，自动化部署实战，附安装包",
  "date": "2020-09-20",
  "description": "导读 之前用的都是SVN，由于工作需要用到Git，**求人不如求己**，**技多不压身**，**多学一项技能**，**未来就少求别人一次**，系统的学一遍，自己搭建一整套环境，自动化部署(自动发版)，代码质量检测等等(**为啥不用docker搭建环境呢，个人平时比较忙，暂未学习docker，过段时间",
  "tags": [
    "Git"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/qq543210188.html"

}

# 导读

　　之前用的都是SVN，由于工作需要用到Git，**求人不如求己**，**技多不压身**，**多学一项技能**，**未来就少求别人一次**，系统的学一遍，自己搭建一整套环境，自动化部署(自动发版)，代码质量检测等等(**为啥不用docker搭建环境呢，个人平时比较忙，暂未学习docker，过段时间会学docker相关，也会写相应博文**)。为啥要打水印，Wechat上有人告诉我，之前很多博文，被某些网站白嫖，然后挂到自己网站(**未来博客上都会打水印**)，~@￥#%￥@%#@%￥再次声明，**创作不易，严禁转载！！！**

## 踩坑

　　从10月12、13(周末)天天搞到夜里2、3点，周一至周五，由于个人原因，刚换份工作，平时也忙，个人精力有限，只能晚上花2、3小时，学习-搭建-踩坑-度娘-搭建-成功，一直到今天，才完整的搭建出来，博客才发出来。安装过程中，并不是一帆风顺的，在此为了避免学习的小朋友踩相同的坑，最好版本和我一致，下面都会有提供我使用的安装包。**那些坑，我已经巧妙的绕开啦，按照我的步骤来，干就完事儿啦，欧力给~**

## 演示环境

1. mac系统
2. 虚拟机：Centos 6.5(**我分配了4G，2核，配置低了会卡！里面用到ES服务器配置低，服务起不来，ES脑补链接：[点我直达](https://www.cnblogs.com/chenyanbin/category/1811337.html)，磁盘至少分50G，当初我给了20G，最后服务配置太多以后，导致服务跑不起来了**)

# Git

## Git是什么

　　Git 是一个**开源**的**分布式版本控制**系统，用于**敏捷高效**地处理任何或小或大的**项目**。

　　Git 是 Linus Torvalds 为了帮助管理 Linux 内核开发而开发的一个开放源码的版本控制软件。

　　Git 与常用的版本控制工具 CVS, Subversion 等不同，它采用了分布式版本库的方式，不必服务器端软件支持。

## Git的安装

　　官网地址：[https://git-scm.com/downloads](https://git-scm.com/downloads)[
](https://git-scm.com/)

　　不要慌，最下面我会提供我使用的所有安装包

```text
linux：yum install -y git
mac：自带的有git
windows：需要自动手动下载,一直下一步即可
```

![](./images/images/img_001_d2d561e0089d.png)

安装git完成

![](./images/images/img_002_368ef4fa671e.png)

　　yum自动下载的git不是最新的，如果想安装最新的git版本，自行百度查，方法很多滴~由于时间关系，就不带领小伙伴实操啦，功能都大差不差的。

## 常用命令

### 帮助

```text
1、git                       查看git的帮助文档
2、git --help              查看git的帮助文档
3、git add --help        查看某个命令的帮助文档
```

![](./images/images/img_003_9addbf69f23b.png)

### 版本号

![](./images/images/img_004_512fd96751cd.png)

### 生产空的本地仓库

![](./images/images/img_005_42b0a31728fc.png)

### 将文件添加暂存区

![](./images/images/img_006_861b2b9f61f2.png)

### 提交

初次commit之前，需要配置用户邮箱及用户名

```text
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

git commit：将暂存区的文件提交到本地仓库

### 远程仓库

![](./images/images/img_007_d67f8a2726cb.gif)

```text
echo "# git-test" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/543210188/git-test.git
git push -u origin master
```

![](./images/images/img_008_330f362249dc.png)

![](./images/images/img_009_f872e9c65464.png)

### 推送

git push -u origin master：往名字为origin的仓库的master分支上提交变更

### 拉取

```text
1、git fetch       拉取远程仓库的变更到本地仓库
2、git merge origin/master    将远程的变更，合并到本地仓库的master分支

3、上面2个命令等价于 git pull
```

### 取消添加

```text
git rm --cache 1.txt
注意：如果只是：git rm --cache，仅删除暂存区里的文件
如果不加--cache，会删除工作区里的文件，并提交到暂存区
```

### 恢复文件

```text
1、git checkout master 文件名
```

注：直接加文件名，从暂存区将文件恢复到工作区，如果工作区已经有该文件，则会覆盖

加了[分支名]+文件名，表示从分支名为所写的分支名中拉取文件，并覆盖工作区里的文件

### git文件状态

```text
git status  查看git的状态
```

## git图形化客户端

官网：[https://www.sourcetreeapp.com/ ](https://www.sourcetreeapp.com/)

![](./images/images/img_010_9724e7c38e17.png)

### 拉取代码

![](./images/images/img_011_0a2c2bb4986e.gif)

![](./images/images/img_012_5ee553253e66.gif)

## 分支

　　软件项目中**启动一套单独**的**开发路线**的方法，可以**避免版本兼容**开发问题，**避免**不同**版本**之**间**的**影响**，封装一个开发阶段，解决bug的时候新建分支，用于对该bug的研究。

![](./images/images/img_013_4e316796fcf0.png)

### 创建分支&查看分支

```text
创建分支：git branch 分支名
查看分支：git branch
注：列出所有的分支，分支前面有*号，代表当前所在那个分支
```

![](./images/images/img_014_eeee4ce05661.png)

### 删除分支

```text
删除：git branch -d 分支名
注：不能删除当前所在的分支
```

![](./images/images/img_015_ade6169c7c91.png)

### 修改分支名

```text
修改分支名：git branch -m 旧分支名 新分支名
```

![](./images/images/img_016_6a9a391cf04a.png)

### 开发v2.0版本分支(切换分支并推送到github)

```text
切换分支：git checkout 分支名
注：如果在分支上面对文件进行修改之后，没有commit就切换到另外一个分支，是不允许的，必须commit之后，才能切换分支

强制切换分支：git checkout -f 分支名
注：强制切换分支，如果有未提交的变更，直接丢弃
```

![](./images/images/img_017_0fc68041059c.png)

![](./images/images/img_018_8690e8694ba4.png)

## 查看历史

```text
查看提交历史：git log
查看最近2次的提交：git log -2
查看最近2次提交差异：git log -p -2
查看某个人提交的代码：git log --author 作者
显示简要的信息：git log --oneline
整个提交历史：git log --graph
```

![](./images/images/img_019_2e4ab4606ba1.png)

## 代码对比

### 作用

1. 解决冲突
2. 制作补丁

```text
比较工作区跟暂存区的差异：git diff
比较暂存区与分支差异：git diff --cached 或者 --staged
跟当前分支比较：git diff HEAD
比较当前分支与另外一个分支差异：git diff 分支名
查看两个分支的差异(针对已提交)：git diff 分支名1 分支名2
查看单纯的一个文件差异：git diff 文件名
查看两次不同提交差异：git diff commitid_1 commitid_2
查看有变更的文件：git diff --stat
```

![](./images/images/img_020_770913b010a4.png)

## git更改提交 

### 用途

1. 将暂存区中不必要的文件移除
2. 版本回滚
3. 只修改提交的摘要信息

```text
把暂存区中的文件移除出来_1：git reset HEAD 文件名
把暂存区中的文件移除出来_2：git reset HEAD^
修改暂存区中的摘要信息(需要重新提交git commit -m "test")：git reset --soft HEAD^
丢失修改过的代码(重置代码)：git reset --hard HEAD^
```

## 分支合并冲突

```text
分支合并(拿指定的分支名与当前分支进行合并)：git merge 分支名
```

![](./images/images/img_021_6d2551deceb7.png)

![](./images/images/img_022_d7082e75f426.png)

### 冲突解决

```text
合并分支：git merge 分支名
查看冲突文件(重要)：git diff --name-only --diff-filter=U
```

**注：视情况，是只要master的代码还是v2.0(分支)代码，我这里处理是要2边的代码。 **
![](./images/images/img_023_28363b9e514d.gif)

## 标签

```text
打上标签(给最近的打上标签)：git tag 标签名
给指定的提交打上标签(git log获取commitid值，也就是获取提交的版本)：git tag 标签名 commitid
显示标签(以字母序，非时间)：git tag
显示该标签提交的那次相关信息：git show 标签名
删除标签(不会删除那次提交)：git tag -d 标签名
将标签推送到远程服务器上(标签必须存在)：git push origin 分支名 标签名
删除远程服务器上的标签：
1、删除本地的标签：git tag -d 标签名
2、删除远程的：git push origin :refs/tags/标签名
```

![](./images/images/img_024_67091512fe5b.gif)

![](./images/images/img_025_ffbf4f335988.png)

## gitignore文件 

### 用途

1.

忽略不必要的文件 

```text
1、创建gitignore文件：touch .gitignore
2、在.gitignore添加忽略的目录：
target
.idea

.log：表示忽略项目中所有以.log结尾的文件
123?.log：表示忽略项目中所有以123加任意字符的文件
/error.log：表示忽略项目中根目录中的error.log 这个文件
src/main/test/：表示忽略/src/main/test/目录下的所有文件
*.class **/java/：匹配所有java目录下的所有文件
!/error.log：表示在之前的匹配规则下，被命中的文件，可以使用!对前面的规则进行否定
```

```text
如果项目已经推送到远程服务器中，可通过这种方式删除
1、先删除本地暂存区文件(git rm -rf --cache target/)：git rm -rf --cache 目录名
2、提交：git commit -m "删除本地暂存区"
3、推送：git push
```

![](./images/images/img_026_d3a6a688c4d8.png)

![](./images/images/img_027_faa3ec0279aa.png)

# Gitlab

## 简介

　　GitLab 是一个用于仓库管理系统的开源项目，使用[Git](https://baike.baidu.com/item/Git)作为代码管理工具，并在此基础上搭建起来的web服务。安装方法是参考GitLab在GitHub上的Wiki页面。

## 为什么要使用gitlab？ 

1. 基础功能开源，可自行搭建
2. 可以进行权限控制，使代码对部分人可见

## 安装gitlab(Centos6.5)

### 目录结构及说明

```text
/etc/gitlab/gitlab.rb          #gitlab配置文件
/opt/gitlab                    #gitlab的程序安装目录
/var/opt/gitlab                #gitlab目录数据目录
/var/opt/gitlab/git-data       #存放仓库数据
gitlab-ctl reconfigure         #重新加载配置
gitlab-ctl status              #查看当前gitlab所有服务运行状态
gitlab-ctl stop                #停止gitlab服务
gitlab-ctl stop nginx          #单独停止某个服务
gitlab-ctl tail                #查看所有服务的日志

Gitlab的服务构成：
nginx：                 静态web服务器
gitlab-workhorse        轻量级反向代理服务器
logrotate              日志文件管理工具
postgresql             数据库
redis                  缓存数据库
sidekiq                用于在后台执行队列任务（异步执行）
```

### 官网

官网：[https://about.gitlab.com/](https://about.gitlab.com/)

国内镜像：[https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/](https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/)

### 在线下载及安装

```text
yum install -y curl policycoreutils-python openssh-server        #安装依赖
wget https://mirrors.tuna.tsinghua.edu.cn/gitlab-ce/yum/el6/gitlab-ce-13.1.11-ce.0.el6.x86_64.rpm --no-check-certificate  #centos6.5
rpm -ivh gitlab-ce-13.1.11-ce.0.el6.x86_64.rpm # 安装包gitlab
sudo service postfix start
sudo chkconfig postfix on
```

### linux其他版本安装方式

　　centos其他版本下载包方式，当然啦，也**可以先把包下载到本地，然后在丢到linux，执行安装效果是一样的**。

![](./images/images/img_028_8311ed55e978.png)

### 修改对外开放域名或ip

```text
vim /etc/gitlab/gitlab.rb
```

打开后有一行 external_url 的设置改成要对外开放 web 的 url ，
例如我可以指定 git.chenyanbin.com
只想內部使用也可以改成 http://192.168.199.199:8888 这样的内部IP地址.

![](./images/images/img_029_3f9d2f67647d.png)

```text
配置生效：gitlab-ctl reconfigure
重启：gitlab-ctl restart
```

```text
设置防火墙端口(防火墙已全部关闭的话，可忽略)：vim /etc/sysconfig/iptables
```

![](./images/images/img_030_c3a8313f59b5.png)

## 启动gitlab

```text
sudo gitlab-ctl reconfigure
sudo lokkit -s http -s ssh
```

```text
停止gitlab：gitlab-ctl stop
重启gitlab：gitlab-ctl start
```

## 登录

　　注：第一次登录时，需要设置初始密码，然后用root+密码登录即可

![](./images/images/img_031_e4bbdb091deb.gif)

## 创建项目并推送到gitlab

　　本地新建一个项目并用git，将文件夹推送到gitlab上。

![](./images/images/img_032_2dae024a8952.gif)

![](./images/images/img_033_fa0efaca6fdc.gif)

## 邮件服务

### 作用

1. 有合并请求时，邮件通知
2. 账号注册时，邮件验证
3. 修改密码时，通过邮件修改

### 步骤

1. 开启QQ邮箱的smtp服务
2. 修改gitlab配置
3. 测试邮件服务是否正常

![](./images/images/img_034_beaf613f4da8.gif)

```text
gitlab_rails['smtp_enable'] = true
gitlab_rails['smtp_address'] = "smtp.qq.com"
gitlab_rails['smtp_port'] = 465
gitlab_rails['smtp_user_name'] = "543210188@qq.com"
gitlab_rails['smtp_password'] = "邮箱随机字符串"
gitlab_rails['smtp_domain'] = "qq.com"
gitlab_rails['smtp_authentication'] = "login"
gitlab_rails['smtp_enable_starttls_auto'] = true
gitlab_rails['smtp_tls'] = true
user['git_user_email'] = "543210188@qq.com"
gitlab_rails['gitlab_email_from'] = '543210188@qq.com'
```

```text
重启配置文件：gitlab-ctl reconfigure
重启服务：gitlab-ctl restart
```

###  测试邮件

```text
gitlab-rails console
Notify.test_email('543210188@qq.com','邮件测试','博客地址：https://www.cnblogs.com/chenyanbin/').deliver_now
```

![](./images/images/img_035_ed8a7acdbed6.gif)

## 账号注册和分组

### 用户注册(未开启邮箱检验)

　　缺点：随便添加账户，乱注册，不符合企业管理标准

![](./images/images/img_036_04c5f08bdab2.gif)

![](./images/images/img_037_dedf20e59e37.gif)

### 用户注册(邮箱校验)

　　开启校验并真实邮箱注册

![](./images/images/img_038_617cb823bec8.gif)

![](./images/images/img_039_6af4bc5fb98b.gif)

### 创建组并邀请成员(配置过邮件服务，会邮件提醒)

#### 访问权限

1. private：只有组成员才能看到
2. Internal：只要登录的用户就能看到
3. Public：所有人都能看到

#### 组权限

1. Guest：可以创建issue、发表评论，不能读写版本库
2. Reporter：可以克隆代码，不能提交
3. Developer(**推荐**)：可以克隆代码、开发、提交、push
4. Master：可以创建项目、添加tag、保护分支、添加项目成员、编辑项目
5. Owner：可以设置项目访问权限 - Visibility Level、删除项目、迁移项目、管理组成员

![](./images/images/img_040_93d2252af321.gif)

![](./images/images/img_041_9b5b3982e946.gif)

生成随机密钥

```text
ssh-keygen -t rsa
```

![](./images/images/img_042_fa89080b1bc2.gif)

## 分支及标签保护

### 为什么要保护分支？

　　保护特定的分支不被随便合并，以免影响相应的分支

![](./images/images/img_043_078398f621f6.gif)

![](./images/images/img_044_cb0110020e38.gif)

![](./images/images/img_045_f12f091dc837.png)

![](./images/images/img_046_00bb4a6d193c.png)

　　自己部署好gitlab，然后赋予账户权限，体验下就好

注：能push就能merge，相应的权限自我控制(master分支设置只能master可以合并)。 

第二种方式合并请求

![](./images/images/img_047_1528395b92f8.gif)

![](./images/images/img_048_a9ff19a1306f.gif)

# 敏捷持续集成

## 简介

　　持续集成是一种软件开发实践，即团队开发成员经常集成他们的工作，通过每个成员每天至少集成一次，也就意味着每天可能会发生多次集成。每次集成都通过自动化的构建（包括编译，发布，自动化测试）来验证，从而尽早地发现集成错误。

## 好处

1. 节省人力成本
2. 加快软件开发进度
3. 实时交付

## 重要组件

1. git
2. gitlab
3. Jenkins：持续集成引擎
4. maven：构建
5. sonarqube：代码质量管理
6. JDK
7. Tomcat

## jdk和maven安装

jdk安装：[点我直达](https://www.cnblogs.com/chenyanbin/p/12843149.html)

maven安装：[点我直达](https://www.cnblogs.com/chenyanbin/p/13662849.html)

## nexus私服安装

官网：[点我直达](https://www.sonatype.com/nexus/repository-oss/download)

　　下面百度云盘也会提供哟~

![](./images/images/img_049_6830be097406.png)

### 解压

```text
tar -zxvf nexus-3.27.0-03-unix.tar.gz -C /usr/local
```

### 修改启动端口号

```text
vim /usr/local/nexus-3.27.0-03/etc/nexus-default.properties
```

![](./images/images/img_050_69580d4c8ecc.png)

### 开启防火墙端口

　　注：因为我本地没有使用8081端口，所以默认端口可以使用。但是防火墙端口记得开放哟~ 

```text
vim /etc/sysconfig/iptables
```

![](./images/images/img_051_e9da535c8e48.png)

### 重启防火墙

```text
service iptables restart
```

### 启动nexus

**注意：jdk版本必须得1.8！！！nexus版本不同，可能需要的jdk版本不同**

![](./images/images/img_052_ee69aa5830a9.png)

```text
nexus不推荐使用root用户启动(可忽略)

也可以自己手动创建个用户，然后加入到组，赋予权限，步骤如下
1、useradd nexus
2、chown -R nexus:nexus xxxx/xxxx/nexus-3.27xxx/
3、chown -R nexus:nexus xxxx/xxxx/sonatype-work/
4、su nexus
5、./nexus start
```

#### 踩了个坑

![](./images/images/img_053_8f965a9b1739.png)

#### 小技巧

**注：./nexus start，启动完成之后，查看nexus是否启动：ps aux|grep nexus，若没有启动的话，可以使用：./nexus run；此时启动项目就会提示哪里出错啦~**

### 访问

![](./images/images/img_054_a3df5182f3b8.gif)

**注：点击右上角登录，默认账号密码：admin/admin123；从nexus3.17以后，默认密码改为随机的了，文件路径在：/usr/local/sonatype-work/nexus3/admin.password里！！！**

![](./images/images/img_055_2e302b2cfcc3.png)

#### 修改最大文件数(默认1024)

![](./images/images/img_056_fa6419fecb4e.png)

![](./images/images/img_057_05211bebed85.png)

**注：记得重启！！！**

#### 设置nexus开机自启动

```text
 vim /etc/rc.d/rc.local
```

![](./images/images/img_058_536a75b027e4.png)

## nexus安装及使用

### 项目maven大概过程分析

![](./images/images/img_059_d4024351c4f3.png)

### 设置maven的setting.xml

```text
<?xml version="1.0" encoding="UTF-8"?>
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
    <pluginGroups/>
    <proxies/>
    <servers>
        <server>
            <id>ybchen-releases</id>
            <username>admin</username>
            <password>admin</password>
        </server>
        <server>
            <id>ybchen-snapshots</id>
            <username>admin</username>
            <password>admin</password>
        </server>
    </servers>
    <mirrors/>
    <profiles>
        <profile>
            <id>ybchen</id>
            <activation>
                <activeByDefault>false</activeByDefault>
            </activation> <!-- 私有库地址-->
            <repositories>
                <repository>
                    <id>ybchen</id>
                    <url>http://192.168.199.199:8088/repository/maven-public/</url>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                    <snapshots>
                        <enabled>true</enabled>
                    </snapshots>
                </repository>
            </repositories> <!--插件库地址-->
            <pluginRepositories>
                <pluginRepository>
                    <id>ybchen</id>
                    <url>http://192.168.199.199:8088/repository/maven-public/</url>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                    <snapshots>
                        <enabled>true</enabled>
                    </snapshots>
                </pluginRepository>
            </pluginRepositories>
        </profile>
    </profiles>
    <activeProfiles>
        <activeProfile>ybchen</activeProfile>
    </activeProfiles>
</settings>
```

### 设置nexus的代理地址，并添加到组中

　　阿里云地址：http://maven.aliyun.com/nexus/content/groups/public/ 

![](./images/images/img_060_297fd63bc549.gif)

### 测试

　　本地库，我已经清空，所有下载的都会先去nexus看看，没有的话，才会走阿里云代理上下载，然后还会下载到nexus。  
![](./images/images/img_061_43210816c50d.gif)

### 将本地jar上传至nexus

![](./images/images/img_062_f7b8241c55a9.png)

![](./images/images/img_063_daa276c37b78.gif)

```text
<distributionManagement>
    <repository>
        <id>ybchen-releases</id>
        <name>Nexus Release Repository</name>
        <url>http://xxx.xxx.xxx.xxx:port/repository/maven-releases/</url>
    </repository>
    <snapshotRepository>
        <id>ybchen-releases</id>
        <name>Nexus Release Repository</name>
        <url>http://xxxx.xxxx.xxx.xxx:port/repository/maven-snapshots/</url>
    </snapshotRepository>
</distributionManagement>
```

## 安装mysql

[点我直达](https://www.cnblogs.com/chenyanbin/p/13144042.html)

## 代码质量管理平台sonarQube安装及使用

### 前置条件

- mysql 5.6 | 5.7
- jdk1.8

 我使用的是7.0，版本要求：[点我直达](https://docs.sonarqube.org/7.0/Requirements.html)[
](https://docs.sonarqube.org/7.9/requirements/requirements/)

![](./images/images/img_064_d60333d581e4.gif)

下载地址：[点我直达](https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-7.0.zip)

### 官网

[点我直达](https://www.sonarqube.org/)

### 安装

```text
1、依赖：yum install unzip -y
2、解压：unzip sonarqube-7.0.zip
3、移动：mv sonarqube-7.0 /usr/local/
4、切换： cd /usr/local/
5、登录mysql：mysql -u root -p
6、创建库：CREATE DATABASE sonar DEFAULT CHARACTER SET utf8;
7、退出mysql：exit
8、进入sonarqube：cd sonarqube-7.0/conf/
```

### 修改配置

```text
vim sonar.properties
```

```text
主要配置以下内容
sonar.jdbc.username=root
sonar.jdbc.password=root
sonar.jdbc.url=jdbc:mysql://localhost:3306/sonar?useUnicode=true&characterEncoding=utf8&rewriteBatchedStatements=true&useConfigs=maxPerformance&useSSL=false
sonar.web.host=0.0.0.0
sonar.web.context=/sonar
sonar.web.port=9000
```

### 启动

```text
useradd sonar
chown -R sonar:sonar /usr/local/sonarqube-7.0
su sonar
cd /usr/local/sonarqube-7.0/bin/linux-x86-64/
./sonar.sh start
```

### 访问

**记得开放防火墙端口：9000，账号/密码：admin/admin**

![](./images/images/img_065_4bac94fa3dc5.gif)

### 汉化

![](./images/images/img_066_048f41494399.gif)

　　安装完，重启服务再次打开网页即可

```text
sonar7.0的中文包，网页在线安装不上，我是去github上下载，手动安装的，按照以下几步即可，下面我也会提供，我直接下载的是jar包，源码包还得编码(因为我懒)
1. 在https://github.com/SonarCommunity/sonar-l10n-zh，下载汉化包源码；
2. 本地打包，cmd里面，在解压包里面运行： mvn install
3. 将打好的jar包，放到： sonarqube/extensions/plugins  目录先；
4. 重启sonar，即可
```

　　具体操作如下，github地址：[点我直达](https://github.com/SonarQubeCommunity/sonar-l10n-zh)

![](./images/images/img_067_04c8d707f21e.gif)

![](./images/images/img_068_950757c06e28.gif)

### 使用

```text
settings.xml
============================
<?xml version="1.0" encoding="UTF-8"?>
<settings
    xmlns="http://maven.apache.org/SETTINGS/1.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 http://maven.apache.org/xsd/settings-1.0.0.xsd">
    <pluginGroups></pluginGroups>
    <proxies></proxies>
    <servers></servers>
    <mirrors>
        <!--maven代理开始-->
        <mirror>
            <id>huaweicloud</id>
            <mirrorOf>*,!HuaweiCloudSDK</mirrorOf>
            <url>https://mirrors.huaweicloud.com/repository/maven/</url>
        </mirror>
        <mirror>
            <id>aliyun</id>
            <name>aliyun Maven</name>
            <mirrorOf>*,!HuaweiCloudSDK</mirrorOf>
            <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
        </mirror>
        <!--maven代理结束-->
    </mirrors>
    <profiles>
        <!--sonar配置开始-->
        <profile>
            <id>sonar</id>
            <activation>
                <activeByDefault>true</activeByDefault>
            </activation>
            <properties>
                <sonar.jdbc.url>jdbc:mysql://192.168.199.199:3306/sonar?useUnicode=true&amp;characterEncoding=utf8</sonar.jdbc.url>
                <sonar.jdbc.username>root</sonar.jdbc.username>
                <sonar.jdbc.password>root</sonar.jdbc.password>
                <sonar.host.url>http://192.168.199.199:9000/sonar</sonar.host.url>
            </properties>
        </profile>
        <!--sonar配置结束-->
    </profiles>
</settings>
```

```text
git init
mvn clean install
mvn sonar:sonar
```

![](./images/images/img_069_a2ae73db0cb1.gif)

![](./images/images/img_070_dfddab6db51c.gif)

```text
忽略某一条规则，pom.xml下面追加

<properties>
    <sonar.exclusions>
        src/main/java/com/.../domain/model/**/*,
        src/main/java/com/.../exchange/**/*
</sonar.exclusions>
</properties>
```

## Jenkins

### 安装

前置条件

1. JDK(jdk8)；安装：[点我直达](https://www.cnblogs.com/chenyanbin/p/12843149.html)
2. tomcat(tomcat9)；安装：[点我直达](https://www.cnblogs.com/chenyanbin/p/12548645.html)

jenkins下载：[点我直达](https://www.jenkins.io/download/)

![](./images/images/img_071_ed84d70ac80d.png)

将jenkins放到tomcat中

![](./images/images/img_072_c5e85bd479fa.png)

### 问题排查(重要)

1. 查看tomcat是否启动
2. 查看端口8080是否开启：netstat -tlun
3. 查看防火墙端口是否开启，记得重启防火墙
4. 查看tomcat日志：/var/soft/apache-tomcat-9.0.38/logs/catalina.out

![](./images/images/img_073_376fd13fd892.png)

**注：可以看到，地址被占用了！**

修改tomcat的端口号，我这里修改为：9999，记得防火墙！！！

![](./images/images/img_074_47195999a51b.png)

### 访问

![](./images/images/img_075_42a686b3a149.png)

![](./images/images/img_076_12000a87a0e6.png)

### 安装推荐组件

![](./images/images/img_077_e09b1deccd93.gif)

![](./images/images/img_078_fcb8b8621d10.gif)

### 创建用户名密码

![](./images/images/img_079_e0c41c1000ba.png)

### 实例配置

![](./images/images/img_080_d41cd9604db3.png)

### 登录

![](./images/images/img_081_92868d441b00.gif)

### 插件安装及配置

![](./images/images/img_082_aa4794e89e3f.gif)

![](./images/images/img_083_fe41b308da0e.gif)

![](./images/images/img_084_2f150512a7b2.gif)

#### 系统配置

1. jdk
2. maven
3. sonarqube
4. 邮件
5. gitlab授权
6. 免密登录

##### 配置jdk和maven

![](./images/images/img_085_4a30d6243a25.gif)

##### 配置邮件

![](./images/images/img_086_79456b427eab.gif)

##### 配置sonarqube

![](./images/images/img_087_d9e369ab11c8.gif)

继续到全局配置里设置sonarqube

![](./images/images/img_088_eb2166da4f0e.gif)

##### 授权登录

![](./images/images/img_089_4a23ae11b382.gif)

##### 生成密钥

```text
yum -y install openssh-clients
ssh-keygen -t rsa
```

![](./images/images/img_090_5980458eb0c6.png)

生成的key放到gitlab

```text
more ~/.ssh/id_rsa.pub
```

![](./images/images/img_091_102b1ee4c228.gif)

### 创建项目

![](./images/images/img_092_88d08458bd07.gif)

　　注：git方式拉代码，直接不报红，代表搭建成功

### jenkins手动发版测试

```text
linux创建目录
1、cd /
2、mkdir springboot_demo
```

jenkins配置

```text
clean install

mv target/*.jar /springboot_demo/
cd /springboot_demo
BUILD_ID= java -jar spring-boot-demo-0.0.1-SNAPSHOT.jar >log 2>&1 &
```

```text
clean install

mv target/*.jar /springboot_demo/
cd /springboot_demo
BUILD_ID= java -jar spring-boot-demo-0.0.1-SNAPSHOT.jar >log 2>&1 &
```

![](./images/images/img_093_825f0dd713f3.gif)

![](./images/images/img_094_f323703baf39.gif)

![](./images/images/img_095_006a093fa61e.gif)

## 整合sonar然后发布

　　刚开始的时候sonarqube里面没有项目随着代码的重新发布，会将项目也提交到sonarqube中

```text
#projectKey项目的唯一标识，不能重复
sonar.projectKey=yb
sonar.projectName=springboot-test
sonar.projectVersion=1.0
sonar.sourceEncoding=UTF-8
sonar.modules=java-module
# Java module
java-module.sonar.projectName=test
java-module.sonar.language=java
# .表示projectBaseDir指定的目录
java-module.sonar.sources=src
java-module.sonar.projectBaseDir=.
java-module.sonar.java.binaries=target/
```

![](./images/images/img_096_7b3f5da302a1.gif)

![](./images/images/img_097_335db8447fc5.gif)

![](./images/images/img_098_eeec20d1fa10.gif)

## 提交后自动发布

### 功能描述

　　本地代码修改完成之后，往gitlab上推代码，然后Jenkins自动打包发版程序，不用人工手动发版。

### 安装插件(gitlab)

![](./images/images/img_099_5190b6bd5ef6.gif)

**装完插件后，虚拟机上的磁盘满了，导致服务起不来，今天先到这吧，不搞这玩意了(明天要搞其他东西，搭建这一整套东西，恶心我几百回了，处处坑~)，自行去找度娘吧，只需要简单配置2步就好，前面服务都全部搭建出来了，这个因为linux磁盘满了，懒得搞了，有点小遗憾，拜~**

![](./images/images/img_100_a78d984d375e.png)

# 安装包

![](./images/images/img_101_98339b9369a2.png)

```text
链接: https://pan.baidu.com/s/1OixJ3oHvjEjKLtvuvplclA  密码: fbqs
```
