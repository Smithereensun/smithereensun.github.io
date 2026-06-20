{

  "title": "集合工具 - Collections2",
  "has_date": true,
  "description": "Collections2 私有构造器，也没有静态构造器，所以可以很明确它是一个纯工具类了。 filter过滤方法 传入一个带过滤的容器，和一个实现过滤规则的函数类，返回一个带有过滤动作的容器 如果是Collections2.FilteredCollection类，则直接转型到Collections2",
  "tags": [
    "工具库"
  ],
  "source": "local-markdown-library",
  "source_path": "tool-library/guava/guava-collection-tool - 集合工具 - Collections2.md",
  "date": "2025-05-17"

}

## [Collections2](#collections2)

私有构造器，也没有静态构造器，所以可以很明确它是一个纯工具类了。

### [filter过滤方法](#filter过滤方法)

传入一个带过滤的容器，和一个实现过滤规则的函数类，返回一个带有过滤动作的容器

如果是Collections2.FilteredCollection类，则直接转型到Collections2.FilteredCollection，然后返回这个类。如果不是Collections2.FilteredCollection，则new一个，将传入的容器和规则传入。

### [转型方法](#转型方法)

传入一个转型的类，再传入一个转型规则

### [有序排列方法](#有序排列方法)
