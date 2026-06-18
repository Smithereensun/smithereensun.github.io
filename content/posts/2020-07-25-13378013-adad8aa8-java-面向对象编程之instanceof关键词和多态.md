{

  "title": "Java 面向对象编程之InstanceOf关键词和多态",
  "date": "2020-07-25",
  "description": "InstanceOf关键字使用，什么是多态 InstanceOf关键字 是Java的一个二元操作符(运算符)，也是Java的保留关键字 语法 对象类型强制转换前的判断 方法重写和重载 方法重写 override 子类对父类的允许访问的方法的实现过程进行重新编写 注意点 返回值和形参都不能改变 父类的",
  "tags": [
    "Java"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13378013.html"

}

# InstanceOf关键字使用，什么是多态

## InstanceOf关键字

1. 是Java的一个二元操作符(运算符)，也是Java的保留关键字
2. 语法

```text
//如果该object 是该class的⼀个实例，那⼀个实例，或者object是null，则返回falboolean result = object instanceo参数：
　　result ：boolean类型。
　　object ：必选项。任意对象表达式。
　　class：必选项。任意已定义的对象类。
```

## 对象类型强制转换前的判断

```text
Person p1 = new Student();
//判断对象p是否为Student类的实例
if(1p instanceof Student)
{
 //向下转型
 Student s = (Student)p1;
}
```

# 方法重写和重载

## 方法重写 override

- 子类对父类的允许访问的方法的实现过程进行重新编写
- 注意点

  - 返回值和形参都不能改变
  - 父类的成员方法只能被它的子类重写
  - final和static的方法不能被重写
  - 构造方法不能被重写
  - 访问权限不能比父类中被重写的方法的访问权限更低

## 方法重载 overload

- 一个类里面，方法名字相同但参数不同，返回类型可以相同也可以不同
- 比如构造函数重载

## 区分

　　override是在不同类之间的行为，overload是在同一个类中的行为

### Java多态总结

1. 同一个行为具有多个不同表现形式或形态的能力
2. 常见的方式

  1. 继承方法重写
  2. 同类方法重载
  3. 抽象方法
  4. 接口
