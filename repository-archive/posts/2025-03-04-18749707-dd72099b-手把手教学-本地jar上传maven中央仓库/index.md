{

  "title": "手把手教学 本地jar上传maven中央仓库🚀🚀🚀",
  "date": "2025-03-04",
  "description": "准备工作 注册账号 官网地址：https://central.sonatype.com/ 注册命名空间 刚才注册好的账号，登录系统 验证namespace 创建推送的账号密码 复制内容如下 把内容粘贴到maven的配置文件settings.xml中,${server}可以自定义。 GPG验证配置（这",
  "tags": [
    "Java",
    "Maven"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/18749707/mvnrepository"

}

# 准备工作

## 注册账号

官网地址：[https://central.sonatype.com/](https://central.sonatype.com/)

![](./images/images/img_001_1412464d16f6.png)

## 注册命名空间

　　刚才注册好的账号，登录系统

![](./images/images/img_002_b0d69ed0e141.gif)

![](./images/images/img_003_10019d63297d.png)

### 验证namespace

![](./images/images/img_004_01cbbeb50858.png)

## 创建推送的账号密码

![](./images/images/img_005_3b13f96a526d.png)

复制内容如下

```text
<server>
  <id>${server}</id>
  <username>xxxxxx</username>
  <password>xxxxxx</password>
</server>
```

把内容粘贴到maven的配置文件settings.xml中,${server}可以自定义。

![](./images/images/img_006_4aee470560ad.png)

## **GPG验证配置（这步很重要）**

　　GPG，全称为GNU Privacy Guard，是一个开源的加密软件，基于OpenPGP标准（RFC 4880）。它可以用于加密和解密数据、签名和验证数据，以及管理加密密钥。

下载地址：[https://gnupg.org/download/index.html](https://gnupg.org/download/index.html%20)

![](./images/images/img_007_31c05e2c702e.png)

### 生成密钥

```text
gpg --gen-key
```

根据提示输入真实姓名、邮箱(与git仓库邮箱一致),回车生成秘钥,此处会弹出弹框需要输入秘钥密码(**后续上传jar会使用到**)。

![](./images/images/img_008_64c55776f0a4.png)

### **发布gpg秘钥**

　　使用gpg命令上传秘钥到maven中央仓库,这样仓库持有了你的秘钥才能验证你的身份:

```text
gpg --keyserver keyserver.ubuntu.com --send-keys xxxxxx
```

![](./images/images/img_009_e56a3f8a7850.png)

### **验证gpg秘钥（重要）**

** **能查到就代表密钥发布成功了

![](./images/images/img_010_cf5ac01b898d.png)

# 上传jar & 发布

### 添加依赖

```text
    <url>https://github.com/chenyanbin188/ybchen-super-cache-annotation</url>
    <description>Super cache annotation</description>

<licenses>
        <license>
            <name>The Apache Software License, Version 2.0</name>
            <url>http://www.apache.org/licenses/LICENSE-2.0.txt</url>
        </license>
    </licenses>
    <developers>
        <developer>
            <id>chenyanbin</id>
            <name>chenyanbin</name>
            <email>543210188@qq.com</email>
            <roles>
                <role>Architect</role>
            </roles>
        </developer>
    </developers>
    <scm>
        <connection>https://github.com/chenyanbin188/ybchen-super-cache-annotation.git</connection>
        <developerConnection>https://github.com/chenyanbin188/ybchen-super-cache-annotation.git</developerConnection>
        <url>https://github.com/chenyanbin188/ybchen-super-cache-annotation</url>
    </scm>

    <build>
        <plugins>
            <plugin>
                <groupId>org.sonatype.central</groupId>
                <artifactId>central-publishing-maven-plugin</artifactId>
                <version>0.4.0</version>
                <extensions>true</extensions>
                <configuration>
                    <publishingServerId>chenyanbin</publishingServerId>
                    <tokenAuth>true</tokenAuth>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-source-plugin</artifactId>
                <version>2.2</version>
                <executions>
                    <execution>
                        <id>attach-sources</id>
                        <goals>
                            <goal>jar-no-fork</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.2</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-javadoc-plugin</artifactId>
                <version>2.9</version>
                <executions>
                    <execution>
                        <id>attach-javadocs</id>
                        <goals>
                            <goal>jar</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-gpg-plugin</artifactId>
                <version>1.6</version>
                <configuration>
                    <executable>/usr/local/bin/gpg</executable>
                    <keyname>chenyanbin</keyname>
                </configuration>
                <executions>
                    <execution>
                        <id>sign-artifacts</id>
                        <phase>verify</phase>
                        <goals>
                            <goal>sign</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
```

## 推送

![](./images/images/img_011_f2677eb6112c.png)

![](./images/images/img_012_50fd64f3d91f.png)

# 查看发布成功的jar

![](./images/images/img_013_407277736747.png)

# 踩坑

坑一：创建完namespace之后，发布的jar的包路径，两者要保持一致！！！

坑二：创建完namespace之后，不支持删除
