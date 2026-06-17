---
title: "C#连接Oracle数据库字符串(引入DLL)"
date: 2023-05-31
description: "需求：从一台Oracle数据库获取数据，本以为是很简单的事情，直接将原来的SqlClient换成OracleClient调用，结果远没自己想的简单。要么安装Oracle客户端，要么安装PLSQL。网上这方面搜索后，太多的文章，还要不停的去测试。最后找个引入外部类库的方式。这个DLL其实是Oracle"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11324614.html"
---

<p>需求：从一台Oracle数据库获取数据，本以为是很简单的事情，直接将原来的SqlClient换成OracleClient调用，结果远没自己想的简单。要么安装Oracle客户端，要么安装PLSQL。网上这方面搜索后，太多的文章，还要不停的去测试。最后找个引入外部类库的方式。这个DLL其实是Oracle为C#专门提供的，在它的官方也可以下载到（不过找起来很麻烦）。</p>
<p>这里我就把这个方案和dll分享给大家。</p>
<p>链接：https://pan.baidu.com/s/17saKNnBVyDvMbt1L8lSf6A <br>提取码：sr97 <span style="color: rgba(255, 0, 255, 1)"><br></span></p>
<h2><strong><span style="color: rgba(255, 0, 255, 1)">DEMO示例</span></strong></h2>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">using</span><span style="color: rgba(0, 0, 0, 1)"> Oracle.ManagedDataAccess.Client; //引入命名空间

        </span><span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">void</span> button1_Click(<span style="color: rgba(0, 0, 255, 1)">object</span><span style="color: rgba(0, 0, 0, 1)"> sender, EventArgs e)
        {
            </span><span style="color: rgba(0, 0, 255, 1)">string</span> strSql = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">select * from s_user</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;
            DataTable dt </span>=<span style="color: rgba(0, 0, 0, 1)"> QueryDt(strSql);
        }
</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">Oracle连接字符串</span>
<span style="color: rgba(0, 0, 255, 1)">private</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">string</span> strconn = <span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(128, 0, 0, 1)">Data Source=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=172.30.0.37)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=EMES)));Persist Security Info=True;User ID=EMES_DEV;Password=EMES_DEV;</span><span style="color: rgba(128, 0, 0, 1)">"</span><span style="color: rgba(0, 0, 0, 1)">;

        </span><span style="color: rgba(0, 0, 255, 1)">private</span> DataTable QueryDt(<span style="color: rgba(0, 0, 255, 1)">string</span><span style="color: rgba(0, 0, 0, 1)"> sql)
        {
            </span><span style="color: rgba(0, 0, 255, 1)">using</span> (OracleConnection conn = <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> OracleConnection(strconn))
            {
                </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)">
                {
                    </span><span style="color: rgba(0, 0, 255, 1)">if</span> (conn.State !=<span style="color: rgba(0, 0, 0, 1)"> ConnectionState.Open)
                    {
                        conn.Open();
                    }
                    OracleDataAdapter adap </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> OracleDataAdapter(sql, conn);
                    DataTable dt </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> DataTable();
                    adap.Fill(dt);
                    </span><span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)"> dt;
                }
                </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception ex)
                {
                    </span><span style="color: rgba(0, 0, 255, 1)">return</span> <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
                }
                </span><span style="color: rgba(0, 0, 255, 1)">finally</span><span style="color: rgba(0, 0, 0, 1)">
                {
                    conn.Close();
                }
            }
        }</span></pre>
