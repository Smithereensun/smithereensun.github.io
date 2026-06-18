{

  "title": "Linux 之Mycat搭建报错 java.net.MalformedURLException: Local host name unknown: java.net.UnknownHostException",
  "date": "2020-06-19",
  "description": "搭建MyCat环境时出现 错误: 代理抛出异常错误: java.net.MalformedURLException: Local host name unknown: java.net.UnknownHostException: node04: 无法识别当前的主机名 node04 解决办法 保存，重",
  "tags": [
    "Java",
    "Linux"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13166797.html"

}

搭建MyCat环境时出现

错误: 代理抛出异常错误: java.net.MalformedURLException: Local host name unknown: java.net.UnknownHostException: node04:

无法识别当前的主机名 node04

## 解决办法

```text
1.修改network

vi /etc/sysconfig/network
追加一行：

 HOSTNAME=你的主机名（XXXX）
 如果有，请直接进行下一步

2.接着修改： HOSTS

 vi /etc/hosts
 127.0.0.1  localhost.localdomain localhost 你的主机名（XXXX）
```

## 保存，重启电脑
