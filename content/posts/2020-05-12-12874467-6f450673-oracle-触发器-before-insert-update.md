{

  "title": "Oracle 触发器 before insert update",
  "date": "2020-05-12",
  "description": "场景，往A表插入数据时，A表和B表是同一类型的状态下，A表中累计的值，不能超过B表中的值(**注：往数据库插入时，不能批量执行事务！**)，利用触发器before insert update，监控状态，若超过B表中的值，抛异常",
  "tags": [
    "Oracle"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/12874467.html"

}

场景，往A表插入数据时，A表和B表是同一类型的状态下，A表中累计的值，不能超过B表中的值(**注：往数据库插入时，不能批量执行事务！**)，利用触发器before insert update，监控状态，若超过B表中的值，抛异常

```text
CREATE OR REPLACE TRIGGER "RATED_TIME_BUDGET_ITEM_TRG"
    before insert or update on Rated_time_budget_item
    for each row
      declare tmp_dw number; -- 详设
      tmp_pw number; --生设
      tmp_gw number; --非图
      sum_dw number; --合计详设
      sum_pw number; --合计生设
      sum_gw number; --合计非图
      pragma autonomous_transaction; --指定自定义事务类型，不加要不然update会报错
    begin
      if :new.id is null then
      select Rated_time_budget_item_seq.Nextval into:new.id from dual;
      select DETIAL_WORKHOUR into tmp_dw from Rated_Time_Budget_Hdr where ID=:new.RATED_TIME_BUDGET_HDR_ID; --详设工时
      select PRODU_WORKHOUR into tmp_pw from Rated_Time_Budget_Hdr where ID=:new.RATED_TIME_BUDGET_HDR_ID; --生设工时
      select GENERAL_WORKHOUR into tmp_gw from Rated_Time_Budget_Hdr where ID=:new.RATED_TIME_BUDGET_HDR_ID; --非图工时
      if (:new.S_TYPE=0) then
        SELECT NVL(SUM(BUDGET_HOUR),0)+:new.BUDGET_HOUR INTO sum_dw FROM Rated_Time_Budget_ITEM WHERE RATED_TIME_BUDGET_HDR_ID=:new.RATED_TIME_BUDGET_HDR_ID AND S_TYPE=0; --合计详设工时
      end if;
      if (:new.S_TYPE=1) then
        SELECT NVL(SUM(BUDGET_HOUR),0)+:new.BUDGET_HOUR INTO sum_pw FROM Rated_Time_Budget_ITEM WHERE RATED_TIME_BUDGET_HDR_ID=:new.RATED_TIME_BUDGET_HDR_ID AND S_TYPE=1; --合计生设工时
      end if;
      if (:new.S_TYPE=4) then
        SELECT NVL(SUM(BUDGET_HOUR),0)+:new.BUDGET_HOUR INTO sum_gw FROM Rated_Time_Budget_ITEM WHERE RATED_TIME_BUDGET_HDR_ID=:new.RATED_TIME_BUDGET_HDR_ID AND S_TYPE=4; --合计非图工时
      end if;
      if(sum_dw>tmp_dw) then
          RAISE_APPLICATION_ERROR(-20000,'新增-合计详设工时：'||sum_dw||'，超过:'||tmp_dw||'!');
      end if;
      if(sum_pw>tmp_pw) then
          RAISE_APPLICATION_ERROR(-20000,'新增-合计生设工时：'||sum_pw||'，超过:'||tmp_pw||'!');
      end if;
      if(sum_gw>tmp_gw) then
          RAISE_APPLICATION_ERROR(-20000,'新增-合计非图工时：'||sum_gw||'，超过:'||tmp_gw||'!');
      end if;
     else
        select DETIAL_WORKHOUR into tmp_dw from Rated_Time_Budget_Hdr where ID=:old.RATED_TIME_BUDGET_HDR_ID; --详设工时
        select PRODU_WORKHOUR into tmp_pw from Rated_Time_Budget_Hdr where ID=:old.RATED_TIME_BUDGET_HDR_ID; --生设工时
        select GENERAL_WORKHOUR into tmp_gw from Rated_Time_Budget_Hdr where ID=:old.RATED_TIME_BUDGET_HDR_ID; --非图工时
        if (:old.S_TYPE=0) then
          SELECT NVL(SUM(BUDGET_HOUR),0)+:new.BUDGET_HOUR into sum_dw FROM Rated_Time_Budget_ITEM WHERE RATED_TIME_BUDGET_HDR_ID=:old.RATED_TIME_BUDGET_HDR_ID AND S_TYPE=0 AND ID!=:old.id; --合计详设工时
        end if;
        if (:old.S_TYPE=1) then
          SELECT NVL(SUM(BUDGET_HOUR),0)+:new.BUDGET_HOUR into sum_pw FROM Rated_Time_Budget_ITEM WHERE RATED_TIME_BUDGET_HDR_ID=:old.RATED_TIME_BUDGET_HDR_ID AND S_TYPE=1 AND ID!=:old.id; --合计生设工时
        end if;
        if (:old.S_TYPE=4) then
          SELECT NVL(SUM(BUDGET_HOUR),0)+:new.BUDGET_HOUR into sum_gw FROM Rated_Time_Budget_ITEM WHERE RATED_TIME_BUDGET_HDR_ID=:old.RATED_TIME_BUDGET_HDR_ID AND S_TYPE=4 AND ID!=:old.id; --合计非图工时
        end if;
      if(sum_dw>tmp_dw) then
          RAISE_APPLICATION_ERROR(-20000,'修改-合计详设工时：'||sum_dw||'，超过:'||tmp_dw||'!');
      end if;
      if(sum_pw>tmp_pw) then
          RAISE_APPLICATION_ERROR(-20000,'修改-合计生设工时：'||sum_pw||'，超过:'||tmp_pw||'!');
      end if;
      if(sum_gw>tmp_gw) then
          RAISE_APPLICATION_ERROR(-20000,'修改-合计非图工时：'||sum_gw||'，超过:'||tmp_gw||'!');
      end if;
    end if;
    commit; --提交事务
  end Rated_time_budget_item_trg;
```

```text
create or replace trigger Rated_TYPE_TRI
   before
      insert or update on Rated_Time_Budget_WORK_TYPE
   for each row
declare tmp_wth number; -- 工时
   sum_wth number; --总工时
   pragma autonomous_transaction;
 begin
   if :new.id is null then
      SELECT Rated_TYPE_SEQ.Nextval  INTO :NEW.ID FROM DUAL;
      SELECT BUDGET_HOUR into tmp_wth FROM Rated_time_budget_item WHERE ID=:new.RATED_TIME_BUDGET_ITEM_ID; --工时
      SELECT NVL(SUM(WORK_TYPE_HOUR),0)+:new.WORK_TYPE_HOUR INTO sum_wth FROM Rated_Time_Budget_WORK_TYPE WHERE RATED_TIME_BUDGET_ITEM_ID=:new.RATED_TIME_BUDGET_ITEM_ID; --合计预算工时
     if(sum_wth>tmp_wth) then
          RAISE_APPLICATION_ERROR(-20000,'新增-合计预算工时：'||sum_wth||'，超过:'||tmp_wth||'!');
      end if;
   else
     SELECT BUDGET_HOUR into tmp_wth FROM Rated_time_budget_item WHERE ID=:old.RATED_TIME_BUDGET_ITEM_ID; --工时
     SELECT NVL(SUM(WORK_TYPE_HOUR),0)+:new.WORK_TYPE_HOUR INTO sum_wth FROM Rated_Time_Budget_WORK_TYPE WHERE RATED_TIME_BUDGET_ITEM_ID=:old.RATED_TIME_BUDGET_ITEM_ID AND id!=:old.id; --合计预算工时
      if(sum_wth>tmp_wth) then
          RAISE_APPLICATION_ERROR(-20000,'修改-合计预算工时：'||sum_wth||'，超过:'||tmp_wth||'!');
      end if;
   end if;
 end Rated_TYPE_TRI;
```
