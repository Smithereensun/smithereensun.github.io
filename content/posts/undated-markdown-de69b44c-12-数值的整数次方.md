{

  "title": "12、数值的整数次方",
  "has_date": false,
  "description": "题⽬描述 给定⼀个 double 类型的浮点数 base 和 int 类型的整数 exponent 。求 base 的exponent 次⽅。保证 base 和 exponent 不同时为 0 。 示例1: 输⼊：2.00000,3 返回值：8.00000 示例2: 输⼊：2.10000,3 返回值",
  "tags": [
    "算法"
  ],
  "source": "local-markdown-library",
  "source_path": "algorithmsguide/sword-finger-offer/bitwise-operation/12-power - 12、数值的整数次方.md"

}

---

## [题⽬描述](#题目描述)

给定⼀个 double 类型的浮点数 base 和 int 类型的整数 exponent 。求 base 的exponent
 次⽅。保证 base 和 exponent 不同时为 0 。

示例1:
 输⼊：2.00000,3
 返回值：8.00000

示例2:
 输⼊：2.10000,3
 返回值：9.26100

## [思路及解答](#思路及解答)

### [暴力求解](#暴力求解)

如果使⽤暴⼒解答，那么就是不断相乘，对于负数⽽⾔，则是相除，并且符号取反。

### [拆解递归](#拆解递归)

题⽬中的 double 类型不能拆解，但是 int 类型的整数 exponet 可以做点⽂章，我们平时求次⽅的时候，假设有个 x 的 4 次⽅，我们通常是求出⼀个 x 的平⽅数 x^2，然后两个 x^2相乘就可以得出 x^4 。

对于xⁿ，可以分解为：

- 如果n为偶数：xⁿ = xⁿ/² * xⁿ/²

- 如果n为奇数：xⁿ = x * xⁿ/² * xⁿ/²

这⾥思路也⼀样，使⽤递归，同时考虑边界条件。如果指数是负数，则先取反，最后取结果的倒数即可。
![](/imported/markdown/undated-markdown-de69b44c-12-数值的整数次方/images/844b1e51aeb3-202503221105709.png)

- 时间复杂度： O(logn)，每次计算后规模缩⼩⼀半

- 空间复杂度： O(logn)，递归的时候，栈需要⽤到变量

### [迭代快速幂算法](#迭代快速幂算法)

将指数表示为二进制形式，通过位运算减少乘法次数。例如，计算3¹³（1101₂）可以分解为3⁸ * 3⁴ * 3¹。
![](/imported/markdown/undated-markdown-de69b44c-12-数值的整数次方/images/0195b8d79458-202605301125891.png)![](/imported/markdown/undated-markdown-de69b44c-12-数值的整数次方/images/952912cf6a76-202605301126657.png)
### [Java标准库](#java标准库)
