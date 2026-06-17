---
title: "Mybatis 快速入门(XML方式) 底层源码对象初始化过程分析"
date: 2023-05-31
description: "导读 官网地址 https://mybatis.org/mybatis-3/zh/index.html 架构原理图 说明 mybatis配置文件 SqlMapConfig.xml，此文件为mybatis的全局配置文件，配置了mybatis的运行环境等信息 XXXMapper.xml，此文件作为myb"
tags:
  - "MyBatis"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12895291.html"
---

<h1 style="text-align: center">导读</h1>
<h2>官网地址</h2>
<p>https://mybatis.org/mybatis-3/zh/index.html</p>
<h2>架构原理图</h2>
<p><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200515233953739-783515663.png" alt="" /></p>
<h2>说明</h2>
<h3><span style="color: rgba(255, 0, 0, 1)">mybatis配置文件</span></h3>
<ol>
<li>SqlMapConfig.xml，此文件为mybatis的全局配置文件，配置了mybatis的运行环境等信息</li>
<li>XXXMapper.xml，此文件作为mybatis的sql映射文件，文件中配置了操作数据库的CRUD语句。需要在SqlMapConfig.xml中加载</li>
</ol>
<h3><span style="color: rgba(255, 0, 0, 1)">SqlSessionFactory</span></h3>
<ol>
<li>通过mybatis环境等配置信息构造SqlSessionFactory，既会话工厂</li>
</ol>
<h3><span style="color: rgba(255, 0, 0, 1)">***跟底层源码查看创建SqlSessionFactory流程***</span></h3>
<p><span style="color: rgba(255, 0, 0, 1)">注：底层如何获取标签值，请自行研究(<span style="background-color: rgba(255, 0, 0, 1); color: rgba(255, 255, 255, 1); font-size: 15px"><strong>剧透：for循环遍历XML获取标签中的值，然后放入Map</strong></span>)！~</span></p>
<p><span style="color: rgba(255, 0, 0, 1)"><img src="https://img2020.cnblogs.com/blog/1504448/202005/1504448-20200516000220224-175903583.gif" alt="" /></span></p>
<h3><span style="color: rgba(255, 0, 0, 1)">SqlSession</span></h3>
<ol>
<li>通过会员工厂创建SqlSession即会话，程序通过SqlSession会话接口对数据库进行CRUD操作。</li>
</ol>
<h3><span style="color: rgba(255, 0, 0, 1)">Executor执行器</span></h3>
<p>　　mybatis底层自定义了Executor执行器接口来具体操作数据库，Executor接口有两个实现，一个是基本执行器(默认)，一个缓存执行器，SqlSession底层是通过executor接口操作数据库</p>
<h3><span style="color: rgba(255, 0, 0, 1)">Mapped Statement</span></h3>
<p>　　他是mybatis一个底层封装对象，包装了mybatis配置信息及XXXMapper.xml映射文件等。XXXMapper.xml文件中一个个<span style="color: rgba(255, 0, 0, 1)"><strong>select/insert/update/delete标签对应一个Mapped Statement对象</strong></span>。</p>
<h2>原始JDBC代码</h2>
<p>　　原始JDBC和mybatis操作数据库数据，与上面架构图流程相对应。</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">class</span><span style="color: rgba(0, 0, 0, 1)"> JDBCTest {

    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">static</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> main(String[] args) {
        Connection connection </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
        PreparedStatement preparedStatement </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;
        ResultSet resultSet </span>= <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">;

        </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 加载数据库驱动</span>
            Class.forName("com.mysql.jdbc.Driver"<span style="color: rgba(0, 0, 0, 1)">);

            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 通过驱动管理类获取数据库链接connection = DriverManager</span>
            connection =<span style="color: rgba(0, 0, 0, 1)"> DriverManager.getConnection(
                              </span>"jdbc:mysql://localhost:3306/mybatis?characterEncoding=utf-8"<span style="color: rgba(0, 0, 0, 1)">,
                             </span>"root"<span style="color: rgba(0, 0, 0, 1)">, 
                              </span>"root"<span style="color: rgba(0, 0, 0, 1)">
                              );

            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 定义sql语句 ?表示占位符</span>
            String sql = "select * from user where username = ?"<span style="color: rgba(0, 0, 0, 1)">;
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 获取预处理 statement</span>
            preparedStatement =<span style="color: rgba(0, 0, 0, 1)"> connection.prepareStatement(sql);
            
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 设置参数，第一个参数为 sql 语句中参数的序号（从 1 开始），第二个参数为设置的</span>
            preparedStatement.setString(1, "王五"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 向数据库发出 sql 执行查询，查询出结果集</span>
            resultSet =<span style="color: rgba(0, 0, 0, 1)"> preparedStatement.executeQuery();
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 遍历查询结果集</span>
            <span style="color: rgba(0, 0, 255, 1)">while</span><span style="color: rgba(0, 0, 0, 1)"> (resultSet.next()) {
                System.out.println(
                                  resultSet.getString(</span>"id"<span style="color: rgba(0, 0, 0, 1)">) 
                                  </span>+ " " +<span style="color: rgba(0, 0, 0, 1)"> 
                                  resultSet.getString(</span>"username"<span style="color: rgba(0, 0, 0, 1)">)
                     );
            }
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception e) {
            e.printStackTrace();
        } </span><span style="color: rgba(0, 0, 255, 1)">finally</span><span style="color: rgba(0, 0, 0, 1)"> {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> 释放资源</span>
            <span style="color: rgba(0, 0, 255, 1)">if</span> (resultSet != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
                </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
                    resultSet.close();
                } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (SQLException e) {
                    e.printStackTrace();
                }
            }
            </span><span style="color: rgba(0, 0, 255, 1)">if</span> (preparedStatement != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
                </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
                    preparedStatement.close();
                } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (SQLException e) {
                    e.printStackTrace();
                }
            }
            </span><span style="color: rgba(0, 0, 255, 1)">if</span> (connection != <span style="color: rgba(0, 0, 255, 1)">null</span><span style="color: rgba(0, 0, 0, 1)">) {
                </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
                    connection.close();
                } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (SQLException e) {
                    </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)"> TODO Auto-generated catch block e.printStackTrace();</span>
<span style="color: rgba(0, 0, 0, 1)">                }
            }
        }
    }
}</span></pre>
