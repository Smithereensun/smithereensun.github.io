{

  "title": "JavaSE基础知识之修饰符和使用场景，你真的了解嘛",
  "date": "2020-07-22",
  "description": "修饰符的作用是啥？ 用来定义类、方法或者变量的访问权限 两大类 访问修饰符 限定类、属性或方法是否可以被程序里的其他部分访问和调用的修饰符 private 公开对外部可见 protected ->对包和所有子类可见 private ->仅对类内部可见 方法级别 修饰符 当前类 同一包内 不同包中的子",
  "tags": [
    "Java"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13363531.html"

}

# 修饰符的作用是啥？

　　用来定义类、方法或者变量的访问权限

## 两大类

### 访问修饰符

- 限定类、属性或方法是否可以被程序里的其他部分访问和调用的修饰符

  - private<default<protected<public

### 非访问修饰符

- 例如static、final、abstract、synchronized等

## 死记硬背

- 外部类修饰符：public或者为默认(default)
- 方法、属性修饰符：private、default、protected、public

  - public ->公开对外部可见
  - protected ->对包和所有子类可见
  - private ->仅对类内部可见

## 方法级别 

<table border="0"> <tbody> <tr> <td>修饰符</td> <td>当前类</td> <td>同一包内</td> <td>不同包中的子类</td> <td>不同包中的非子类</td> </tr> <tr> <td>public</td> <td>Y</td> <td>Y</td> <td>Y</td> <td>Y</td> </tr> <tr> <td>protected</td> <td>Y</td> <td>Y</td> <td>Y</td> <td>N</td> </tr> <tr> <td>default</td> <td>Y</td> <td>Y</td> <td>N</td> <td>N</td> </tr> <tr> <td>private</td> <td>Y</td> <td>N</td> <td>N</td> <td>N</td> </tr> </tbody> </table>

我们主要来验证下，不熟悉的default，**什么修饰符都不加，默认为default，必须要在同一包下，才能访问的到！！！！**

![](./images/images/img_001_f2f035ec69d2.gif)
