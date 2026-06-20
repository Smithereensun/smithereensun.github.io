{

  "title": "Queue & Stack：实现机制与使用场景深度分析",
  "has_date": true,
  "description": "为什么不推荐使用Stack Java已不推荐使用Stack，而是推荐使用更高效的ArrayDeque 为什么不推荐使用 性能低：是因为 Stack 继承自 Vector， 而 Vector 在每个方法中都加了锁。由于需要兼容老的项目，很难在原有的基础上进行优化，因此 Vector 就被淘汰掉了，使用",
  "tags": [
    "Java",
    "集合"
  ],
  "source": "local-markdown-library",
  "source_path": "java/collection/02-collection4-queue-stack - Queue & Stack：实现机制与使用场景深度分析.md",
  "date": "2025-05-17"

}

## [为什么不推荐使用Stack](#为什么不推荐使用stack)

Java已不推荐使用Stack，而是推荐使用更高效的ArrayDeque

### [为什么不推荐使用](#为什么不推荐使用)

- 性能低：是因为 Stack 继承自 Vector， 而 Vector 在每个方法中都加了锁。由于需要兼容老的项目，很难在原有的基础上进行优化，因此 Vector 就被淘汰掉了，使用 ArrayList 和 CopyOnWriteArrayList 来代替，如果在非线程安全的情况下可以使用 ArrayList，线程安全的情况下可以使用 CopyOnWriteArrayList 。

- 破坏了原有的数据结构：栈的定义是在一端进行 push 和 pop 操作，除此之外不应该包含其他 入栈和出栈 的方法，但是 Stack 继承自 Vector，使得 Stack 可以使用父类 Vector 公有的方法。

### [为什么现在还在用](#为什么现在还在用)

但是为什么还有很多人在使用 Stack。总结了一下主要有两个原因。

- JDK 官方是不推荐使用 Stack，之所以还有很多人在使用，是因为 JDK 并没有加 deprecation 注解，只是在文档和注释中声明不建议使用，但是很少有人会去关注其实现细节

- 在笔试面试需要做算法题的时候，更多关注点是在解决问题的算法逻辑思路上，并不会关注在不同语言下 Stack 实现细节，但是对于使用 Java 语言的业务开发者，不仅需要关注算法逻辑本身，也需要关注它的实现细节

### [为什么推荐使用 Deque 接口替换栈](#为什么推荐使用-deque-接口替换栈)

如果 JDK 不推荐使用 Stack，那应该使用什么集合类来替换栈，一起看看官方的文档。
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/01e53c40f43b-202404250856058.jpg)
正如图中标注部分所示，栈的相关操作应该由 Deque 接口来提供，推荐使用 Deque 这种数据结构， 以及它的子类，例如 ArrayDeque。

使用 Deque 接口来实现栈的功能有什么好处：

- 速度比 Stack 快

![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/3760f81bdbbb-202404250856079.jpg)
这个类作为栈使用时可能比 Stack 快，作为队列使用时可能比 LinkedList 快。因为原来的 Java 的 Stack 继承自 Vector，而 Vector 在每个方法中都加了锁，而 Deque 的子类 ArrayDeque 并没有锁的开销。

- 屏蔽掉无关的方法

原来的 Java 的 Stack，包含了在任何位置添加或者删除元素的方法，这些不是栈应该有的方法，所以需要屏蔽掉这些无关的方法。声明为 Deque 接口可以解决这个问题，在接口中声明栈需要用到的方法，无需管子类是如何是实现的，对于上层使用者来说，只可以调用和栈相关的方法。

### [Stack 和 ArrayDeque的 区别](#stack-和-arraydeque的-区别)
集合类型数据结构是否线程安全Stack数组是ArrayDeque数组否
Stack 常用的方法如下所示：
操作方法入栈push(E item)出栈pop()查看栈顶peek() 为空时返回 null
ArrayDeque 常用的方法如下所示：
操作方法入栈push(E item)出栈poll() 栈为空时返回 nullpop() 栈为空时会抛出异常查看栈顶peek() 为空时返回 null
## [Queue介绍](#queue介绍)

Java里有一个叫做Stack的类，却没有叫做Queue的类(它是个接口名字)。当需要使用栈时，Java已不推荐使用Stack，而是推荐使用更高效的ArrayDeque；既然Queue只是一个接口，当需要使用队列时也就首选ArrayDeque了(次选是LinkedList)。

### [Queue](#queue)

Queue接口继承自Collection接口，除了最基本的Collection的方法之外，它还支持额外的insertion, extraction和inspection操作。这里有两组格式，共6个方法，一组是抛出异常的实现；另外一组是返回值的实现(没有则返回null)。
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/02af11436415-202404250856302.gif)
### [Deque](#deque)

Deque 是"double ended queue", 表示双向的队列，英文读作"deck". Deque 继承自 Queue接口，除了支持Queue的方法之外，还支持 insert , remove 和 examine操作，由于Deque是双向的，所以可以对队列的头和尾都进行操作，它同时也支持两组格式，一组是抛出异常的实现；另外一组是返回值的实现(没有则返回null)。共12个方法如下:
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/b974724d13d1-202404250856307.gif)
当把 Deque 当做FIFO的 queue 来使用时，元素是从 deque 的尾部添加，从头部进行删除的； 所以 deque 的部分方法是和 queue 是等同的。具体如下:
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/2ae4d9ab67da-202404250856311.gif)
Deque的含义是“double ended queue”，即双端队列，它既可以当作栈使用，也可以当作队列使用。下表列出了Deque与Queue相对应的接口:
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/0a06847b459b-202404250856322.gif)
下表列出了Deque与Stack对应的接口:
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/c2498eca746e-202404250856314.gif)
上面两个表共定义了Deque的12个接口。添加，删除，取值都有两套接口，它们功能相同，区别是对失败情况的处理不同。一套接口遇到失败就会抛出异常，另一套遇到失败会返回特殊值( false 或 null )。除非某种实现对容量有限制，大多数情况下，添加操作是不会失败的。虽然Deque的接口有12个之多，但无非就是对容器的两端进行操作，或添加，或删除，或查看。

ArrayDeque和LinkedList是Deque的两个通用实现，由于官方更推荐使用AarryDeque用作栈和队列，加之上一篇已经讲解过LinkedList，本文将着重讲解ArrayDeque的具体实现

从名字可以看出ArrayDeque底层通过数组实现，为了满足可以同时在数组两端插入或删除元素的需求，该数组还必须是循环的，即循环数组(circular array)，也就是说数组的任何一点都可能被看作起点或者终点。ArrayDeque是非线程安全的(not thread-safe)，当多个线程同时使用的时候，需要程序员手动同步；另外，该容器不允许放入 null 元素。
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/e717fcc37d08-202404250856328.jpg)
上图中我们看到， head 指向首端第一个有效元素， tail 指向尾端第一个可以插入元素的空位。因为是循环数组，所以 head 不一定总等于0， tail 也不一定总是比 head 大。

## [方法剖析](#方法剖析)

### [addFirst()](#addfirst)

addFirst(E e)的作用是在Deque的首端插入元素，也就是在head的前面插入元素，在空间足够且下标没有越界的情况下，只需要将elements[--head] = e即可。
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/4c6678a3dba6-202404250856996.jpg)
实际需要考虑:

1. 空间是否够用

1. 下标是否越界的问题

上图中，如果head为0之后接着调用addFirst()，虽然空余空间还够用，但head为-1，下标越界了。

**上述代码可以看到， 空间问题是在插入之后解决的；**首先，因为tail总是指向下一个可插入的空位，也就意味着elements数组至少有一个空位，所以插入元素的时候不用考虑空间问题。

下标越界的处理解决起来非常简单，head = (head - 1) & (elements.length - 1)就可以了，**这段代码相当于取余，同时解决了head为负值的情况**。因为elements.length必需是2的指数倍，elements - 1就是二进制低位全1，跟head - 1相与之后就起到了取模的作用，如果head - 1为负数(其实只可能是-1)，则相当于对其取相对于elements.length的补码。

计算机里数值都是用补码表示的，如果是8位的，-1就是1111 1111，而 (elements.length - 1) 也是 1111 1111，因此两者相与也就是(elements.length - 1)；

head = (head - 1) & (elements.length - 1) 最后再让算出的位置赋值给head，因此其实这段代码就是让head再从后往前赋值

扩容函数doubleCapacity()，其逻辑是申请一个更大的数组(原数组的两倍)，然后将原数组复制过去。过程如下图所示:
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/0e6591575e16-202404250856017.jpg)
图中可以看到，复制分两次进行，第一次复制head右边的元素，第二次复制head左边的元素。

### [addLast()](#addlast)

addLast(E e)的作用是在**Deque**的尾端插入元素，也就是在tail的位置插入元素，由于tail总是指向下一个可以插入的空位，因此只需要elements[tail] = e;即可。插入完成后再检查空间，如果空间已经用光，则调用doubleCapacity()进行扩容。
![](/imported/markdown/2025-05-17-markdown-199a7b2f-queue-stack-实现机制与使用场景深度分析/images/11b85f9dff5a-202404250856038.jpg)
### [pollFirst()](#pollfirst)

pollFirst()的作用是删除并返回**Deque**首端元素，也即是head位置处的元素。如果容器不空，只需要直接返回elements[head]即可，当然还需要处理下标的问题。由于ArrayDeque中不允许放入null，当elements[head] == null时，意味着容器为空。

### [pollLast()](#polllast)

pollLast()的作用是删除并返回Deque尾端元素，也即是tail位置前面的那个元素。

### [peekFirst()](#peekfirst)

peekFirst()的作用是返回但不删除**Deque**首端元素，也即是head位置处的元素，直接返回elements[head]即可。

### [peekLast()](#peeklast)

peekLast()的作用是返回但不删除**Deque**尾端元素，也即是tail位置前面的那个元素。
