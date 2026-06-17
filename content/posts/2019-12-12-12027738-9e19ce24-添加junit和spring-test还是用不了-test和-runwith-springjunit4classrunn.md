{

  "title": "添加junit和spring-test还是用不了@Test和@RunWith(SpringJUnit4ClassRunner.class)注解",
  "date": "2019-12-12",
  "description": "pom.xml依赖如下 问题解答 上述scope配置了Junit可用的位置，test表示只能在src下的test文件夹下面才可以使用** 解决办法 去掉scope配置就可以 解决后的依赖包修改为如下",
  "tags": [
    "JAVA"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12027738.html"

}

pom.xml依赖如下

```text
        <!-- spring 单元测试组件包 -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-test</artifactId>
            <version>5.0.7.RELEASE</version>
                        <scope>test</scope>
        </dependency>

        <!-- 单元测试Junit -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
                        <scope>test</scope>
        </dependency>
```

问题解答

**上述scope配置了Junit可用的位置，test表示只能在src下的test文件夹下面才可以使用**

解决办法

　　去掉scope配置就可以

解决后的依赖包修改为如下

```text
        <!-- spring 单元测试组件包 -->
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-test</artifactId>
            <version>5.0.7.RELEASE</version>
        </dependency>

        <!-- 单元测试Junit -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.12</version>
        </dependency>
```
