{

  "title": "17、树的⼦结构",
  "has_date": false,
  "description": "题⽬描述 输⼊两棵⼆叉树A， B，判断B 是不是A 的⼦结构。（ps：我们约定空树不是任意⼀个树的⼦结构） 假如给定A 为{8,8,7,9,2,#,#,#,#,4,7}， B 为{8,9,2}， 2 个树的结构如下，可以看出B是A 的⼦结构: 思路及解答 双重递归法（标准解法） 使用两个递归函数： ",
  "tags": [
    "算法"
  ],
  "source": "local-markdown-library",
  "source_path": "algorithmsguide/sword-finger-offer/tree/17-hasSubtree - 17、树的⼦结构.md"

}

---

## [题⽬描述](#题目描述)

输⼊两棵⼆叉树A， B，判断B 是不是A 的⼦结构。（ps：我们约定空树不是任意⼀个树的⼦结构）

假如给定A 为{8,8,7,9,2,#,#,#,#,4,7}， B 为{8,9,2}， 2 个树的结构如下，可以看出B是A 的⼦结构:
![](/imported/markdown/undated-markdown-eca9d961-17-树的-结构/images/277d02f60bbf-202503291233833.png)
## [思路及解答](#思路及解答)

### [双重递归法（标准解法）](#双重递归法-标准解法)

使用两个递归函数：

1. `isSubStructure`：遍历树A的每个节点，寻找与树B根节点值相同的节点

1. `recur`：从匹配的节点开始，递归比较两棵树的对应节点是否相同

![](/imported/markdown/undated-markdown-eca9d961-17-树的-结构/images/1144beea3a85-202605231159771.png)

- **时间复杂度**​：O(mn)，m和n分别是树A和树B的节点数

- **空间复杂度**​：O(m)，递归栈的深度最大为树A的高度

### [迭代+递归混合法](#迭代-递归混合法)

1. 使用迭代法（栈或队列）遍历树A

1. 当找到与树B根节点值相同的节点时，切换到递归比较

1. 结合了迭代和递归的优点

![](/imported/markdown/undated-markdown-eca9d961-17-树的-结构/images/955b24cf7a4a-202605231200363.png)

- **时间复杂度**​：O(mn)

- **空间复杂度**​：O(m)，栈的空间消耗
