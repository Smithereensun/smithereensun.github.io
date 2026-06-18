{

  "title": "Java 多线程并发编程",
  "date": "2020-09-30",
  "description": "导读 创作不易，禁止转载！** 并发编程简介 发展历程 早起**计算机，**从头到尾执行一个程序**，这样就严重造成**资源**的**浪费**。然后**操作系统**就**出现**了，计算机能运行多个程序，不同的程序在不同的单独的进程中运行，**一个进程**，**有多个线程**，**提高资源的利用率*",
  "tags": [
    "Java"
  ],
  "source": "cnblogs-export",
  "source_url": "https://www.cnblogs.com/chenyanbin/p/13629067.html"

}

# 导读

**创作不易，禁止转载！**

# 并发编程简介

## 发展历程

**早起**计算机，**从头到尾执行一个程序**，这样就严重造成**资源**的**浪费**。然后**操作系统**就**出现**了，计算机能运行多个程序，不同的程序在不同的单独的进程中运行，**一个进程**，**有多个线程**，**提高资源的利用率**。ok，如果以上你还不了解的话，我这里有2个脑补链接([点我直达1](https://baike.baidu.com/item/%E8%AE%A1%E7%AE%97%E6%9C%BA)、[点我直达2](https://baike.baidu.com/tashuo/browse/content?id=7e4db7414abe634e5cd90c64))

## 简介(百度百科)

　　所谓并发编程是指在一台处理器上“**同时**”**处理多个任务**。并发是在同一实体上的多个事件。多个事件在同一时间间隔发生。

## 目标(百度百科)

　　并发编程的目标是**充分**的**利用处理器的每一个核**，以达到**最高**的**处理性能**。

## 串行与并行的区别

　　可能这个**栗子不是很恰当**，**仁者见仁智者见智**。**智者****get到点**，**愚者咬文爵字**，啊！你这个栗子不行，不切合实际，巴拉巴拉 .....为啥**加起来**是**2小时6分钟**，**吃饭不要时间麽**(**洗衣服：把要洗的衣服塞到洗衣机，包括倒洗衣液等等3分钟；做饭：同理**)，你大爷的，吃饭的时候不能看电影嘛。**好了，请出门右转，这里不欢迎杠精，走之前把门关上！！！**通过这个栗子，可以看出做相同的事情，所花费的时间不同(这就是为啥**工作中**，**每个人的工作效率有高低了叭**)。

![](./images/images/img_001_61b8630f751e.png)

## 什么时候适合并发编程

1. 任务**阻塞线程**，导致之后的代码不能执行：**一边从文件中读取，一边进行大量计算**
2. 任务**执行时间过长**，可以瓜分为分工明确的子任务：**分段下载文件**
3. 任务**间断性执行**：**日志打印**
4. 任务**协作执行**：**生产者消费者问题**

## 并发编程中的上下文切换

　　以下内容，**百度百科原话**([点我直达](https://baike.baidu.com/item/%E4%B8%8A%E4%B8%8B%E6%96%87%E5%88%87%E6%8D%A2/4842616?fr=aladdin))。

　　上下文切换指的是[内核](https://baike.baidu.com/item/%E5%86%85%E6%A0%B8/108410)（操作系统的核心）在[CPU](https://baike.baidu.com/item/CPU/120556)上对进程或者线程进行切换。上下文切换过程中的信息被保存在进程控制块（PCB-Process Control Block）中。PCB又被称作切换桢（SwitchFrame）。上下文切换的信息会一直被保存在CPU的内存中，直到被再次使用。

　　上下文切换 (context switch) , 其实际含义是任务切换, 或者CPU寄存器切换。当多任务内核决定运行另外的任务时, 它保存正在运行任务的当前状态, 也就是CPU寄存器中的全部内容。这些内容被保存在任务自己的堆栈中, 入栈工作完成后就把下一个将要运行的任务的当前状况从该任务的栈中重新装入CPU寄存器, 并开始下一个任务的运行, 这一过程就是context switch。

[
![](https://bkimg.cdn.bcebos.com/pic/b8014a90f603738da977097f0e53a751f8198618461f?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1)](https://baike.baidu.com/pic/%E4%B8%8A%E4%B8%8B%E6%96%87%E5%88%87%E6%8D%A2/4842616/0/b8014a90f603738da977097f0e53a751f8198618461f?fr=lemma&ct=single)

每个任务都是整个应用的一部分, 都被赋予一定的优先级, 有自己的一套CPU寄存器和栈空间。

　　最重要的一句话：**上下文频繁的切换，会带来一定的性能开销。**

### 减少上下文切换开销方法

- 无锁并发编程

  - 多线程竞争锁时，会引起上下文切换，所以多个线程处理数据时，可以用一些办法来避免使用锁，如将数据的ID按照Hash算法取模分段，不同的线程处理不同段的数据

- CAS

  - Java的Atomic包使用CAS算法来更新数据，而不需要加锁

- 控制线程数

  - 避免创建过多不需要的线程，当任务少的时候，但是创建很多线程来处理，这样会造成大量线程都处于等待状态

协程(GO语言)

  - 在单线程里实现多任务的调度，并在单线程里维持多个任务间的切换。

知乎上，有个人写的不错，推荐给大家：[点我直达](https://zhuanlan.zhihu.com/p/110508316)

## 死锁(代码演示)

**第一次**执行，**没有发生死锁**，**第二次**执行时，先让线程A睡眠50毫秒，程序一直卡着不动，**发生死锁**。**你不让我，我不让你，争夺YB_B的资源**。

![](./images/images/img_003_015d99276ab8.gif)

### 查看死锁(**在重要不过啦**)(**jdk提供的一些工具**)

1. **命令行工具**：jps
2. **查看堆栈**：jstack pid
3. **可视化工具**：jconsole

#### jps&jstack

![](./images/images/img_004_116fb5247664.gif)

##### 分析

![](./images/images/img_005_c354e47cd2b2.png)

### jconsole

　　控制台输入：jconsole，然后按照gif，看线程->检测死锁

![](./images/images/img_006_4ccf97a33c25.gif)

### 代码拷贝区

```text
package com.yb.thread;

/**
 * @ClassName：DeadLockDemo
 * @Description：死锁代码演示
 * @Author：chenyb
 * @Date：2020/9/7 10:23 下午
 * @Versiion：1.0
 */
public class DeadLockDemo {
    private static final Object YB_A=new Object();
    private static final Object YB_B=new Object();

    public static void main(String[] args) {
        new Thread(()->{
            synchronized (YB_A){
                try {
                    //让线程睡眠50毫秒
                    Thread.sleep(50);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                synchronized (YB_B){
                    System.out.println("线程-AAAAAAAAAAAAA");
                }
            }
        }).start();
        new Thread(()->{
            synchronized (YB_B){
                synchronized (YB_A){
                    System.out.println("线程-BBBBBBBBBBBBB");
                }
            }
        }).start();
    }
}
```

# 线程基础

## 进程与线程的区别

**进程**：是**系统**进行**分配**和**管理资源**的**基本单位**

**线程**：进程的一个执行单元，是进程内调度的实体、是CPU调度和分派的基本单位，是比进程更小的独立运行的基本单位。线程也被称为轻量级进程，**线程**是**程序执行**的**最小单位**。

**一个程序至少一个进程，一个进程至少一个线程。**

## 线程的状态(**枚举**)

![](./images/images/img_007_31930ad4ff7c.gif)

- 初始化(**NEW**)

  - 新建了一个线程对象，但还没有调用start()方法

- 运行(**RUNNABLE**)

  - 处于可运行状态的线程正在JVM中执行，但他可能正在等待来自操作系统的其他资源

- 阻塞(**BLOCKED**)

  - 线程阻塞与synchronized锁，等待获取synchronized锁的状态

- 等待(**WAITING**)

  - Object.wait()、join()、LockSupport.part()，进入该状态的线程需要等待其他线程做出一些特定动作(通知|中断)

- 超时等待(**TIME_WAITING**)

  - Object.wait(long)、Thread.join()、LockSupport.parkNanos()、LockSupport.parkUntil，该状态不同于WAITING

- 终止(**TERMINATED**)

  - 该线程已经执行完毕

![](./images/images/img_008_f96cae3b6e01.gif)

![](./images/images/img_009_be4a10b144b1.gif)

## 创建线程

### 方式一

![](./images/images/img_010_5528eb1640a2.png)

### 方式二(推荐)

![](./images/images/img_011_3f439c1876c6.png)

#### 好处

1. java只能单继承，但是接口可以继承多个
2. 增加程序的健壮性，代码可以共享

#### 注意事项

![](./images/images/img_012_ecee14849581.png)

### 方式三(匿名内部类)

![](./images/images/img_013_66a4e6cecfe2.png)

### 方式四(Lambada)

![](./images/images/img_014_4ffa3814be3d.png)

### 方式五(线程池)

![](./images/images/img_015_089b7515dda3.png)

**注意：程序还未关闭！！！！**

## 线程的挂起与恢复

### 方式一(不推荐)

![](./images/images/img_016_ac64c2bf180b.gif)

　　不推荐使用，会造成死锁~

### 方式二(推荐)

![](./images/images/img_017_294692eec9f5.gif)

**wait**()：暂停执行，放弃已获得的锁，进入等待状态

**notify**()：随机唤醒一个在等待锁的线程

**notifyAll**()：唤醒所有在等待锁的线程，自行抢占CPU资源

![](./images/images/img_018_fb4716ff056d.gif)

## 线程的中断

### 方式一(不推荐)

![](./images/images/img_019_e9dd73014a31.gif)

　　注意：使用**stop()可以中断线程**，但是会带来**线程不安全**问题(stop被调用，线程立刻停止)，理论上numA和numB都是1，结果numB=0；还是没搞明白的，给你个眼神，自己体会~

### 方式二(推荐)

![](./images/images/img_020_8bba5e58cf76.gif)

### 方式三(更推荐)

![](./images/images/img_021_9a1793b5935c.gif)

## 线程优先级

　　线程的**优先级**告诉程序该**线程**的**重要程度有多大**。如果有大量线程都被阻塞，都在等候运行，程序会尽可能地先运行优先级的那个线程。但是，这并不表示优先级较低的线程不会运行。若线程的优先级较低，只不过表示它被准许的机会小一些而已。

### 线程的优先级

1. 最小=1
2. 最大=10
3. 默认=5

![](./images/images/img_022_a5a5f256ba37.gif)

### 验证

　　可以看出，打印线程2的几率比较大，因为线程优先级高。线程优先级，推荐使用(不同平台对线程的优先级支持不同)：1、5、10

![](./images/images/img_023_9a73d92c866e.gif)

## 守护线程(不建议使用)

　　任何一个守护线程都是整个程序中所有用户线程的守护者，只要有活着的用户线程，守护线程就活着。

![](./images/images/img_024_b49a6d2d4d6c.gif)

# 线程安全性

## synchronized

[点我直达](https://www.cnblogs.com/chenyanbin/p/11796709.html)

修改**普通**方法：锁住**对象的实例**

修饰**静态**方法：锁住**整个类**

修改**代码块**：锁住**一个对象*synchronized (lock)***

![](./images/images/img_025_6133ea083560.gif)

![](./images/images/img_026_03eba585b3b6.gif)

## volatile

**仅**能**修饰变量**，保证该对象的**可见性**(**多线程共享的变量**)，**不保证原子性**。

### 用途

1. 线程开关
2. 单例修改对象的实例

![](./images/images/img_027_28327eef4824.png)

# 锁

## lock的使用

![](./images/images/img_028_f7ee2c286a5a.gif)

## lock与synchronized区别

　　lock：需要手动设置加锁和释放锁

　　synchronized：托管给jvm执行

## 查看lock的实现类有哪些

![](./images/images/img_029_7427ec0f9321.gif)

## 多线程下调试

![](./images/images/img_030_ecdf2bd0ed17.gif)

　　注意看图，线程1、2、3的状态：Runnable|wailting，还没get到点的话，你真的要反思一下了

## 读写锁

**读写互斥、写写互斥、读读不互斥**

![](./images/images/img_031_594cc9d0b5ee.gif)

　　如果要想debug调试查看效果，可开2个线程，一个自增，一个输出

```text
package com.yb.thread.lock;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

/**
 * @ClassName：ReentrantReadWriteLockDemo
 * @Description：读写锁
 * @Author：chenyb
 * @Date：2020/9/26 3:14 下午
 * @Versiion：1.0
 */
public class ReentrantReadWriteLockDemo {
    private int num_1 = 0;
    private int num_2 = 0;
    private ReentrantReadWriteLock lock = new ReentrantReadWriteLock();
    //读锁
    private Lock readLock = lock.readLock();
    //写锁
    private Lock writeLock = lock.writeLock();

    public void out() {
        readLock.lock();
        try {
            System.out.println(Thread.currentThread().getName() + "num1====>" + num_1 + ";num_2======>" + num_2);
        } finally {
            readLock.unlock();
        }
    }

    public void inCreate() {
        writeLock.lock();
        try {
            num_1++;
            try {
                Thread.sleep(500L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            num_2++;
        } finally {
            writeLock.unlock();
        }
    }

    public static void main(String[] args) {
        ReentrantReadWriteLockDemo rd = new ReentrantReadWriteLockDemo();
//        for(int x=0;x<3;x++){
//            new Thread(()->{
//                rd.inCreate();
//                rd.out();
//            }).start();
//        }

        //=========读写互斥
        new Thread(() -> {
            rd.inCreate();
        }, "写").start();
        new Thread(() -> {
            rd.out();
        }, "读").start();

        //========写写互斥
        new Thread(() -> {
            rd.inCreate();
        }, "写1").start();
        new Thread(() -> {
            rd.inCreate();
        }, "写2").start();

        //==========读读不互斥
        new Thread(() -> {
            rd.out();
        }, "读1").start();
        new Thread(() -> {
            rd.out();
        }, "读2").start();
    }
}
```

## 锁降级

　　写线程获取写锁后可以获取读锁，然后释放写锁，这样写锁变成了读锁，从而实现锁降级。

　　注：**锁降级之后，写锁不会直接降级成读锁，不会随着读锁的释放而释放，因此要显示地释放写锁**。

![](./images/images/img_032_0ed9f788b6b2.gif)

### 用途

　　用于对数据比较敏感，需要在对数据修改之后，获取到修改后的值，并进行接下来的其他操作。**理论**上已经会输入依据：“num=1”，**实际多线程下没输出**，此时可以用**锁降级解决**。给你个眼神，自己体会

![](./images/images/img_033_dff950464940.gif)

```text
package com.yb.thread.lock;

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

/**
 * @ClassName：LockDegradeDemo
 * @Description：锁降级demo
 * @Author：chenyb
 * @Date：2020/9/26 10:53 下午
 * @Versiion：1.0
 */
public class LockDegradeDemo {
    private int num = 0;
    //读写锁
    private ReentrantReadWriteLock readWriteLOck = new ReentrantReadWriteLock();
    Lock readLock = readWriteLOck.readLock();
    Lock writeLock = readWriteLOck.writeLock();

    public void doSomething() {
        //写锁
        writeLock.lock();
        //读锁
        readLock.lock();
        try {
            num++;
        } finally {
            //释放写锁
             writeLock.unlock();
        }
        //模拟其他复杂操作
        try {
            Thread.sleep(2000L);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        try {
            if (num == 1) {
                System.out.println("num=" + num);
            } else {
                System.out.println(num);
            }
        } finally {
            //释放度锁
             readLock.unlock();
        }
    }

    public static void main(String[] args) {
        LockDegradeDemo ld = new LockDegradeDemo();
        for (int i = 0; i < 4; i++) {
            new Thread(() -> {
                ld.doSomething();
            }).start();
        }
    }
}
```

## 锁升级？

　　注：**从图可以看出，线程卡着，验证不存在先读后写，从而不存在锁升级这种说法**

![](./images/images/img_034_f135af990765.gif)

## StampedLock锁

### 简介

**一般应用**，都是**读多写少**，ReentrantReadWriteLock，因为**读写互斥**，所以**读时阻塞写**，**性能提不上去**。可能会使写线程饥饿

### 特点

1. **不可重入**：一个线程已经持有写锁，再去获取写锁的话，就会造成死锁
2. 支持**锁升级、降级**
3. **可**以**乐观读**也可以**悲观读**
4. 使用有限次自旋，增加锁获得的几率，避免上下文切换带来的开销，乐观读不阻塞写操作，悲观读，阻塞写

### 优点

　　相比于ReentrantReadWriteLock，**吞吐量大幅提升**

### 缺点

1. api复杂，容易用错
2. 实现原理相比于ReentrantReadWriteLock复杂的多

### demo

```text
package com.yb.thread.lock;

import java.util.concurrent.locks.StampedLock;

/**
 * @ClassName：StampedLockDemo
 * @Description：官方例子
 * @Author：chenyb
 * @Date：2020/9/26 11:37 下午
 * @Versiion：1.0
 */
public class StampedLockDemo {
    //成员变量
    private double x, y;
    //锁实例
    private final StampedLock sl = new StampedLock();

    //排它锁-写锁(writeLock)
    void move(double deltaX, double deltaY) {
        long stamp = sl.writeLock();
        try {
            x += deltaX;
            y += deltaY;
        } finally {
            sl.unlockWrite(stamp);
        }
    }

    //乐观读锁
    double distanceFromOrigin() {
        //尝试获取乐观锁1
        long stam = sl.tryOptimisticRead();
        //将全部变量拷贝到方法体栈内2
        double currentX = x, currentY = y;
        //检查在1获取到读锁票据后，锁有没被其他写线程排他性抢占3
        if (!sl.validate(stam)) {
            //如果被抢占则获取一个共享读锁(悲观获取)4
            stam = sl.readLock();
            try {
                //将全部变量拷贝到方法体栈内5
                currentX = x;
                currentY = y;
            } finally {
                //释放共享读锁6
                sl.unlockRead(stam);
            }
        }
        //返回计算结果7
        return Math.sqrt(currentX * currentX + currentY * currentY);
    }

    //使用悲观锁获取读锁，并尝试转换为写锁
    void moveIfAtOrigin(double newX, double newY) {
        //这里可以使用乐观读锁替换1
        long stamp = sl.readLock();
        try {
            //如果当前点远点则移动2
            while (x == 0.0 && y == 0.0) {
                //尝试将获取的读锁升级为写锁3
                long ws = sl.tryConvertToWriteLock(stamp);
                //升级成功后，则更新票据，并设置坐标值，然后退出循环4
                if (ws != 0L) {
                    stamp = ws;
                    x = newX;
                    y = newY;
                    break;
                } else {
                    //读锁升级写锁失败则释放读锁，显示获取独占写锁，然后循环重试5
                    sl.unlockRead(stamp);
                    stamp = sl.writeLock();
                }
            }
        } finally {
            //释放锁6
            sl.unlock(stamp);
        }
    }
}
```

# 生产者消费者模型

## Consumer.java

```text
package com.yb.thread.communication;

/**
 * 消费者
 */
public class Consumer implements Runnable {
    private Medium medium;

    public Consumer(Medium medium) {
        this.medium = medium;
    }

    @Override
    public void run() {
        while (true) {
            medium.take();
        }
    }
}
```

## Producer.java

```text
package com.yb.thread.communication;

/**
 * 生产者
 */
public class Producer implements Runnable {
    private Medium medium;

    public Producer(Medium medium) {
        this.medium = medium;
    }

    @Override
    public void run() {
        while (true) {
            medium.put();
        }
    }
}
```

## Medium.java

```text
package com.yb.thread.communication;

/**
 * 中间商
 */
public class Medium {
    //生产个数
    private int num = 0;
    //最多生产数
    private static final int TOTAL = 20;

    /**
     * 接受生产数据
     */
    public synchronized void put() {
        //判断当前库存，是否最大库存容量
        //如果不是，生产完成之后，通知消费者消费
        //如果是，通知生产者进行等待
        if (num < TOTAL) {
            System.out.println("新增库存--------当前库存" + ++num);
            //唤醒所有线程
            notifyAll();
        } else {
            try {
                System.out.println("新增库存-----库存已满" + num);
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    /**
     * 获取消费数据
     */
    public synchronized void take() {
        //判断当前库存是否不足
        //如果充足，在消费完成之后，通知生产者进行生产
        //如果不足，通知消费者暂停消费
        if (num > 0) {
            System.out.println("消费库存-------当前库存容量" + --num);
            //唤醒所有线程
            notifyAll();
        } else {
            System.out.println("消费库存--------库存不足" + num);
            try {
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
```

## 测试

![](./images/images/img_035_a7a65a797693.gif)

# 管道流通信

　　以内存为媒介，用于线程之间的数据传输

　　面向字节：PipedOutputStream、PipedInputStream

　　面向字符：PipedReader、PipedWriter

## Reader.java

```text
package com.yb.thread.communication.demo;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PipedInputStream;
import java.util.stream.Collectors;

/**
 * @ClassName：Reader
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/27 10:22 下午
 * @Versiion：1.0
 */
public class Reader implements Runnable{
    private PipedInputStream pipedInputStream;
    public Reader(PipedInputStream pipedInputStream){
        this.pipedInputStream=pipedInputStream;
    }
    @Override
    public void run() {
        if (pipedInputStream!=null){
            String collect = new BufferedReader(new InputStreamReader(pipedInputStream)).lines().collect(Collectors.joining("\n"));
            System.out.println(collect);
        }
        //关闭流
        try {
            pipedInputStream.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

## Main.java

```text
package com.yb.thread.communication.demo;

import java.io.*;

/**
 * @ClassName：Main
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/27 10:22 下午
 * @Versiion：1.0
 */
public class Main {
    public static void main(String[] args) {
        PipedInputStream pipedInputStream = new PipedInputStream();
        PipedOutputStream pipedOutputStream = new PipedOutputStream();
        try {
            pipedOutputStream.connect(pipedInputStream);
        } catch (IOException e) {
            e.printStackTrace();
        }
        new Thread(new Reader(pipedInputStream)).start();
        BufferedReader bufferedReader = null;
        try {
            bufferedReader = new BufferedReader(new InputStreamReader(System.in));
            pipedOutputStream.write(bufferedReader.readLine().getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                pipedOutputStream.close();
                if (bufferedReader!=null){
                    bufferedReader.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }

        }
    }
}
```

## 测试

![](./images/images/img_036_fa32407461ee.gif)

# Thread.join

　　线程A执行一半，需要数据，这个数据需要线程B去执行修改，B修改完成后，A才继续操作

## 演示

![](./images/images/img_037_dfac2198617a.gif)

# ThreadLocal

线程变量，是一个以ThreadLocal对象为键、任意对象为值的存储结构。

1、ThreadLocal.get: 获取ThreadLocal中当前线程共享变量的值。
		2、ThreadLocal.set: 设置ThreadLocal中当前线程共享变量的值。
		3、ThreadLocal.remove: 移除ThreadLocal中当前线程共享变量的值。
		4、ThreadLocal.initialValue: ThreadLocal没有被当前线程赋值时或当前线程刚调用remove方法后调用get方法，返回此方法值。

![](./images/images/img_038_499c38d8f529.gif)

# 原子类

## 概念

　　对多线程访问同一个变量，我们需要加锁，而锁是比较消耗性能的，JDK1.5之后，新增的原子操作类提供了一种用法简单、性能高效、线程安全地更新一个变量的方式，这些类同样位于JUC包下的atomic包下，发展到JDK1.8，该包下共有17个类，**囊括了原子更新基本类型、原子更新数组、原子更新属性、原子更新引用**。

## 1.8新增的原子类

1. DoubleAccumulator
2. DoubleAdder
3. LongAccumulator
4. LongAdder
5. Striped64

## 原子更新基本类型

### JDK1.8之前有以下几个

1. AtomicBoolean
2. AtomicInteger
3. AtomicLong
4. DoubleAccumulator
5. DoubleAdder
6. LongAccumulator
7. LongAdder

### 大致3类

1. 元老级的原子更新，方法几乎一模一样：AtomicBoolean、AtomicInteger、AtomicLong
2. 对Double、Long原子更新性能进行优化提升：DoubleAdder、LongAdder
3. 支持自定义运算：DoubleAccumulator、LongAccumulator

### 演示

#### 元老级

![](./images/images/img_039_ac92cefb83bd.gif)

#### 自定义运算

![](./images/images/img_040_731e35f3f901.gif)

## 原子更新数组

### JDK1.8之前大概有以下几个

1. AtomicIntegerArray
2. AtomicLongArray
3. AtomicReferenceArray

![](./images/images/img_041_0cc81770e101.gif)

## 原子更新属性

1. AtomicIntegerFieldUpdater
2. AtomicLongFieldUpdater
3. AtomicStampedReference
4. AtomicReferenceFieldUpdater

![](./images/images/img_042_7ee5aafefc85.gif)

## 原子更新引用

1. AtomicReference：用于对引用的原子更新
2. AtomicMarkableReference：带版本戳的原子引用类型，版本戳为boolean类型
3. AtomicStampedReference：带版本戳的原子引用类型，版本戳为int类型

![](./images/images/img_043_dd66536c1929.gif)

# 容器

## 同步容器

 　　Vector、HashTable：JDK提供的同步容器类

　　Collections.SynchronizedXXX：对相应容器进行包装

### 缺点

　　在单独使用里面的方法的时候，可以保证线程安全，但是，复合操作需要额外加锁来保证线程安全，使用Iterator迭代容器或使用for-each遍历容器，在迭代过程中修改容器会抛ConcurrentModificationException异常。想要避免出现这个异常，就必须在迭代过程持有容器的锁。但是若容器较大，则迭代的时间也会较长。那么需要访问该容器的其他线程将会长时间等待。从而极大降低性能。

　　若不希望在迭代期间对容器加锁，可以使用“克隆”容器的方式。使用线程封闭，由于其他线程不会对容器进行修改，可以避免ConcurrentModificationException。但是在创建副本的时候，存在较大性能开销。toString、hashCode、equalse、containsAll、removeAll、retainAll等方法都会隐式的Iterate，也即可能抛出ConcurrentModificationException。

![](./images/images/img_044_ef964f65025c.gif)

```text
package com.yb.thread.container;

import java.util.Iterator;
import java.util.Vector;

/**
 * @ClassName：VectorDemo
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/29 9:35 下午
 * @Versiion：1.0
 */
public class VectorDemo {
    public static void main(String[] args) {
        Vector<String> strings = new Vector<>();
        for (int i = 0; i <1000 ; i++) {
            strings.add("demo"+i);
        }
        //错误遍历
//        strings.forEach(e->{
//            if (e.equals("demo3")){
//                strings.remove(e);
//            }
//            System.out.println(e);
//        });

        //正确迭代---->单线程
//        Iterator<String> iterator = strings.iterator();
//        while (iterator.hasNext()){
//            String next = iterator.next();
//            if (next.equals("demo3")){
//                iterator.remove();
//            }
//            System.out.println(next);
//        }

        //正确迭代--->多线程
        Iterator<String> iterator = strings.iterator();
        for (int i = 0; i < 4; i++) {
            new Thread(()->{
                synchronized (iterator){
                    while (iterator.hasNext()){
                        String next = iterator.next();
                        if (next.equals("demo3")){
                            iterator.remove();
                        }
                    }
                }
            }).start();
        }
    }
}
```

## 并发容器

　　CopyOnWrite、Concurrent、BlockingQueue：根据具体场景进行设计，尽量避免使用锁，提高容器的并发访问性。

　　ConcurrentBlockingQueue：基于queue实现的FIFO的队列。队列为空，去操作会被阻塞

　　ConcurrentLinkedQueue：队列为空，取得时候就直接返回空

![](./images/images/img_045_2c0eac042251.gif)

```text
package com.yb.thread.container;

import java.util.Iterator;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * @ClassName：Demo
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/29 9:50 下午
 * @Versiion：1.0
 */
public class Demo {
    public static void main(String[] args) {
        CopyOnWriteArrayList<String> strings=new CopyOnWriteArrayList<>();
        for (int i = 0; i < 1000; i++) {
            strings.add("demo"+i);
        }
        //正常操作--->单线程
//        strings.forEach(e->{
//            if (e.equals("demo2")){
//                strings.remove(e);
//            }
//        });

        //错误操作，不支持迭代器移除元素，直接抛异常
//        Iterator<String> iterator = strings.iterator();
//        while (iterator.hasNext()){
//            String next = iterator.next();
//            if (next.equals("demo2")){
//                iterator.remove();
//            }
//        }

        //正常操作--->多线程
        for (int i = 0; i < 4; i++) {
            new Thread(()->{
                strings.forEach(e -> {
                    if (e.equals("demo2")) {
                        strings.remove(e);
                    }
                });
            }).start();
        }
    }
}
```

## LinkedBlockingQueue

　　可以作为生产者消费者的中间商(使用put、take)。

```text
package com.yb.thread.container;

import java.util.concurrent.LinkedBlockingDeque;

/**
 * @ClassName：Demo2
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/29 10:05 下午
 * @Versiion：1.0
 */
public class Demo2 {
    public static void main(String[] args) {
        LinkedBlockingDeque<String> strings = new LinkedBlockingDeque<>();
        //添加元素，3种方式
        strings.add("陈彦斌"); //队列满的时候，会抛异常
        strings.offer("陈彦斌"); //如果队列满了，直接入队失败
        try {
            strings.put("陈彦斌"); //队列满，进入阻塞状态
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        //从队列中取元素，3种方式
        String remove = strings.remove(); //会抛出异常
        strings.poll(); //在队列为空的时候，直接返回null
        try {
            strings.take(); //队列为空的时候，会进入等待状态
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
```

# 并发工具类

## CountDownLatch

1. await()：进入等待状态
2. countDown：计算器减一

### 应用场景

1. 启动三个线程计算，需要对结果进行累加

![](./images/images/img_046_b2a8df227fd2.gif)

```text
package com.yb.thread.tool;

import java.util.concurrent.CountDownLatch;

/**
 * @ClassName：CountDownLatchDemo
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/29 10:26 下午
 * @Versiion：1.0
 */
public class CountDownLatchDemo {
    public static void main(String[] args) {
        //模拟场景，学校比较，800米，跑完之后，有跨栏
        //需要先将800米跑完，在布置跨栏，要不然跑800米的选手会被累死
        CountDownLatch countDownLatch = new CountDownLatch(8);
        new Thread(()->{
            try {
                countDownLatch.await();
                System.out.println("800米比赛结束，准备清跑道，并进行跨栏比赛");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }).start();
        for (int i = 0; i < 8; i++) {
            int finalI = i;
            new Thread(()->{
                try {
                    Thread.sleep(finalI *1000L);
                    System.out.println(Thread.currentThread().getName()+"，到达终点");
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }finally {
                    countDownLatch.countDown();
                }
            }).start();
        }
    }
}
```

## CyclicBarrier

　　允许一组线程相互等待达到一个公共的障碍点，之后继续执行

### 区别

1. CountDownLatch一般用于某个线程等待若干个其他线程执行完任务之后，他才执行：不可重复使用
2. CyclicBarrier一般用于一组线程相互等待至某个状态，然后这一组线程再同时执行：可重用

![](./images/images/img_047_4492fc90094d.gif)

```text
package com.yb.thread.tool;

import java.util.concurrent.BrokenBarrierException;
import java.util.concurrent.CyclicBarrier;

/**
 * @ClassName：CyclicBarrierDemo
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/29 10:42 下午
 * @Versiion：1.0
 */
public class CyclicBarrierDemo {
    public static void main(String[] args) {
        //模拟场景：学校800米跑步，等到所有选手全部到齐后，一直跑
        CyclicBarrier cyclicBarrier=new CyclicBarrier(8);
        for (int i = 0; i < 8; i++) {
            int finalI = i;
            new Thread(()->{
                try {
                    Thread.sleep(finalI *1000L);
                    System.out.println(Thread.currentThread().getName()+",准备就绪");
                    cyclicBarrier.await();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (BrokenBarrierException e) {
                    e.printStackTrace();
                }
                System.out.println("选手已到齐，开始比赛");
            }).start();
        }
    }
}
```

## Semaphore(信号量)

　　控制线程并发数量

### 应用场景

1. 接口限流

![](./images/images/img_048_da3d007c8b84.gif)

```text
package com.yb.thread.tool;

import java.util.concurrent.Semaphore;

/**
 * @ClassName：SemaphoreDemo
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/29 11:11 下午
 * @Versiion：1.0
 */
public class SemaphoreDemo {
    public static void main(String[] args) {
        Semaphore semaphore = new Semaphore(8);
        for (int i = 0; i < 20; i++) {
            new Thread(() -> {

                try {
                    semaphore.acquire();
                    System.out.println(Thread.currentThread().getName() + ",开始执行");
                    Thread.sleep(2000L);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } finally {
                    //释放
                    semaphore.release();
                }
            }).start();
        }
    }
}
```

## Exchange

　　它提供一个同步点，在这个同步点两个线程可以交换彼此的数据(成对)。

### 应用场景

1. 交换数据

![](./images/images/img_049_bd69b09efc61.gif)

```text
package com.yb.thread.tool;

import java.util.concurrent.Exchanger;

/**
 * @ClassName：ExchangerDemo
 * @Description：TODO
 * @Author：chenyb
 * @Date：2020/9/29 11:21 下午
 * @Versiion：1.0
 */
public class ExchangerDemo {
    public static void main(String[] args) {
        Exchanger<String> stringExchanger=new Exchanger<>();
        String str1="陈彦斌";
        String str2="ybchen";
        new Thread(()->{
            System.out.println(Thread.currentThread().getName()+"--------------初始值:"+str1);
            try {
                String exchange = stringExchanger.exchange(str1);
                System.out.println(Thread.currentThread().getName()+"--------------交换:"+exchange);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        },"线程A").start();
        new Thread(()->{
            System.out.println(Thread.currentThread().getName()+"--------------初始值:"+str2);
            try {
                String exchange = stringExchanger.exchange(str2);
                System.out.println(Thread.currentThread().getName()+"--------------交换:"+exchange);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        },"线程B").start();
    }
}
```
