{

  "title": "PriorityQueue的秘密：堆结构的高效应用与实现原理",
  "has_date": true,
  "description": "介绍 优先级队列的作用是能保证每次取出的元素都是队列中权值最小(或最大)的**。这里**元素大小的评判可以通过元素本身的自然顺序(natural ordering)，也可以通过构造时传入的比较器**(**Comparator**)。 Java中**PriorityQueue**实现了**Queue*",
  "tags": [
    "Java",
    "集合"
  ],
  "source": "local-markdown-library",
  "source_path": "java/collection/02-collection3-priorityqueue - PriorityQueue的秘密：堆结构的高效应用与实现原理.md",
  "date": "2025-05-17"

}

## [介绍](#介绍)

**优先级队列的作用是能保证每次取出的元素都是队列中权值最小(或最大)的**。这里**元素大小的评判可以通过元素本身的自然顺序(natural ordering)，也可以通过构造时传入的比较器**(**Comparator**)。

Java中**PriorityQueue**实现了**Queue**接口，不允许放入null元素；其通过堆实现，具体说是通过完全二叉树(**complete binary tree**)实现的**小顶堆**(任意一个非叶子节点的权值，都不大于其左右子节点的权值)，也就意味着可以通过数组来作为**PriorityQueue**的底层实现。
![](/imported/markdown/2025-05-17-markdown-bfe9f095-priorityqueue的秘密-堆结构的高效应用与实现原理/images/7b9e81ac9f2a-202404250853729.jpg)
## [方法剖析](#方法剖析)

### [add()和offer()](#add-和offer)

add(E e)和offer(E e)的语义相同，都是向优先队列中插入元素，只是Queue接口规定二者对插入失败时的处理不同，前者在插入失败时抛出异常，后则则会返回false。对于**PriorityQueue**这两个方法其实没什么差别。
![](/imported/markdown/2025-05-17-markdown-bfe9f095-priorityqueue的秘密-堆结构的高效应用与实现原理/images/8acbff73a86e-202404250853736.jpg)
新加入的元素可能会破坏小顶堆的性质，因此需要进行必要的调整。

这里扩容函数 grow() 类似于 ArrayList 里的 grow() 函数，就是再申请一个更大的数组，并将原数组的元素复制过去。需要注意的是siftUp(int k, E x)方法，该方法用于插入元素x并维持堆的特性。

新加入的元素x可能会破坏小顶堆的性质，因此需要进行调整。调整的过程为:

从k指定的位置开始，将x逐层与当前点的parent进行比较并交换，直到满足x &gt;= queue[parent]为止。注意这里的比较可以是元素的自然顺序，也可以是依靠比较器的顺序。

### [element()和peek()](#element-和peek)

element()和peek()的语义完全相同，都是获取但不删除队首元素，也就是队列中权值最小的那个元素，二者唯一的区别是当方法失败时前者抛出异常，后者返回null。根据小顶堆的性质，堆顶那个元素就是全局最小的那个；由于堆用数组表示，根据下标关系，0下标处的那个元素既是堆顶元素。所以**直接返回数组0下标处的那个元素即可**。
![](/imported/markdown/2025-05-17-markdown-bfe9f095-priorityqueue的秘密-堆结构的高效应用与实现原理/images/ec7f80465905-202404250853738.jpg)
### [remove()和poll()](#remove-和poll)

remove()和poll()方法的语义也完全相同，都是获取并删除队首元素，区别是当方法失败时前者抛出异常，后者返回null。由于删除操作会改变队列的结构，为维护小顶堆的性质，需要进行必要的调整。
![](/imported/markdown/2025-05-17-markdown-bfe9f095-priorityqueue的秘密-堆结构的高效应用与实现原理/images/6ebf9c05e2ac-202404250853733.jpg)
上述代码首先记录0下标处的元素，并用最后一个元素替换0下标位置的元素，之后调用siftDown()方法对堆进行调整，最后返回原来0下标处的那个元素(也就是最小的那个元素)。重点是siftDown(int k, E x)方法，该方法的作用是**从k指定的位置开始，将x逐层向下与当前点的左右孩子中较小的那个交换，直到x小于或等于左右孩子中的任何一个为止**。

### [remove(Object o)](#remove-object-o)

remove(Object o)方法用于删除队列中跟o相等的某一个元素(如果有多个相等，只删除一个)，该方法不是**Queue**接口内的方法，而是**Collection**接口的方法。由于删除操作会改变队列结构，所以要进行调整；又由于删除元素的位置可能是任意的，所以调整过程比其它函数稍加繁琐。

具体来说，remove(Object o)可以分为2种情况:

1. 删除的是最后一个元素。直接删除即可，不需要调整。

1. 删除的不是最后一个元素，从删除点开始以最后一个元素为参照调用一次siftDown()即
