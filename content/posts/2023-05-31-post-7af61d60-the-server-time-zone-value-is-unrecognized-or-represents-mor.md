---
title: "The server time zone value '�й���׼ʱ��' is unrecognized or represents more than one time zone."
date: 2023-05-31
description: "介绍 再使用spring操作mysql数据库报错 @Test public void test() { try { //创建连接池，先使用spring框架内置的连接池 DriverManagerDataSource dataSource =new DriverManagerDataSource();"
tags:
  - "JAVA"
  - "Spring"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11839136.html"
---

<h1>介绍</h1>
<p>　　再使用spring操作mysql数据库报错</p>
<div class="cnblogs_code">
<pre><span style="color: rgba(0, 0, 0, 1)">    @Test
    </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> test() {
        </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)"> {
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建连接池，先使用spring框架内置的连接池</span>
            DriverManagerDataSource dataSource =<span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> DriverManagerDataSource();
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">数据库驱动程序</span>
            dataSource.setDriverClassName("com.mysql.cj.jdbc.Driver"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">数据库连接字符串</span>
            dataSource.setUrl("jdbc:mysql://localhost:3306/demo"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">账号</span>
            dataSource.setUsername("root"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">密码</span>
            dataSource.setPassword("root"<span style="color: rgba(0, 0, 0, 1)">);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建模板类</span>
            JdbcTemplate jdbcTemplate=<span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> JdbcTemplate(dataSource);
            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">完成数据的添加</span>
            <span style="color: rgba(0, 0, 255, 1)">int</span> res = jdbcTemplate.update("insert into s_user (age,name) values (?,?)",22,"测试人员"<span style="color: rgba(0, 0, 0, 1)">);
        } </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception e) {
            e.printStackTrace();
        }
    }</span></pre>
