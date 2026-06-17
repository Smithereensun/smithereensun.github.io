{

  "title": "SpringBoot 启动时报错Unable to start embedded Tomcat",
  "date": "2023-09-18",
  "description": "导读 最近公司有个gradle构建的工程，需要改造成maven方式构建（点我直达）。转为maven后，启动时一直报tomcat错误，最终排查是因为servlet-api这个包导致的依赖冲突，将这个依赖排除即可启动 解决 排除依赖，检查项目是否包含：**javax.servlet-api**",
  "tags": [
    "Spring Boot",
    "Maven"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/17712976.html"

}

# 导读

　　最近公司有个gradle构建的工程，需要改造成maven方式构建（[点我直达](https://www.cnblogs.com/chenyanbin/p/gradle.html)）。转为maven后，启动时一直报tomcat错误，最终排查是因为servlet-api这个包导致的依赖冲突，将这个依赖排除即可启动

## 解决

排除依赖，检查项目是否包含：**javax.servlet-api**

```text
   <exclusions>
                <exclusion>
                    <groupId>javax.servlet</groupId>
                    <artifactId>javax.servlet-api</artifactId>
                </exclusion>
            </exclusions>
```
