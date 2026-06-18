{

  "title": "Mac mysql 5.7.x 设置服务开机自启动",
  "date": "2020-12-15",
  "description": "在终端输入 输入以下内容 启动 查看启动状态 操作步骤",
  "tags": [
    "MySQL",
    "Mac"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/14137117.html"

}

# 在终端输入

```text
sudo vi /Library/LaunchDaemons/com.mysql.mysql.plist
```

# 输入以下内容

```text
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>
    <key>KeepAlive</key>
    <true/>
    <key>Label</key>
    <string>com.mysql.mysqld</string>
    <key>ProgramArguments</key>
    <array>
    <string>/usr/local/mysql/bin/mysqld_safe</string>
    <string>--user=root</string>
    </array>
  </dict>
</plist>
```

# 启动

```text
sudo launchctl load -w /Library/LaunchDaemons/com.mysql.mysql.plist
```

# 查看启动状态

```text
ps -ef|grep mysql
```

# 操作步骤

![](./images/images/img_001_26751603486f.gif)
