---
title: "使用bootstrap-select 动态加载数据不显示的问题，级联数据置为空"
date: 2020-05-26
description: "动态加载数据 $.showLoading(&#39;数据加载中&#39;);//开启遮挡层 $.ajax({ url: &quot;/PickoutStock/GetSendReceive&quot;, data: { n: no }, success: function (result) { $."
tags:
  - "JavaScript"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12963160.html"
---

<h2>动态加载数据</h2>
<div class="cnblogs_code">
<pre>                $.showLoading('数据加载中');<span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">开启遮挡层</span>
<span style="color: rgba(0, 0, 0, 1)">                $.ajax({
                    url: </span>"/PickoutStock/GetSendReceive"<span style="color: rgba(0, 0, 0, 1)">,
                    data: { n: no },
                    success: </span><span style="color: rgba(0, 0, 255, 1)">function</span><span style="color: rgba(0, 0, 0, 1)"> (result) {
                        $.hideLoading();</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">关闭遮挡层</span>
                        <span style="color: rgba(0, 0, 255, 1)">var</span> result =<span style="color: rgba(0, 0, 0, 1)"> $.parseJSON(result);
                        </span><span style="color: rgba(0, 0, 255, 1)">if</span> (result.success == "false") <span style="color: rgba(0, 0, 255, 1)">return</span><span style="color: rgba(0, 0, 0, 1)">;
                        </span><span style="color: rgba(0, 0, 255, 1)">if</span><span style="color: rgba(0, 0, 0, 1)"> (result.success) {
                            </span><span style="color: rgba(0, 0, 255, 1)">var</span> option_send = ""<span style="color: rgba(0, 0, 0, 1)">;
                            </span><span style="color: rgba(0, 0, 255, 1)">for</span> (<span style="color: rgba(0, 0, 255, 1)">var</span> i = 0; i &lt; result.listSend.length; i++<span style="color: rgba(0, 0, 0, 1)">) {
                                option_send </span>= $('&lt;option value="' + result.listSend[i].K + '"&gt;' + result.listSend[i].V + '&lt;/option&gt;'<span style="color: rgba(0, 0, 0, 1)">);
                                $(</span>'#send_receive'<span style="color: rgba(0, 0, 0, 1)">).append(option_send);
                            }
                            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">刷新</span>
                            $('#send_receive').selectpicker('refresh'<span style="color: rgba(0, 0, 0, 1)">);
                            </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">渲染</span>
                            $('#send_receive').selectpicker('render'<span style="color: rgba(0, 0, 0, 1)">);
                        }
                    },
                    error: </span><span style="color: rgba(0, 0, 255, 1)">function</span><span style="color: rgba(0, 0, 0, 1)"> () {
                        $.hideLoading();</span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">关闭遮挡层</span>
                        $.toast(result.Msg || '系统繁忙请稍后再试!', "text"<span style="color: rgba(0, 0, 0, 1)">);
                    }
                })</span></pre>
