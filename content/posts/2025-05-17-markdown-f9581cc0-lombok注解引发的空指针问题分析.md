{

  "title": "Lombok注解引发的空指针问题分析",
  "has_date": true,
  "description": "问题描述 在一次上线后，日志中出现空指针的报错，但是报错代码位置以及相应工具类未进行过修改，接下来进一步分析。 以下为报错堆栈信息： 问题分析 分析链路长，直接抛结论 通过Lombok提供的功能使得我们不必在对象中显式定义get和set方法。并且Lombok提供链式编程，通过在对象头部加上@Acce",
  "tags": [
    "系统设计"
  ],
  "source": "local-markdown-library",
  "source_path": "system-design/best-practices/lombok-nullpointerproblem - Lombok注解引发的空指针问题分析.md",
  "date": "2025-05-17"

}

## [问题描述](#问题描述)

在一次上线后，日志中出现空指针的报错，但是报错代码位置以及相应工具类未进行过修改，接下来进一步分析。

以下为报错堆栈信息：

## [问题分析](#问题分析)

### [分析链路长，直接抛结论](#分析链路长-直接抛结论)

通过Lombok提供的功能使得我们不必在对象中显式定义get和set方法。并且Lombok提供链式编程，通过在对象头部加上@Accessors(chain = true)注解，给属性赋值时，可以写成obj.setA(a).setB(b).setC(c)，省去先new再对属性逐个set赋值。使用了该注解，这个类的set方法返回我就不是void而是this对象本身。

而JDK Introspector（它为目标JavaBean提供了一种了解原类方法、属性和事件的标准方法）中对写入方法是有特殊判断的，截取Introspector.getBeanInfo(beanClass)中一段源码，只有返回值是void，且方法名以set作为前缀的，才会被当做writeMethod，即写入方法。所以返回值为void且是“set”开头的才是Introspector认为的写入方法，一种狭义的定义。

像BeanCopier依赖Introspector的writeMethod对目标类赋值的工具，在转换使用了@Accessors(chain = true)注解的类时，在获取属性描述PropertyDescriptor就不会返回这个属性的writeMethod属性，就相当于该类的属性没有“写入方法”，这就造成了拷贝对象过程中出现空指针问题。

### [分析路径](#分析路径)

（1）通过报错信息定位到代码端，通常情况看到mtProcessDtoList是从服务中获取，第一印象认为对象是可能为null，其实不然，仔细看堆栈，问题还是出在工具类里，“***.CglibBeanCopier.copyProperties”，继续看这段代码是存在判空操作的，造成空指针的还是copyProperties这个方法。

（2）具体看copyProperties这个代码的实现，工具类的封装的底层能力是BeanCopier提供的，从传参来看并没有我们常见的传null后对null进行操作引起的空指针，还需要对BeanCopier的源码进行分析。

（3）由于jar是进行反编译的，堆栈里提供的代码行数已经失真了，直接贴上报空指针的源码截图。
![](/imported/markdown/2025-05-17-markdown-f9581cc0-lombok注解引发的空指针问题分析/images/bf2ca2db5395-202407022332661.webp)![](/imported/markdown/2025-05-17-markdown-f9581cc0-lombok注解引发的空指针问题分析/images/b0017feb087a-202407022332298.webp)
getMethodInfo入参member是null，从而导致空指针。需要通过断点跟踪运行时的变量值，找到setters数组中的元素是如何生成的。
![](/imported/markdown/2025-05-17-markdown-f9581cc0-lombok注解引发的空指针问题分析/images/570e442aaafb-202407022332361.webp)
（4）target是作为对象拷贝的目标对象的类，setters这个数组就是通过反射获取该目标类的所有具备读方法的描述对象（PropertyDescriptor对象，可以理解为属性/方法描述）。这里面方法名有些歧义，不是说只返回getter相关的属性对象，返回的是该类所有具备读或写方法的属性描述，两个布尔值的类型分别控制校验读或写。
![](/imported/markdown/2025-05-17-markdown-f9581cc0-lombok注解引发的空指针问题分析/images/c04e0d20f47b-202407022332033.webp)![](/imported/markdown/2025-05-17-markdown-f9581cc0-lombok注解引发的空指针问题分析/images/67cdda463a77-202407022333461.webp)
综上，由于无法获取目标类的writeMethod，从而没有办法找到这个属性的写入方法，就没有办法对目标对象继续赋值。
![](/imported/markdown/2025-05-17-markdown-f9581cc0-lombok注解引发的空指针问题分析/images/0a6e109db125-202407022333054.webp)
此时方向就转到了目标类的实现上，分析到这里就跟Lombok产生了联系。此处确实被修改过，WaybillProcess类增加了@Accessors这个注解。

（5）WaybillProcess使用了@Accessors(chain = true)这个注解，这就回到了开头提到的，在使用了这个注解后该类生成的set方法返回值就不是void而是this，在通过Introspector获取属性描述时就不会被认定是写入方法，在去掉这个注解后，writeMethodName就有值了。
![](/imported/markdown/2025-05-17-markdown-f9581cc0-lombok注解引发的空指针问题分析/images/5534bd11d408-202407022333729.webp)
## [解决办法](#解决办法)

解决办法1：删除该注解，将工程里链式set改成了常规的set赋值方式。

解决办法2：保留该注解，替换对象拷贝的工具类，建议使用MapStruct配合Lombok，直接在编译时生成get/set方法，更加安全，功能也更加强大。

## [总结](#总结)

凡是依赖JDK Introspector获取类set方法描述的工具类、组件都会受到其写入方法定义导致的一些列问题，目前在工程实践中遇到了BeanCopier进行对象拷贝、BeanUtils对属性进行赋值都会遇到问题。所以大家在日常开发过程中，如果该类已经被大面积地使用，在使用组件特性时需要多留意。
