{

  "title": "JDK 8 新特性，从入门到精通",
  "date": "2020-12-21",
  "description": "default关键字 在**jdk1.8以前**接口里面是**只能有抽象方法**，**不能有任何方法的实现的**。 在**jdk1.8里面打破**了这个**规定**，**引入**了**新**的**关键字**：**default**，使用**default修饰方法**，**可以在接口里定义具体的方法*",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/jdk8.html"

}

# default关键字

　　在**jdk1.8以前**接口里面是**只能有抽象方法**，**不能有任何方法的实现的**。

　　在**jdk1.8里面打破**了这个**规定**，**引入**了**新**的**关键字**：**default**，使用**default修饰方法**，**可以在接口里定义具体的方法**

## 创建一个工程

![](./images/images/img_001_b8a6776aca09.gif)

## 代码实现

### 默认方法

　　接口里面定义了一个默认方法，这个接口的实现类实现了这个接口之后，不用管这个default修饰的方法就可以直接调用，即接口方法的默认实现。

![](./images/images/img_002_67367e72f915.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.defaults;

public interface People {
    void run();
    void eat();
    default void speak(){
        System.out.println("讲中国话");
    }
}
```

People

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.defaults;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/19 2:30 下午
 * @Versiion：1.0
 */
public class LaoChen implements People{
    @Override
    public void run() {
        System.out.println("老陈同志在跑步");
    }

    @Override
    public void eat() {
        System.out.println("老陈同志在吃饭");
    }
}
```

LaoChen

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.defaults;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/19 2:31 下午
 * @Versiion：1.0
 */
public class DefaultMain {
    public static void main(String[] args) {
        People people=new LaoChen();
        people.eat();
        people.run();
        people.speak();
    }
}
```

DefaultMain

### 静态方法

　　调用方式：**接口名.静态方法**，来访问接口中的静态方法

![](./images/images/img_005_c5747641edb5.gif)

# base64加解密API

![](./images/images/img_006_5ef1f03e8f9c.png)

## 旧实现方式

　　使用JDK里的**sun.misc**下的**BASE64Encoder**和**BASE64Decoder**两个类

![](./images/images/img_007_e4a0fbdbc2a9.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.base64;

import sun.misc.BASE64Decoder;
import sun.misc.BASE64Encoder;

import java.io.IOException;

/**
 * @Description：base64 加密、解密
 * @Author：chenyanbin
 * @Date：2020/12/19 2:58 下午
 * @Versiion：1.0
 */
public class Base64Demo {
    public static void main(String[] args) throws IOException {
        BASE64Encoder encoder=new BASE64Encoder();
        BASE64Decoder decoder=new BASE64Decoder();
        String str="博客地址：https://www.cnblogs.com/chenyanbin/";
        //加密
        String encode = encoder.encode(str.getBytes("utf-8"));
        System.out.println("加密后的值:"+encode);
        //解密
        byte[] bytes = decoder.decodeBuffer(encode);
        String decoderStr=new String(bytes,"utf-8");
        System.out.println("解密后的值:"+decoderStr);
    }
}
```

Base64Demo

## jdk1.8实现方式

　　在jdk1.8的**java.util**包中

![](./images/images/img_008_d44ed7398c18.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.base64;

import java.io.IOException;
import java.util.Base64;

/**
 * @Description：base64 加密、解密
 * @Author：chenyanbin
 * @Date：2020/12/19 2:58 下午
 * @Versiion：1.0
 */
public class Base64Demo {
    public static void main(String[] args) throws IOException {
        String str = "博客地址：https://www.cnblogs.com/chenyanbin/";
        Base64.Encoder encoder = Base64.getEncoder();
        Base64.Decoder decoder = Base64.getDecoder();
        //加密
        String encode = encoder.encodeToString(str.getBytes("utf-8"));
        System.out.println("加密后的值:" + encode);
        //解密
        byte[] bytes = decoder.decode(encode);
        String decoderStr = new String(bytes, "utf-8");
        System.out.println("解密后的值:" + decoderStr);
    }
}
```

Base64Demo

# 日期处理类(必备)

　　包所在的位置：java.time

## 核心类

- LocalDate：不包含具体时间的日期
- LocalTime：不含日期的时间
- LocalDateTime：包含日期及时间

![](./images/images/img_009_ac291f709df5.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.local_date;

import java.time.LocalDate;

/**
 * @Description：LocalDate，不包含具体时间的日期
 * @Author：chenyanbin
 * @Date：2020/12/19 4:00 下午
 * @Versiion：1.0
 */
public class LocalDateDemo {
    public static void main(String[] args) {
        LocalDate today = LocalDate.now();
        System.out.println("今天日期：" + today);
        //年
        System.out.println("现在是那年：" + today.getYear());
        //月
        System.out.println("现在是那月(英文)：" + today.getMonth());
        System.out.println("现在是那月(数字)：" + today.getMonthValue());
        //这月的那一天
        System.out.println("现在是这月的那天：" + today.getDayOfMonth());
        //现在是周几
        System.out.println("现在是周几" + today.getDayOfWeek());
        //现在是这年的第几天
        System.out.println("现在是这年的第几天:" + today.getDayOfYear());
        //加一年
        System.out.println("加一年："+today.plusYears(1));
        //加一月
        System.out.println("加一月："+today.plusMonths(1));
        //加一天
        System.out.println("加一天:"+today.plusDays(1));
        //减一年
        System.out.println("减一年："+today.minusYears(1));
        //减一月
        System.out.println("减一月："+today.minusMonths(1));
        //减一天
        System.out.println("减一天："+today.minusDays(1));
        //减一周
        System.out.println("减一周"+today.minusWeeks(1));
        //日期比较，是否在某年之后
        LocalDate plusYearDate = today.plusYears(1);
        System.out.println("是否在某年之后："+today.isAfter(plusYearDate));
        //日期比较，两个日期对象是否相等
        System.out.println("两个日期是否相等:"+today.isEqual(plusYearDate));
    }
}
```

LocalDateDemo

![](./images/images/img_010_9e8f3647c6a3.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.local_date;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

/**
 * @Description：日期格式化
 * @Author：chenyanbin
 * @Date：2020/12/19 11:52 下午
 * @Versiion：1.0
 */
public class LocalDateTimeFormatDemo {
    public static void main(String[] args) {
        //日期格式化
        LocalDateTime localDateTime = LocalDateTime.now();
        System.out.println(localDateTime);
        DateTimeFormatter dateTimeFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
        System.out.println("格式化后的日期格式：" + localDateTime.format(dateTimeFormatter));
        //获取指定的日期时间对象
        LocalDateTime ldt = LocalDateTime.of(2020, 12, 19, 11, 59, 59);
        System.out.println("获取指定日期时间对象：" + ldt);
        //计算日期时间差
        LocalDateTime toDay = LocalDateTime.now();
        System.out.println(toDay);
        LocalDateTime changeDate = LocalDateTime.of(2020, 12, 29, 11, 59, 59);
        System.out.println(changeDate);
        //相差多少天
        Duration duration = Duration.between(toDay, changeDate);
        System.out.println("相差多少天:"+ duration.toDays());
        System.out.println("相差多少小时:"+duration.toHours());
        System.out.println("相差多少分钟："+duration.toMinutes());
        System.out.println("相差多少毫秒数："+duration.toMillis());
        System.out.println("相差的纳秒数："+duration.toNanos());
    }
}
```

LocalDateTimeFormatDemo

# Optional类

## 作用

1.

 空指针异常(NPE)

## 演示

![](./images/images/img_011_795fbdfd4152.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.opt;

import java.util.Optional;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/20 12:15 上午
 * @Versiion：1.0
 */
public class OptionDemo {
    public static void main(String[] args) {
        Student student=null;
//        Student student=new Student("1","2");
        //null值作为参数传递进去，会抛异常
//        Optional<Student> optStudent = Optional.of(student);
//        //如果对象即可能是null也可能是非null，应该使用ofNullable
//        Optional<Student> optStudent2 = Optional.ofNullable(student);
//        //isPresent如果不为null时，返回true
//        if (optStudent2.isPresent()){
//            System.out.println("不为null");
//            //获取泛型中的值
//            Student student2 = optStudent2.get();
//            System.out.println(student2);
//        }else {
//            System.out.println("为null");
//        }
//
        //兜底orElse方法
        Student student3 = new Student("1", "2");
        Student student1 = Optional.ofNullable(student).orElse(student3);
        System.out.println(student1);
    }
}
```

OptionDemo

# Lambda表达式

## 语法

```text
(parameters) -> expression
或
(parameters) ->{ statements; }
```

## 重要特征

- **可选类型声明**：不需要声明参数类型，编译器可以统一识别参数值
- **可选的参数圆括号**：一个参数无需定义圆括号，但多个参数需要定义圆括号
- **可选的大括号**：如果主题包含了一个语句，就不需要使用大括号
- **可选的返回关键字**：如果主体只有一个表达式返回值则编译器会自动返回值，大括号需要指明表达式返回了一个数值。

## 本质

　　Lambda表达式的实现方式本质是“**以匿名内部类的方法**”进行实现，重构现有臃肿代码，更高的开发效率。

```text
package com.ybchen.lambda;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * @Description：lambda代码演示
 * @Author：chenyanbin
 * @Date：2020/12/20 11:16 上午
 * @Versiion：1.0
 */
public class LambdaDemo {
    public static void main(String[] args) {
        //使用多线程打印一句话
        //jdk1.8之前
        new Thread(new Runnable() {
            @Override
            public void run() {
                System.out.println("博客地址：https://www.cnblogs.com/chenyanbin/");
            }
        }).start();
        //jdk1.8之后需
        new Thread(() -> System.out.println("博客地址：https://www.cnblogs.com/chenyanbin/")).start();

        //List排序
        List<String> list= Arrays.asList("a","f","b","c");
        //jdk1.8之前排序：Comparator
//        Collections.sort(list, new Comparator<String>() {
//            @Override
//            public int compare(String o1, String o2) {
//                return o1.compareTo(o2);
//            }
//        });
//        System.out.println(list);
        //jdk 1.8 lambda排序
        Collections.sort(list,(o1, o2)->o1.compareTo(o2));
        System.out.println(list);
    }
}
```

## 自定义Lambda接口编程

- 定义一个函数式接口，需要标注此接口：**@FunctionalInterface**，否则万一团队成员在接口上加了其他方法则容易出现故障
- 编写一个方法，输入需要操作的数据和接口
- 在调用方法时传入数据和lambda表达式，用来操作数据

### 需求

　　定义一个可以使用加减乘除的接口，以前的话，需要定义4个接口，现在只需要定义一个即可。

### 代码实现

![](./images/images/img_012_e1a1c69727f4.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.lambda;
@FunctionalInterface
//R:return；T：参数
public interface OperatorFunction<R,T> {
    R operator(T t1,T t2);
}
```

OperatorFunction

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.lambda;

/**
 * @Description：四则运算
 * @Author：chenyanbin
 * @Date：2020/12/20 1:35 下午
 * @Versiion：1.0
 */
public class OperatorDemo {
    public static void main(String[] args) {
        System.out.println("加法：" + operator(20, 5, (x, y) -> x + y));
        System.out.println("减法：" + operator(20, 5, (x, y) -> x - y));
        System.out.println("乘法：" + operator(20, 5, (x, y) -> x * y));
        System.out.println("除法：" + operator(20, 5, (x, y) -> x / y));
    }

    private static Integer operator(Integer x, Integer y, OperatorFunction<Integer, Integer> operatorFunction) {
        return operatorFunction.operator(x, y);
    }
}
```

OperatorDemo

## JDK 1.8 新增加的函数接口

　　文档地址：[点我直达](https://www.runoob.com/java/java8-functional-interfaces.html)

![](./images/images/img_013_e34505b4ccaf.png)

![](./images/images/img_014_d3b7d7f43d8c.png)

![](./images/images/img_015_0b99a1abe42a.png)

![](./images/images/img_016_af7959a5502a.png)

![](./images/images/img_017_e363cf5223e5.png)

### 函数式编程Function

- **传入一个值经过函数的计算返回另一个值**
- **T**：入参类型，R：出参类型
- **调用方法**：R apply(T t)

![](./images/images/img_018_c1afc6e880bf.png)

### 函数式编程Bifunction

- **Function**只能**接收一个参数**， 如果要传递**两个参数**，则**用Bifunction**

![](./images/images/img_019_d1dae576e20d.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.lambda;

import java.util.function.BiFunction;

/**
 * @Description：BiFunction
 * @Author：chenyanbin
 * @Date：2020/12/20 2:27 下午
 * @Versiion：1.0
 */
public class BiFunctionDemo {
    public static void main(String[] args) {
        System.out.println("加法：" + operator(20, 5, (x, y) -> x + y));
        System.out.println("减法：" + operator(20, 5, (x, y) -> x - y));
        System.out.println("乘法：" + operator(20, 5, (x, y) -> x * y));
        System.out.println("除法：" + operator(20, 5, (x, y) -> x / y));
    }
    private static Integer operator(Integer x, Integer y, BiFunction<Integer,Integer,Integer> biFunction){
        return biFunction.apply(x,y);
    }
}
```

BiFunctionDemo

### 函数式编程Consumer

- **有入参，无返回值**
- 用途：因为没有出参，**常用于打印、发送短信**等消费动作

![](./images/images/img_020_1452b449b190.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.lambda;

import java.util.function.Consumer;

/**
 * @Description：Consumer
 * @Author：chenyanbin
 * @Date：2020/12/20 2:35 下午
 * @Versiion：1.0
 */
public class ConsumerDemo {
    public static void main(String[] args) {
        Consumer<String> consumer=(phone)->{
            System.out.println("手机号："+phone);
            System.out.println("发送短信成功");
        };
        sendMsg("11111",consumer);
    }
    private static void sendMsg(String phone, Consumer<String> consumer){
        consumer.accept(phone);
    }
}
```

ConsumerDemo

#### jdk源码中的使用

![](./images/images/img_021_6ca324a8edae.gif)

### 函数式编程Supplier

- **供给型接口**：无入参，有返回值
- **T**：出参类型，没有入参
- 用途：**泛型一定和方法**的**返回值类型**是**一种类型**，如果需要获得一个数据，并且不需要传入参数，可以使用Supplier接口，例如：无参的工厂方法，即工厂设计模式创建([点我直达](https://www.cnblogs.com/chenyanbin/p/14027999.html))对象，简单来说就是 提供者，**方便程序的解耦，**(**给你个眼神自己体会**)

![](./images/images/img_022_482a7c82c1cc.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.lambda;

import java.util.function.Supplier;

/**
 * @Description：Supplier功能演示
 * @Author：chenyanbin
 * @Date：2020/12/20 8:30 下午
 * @Versiion：1.0
 */
public class SupplierDemo {
    public static void main(String[] args) {
        Student2 stu=getStudent2();
        System.out.println(stu);
    }
    private static Student2 getStudent2(){
        Supplier<Student2> supplier=()->{
            Student2 student2=new Student2();
            student2.setId("2");
            student2.setName("默认名称");
            return student2;
        };
        return supplier.get();
    }
}
class Student2{
    private String id;
    private String name;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Student2{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                '}';
    }
}
```

SupplierDemo

### 函数式编程Predicate

- **断言型接口**：有入参，有返回值i，返回值类型确定是Boolean
- **T**：入参类型；出参类型是Boolean
- **调用方法**：boolean test(T t)
- **用途**：接收一个参数，用于判断**是否****满足**一定的**条件**，**过滤数据**

![](./images/images/img_023_74b2739f4ec5.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.lambda;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

/**
 * @Description：Predicate断言演示
 * @Author：chenyanbin
 * @Date：2020/12/20 8:56 下午
 * @Versiion：1.0
 */
public class PredicateDemo {
    public static void main(String[] args) {
        List<Integer> list= Arrays.asList(1,2,3,4,5,6);
        List<Integer> fileter = fileter(list, num -> num % 2 == 0);
        fileter.forEach(num-> System.out.println(num));
    }
    private static List<Integer> fileter(List<Integer> list, Predicate<Integer> predicate){
        List<Integer> resultList=new ArrayList<>();
        for (Integer i:list){
            if (predicate.test(i)){
                resultList.add(i);
            }
        }
        return resultList;
    }
}
```

PredicateDemo

### **BiConsumer 非常重要**

** **一般用于泛型中，动态设置某个值

```text
setValue(userVO,UserVO::getName,UserVO::setName);

    public static <T> void setValue(T t,Function<T,String> getValue,BiConsumer<T,String> setValue){
        String oldValue = getValue.apply(t);
        setValue.accept(t,"我是新增"+oldValue);
    }
```

# 构造函数引用

　　jdk1.8之前，方法调用，**对象.方法名**，或者 **类名.方法名**

　　jdk1.8提供了另外一种调用方式**::**

　　方法引用时一种更简洁易懂的lambda表达式，操作符是双冒号“**::**”，用来**直接访问类**或者**实例**已经**存在**的**方法或构造方法**。

- **静态方法**，ClassName::methodName
- **实例方法**，Intance::methodName
- **构造函数**，类名::new

```text
package com.ybchen.lambda;

import java.util.function.BiFunction;
import java.util.function.Function;

/**
 * @Description：构造函数的引用
 * @Author：chenyanbin
 * @Date：2020/12/20 9:33 下午
 * @Versiion：1.0
 */
public class ConstructionDemo {
    public static void main(String[] args) {
        //使用双冒号::，来构造静态函数的引用
        Function<String,Integer> func=Integer::parseInt;
        System.out.println(func.apply("123") instanceof Integer);
        //使用双冒号::，来构造非静态函数的引用
        String content="博客地址：https://www.cnblogs.com/chenyanbin/";
        Function<Integer,String> func2=content::substring;
        String result = func2.apply(2);
        System.out.println(result);
        //构造函数
        Function<String,Student3> func3=Student3::new;
        Student3 stu3 = func3.apply("1");
        System.out.println(stu3);
        BiFunction<String,String,Student3> func4=Student3::new;
        Student3 stu4 = func4.apply("1", "老陈");
        System.out.println(stu4);
    }
}
class Student3{
    private String id;
    private String name;

    public Student3() {
    }

    public Student3(String id) {
        this.id = id;
    }

    public Student3(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Student3{" +
                "id='" + id + '\'' +
                ", name='" + name + '\'' +
                '}';
    }
}
```

```text
true
地址：https://www.cnblogs.com/chenyanbin/
Student3{id='1', name='null'}
Student3{id='1', name='老陈'}

Process finished with exit code 0
```

# 集合框架 

## 什么是Stream？

　　Stream中文称为“流”，通过**将集合转换**为“**流**”的**元素队列**，通过声明性方式，能够对集合中的每个元素进行一系列并行或串行的流水线操作

## map和filter函数

### map

- 将流中的每一个元素T映射为R
- 应用场景：转换对象，如：**DO对象转换为DTO对象**

![](./images/images/img_024_3d352b572978.gif)

![](./images/images/img_025_73b5e9797824.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Description：map功能演示
 * @Author：chenyanbin
 * @Date：2020/12/20 10:15 下午
 * @Versiion：1.0
 */
public class MapDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("老陈","老李","老王");
        List<String> collect = list.stream().map(name -> "我叫：" + name).collect(Collectors.toList());
        collect.forEach(name-> System.out.println(name));
    }
}
```

MapDemo

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Description：map，do转dto功能演示
 * @Author：chenyanbin
 * @Date：2020/12/20 10:48 下午
 * @Versiion：1.0
 */
public class MapDemo2 {
    public static void main(String[] args) {
        List<User> list= Arrays.asList(new User("1","老陈","123"),
                new User("1","老王","123456"));
        List<UserDTO> collect = list.stream().map(obj -> new UserDTO(obj.getId(), obj.getName())).collect(Collectors.toList());
        collect.forEach(obj-> System.out.println(obj));
    }
}
class User{
    private String id;
    private String name;
    private String pwd;

    public User() {
    }

    public User(String id, String name, String pwd) {
        this.id = id;
        this.name = name;
        this.pwd = pwd;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getPwd() {
        return pwd;
    }
}
class UserDTO{
    private String userId;
    private String userName;

    public UserDTO(String userId, String userName) {
        this.userId = userId;
        this.userName = userName;
    }

    @Override
    public String toString() {
        return "UserDTO{" +
                "userId='" + userId + '\'' +
                ", userName='" + userName + '\'' +
                '}';
    }
}
```

MapDemo2

### filter

- 应用：**用于设置条件的过滤**

![](./images/images/img_026_64fdf397dc87.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Description：Filter功能演示，过滤对2取余等于0的元素
 * @Author：chenyanbin
 * @Date：2020/12/20 10:19 下午
 * @Versiion：1.0
 */
public class FilterDemo {
    public static void main(String[] args) {
        List<Integer> list= Arrays.asList(1,2,3,4,5,6,7,8,9,10);
        List<Integer> collect = list.stream().filter(num -> num % 2 == 0).collect(Collectors.toList());
        collect.forEach(num-> System.out.println(num));
    }
}
```

FilterDemo

## limit、skip、sorted函数

### sorted

- 对流进行自然排序，其中的元素**必须实现Comparable接口**

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/20 11:23 下午
 * @Versiion：1.0
 */
public class SortedDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("SpringBoot","SpringMvc","Dubbo","SpringCloud");
        //默认升序
        List<String> collect = list.stream().sorted().collect(Collectors.toList());
        System.out.println(collect);
        System.out.println("-----------");
        //自定义排序，根据长度升序
        List<String> collect1 = list.stream().sorted(Comparator.comparing(obj -> obj.length())).collect(Collectors.toList());
        System.out.println(collect1);
        //自定义排序，根据长度降序
        List<String> collect2 = list.stream().sorted(Comparator.comparing(obj -> obj.length(),Comparator.reverseOrder())).collect(Collectors.toList());
        System.out.println(collect2);
        //方法引用的玩法
        List<String> collect3 = list.stream().sorted(Comparator.comparing(String::length,Comparator.reverseOrder())).collect(Collectors.toList());
        System.out.println(collect3);

    }
}
```

### limit

- **截断**流使用最多只包含**指定数量的元素**

![](./images/images/img_027_34f12a644312.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Description：获取前3个元素
 * @Author：chenyanbin
 * @Date：2020/12/20 11:36 下午
 * @Versiion：1.0
 */
public class LimitDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("SpringBoot","SpringMvc","Dubbo","SpringCloud");
        List<String> collect = list.stream().limit(3).collect(Collectors.toList());
        System.out.println(collect);
    }
}
```

LimitDemo

### skip

- **跳过多少个元素**

![](./images/images/img_028_624e59031cec.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Description：跳过前2个元素
 * @Author：chenyanbin
 * @Date：2020/12/20 11:41 下午
 * @Versiion：1.0
 */
public class SkipDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("SpringBoot","SpringMvc","Dubbo","SpringCloud");
        List<String> collect = list.stream().skip(2).collect(Collectors.toList());
        System.out.println(list);
        System.out.println(collect);
    }
}
```

SkipDemo

## allMatch和anyMatch函数

### allMatch

- **检查**是否匹配**所有元素**，只有**全部符合才返回true**

![](./images/images/img_029_b745d95d931a.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/20 11:46 下午
 * @Versiion：1.0
 */
public class AllMatchDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("SpringBoot","SpringMvc","SDubbo","SpringCloud");
        boolean b = list.stream().allMatch(str -> str.startsWith("S"));
        System.out.println(b);
    }
}
```

AllMatchDemo

### anyMatch

- **检查**是否**至少匹配一个元素**

![](./images/images/img_030_0b26eeed8882.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;

/**
 * @Description：至少匹配一个返回true
 * @Author：chenyanbin
 * @Date：2020/12/20 11:48 下午
 * @Versiion：1.0
 */
public class AnyMatchDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("SpringBoot","SpringMvc","Dubbo","SpringCloud");
        boolean b = list.stream().anyMatch(str -> str.startsWith("s"));
        System.out.println(b);
    }
}
```

AnyMatchDemo

## max和min函数

- 求最大、最小

![](./images/images/img_031_9efa7e5b9af0.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;

/**
 * @Description：求最大、最小
 * @Author：chenyanbin
 * @Date：2020/12/21 12:01 上午
 * @Versiion：1.0
 */
public class MaxAndMinDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("SpringBoot","SpringMvc","Dubbo","SpringCloud");
        String s = list.stream().max((str1, str2) -> str1.length() - str2.length()).get();
        System.out.println(s);
        String s2 = list.stream().min((str1, str2) -> str1.length() - str2.length()).get();
        System.out.println(s2);
    }
}
```

MaxAndMinDemo

## distinct函数

![](./images/images/img_032_e07884c8e2f8.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

/**
 * @Description：对元素去重
 * @Author：chenyanbin
 * @Date：2020/12/20 11:54 下午
 * @Versiion：1.0
 */
public class DistinctDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("SpringBoot","SpringMvc","Dubbo","SpringCloud","Dubbo");
        System.out.println(list);
        List<String> collect = list.stream().distinct().collect(Collectors.toList());
        System.out.println(collect);
    }
}
```

DistinctDemo

## 并行流parallelStream

- 集合做重复的操作，如果使用串行执行会相当耗时，因此一般会采用多线程来加快，java 8的paralleStream用fork/join框架提供了并发执行能力

![](./images/images/img_033_e75d263af30c.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;

/**
 * @Description：ParallelStream串行流演示
 * @Author：chenyanbin
 * @Date：2020/12/21 9:41 下午
 * @Versiion：1.0
 */
public class ParallelStreamDemo {
    public static void main(String[] args) {
        List<Integer> list= Arrays.asList(1,2,3,4,5,6,7,8);
        list.stream().forEach(System.out::println);
        System.out.println("===============");
        list.parallelStream().forEach(System.out::println);
    }
}
```

ParallelStreamDemo

### 注意事项

- parallelStream里面使用外部变量时，会出现线程安全问题，集合一定要使用线程安全集合

## reduce操作

- 根据一定的规则将Stream中的元素进行计算后返回一个唯一的值 

### 常用方法一 

![](./images/images/img_034_f7c272946404.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.stream.Stream;

/**
 * @Description：Reduce功能演示
 * @Author：chenyanbin
 * @Date：2020/12/21 10:01 下午
 * @Versiion：1.0
 */
public class ReduceDemo {
    public static void main(String[] args) {
        Integer sum = Stream.of(1, 2, 3, 4).reduce((num1, num2) -> num1 + num2).get();
        System.out.println(sum);
    }
}
```

ReduceDemo

求一堆数的最大值

![](./images/images/img_035_1e882acb35ea.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.stream.Stream;

/**
 * @Description：Reduce功能演示
 * @Author：chenyanbin
 * @Date：2020/12/21 10:01 下午
 * @Versiion：1.0
 */
public class ReduceDemo {
    public static void main(String[] args) {
        //求一堆数的最大值
        Integer maxValue = Stream.of(1, 33, 5, 6, 2).reduce((num1, num2) -> num1 > num2 ? num1 : num2).get();
        System.out.println(maxValue);
    }
}
```

ReduceDemo

### 常用方法二

　　提供一个初始值，进行数据累加

![](./images/images/img_036_ffb6273dce89.gif)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.stream.Stream;

/**
 * @Description：Reduce功能演示
 * @Author：chenyanbin
 * @Date：2020/12/21 10:01 下午
 * @Versiion：1.0
 */
public class ReduceDemo {
    public static void main(String[] args) {
        //提供一个初始值，对数据进行累加操作
        Integer sum = Stream.of(1, 2, 3, 4).reduce(100,(num1, num2) -> num1 + num2);
        System.out.println(sum);
    }
}
```

ReduceDemo

# 收集器和集合统计

## collector收集器

```text
package com.ybchen.stream;

import java.util.*;
import java.util.stream.Collectors;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/21 10:45 下午
 * @Versiion：1.0
 */
public class CollectorDemo {
    public static void main(String[] args) {
        List<Integer> list= Arrays.asList(1,2,3,4,5);
        List<Integer> collect = list.stream().collect(Collectors.toList());
        Set<Integer> collect1 = list.stream().collect(Collectors.toCollection(TreeSet::new));
        List<Integer> collect2 = list.stream().collect(Collectors.toCollection(LinkedList::new));
    }
}
```

## joining函数

- 拼接函数，Collectors.joining

![](./images/images/img_037_9765a61b027d.png)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * @Description：字符串拼接
 * @Author：chenyanbin
 * @Date：2020/12/21 10:51 下午
 * @Versiion：1.0
 */
public class JoinDemo {
    public static void main(String[] args) {
        List<String> list= Arrays.asList("a","b","c","d");
        String collect = list.stream().collect(Collectors.joining());
        System.out.println(collect);
        System.out.println("==========");
        String collect2 = list.stream().collect(Collectors.joining("_"));
        System.out.println(collect2);
        System.out.println("==========");
        String collect3 = list.stream().collect(Collectors.joining("_","(",")"));
        System.out.println(collect3);
        System.out.println("=========");
        String result = Stream.of("a", "b", "c", "d").collect(Collectors.joining(",", "「", "」"));
        System.out.println(result);
    }
}
```

JoinDemo

## partitioningBy分组

- Collectors.partitioningBy分组，key是boolean类型 

![](./images/images/img_038_330028359311.png)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * @Description：
 * @Author：chenyanbin
 * @Date：2020/12/21 11:01 下午
 * @Versiion：1.0
 */
public class PartitioningByDemo {
    public static void main(String[] args) {
        List<Integer> list= Arrays.asList(1,2,3,4,5,6);
        Map<Boolean, List<Integer>> collect = list.stream().collect(Collectors.partitioningBy(num -> num % 2 == 0));
        System.out.println(collect);
    }
}
```

PartitioningByDemo

## groupby分组

- 分组，Collectors.groupingBy()

![](./images/images/img_039_8b95790a7663.png)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * @Description：根据学生所在的省份，进行分组
 * @Author：chenyanbin
 * @Date：2020/12/21 11:05 下午
 * @Versiion：1.0
 */
public class GroupByDemo {
    public static void main(String[] args) {
        List<Student> list= Arrays.asList(
                new Student("老陈","上海"),
                new Student("老王","北京"),
                new Student("老李","上海"),
                new Student("老赵","广东"));
        Map<String, List<Student>> collect = list.stream().collect(Collectors.groupingBy(obj -> obj.getProvince()));
        System.out.println(collect);
    }
}
class Student{
    private String name;
    private String province;

    public Student(String name, String province) {
        this.name = name;
        this.province = province;
    }

    public String getProvince() {
        return province;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", province='" + province + '\'' +
                '}';
    }
}
```

GroupByDemo

## counting集合统计

- 聚合函数进行统计查询，分组后统计个数
- Collectors.counting()：统计元素个数

需求：统计省份的人数

![](./images/images/img_040_3c6bd75dc842.png)

![](./images/images/img_003_8f900a89c634.gif)
![](./images/images/img_004_961ddebeb323.gif)

```text
package com.ybchen.stream;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

/**
 * @Description：根据学生所在的省份，进行分组
 * @Author：chenyanbin
 * @Date：2020/12/21 11:05 下午
 * @Versiion：1.0
 */
public class GroupByDemo {
    public static void main(String[] args) {
        List<Student> list= Arrays.asList(
                new Student("老陈","上海"),
                new Student("老王","北京"),
                new Student("老李","上海"),
                new Student("老赵","广东"));
        Map<String, Long> collect = list.stream().collect(Collectors.groupingBy(obj -> obj.getProvince(), Collectors.counting()));
        System.out.println(collect);
    }
}
class Student{
    private String name;
    private String province;

    public Student(String name, String province) {
        this.name = name;
        this.province = province;
    }

    public String getProvince() {
        return province;
    }

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", province='" + province + '\'' +
                '}';
    }
}
```

GroupByDemo
