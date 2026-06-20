{

  "title": "7、编写一段代码，使其必定产生死锁",
  "has_date": false,
  "description": "编写一段代码，使得这段代码必定会产生死锁 使用Thread.sleep 以下是一个经典的 Java 死锁实现，通过两个线程互相持有对方需要的锁来确保必定发生死锁： 不使用Thread.sleep 可以使用 countDownLatch来实现死锁，思路为: 新建一个count为2的 CountDown",
  "tags": [
    "算法"
  ],
  "source": "local-markdown-library",
  "source_path": "algorithmsguide/freq-algorithms/dead-lock - 7、编写一段代码，使其必定产生死锁.md"

}

---

编写一段代码，使得这段代码必定会产生死锁

## [使用Thread.sleep](#使用thread-sleep)

以下是一个经典的 Java 死锁实现，通过两个线程互相持有对方需要的锁来确保必定发生死锁：

## [不使用Thread.sleep](#不使用thread-sleep)

可以使用 countDownLatch来实现死锁，思路为:

1. 新建一个count为2的 CountDownLatch 对象 latch。

1. thread1 持有 lock1 后，调用 latch.countDown() 将计数减一，随后调用 latch.await() 等待，直到 thread2 也持有 lock2 后调用 latch.countDownd()

1. thread2 持有 lock2 后，调用 latch.countDown()将计数减一，随后调用 latch.await() 直到 thread1 调用 latch.countDown()

1. thread1 想要 lock2，但 thread2 持有了它

1. thread2 想要 lock1，但 thread1 持有了它

1. 由于互相等待对方释放锁，因此死锁发生

除此之外，也可以使用CycliBarrier

## [错误示范](#错误示范)

上述的代码无法保证死锁，因为Java 的线程调度是由操作系统决定的，线程的执行顺序是不可预测的，thread1 可能会在 thread2 运行前快速获取 lock1 和lock2，然后释放它们，从而避免死锁

所以这段代码死锁的发生概率不是 100%。这也是为什么第一种方式要使用Thread.sleep来保证两个线程都分别获得了锁
