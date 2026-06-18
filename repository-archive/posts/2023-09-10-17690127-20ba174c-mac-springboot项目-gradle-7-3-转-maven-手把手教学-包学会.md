{

  "title": "Mac SpringBoot项目 Gradle 7.3 转 Maven 手把手教学，包学会~",
  "date": "2023-09-10",
  "description": "导读 最近我手上有个使用Gradle构建的项目，国内使用Gradle的人相对较少。而且我也觉得Gradle的依赖管理方式有些复杂，让我感到有些困惑。因此，我想将项目转换为Maven构建方式。Maven构建的SpringBoot的方式，想必大家都不陌生了吧~我特地记录下来，以备将来可能还会用到。 这里",
  "tags": [
    "Spring Boot",
    "Spring",
    "Mac"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/gradle.html"

}

# 导读

　　最近我手上有个使用Gradle构建的项目，国内使用Gradle的人相对较少。而且我也觉得Gradle的依赖管理方式有些复杂，让我感到有些困惑。因此，我想将项目转换为Maven构建方式。Maven构建的SpringBoot的方式，想必大家都不陌生了吧~我特地记录下来，以备将来可能还会用到。

　　这里为了演示方便，我快速创建一个SpringBoot用Gradle构建的项目，将他改成Maven方式构建项目~~~~~

# 本地安装Gradle

## 下载地址

[https://gradle.org/releases/](https://gradle.org/releases/)

```text
https://downloads.gradle.org/distributions/gradle-7.3-all.zip
```

　　注：我下载的是7.3！！！ 

![](images/img_001_27c112b4ce1d.gif)

## 配置环境变量

```text
# 修改环境变量
vi ~/.bash_profile

# 添加如下配置
export GRADLE_HOME="/Users/chenyanbin/plus/gradle-7.3"
export PATH="$PATH:$GRADLE_HOME/bin"
export PATH="$PATH:/Users/chenyanbin/plus/gradle-7.3/bin"

# 让配置立即生效
source ~/.bash_profile

# 查看gradle版本
gradle -v
```

![](images/img_002_c9a1ebd90880.gif)

# 新建SpringBoot Gradle构建的项目

![](images/img_003_31a20713eb04.png)

## Idea配置gradle

![](images/img_004_46095348d220.png)

## Gradle 转 Maven 

　　注意：Gradle 版本不一样，添加Maven插件方式不一样，我使用的是Gradle 7.3，这个项目我就引入的SpringBoot web依赖和lombok，下面开始Gradle转Maven

## 操作步骤

1. 将生成的build中的pom-default.xml 拷贝出去，并重命名pom.xml
2. 删除之前项目跟gradle相关的文件
3. 将pom.xml添加至maven
4. 移除gradle构建项目

**温馨提示：Gradle版本不一样，转换Maven方式！！！我的Gradle 7.3**

```text
apply plugin: 'maven-publish'

publishing {
    publications {
        publish2Local(MavenPublication) {
            groupId = project.group
            artifactId = "$project.name"
            version = project.version
            from components.java
        }
    }

    repositories {
        maven {
            url = "$buildDir/repo"
        }
    }
}
```

## 演示 

![](images/img_005_b264830a8ab2.gif)

![](images/img_006_2ea3c961c980.gif)

### 测试一下

　　修改端口号、写个Controller  
![](images/img_007_c80e42d6a01c.gif)

## 遇到的问题

1. maven-publish这个插件不是100%翻译成maven依赖的，可能需要自己解决依赖冲突等问题
2. 没有翻译过来的依赖，需要自己手动单独添加maven依赖项
3. Idea没有正确指定Gradle版本，需要指定本地安装的Gradle 7.3
