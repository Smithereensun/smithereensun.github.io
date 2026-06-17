---
title: "Mac 完整卸载mysql"
date: 2020-12-15
description: "依次执行 cd ~ sudo rm /usr/local/mysql sudo rm -rf /usr/local/mysql* sudo rm -rf /Library/StartupItems/MySQLCOM sudo rm -rf /Library/PreferencePanes/My* r"
tags:
  - "Mac系统"
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/14137560.html"
---

<h1>依次执行</h1>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">cd ~

sudo rm /usr/local/mysql
sudo rm -rf /usr/local/mysql*
sudo rm -rf /Library/StartupItems/MySQLCOM
sudo rm -rf /Library/PreferencePanes/My*
rm -rf ~/Library/PreferencePanes/My*
sudo rm -rf /Library/Receipts/mysql*
sudo rm -rf /Library/Receipts/MySQL*
sudo rm -rf /var/db/receipts/com.mysql.*</span></pre>
