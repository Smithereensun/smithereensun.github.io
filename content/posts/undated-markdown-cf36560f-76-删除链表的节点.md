{

  "title": "76、删除链表的节点",
  "has_date": false,
  "description": "题⽬描述 给定单向链表的头指针和⼀个要删除的节点的值，定义⼀个函数删除该节点。返回删除后的链表的头节点。 此题对⽐原题有改动 题⽬保证链表中节点的值互不相同 该题只会输出返回的链表和结果做对⽐，所以若使⽤ C 或 C++ 语⾔，你不需要 free 或 delete 被删除的节点 数据范围: &lt;",
  "tags": [
    "算法"
  ],
  "source": "local-markdown-library",
  "source_path": "algorithmsguide/sword-finger-offer/linkedlist/76-deleteNode - 76、删除链表的节点.md"

}

---

## [题⽬描述](#题目描述)

给定单向链表的头指针和⼀个要删除的节点的值，定义⼀个函数删除该节点。返回删除后的链表的头节点。

1. 此题对⽐原题有改动

1. 题⽬保证链表中节点的值互不相同

1. 该题只会输出返回的链表和结果做对⽐，所以若使⽤ C 或 C++ 语⾔，你不需要 free 或 delete 被删除的节点

数据范围:

- 0&lt;=链表节点值&lt;=10000

- 0&lt;=链表⻓度&lt;=10000

示例1

示例2

## [思路及解答](#思路及解答)

### [虚拟头节点](#虚拟头节点)

如果要删除链表⾥⾯的⼀个节点，其实就是将前置节点的next 直接指向当前节点的后置节点，这样在链表中再也找不到该节点了，也就是相当于删除了。

假设有⼀个链表，我们需要删除⾥⾯的 5 :
![](/imported/markdown/undated-markdown-cf36560f-76-删除链表的节点/images/3bef87817304-202503231330111.png)
⾸先需要判断链表头结点是不是为空，如果为空，那么就直接返回NULL，如果等于我们要找的，那么直接返回下⼀个节点引⽤即可。

如果不符合以上说的，那么我们需要新建⼀个前置节点pre ,与现在的链表连接在⼀起：
![](/imported/markdown/undated-markdown-cf36560f-76-删除链表的节点/images/8f7424f7bf43-202503231330139.png)
然后初始化⼀个 cur 节点表示当前节点，指向 head 节点：
![](/imported/markdown/undated-markdown-cf36560f-76-删除链表的节点/images/1e14202d5073-202503231330133.png)
cur 不为空， cur 和 pre 后移：
![](/imported/markdown/undated-markdown-cf36560f-76-删除链表的节点/images/73011100f1bc-202503231331982.png)
发现 cur 正是我们需要查找的 5，那么记录下 5 的下⼀个节点 1 ,也就是next :
![](/imported/markdown/undated-markdown-cf36560f-76-删除链表的节点/images/8492c6b5d19f-202503231331572.png)
cur 的 next 指向 NULL ,使⽤ pre 的 next 指向刚刚记录的 next :
![](/imported/markdown/undated-markdown-cf36560f-76-删除链表的节点/images/f3b3a2fed17b-202503231332010.png)
简化链表也就是：
![](/imported/markdown/undated-markdown-cf36560f-76-删除链表的节点/images/0f82293f0a7a-202503231332195.png)
取之前虚拟的头结点的后⼀个节点，就是删除掉之后的新链表：
![](/imported/markdown/undated-markdown-cf36560f-76-删除链表的节点/images/e0869a5dee26-202503231332191.png)
### [迭代](#迭代)

通过遍历链表找到目标节点并修改指针，维护前驱指针，当找到目标节点时修改指针跳过该节点。这个和上面方法类似，只是不同写法

- **时间复杂度**：O(n)，最坏情况下需要遍历整个链表

- **空间复杂度**：O(1)，只使用常数空间

### [递归](#递归)

当前节点是要删除的节点则返回next，否则递归处理剩余链表

- **时间复杂度**：O(n)，需要处理每个节点

- **空间复杂度**：O(n)，递归调用栈的深度
