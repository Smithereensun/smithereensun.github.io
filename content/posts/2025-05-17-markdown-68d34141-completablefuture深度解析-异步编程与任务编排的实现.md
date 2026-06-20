{

  "title": "CompletableFuture深度解析：异步编程与任务编排的实现",
  "has_date": true,
  "description": "前言 CompletableFuture是jdk8的新特性。 的实现与使用上，处处体现出了**函数式异步编程**的味道。一个 对象可以被一个环节接一个环节的处理、也可以对两个或者多个 进行组合处理或者等待结果完成。通过对 各种方法的合理使用与组合搭配，可以在很多的场景都可以应付自如。 Complet",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/05-concurrenttools7-completablefuture - CompletableFuture深度解析：异步编程与任务编排的实现.md",
  "date": "2025-05-17"

}

## [前言](#前言)

CompletableFuture是jdk8的新特性。`CompletableFuture`的实现与使用上，处处体现出了**函数式异步编程**的味道。一个`CompletableFuture`对象可以被一个环节接一个环节的处理、也可以对两个或者多个`CompletableFuture`进行组合处理或者等待结果完成。通过对`CompletableFuture`各种方法的合理使用与组合搭配，可以在很多的场景都可以应付自如。

CompletableFuture实现了CompletionStage接口和Future接口，前者是对后者的一个扩展，增加了异步会点、流式处理、多个Future组合处理的能力，使Java在处理多任务的协同工作时更加顺畅便利。

假设现在需求如下：
 从网上查询某个产品的最低价格，例如可以从淘宝、京东、拼多多去获取某个商品的价格、优惠金额，并计算出实际的付款金额，最终返回价格最低的价格信息。

这里假设每个平台获取原价格与优惠券的接口已经实现、且都是需要调用HTTP接口查询的耗时操作，接口每个耗时`1s`左右。

根据需求理解，可以很自然的写出对应实现代码：

运行测试下：

结果符合预期，功能正常，但是耗时较长。试想一下，假如你在某个APP操作需要等待6s才返回最终计算结果，那不得直接摔手机？

梳理下代码的实现思路：
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/70f3677166cc-202409111511884.jpg)
可以知道所有的环节都是`串行实现的`的，由于每个查询接口的耗时都是1s，因此每个环节耗时加到一起，接口总耗时超过6s。

但实际上，每个平台之间的操作是**互不干扰**的，那其实就可以通过`多线程`的方式，同时去分别执行各个平台的逻辑处理，最后将各个平台的结果汇总到一起比对得到最低价格。

所以整个执行过程会变成如下的效果：
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/385222f5914c-202409111515372.jpg)
因此为了提升性能，可以采用**线程池**来负责多线程的处理操作，因为需要得到各个子线程处理的结果，所以需要使用 `Future`来实现：

上述代码中，将三个不同平台对应的`Callable`函数逻辑放入到`ThreadPool`中去执行，返回`Future`对象，然后再逐个通过`Future.get()`接口**阻塞**获取各自平台的结果，最后经比较处理后返回最低价信息。

执行代码，可以看到执行结果与过程如下：

接口总耗时从`6s`下降到了`2s`，效果还是很显著的。但是，是否还能再压缩一些呢？

基于上面按照平台拆分并行处理的思路继续推进，我们可以看出每个平台内的处理逻辑其实可以分为3个主要步骤：

1. 获取原始价格（耗时操作）

1. 获取折扣优惠（耗时操作）

1. 得到原始价格和折扣优惠之后，计算实付价格

这3个步骤中，其实第1、2两个耗时操作也是相对独立的，如果也能并行处理的话，响应时长上应该也能继续缩短，即如下的处理流程：
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/d2acfc6ab56d-202409111524403.jpg)
这里当然也可以继续使用上面提到的`线程池+Future`的方式，但`Future`在应对并行结果组合以及后续处理等方面显得力不从心，**弊端**明显：

代码写起来会**非常拖沓**：先封装`Callable`函数放到线程池中去执行查询操作，然后分三组`阻塞等待`结果并计算出各自结果，最后再`阻塞等待`价格计算完成后汇总得到最终结果。

说到这里呢，就需要`CompletableFuture`登场了，`CompletableFuture`可以很轻松的来完成任务的并行处理，以及各个并行任务结果之间的组合再处理等操作。使用`CompletableFuture`编写实现代码如下：

看下执行结果符合预期，而接口耗时则降到了`1s`（因为依赖的每一个查询实际操作的接口耗时都是模拟的1s，所以这个结果已经算是此复合接口能达到的极限值了）。

这里**CompletableFuture**执行时所使用的默认线程池是`ForkJoinPool`。

## [Future与CompletableFuture](#future与completablefuture)

首先，先来理一下Future与CompletableFuture之间的关系。

### [Future](#future)

如果接触过多线程相关的概念，那`Future`应该不会陌生，早在**Java5**中就已经存在了。

该如何理解`Future`呢？举个生活中的例子：

你去咖啡店点了一杯咖啡，然后服务员会给你一个订单小票。 当服务员在后台制作咖啡的时候，你并没有在店里等待，而是出门到隔壁甜品店又买了个面包。 当面包买好之后，你回到咖啡店，拿着订单小票去取咖啡。 取到咖啡后，你边喝咖啡边把面包吃了……嗝~

是不是很熟悉的生活场景？ 对比到我们多线程异步编程的场景中，咖啡店的订单小票其实就是Future，通过Future可以让稍后适当的时候可以获取到对应的异步执行线程中的执行结果。

上面的场景，我们翻译为代码实现逻辑：

Future相关的了解可以看这篇文章：FutureTask是Future的基础实现

### [CompletableFuture](#completablefuture)

Future在应对一些简单且相互独立的异步执行场景很便捷，但是在一些复杂的场景，比如同时需要多个有依赖关系的异步独立处理的时候，或者是一些类似流水线的异步处理场景时，就显得力不从心了。比如：

- 同时执行多个并行任务，等待最快的一个完成之后就可以继续往后处理

- 多个异步任务，每个异步任务都需要依赖前一个异步任务执行的结果再去执行下一个异步任务，最后只需要一个最终的结果

- 获取计算结果的 `get()` 方法为阻塞调用

Java 8 才被引入`CompletableFuture` 类可以解决`Future` 的这些缺陷。`CompletableFuture` 除了提供了更为好用和强大的 `Future` 特性之外，还提供了函数式编程、异步任务编排组合（可以将多个异步任务串联起来，组成一个完整的链式调用）等能力。

可以看到，`CompletableFuture` 同时实现了 `Future` 和 `CompletionStage` 接口。
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/da3685949455-202409111537617.jpeg)
## [CompletableFuture使用方式](#completablefuture使用方式)

### [创建**CompletableFuture**并执行](#创建completablefuture并执行)

当需要进行异步处理的时候，可以通过`CompletableFuture.supplyAsync`方法，传入一个具体的要执行的处理逻辑函数，这样就轻松的完成了**CompletableFuture**的创建与触发执行。
方法名称作用描述supplyAsync静态方法，用于构建一个`CompletableFuture&lt;T&gt;`对象，并异步执行传入的函数，允许执行函数有返回值`T`。runAsync静态方法，用于构建一个`CompletableFuture&lt;Void&gt;`对象，并异步执行传入函数，与supplyAsync的区别在于此方法传入的是Callable类型，**仅执行，没有返回值**。
使用示例：

特别补充：

`supplyAsync`或者`runAsync`创建后便会立即执行，无需手动调用触发。

### [线程串行化方法](#线程串行化方法)

#### [使用方法](#使用方法)

在流水线处理场景中，往往都是一个任务环节处理完成后，下一个任务环节接着上一环节处理结果继续处理。`CompletableFuture`用于这种流水线环节驱动类的方法有很多，相互之间主要是在返回值或者给到下一环节的入参上有些许差异，使用时需要注意区分：
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/93eecbd397c4-202409111557853.png)
具体的方法的描述归纳如下：
方法名称作用描述thenApply对`CompletableFuture`的执行后的具体结果进行追加处理，并将当前的`CompletableFuture`泛型对象更改为处理后新的对象类型，返回当前`CompletableFuture`对象。thenCompose与`thenApply`类似。区别点在于：此方法的入参函数是一个`CompletableFuture`类型对象，适用于回调函数需要启动另一个异步计算，并且想要一个扁平化的结果CompletableFuture，而不是嵌套的`CompletableFuture&lt;CompletableFuture&lt;U&gt;&gt;`thenAccept与`thenApply`方法类似，区别点在于`thenAccept`返回**void**类型，**没有具体结果输出**，适合无需返回值的场景。thenRun与`thenAccept`类似，区别点在于`thenAccept`可以将前面`CompletableFuture`执行的实际结果作为入参进行传入并使用，但是`thenRun`方法**没有任何入参**，只能执行一个Runnable函数，并且**返回void类型**。
因为上述`thenApply`、`thenCompose`方法的输出仍然都是一个**CompletableFuture**对象，所以各个方法是可以一环接一环的进行调用，形成流水线式的处理逻辑：
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/2eb4be07fd30-202409111558423.png)
##### [thenApply](#thenapply)

上面任务执行完执行 + 能获取上步返回值 + 自己有返回值

结果：

##### [thenAccept](#thenaccept)

上面任务执行完执行 + 能获取上步返回值

结果：

##### [thenRun](#thenrun)

上面任务执行完执行

结果：

##### [thenCompose](#thencompose)

接收返回值并生成新的任务

- thenApply()：转换的是泛型中的类型，相当于将CompletableFuture 转换生成新的CompletableFuture

- thenCompose()：用来连接两个CompletableFuture，是生成一个新的CompletableFuture。

#### [串联示例](#串联示例)

### [线程并联方法](#线程并联方法)

很多时候为了提升并行效率，一些没有依赖的环节我们会让他们同时去执行，然后在某些环节需要依赖的时候，进行结果的依赖合并处理，类似如下图的效果。
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/26d410709a5c-202409111622730.png)
`CompletableFuture`相比于`Future`的一大优势，就是可以方便的实现多个并行环节的合并处理。相关涉及方法介绍归纳如下：
方法名称作用描述thenCombine将两个`CompletableFuture`对象组合起来进行下一步处理，可以拿到两个执行结果，并传给自己的执行函数进行下一步处理，最后返回一个新的`CompletableFuture`对象。thenAcceptBoth与`thenCombine`类似，区别点在于`thenAcceptBoth`传入的执行函数没有返回值，即thenAcceptBoth返回值为`CompletableFuture&lt;Void&gt;`。runAfterBoth等待两个`CompletableFuture`都执行完成后再执行某个Runnable对象，再执行下一个的逻辑，类似thenRun。applyToEither两个`CompletableFuture`中任意一个完成的时候，继续执行后面给定的新的函数处理。再执行后面给定函数的逻辑，类似thenApply。acceptEither两个`CompletableFuture`中任意一个完成的时候，继续执行后面给定的新的函数处理。再执行后面给定函数的逻辑，类似thenAccept。runAfterEither等待两个`CompletableFuture`中任意一个执行完成后再执行某个Runnable对象，可以理解为`thenRun`的升级版，注意与`runAfterBoth`对比理解。allOf静态方法，**阻塞**等待所有给定的`CompletableFuture`执行结束后，返回一个`CompletableFuture&lt;Void&gt;`结果。anyOf静态方法，阻塞等待任意一个给定的`CompletableFuture`对象执行结束后，返回一个`CompletableFuture&lt;Void&gt;`结果。
#### [使用方法](#使用方法-1)

##### [thenCombine](#thencombine)

消费两个结果 + 返回结果

结果：

##### [thenAcceptBoth](#thenacceptboth)

消费两个结果 + 无返回

结果

##### [runAfterBoth](#runafterboth)

两个任务都完成后，再接着运行

结果

##### [applyToEither](#applytoeither)

只要有一个执行完就执行 + 获取返回值 + 有返回值

结果

##### [acceptEither](#accepteither)

只要有一个执行完就执行 + 获取返回值

结果

##### [runAfterEither](#runaftereither)

只要有一个执行完就执行

结果

##### [allOf](#allof)

等待全部完成后才执行

结果

##### [anyOf](#anyof)

等待其中之一完成后就执行

结果

#### [并联示例](#并联示例)

### [结果等待与获取](#结果等待与获取)

在执行线程中将任务放到工作线程中进行处理的时候，执行线程与工作线程之间是异步执行的模式，如果执行线程需要获取到共工作线程的执行结果，则可以通过`get`或者`join`方法，**阻塞等待**并从`CompletableFuture`中获取对应的值。
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/5e7f107b2c88-202409111647261.png)
对`get`和`join`的方法功能含义说明归纳如下：
方法名称作用描述get()等待`CompletableFuture`执行完成并获取其具体执行结果，可能会抛出异常，**需要**代码调用的地方手动`try...catch`进行处理。get(long, TimeUnit)与get()相同，只是**允许设定阻塞等待超时时间**，如果等待超过设定时间，则会抛出异常终止阻塞等待。join()等待`CompletableFuture`执行完成并获取其具体执行结果，可能会抛出运行时异常，**无需**代码调用的地方手动try...catch进行处理。
从介绍上可以看出，两者的区别就在于是否需要调用方**显式的进行try...catch处理逻辑**，使用代码示例如下：

### [异常处理](#异常处理)

在编排流水线的时候，如果某一个环节执行抛出异常了，会导致整个流水线后续的环节就没法再继续下去了，比如下面的例子：

执行之后会发现，supplyAsync抛出异常后，后面的thenApply并没有被执行。

那如果想要让流水线的每个环节处理失败之后都能让流水线继续往下面环节处理，让后续环节可以拿到前面环节的结果或者是抛出的异常并进行对应的应对处理，就需要用到`handle`和`whenCompletable`方法了。

先看下两个方法的作用描述：
方法名称作用描述handle与`thenApply`类似，区别点在于handle执行函数的入参有两个，一个是`CompletableFuture`执行的实际结果，一个是**Throwable对象**，这样如果前面执行出现异常的时候，可以通过handle获取到异常并进行处理。whenComplete与`handle`类似，区别点在于`whenComplete`执行后**无返回值**。exceptionally捕获异常并返回指定值
#### [handle](#handle)

入参为 结果 或者 异常，返回新结果

结果

#### [whenComplete](#whencomplete)

whenComplete虽然得到异常信息，但是不能修改返回信息

结果

#### [exceptionally](#exceptionally)

结果

### [实现超时](#实现超时)

由于网络波动或者连接节点下线等种种问题，对于大多数网络异步任务的执行常常会进行超时限制，在异步开发中可以看成是一个常见的问题。

在 Java 9 中，`CompletableFuture` 引入了支持超时和延迟执行的改进，这两个功能对于控制异步操作行为至关重要。

#### [orTimeout()](#ortimeout)

允许为 CompletableFuture 设置一个超时时间。如果在指定的超时时间内未完成，CompletableFuture 将以 TimeoutException 完成

- 示例

#### [completeOnTimeout()](#completeontimeout)

允许在指定的超时时间内如果未完成，则用一个默认值来完成 `CompletableFuture`。该方法提供了一种优雅的回退机制，确保即使在超时的情况下也能保持异步流的连续性和完整性。

- 示例

### [延迟执行](#延迟执行)

`CompletableFuture` 提供了`delayedExecutor()` 来支持延迟执行，该方法创建一个延迟执行的 `Executor`，可以将任务的执行推迟到未来某个时间点。能够让我们更加精确地控制异步任务的执行时机，特别是在需要根据时间安排任务执行的场景中。

- 示例

## [CompletableFuture的Async版本](#completablefuture的async版本)

在使用**CompletableFuture**的时候会发现，有很多的方法，都会同时有两个以**Async**命名结尾的方法版本。以`thenCombine`方法为例：

1. thenCombine(CompletionStage, BiFunction)

1. thenCombineAsync(CompletionStage, BiFunction)

1. thenCombineAsync(CompletionStage, BiFunction, Executor)

从参数上看，区别并不大，仅第三个方法入参中多了线程池Executor对象。看下三个方法的源码实现，会发现其整体实现逻辑都是一致的，仅仅是使用线程池这个地方的逻辑有一点点的差异：
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/17106ecb2fd8-202406092159870.webp)
有兴趣的可以去翻一下此部分的源码实现，这里概括下三者的区别：

1. thenCombine方法，沿用上一个执行任务所使用的线程池进行处理

1. thenCombineAsync两个入参的方法，使用默认的ForkJoinPool线程池中的工作线程进行处理

1. themCombineAsync三个入参的方法，支持自定义线程池并指定使用自定义线程池中的线程作为工作线程去处理待执行任务。

为了更好的理解下上述的三个差异点，通过下面的代码来演示下：

- **用法1： **其中thenCombineAsync指定使用自定义线程池，supplyAsync方法不指定线程池（使用默认线程池）

没有指定自定义线程池的supplyAsync方法，其使用了默认的`ForkJoinPool`工作线程来运行，而指定了自定义线程池的方法，则使用了自定义线程池来执行。

- **用法2**： 不指定自定义线程池，使用默认线程池策略，使用thenCombine方法

执行结果如下，可以看到执行线程名称与**用法1**示例相比发生了变化。因为没有指定线程池，所以两个`supplyAsync`方法都是用的默认的`ForkJoinPool`线程池，而`thenCombine`使用的是上一个任务所使用的线程池，所以也是用的`ForkJoinPool`。

现在，我们知道了方法名称带有Async和不带Async的实现策略上的差异点就在于使用哪个线程池来执行而已。那么，对我们实际的指导意义是啥呢？实际使用的时候，应该怎么判断自己应该使用带Async结尾的方法、还是不带Async结尾的方法呢？
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/b15af753ba66-202406092200130.webp)
上面是Async结尾方法默认使用的ForkJoinPool创建的逻辑，这里可以看出，默认的线程池中的工作线程数是`CPU核数 - 1`，并且指定了默认的丢弃策略等，这就是一个主要关键点。所以说，符合以下几个条件的时候，可以考虑使用带有Async后缀的方法，指定自定义线程池：

- 默认线程池的线程数满足不了实际诉求

- 默认线程池的类型不符合自己业务诉求

- 默认线程池的队列满处理策略不满足自己诉求

## [使用注意点](#使用注意点)

### [与Stream结合](#与stream结合)

在涉及批量进行并行处理的时候，通过`Stream`与`CompletableFuture`结合使用，可以简化很多编码逻辑。但是**在使用细节方面需要注意下**，避免达不到使用`CompletableFuture`的预期效果。

**需求场景：** 在同一个平台内，传入多个商品，查询不同商品对应的价格与优惠信息，并选出实付价格最低的商品信息。

结合前面的介绍分析，我们应该知道最佳的方式，就是同时并行的方式去各自请求数据，最后合并处理即可。所以我们规划按照如下的策略来实现：
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/081b9e4e6181-202409111654500.jpeg)
先看第一种编码实现：

对于List的处理场景，这里采用了Stream方式来进行遍历与结果的收集、排序与返回。看似正常，但是执行的时候会发现，并没有达到我们预期的效果：

从上述执行结果可以看出，其具体处理的时候，其实是按照下面的逻辑去处理了：
![](/imported/markdown/2025-05-17-markdown-68d34141-completablefuture深度解析-异步编程与任务编排的实现/images/1eba18b1ef63-202409111703727.jpg)
为什么会出现这种实际与预期的差异呢？原因就在于使用的Stream上面！虽然Stream中使用两个`map`方法，但Stream处理的时候并不会分别遍历两遍，其实写法等同于下面这种写到`1个`map中处理，改为下面这种写法，其实也就更容易明白为啥会没有达到我们预期的整体并行效果了：

既然如此，这种场景是不是就不能使用Stream了呢？也不是，其实**拆开成两个Stream**分步操作下其实就可以了。

再看下面的第二种实现代码：

执行结果：

从执行结果可以看出，三个商品并行处理，整体处理耗时相比前面编码方式有很大提升，达到了预期的效果。

**归纳下**：因为Stream的操作具有**惰性执行**的特点，且只有遇到终止操作（比如collect方法）的时候才会真正的执行。所以遇到这种需要并行处理且需要合并多个并行处理流程的情况下，需要将并行流程与合并逻辑放到两个Stream中，这样分别触发完成各自的处理逻辑，就可以了。

### [使用自定义线程池](#使用自定义线程池)

`CompletableFuture` 默认使用`ForkJoinPool.commonPool()` 作为执行器，这个线程池是全局共享的，可能会被其他任务占用，导致性能下降或者饥饿。因此，建议使用自定义的线程池来执行 `CompletableFuture` 的异步任务，可以提高并发度和灵活性。

### [尽量避免使用get()](#尽量避免使用get)

`CompletableFuture`的`get()`方法是阻塞的，尽量避免使用。如果必须要使用的话，需要添加超时时间，否则可能会导致主线程一直等待，无法执行其他任务。
