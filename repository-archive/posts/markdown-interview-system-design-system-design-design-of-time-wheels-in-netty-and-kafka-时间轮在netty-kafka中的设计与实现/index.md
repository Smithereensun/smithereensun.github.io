{

  "title": "时间轮在Netty,Kafka中的设计与实现",
  "has_date": false,
  "description": "本文基于 Netty 4.1.112.Final , Kafka 3.9.0 版本进行讨论 在业务开发的场景中，我们经常会遇到很多定时任务的需求。比如，生成业务报表，周期性对账，同步数据，订单支付超时处理等。针对业务场景中定时任务逻辑复杂，执行时间长的特点，市面上已经有很多成熟的任务调度中间件可供我",
  "tags": [
    "面试",
    "系统设计",
    "Kafka"
  ],
  "source": "local-markdown-library",
  "source_path": "interview/system-design/system-design/Design-of-Time-Wheels-in-Netty-and-Kafka - 时间轮在Netty,Kafka中的设计与实现.md"

}

---

本文基于 Netty 4.1.112.Final , Kafka 3.9.0 版本进行讨论

在业务开发的场景中，我们经常会遇到很多定时任务的需求。比如，生成业务报表，周期性对账，同步数据，订单支付超时处理等。针对业务场景中定时任务逻辑复杂，执行时间长的特点，市面上已经有很多成熟的任务调度中间件可供我们选择。比如：ElasticJob , XXL-JOB , PowerJob 等等。

而在中间件的场景中，同样也存在很多定时任务的需求。比如，网络连接的心跳检测，网络请求超时或失败的重试机制，网络连接断开之后的重连机制。和业务场景不同的是，这些中间件场景的定时任务特点是逻辑简单，执行时间非常短，而且对时间精度的要求比较低。比如，心跳检测以及失败重试这些定时任务，其实晚执行个几十毫秒或者 100 毫秒也无所谓。

于是针对中间件场景中的这些定时任务特点：

1.
海量任务

1.
任务逻辑简单

1.
执行时间短

1.
对任务调度的及时性没有那么高的要求

各大中间件设计了时间轮来调度具有上述 4 种特征的定时任务，而本文主要讨论的就是时间轮的设计与实现。但在这之前我们需要搞清楚时间轮这个设计需求是怎么产生的，我们先从 JDK 中的任务调度组件开始聊起，看看 JDK 中的这些任务调度组件为什么不能满足中间件的场景。

## [JDK 中的任务调度组件](#jdk-中的任务调度组件)

说到定时任务，我们第一时间就能想到的调度组件就是 JDK 中的 Timer，为什么这么说呢，因为笔者刚参加工作时的第一个任务就是用 Timer 实现的，当时对 Java 一无所知，完全零基础。主管交给我一个定时任务的需求，两眼抹黑。于是带着清澈而又稚嫩的眼神到网上一顿搜索，找到了这个 Timer，如获至宝。

### [Timer](#timer)

Timer 中有两个核心组件，一个是用于调度延时任务的 TimerThread，另一个是 TaskQueue，用于组织延时任务。它是一个优先级队列，其底层是一个数组实现的小根堆。

`

TaskQueue 会将所有延时任务按照它们的 ExecutionTime，由近到远的组织在小根堆中，堆顶永远存放的是 ExecutionTime 最近的延时任务。

TimerThread 会不断的从 TaskQueue 中获取堆顶任务，如果堆顶任务的 ExecutionTime 已经达到 —— `executionTime &lt;= currentTime` , 则执行任务。如果该任务是一个周期性任务，则将任务重新放入到 TaskQueue 中。

如果堆顶任务的 ExecutionTime 还没有到达，那么 TimerThread 就会等待 `executionTime - currentTime` 的时间，一直到堆顶任务的执行时间到达，TimerThread 被重新唤醒执行堆顶任务。

根据以上 Timer 的核心实现，我们可以总结出 Timer 在应对中间件场景的延时任务时，有以下四种不足：

1. 首先用于组织延时任务的 TaskQueue 本质上是一个小根堆。对于堆这种数据结构来说，添加，删除一个延时任务时，堆都要向上，向下调整以便满足小根堆的特性。单次操作的时间复杂度为 `O(logn)`。显然在面对海量定时任务的添加，删除时，性能上还是差点意思。

1. Timer 调度框架中只有一个 TimerThread 线程来负责延时任务的调度，执行。在面对海量任务的时候，通常会显得力不从心。

1. 另外一个严重问题是，当延时任务在执行的过程中出现异常时， Timer 并不会捕获，会导致 TimerThread 终止。这样一来，TaskQueue 中的其他延时任务将永远不会得到执行。

1. Timer 依赖于系统的绝对时间，如果系统时间本身不准确，那么延时任务的调度就可能会出问题。

### [DelayQueue](#delayqueue)

DelayQueue 是 JDK 提供的一个延时队列，我们可以利用它来延时获取队列中的元素，它的实现其实和 Timer 中的 TaskQueue 很类似，其底层都是一个优先级队列。

本质上还是一个数组实现的小根堆。添加，删除任务的时间复杂度仍然是 `O(logn)`。

DelayQueue 中的元素必须实现 `Delayed` 接口中的 `getDelay` , `compareTo` 方法。

其中 `getDelay` 方法用于获取任务还有多久到期。返回值如果小于等于 0，则表示该任务已经到期了。

`compareTo` 方法用于调整任务在 DelayQueue 中的位置，DelayQueue 是一个小根堆，每次向 DelayQueue 添加新的任务时，先是把任务放到 DelayQueue 的末尾，然后依次向上调整，直到任务的过期时间大于等于其 parent 。 这样就可以保证 DelayQueue 的小根堆特性 —— 堆顶元素永远是过期时间最近的任务。

我们可以通过 `take()` 方法从 DelayQueue 获取到期的堆顶任务，如果堆顶任务还没到期，那么就会在 DelayQueue 上阻塞等待，直到堆顶任务到期为止。

从 DelayQueue 的实现上可以看出，相比于 Timer，DelayQueue 只是一个延时任务的管理队列，而 Timer 却是一个完整的任务调度组件。我们需要在 DelayQueue 的基础之上，额外地实现任务调度功能。

但其底层的核心数据结构仍然是一个小根堆。和 Timer 一样，添加删除延时任务的时间复杂度都是 `O(logn)`。同样无法满足海量延时任务的调度。

### [ScheduledThreadPoolExecutor](#scheduledthreadpoolexecutor)

ScheduledThreadPoolExecutor 是多线程版本的 Timer，它是在 DelayQueue 的基础上增加了多线程调度延时任务的能力。ScheduledThreadPoolExecutor 中负责组织管理延时任务的是 DelayedWorkQueue，它也是一个小根堆实现的优先级队列，延时任务 ScheduledFutureTask 按照到期时间由近及远的组织在 DelayedWorkQueue 中。DelayedWorkQueue 的第一个元素是到期时间最近的 ScheduledFutureTask。

业务线程可以通过 schedule , scheduleAtFixedRate , scheduleWithFixedDelay 方法将延时任务 ScheduledFutureTask 添加到 DelayedWorkQueue 中。

ScheduledThreadPoolExecutor 负责调度延时任务的是一个线程池，里边包含了多个 worker 调度线程，每个 worker 线程负责从 DelayedWorkQueue 中获取已经到期的 ScheduledFutureTask，然后执行。如果 DelayedWorkQueue 中没有任务到期，那么 worker 线程就会在 DelayedWorkQueue 上阻塞等待，直到有到期的任务出现。

虽然 ScheduledThreadPoolExecutor 提供了多线程的调度能力，在一定程度上保证了延时任务调度的及时性，但是其底层仍然是依赖 DelayedWorkQueue 来管理延时任务，在面对海量延时任务的添加，删除时，时间复杂度依然还是 `O(logn)` 。那么有没有一种数据结构可以将这个时间复杂度降低为 `O(1)` 呢 ？ 这就是本文我们要讨论的重点内容 —— 时间轮的设计与实现。

## [Netty 时间轮的设计原理](#netty-时间轮的设计原理)

时间轮的设计灵感来自于我们日常生活中用的钟表，钟表有秒针，分针，时针，共三个指针，60 个刻度。秒针每走一个刻度就是一秒，秒针走完一个时钟周期（60s），分针走一个刻度就是一分钟，当分针走完一个时钟周期（60m），时针走一个刻度就是一个小时。

比如我们要在今天的 10 点 10 分 0 秒这个时刻去开一个重要的会议，那么当钟表的秒针指向 0 这个刻度，分针指向 10 这个刻度，时针指向 10 这个刻度的时候，闹钟就会响起，提醒我们去执行开会这个延时任务。

如果我们能把钟表里的刻度抽象成一个数据结构，用这个数据结构来存放对应刻度的延时任务的话，那么当钟表的时针，分针，秒针指向某个刻度的时候，我们就去执行这个刻度对应的延时任务，这样一来，一种新的延时任务调度思路就出来了，这也是时间轮的设计理念。
![](./images/images/0e398f195dc7-202502142021168.png)
如上图所示，Netty 将钟表的刻度抽象成了一个 HashedWheelBucket 的数据结构，钟表的表盘被抽象成一个 HashedWheelBucket 类型的环形数组，钟表中有 60 个刻度，而 Netty 的时间轮 HashedWheelTimer 一共有 512 个刻度。

钟表中一共有三个指针，分别是秒针，分针，时针。而 HashedWheelTimer 中只有一个 tick 指针，tick 每隔 tickDuration (100ms) 走一个刻度，也就是说 Netty 时间轮的时钟精度就是 100 ms , 定时任务的调度延时有时会在 100ms 左右。如果你接受不了这么大的调度误差，那么可以将 tickDuration 适当调小一些，但最小不能低于 1ms 。

什么意思呢 ？比如现在我们需要在 5ms 之后执行一个延时任务，那么时间轮可能在 8ms 之后才会调度这个任务，也可能在 65ms 之后调度，也有可能在 108ms 之后调度，这就使得定时任务的执行有了大约 100ms 左右的延时。

具体延时多少，取决于我们在什么时刻将这个定时任务添加到时间轮中。关于这一点，笔者后面会在介绍时间轮具体实现细节的时候详细讨论，这里点到为止，本小节我们还是主要聚焦于时间轮的设计原理。

对于钟表的秒针来说，它的 tickDuration 就是 1s , 走完一个时钟周期就是 60s 。 对于分针来说，它的 tickDuration 就是 1m , 走完一个时钟周期就是 60m。对于时针来说，它的 tickDuration 就是 1h , 走完一个时钟周期就是 12h。

由于 HashedWheelTimer 中的 tickDuration 是 100ms , 有 512 个刻度 (HashedWheelBucket) , 所以时间轮中的 tick 指针走完一个时钟周期需要 51200ms 。

HashedWheelBucket 是一个具有头尾指针的双向链表，链表中存储的元素类型为 HashedWheelTimeout 用于封装定时任务。HashedWheelBucket 中的 head 指向双向链表中的第一个 HashedWheelTimeout， tail 指向双向链表中的最后一个 HashedWheelTimeout。
![](./images/images/166d5ffd08ff-202502142022582.png)
HashedWheelTimeout 用于封装时间轮中的延时任务，提交到时间轮中的延时任务必须实现 TimerTask 接口。

HashedWheelTimeout 中有一个重要的属性 deadline，它规定了延时任务 TimerTask 的到期时间。deadline 是一个绝对时间值，它以时间轮的启动时间 startTime 为起点，表示从 startTime 这个时间点开始，到 deadline 这个时间点到期。
![](./images/images/ab7d1241cfc1-202502142032861.png)
Netty 时间轮中的时间坐标系全部是以时间轮的启动时间点 startTime 为基准的，当时间轮启动之后，会将那一刻的时间戳设置到 startTime 中。

时间轮中的 tick 指针也是一个绝对值，当时间轮启动之后，tick 指向 0，每隔 100ms (tickDuration)，tick 向前转动一下。但需要注意的是 tick 的值是只增不减的，只要时间轮在运行，那么 tick 的值就会一直递增上去。比如，当 tick 转动完一个时钟周期（51200ms）之后，tick 的值是 512 而不是重新指向 0 。

tick 与 HashedWheelBucket 之间的映射关系通过 `ticks & mask` 计算得出。mask 为 HashedWheelBucket 的个数减 1，所以这就要求时间轮中 HashedWheelBucket 的个数必须是 2 的次幂。

在时间轮中，属于同一个 HashedWheelBucket 中的延时任务 HashedWheelTimeouts，它们的到期时间 deadline 都在同一时间范围内 —— `[ tick , tick + 1) * tickDuration` 。

比如，在时间轮刚刚启动之后，tick 指向 0，那么 wheel[0] 指向的 HashedWheelBucket 里存放的 HashedWheelTimeouts，它们的到期时间均在 `[ 0 , 100) ms` 之内。

假如我们在 `tick = 0` 这个时刻，向时间轮中添加了一个延时 `5ms` 执行的 HashedWheelTimeout，那么它就会被放入 wheel[0] 中。如果添加的是一个延时 `101ms` 执行的 HashedWheelTimeout，那么它就会被放入 wheel[1] 中。同样的道理，如果添加的是一个延时 `360ms` 执行的 HashedWheelTimeout，那么它就会被放入 wheel[3] 中。
![](./images/images/4fc81ec2e9b4-202502142032213.png)
当时间过了 100ms 之后，Netty 就会将 `HashedWheelBucket0` 中的延时任务拉出来执行，执行完之后，tick 的值加 1，从 0 转动到 1 。在经过 100 ms 之后，Netty 就会将 `HashedWheelBucket1` 中的延时任务拉出来执行，执行完之后，tick 的值加 1，从 1 转动到 2，如此往复循环。这就是整个时间轮的运转逻辑。

但从这个过程中我们可以看出，延时任务的调度存在 tickDuration（100ms）左右的延迟。比如，在 `tick = 0` 这个时刻，添加到 `HashedWheelBucket0` 中的延时任务，我们本来是期望这些延时任务分别在 5ms , 10ms , 95ms 之后执行，但时间轮的真正调度时间却在 100ms 之后。这就导致了任务调度产生了 100ms 左右的延迟。

如果你接受不了 100ms 的延迟，那么可以在创建时间轮的时候，将 tickDuration 的值调低，但不能低于 1ms 。tickDuration 的值越小，时间轮的精度越高，性能开销也就越大。tickDuration 的值越大，时间轮的精度也就越低，性能开销越小。

但在中间件的场景中，往往对延时任务调度的及时性没有那么高的要求，同时为了兼顾时间轮的精度与性能，tickDuration 默认设置为100ms 是刚好合适的，通常不需要调整。

另外在默认情况下，只有一个线程 workerThread 负责推动时间轮的转动，以及延时任务的执行。

从上面的过程可以看出，只有当前 tick 对应的 HashedWheelBucket 中的延时任务全部被执行完毕的时候，tick 才会向前推动。所以为了保证任务调度的及时性，时间轮中的延时任务执行时间不能太长，只适合逻辑简单，执行时间短的延时任务。

但毕竟在默认情况下就只有这一个 workerThread，既负责延时任务的调度，又负责延时任务的执行，对于有海量并发延时任务的场景，还是显得力不从心。为了应对这种情况，我们可以在创建时间轮的时候，指定一个专门用于执行延时任务的 Executor。

这样一来，时间轮中的延时任务调度还是由单线程 workerThread 负责，到期的延时任务由线程池 Executor 来负责执行，近一步提升延时任务调度的及时性。但事实上，在大部分场景中，有一个 workerThread 就够了，并不需要额外的指定 Executor。大家可以根据实际情况，自由裁定。

另外还有一个问题就是，上图时间轮中的延时任务，它们的延时时间都在同一时钟周期内。Netty 时间轮中的一个时钟周期是 51200ms 。

也就是说，在 `tick = 0` 这个时刻，只要延时任务的延时时间在 51200ms 之内，那么当 tick 转动完 512 个刻度之后（一个时钟周期），这 512 个刻度对应的 HashedWheelBucket 中的延时任务全部会被执行到。

如果我们在 `tick = 0` 这个时刻，添加一个延时任务，但它的延时时间超过了一个时钟周期，比如在 `51250ms` 之后执行。 那么这个延时任务也会被添加到 `HashedWheelBucket0` 中。
![](./images/images/86226e1509e8-202502142034732.png)
当时间过了 100ms 之后，workerThread 就会执行 `HashedWheelBucket0` 中的延时任务。但此时只能执行延时 5ms , 10ms 的任务，不能执行延时 `51250ms` 的任务，因为它需要等到下一个时钟周期才能执行。

那么 workerThread 在执行延时任务的时候如何才能知道，哪些任务是本次时钟周期内可以执行的，哪些任务是要等到下一次或者下下次时钟周期才能执行的呢 ？

在延时任务模型 HashedWheelTimeout 中有一个字段 —— remainingRounds，用于记录延时任务还剩多少时钟周期可以执行。

本次时钟周期内可以执行的延时任务，它的 remainingRounds = 0，workerThread 在遇到 `remainingRounds = 0` 的 HashedWheelTimeout 就会执行。

下一个时钟周期才能执行的延时任务，它的 remainingRounds = 1，依次类推。当 workerThread 遇到 `remainingRounds &gt; 0` 的 HashedWheelTimeout 就会直接跳过，并将 remainingRounds 减 1 。

比如，上图中 HashedWheelBucket0 中的这几个延时任务，其中延时 5ms , 10ms 的 HashedWheelTimeout 它们的 `remainingRounds = 0`, 表示在本次时钟周期内就可以马上执行。
![](./images/images/3e8483e89bf0-202502142036682.png)
延时 51250ms 的 HashedWheelTimeout 它的 `remainingRounds = 1`， 表示在下一个时钟周期才能执行。

好了，现在整个时间轮的设计原理笔者就为大家介绍完了，那么让我们再次回到本小节开头的问题，在面对海量延时任务的添加与取消时，时间轮如何将这个时间复杂度降低为 `O(1)` 呢 ？

首先，时间轮的核心数据结构就是一个 HashedWheelBucket 类型的环形数组 wheel， 数组长度默认为 512 。wheel 数组用于组织管理时间轮中的所有延时任务。

与之前介绍的延时队列 DelayedWorkQueue 不同的是，环形数组 wheel 会按照延时时间的不同，将延时任务分散到 512 个 HashedWheelBucket 中管理。每个 HashedWheelBucket 负责管理到期时间范围在 `[ tick , tick + 1) * tickDuration` 之间的任务。

而 DelayedWorkQueue 则是用一个优先级队列来管理所有的延时任务，为了维护小根堆的特性，每次在向 DelayedWorkQueue 添加或者删除延时任务的时间复杂度为 `O(logn)`。

当我们向时间轮添加一个延时任务时，Netty 首先会根据延时任务的 deadline 以及 tickDuration 计算出该延时任务最终会停留在哪一个 tick 上。注意，延时任务中的 deadline 是一个绝对值而不是相对值，是以时间轮启动时间 startTime 为基准的一个绝对时间戳。tick 也是一个绝对值而不是相对值，是以时间轮刚刚启动时 `tick = 0` 为基准的绝对值，只增不减。

比如，前面这个延时 51250ms 的任务，它最终会停留在 `tick = 512` 上。但由于时间轮是一个环形数组，所以 tick 512 与数组长度 512 取余得到所属 HashedWheelBucket 在 wheel 数组中的 index = 0。

然后将延时任务添加到 HashedWheelBucket 的末尾，前面我们已经提过，HashedWheelBucket 是一个双向链表，向链表末尾添加一个元素的时间复杂度为 `O(1)` 。

延时任务的取消逻辑也很简单，就是将这个延时任务从其所属的 HashedWheelBucket 中删除即可。从一个双向链表中删除某个指定的元素时间复杂度也是 `O(1)`。

从以上过程我们可以看出，时间轮在面对海量延时任务的添加，取消的时候，所需的时间复杂度都是 `O(1)`，聊完了延时任务的管理，现在我们在来看一下延时任务的调度与执行。

Netty 只靠一个单线程 workThread 来推动时间轮一个 tick 一个 tick 地向前转动，当时间轮转动到某一个 tick 时，workThread 会等待一个 tickDuration （默认 100ms）的时间，随后 workThread 会将该 tick 对应的 HashedWheelBucket 中 `remainingRounds = 0` 的延时任务全都拉取下来挨个执行。

当执行完 HashedWheelBucket 中的延时任务之后，tick 向前推进一格（tick++），workThread 继续睡眠等待一个 tickDuration，然后重复上述过程。

这里我们可以看出，延时任务的调度与执行在默认情况下全部都是由一个单线程 workThread 来执行。如果时间轮中的延时任务逻辑复杂，执行时间长，那么就会影响整个时间轮的调度，tick 的转动就会出现延时，所以**时间轮虽然可以处理海量的延时任务，但是这些延时任务的逻辑必须要简单，执行时间要短**。当然了，我们也可以在创建时间轮的时候指定一个专门执行延时任务的线程池来加快任务的执行。

由于延时任务的调度通常会有一个 tickDuration 左右的延时。比如，任务的调度可能会晚几毫秒或者几十毫秒，也有可能晚一个 tickDuration 左右。**所以时间轮只能处理那些对任务调度的及时性要求没那么高的场景**。

## [Netty 时间轮相关设计模型的实现](#netty-时间轮相关设计模型的实现)
![](./images/images/0e398f195dc7-202502142021168.png)
### [HashedWheelTimer](#hashedwheeltimer)

Netty 使用一个叫做 HashedWheelTimer 的结构来描述时间轮，其中包含了第二小节中介绍的所有重要属性以及核心结构。其中最核心的就是 wheel 环形数组，它相当于钟表的表盘，表盘中的每一个刻度用 HashedWheelBucket 结构描述。

时间轮中究竟包含多少个刻度，是由构造参数 `ticksPerWheel` 决定的，默认为 512 。Netty 会根据延时时间的不同将所有提交到时间轮的延时任务分散到 512 个 HashedWheelBucket 中组织管理。定位延时任务所在的 HashedWheelBucket 以及向 HashedWheelBucket 中添加，取消延时任务的时间复杂度均为 `O(1)`。

如果时间轮中需要调度的延时任务非常多，那么每个 HashedWheelBucket 中就可能包含大量的延时任务，这就导致时间轮的调度发生延迟。针对这种情况，我们可以适当增加 ticksPerWheel 的个数，让更多的 HashedWheelBucket 来分摊延时任务。但 ticksPerWheel 必须是 2 的次幂。

这样一来，当我们向时间轮添加延时的任务的时候，就可以通过 `&` 运算来代替 `%` 运算去寻找延时任务对应的 HashedWheelBucket。

第二小节我们已经介绍过了，在向时间轮添加延时任务时，我们需要首先定位到这个延时任务最终会停留在哪一个 tick 上，时间轮中的 tick 是一个绝对值，它不会按照时钟周期的结束而自动归 0，而是一直会往上递增。

calculated 也是一个绝对值，表示延时任务最终会停留在哪一个 tick 上，随后通过 `calculated & mask` 定位到对应的 HashedWheelBucket，时间复杂度为 `O(1)`。

`tickDuration` 表示时间轮中的时钟精度，也就是 tick 指针多久转动一次，默认为 100ms，我们可以通过构造参数 tickDuration 进行指定，但最小不能低于 1ms。

tickDuration 的值越小，时间轮的精度越高，性能开销也就越大。tickDuration 的值越大，时间轮的精度也就越低，性能开销越小。

现在时间轮的基本骨架就有了，而时间轮的运转靠的就是 workerThread，由它来驱动时钟 tick 一下一下的转动，并执行对应 HashedWheelBucket 中的延时任务。

由于在默认情况下，Netty 时间轮中就只有这一个单线程 workerThread 来负责延时任务的调度与执行，在面对海量并发任务的时候，难免显得有点力不从心。执行任务的时间过长，就会导致 tick 的转动产生很大的延时。于是 Netty 又在 4.1.69.Final 中引入了一个 taskExecutor，来专门负责执行延时任务。

我们可以通过构造参数 `taskExecutor` 来指定自定义的线程池，默认情况下为 ImmediateExecutor，其本质还是由 workerThread 来执行延时任务。

workerThread 负责从对应 tick 的 HashedWheelBucket 中拉取延时任务，然后将延时任务丢给 taskExecutor 来执行。这在一定程度上提高了延时任务的消费速度，不至于拖慢 workerThread 从而影响到整个时间轮的运转。

时间轮中待执行延时任务的最大个数受到参数 `maxPendingTimeouts` 限制，默认为 -1 。当 maxPendingTimeouts 的值小于等于 0 的时候，表示 Netty 不会对时间轮中的延时任务个数进行限制。

当时间轮中的延时任务个数超过了 maxPendingTimeouts 的限制时，再向时间轮添加延时任务就会得到 `RejectedExecutionException` 异常。

另外时间轮 HashedWheelTimer 在 JVM 进程中的实例个数会受到 `INSTANCE_COUNT_LIMIT` 的限制，默认为 64 。

如果当前 JVM 进程中的 HashedWheelTimer 实例个数超过了 64，那么 Netty 就会打印 `Error` 日志进行警告。

从上面的警告信息我们可以看出，时间轮是一种共享的资源，既然是一种系统资源，那么就和内存资源一样（ByteBuf）都存在资源泄露的风险。当我们使用完时间轮但忘记调用它的 `stop` 方法进行关闭的时候，就发生了资源泄露。

和 ByteBuf 一样，在 HashedWheelTimer 中也有一个 `ResourceLeakTracker` 用于跟踪探测资源泄露的发生，如果发生资源泄露，Netty 就会以 `Error` 日志的形式打印出泄露的位置。

我们在创建 HashedWheelTimer 的时候可以通过构造参数 `leakDetection` 来开启，关闭时间轮的资源泄露探测。leakDetection 默认为 true , 表示无条件开启资源泄露的探测。如果设置为 false , 那么只有当 workerThread 不是守护线程的时候才会开启资源泄露探测。

workerThread 默认情况下并不是一个守护线程。

### [延时任务的添加](#延时任务的添加)
![](./images/images/390b02c5030f-202502142053593.png)
如上图所示，当我们向时间轮添加一个延时任务时，并不是大家想象的那样，直接将延时任务添加到时间轮中，而是首先添加到一个叫做 timeouts 的 MpscQueue 中。

为什么会这么设计呢 ？ 时间轮是一个单线程驱动的模型，内部只有一个 workerThread 来推动 tick 的转动，并从对应 HashedWheelBucket 中拉取延时任务。所以时间轮采用的是无锁化的设计，workerThread 在访问内部任何数据结构的时候都不会加锁。

而向时间轮添加延时任务的操作却是多线程执行的，如果任务被直接添加到时间轮中，那么就破坏了无锁化的设计，workerThread 在访问内部相关数据结构的时候就必须加锁了。

所以为了避免加锁的开销，Netty 引入了一个 MpscQueue 作为中转，业务多线程首先会将延时任务添加到 MpscQueue 中。等到下一个 tick , workerThread 调度延时任务的时候，会统一将 MpscQueue 中的延时任务转移到时间轮中。保证了 workerThread 单线程的无锁化运行。

另外 Netty 时间轮采用了懒启动的设计，只有第一次向时间轮添加延时任务的时候才会启动。因为时间轮一旦启动之后，workerThread 就开始运行，推动 tick 一下一下的向前推进。如果时间轮刚被创建出来就启动，此时内部又没有任何延时任务，这就导致了 tick 不必要的空转。

当时间轮启动之后，就会根据延时任务 TimerTask 的延时时间 delay 计算到期时间 deadline， 然后将 TimerTask 封装成 HashedWheelTimeout 添加到 MpscQueue 中。

之前我们提到过，HashedWheelTimeout 中最重要的一个属性就是延时任务的到期时间 deadline， deadline 是一个绝对时间戳，Netty 时间轮中的时间坐标系全部是以时间轮的启动时间点 startTime 为基准的，deadline 表示从 startTime 这个时间点开始，到 deadline 这个时间点到期。
![](./images/images/ab7d1241cfc1-202502142032861.png)
为什么这么设计呢 ？ 这是因为我们需要把时间轮的启动时间也考虑进延时时间的计算当中。比如，我们向时间轮中添加一个延时 5ms 执行的任务，其中时间轮启动花了 2ms , 那么这个延时任务就应该在时间轮启动后 3ms 开始执行。所以在计算延时任务到期时间戳 deadline 的时候需要减去时间轮的启动时间。后续时间轮的时间坐标轴均以 startTime 为基准。

下面是延时任务完整的添加逻辑，整个时间复杂度为 `O(1)` ：

### [延时任务的取消](#延时任务的取消)

延时任务的取消和添加一样，它们都是在 workerThread 之外进行操作的，所以当业务线程取消一个延时任务时，也是先将这个被取消的延时任务放到一个 MpscQueue 中暂存。

等到下一个 tick 到来的时候，workerThread 会统一处理 cancelledTimeouts 集合中已经被取消的延时任务。

延时任务 HashedWheelTimeout 的状态一共有三个，初始为 ST_INIT，任务被取消之后会更新为 ST_CANCELLED，任务准备执行的时候会更新为 ST_EXPIRED。

### [时间轮的启动](#时间轮的启动)

之前我们提过，Netty 时间轮采用了懒启动的设计，当我们首次向时间轮添加延时任务的时候才会启动。时间轮有三种状态，刚被创建出来的时候状态为 WORKER_STATE_INIT，启动之后状态为 WORKER_STATE_STARTED，关闭之后状态为 WORKER_STATE_SHUTDOWN。

时间轮中有一个重要的属性 startTime，初始状态下为 0，启动之后，workerThread 会将启动那一刻的时间戳设置到 startTime 中，这个 startTime 非常重要，因为后续时间轮中的时间坐标系均是以 startTime 为基准的。时间轮启动的一项重要工作就是设置这个 startTime。

### [时间轮的运转](#时间轮的运转)
![](./images/images/74a347bd626b-202502142056470.png)
时间轮会按照一定的到期 deadline 时间范围将所有的延时任务分别打散到 512 个 HashedWheelBucket 中，比如，**我们在 `tick = 0` 这个时刻**向时间轮添加延时任务，如果这个任务的 deadline 在 `[ 0 , 100 )ms` 内，那么它将会被添加到 HashedWheelBucket0，中，如果 deadline 在 `[ 100 , 200 )ms` 内，那么就会被添加到 HashedWheelBucket1 中。同样的道理，如果 deadline 在 `[ 200, 300 )ms` 内，它将会被添加到 HashedWheelBucket2 中，以此类推。

假设当前 `tick = 2` , 那么就表示 HashedWheelBucket2 中的延时任务马上要被 workerThread 调度执行，那么具体在什么时间执行呢 ？

时间轮中的时间纪元是 `tick = 0`，也就是从 0ms 开始， HashedWheelBucket2 中所有的延时任务，它们的 deadline 都在 `[ 200, 300 )ms` 以内。那么当 tick 从 0 转动到 2 的时候，就表示时间已经过去了 200ms。

但此时还不能马上就开始执行 HashedWheelBucket2 中的任务，因为它们的延时时间可能是 210ms , 250ms 也可能是 299ms，如果在 tick = 2 也就是 200ms 的这个时间点就马上执行，那么这些任务就被提前执行了。

所以我们需要等到 300ms 也就是 tick = 3 这个时刻才能执行 HashedWheelBucket2 中的延时任务，**注意这里 `tick = 3` 指的是具体真实的时间已经到了 300ms 这个时间点，而时间轮中的 tick 还是指向 2，并没有向前推进**。

也就是说，延时 210ms , 250ms , 299ms 的任务，需要等到 300ms 之后才能得到执行，这里我们也可以看出，时间轮的精度是 tickDuration （默认 100ms），延时任务的调度通常会晚一个 100ms 左右。

这里提到 "100ms 左右" 的意思是，时间轮中的延时任务可能会被晚调度 5ms ,也可能晚调度 9ms ,也可能是几十毫秒，也有可能是 105ms， 108ms , 111ms 。具体这个调度延迟的不确定性是如何产生的，我们放在下一个小节在讨论，这里大家有这个概念就可以了。

因此 workerThread 在调度延时任务的时候，通常会首先等到 next tick 的时间点来临才会开始执行当前 tick 对应的 HashedWheelBucket。

时间轮的精度是由 tickDuration 决定的，这个值我们可以调节，默认为 100ms , 但最小不能低于 1ms 。tickDuration 越小，时间轮的精度越高，同时 workerThread 的繁忙程度也越高 。如果 tickDuration 设置的过小，那么 workerThread 在这里就会被频繁的唤醒。

所以为了防止 workerThread 被频繁的唤醒，我们需要保证至少要 sleep 1ms 。

如果 `sleepTimeMs &lt;= 0` 则说明当前时间点 currentTime 已经过了 tick + 1 对应的时间戳 deadline， 这样就不用在这里等待了，直接返回 currentTime。

只要当前 tick 对应的 HashedWheelBucket 中的延时任务到期时间小于等于 currentTime （延时任务以过期），workerThread 会将会执行它们。

如果 `sleepTimeMs &gt; 0` 则说明当前时间还没有到达 tick + 1 这个时间点，那么 workerThread 就会在这里睡眠等待。

当时间到达 tick + 1 这个时间点之后，workerThread 就会从这里唤醒，转去执行当前 tick 对应的 HashedWheelBucket 里的延时任务

但 HashedWheelBucket 里面此时可能还是空的，没有任何延时任务。因为当业务线程在向时间轮添加延时任务的时候，首先是要将任务添加到一个叫做 timeouts 的 MpscQueue 中。也就是说延时任务首先会在 timeouts 中缓存，并不会直接添加到对应的 HashedWheelBucket 中，

那么 workerThread 在被唤醒之后，首先要做的就是从 timeouts 中将延时任务转移到时间轮对应的 HashedWheelBucket 中。

当任务转移完成之后，workerThread 开始处理当前 tick 对应的HashedWheelBucket，将 HashedWheelBucket 中的延时任务挨个拉取出来执行。当所有到期的延时任务被执行完之后，tick 向前推进一格，开启新一轮的循环。
![](./images/images/3e8483e89bf0-202502142036682.png)
时间轮中的延时任务默认情况下是由 workerThread 执行的，但如果我们在创建时间轮的时候指定了专门的 taskExecutor， 那么延时任务就会由这个 taskExecutor 负责执行，workerThread 只负责调度，大大减轻了 workerThread 的负荷。

下面是时间轮运转的完整逻辑流程：

### [调度延迟的不确定性是如何产生的](#调度延迟的不确定性是如何产生的)

前面我们提到过，时间轮只适合那种对延时任务的调度及时性要求没那么高的场景，Netty 时间轮的精度为一个 tickDuration，默认为 100ms 。延时任务的调度通常会晚 100ms 左右。

比如，现在我们向时间轮添加一个延时 5ms 之后执行的任务，那么这个延时任务可能会在 8ms 之后执行，也可能是 65ms 之后执行，也有可能在 108ms 之后执行。总之，时间轮调度的延迟范围会在 100ms 左右。那为什么会出现这种不确定性呢 ？

这其中主要有两个原因，首先第一个原因就是时间轮的延时任务太多，延时任务的逻辑比较复杂，执行时间略长，导致了 workerThread 的阻塞，从而造成了任务调度的延迟。减缓这种情况的一个措施就是在创建时间轮的时候，我们可以指定一个自定义的 taskExecutor 来专门负责延时任务的执行，减轻 workerThread 的负荷。或者增大 HashedWheelBucket 的个数，尽量的分散延时任务，不要让它们集中在某一个 HashedWheelBucket 中。

第二个原因是要看我们究竟在哪一个时间点向时间轮添加延时任务。不同的添加时机，也会造成调度的不确定性。这可能有点难以理解，我们来看一个具体的例子。
![](./images/images/dcaaa26993bc-202502142100529.png)
比如，我们在下图时间轴中 1ms 这个时刻向时间轮添加一个延时 5ms 执行的任务。当前时间轮如上图所示，tick 指向 0 。
![](./images/images/38a30a46a61b-202502142100294.png)
延时 5ms 的任务会被添加到 HashedWheelBucket0 中，此时 workerThread 还在 sleep 等待 next tick 也就是 100ms 这个时间点的到来。

我们在 1ms 这个时刻添加的这个延时任务本来应该在时间轴中的 6ms 这个时间点执行，但是现在 workerThread 还在睡眠，需要等到 100ms 这个时间点才能被唤醒去执行 HashedWheelBucket0 中的延时任务。这就产生了 90 ms 的调度延时。

但如果我们在时间轴的 94ms 位置处添加这个 5ms 的延时任务，那么这个延时任务本应该在时间轴的 99ms 这个时间点被执行，但由于 workerThread 在 100ms 这个时间点才会被唤醒，所以产生了 1ms 的调度延时。

如果非常不幸，我们恰好卡在了时间轴 95ms 这个时间点添加这个 5ms 的延时任务，此时要注意，这个延时任务会被放在 HashedWheelBucket1 中而不是 HashedWheelBucket0。

而 HashedWheelBucket1 中的延时任务，workerThread 需要等到时间轴 200ms 这个时间点才会去执行，这样一来，本应该在 100ms 这个时间点执行的延时任务，时间轮却在 200ms 这个时间点来调度，这就产生了 100ms 的调度延时。如果在算上 CPU 调度 workerThread 的时间，那么这个延迟可能就在 105ms 或者 108ms 左右。这里大家可以对照上小节的内容，仔细想想是不是这么回事。

### [时间轮的关闭](#时间轮的关闭)

时间轮定义了三种状态，在刚被创建出来的时候状态为 WORKER_STATE_INIT，启动之后状态为 WORKER_STATE_STARTED。

待更新：[https://www.cnblogs.com/binlovetech/p/18629491](https://www.cnblogs.com/binlovetech/p/18629491)
