# JS 引擎之事件循环




## 1. Promise 的使用注意与 async 和 await

1.1 async 与 await 就是两个语法糖

标准的 Promise 的语法形式

  function func() {
    return new Promise( ... )
  }

使用的时候使用语法

  func( ... ).then( res => {
    // ... 过一段时间会执行的代码
  } )

虽然 Promise 不再是回调地狱, 但是 Promise 依旧是 回调

使用的感觉

1. Promise 执行后悔得到一个结果 ( 即内部 resolve( res ) )
2. 在使用使用的时候 then 方法里的函数参数 就是在给用户一个入口

function get( url ) {
  return new Peomise( resolve => {
    var xhr = new XMLHttpRequest();
    xhr.open( 'GET', url );
    xhr.send();
    xhr.onreadystatechange = function () {
      if ( xhr.readyState === 4 && xhr.status === 200 ) {
        resolve( xhr.responseText );
      }
    }
  } );
}

get( 'http://.....' ).then( function ( res ) { ... } )

感觉: 请求回来, 内部就会调用 then 里面传入的这个函数, 将请求的结果作为参数传递给 这个函数

调用 Promise

1. 要执行一个异步行为
2. 拿到异步行为的结果

语法说明

1. await 必须写在函数中, 含有 await 的函数必须使用 async 修饰
2. await 后面必须跟上一个 Promise
3. await 得到的结果就好像是 Promise 中 then 的回调拿到的数据, 可以同步的返回给左边的变量了


async function func() {
  // ...
  await 一个 Promise
  // ...
}

使用 await 修饰后

async function mian() {

  let res = await get( 'http:// ....' );

}

原始的 Promise 与 async await 的语法, 逻辑是一模一样的, 只是调用形式不一样, async/await 没有了回调



async 与 await 里面的坑

let res = await fetch( 'http://127.0.0.1:8080/api/test' );
let json = await res.json();
// 后续的代码

**本质** 等价于

fetch( 'http://127.0.0.1:8080/api/test' )
  .then( function ( res ) {

    res.json().then( function ( json ) {

      // 后续的代码
    } );

  } )

如果请求时非常耗时的, 那么 在两个 await 中间会等很长的时间



需求：

1. 获得分类数据（全部）
2. 得到产品的数据（筛选）
3. 将分类数据与产品数据合并, 得到一个树结构

分类1
  产品1
  产品2
  产品3
  ...
分类2
  产品
  产品
  ...
分类3

实现逻辑: 
  let categories = await get( '请求产品的分类: 200' );
  let products = await get( '请求所有的产品: 700' );
  // 合并 categoryies 与 products

  // 用上面这个方法消耗的时间是累计

  get( '请求产品的分类: 200' ).then( categories => {
    get( '请求所有的产品: 700' ).then( products => {
      // 合并 categoryies 与 products
    } );
  } );


同时请求
  let finished1 = false, finished2 = false;
  get( '请求产品的分类: 200' ).then( res => {
    finished1 = true;
    // 结果
    // 判断 完成没有
    if ( finished1 === true && finished2 == true ) {
      // 全部完成, 可以处理了
    }
  } )

  get( '请求所有的产品: 700' ).then( res => {
    finished2 = true;
    // 结果
    // 判断 完成没有
    if ( finished1 === true && finished2 == true ) {
      // 全部完成, 可以处理了
    }
  } )
  
  // 使用这个方法时间是 取其大

  // 这个方法还有一个难点, 如果两个请求耗时非常相近 怎么办?

  Promise.all( [ 元素是 Promise ] ).then...  返回的也是 Promise 



## 2. 事件循环 ( 规则 )

  1. 线性执行
  2. 函数调用栈
  3. 事件队列

事件队列就是一个函数队列 ( 函数数组 )
每次执行 **耗时的操作** ( 其他进程处理 ) 都会提供一个回调函数, 交给其他进程
当其他进程实现完耗时操作以后 回调函数 连同处理的结果 作为参数会投递到 函数队列 中

js 引擎, 从队列中取一个函数执行,
执行完成以后 再 从队列中取一个函数执行,
直到队列为空, 那么就停止
然后如果又有人将事件投递到队列中, js 引擎又会运行起来.

通俗的比喻 js 引擎就好比一个公司的老板
老板要做事情不是自己做, 将任务分配给人员, 将这个任务会记录到工作日志中
如果有一个人把事情做完了, 走到老板身边, 如果老板现在正在处理一些事情, 怎么办?
等待, 事件的结果交给老板的秘书
如果又有一个人完成, 交给秘书( 排序, 汇报 )



在 js 中它的事件队列非常复杂 ( V8 )

  timer 队列
  pending poll 队列( 不是 **一个** 队列, 这专门处理 IO, 很多队列, 只是我们不需要考虑 )
  check 队列
  close 队列

  内部的逻辑 ( 伪代码 )

  var queue = [
    [],           // timer 队列, 专门用于存放 timeout 回调 ( web, fullstack, gost )
    [],           // 综合队列, 可以**简单**的理解为 IO 队列 ( gost )
    [],           // check 队列, 专门有从来存放 setImmediate 回调 ( web, fullstack, gost )
    []            // close 队列, 专门用来存放 close 行为 ( fullstack, gost )
  ]


  js 引擎 处理队列


  var i = 0;
  var len = queue.length;

  引擎内部的处理流程

  while ( true ) {      // 除非所有的队列清空, 否则一直执行下去
                        // 并且如果处于停止状态, 一旦有事件入队, 立即激活该循环
    while( i < len ) {
      var subqueue = queue[ i ];

      处理 子队列, 处理完该子队列

      i++
    }  
    i = 0;
  }





