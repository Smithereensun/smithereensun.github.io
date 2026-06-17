---
title: "Oracle自定义数据类型"
date: 2020-03-31
description: "1 CREATE OR REPLACE FUNCTION split(p_str IN clob, 2 p_delimiter IN VARCHAR2 default (&#39;,&#39;) --分隔符，默认逗号 3 ) RETURN split_type IS 4 j INT := 0; 5"
tags:
  - "SQL"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/11677521.html"
---

<div class="cnblogs_code">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> <span style="color: rgba(0, 0, 0, 1)">CREATE OR REPLACE FUNCTION split(p_str       IN clob,
</span><span style="color: rgba(0, 128, 128, 1)"> 2</span>                                      p_delimiter IN VARCHAR2 <span style="color: rgba(0, 0, 255, 1)">default</span> (<span style="color: rgba(128, 0, 0, 1)">'</span><span style="color: rgba(128, 0, 0, 1)">,</span><span style="color: rgba(128, 0, 0, 1)">'</span>) --<span style="color: rgba(0, 0, 0, 1)">分隔符，默认逗号
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> <span style="color: rgba(0, 0, 0, 1)">                                     ) RETURN split_type IS
</span><span style="color: rgba(0, 128, 128, 1)"> 4</span>   j        INT := <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span>   i        INT := <span style="color: rgba(128, 0, 128, 1)">1</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span>   len      INT := <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span>   len1     INT := <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)">;
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">  str      clob;
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span>   my_split split_type :=<span style="color: rgba(0, 0, 0, 1)"> split_type();
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">BEGIN
</span><span style="color: rgba(0, 128, 128, 1)">11</span>   len  :=<span style="color: rgba(0, 0, 0, 1)"> LENGTH(p_str);
</span><span style="color: rgba(0, 128, 128, 1)">12</span>   len1 :=<span style="color: rgba(0, 0, 0, 1)"> LENGTH(p_delimiter);
</span><span style="color: rgba(0, 128, 128, 1)">13</span> 
<span style="color: rgba(0, 128, 128, 1)">14</span>   WHILE j &lt;<span style="color: rgba(0, 0, 0, 1)"> len LOOP
</span><span style="color: rgba(0, 128, 128, 1)">15</span>     j :=<span style="color: rgba(0, 0, 0, 1)"> INSTR(p_str, p_delimiter, i);
</span><span style="color: rgba(0, 128, 128, 1)">16</span> 
<span style="color: rgba(0, 128, 128, 1)">17</span>     IF j = <span style="color: rgba(128, 0, 128, 1)">0</span><span style="color: rgba(0, 0, 0, 1)"> THEN
</span><span style="color: rgba(0, 128, 128, 1)">18</span>       j   :=<span style="color: rgba(0, 0, 0, 1)"> len;
</span><span style="color: rgba(0, 128, 128, 1)">19</span>       str :=<span style="color: rgba(0, 0, 0, 1)"> SUBSTR(p_str, i);
</span><span style="color: rgba(0, 128, 128, 1)">20</span> <span style="color: rgba(0, 0, 0, 1)">      my_split.EXTEND;
</span><span style="color: rgba(0, 128, 128, 1)">21</span>       my_split(my_split.COUNT) :=<span style="color: rgba(0, 0, 0, 1)"> str;
</span><span style="color: rgba(0, 128, 128, 1)">22</span> 
<span style="color: rgba(0, 128, 128, 1)">23</span>       IF i &gt;=<span style="color: rgba(0, 0, 0, 1)"> len THEN
</span><span style="color: rgba(0, 128, 128, 1)">24</span> <span style="color: rgba(0, 0, 0, 1)">        EXIT;
</span><span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">      END IF;
</span><span style="color: rgba(0, 128, 128, 1)">26</span> <span style="color: rgba(0, 0, 0, 1)">    ELSE
</span><span style="color: rgba(0, 128, 128, 1)">27</span>       str := SUBSTR(p_str, i, j -<span style="color: rgba(0, 0, 0, 1)"> i);
</span><span style="color: rgba(0, 128, 128, 1)">28</span>       i   := j +<span style="color: rgba(0, 0, 0, 1)"> len1;
</span><span style="color: rgba(0, 128, 128, 1)">29</span> <span style="color: rgba(0, 0, 0, 1)">      my_split.EXTEND;
</span><span style="color: rgba(0, 128, 128, 1)">30</span>       my_split(my_split.COUNT) :=<span style="color: rgba(0, 0, 0, 1)"> str;
</span><span style="color: rgba(0, 128, 128, 1)">31</span> <span style="color: rgba(0, 0, 0, 1)">    END IF;
</span><span style="color: rgba(0, 128, 128, 1)">32</span> <span style="color: rgba(0, 0, 0, 1)">  END LOOP;
</span><span style="color: rgba(0, 128, 128, 1)">33</span> 
<span style="color: rgba(0, 128, 128, 1)">34</span> <span style="color: rgba(0, 0, 0, 1)">  RETURN my_split;
</span><span style="color: rgba(0, 128, 128, 1)">35</span> END split;</pre>
