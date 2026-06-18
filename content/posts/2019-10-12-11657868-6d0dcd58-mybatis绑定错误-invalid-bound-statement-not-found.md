{

  "title": "mybatis绑定错误-- Invalid bound statement (not found)",
  "date": "2019-10-12",
  "description": "错误截图 分析原因 首先，给定的异常提示信息并不精准，有多个错误原因都会抛出该异常。mybatis出现这个问题，通常是由Mapper interface和对应的xml文件的定义对应不上引起的，这时就需要仔细检查对比包名、xml中的namespace、接口中的方法名称等是否对应。我之前就因为称忘记在x",
  "tags": [
    "笔记"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/11657868.html"

}

错误截图

![](/imported/posts/2019-10-12-11657868-6d0dcd58-mybatis绑定错误-invalid-bound-statement-not-found/images/img_001_9fa3d05e0158.png)

##  分析原因

　　首先，给定的异常提示信息并不精准，有多个错误原因都会抛出该异常。mybatis出现这个问题，通常是由Mapper interface和对应的xml文件的定义对应不上引起的，这时就需要仔细检查对比包名、xml中的namespace、接口中的方法名称等是否对应。我之前就因为称忘记在xml标签的id属性中添加方法名或写错方法名而出现这个错误。

出现这个错误时，按以下步骤检查一般就会解决问题：
1：检查xml文件所在package名称是否和Mapper interface所在的包名一一对应；
2：检查xml的namespace是否和xml文件的package名称一一对应；
3：检查方法名称是否对应；
4：去除xml文件中的中文注释；
5：随意在xml文件中加一个空格或者空行然后保存。

按照以上步骤，可以捣鼓出来，我也是花了1 2个小时，捣鼓出来的，不容易呀，洗洗睡了
