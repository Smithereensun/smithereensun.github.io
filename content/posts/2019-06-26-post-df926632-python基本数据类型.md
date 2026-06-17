---
title: "Python基本数据类型"
date: 2019-06-26
description: "•数字 int -int 将字符串转数字 a=&quot;123&quot; b=int(a) b=b+1000 查看数据类型 type() print(type(a)) 进制转换 num = &quot;a&quot; v = int(num, base=16) print(v) -bit_len"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10217353.html"
---

<p>•数字 int</p>
<p>　　-int</p>
<p>　　　　将字符串转数字</p>
<p>　　　　&nbsp; &nbsp;a="123"</p>
<p>　　　　&nbsp; &nbsp;b=int(a)</p>
<p>　　　　&nbsp; &nbsp;b=b+1000</p>
<p>　　　　查看数据类型 type()</p>
<p>　　　　&nbsp; &nbsp;print(type(a))&nbsp;</p>
<p>　　　　进制转换</p>
<p>　　　　num = "a"</p>
<p>　　　　v = int(num, base=16)</p>
<p>　　　　print(v)</p>
<p>　　-bit_lenght(1字节=8位) 此函数代表当前数字二进制，用几位来表示</p>
<p>　　　　age=5</p>
<p>　　　　#1　　1</p>
<p>　　　　#2　　10</p>
<p>　　　　#3　　11</p>
<p>　　　　#4　　100</p>
<p>　　　　#5　　101</p>
<p>　　　　r = age.bit_lenght()</p>
<p>　　　　print(r)　　 打印结果为3</p>
<p>•字符串 str (注：字符串一旦创建，不可修改；一旦修改或者拼接，都会造成重新生成字符串)</p>
<p>　　-capitalize() 首字母大写</p>
<p>　　　　test = "alex"</p>
<p>　　　　v = test.capitalize()</p>
<p>　　　　print(v)　　打印结果：Alex</p>
<p>　　-casefold()和lower() 前者更厉害，很多未知的对应关系变小写</p>
<p>　　　　test = "aLex"</p>
<p>　　　　v = test.casefold()&nbsp; 或者&nbsp;v = test.lower()&nbsp;</p>
<p>　　　　print(v)&nbsp;　　打印结果：alex</p>
<p>　　-center() 设置宽度，并将内容居中</p>
<p>　　-ljust()</p>
<p>　　　　test = "alex"</p>
<p>　　　　v = test.ljust(20,"*")</p>
<p>　　　　print(v)　　打印结果:alex******</p>
<p>　　-rjust()</p>
<p>　　　　test = "alex"</p>
<p>　　　　v = test.rjust(20,"*")</p>
<p>　　　　print(v)　　打印结果:*****alex</p>
<p>　　-count() 计算在一个字符中出现的次数</p>
<p>　　　　test = "alexalexr"</p>
<p>　　　　v = test.count('e')</p>
<p>　　　　print(v)</p>
<p>　　-startswith() 返回一个布尔值，以什么开始</p>
<p>　　-endswith() 返回一个布尔值，以什么结尾</p>
<p>　　　　test = "ales"</p>
<p>　　　　v = test.endswith('a')</p>
<p>　　　　print(v)　　打印结果为：false</p>
<p>　　-find() 从开始往后找，找到第一个之后，返回其位置，从0开始数</p>
<p>　　　　test = "alexalex"</p>
<p>　　　　v = test.find('ex')</p>
<p>　　　　print(v)　　打印结果为：2</p>
<p>　　-format() 格式化，将一个字符串中的占位符替换指定的值</p>
<p>　　　　test = " i am {name}, age {a}"</p>
<p>　　　　v = test.format(name='alex',a=15)</p>
<p>　　　　print(v)　　打印结果为：i am alex,age 19</p>
<p>　　-format_map()</p>
<p>　　　　test = "i am {name},age {a}"</p>
<p>　　　　v = test.format_map({"name": 'alex',"a": 19})</p>
<p>　　　　print(v)　　打印结果为：i am alex,age 19</p>
<p>　　-isalnum 返回一个布尔值，字符串中只能出现字符或数字</p>
<p>　　-isalpha() 返回一个布尔值，字符串中只能出现字母或中文</p>
<p>　　-isdecimal()和isdigit()和isnumeric() 返回一个布尔值，字符串中只能出现数字,两个区别在于有些支持，有些不支持</p>
<p>　　-isidentifier() 返回一个布尔值，是否为标识符：数字、字母、下划线</p>
<p>　　-islower()和lower()&nbsp;前者返回一个布尔值，字符串中是否小写，后者将字符串全部转换为小写</p>
<p>　　- isprintable() 返回一个布尔值，字符串中是否有不可显示的内容，比如：\t \n</p>
<p>　　-isspace 返回一个布尔值，字符串中是否全部都是空格</p>
<p>　　-istitle()和tile() 前者判断是否为标题样式(每个单词首字母大写)，后者将字符串转换为标题样式</p>
<p>　　-join() 将字符串中的每一个元素按照指定分隔符进行拼接</p>
<p>　　　　test = "你是风儿我是沙"</p>
<p>　　　　t = ' '</p>
<p>　　　　v = t.join(test)</p>
<p>　　　　print(v)</p>
<p>　　-strip()和lstrip()和rstrip() 去除字符串中的空格，还可以去除\r或\t，还可以指定去除的字符</p>
<p>　　　　test = "alex"</p>
<p>　　　　v = test.strip("a")</p>
<p>　　　　print(v)</p>
<address>　　-maketrans()和translate() 替换和转义</address>
<p>　　　　v = "abcdefghijklmnopqrstuvwxyz"</p>
<p>　　　　m = str.maketrans("aeiou", "12345")</p>
<p>　　　　new_v = v.translate(m)</p>
<p>　　　　print(new_v)</p>
<p>　　-partition()和rpartition()和split()和rsplit() 字符串分割(前两者分割3份，后两者分割除分割的字符之外的)</p>
<p>　　-startswith()和endswith() 返回一个布尔值，判断字符是否以XXX开始或结尾</p>
<p>　　-swapcase() 大小写互换</p>
<p>&nbsp;　　-len() 获取字符串中当前的长度,返回的是一个int值</p>
<p>　　　　test = "alex"</p>
<p>　　　　v = len(test)</p>
<p>　　　　pirnt(v)</p>
<p>　　-replace() 替换字符串</p>
<p>&nbsp;　　　　test = "alex"</p>
<p>　　　　v = test.replace("e", "bb")</p>
<p>　　　　print(v)</p>
<p>　　-range() 创建连续的数字，默认从0开始计数，还可以设置步长，第三个参数;range(0,100,5)</p>
<p>•列表 list：有序，元素可以被修改</p>
<p>　　-apend() 追加</p>
<p>　　　　li = [11,22,33]</p>
<p>　　　　li.apend(44)</p>
<p>　　　　print(li)</p>
<p>　　-clear() 清空列表</p>
<p>　　-copy() 复制/拷贝</p>
<p>　　　　v = li.copy()</p>
<p>　　　　print(v)</p>
<p>　　-count() 计算元素在列表中出现的次数</p>
<p>　　　　v = li.count(11)</p>
<p>　　　　print(v)</p>
<p>　　-extend() 扩展原列表,参数：可迭代对象</p>
<p>　　　　li.extend("465")</p>
<p>　　　　print(li)</p>
<p>　　-index() 根据值，获取当前值所在的位置,返回的是一个int类型的</p>
<p>　　　　v = li.index(22)</p>
<p>　　　　print(v)</p>
<p>　　-insert() 在指定索引位置插入元素</p>
<p>　　　　li.insert(0,"44")</p>
<p>　　-pop() 和 remove() 删除元素</p>
<p>　　　　li = [11,22,33,44]</p>
<p>　　　　v = li.pop()</p>
<p>　　　　v = li.pop(2) 指定删除的索引</p>
<p>　　　　print(li) 查看li列表，默认删除的为最后一个值</p>
<p>　　　　print(v) 查看被删除的值</p>
<p>　　-reverse() 将当前列表进行翻转</p>
<p>　　-sort() 排序，默认从小到大排序，参数 reverse=True 从大到小排序</p>
<p>•元祖 tuple :一级元祖不可被修改，不能被增加或者删除，二级元祖可以修改</p>
<p>　　#列表</p>
<p>　　li = [11, 22, 33, 44, 55]</p>
<p>　　#元祖</p>
<p>　　tu = (11, 22, 33, 44, 55,)</p>
<p>　　-count() 获取元祖中指定元素的个数</p>
<p>　　-index 找到元祖中元素的索引，从0开始计数</p>
<p>•字典 dict :</p>
<p>　　特点:</p>
<p>　　1、键值对</p>
<p>　　2、列表、字典不能作为字典的Key</p>
<p>　　3、字典无需</p>
<p>　　-del 删除</p>
<p>　　　　info = {"k1": "v1","k2": "v2"}</p>
<p>　　　　del info["k1"]</p>
<p>　　　　print(info)</p>
<p>　　-get()获取值</p>
<p>　　　　dic = {"k1": "v1"}</p>
<p>　　　　v = dic.get("k1") / v = dic.get("k2", 456) 如果键值对中没有这个键，返回一个默认值</p>
<p>　　　　print(v)</p>
<p>　　-pop() 删除</p>
<p>　　　　dic = {"k1": "v1","k2": "v2"}</p>
<p>　　　　v = dic.pop("k1")</p>
<p>　　　　print(dic,v) 此处的v，是 values</p>
<p>　　-popitem() 随机删除某一个值</p>
<address>　　-setdefault() 设置值，如果已经存在，不设置，获取当前key对应的值,不存在，设置，获取当前key对应的values值<strong><br></strong></address><address>　　　　dic = {"k1": "v1"}</address><address>　　　　v = dic.setdefault("k22","456")</address><address>　　　　print(dic, v)</address><address>　　-update()&nbsp; 获取值；如果已经存在，更新；不存在，则插入</address><address>　　　　dic = {"k1": "v1", "k2": "v2"}</address><address>　　　　dic.update({"k1": "111", "k3": "222"})&nbsp; / dic.update(k1=123. k2=456)</address><address>　　　　print(dic)</address>
<p>　　获取values值</p>
<p>　　for item in info.values():</p>
<p>　　　　print(info)</p>
<p>　　获取键值对</p>
<p>　　for k,v in info.items():</p>
<p>　　　　print(k,v)</p>
<p>•布尔值 bool</p>
