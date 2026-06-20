{

  "title": "dubbo - SPI机制",
  "has_date": true,
  "description": "JDK的SPI机制的缺点 ⽂件中的所有类都会被加载且被实例化。这样也就导致获取某个实现类的方式不够灵活，只能通过 Iterator 形式获取，不能根据某个参数来获取对应的实现类。如果不想用某些实现类，或者某些类实例化很耗时，它也被载入并实例化了，没有办法指定某⼀个类来加载和实例化，这就造成了浪费。 ",
  "tags": [
    "微服务",
    "Dubbo"
  ],
  "source": "local-markdown-library",
  "source_path": "microservices/rpc/dubbo-spimechanism - dubbo - SPI机制.md",
  "date": "2026-01-19"

}

## [JDK的SPI机制的缺点](#jdk的spi机制的缺点)

⽂件中的所有类都会被加载且被实例化。这样也就导致获取某个实现类的方式不够灵活，只能通过 Iterator 形式获取，不能根据某个参数来获取对应的实现类。如果不想用某些实现类，或者某些类实例化很耗时，它也被载入并实例化了，没有办法指定某⼀个类来加载和实例化，这就造成了浪费。

此时dubbo的SPI可以解决

## [dubbo的SPI机制](#dubbo的spi机制)

dubbo⾃⼰实现了⼀套SPI机制来解决Java的SPI机制存在的问题。

dubbo中则采用了类似kv对的样式，在具体使用的时候则通过相关想法即可获取，而且获取的文件路径也不一致

**ExtensionLoader 类文件**

如上述代码片段可知，dubbo是支持从META-INF/dubbo/,META-INF/dubbo/internal/以及META-INF/services/三个文件夹的路径去获取spi配置
![](/imported/markdown/2026-01-19-markdown-e0a16217-dubbo-spi机制/images/0025594aef8f-202404301931070.png)
例如com.alibaba.dubbo.rpc.Protocol 文件内容

不过观察上述文件会发现，HttpProtocol是没有对应的k值，那就是说无法通过kv对获取到其协议实现类。后面通过源码可以发现，如果没有对应的name的时候，dubbo会通过findAnnotationName方法获取一个可用的name

## [Dubbo SPI 使用](#dubbo-spi-使用)

如何自定义一个 Dubbo 的 SPI 扩展？

要自定义一个 Dubbo 的 SPI（Service Provider Interface）扩展，一般需要遵循以下几个步骤：

1. 定义接口：创建你想要扩展的接口，并使用 Dubbo 的 @SPI 注解标记它。

1. 实现接口：创建该接口的具体实现类。

1. 创建 SPI 配置文件：在 `META-INF/dubbo/` 目录下创建相应的配置文件，其名称为接口的全限定名，内容是实现类的键值对。

1. 在代码中使用：通过 ExtensionLoader 加载和使用你自定义的 SPI 扩展。

下面是示例代码：

1）定义一个接口，并用 @SPI 注解标记：

2）实现这个接口：

3）创建 `SPI` 配置文件：
 文件路径：`META-INF/dubbo/com.example.extension.MyService` 内容如下：

4）在代码中使用扩展：

## [Dubbo源码学习](#dubbo源码学习)

通过获取协议的代码来分析下具体的操作过程

### [Protocol 获取](#protocol-获取)

Protocol protocol = ExtensionLoader.getExtensionLoader(Protocol.class).getAdaptiveExtension();

如下代码Protocol$Adpative 整个的类就是通过createAdaptiveExtensionClassCode()方法**生成的一个大字符串**

到现在可以认为是最上面的获取protocol的方法Protocol protocol = ExtensionLoader.getExtensionLoader(Protocol.class).getAdaptiveExtension() 返回了一个代码拼接而成然后编译操作的实现类Protocol$Adpative

可是得到具体的实现呢？在com.alibaba.dubbo.rpc.Protocol extension = (com.alibaba.dubbo.rpc.Protocol)ExtensionLoader.getExtensionLoader(com.alibaba.dubbo.rpc.Protocol.class).getExtension(extName)这个代码中，当然这个是有在具体的暴露服务或者引用远程服务才被调用执行的。

到这一步就可以认为是dubbo的spi加载整个的过程完成了，整个链路有些长，需要好好的梳理一下

### [SPI配置文件解析](#spi配置文件解析)

上文说到getExtensionClasses完成对spi文件的解析

这样完成了对spi配置文件的整个的扫描过程了
