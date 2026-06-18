{

  "title": "Spring DI(依赖注入)自动装配 @Autowired、@Resource注解",
  "date": "2020-05-21",
  "description": "@Autowired：一部分功能是**查找实例**，从Spring容器中**根据类型**（Java类）**获取对应的实例**；另一部分功能就是**赋值**，将找到的实例，装配给另一个实例的属性值。（**注：一个Java类型在同一个Spring容器中，只能有一个实例。**） @Resource：一部分",
  "tags": [
    "Spring",
    "Elasticsearch"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12929760.html"

}

1. @Autowired：一部分功能是**查找实例**，从Spring容器中**根据类型**（Java类）**获取对应的实例**；另一部分功能就是**赋值**，将找到的实例，装配给另一个实例的属性值。（**注：一个Java类型在同一个Spring容器中，只能有一个实例。**）
2. @Resource：一部分功能是**查找实例**，从Spring容器中**根据Bean的名称**（bean标签的名称）**获取对应的实例**；另一部分功能就是**赋值**，将找到的实例，装配给另一个实例的属性值。
