---
title: "Python文件处理"
date: 2019-06-26
description: "一、文件处理流程 1.打开文件，得到文件句柄并赋值给一个变量 2.通过句柄对文件进行操作 3.关闭文件 1 歌曲名:少女的祈祷 2 歌手:蒋雅文&amp;李逸朗 3 专辑:冬之恋人 4 张智霖 5 少女的祈祷 6 沿途与他车箱中私奔般恋爱 7 再挤逼都不放开 8 祈求在路上没任何的阻碍 9 令愉快旅"
tags:
  - "Python"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/10292288.html"
---

<p>一、文件处理流程</p>
<p>　　1.打开文件，得到文件句柄并赋值给一个变量</p>
<p>　　2.通过句柄对文件进行操作</p>
<p>　　3.关闭文件</p>
<div class="cnblogs_code"><img id="code_img_closed_ac693b0f-a734-474b-b5f0-913684e371db" class="code_img_closed" src="https://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif" alt="" /><img id="code_img_opened_ac693b0f-a734-474b-b5f0-913684e371db" class="code_img_opened" style="display: none" src="https://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif" alt="" />
<div id="cnblogs_code_open_ac693b0f-a734-474b-b5f0-913684e371db" class="cnblogs_code_hide">
<pre><span style="color: rgba(0, 128, 128, 1)"> 1</span> 歌曲名<span style="color: rgba(128, 0, 0, 1)">:少女的祈祷</span>
<span style="color: rgba(0, 128, 128, 1)"> 2</span> 歌手<span style="color: rgba(128, 0, 0, 1)">:蒋雅文</span><span style="color: rgba(0, 0, 0, 1)">&amp;李逸朗
</span><span style="color: rgba(0, 128, 128, 1)"> 3</span> 专辑<span style="color: rgba(128, 0, 0, 1)">:冬之恋人</span>
<span style="color: rgba(0, 128, 128, 1)"> 4</span> <span style="color: rgba(0, 0, 0, 1)">张智霖
</span><span style="color: rgba(0, 128, 128, 1)"> 5</span> <span style="color: rgba(0, 0, 0, 1)">少女的祈祷
</span><span style="color: rgba(0, 128, 128, 1)"> 6</span> <span style="color: rgba(0, 0, 0, 1)">沿途与他车箱中私奔般恋爱
</span><span style="color: rgba(0, 128, 128, 1)"> 7</span> <span style="color: rgba(0, 0, 0, 1)">再挤逼都不放开
</span><span style="color: rgba(0, 128, 128, 1)"> 8</span> <span style="color: rgba(0, 0, 0, 1)">祈求在路上没任何的阻碍
</span><span style="color: rgba(0, 128, 128, 1)"> 9</span> <span style="color: rgba(0, 0, 0, 1)">令愉快旅程变悲哀
</span><span style="color: rgba(0, 128, 128, 1)">10</span> <span style="color: rgba(0, 0, 0, 1)">运气两次绿灯都过渡了
</span><span style="color: rgba(0, 128, 128, 1)">11</span> <span style="color: rgba(0, 0, 0, 1)">与他再爱几公里
</span><span style="color: rgba(0, 128, 128, 1)">12</span> <span style="color: rgba(0, 0, 0, 1)">当这盏灯转红便会别离
</span><span style="color: rgba(0, 128, 128, 1)">13</span> <span style="color: rgba(0, 0, 0, 1)">凭运气决定我生死
</span><span style="color: rgba(0, 128, 128, 1)">14</span> <span style="color: rgba(0, 0, 0, 1)">祈求天地放过一双恋人
</span><span style="color: rgba(0, 128, 128, 1)">15</span> <span style="color: rgba(0, 0, 0, 1)">怕发生的永远别发生
</span><span style="color: rgba(0, 128, 128, 1)">16</span> <span style="color: rgba(0, 0, 0, 1)">从来未顺利遇上好景降临状态
</span><span style="color: rgba(0, 128, 128, 1)">17</span> <span style="color: rgba(0, 0, 0, 1)">如何能重拾信心
</span><span style="color: rgba(0, 128, 128, 1)">18</span> <span style="color: rgba(0, 0, 0, 1)">祈求天父做十分钟好人
</span><span style="color: rgba(0, 128, 128, 1)">19</span> <span style="color: rgba(0, 0, 0, 1)">赐我他的吻
</span><span style="color: rgba(0, 128, 128, 1)">20</span> <span style="color: rgba(0, 0, 0, 1)">如怜悯罪人
</span><span style="color: rgba(0, 128, 128, 1)">21</span> <span style="color: rgba(0, 0, 0, 1)">我爱主 同时亦爱一位世人
</span><span style="color: rgba(0, 128, 128, 1)">22</span> <span style="color: rgba(0, 0, 0, 1)">祈求 沿途未变心
</span><span style="color: rgba(0, 128, 128, 1)">23</span> <span style="color: rgba(0, 0, 0, 1)">请给我护荫
</span><span style="color: rgba(0, 128, 128, 1)">24</span> <span style="color: rgba(0, 0, 0, 1)">为了他
</span><span style="color: rgba(0, 128, 128, 1)">25</span> <span style="color: rgba(0, 0, 0, 1)">不懂祷告都敢祷告
</span><span style="color: rgba(0, 128, 128, 1)">26</span> <span style="color: rgba(0, 0, 0, 1)">谁愿眷顾这种信徒
</span><span style="color: rgba(0, 128, 128, 1)">27</span> <span style="color: rgba(0, 0, 0, 1)">用两手遮掩双眼专心倾诉
</span><span style="color: rgba(0, 128, 128, 1)">28</span> <span style="color: rgba(0, 0, 0, 1)">宁愿答案
</span><span style="color: rgba(0, 128, 128, 1)">29</span> <span style="color: rgba(0, 0, 0, 1)">望不到
</span><span style="color: rgba(0, 128, 128, 1)">30</span> <span style="color: rgba(0, 0, 0, 1)">唯求与他车箱中可抵达未来
</span><span style="color: rgba(0, 128, 128, 1)">31</span> <span style="color: rgba(0, 0, 0, 1)">到车毁都不放开
</span><span style="color: rgba(0, 128, 128, 1)">32</span> <span style="color: rgba(0, 0, 0, 1)">无论路上历尽任何的伤害
</span><span style="color: rgba(0, 128, 128, 1)">33</span> <span style="color: rgba(0, 0, 0, 1)">任由我决定爱不爱
</span><span style="color: rgba(0, 128, 128, 1)">34</span> <span style="color: rgba(0, 0, 0, 1)">祈求天地放过一双恋人
</span><span style="color: rgba(0, 128, 128, 1)">35</span> <span style="color: rgba(0, 0, 0, 1)">怕发生的永远别发生
</span><span style="color: rgba(0, 128, 128, 1)">36</span> <span style="color: rgba(0, 0, 0, 1)">从来未顺利遇上好景降临状态
</span><span style="color: rgba(0, 128, 128, 1)">37</span> <span style="color: rgba(0, 0, 0, 1)">如何能重拾信心
</span><span style="color: rgba(0, 128, 128, 1)">38</span> <span style="color: rgba(0, 0, 0, 1)">祈求天父做十分钟好人
</span><span style="color: rgba(0, 128, 128, 1)">39</span> <span style="color: rgba(0, 0, 0, 1)">赐我他的吻
</span><span style="color: rgba(0, 128, 128, 1)">40</span> <span style="color: rgba(0, 0, 0, 1)">如怜悯罪人
</span><span style="color: rgba(0, 128, 128, 1)">41</span> <span style="color: rgba(0, 0, 0, 1)">我爱主 同时亦爱一位爱人
</span><span style="color: rgba(0, 128, 128, 1)">42</span> <span style="color: rgba(0, 0, 0, 1)">祈求 沿途未变心
</span><span style="color: rgba(0, 128, 128, 1)">43</span> <span style="color: rgba(0, 0, 0, 1)">请给我护荫
</span><span style="color: rgba(0, 128, 128, 1)">44</span> <span style="color: rgba(0, 0, 0, 1)">为了他
</span><span style="color: rgba(0, 128, 128, 1)">45</span> <span style="color: rgba(0, 0, 0, 1)">不懂祷告都敢祷告
</span><span style="color: rgba(0, 128, 128, 1)">46</span> <span style="color: rgba(0, 0, 0, 1)">谁愿眷顾这种信徒
</span><span style="color: rgba(0, 128, 128, 1)">47</span> <span style="color: rgba(0, 0, 0, 1)">太爱他怎么想到这么恐怖
</span><span style="color: rgba(0, 128, 128, 1)">48</span> <span style="color: rgba(0, 0, 0, 1)">宁愿答案
</span><span style="color: rgba(0, 128, 128, 1)">49</span> <span style="color: rgba(0, 0, 0, 1)">望不到
</span><span style="color: rgba(0, 128, 128, 1)">50</span> <span style="color: rgba(0, 0, 0, 1)">然而天父并未体恤好人
</span><span style="color: rgba(0, 128, 128, 1)">51</span> <span style="color: rgba(0, 0, 0, 1)">到我睁开眼
</span><span style="color: rgba(0, 128, 128, 1)">52</span> <span style="color: rgba(0, 0, 0, 1)">无明灯指引
</span><span style="color: rgba(0, 128, 128, 1)">53</span> <span style="color: rgba(0, 0, 0, 1)">我爱主 为何任我身边爱人
</span><span style="color: rgba(0, 128, 128, 1)">54</span> <span style="color: rgba(0, 0, 0, 1)">离弃了我 下了车
</span><span style="color: rgba(0, 128, 128, 1)">55</span> 你怎可答允</pre>
