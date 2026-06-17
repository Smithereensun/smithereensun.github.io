---
title: "ActiveMQ 持久订阅者，执行结果与初衷相违背，验证离线订阅者无效，问题解决"
date: 2023-05-31
description: "导读 最新在接触ActiveMQ，里面有个持久订阅者模块，功能是怎么样也演示不出来效果。配置参数比较简单(配置没几个参数)，消费者第一次运行时，需要指定ClientID(此时Broker已经记录离线订阅者信息)，在启动提供者，此时消息队列存在一条记录，然后在启动消费者，但是怎么样也获取不到消息，阿西"
tags:
  - "MQ"
source: "cnblogs"
source_url: "https://www.cnblogs.com/chenyanbin/p/12866452.html"
---

<h1 style="text-align: center">导读</h1>
<p>　　最新在接触<strong><span style="color: rgba(255, 0, 0, 1)">ActiveMQ</span></strong>，里面有个<span style="color: rgba(255, 0, 0, 1)"><strong>持久订阅者</strong></span>模块，<strong><span style="color: rgba(255, 0, 0, 1)">功能是怎么样也演示不出来效果</span></strong>。配置参数比较简单(配置没几个参数)，消费者第一次运行时，需要指定ClientID(<span style="color: rgba(255, 0, 0, 1)"><strong>此时Broker已经记录离线订阅者信息</strong></span>)，在启动提供者，此时消息队列存在一条记录，然后在启动消费者，但是怎么样也获取不到消息，阿西吧~~~什么鬼，百度上一大堆，都是这样步骤，消费者端，指定以下ClientID就好了，可，想要的效果死活不出来。。。。。。</p>
<h1 style="text-align: center">采坑之路</h1>
<p>废话不多说，先上代码，后面再分析</p>
<h2>消费者端代码</h2>
<div class="cnblogs_code">
<pre>    <span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span> testTopicConsumer2() <span style="color: rgba(0, 0, 255, 1)">throws</span><span style="color: rgba(0, 0, 0, 1)"> Exception {
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第一步：创建ConnectionFactory</span>
        String brokerURL = "tcp://192.168.31.215:61616"<span style="color: rgba(0, 0, 0, 1)">;
        ConnectionFactory connectionFactory </span>= <span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> ActiveMQConnectionFactory(brokerURL);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第二步：通过工厂，创建Connection</span>
        Connection connection =<span style="color: rgba(0, 0, 0, 1)"> connectionFactory.createConnection();
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">设置持久订阅的客户端ID</span>
        String clientId = "10086"<span style="color: rgba(0, 0, 0, 1)">;
        connection.setClientID(clientId);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第三步：打开链接</span>
<span style="color: rgba(0, 0, 0, 1)">        connection.start();
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第四步：通过Connection创建session</span>
        Session session = connection.createSession(<span style="color: rgba(0, 0, 255, 1)">false</span><span style="color: rgba(0, 0, 0, 1)">, Session.AUTO_ACKNOWLEDGE);
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第五步：通过session创建Consumer</span>
        Topic topic = session.createTopic("cyb-topic"<span style="color: rgba(0, 0, 0, 1)">);

        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">创建持久订阅的消费者客户端
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第一个参数是指定Topic
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第二个参数是自定义的ClientId</span>
        MessageConsumer consumer =<span style="color: rgba(0, 0, 0, 1)"> session.createDurableSubscriber(topic, clientId);
        consumer.setMessageListener(</span><span style="color: rgba(0, 0, 255, 1)">new</span><span style="color: rgba(0, 0, 0, 1)"> MessageListener() {
            @Override
            </span><span style="color: rgba(0, 0, 255, 1)">public</span> <span style="color: rgba(0, 0, 255, 1)">void</span><span style="color: rgba(0, 0, 0, 1)"> onMessage(Message message) {
                </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第七步：处理信息</span>
                <span style="color: rgba(0, 0, 255, 1)">if</span> (message <span style="color: rgba(0, 0, 255, 1)">instanceof</span><span style="color: rgba(0, 0, 0, 1)"> TextMessage){
                    TextMessage tm</span>=<span style="color: rgba(0, 0, 0, 1)">(TextMessage)message;
                    </span><span style="color: rgba(0, 0, 255, 1)">try</span><span style="color: rgba(0, 0, 0, 1)">{
                        System.out.println(tm.getText());
                    }
                    </span><span style="color: rgba(0, 0, 255, 1)">catch</span><span style="color: rgba(0, 0, 0, 1)"> (Exception e){
                        e.printStackTrace();
                    }
                }
            }
        });
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">session.commit();
        </span><span style="color: rgba(0, 128, 0, 1)">//</span><span style="color: rgba(0, 128, 0, 1)">第八步：关闭资源</span>
<span style="color: rgba(0, 0, 0, 1)">        consumer.close();
        session.close();
        connection.close();

    }</span></pre>
