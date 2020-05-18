<!-- The Node.js Event Loop, Timers, and process.nextTick() -->

# Node.js 的事件循环 ( Event Loop ), 计时器 ( Timers ), 以及 `process.nextTick()`

<!-- What is the Event Loop? -->

## 1. 什么是事件循环

<!-- The event loop is what allows Node.js to perform non-blocking I/O operations — despite the fact that JavaScript is single-threaded — by offloading operations to the system kernel whenever possible. -->

尽管 JavaScript 是单线程执行的, 事件循环依旧使得 Node.js 可以执行非阻塞的 I/O 操作. 
事实上, 事件循环使得 I/O 操作尽可能降级为系统内核行为.

<!-- Since most modern kernels are multi-threaded, they can handle multiple operations executing in the background. When one of these operations completes, the kernel tells Node.js so that the appropriate callback may be added to the poll queue to eventually be executed. We'll explain this in further detail later in this topic. -->

现代操作系统内核均是多线程的, 它可以处理多个后台任务.
一旦有一个任务完成后, 内核就会通知 Node.js 在适当的时候将回调任务加入到轮询队列中, 并最终执行它.
我们将在本专题中详细讨论这些内容.


<!-- Event Loop Explained -->

## 2. 什么是事件循环

<!-- When Node.js starts, it initializes the event loop, processes the provided input script (or drops into the REPL, which is not covered in this document) which may make async API calls, schedule timers, or call process.nextTick(), then begins processing the event loop. -->

在 Node,js 启动的时候, 会初始化事件循环. 它可以处理传入的脚本 ( 也可以是 REPL 环境, 
但是本部不考虑这种情况. ). 脚本中可以包含 异步 API 的调用, 可以包含计时器调用, 
以及 `process.nextTick()` 方法的调用. 事实上此时就已经启动事件循环了.

<!-- The following diagram shows a simplified overview of the event loop's order of operations. -->

下面的图中表展示了一个简单事件循环的处理流程.


```txt
     ┌───────────────────────────┐
  ┌─>│           timers          │
  │  └─────────────┬─────────────┘
  │  ┌─────────────┴─────────────┐
  │  │     pending callbacks     │
  │  └─────────────┬─────────────┘
  │  ┌─────────────┴─────────────┐
  │  │       idle, prepare       │
  │  └─────────────┬─────────────┘      ┌───────────────┐
  │  ┌─────────────┴─────────────┐      │   incoming:   │
  │  │           poll            │<─────┤  connections, │
  │  └─────────────┬─────────────┘      │   data, etc.  │
  │  ┌─────────────┴─────────────┐      └───────────────┘
  │  │           check           │
  │  └─────────────┬─────────────┘
  │  ┌─────────────┴─────────────┐
  └──┤      close callbacks      │
     └───────────────────────────┘
```

<!-- note: each box will be referred to as a "phase" of the event loop. -->

*说明: 每一个矩形区域都是一个事件循环的处理环节.*

<!-- Each phase has a FIFO queue of callbacks to execute. While each phase is special in its own way, generally, when the event loop enters a given phase, it will perform any operations specific to that phase, then execute callbacks in that phase's queue until the queue has been exhausted or the maximum number of callbacks has executed. When the queue has been exhausted or the callback limit is reached, the event loop will move to the next phase, and so on. -->

每一个处理环节都含有一个需要执行的 FIFO 回调队列 ( 译注: FIFO, First IN First Out ).
每一个环节都有自己的任务 ( 译注: 每一个阶段的任务丢都一样, 各个阶段完成不同的事情 ). 
通常, 当事件循环进入某一个环节时, 它便会执行这个环节应该处理的所有事情. 
然后执行该环节的回调函数队列, 只到队列清空, 或回调栈已达最大值 ( 译注: 不清楚栈溢出是否会中断 ).
若队列清空, 或回调栈已达最大值, 则事件循环会进入下一环节, 如此往复.


<!-- Since any of these operations may schedule more operations and new events processed in the poll phase are queued by the kernel, poll events can be queued while polling events are being processed. As a result, long running callbacks can allow the poll phase to run much longer than a timer's threshold. See the timers and poll sections for more details. -->

所有的处理过程都可能再创建额外的处理过程. **poll** 环节中, 新的事件处理会被内核排队. 
而 poll 事件则会在处理轮询事件的过程中被排队. ( 译注: 晕 ... )
因此, 执行回调的时间长度限制比起执行计时器的时间限制要长. 
详情可以参考 [计时器](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#timers) 
以及 [poll](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#poll) 部分.

<!-- NOTE: There is a slight discrepancy between the Windows and the Unix/Linux implementation, but that's not important for this demonstration. The most important parts are here. There are actually seven or eight steps, but the ones we care about — ones that Node.js actually uses - are those above. -->


*注意: 虽然在 Windows 和 Unix/Linux 中的实现略有不同的, 但这一点在本文中是不影响的. 而事实上, 整个流程有七到八步, 而最重要的都在这里了. 但是在上面的步骤中, 我们更加关心哪一些是 Node.js 实际使用到的.*



<!-- Phases Overview -->

## 3. 步骤概览

<!-- timers: this phase executes callbacks scheduled by setTimeout() and setInterval().
pending callbacks: executes I/O callbacks deferred to the next loop iteration.
idle, prepare: only used internally.
poll: retrieve new I/O events; execute I/O related callbacks (almost all with the exception of close callbacks, the ones scheduled by timers, and setImmediate()); node will block here when appropriate.
check: setImmediate() callbacks are invoked here.
close callbacks: some close callbacks, e.g. socket.on('close', ...). -->


- **timers**: 这一阶段执行 `setTimeout()` 和 `setInterval()` 指定的回调函数.
- **pending callback**: 执行延迟到下一次循环迭代的 I/O 回调.
- **idle, prepare**: 仅在内部使用.
- **poll**: 查询新的 I/O 事件, 执行相关的 I/O 回调 ( 除了 close 回调, 计时器指定的回调, 以及 `setImmediate()` ); node 可能会在此处阻塞.
- **check**: `setImmediate()` 回调会在此处执行.
- **close callback**: 一些 close 回调会执行, 例如 `socket.on( 'close', ... )`.

<!-- Between each run of the event loop, Node.js checks if it is waiting for any asynchronous I/O or timers and shuts down cleanly if there are not any. -->

在执行事件循环的每一个环节中, Node.js 会检查是否存在异步 I/O 与计时器, 若没有则会检查是否已经执行完毕.


<!-- Phases in Detail -->

## 4. 步骤细节

<!-- timers -->

### 4.1 timer 阶段

<!-- A timer specifies the threshold after which a provided callback may be executed rather than the exact time a person wants it to be executed. Timers callbacks will run as early as they can be scheduled after the specified amount of time has passed; however, Operating System scheduling or the running of other callbacks may delay them. -->

计时器会指定一个时间临界点, 在时间临界点后指定的回调可能会被执行, 但并不是在人们预想的时间执行.
计时器指定的回调函数会在时间到来后尽快的被安排执行. 这是因为操作系统的调度以及其他回调的执行会加重这种延迟.

<!-- Note: Technically, the poll phase controls when timers are executed. -->

*注意: 技术上讲, [poll 环节](https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/#poll)控制了计时器的执行时机.*

<!-- For example, say you schedule a timeout to execute after a 100 ms threshold, then your script starts asynchronously reading a file which takes 95 ms: -->

例如, 你要在 100ms 后执行一个计时器, 然而, 可能你的代码开始执行后, 其中文件的异步读取花费了 95ms:

```js
const fs = require( 'fs' );

function someAsyncOperation( callback ) {
   // 假设, 该代码的执行会消耗 95ms
   fs.readFile( 'path/to/file', callback );
}

const timeoutScheduled = new Date();

setTimeout( () => {

   const delay = Date.now() - timeoutScheduled;

   console.log( `距离我定义计时器后已过了 ${ delay }ms` );

}, 100 );

// 执行 someAsyncOperation 方法, 并会消耗 95ms
someAsyncOperation( () => {

   const startCallback = Date.now();

   // 执行会消耗 10ms 的代码 ...
   while( Date.now() - startCallback < 10 ) {
      // 什么也不用做
   }

} );
```

<!-- When the event loop enters the poll phase, it has an empty queue (fs.readFile() has not completed), so it will wait for the number of ms remaining until the soonest timer's threshold is reached. While it is waiting 95 ms pass, fs.readFile() finishes reading the file and its callback which takes 10 ms to complete is added to the poll queue and executed. When the callback finishes, there are no more callbacks in the queue, so the event loop will see that the threshold of the soonest timer has been reached then wrap back to the timers phase to execute the timer's callback. In this example, you will see that the total delay between the timer being scheduled and its callback being executed will be 105ms. -->

在 时间循环进入 poll 环节的时候, 队列是空的 ( `fs.readFile()` 还未执行完 ), 运行时依旧会等待数毫秒, 直到最近的计时器的时间来到.
在此期间会等待 95ms, `fs.readFile()` 读取文件结束后, 其回调会投递到队列中并执行消耗 10ms.
在回调执行完毕后, 队列中再无其他回调. 因此事件循环会在下一次 timer 环节中保证最近的计时器临界值的到来, 并执行计时器的回调.
在本例中, 你可以看到在计时器被定义到回调被执行总时间是 105ms.


<!-- Note: To prevent the poll phase from starving the event loop, libuv (the C library that implements the Node.js event loop and all of the asynchronous behaviors of the platform) also has a hard maximum (system dependent) before it stops polling for more events. -->

注意: 为避免事件循环在 poll 阶段被饿死, 
[libuv](https://libuv.org/) ( 一个 C 语言库, 它是 Node.js 事件循环, 以及所有异步行为的实现库 ) 会提供一个魔数 ( 由系统提供 ),
在此之前不去处理其他事件.

<!-- pending callbacks -->

### 4.2 pending callback 阶段

<!-- This phase executes callbacks for some system operations such as types of TCP errors. For example if a TCP socket receives ECONNREFUSED when attempting to connect, some *nix systems want to wait to report the error. This will be queued to execute in the pending callbacks phase. -->

在这一阶段会执行诸如 TCP 各种错误处理的系统回调. 例如, 在 TCP 尝试连接的时候收到 ECONNREFUSED 的消息, 大多数 *nix 系统会等待错误报告.
那么就会在 pending callback 环节进行排队.


<!-- poll -->

### 4.3 poll 阶段

<!-- The poll phase has two main functions: -->

在 poll 阶段有两个主要的任务:

<!-- Calculating how long it should block and poll for I/O, then
Processing events in the poll queue. -->

1. 计算需要阻塞多长时间, 以及轮询 I/O
2. 处理轮询队列中的事件 

<!-- When the event loop enters the poll phase and there are no timers scheduled, one of two things will happen: -->

若没有计时器的定义, 那么事件循环在进入 poll 环节时, 会有下面两者中的一个发生:

<!-- - If the poll queue is not empty, the event loop will iterate through its queue of callbacks executing them synchronously until either the queue has been exhausted, or the system-dependent hard limit is reached.

- If the poll queue is empty, one of two more things will happen:

   - If scripts have been scheduled by setImmediate(), the event loop will end the poll phase and continue to the check phase to execute those scheduled scripts.

   - If scripts have not been scheduled by setImmediate(), the event loop will wait for callbacks to be added to the queue, then execute them immediately. 
-->

- 如果 poll 队列非空, 事件循环会依次同步执行队列中的回调, 直到队列清空, 或者达到系统设定的时间上限.
- 如果 poll 队列为空, 还会有两件事情:
  - 若代码中使用 `setImmediate()` 方法设定了回调, 事件循环会在 poll 阶段结束后的 check 阶段执行这些回调.
  - 如果没有使用 `setImmediate()` 方法设定了回调, 事件循环会等待已经入队的所有回调执行完毕.

<!-- Once the poll queue is empty the event loop will check for timers whose time thresholds have been reached. If one or more timers are ready, the event loop will wrap back to the timers phase to execute those timers' callbacks. -->

一旦 poll 队列为空, 事件循环就会检查计时器指定的回调是否到达预定时间. 若已有计时器到达, 则事件循环会绕回到 timer 环节去执行计时器回调.

> 译注: wrap back 是回到 timer 阶段, 还是进入下一循环阶段的 timer ?

<!-- check -->

### 4.4 check 环节

<!-- This phase allows a person to execute callbacks immediately after the poll phase has completed. If the poll phase becomes idle and scripts have been queued with setImmediate(), the event loop may continue to the check phase rather than waiting. -->

该个阶段在 poll 阶段完毕后执行, 它允许回调立即执行. 若 poll 环节变为空闲 ( idle ), 同时 `setImmedate()` 指定的脚本已入队, 
那么事件循环可能继续处于 check 环节, 而不是等待.

<!-- setImmediate() is actually a special timer that runs in a separate phase of the event loop. It uses a libuv API that schedules callbacks to execute after the poll phase has completed. -->

`setImmediate()` 实际上是一个特殊的计时器, 它会在事件循环中的一个指定环节运行.
它会使用 libuv 的 API 来指定在 poll 环节结束后执行回调函数.


<!-- Generally, as the code is executed, the event loop will eventually hit the poll phase where it will wait for an incoming connection, request, etc. However, if a callback has been scheduled with setImmediate() and the poll phase becomes idle, it will end and continue to the check phase rather than waiting for poll events. -->

一般, 代码被执行后, 事件循环将进入 poll 环节, 它会等待连接, 请求等处理. 
然而, 如果一个回调被 `setImmediate()` 所指定, 那么 poll 环节会进入空闲状态, 然后结束.
接下来进入 check 环节, 而不是继续等待 事件轮询.

<!-- close callbacks -->

### 4.5 close callback 环节

<!-- If a socket or handle is closed abruptly (e.g. socket.destroy()), the 'close' event will be emitted in this phase. Otherwise it will be emitted via process.nextTick(). -->

如果一个 socket 或句柄突然关闭 ( 例如 `socket.destroy()` ), 那么 `close` 事件会在该环节被触发. 或者利用 `process.nextTick()` 来触发.



<!-- setImmediate() vs setTimeout() -->

## `setImmediate()` 与 `setTimeout()` 

<!-- setImmediate() and setTimeout() are similar, but behave in different ways depending on when they are called. -->

`setImmediate()` 与 `setTimeout()` 两个方法很类似, 不同之处在于它们何时被调用.

<!-- setImmediate() is designed to execute a script once the current poll phase completes.
setTimeout() schedules a script to be run after a minimum threshold in ms has elapsed. -->

- `setImmediate()` 是在当前 poll 环节完成后执行一次代码.
- `setTimeout()` 是在毫秒范围内, 指定一个最小时间后再执行代码.

<!-- The order in which the timers are executed will vary depending on the context in which they are called. If both are called from within the main module, then timing will be bound by the performance of the process (which can be impacted by other applications running on the machine). -->

执行计时器的顺序会随着调用它们的上下文变化而改变. 
如果在主模块中调用它们, 那么时间会受到处理性能的影响 ( 当前机器上的其他程序的运行会影响到当前进程 ).

<!-- For example, if we run the following script which is not within an I/O cycle (i.e. the main module), the order in which the two timers are executed is non-deterministic, as it is bound by the performance of the process: -->

例如, 在没有 I/O 操作的逻辑中, 执行下面的代码 ( 即, 主模块 ), 那么两个计时器的执行是不确定的, 它取决于当前处理器性能:

```js
// timeout_vs_immediate.js

setTimeout( () => {
   console.log( 'timeout' );
}, 0 );

setImmediate( () => {
   console.log( 'immediate' );
} );
```

![](assets/2019-09-03-15-31-29.png)


<!-- However, if you move the two calls within an I/O cycle, the immediate callback is always executed first: -->

但是, 如果你将代码写在 包含 I/O 操作的环境中, 那么 immediate 回调总数先执行:

```js
// timeout_vs_immediate.js
const fs = require( 'fs' );

fs.readFile( __filename, () => {
   setTimeout( () => {
      console.log( 'timeout' );
   }, 0 );

   setImmediate( () => {
      console.log( 'immediate' );
   } );
} );
```

![](assets/2019-09-03-15-34-52.png)

<!-- The main advantage to using setImmediate() over setTimeout() is setImmediate() will always be executed before any timers if scheduled within an I/O cycle, independently of how many timers are present. -->

无论是否存在 I/O 操作, 只要在 `setTimeout()` 中存在 `setImmediate()`, 那么 `setImmediate()` 一定比其他 timer 先执行, 而不考虑有多少计时器.


<!-- process.nextTick() -->

## 5. `process.netTick()`

<!-- Understanding process.nextTick() -->

### 5.1 理解 `process.nextTick()`

<!-- You may have noticed that process.nextTick() was not displayed in the diagram, even though it's a part of the asynchronous API. This is because process.nextTick() is not technically part of the event loop. Instead, the nextTickQueue will be processed after the current operation is completed, regardless of the current phase of the event loop. Here, an operation is defined as a transition from the underlying C/C++ handler, and handling the JavaScript that needs to be executed. -->

你可能注意到 `process.nextTick()` 并不在上面的图表中, 即使它是异步 API. 这是因为 `process.nextTick()` 并不是事件循环中的技术.
事实上, 在当前操作结束后, `nextTickQueue` 就会被处理, 而不考虑当前环节是事件循环中的哪一个环节.
这里的 *操作* 是指一个切换, 该切换是从底层 C/C++ 的代码到需要被执行的 JavaScript 代码的切换.


<!-- Looking back at our diagram, any time you call process.nextTick() in a given phase, all callbacks passed to process.nextTick() will be resolved before the event loop continues. This can create some bad situations because it allows you to "starve" your I/O by making recursive process.nextTick() calls, which prevents the event loop from reaching the poll phase. -->

再次查看前面的图表, 任何环节都可以调用 `process.nextTick()`. 所有传入 `process.nextTick()` 的回调函数都会在事件循环继续之前被处理.
这会出现一个尴尬的局面, 因为此时**允许使用递归调用 `process.nextTick()` 方法, 那么你的 I/O 将会被饿死.** 因为这个递归会阻止事件循环到达 poll 阶段.


<!-- Why would that be allowed? -->

### 5.2 为什么会被允许呢?

<!-- Why would something like this be included in Node.js? Part of it is a design philosophy where an API should always be asynchronous even where it doesn't have to be. Take this code snippet for example: -->

为什么像这样的东西会被包含在 Node.js 中呢? 实际上, Node.js 中的设计哲学包含一个特征, 它就是无论如何 API 都应该是异步的.
以下面的代码片段为例:

```js
function apiCall( arg, callback ) {
   if ( typeof arg !== 'string' ) {
      return process.nextTick( callback,
                               new TypeError( '参数必须是字符串' ) );
   }
}
```

<!-- The snippet does an argument check and if it's not correct, it will pass the error to the callback. The API updated fairly recently to allow passing arguments to process.nextTick() allowing it to take any arguments passed after the callback to be propagated as the arguments to the callback so you don't have to nest functions. -->

代码片段中会检查传入的参数, 若参数不符合要求, 则会将错误传入回调函数.
最近 API 进行了更新 ( 译注: 文章比较早, 从 Node.js 4.0.0 开始, `process.nextTick` 可以给回调提供参数 ),
允许给 `process.nextTick()` 传入任意参数, 并在回调时将该参数传递给回调函数. 这样就不需要嵌套函数了.


<!-- What we're doing is passing an error back to the user but only after we have allowed the rest of the user's code to execute. By using process.nextTick() we guarantee that apiCall() always runs its callback after the rest of the user's code and before the event loop is allowed to proceed. To achieve this, the JS call stack is allowed to unwind then immediately execute the provided callback which allows a person to make recursive calls to process.nextTick() without reaching a RangeError: Maximum call stack size exceeded from v8. -->

我们所做的事情是传递给用户一个错误信息, 但是这个行为只有在用户所有的代码执行结束后才会处理.
通过使用 `process.nextTick()` 方法, 我们可以保证在用户代码执行结束后, 在下一个事件循环开始之前执行 apiCall() 方法中的回调.
为实现这个特性, 在执行回调的时候, JS 调用栈可以被展开. 这个回调则允许递归调用 `process.nextTick()` 方法, 
但是不会触发 v8 中定义的栈溢出错误 ( 范围错误: 函数调用栈达到最大 ). 

<!-- This philosophy can lead to some potentially problematic situations. Take this snippet for example: -->

这个哲学思想会导致一些潜在的问题. 以下面的代码片段为例:

```js
let bar;

// this has an asynchronous signature, but calls callback synchronously
// 这是一个异步函数, 但是回调是同步调用的
function someAsyncApiCall( callback ) { callback(); }

// the callback is called before `someAsyncApiCall` completes.
// 回调函数会在 `someAsyncApiCall` 调用完成后被调用
someAsyncApiCall( () => {
   // since someAsyncApiCall has completed, bar hasn't been assigned any value
   // 此时 someAsyncApiCall 已经完成, 但是 bar 还未被赋值
   console.log( 'bar', bar ); // undefined
} );

bar = 1;
```

<!-- The user defines someAsyncApiCall() to have an asynchronous signature, but it actually operates synchronously. When it is called, the callback provided to someAsyncApiCall() is called in the same phase of the event loop because someAsyncApiCall() doesn't actually do anything asynchronously. As a result, the callback tries to reference bar even though it may not have that variable in scope yet, because the script has not been able to run to completion. -->

用户定义的 `someAsyncApiCall()` 函数有异步签名, 但是实际上执行是同步的. 
在该函数被调用时, 传入 `someAsyncApiCall()` 函数的回调, 会在该事件循环的当前环节被调用.
因为 `someAsyncApiCall()` 函数没有任何异步行为. 
那么结果就是, 回调函数会尝试去引用 `bar`, 即使当前作用域中还没有该变量. 因为代码还没有执行完毕.


<!-- By placing the callback in a process.nextTick(), the script still has the ability to run to completion, allowing all the variables, functions, etc., to be initialized prior to the callback being called. It also has the advantage of not allowing the event loop to continue. It may be useful for the user to be alerted to an error before the event loop is allowed to continue. Here is the previous example using process.nextTick(): -->

将回调函数放到 `process.nextTick()` 中, 代码依旧有能力运行成功. 
同时可以在回调函数调用之前完成变量, 函数等的初始化.
还有一个特点, 那就是不会进入事件循环的下一个环节.
这在事件循环进入下一个环节的时候, 若要通知用户是很方便的.
下面是上一个案例使用 `process.nextTick()` 的版本:

```js
let bar;

function someAsyncApiCall( callback ) {
   process.nextTike( callback );
}
someAsyncApiCall( () => {
   console.log( 'bar', bar ); // 1
} );

bar = 1;
```

<!-- Here's another real world example: -->

这是另一个真实的案例:

```js
const server = net.createServer( () => {} ).listen( 8080 );

server.on( 'listening', () => {} );
```

<!-- When only a port is passed, the port is bound immediately. So, the 'listening' callback could be called immediately. The problem is that the .on('listening') callback will not have been set by that time. -->

在传入端口后, 绑定才立刻绑定该端口. 因此 `'listening'` 回调才会立即执行. 
问题是, 在这个时候 `.on( 'listening' )` 的回调函数不会被调用.

<!-- To get around this, the 'listening' event is queued in a nextTick() to allow the script to run to completion. This allows the user to set any event handlers they want. -->

为了避开这个问题, `'listening'` 事件会进入 `nextTick()` 方法的队列中, 并在代码执行完毕后调用. 这样, 用户就可以绑定任意的事件监听了( 或者译为: 就可以订阅任意事件处理函数了 ).


<!-- process.nextTick() vs setImmediate() -->

## 6. `process.nextTick()` 与 `setImmediate()`

<!-- We have two calls that are similar as far as users are concerned, but their names are confusing. -->

有两个用户们比较关心的调用, 它们的名字看起来也比较迷惑.

<!-- process.nextTick() fires immediately on the same phase
setImmediate() fires on the following iteration or 'tick' of the event loop -->

- `process.nextTick()` 会在同一个阶段中触发.
- `setImmediate()` 在迭代后或事件循环的 'tick' 后触发.


<!-- In essence, the names should be swapped. process.nextTick() fires more immediately than setImmediate(), but this is an artifact of the past which is unlikely to change. Making this switch would break a large percentage of the packages on npm. Every day more new modules are being added, which means every day we wait, more potential breakages occur. While they are confusing, the names themselves won't change. -->

事实上, 它们的名字应该交换一下. `process.nextTick()` 早于 `setImmediate()` 来执行. 
但是这个历史遗留问题, 并不好改变. 如果修改了, 会破坏 npm 上绝大部分的包. 
每天都有很多的包被添加进来. 这表示, 每天都会有潜在的问题发生.
虽然这两个名字会令人迷惑, 但是明白了其执行原理后, 它们本身是不会发生改变的.


<!-- Why use process.nextTick()? -->

## 7. 为什么使用 `process.nextTick()`?

<!-- There are two main reasons: -->

有两个主要原因:

<!-- Allow users to handle errors, cleanup any then unneeded resources, or perhaps try the request again before the event loop continues.

At times it's necessary to allow a callback to run after the call stack has unwound but before the event loop continues. -->

1. 允许用户处理错误, 清除其他不需要的资源, 或者在事件循环进入下一个环节之前继续发出请求.
2. 需要在调用栈清空后, 事件循环进入下一个阶段之前触发回调.

<!-- One example is to match the user's expectations. Simple example: -->

这个案例是获得用户的期望, 简单描述如下:

```js
const server = net.createServer();
server.on( 'connection', (conn) => { } );

server.listen( 8000 );
server.on( 'listening', () => {} );
```

<!-- Say that listen() is run at the beginning of the event loop, but the listening callback is placed in a setImmediate(). Unless a hostname is passed, binding to the port will happen immediately. For the event loop to proceed, it must hit the poll phase, which means there is a non-zero chance that a connection could have been received allowing the connection event to be fired before the listening event. -->

假如 `listen()` 在事件循环开始运行, 但是监听的回调函数位于 `setImmediate()` 中. 
除非提供主机名, 否则会立即绑定到端口. 
事件循环会继续, 即它会进入到 poll 环节, 这表示有可能已经收到一个连接.
即在监听事件触发之前就可能触发连接事件.

<!-- Another example is running a function constructor that was to, say, inherit from EventEmitter and it wanted to call an event within the constructor: -->

另一个例子在一个构造函数中, 假如它继承自 `EventEmitter` 并且要在构造函数中调用一个事件:

```js
const EventEmitter = require( 'events' );
const util = require( 'util' );

function MyEmitter() {
   EventEmitter.call( this );
   this.emit( 'event' );
}

util.inherits( MyEmitter, EventEmitter );

const myEmitter = new MyEmitter();
myEmitter.on( 'event', () => {
   console.log( 'event 事件被触发' );
} );

```

<!-- You can't emit an event from the constructor immediately because the script will not have processed to the point where the user assigns a callback to that event. So, within the constructor itself, you can use process.nextTick() to set a callback to emit the event after the constructor has finished, which provides the expected results: -->

在构造函数中, 你无法立即发射事件. 因为用户提供该事件的回调的代码不会被执行.
那么, 若要在构造函数中触发事件, 可以使用 `process.nextTick()` 来设置回调,
在构造函数执行结束后发射事件. 其代码如下:

```js
const EventEmitter = require( 'events' );
const util = require( 'util' );

function MyEmitter() {
   EventEmitter.call( this );

   // 一旦事件被赋值后, 使用 nextTick 发射事件
   process.nextTick( () => {
      this.emit( 'event' );
   } );
}

util.inherits( MyEmitter, EventEmitter );

const myEmitter = new MyEmitter();

myEmitter.on( 'event', () => {
   console.log( 'event 事件被触发' );
} );

```
