{

  "title": "47、求1+2+3...+n",
  "has_date": false,
  "description": "题⽬描述 求 1+2+3+...+n，要求不能使⽤乘除法、 for 、 while 、 if 、 else 、 switch 、 case 等关键字及条件判断语句（ A?B:C ）。 示例 输⼊：5 输出：15 思路及解答 用for循环 这个问题，如果直接使⽤ for 循环，超级简单，重拳出击，时间",
  "tags": [
    "算法"
  ],
  "source": "local-markdown-library",
  "source_path": "algorithmsguide/sword-finger-offer/bitwise-operation/47-Sum - 47、求1+2+3...+n.md"

}

---

## [题⽬描述](#题目描述)

求 1+2+3+...+n，要求不能使⽤乘除法、 for 、 while 、 if 、 else 、 switch 、 case 等关键字及条件判断语句（ A?B:C ）。

示例
 输⼊：5
 输出：15

## [思路及解答](#思路及解答)

### [用for循环](#用for循环)

这个问题，如果直接使⽤ for 循环，超级简单，重拳出击，时间复杂度为 O(n) 。代码如下：

可是上⾯的明显违反了使⽤for 循环的原则

### [乘除法](#乘除法)

试试公式法， 1+2+3+...+(n-1)+n = n * (n+1)/2 ,

但是上⾯的做法，同样是使⽤乘法，也违反了原则，那么要不使⽤循环，也不适⽤乘法，怎么做呢？

### [递归](#递归)

递归可以模拟出循环，⼏乎所有的for 循环操作，都可以以递归的⽅式实现。每⼀次递归，我们让n 减少1，直到减少为0 。
![](/imported/markdown/undated-markdown-494cf568-47-求1-2-3-n/images/5aa4ac69d1e2-202505181432794.png)

- 时间复杂度为O(n)

- 空间复杂度也是O(n)

### [位运算乘法](#位运算乘法)

位运算乘法法：通过位运算实现乘法操作

思路：将n(n+1)用位运算实现，然后右移1位代替除以2
![](/imported/markdown/undated-markdown-494cf568-47-求1-2-3-n/images/b181d7717654-202605301129352.png)![](/imported/markdown/undated-markdown-494cf568-47-求1-2-3-n/images/17474598266f-202605301130909.png)

- 时间复杂度：O(log n) - 取决于数字的位数

- 空间复杂度：O(1)

案例解析：
