{

  "title": "Phaser深度解析：多阶段任务协调实现机制",
  "has_date": true,
  "description": "Phaser运行机制 Registration(注册) 跟其他barrier不同，在phaser上注册的parties会随着时间的变化而变化。任务可以随时注册(使用方法register,bulkRegister注册，或者由构造器确定初始parties)，并且在任何抵达点可以随意地撤销注册(方法arr",
  "tags": [
    "Java",
    "并发"
  ],
  "source": "local-markdown-library",
  "source_path": "java/concurrent/05-concurrenttools5-phaser - Phaser深度解析：多阶段任务协调实现机制.md",
  "date": "2025-05-17"

}

## [Phaser运行机制](#phaser运行机制)
![](/imported/markdown/2025-05-17-markdown-d2e1bfbe-phaser深度解析-多阶段任务协调实现机制/images/82417cb3b9ad-202404251558361.jpg)

- Registration(注册)

跟其他barrier不同，在phaser上注册的parties会随着时间的变化而变化。任务可以随时注册(使用方法register,bulkRegister注册，或者由构造器确定初始parties)，并且在任何抵达点可以随意地撤销注册(方法arriveAndDeregister)。就像大多数基本的同步结构一样，注册和撤销只影响内部count；不会创建更深的内部记录，所以任务不能查询他们是否已经注册。(不过，可以通过继承来实现类似的记录)

- Synchronization(同步机制)

和CyclicBarrier一样，Phaser也可以重复await。方法arriveAndAwaitAdvance的效果类似CyclicBarrier.await。phaser的每一代都有一个相关的phase number，初始值为0，当所有注册的任务都到达phaser时phase+1，到达最大值(Integer.MAX_VALUE)之后清零。使用phase number可以独立控制 到达phaser 和 等待其他线程 的动作，通过下面两种类型的方法:

**Arrival(到达机制)** arrive和arriveAndDeregister方法记录到达状态。这些方法不会阻塞，但是会返回一个相关的arrival phase number；也就是说，phase number用来确定到达状态。当所有任务都到达给定phase时，可以执行一个可选的函数，这个函数通过重写onAdvance方法实现，通常可以用来控制终止状态。重写此方法类似于为CyclicBarrier提供一个barrierAction，但比它更灵活。**Waiting(等待机制)** awaitAdvance方法需要一个表示arrival phase number的参数，并且在phaser前进到与给定phase不同的phase时返回。和CyclicBarrier不同，即使等待线程已经被中断，awaitAdvance方法也会一直等待。中断状态和超时时间同样可用，但是当任务等待中断或超时后未改变phaser的状态时会遭遇异常。如果有必要，在方法forceTermination之后可以执行这些异常的相关的handler进行恢复操作，Phaser也可能被ForkJoinPool中的任务使用，这样在其他任务阻塞等待一个phase时可以保证足够的并行度来执行任务。

- Termination(终止机制)

可以用isTerminated方法检查phaser的终止状态。在终止时，所有同步方法立刻返回一个负值。在终止时尝试注册也没有效果。当调用onAdvance返回true时Termination被触发。当deregistration操作使已注册的parties变为0时，onAdvance的默认实现就会返回true。也可以重写onAdvance方法来定义终止动作。forceTermination方法也可以释放等待线程并且允许它们终止。

- Tiering(分层结构)

Phaser支持分层结构(树状构造)来减少竞争。注册了大量parties的Phaser可能会因为同步竞争消耗很高的成本， 因此可以设置一些子Phaser来共享一个通用的parent。这样的话即使每个操作消耗了更多的开销，但是会提高整体吞吐量。 在一个分层结构的phaser里，子节点phaser的注册和取消注册都通过父节点管理。子节点phaser通过构造或方法register、bulkRegister进行首次注册时，在其父节点上注册。子节点phaser通过调用arriveAndDeregister进行最后一次取消注册时，也在其父节点上取消注册。

- Monitoring(状态监控)

由于同步方法可能只被已注册的parties调用，所以phaser的当前状态也可能被任何调用者监控。在任何时候，可以通过getRegisteredParties获取parties数，其中getArrivedParties方法返回已经到达当前phase的parties数。当剩余的parties(通过方法getUnarrivedParties获取)到达时，phase进入下一代。这些方法返回的值可能只表示短暂的状态，所以一般来说在同步结构里并没有啥卵用。

## [Phaser源码详解](#phaser源码详解)

### [核心参数](#核心参数)

state状态说明：Phaser使用一个long型state值来标识内部状态:

- 低0-15位表示未到达parties数；

- 中16-31位表示等待的parties数；

- 中32-62位表示phase当前代；

- 高63位表示当前phaser的终止状态。

注意: 子Phaser的phase在没有被真正使用之前，允许滞后于它的root节点。这里在后面源码分析的reconcileState方法里会讲解。 Qnode是Phaser定义的内部等待队列，用于在阻塞时记录等待线程及相关信息。实现了ForkJoinPool的一个内部接口ManagedBlocker，上面已经说过，Phaser也可能被ForkJoinPool中的任务使用，这样在其他任务阻塞等待一个phase时可以保证足够的并行度来执行任务(通过内部实现方法isReleasable和block)。

### [函数列表](#函数列表)

### [方法 - register()](#方法-register)

说明: register方法为phaser添加一个新的party，如果onAdvance正在运行，那么这个方法会等待它运行结束再返回结果。如果当前phaser有父节点，并且当前phaser上没有已注册的party，那么就会交给父节点注册。

register和bulkRegister都由doRegister实现，大概流程如下:

- 如果当前操作不是首次注册，那么直接在当前phaser上更新注册parties数

- 如果是首次注册，并且当前phaser没有父节点，说明是root节点注册，直接更新phase

- 如果当前操作是首次注册，并且当前phaser由父节点，则注册操作交由父节点，并更新当前phaser的phase

- 上面说过，子Phaser的phase在没有被真正使用之前，允许滞后于它的root节点。非首次注册时，如果Phaser有父节点，则调用reconcileState()方法解决root节点的phase延迟传递问题， 源码如下:

当root节点的phase已经advance到下一代，但是子节点phaser还没有，这种情况下它们必须通过更新未到达parties数 完成它们自己的advance操作(如果parties为0，重置为EMPTY状态)。

回到register方法的第一步，如果当前未到达数为0，说明上一代phase正在进行到达操作，此时调用internalAwaitAdvance()方法等待其他任务完成到达操作，源码如下:

简单介绍下第二个参数node，如果不为空，则说明等待线程需要追踪中断状态或超时状态。以doRegister中的调用为例，不考虑线程争用，internalAwaitAdvance大概流程如下:

- 首先调用releaseWaiters唤醒上一代所有等待线程，确保旧队列中没有遗留的等待线程。

- 循环SPINS_PER_ARRIVAL指定的次数或者当前线程被中断，创建node记录等待线程及相关信息。

- 继续循环调用ForkJoinPool.managedBlock运行被阻塞的任务

- 继续循环，阻塞任务运行成功被释放，跳出循环

- 最后唤醒当前phase的线程

### [方法 - arrive()](#方法-arrive)

说明: arrive方法手动调整到达数，使当前线程到达phaser。arrive和arriveAndDeregister都调用了doArrive实现，大概流程如下:

- 首先更新state(state - adjust)；

- 如果当前不是最后一个未到达的任务，直接返回phase

- 如果当前是最后一个未到达的任务:

- 如果当前是root节点，判断是否需要终止phaser，CAS更新phase，最后释放等待的线程；

- 如果是分层结构，并且已经没有下一代未到达的parties，则交由父节点处理doArrive逻辑，然后更新state为EMPTY。

### [方法 - arriveAndAwaitAdvance()](#方法-arriveandawaitadvance)

说明: 使当前线程到达phaser并等待其他任务到达，等价于awaitAdvance(arrive())。如果需要等待中断或超时，可以使用awaitAdvance方法完成一个类似的构造。如果需要在到达后取消注册，可以使用awaitAdvance(arriveAndDeregister())。效果类似于CyclicBarrier.await。大概流程如下:

- 更新state(state - 1)；

- 如果未到达数大于1，调用internalAwaitAdvance阻塞等待其他任务到达，返回当前phase

- 如果为分层结构，则交由父节点处理arriveAndAwaitAdvance逻辑

- 如果未到达数&lt;=1，判断phaser终止状态，CAS更新phase到下一代，最后释放等待当前phase的线程，并返回下一代phase。

### [方法 - awaitAdvance(int phase)](#方法-awaitadvance-int-phase)

说明: awaitAdvance用于阻塞等待线程到达，直到phase前进到下一代，返回下一代的phase number。方法很简单，不多赘述。awaitAdvanceInterruptibly方法是响应中断版的awaitAdvance，不同之处在于，调用阻塞时会记录线程的中断状态
