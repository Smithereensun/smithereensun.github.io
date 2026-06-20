{

  "title": "2、替换空格",
  "has_date": false,
  "description": "题目描述 请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为\"We Are Happy\"，则经过替换之后的字符串为\"We%20Are%20Happy\"。 思路及解答 调⽤API函数 java ⾥⾯有可以直接使⽤的函数replace()，直接写成下⾯这样即可通过。 使用String",
  "tags": [
    "算法"
  ],
  "source": "local-markdown-library",
  "source_path": "algorithmsguide/sword-finger-offer/other/2-replaceSpace - 2、替换空格.md"

}

---

## [题目描述](#题目描述)

请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为"We Are Happy"，则经过替换之后的字符串为"We%20Are%20Happy"。

## [思路及解答](#思路及解答)

### [调⽤API函数](#调用api函数)

java ⾥⾯有可以直接使⽤的函数replace()，直接写成下⾯这样即可通过。

### [使用StringBuilder拼接](#使用stringbuilder拼接)

使用额外的空间。对字符串进行遍历，然后使用StringBuilder进行字符串的拼接，遇到空格添加`%20`，没有则直接添加。

但是这里用到了额外的空间，额外用到StringBuilder进行存储

### [不使用额外空间](#不使用额外空间)

不使用额外的空间，那么我们只能在原String上进行修改了：

1. 将字符串转换成为字符数组，遍历⼀次，统计出空格的个数。

1. 对数组进行扩容，保证空格替换成`%20`有足够的空间：初始化的⼤⼩ = 原来的字符数组⻓度 + 空格⻓度 x 2

1. 遍历⼀次，复制，当不为空格时直接复制，当为空格时，则把 %20 这三个字符复制过去。
