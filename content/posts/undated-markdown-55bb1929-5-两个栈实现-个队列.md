{

  "title": "5、两个栈实现⼀个队列",
  "has_date": false,
  "description": "题⽬描述 ⽤两个栈来实现⼀个队列，完成队列的 Push 和 Pop 操作。 队列中的元素为 int 类型。 思路及解答 栈的特性是先进后出 队列的特性是先进先出 有两个栈 stack1 , stack2 ； 如果有新的数据进⼊，那么我们可以直接 push 到 stack1 ； 如果需要取出数据，那么",
  "tags": [
    "算法"
  ],
  "source": "local-markdown-library",
  "source_path": "algorithmsguide/sword-finger-offer/queue-stack-heap/5-stackToQueue - 5、两个栈实现⼀个队列.md"

}

---

## [题⽬描述](#题目描述)

⽤两个栈来实现⼀个队列，完成队列的 Push 和 Pop 操作。 队列中的元素为 int 类型。

## [思路及解答](#思路及解答)

- 栈的特性是先进后出

- 队列的特性是先进先出

有两个栈 stack1 , stack2 ；

- 如果有新的数据进⼊，那么我们可以直接 push 到 stack1 ；

- 如果需要取出数据，那么我们优先取出 stack2 的数据，如果 stack2 ⾥⾯数据是空的，那么我们需要把所有的 stack1 的数据倒⼊ stack2 。再从 stack2 取数据。

例如：

1. push 1 --&gt; push 2

![](/imported/markdown/undated-markdown-55bb1929-5-两个栈实现-个队列/images/d41147564aea-202503161709874.png)

1. pop 1

![image-20250316170844217](/imported/markdown/undated-markdown-55bb1929-5-两个栈实现-个队列/images/5bdf1454ceaa-202503161709866.png)image-20250316170844217

1. push 3 --&gt; push 4

![](/imported/markdown/undated-markdown-55bb1929-5-两个栈实现-个队列/images/5a4450bf8476-202503161709847.png)

1. pop 2

![](/imported/markdown/undated-markdown-55bb1929-5-两个栈实现-个队列/images/b1c574aec938-202503161709761.png)
## [扩展-两个队列实现栈](#扩展-两个队列实现栈)

**队列是先进先出的规则，把一个队列中的数据导入另一个队列中，数据的顺序并没有变，并没有变成先进后出的顺序。**

所以用栈实现队列， 和用队列实现栈的思路还是不一样的，这取决于这两个数据结构的性质。

但是依然还是要用两个队列来模拟栈，只不过没有输入和输出的关系，而是另一个队列完全用来备份的！
![](/imported/markdown/undated-markdown-55bb1929-5-两个栈实现-个队列/images/a10d3f304916-202605202224918.png)

- 时间复杂度: pop为O(n)，其他为O(1)

- 空间复杂度: O(n)

优化：

其实这道题目就是用一个队列就够了。

**一个队列在模拟栈弹出元素的时候只要将队列头部的元素（除了最后一个元素外） 重新添加到队列尾部，此时再去弹出元素就是栈的顺序了。**

- 时间复杂度: pop为O(n)，其他为O(1)

- 空间复杂度: O(n)
