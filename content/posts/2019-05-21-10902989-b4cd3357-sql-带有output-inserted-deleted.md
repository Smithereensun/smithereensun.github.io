{

  "title": "SQL 带有output、inserted、deleted",
  "date": "2019-05-21",
  "description": "因需求的关系需要将修改的值返回,故查了些资料发现了OUTPUT这个好东西,现记录下来以防以后忘记 使用例子: 对于INSERT,可以引用inserted表以查询新行的属性. insert into [表名] (a) OUTPUT Inserted.a values ('a') 对于DELETE,可以",
  "tags": [
    "SQL"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/10902989.html"

}

因需求的关系需要将修改的值返回,故查了些资料发现了OUTPUT这个好东西,现记录下来以防以后忘记 

使用例子: 
1.对于INSERT,可以引用inserted表以查询新行的属性. 
   insert into [表名] (a) OUTPUT Inserted.a values ('a')      
2.对于DELETE,可以引用deleted表以查询旧行的属性. 
   delete [表名] OUTPUT deleted.a where links = 'a' 
3.对于UPDATE,使用deleted表查询被更新行在更改前的属性,用inserted表标识被更新行在更改后的值. 
   update [表名] set a = 'b' OUTPUT Inserted.a where a = 'a'(返回修改后的值) 
   update [表名] set a = 'b' OUTPUT deleted.a where a = 'a' (返回修改前的值)
